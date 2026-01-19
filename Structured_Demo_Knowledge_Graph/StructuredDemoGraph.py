from GraphModel.Graph import Graph
from Structured_Main_Knowledge_Graph.GraphStructure.ExternePerspektiven import (
    ExternePerspektivenSubGraph,
)


class StructuredDemoGraph:
    def __init__(self, graph: Graph):
        self.create_structured_demo_graph(graph)

    def create_structured_demo_graph(self, graph: Graph):
        ExternePerspektivenSubGraph(graph)
