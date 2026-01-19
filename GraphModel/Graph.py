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
import math
import random

from GraphModel.Nodes.Node import Node


class Graph:
    """
    The Graph class represents a graph structure consisting of nodes.
    It provides functionality to manage and manipulate a collection of nodes,
    including adding new nodes and defining their initial positions.
    This class serves as the core data structure.
    """
    # Default team name associated with the graph
    team_name = "Die mutigen Mungos"
    # Initial central position for new nodes
    INITIAL_CENTER_POSITION = 5000000
    MIN_RADIUS = 300
    # List to store all nodes in the graph
    nodes = []
    nodes_dict = {}
    similarity_dict = {}

    def __init__(self):
        self.author_angle_dict = {}
        self.max_authors = 14

    def add_new_node_to_graph(self, node: Node):
        """
        Adds a new Node to the graph. This method calculates a random position for the node
        near the center of the graph's defined initial central position.

        :param: node: An instance of Node to be added to the graph.
        """
        # Bestimme den Winkelabstand zwischen den Autoren
        angle_increment = 360 / self.max_authors

        # Weise dem Autor einen Winkel zu, falls noch nicht geschehen
        if node.author not in self.author_angle_dict:
            # Der Winkel basiert auf der Anzahl der bereits zugewiesenen Autoren
            assigned_angles = len(self.author_angle_dict)
            self.author_angle_dict[node.author] = assigned_angles * angle_increment

        # Hole den Winkel für diesen Autor
        node_angle = self.author_angle_dict[node.author]

        # Konvertiere Winkel zu Radianten
        angle_rad = math.radians(node_angle)

        # Zufällige Abweichung im Bereich
        offset_x = random.uniform(-10, 10)
        offset_y = random.uniform(-10, 10)

        # Berechne die Position
        node.x = self.INITIAL_CENTER_POSITION + self.MIN_RADIUS * math.cos(angle_rad) + offset_x
        node.y = self.INITIAL_CENTER_POSITION + self.MIN_RADIUS * math.sin(angle_rad) + offset_y

        self.nodes.append(node)
        self.nodes_dict[node.uuid] = node

    def clear(self):
        self.nodes.clear()
        self.nodes_dict.clear()
        self.similarity_dict.clear()

    def get_similarity(self, node_uuid):
        """
        Get similarity dictionary for a specific node.
        """
        return self.similarity_dict.get(node_uuid, {})
