import pygame

from View.GraphView.GraphVisualizer import GraphVisualizer


class CustomGraphVisualizer(GraphVisualizer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Slightly larger font for readability.
        self.font = pygame.font.Font(None, 18)
        # Show connections by default, keep similarity hidden.
        self.connection_edges_rendering = True
        self.similarity_edges_rendering = False
