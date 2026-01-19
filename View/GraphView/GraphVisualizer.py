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
import hashlib
from collections import deque

import pygame

from ApplicationSettings import ApplicationSettings
from GraphController.ScaleOffSetTransformer.IScaleOffsetTransformerObserver import IScaleOffsetTransformerObserver
from GraphModel import Graph, SelectedNodeContainer
from GraphModel.Nodes import Node
from GraphController.ScaleOffSetTransformer import IScaleOffsetTransformer
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from GraphModel.Nodes.NodeSourceBook import NodeSourceBook
from GraphModel.Nodes.NodeSourceOnline import NodeSourceOnline
from GraphModel.Nodes.NodeSourcePaper import NodeSourcePaper
from View.GraphView.IGraphVisualizer import IGraphVisualizer
from View.GraphView.Legend import Legend
from View.UI.UIThemes import UITheme


class GraphVisualizer(IGraphVisualizer, IScaleOffsetTransformerObserver):
    """
    The GraphVisualizer class is responsible for rendering a graph onto a screen using Pygame.
    It manages the drawing of nodes and edges and handles the visual representation of the graph,
    including highlighting selected nodes and their subtrees.
    """

    def __init__(self, window_width, scale_offset_transformer: IScaleOffsetTransformer,
                 screen, graph: Graph, selected_node_container: SelectedNodeContainer,
                 ui_theme: UITheme, similarity_threshold, viewport, application_settings: ApplicationSettings):
        """
        Initializes the GraphVisualizer with necessary components and visual properties.

        :param: scale_offset_transformer: An instance of IScaleOffsetTransformer for coordinate scaling and transformation.
        :param: screen: The Pygame screen object where the graph will be drawn.
        :param: graph: The graph to be visualized.
        :param: selected_node_container: A container holding the currently selected node, if any.
        :param: edge_color: The color to be used for drawing graph edges.
        :param: node_color: The color to be used for drawing nodes.
        :param: selected_node_color: The color to be used for highlighting the selected node.
        :param: selected_node_subtree_color: The color to be used for highlighting the subtree of the selected node.
        :param: legend_mode_activated: Shall the Legend be displayed and shall the nodes
        be colored in the colors of the legend
        """
        self.base_node_diameter = application_settings.base_node_diameter
        self.base_node_highlight_diameter = application_settings.base_node_highlight_diameter
        self.selected_node_special_highlight_diameter = application_settings.selected_node_special_highlight_diameter
        self.show_node_labels = True


        self.window_width = window_width
        self.ui_theme = ui_theme
        self.viewport = viewport
        self.similarity_threshold = similarity_threshold
        self.scaleOffsetTransformer = scale_offset_transformer
        self.graph = graph
        self.set_node_color_based_on_type()
        self.selectedNodeContainer = selected_node_container
        self.screen = screen

        self.edge_color = self.ui_theme.EDGE_COLOR
        self.node_color = self.ui_theme.NODE_COLOR

        self.selected_node_color = self.ui_theme.SELECTED_NODE_COLOR
        self.selected_node_subtree_color = self.ui_theme.SELECTED_NODE_SUBTREE_COLOR
        pygame.font.init()  # Initialisieren Sie das Schriftart-System
        self.font = pygame.font.Font(None, 16)  # Wählen Sie eine Schriftart und Größe
        self.similarity_edges_rendering = False
        self.connection_edges_rendering = False
        self.visible_nodes_cache = set()
        self._update_visible_nodes_cache()
        self.author_color_cache = {}
        self.legend_mode_activated = application_settings.team_legend_activated
        self.legend = Legend(self.screen, self.font, self.ui_theme,
                             (window_width - 200 - 10, 10), 200, 300, 20, self.selected_node_color)

        self.highlighted_author = ""
        self.highlight_author = False

    def set_node_color_based_on_type(self):
        for node in self.graph.nodes:
            if type(node) == NodeKnowledge:
                node.color = self.ui_theme.NODE_COLOR
            elif type(node) == NodeSourceBook:
                node.color = self.ui_theme.NODE_SOURCE_BOOK
            elif type(node) == NodeSourcePaper:
                node.color = self.ui_theme.NODE_SOURCE_PAPER
            elif type(node) == NodeSourceOnline:
                node.color = self.ui_theme.NODE_SOURCE_ONLINE
            elif type(node) == NodeIllustration:
                node.color = self.ui_theme.NODE_ILLUSTRATION
            else:
                node.color = self.ui_theme.NODE_COLOR



    def handle_legend_click(self, position):
        mouse_x, mouse_y = position
        if self.legend.legend_surface_rect.collidepoint(mouse_x, mouse_y):
            for (x1, y1, x2, y2), author in self.legend.legend_entries.items():
                if x1 <= mouse_x <= x2 and y1 <= mouse_y <= y2:
                    # Klick innerhalb eines Legenden-Eintrags erkannt
                    self.highlight_nodes_by_author(author)
                    break
        else:
            self.disable_highlight_nodes_by_author()

    def highlight_nodes_by_author(self, author):
        self.highlight_author = True
        self.highlighted_author = author

    def disable_highlight_nodes_by_author(self):
        self.highlight_author = False

    def draw_legend(self):
        self.legend.draw()

    def _update_visible_nodes_cache(self):
        self.visible_nodes_cache.clear()
        for node in self.graph.nodes:
            if self.viewport.contains(node):
                self.visible_nodes_cache.add(node)

    def notify(self):
        self._update_visible_nodes_cache()

    def draw_text(self, text, position):
        """
        Zeichnet Text an einer bestimmten Position auf dem Bildschirm.

        :param: text: Der zu zeichnende Text.
        :param: position: Eine Tupel-Position (x, y), an der der Text gezeichnet wird.
        """
        text_surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, position)

    def draw_graph(self):
        """
        Renders the graph on the screen, drawing both nodes and edges.
        This method also handles the highlighting of the selected node and its subtree if applicable.
        """
        # Zeichnen der Ähnlichkeits-basierten Kanten
        if self.scaleOffsetTransformer.zoom > 0.05:
            self.draw_similarity_edges()

        if self.scaleOffsetTransformer.zoom > 0.05:
            self.draw_connection_edges()

        if self.selectedNodeContainer.selected_node is not None and self.connection_edges_rendering:
            self.highlight_selected_subtree(self.selectedNodeContainer.selected_node)

        elif not self.connection_edges_rendering:
            self.highlight_selected_node(self.selectedNodeContainer.selected_node)

        self.draw_all_visible_nodes()

        
    def draw_all_visible_nodes(self):
        if self.legend_mode_activated:
            self.draw_nodes_with_legend()
            self.draw_legend()
        else:
            self.draw_nodes_without_legend()

    def draw_nodes_with_legend(self):
        # Zeichne Knoten
        for node in self.visible_nodes_cache:
            if self.highlight_author and node.author == self.highlighted_author:
                self.highlight_selected_node(node)

            # Überprüfe, ob die Farbe für diesen 'author' bereits berechnet wurde
            if node.author not in self.author_color_cache:
                color = self.string_to_color_sha1(node.author)
                self.author_color_cache[node.author] = color
                self.legend.update_author_color_cache(node.author, color)

            self.node_color = self.author_color_cache[node.author]

            self.draw_single_node(node)

    def draw_nodes_without_legend(self):
        # Zeichne Knoten
        for node in self.visible_nodes_cache:
            self.draw_single_node(node)


    def draw_single_node(self, node):
        scaled_x, scaled_y = self.scaleOffsetTransformer.get_scaled_coordinates(node)
        pygame.draw.circle(self.screen, node.color, (scaled_x, scaled_y), self.base_node_diameter)

        if self.show_node_labels and self.scaleOffsetTransformer.zoom > 2.00:
            self.draw_text(node.titel, (scaled_x, scaled_y + self.base_node_diameter + 5))


    def string_to_color_sha1(self, input_string):
        # SHA-1 Hash des Strings erzeugen
        hash_object = hashlib.sha1(input_string.encode())
        hash_string = hash_object.hexdigest()

        # Die ersten 6 Hex-Zeichen als Farbe verwenden
        red = int(hash_string[0:2], 16)
        green = int(hash_string[2:4], 16)
        blue = int(hash_string[4:6], 16)

        # Die Farbe als RGB-Tupel zurückgeben
        return red, green, blue

    def highlight_selected_subtree(self, node: Node):
        """
        Highlights the subtree rooted at a specified node. This method visually differentiates
        the selected node and its connected nodes from the rest of the graph.

        :param: node: The root node of the subtree to be highlighted.
        """
        if node is None:
            return

        stack = deque()
        stack.append(node)

        visited_nodes = set()

        while stack:
            current_node = stack.pop()
            if current_node == self.selectedNodeContainer.selected_node:
                scaled_start = self.scaleOffsetTransformer.get_scaled_coordinates(current_node)
                pygame.draw.circle(self.screen, self.selected_node_color, scaled_start,
                                   self.selected_node_special_highlight_diameter)
            else:
                scaled_start = self.scaleOffsetTransformer.get_scaled_coordinates(current_node)
                pygame.draw.circle(self.screen, self.selected_node_color, scaled_start,
                                   self.base_node_highlight_diameter)

            visited_nodes.add(current_node)

            for connected_node in current_node.get_connected_nodes().values():
                scaled_end = self.scaleOffsetTransformer.get_scaled_coordinates(connected_node)
                pygame.draw.aaline(self.screen, self.selected_node_subtree_color, scaled_start, scaled_end)

                if connected_node not in visited_nodes:
                    stack.append(connected_node)

    def highlight_selected_node(self, node: Node):
        """
        Highlights a single node. This method visually differentiates the specified node from the rest of the graph.

        :param: node: The node to be highlighted.
        """

        if node is None:
            return

        # Get the scaled coordinates of the node for proper positioning on the screen
        scaled_coordinates = self.scaleOffsetTransformer.get_scaled_coordinates(node)

        # Draw a circle at the node's location to highlight it
        pygame.draw.circle(self.screen, self.selected_node_color, scaled_coordinates,
                           self.selected_node_special_highlight_diameter)

    def toggle_node_labels(self):
        """
        Toggles the display of the Node Labels.
        """
        self.show_node_labels = not self.show_node_labels

    def set_similarity_edges_rendering(self, active: bool):
        self.similarity_edges_rendering = active

    def get_similarity_edges_rendering_state(self):
        return self.similarity_edges_rendering

    def set_connection_edges_rendering(self, active: bool):
        self.connection_edges_rendering = active

    def get_connection_edges_rendering_state(self):
        return self.connection_edges_rendering

    def draw_similarity_edges(self):
        """
        Zeichnet Kanten basierend auf der Ähnlichkeit der Node-Beschreibungen.
        Die Farbe der Kanten variiert von Blau (niedrige Ähnlichkeit) zu Rot (hohe Ähnlichkeit).
        """
        if self.graph.similarity_dict and self.similarity_edges_rendering:
            similarity_threshold = self.similarity_threshold

            # for node in self.visible_nodes_cache:
            for node in self.graph.nodes:
                scaled_start = self.scaleOffsetTransformer.get_scaled_coordinates(node)
                node_similarity = self.graph.get_similarity(node.uuid)
                for other_node_uuid, similarity in node_similarity.items():
                    if similarity >= similarity_threshold:
                        other_node = next((n for n in self.graph.nodes if n.uuid == other_node_uuid), None)
                        if other_node:
                            scaled_end = self.scaleOffsetTransformer.get_scaled_coordinates(other_node)

                            # Farbinterpolation zwischen Blau bei Threshold und Rot (bei 1.0)
                            if similarity < similarity_threshold:
                                interpolated_color = (0, 0, 255)  # Vollständig Blau
                            else:
                                scaled_similarity = (similarity - similarity_threshold) / (1 - similarity_threshold)
                                red_value = int(scaled_similarity * 255)
                                green_value = 150
                                blue_value = int((1 - scaled_similarity) * 255)
                                interpolated_color = (red_value, green_value, blue_value)

                            # Zeichne die Kante, wenn mindestens einer der Knoten im Viewport liegt
                            # if self.viewport.contains(node) or self.viewport.contains(other_node):
                            pygame.draw.aaline(self.screen, interpolated_color, scaled_start, scaled_end)

    def draw_connection_edges(self):
        # Zeichne Kanten
        if self.connection_edges_rendering:
            # for node in self.visible_nodes_cache:
            for node in self.graph.nodes:
                scaled_start = self.scaleOffsetTransformer.get_scaled_coordinates(node)
                for connected_node in node.get_connected_nodes().values():
                    scaled_end = self.scaleOffsetTransformer.get_scaled_coordinates(connected_node)
                    # Zeichne die Kante, wenn mindestens einer der Knoten im Viewport liegt
                    # if self.viewport.contains(node) or self.viewport.contains(connected_node):
                    pygame.draw.aaline(self.screen, self.edge_color, scaled_start, scaled_end)
