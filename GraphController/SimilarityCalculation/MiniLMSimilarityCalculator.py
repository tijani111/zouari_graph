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
import logging
import os
import time
from multiprocessing import Pool, Manager

import numpy as np
import torch
from transformers import AutoTokenizer, AutoModel  # Generic Auto Classes
from scipy.spatial.distance import cosine
from tqdm import tqdm
import multiprocessing

from GraphController.SimilarityCalculation.ISimilarityCalculator import ISimilarityCalculator
from GraphModel.Graph import Graph
from multiprocessing import Pool
import threading


class MiniLMSimilarityCalculator(ISimilarityCalculator):
    """
    Class to compute similarity between node descriptions in a graph using embeddings.
    Now using all-MiniLM-L6-v2 model for embeddings.
    """
    BATCH_SIZE = 5

    def __init__(self, graph, similarity_threshold=0.0):
        """
        Initialize the class with a Graph object.
        """
        self.similarity_threshold = similarity_threshold
        self.graph = graph
        self.tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
        self.model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

    def _get_embedding(self, text):
        try:
            # Annahme: Verwendung eines Tokenizers und Modells wie z.B. von Hugging Face
            input_ids = self.tokenizer.encode(text, return_tensors='pt', truncation=True, max_length=512)

            # Berechnung der Embeddings
            with torch.no_grad():
                outputs = self.model(input_ids)
                # Extrahieren des letzten versteckten Zustands und Mittelung über die Sequenzdimension
                embedding = outputs.last_hidden_state.mean(dim=1).squeeze()

            return embedding

        except Exception as e:
            # Fehlerbehandlung
            print(f"Fehler beim Berechnen des Embeddings für den Text: '{text[:50]}...'. Fehlermeldung: {e}")
            # Rückgabe eines Null-Tensors der passenden Dimension
            return torch.zeros(self.embedding_dim)

    def _process_batch(self, batch, result_queue, progress_queue):
        embeddings = []
        uuids = []

        attribute_names = [
            'titel', 'description', 'source_author', 'year_of_publication', 'comment',
            'titel_of_the_book', 'place_of_publication', 'publisher', 'ISBN',
            'titel_of_the_website', 'URL', 'date_of_access', 'titel_of_the_article',
            'titel_of_the_journal', 'volume_and_issue'
        ]

        for node in batch:
            text_parts = []

            for attr in attribute_names:
                if hasattr(node, attr):
                    value = getattr(node, attr)
                    if value:  # Überprüfen, ob der Wert nicht leer oder None ist
                        text_parts.append(str(value))

            text = ' '.join(text_parts)

            # Berechne das Embedding für den zusammengesetzten Text
            embedding = self._get_embedding(text)
            embeddings.append(embedding.detach().numpy())
            uuids.append(node.uuid)

        # Ergebnisse an den Hauptprozess senden
        result_queue.put((embeddings, uuids))

        # Fortschrittssignal an progress_queue senden
        progress_queue.put(1)

        # Listen leeren und Speicher bereinigen
        embeddings.clear()
        uuids.clear()
        gc.collect()

    def generate_and_save_embeddings(self):
        file_path = 'node_embeddings.npz'
        if os.path.exists(file_path):
            os.remove(file_path)

        with Manager() as manager:
            result_queue = manager.Queue()
            progress_queue = manager.Queue()

            # Erstelle eine Liste aller Batches
            batches = list(self._batchify(self.graph, self.BATCH_SIZE))

            # Berechne die Gesamtzahl der Batches korrekt
            total_batches = (len(batches))

            with Pool() as pool:
                for batch in batches:
                    pool.apply_async(self._process_batch, args=(batch, result_queue, progress_queue))

                pool.close()
                pool.join()

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
                else:
                    # Kurze Pause einlegen, um CPU-Auslastung zu reduzieren
                    time.sleep(0.1)

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
        self.generate_and_save_embeddings()
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
