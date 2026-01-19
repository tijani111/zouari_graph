from GraphModel.Graph import Graph
from Structured_Main_Knowledge_Graph.GraphStructure.ExternePerspektiven.ExternePerspektivenSubGraph import (
    ExternePerspektivenSubGraph,
)


class StructuredMainGraph:
    """
    Diese Klasse hat die Verantwortlichkeit einen Graphen aus Subgraphen aufzubauen
    und Knoten der Subgraphen nach Bedarf zu verbinden.
    """

    externe_perspektive_subgraph: ExternePerspektivenSubGraph

    def __init__(self, graph: Graph):
        self.assemble_graph(graph)
        self.connect_sub_graphs()

    def assemble_graph(self, graph: Graph):
        """
        Subgraph anlegen und dem Graphen hinzufuegen.
        """
        self.externe_perspektive_subgraph = ExternePerspektivenSubGraph(graph)

    def connect_sub_graphs(self):
        # Nur dein Subgraph: keine weiteren Verbindungen notwendig.
        return
