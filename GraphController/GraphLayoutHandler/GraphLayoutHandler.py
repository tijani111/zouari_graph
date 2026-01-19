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

import pygame

from ApplicationSettings import ApplicationSettings
from GraphModel import Graph
from ..ScaleOffSetTransformer import IScaleOffsetTransformer
from .BarnesHutManager import BarnesHutManager
from .IGraphLayoutHandler import IGraphLayoutHandler
from .QuadtreeBuilder import BarnesHutNode


class AutoLayoutHandler(IGraphLayoutHandler):
    """
    AutoLayoutHandler is a class that implements automatic graph layout using the Barnes-Hut optimization algorithm.
    This class is responsible for positioning the nodes in a graph efficiently, aiming to make the graph
    easy to understand and visually appealing. It uses the Barnes-Hut algorithm to approximate the forces
    between nodes in large graphs, which helps in significantly speeding up the layout calculation.
    """
    barnesHutManager = None
    scaleOffsetTransformer: IScaleOffsetTransformer
    screen = None
    draw_color = (0, 0, 0)
    graph: Graph

    def __init__(self,
                 x_location,
                 y_location,
                 barnes_hut_size,
                 scale_offset_transformer: IScaleOffsetTransformer,
                 screen,
                 draw_color,
                 graph: Graph,
                 similarity_threshold,
                 application_settings: ApplicationSettings):
        """
        Initializes an AutoLayoutHandler instance.

        :param: x_location: The x-coordinate for the Barnes-Hut quadtree root.
        :param: y_location: The y-coordinate for the Barnes-Hut quadtree root.
        :param: barnes_hut_size: The size of the Barnes-Hut quadtree area.
        :param: scale_offset_transformer: An instance of IScaleOffsetTransformer for transforming coordinates.
        :param: screen: The Pygame screen object where the graph is rendered.
        :param: draw_color: The color used for drawing the Barnes-Hut area.
        :param: graph: The graph whose nodes will be arranged.
        """
        self.convergence_steps = 0
        self.convergence_steps_counter = 0
        self.max_velocity = 0
        self.repulsion_force_modification = 0

        self.base_convergence_steps = application_settings.base_convergence_steps
        self.base_max_velocity = application_settings.base_max_velocity
        self.base_repulsion_force_modification = application_settings.base_repulsion_force_modification
        self.base_attraction_force_modification = application_settings.base_attraction_force_modification
        self.minimum_convergence_factor = application_settings.minimum_convergence_factor

        self.calculate_similarity_based_attraction_force = False
        self.calculate_connection_based_attraction_force = False
        self.similarity_threshold = similarity_threshold

        self.graph = graph
        self.barnesHutManager = BarnesHutManager(x_location, y_location, barnes_hut_size)
        self.barnesHutManager.insert_nodes_into_quadtree(self.graph)
        self.scaleOffsetTransformer = scale_offset_transformer
        self.screen = screen
        self.draw_color = draw_color

        # Modifications for Auto Layout
        self.reset_force_convergence()

    def set_similarity_based_attraction_force(self, active: bool):
        self.calculate_similarity_based_attraction_force = active

    def set_connection_based_attraction_force(self, active: bool):
        self.calculate_connection_based_attraction_force = active

    def get_similarity_based_force_calculation_state(self):
        return self.calculate_similarity_based_attraction_force

    def get_connection_based_force_calculation_state(self):
        return self.calculate_connection_based_attraction_force

    def auto_layout(self, pause_layout):
        """
        Performs automatic layout for graphs.

        :param: pause_layout (bool): A flag indicating whether layout should be paused.

        If `pause_layout` is False, this method performs automatic layout for the graph.
        It involves various calculations for arranging nodes and edges.
        The method also measures execution time and prints it to the console.

        """
        # GraphLayoutHandler on loop
        if pause_layout:
            self.reset_force_convergence()

        if not pause_layout:
            if self.max_velocity > 0:
                self.converge_force()

            self.run_barnes_hut_layout()

    def converge_force(self):
        """
        Reduces the force modifiers as well as the maximum acceleration
        to gradually approximate an optimal graph layout.
        """
        # Define a small base value to prevent the convergence factor from reaching zero
        base_value = self.minimum_convergence_factor # This is the minimal value it will approach, adjust as needed

        # Kontrollieren Sie, wann die Dämpfung stärker wird, indem Sie die Logarithmusbasis ändern
        # oder einen zusätzlichen Skalierungsfaktor verwenden
        early_damping_scale = 10  # Ein größerer Wert führt zu einer schnelleren anfänglichen Dämpfung

        if self.convergence_steps_counter >= self.convergence_steps:
            convergence_factor = base_value
        else:
            # Verwenden Sie eine stärkere anfängliche Dämpfung
            scale = early_damping_scale * self.convergence_steps_counter + 1  # Skalieren Sie den Zähler
            damping_factor = math.log(scale) / math.log(early_damping_scale * self.convergence_steps + 1)
            convergence_factor = base_value + (1 - base_value) * (1 - damping_factor)


        # Berechnet einen Faktor, der sich gegen Ende der Konvergenzperiode ändert
        #convergence_factor = base_value + (1 - base_value) * math.exp(
            #-self.convergence_steps_counter / self.convergence_steps)

        # Aktualisieren Sie die Werte unter Verwendung des Konvergenzfaktors
        self.attraction_force_modification = self.base_attraction_force_modification * convergence_factor
        self.repulsion_force_modification = self.base_repulsion_force_modification * convergence_factor
        self.max_velocity = self.base_max_velocity * convergence_factor
        self.convergence_steps_counter += 1

    def reset_force_convergence(self):
        """
        Resets force and velocity modifiers.
        """
        self.convergence_steps = self.base_convergence_steps
        self.attraction_force_modification = self.base_attraction_force_modification
        self.repulsion_force_modification = self.base_repulsion_force_modification
        self.max_velocity = self.base_max_velocity
        self.convergence_steps_counter = 0

    def run_barnes_hut_layout(self):
        # Hier wird die barnes_hut_layout Methode aufgerufen
        self.barnesHutManager.barnes_hut_layout(
            self.graph, self.attraction_force_modification,
            self.repulsion_force_modification, 3.0, self.max_velocity,
            self.calculate_connection_based_attraction_force,
            self.calculate_similarity_based_attraction_force,
            0.1, self.similarity_threshold
        )

    def show_barnes_hut_area(self):
        """
        Request a visualisation of the Barnes Hut Areas.
        """
        bhn = self.barnesHutManager.root_node
        self.__visualize_barnes_hut_area(bhn)

    def __visualize_barnes_hut_area(self, bhn: BarnesHutNode):
        """
        Recursively draw the Barnes-Hut tree areas.

        :param: bhn: The Barnes-Hut node to draw.
        """
        # Get scaled coordinates and size based on the zoom level.
        scaled_x, scaled_y = self.scaleOffsetTransformer.get_scaled_coordinates(bhn)
        scaled_size = int(bhn.size * self.scaleOffsetTransformer.zoom)

        # Draw the current node as a square.
        rect = pygame.Rect(scaled_x - scaled_size, scaled_y - scaled_size, 2 * scaled_size, 2 * scaled_size)
        pygame.draw.rect(self.screen, self.draw_color, rect, 1)

        # Draw straight lines from the x and total_height positions
        # to the edges of the quadrant based on 'size'.
        pygame.draw.line(self.screen, self.draw_color, (scaled_x, scaled_y - scaled_size),
                         (scaled_x, scaled_y + scaled_size))
        pygame.draw.line(self.screen, self.draw_color, (scaled_x - scaled_size, scaled_y),
                         (scaled_x + scaled_size, scaled_y))

        # Draw the children, if they exist.
        for child in bhn.children:
            if child is not None:
                self.__visualize_barnes_hut_area(child)
