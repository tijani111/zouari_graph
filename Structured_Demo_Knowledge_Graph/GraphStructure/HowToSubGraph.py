from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Demo_Knowledge_Graph.GraphContent.HowTo import HowToNodeData
from Structured_Demo_Knowledge_Graph.GraphContent.Illustration_Example import ProblemIllustration


class HowToSubGraph:
    how_to_node: NodeKnowledge  # Instanzattribut: Wir spezifizieren hier explizit den Typ (NodeKnowledge) damit Python weiß welche Methoden und Attribute bereitgestellt werden.

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        """
        Hier wird self genutzt damit der how_to_node (siehe oben) als Instanzattribut bereitsteht.
        Dies ermöglicht es uns in der Klasse StructuredDemoGraph in der Methode connect_sub_graphs diesen Knoten
        zu referenzieren und Verbindungen zu Knoten anderer Subgraphen herzustellen.
        """
        # Knoten anlegen
        self.how_to_node = NodeKnowledge(description=HowToNodeData.CONTENT,
                                         titel=HowToNodeData.TITEL)
        illustration_node_example = NodeIllustration(titel=ProblemIllustration.TITEL,
                                                     image_name=ProblemIllustration.IMAGE_NAME)

        # Knoten verbinden
        self.how_to_node.connect(illustration_node_example)

        # Knoten im Graphen einfügen
        graph.add_new_node_to_graph(self.how_to_node)
        graph.add_new_node_to_graph(illustration_node_example)
