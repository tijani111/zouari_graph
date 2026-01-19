from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from GraphModel.Nodes.NodeSourcePaper import NodeSourcePaper
from Structured_Demo_Knowledge_Graph.GraphContent.PaperSource import SourceTheHumbleProgrammer, PaperSourceExampleData


class PaperSourceSubGraph:
    paper_source_example_knowledge_node: NodeKnowledge  # Instanzattribut: Wir spezifizieren hier explizit den Typ (NodeKnowledge) damit Python weiß welche Methoden und Attribute bereitgestellt werden.

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        """
        Hier wird self genutzt damit der online_source_example_knowledge_node (siehe oben) als Instanzattribut bereitsteht.
        Dies ermöglicht es uns in der Klasse StructuredDemoGraph in der Methode connect_sub_graphs diesen Knoten
        zu referenzieren und Verbindungen zu Knoten anderer Subgraphen herzustellen.
        """
        # Knoten anlegen
        self.paper_source_example_knowledge_node = NodeKnowledge(description = PaperSourceExampleData.CONTENT,
                                                                 titel = PaperSourceExampleData.TITEL)
        paper_source_example_node = NodeSourcePaper(titel_of_the_article=SourceTheHumbleProgrammer.TITEL_OF_THE_ARTICLE,
                                                    source_author=SourceTheHumbleProgrammer.AUTHOR,
                                                    year_of_publication=SourceTheHumbleProgrammer.YEAR_OF_PUBLICATION,
                                                    titel_of_the_journal=SourceTheHumbleProgrammer.TITEL_OF_THE_JOURNAL,
                                                    volume_and_issue=SourceTheHumbleProgrammer.VOLUME_AND_ISSUE,
                                                    comment=SourceTheHumbleProgrammer.COMMENT
                                                    )
        # Knoten verbinden
        self.paper_source_example_knowledge_node.connect(paper_source_example_node)

        # Knoten im Graphen einfügen
        graph.add_new_node_to_graph(self.paper_source_example_knowledge_node)
        graph.add_new_node_to_graph(paper_source_example_node)
