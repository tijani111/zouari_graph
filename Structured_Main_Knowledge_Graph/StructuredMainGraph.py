from GraphModel.Graph import Graph
from Structured_Demo_Knowledge_Graph.GraphStructure.ExternePerspektive.ExternePerspektiveSubGraph import (
    ExternePerspektiveSubGraph,
)


class StructuredMainGraph:
    """
    Diese Klasse hat die Verantwortlichkeit einen Graphen aus Subgraphen aufzubauen
    und Knoten der Subgraphen nach Bedarf zu verbinden.
    """

    externe_perspektive_subgraph: ExternePerspektiveSubGraph

    def __init__(self, graph: Graph):
        self.assemble_graph(graph)
        self.connect_sub_graphs()

    def assemble_graph(self, graph: Graph):
        """
        Subgraph anlegen und dem Graphen hinzufuegen.
        """
        self.externe_perspektive_subgraph = ExternePerspektiveSubGraph(graph)

    def connect_sub_graphs(self):
        # Nur dein Subgraph: keine weiteren Verbindungen notwendig.
        return
