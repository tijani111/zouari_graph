from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from GraphModel.Nodes.NodeSourceOnline import NodeSourceOnline
from Structured_Demo_Knowledge_Graph.GraphContent.OnlineSource import OnlineSourceExampleData, SourceMarkdown


class OnlineSourceSubGraph:
    online_source_example_knowledge_node: NodeKnowledge  # Instanzattribut: Wir spezifizieren hier explizit den Typ (NodeKnowledge) damit Python weiß welche Methoden und Attribute bereitgestellt werden.

    def __init__(self, graph: Graph):
        self.online_source_example_knowledge_node: NodeKnowledge
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        """
        Hier wird self genutzt damit der online_source_example_knowledge_node (siehe oben) als Instanzattribut bereitsteht.
        Dies ermöglicht es uns in der Klasse StructuredDemoGraph in der Methode connect_sub_graphs diesen Knoten
        zu referenzieren und Verbindungen zu Knoten anderer Subgraphen herzustellen.
        """
        # Knoten anlegen
        self.online_source_example_knowledge_node: NodeKnowledge = NodeKnowledge(description = OnlineSourceExampleData.CONTENT,
                                                                                 titel = OnlineSourceExampleData.TITEL)
        online_source_example_node = NodeSourceOnline(titel_of_the_document=SourceMarkdown.TITEL_OF_THE_DOCUMENT,
                                                      source_author=SourceMarkdown.AUTHOR,
                                                      year_of_publication=SourceMarkdown.YEAR_OF_PUBLICATION,
                                                      titel_of_the_website=SourceMarkdown.TITEL_OF_THE_WEBSITE,
                                                      URL=SourceMarkdown.URL,
                                                      date_of_access=SourceMarkdown.DATE_OF_ACCESS)

        # Knoten verbinden
        self.online_source_example_knowledge_node.connect(online_source_example_node)

        # Knoten im Graphen einfügen
        graph.add_new_node_to_graph(self.online_source_example_knowledge_node)
        graph.add_new_node_to_graph(online_source_example_node)
