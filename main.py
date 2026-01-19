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

import pygame.freetype
import sys

from Structured_Main_Knowledge_Graph.StructuredMainGraph import StructuredMainGraph

from View.ApplicationLoopManager import ApplicationLoopManager
from ComponentAssembly.ComponentAssembler import ComponentAssembler
from GraphModel.Graph import Graph


if __name__ == '__main__':
    # Initialisierung von pygame
    pygame.init()

    # WIDTH, HEIGHT = 1000, 800
    WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
    window_width, window_height = WIDTH - 10, HEIGHT - 50
    # screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("EPI Knowledge Graph")

    # Graph
    graph = Graph()
    graph.team_name = "Die Marsianer"
    graph_content = StructuredMainGraph(graph)  # TODO: Hier können Sie sehen wie die Inhalte und Verbindungen von Knoten angelegt werden

    # beautiful_code_graph = StructuredDemoGraph(graph) # TODO: Hier können Sie sehen wie die Inhalte und Verbindungen von Knoten strukturiert angelegt werden

    # Application
    component_assembler = ComponentAssembler(graph, screen, window_width, window_height)
    main = ApplicationLoopManager(component_assembler)
    # pygame beenden
    pygame.quit()
    sys.exit()
