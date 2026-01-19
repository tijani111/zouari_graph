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
import re
import zipfile
from PyQt5.QtWidgets import QApplication, QFileDialog
from GraphModel import Graph
from GraphModel.Nodes.Node import Node
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from GraphModel.Nodes.NodeSource import NodeSource
from GraphModel.Nodes.NodeSourceBook import NodeSourceBook
from GraphModel.Nodes.NodeSourceOnline import NodeSourceOnline
from GraphModel.Nodes.NodeSourcePaper import NodeSourcePaper


class GraphExporter:
    """
    The GraphExporter class is responsible for exporting the data of a graph into different formats.
    This includes gathering all relevant information from the Graph object, such as node details and
    connections, and then saving this data into a file. The class supports exporting to various formats,
    including JSON and ZIP, allowing for easy sharing and storage of graph data. It also handles
    the inclusion of associated image files in the export, ensuring a complete representation of the graph.
    """



    def __init__(self, graph: Graph, resources_folder_path):
        """
        Initializes the GraphExporter with a specific graph and a path to the resources folder.
        """
        self.graph = graph
        self.image_folder_path = os.path.join(resources_folder_path, "Images")

    def export_graph(self):
        """
        Exports the graph data to a ZIP file.
        """
        app = QApplication([])  # Initialize the PyQt application
        graph_data, images_to_export = self.prepare_graph_data()

        file_path, _ = QFileDialog.getSaveFileName(
            caption="Export Graph",
            filter="ZIP files (*.zip)"
        )

        if file_path:
            if not file_path.endswith('.zip'):
                file_path += '.zip'
            self.export_to_zip(graph_data, images_to_export, file_path)

        app.exit()  # Close the PyQt application

    def prepare_graph_data(self):
        """
        Prepares the graph data for export, including nodes and their similarities.
        """
        graph_data = {
            "team_name": self.graph.team_name,
            "nodes": [],
            "similarities": {
                str(key): {str(inner_key): val for inner_key, val in value.items()}
                for key, value in self.graph.similarity_dict.items()
            }
        }
        images_to_export = {}

        for node in self.graph.nodes:
            node_data = self.get_node_data(node)
            graph_data["nodes"].append(node_data)

            if isinstance(node, NodeIllustration):
                # Sanitize author and image name to avoid invalid filename characters
                sanitized_author = self.sanitize_filename(node.author)
                sanitized_image_name = self.sanitize_filename(node.image_name)

                # Concatenate node.author with the image name to prevent collisions
                new_image_name = f"{sanitized_author}_{sanitized_image_name}"
                node_data["image_name"] = new_image_name

                # Add to images to export if not already added
                if node.image_name not in images_to_export:
                    images_to_export[node.image_name] = new_image_name

        return graph_data, images_to_export

    def get_node_data(self, node):
        """
        Returns a dictionary representation of the node based on its class type.
        """
        base_data = {
            "uuid": str(node.uuid),
            "titel": node.titel,
            "x": node.x,
            "y": node.y,
            "author": node.author,
            "type": node.__class__.__name__,  # Store the class name
            "connected_nodes": [str(uuid) for uuid in node.get_connected_nodes()]
        }
        # Check the entire inheritance hierarchy
        if isinstance(node, Node):
            base_data["color"] = node.color
        if isinstance(node, NodeIllustration):
            base_data["image_name"] = node.image_name  # Will be updated later in prepare_graph_data
        if isinstance(node, NodeKnowledge):
            base_data["description"] = node.description
        if isinstance(node, NodeSource):
            base_data.update({
                "source_author": node.source_author,
                "year_of_publication": node.year_of_publication,
                "comment": node.comment
            })
            if isinstance(node, NodeSourceBook):
                base_data.update({
                    "titel_of_the_book": node.titel_of_the_book,
                    "edition": node.edition,
                    "place_of_publication": node.place_of_publication,
                    "publisher": node.publisher,
                    "ISBN": node.ISBN
                })
            elif isinstance(node, NodeSourceOnline):
                base_data.update({
                    "titel_of_the_document": node.titel_of_the_document,
                    "titel_of_the_website": node.titel_of_the_website,
                    "URL": node.URL,
                    "date_of_access": node.date_of_access
                })
            elif isinstance(node, NodeSourcePaper):
                base_data.update({
                    "titel_of_the_article": node.titel_of_the_article,
                    "titel_of_the_journal": node.titel_of_the_journal,
                    "volume_and_issue": node.volume_and_issue
                })
        return base_data

    def export_to_zip(self, graph_data, images_to_export, file_path):
        """
        Exports the graph data to a ZIP file, including the images with updated names.
        """
        with zipfile.ZipFile(file_path, 'w') as zipf:
            json_filename = os.path.basename(file_path).replace('.zip', '.json')
            with zipf.open(json_filename, 'w') as file:
                json_data = json.dumps(graph_data).encode('utf-8')
                file.write(json_data)

            for original_image_name, new_image_name in images_to_export.items():
                original_image_path = os.path.join(self.image_folder_path, original_image_name)
                if os.path.exists(original_image_path):
                    # Add the renamed image file to the ZIP
                    with zipf.open(new_image_name, 'w') as img_file, open(original_image_path, 'rb') as image:
                        img_file.write(image.read())
                else:
                    print(f"Image file {original_image_name} not found.")

    @staticmethod
    def sanitize_filename(filename):
        """
        Sanitizes a string to be used as a valid filename by removing or replacing invalid characters.
        """
        return re.sub(r'[^A-Za-z0-9_.-]', '_', filename)

