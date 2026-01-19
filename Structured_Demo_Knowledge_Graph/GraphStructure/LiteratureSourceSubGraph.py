from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from GraphModel.Nodes.NodeSourceBook import NodeSourceBook
from Structured_Demo_Knowledge_Graph.GraphContent.LiteratureSource import LiteratureSourceExampleData, \
    SourceCleanCraftsmanship


class LiteratureSourceSubGraph:
    literature_source_example_knowledge_node: NodeKnowledge  # Instanzattribut: Wir spezifizieren hier explizit den Typ (NodeKnowledge) damit Python weiß welche Methoden und Attribute bereitgestellt werden.

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        """
        Hier wird self genutzt damit der literature_source_example_knowledge_node (siehe oben) als Instanzattribut bereitsteht.
        Dies ermöglicht es uns in der Klasse StructuredDemoGraph in der Methode connect_sub_graphs diesen Knoten
        zu referenzieren und Verbindungen zu Knoten anderer Subgraphen herzustellen.
        """
        # Knoten anlegen
        self.literature_source_example_knowledge_node = NodeKnowledge(description = LiteratureSourceExampleData.CONTENT,
                                                                      titel = LiteratureSourceExampleData.TITEL)

        literature_source_example_node = NodeSourceBook(titel_of_the_book=SourceCleanCraftsmanship.TITEL_OF_THE_BOOK,
                                                        source_author=SourceCleanCraftsmanship.AUTHOR,
                                                        year_of_publication=SourceCleanCraftsmanship.YEAR_OF_PUBLICATION,
                                                        place_of_publication=SourceCleanCraftsmanship.PLACE_OF_PUBLICATION,
                                                        publisher=SourceCleanCraftsmanship.PUBLISHER,
                                                        ISBN=SourceCleanCraftsmanship.ISBN)

        # Knoten verbinden
        self.literature_source_example_knowledge_node.connect(literature_source_example_node)

        # Knoten im Graphen einfügen
        graph.add_new_node_to_graph(self.literature_source_example_knowledge_node)
        graph.add_new_node_to_graph(literature_source_example_node)
