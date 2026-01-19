"""
Local entry point for running only the personal demo graph
without changing the project's main.py (stammcode).
"""

import pygame.freetype
import sys

from Structured_Demo_Knowledge_Graph.PersonalStructuredGraph import PersonalStructuredGraph

from View.ApplicationLoopManager import ApplicationLoopManager
from ComponentAssembly.CustomComponentAssembler import CustomComponentAssembler
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
    graph_content = PersonalStructuredGraph(graph)

    # Application
    component_assembler = CustomComponentAssembler(graph, screen, window_width, window_height)
    main = ApplicationLoopManager(component_assembler)
    # pygame beenden
    pygame.quit()
    sys.exit()
