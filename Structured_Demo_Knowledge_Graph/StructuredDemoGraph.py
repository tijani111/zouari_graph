from GraphModel.Graph import Graph
from Structured_Demo_Knowledge_Graph.GraphStructure.ExternePerspektive import (
    ExternePerspektiveSubGraph,
)


class StructuredDemoGraph:
    def __init__(self, graph: Graph):
        self.create_structured_demo_graph(graph)

    def create_structured_demo_graph(self, graph: Graph):
        ExternePerspektiveSubGraph(graph)
