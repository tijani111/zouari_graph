"""
Copyright (C) 2023 TH Köln – University of Applied Sciences

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
import gc
import os

import numpy as np
import torch
# from transformers import BertTokenizer, BertModel  # BERT Classic
from transformers import RobertaTokenizer, RobertaModel  # Roberta
from scipy.spatial.distance import cosine
from tqdm import tqdm
import multiprocessing

from GraphController.SimilarityCalculation.ISimilarityCalculator import ISimilarityCalculator
from GraphModel.Graph import Graph
from multiprocessing import Pool
import threading


class BERTSimilarityCalculator(ISimilarityCalculator):
    """
    Class to compute similarity between node descriptions in a graph using BERT embeddings.
    """
    BATCH_SIZE = 5

    def __init__(self, graph, similarity_threshold=0.0):
        """
        Initialize the class with a Graph object.
        """
        self.similarity_threshold = similarity_threshold
        self.graph = graph
        # self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')  # BERT Classic
        # self.model = BertModel.from_pretrained('bert-base-uncased')  # BERT Classic
        self.tokenizer = RobertaTokenizer.from_pretrained('roberta-base')  # Roberta
        self.model = RobertaModel.from_pretrained('roberta-base')  # Roberta

    def _get_bert_embedding(self, text):
        """
        Generate BERT embedding for a given text.
        """
        inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=512)
        outputs = self.model(**inputs)
        return torch.mean(outputs.last_hidden_state, dim=1).squeeze()

    def _process_batch(self, batch, result_queue, progress_queue):
        embeddings = []
        uuids = []
        for node in batch:
            embedding = self._get_bert_embedding(node.titel + node.description)
            embeddings.append(embedding.detach().numpy())
            uuids.append(node.uuid)

        # Send result to main process
        result_queue.put((embeddings, uuids))

        # Clear lists and collect garbage
        embeddings = []
        uuids = []
        gc.collect()

        # Update progress
        progress_queue.put(1)

    def _generate_and_save_embeddings(self):
        file_path = 'node_embeddings.npz'
        if os.path.exists(file_path):
            os.remove(file_path)

        with multiprocessing.Manager() as manager:
            result_queue = manager.Queue()
            progress_queue = manager.Queue()

            with Pool() as pool:
                for batch in self._batchify(self.graph, self.BATCH_SIZE):
                    pool.apply_async(self._process_batch, args=(batch, result_queue, progress_queue))

                pool.close()
                pool.join()

            total_batches = len(self.graph.nodes) // self.BATCH_SIZE + (1 if len(self.graph.nodes) % self.BATCH_SIZE > 0 else 0)
            progress_bar = tqdm(total=total_batches, desc="Processing Batches")

            processed_batches = 0
            while processed_batches < total_batches:
                if not progress_queue.empty():
                    progress_queue.get()
                    processed_batches += 1
                    progress_bar.update(1)
                    while not result_queue.empty():
                        embeddings, uuids = result_queue.get()
                        self._add_embeddings_to_file(embeddings, uuids, file_path)

            progress_bar.close()

    def _add_embeddings_to_file(self, embeddings, uuids, file_path):
        # Load existing data if file exists
        if os.path.exists(file_path):
            data = np.load(file_path, allow_pickle=True)
            existing_embeddings = data['embeddings'].tolist()
            existing_uuids = data['uuids'].tolist()
            embeddings = existing_embeddings + embeddings
            uuids = existing_uuids + uuids

        # Save updated data
        np.savez(file_path, embeddings=np.array(embeddings), uuids=uuids)

    def start_similarity_computation(self):
        """
        Starts similarity calculation in a new thread.
        """
        computation_thread = threading.Thread(target=self._compute_similarities)
        computation_thread.start()

    def _compute_similarities(self):
        """
        Compute similarities between all node descriptions in the graph, using saved embeddings.
        """
        self._generate_and_save_embeddings()
        # Laden der Embeddings und UUIDs aus der .npz-Datei
        data = np.load('node_embeddings.npz', allow_pickle=True)
        embeddings = data['embeddings']
        uuids = data['uuids']

        # Zuordnung von Embeddings zu UUIDs
        embeddings_dict = dict(zip(uuids, embeddings))

        # Compute similarity between each pair of nodes
        for i in tqdm(range(len(uuids)), desc="Computing Similarities"):
            node_id = uuids[i]
            embedding = embeddings_dict[node_id]
            self.graph.similarity_dict[node_id] = {}

            for j in range(len(uuids)):
                if i != j:
                    other_node_id = uuids[j]
                    other_embedding = embeddings_dict[other_node_id]
                    similarity = 1 - cosine(embedding, other_embedding)
                    if similarity >= self.similarity_threshold:
                        self.graph.similarity_dict[node_id][other_node_id] = similarity

    def _batchify(self, graph: Graph, batch_size):
        """
        Split Nodes into Batches.

        :param: graph: Graph containing all Nodes
        :param: batch_size: The amount of Nodes in a single batch

        """
        for i in range(0, len(graph.nodes), batch_size):
            yield graph.nodes[i:i + batch_size]
