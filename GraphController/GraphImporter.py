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

import json
import os
import uuid
import zipfile
from PyQt5.QtWidgets import QApplication, QFileDialog
from ComponentAssembly.GraphAnalyzer import GraphAnalyzer
from GraphModel.Graph import Graph
from GraphModel.Nodes.Node import Node
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from GraphModel.Nodes.NodeSourceBook import NodeSourceBook
from GraphModel.Nodes.NodeSourceOnline import NodeSourceOnline
from GraphModel.Nodes.NodeSourcePaper import NodeSourcePaper


class GraphImporter:
    """
    The GraphImporter class is responsible for importing graph data from external sources into the application.
    It supports importing graph data, including node details and connections, from ZIP files, which may also
    contain related image files. The class handles the extraction and processing of this data, converting it
    into a usable graph structure within the application. It integrates closely with GraphAnalyzer for post-import
    analysis and verification of the graph structure.
    """

    def __init__(self, graph: Graph, resources_folder_path, graph_analyzer: GraphAnalyzer):
        """
        Initializes the GraphImporter.
        """
        self.graph = graph
        self.image_folder_path = os.path.join(resources_folder_path, "Images")
        self.graph_analyzer = graph_analyzer

    def import_graph(self, add_to_existing_graph: bool = False):
        """
        Imports graph data from a selected ZIP file.

        :param add_to_existing_graph: Add the imported graph to the current graph
        """

        if not add_to_existing_graph:
            self.graph.clear()
        else:
            self.graph.similarity_dict.clear()
        app = QApplication([])
        zip_file_paths, _ = QFileDialog.getOpenFileNames(filter="ZIP files (*.zip)")
        for zip_file_path in zip_file_paths:
            if zip_file_path:
                with zipfile.ZipFile(zip_file_path, 'r') as zipf:
                    self.extract_images(zipf)
                    json_file_name = os.path.basename(zip_file_path).replace('.zip', '.json')

                    if json_file_name in zipf.namelist():
                        with zipf.open(json_file_name) as file:
                            graph_json_data = json.load(file)
                        self.create_graph_from_json(graph_json_data, self.graph)

        app.exit()

    def extract_images(self, zipf):
        """
        Extracts images from the ZIP file into the images folder.

        :param zipf: The opened ZIP file object from which images are to be extracted.
        """
        os.makedirs(self.image_folder_path, exist_ok=True)
        for file in zipf.namelist():
            if file.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_path = os.path.join(self.image_folder_path, file)
                if not os.path.exists(image_path):
                    with zipf.open(file) as source, open(image_path, 'wb') as target:
                        target.write(source.read())
                else:
                    print(f"Image file {file} already exists. Skipping extraction.")

    def create_graph_from_json(self, graph_json_data, graph):
        """
        Creates a graph from JSON data.
        """
        self.check_and_update_uuids(graph_json_data, graph)
        team_name = graph_json_data.get("team_name", "Standard Team Name")
        graph.team_name = team_name
        nodes = {}

        for node_data in graph_json_data["nodes"]:
            node_type = node_data.get("type", "Node")
            node = self.create_node_from_data(node_data, node_type)
            nodes[node.uuid] = node
            graph.add_new_node_to_graph(node)

        for node_data in graph_json_data["nodes"]:
            for connected_uuid in node_data["connected_nodes"]:
                if connected_uuid in nodes:
                    nodes[node_data["uuid"]].connect(nodes[connected_uuid])

        graph.similarity_dict = graph_json_data.get("similarities", {})
        self.graph_analyzer.display_statistics(graph)

    def create_node_from_data(self, node_data, node_type):
        """
        Creates a node from the provided data and type.
        """
        if node_type == "NodeIllustration":
            image_name = node_data.get("image_name", "")
            node = NodeIllustration(node_data["titel"], image_name, node_data["x"], node_data["y"])
        elif node_type == "NodeKnowledge":
            node = NodeKnowledge(node_data["description"], node_data["titel"], node_data["x"], node_data["y"])
        elif node_type == "NodeSourceBook":
            node = NodeSourceBook(
                node_data["titel_of_the_book"],
                node_data["source_author"],
                node_data["year_of_publication"],
                node_data["place_of_publication"],
                node_data["publisher"],
                node_data["ISBN"],
                node_data["comment"],
                node_data.get("edition", "1st edition"),
                node_data["x"],
                node_data["y"]
            )
        elif node_type == "NodeSourceOnline":
            node = NodeSourceOnline(
                node_data["titel_of_the_document"],
                node_data["source_author"],
                node_data["year_of_publication"],
                node_data["titel_of_the_website"],
                node_data["URL"],
                node_data["date_of_access"],
                node_data["comment"],
                node_data["x"],
                node_data["y"]
            )
        elif node_type == "NodeSourcePaper":
            node = NodeSourcePaper(
                node_data["titel_of_the_article"],
                node_data["source_author"],
                node_data["year_of_publication"],
                node_data["titel_of_the_journal"],
                node_data["volume_and_issue"],
                node_data["comment"],
                node_data["x"],
                node_data["y"]
            )
        else:
            node = Node(node_data["titel"], node_data["x"], node_data["y"])

        node.uuid = node_data["uuid"]
        node.team = self.graph.team_name
        node.author = node_data.get("author", self.graph.team_name)
        return node

    def check_and_update_uuids(self, graph_json_data, graph):
        """
        Checks if UUIDs in graph_json_data already exist in the graph.
        Replaces conflicting UUIDs in graph_json_data to ensure uniqueness.

        :param graph_json_data: The data of the graph to be imported.
        :param graph: The graph object into which data is being imported.
        """
        uuids_to_replace = {}
        existing_uuids = set(graph.nodes_dict.keys())

        # Detect collisions
        for node_data in graph_json_data["nodes"]:
            node_uuid = node_data["uuid"]
            if node_uuid in existing_uuids or node_uuid in uuids_to_replace:
                # Generate a new UUID and store in mapping
                new_uuid = str(uuid.uuid4())
                uuids_to_replace[node_uuid] = new_uuid

        # Update UUIDs in node data
        if uuids_to_replace:
            for node_data in graph_json_data["nodes"]:
                old_uuid = node_data["uuid"]
                if old_uuid in uuids_to_replace:
                    node_data["uuid"] = uuids_to_replace[old_uuid]

                # Update connected nodes UUIDs
                node_data["connected_nodes"] = [
                    uuids_to_replace.get(uuid_str, uuid_str)
                    for uuid_str in node_data["connected_nodes"]
                ]

            # Recursively check again in case of new collisions
            self.check_and_update_uuids(graph_json_data, graph)