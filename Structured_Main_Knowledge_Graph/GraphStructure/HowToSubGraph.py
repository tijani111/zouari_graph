from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeIllustration import NodeIllustration
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from Structured_Main_Knowledge_Graph.GraphContent.Root import root
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf import InhaltBedarfIllustration
from Structured_Main_Knowledge_Graph import Modullhandbuch
from GraphModel.Nodes.NodeSourceOnline import NodeSourceOnline



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
        self.how_to_node = NodeKnowledge(description=root.CONTENT,
                                         titel=root.TITEL)

        #inhaltBedarf = NodeKnowledge(description=InhaltBedarfIllustration.CONTENT,
                   #   titel=InhaltBedarfIllustration.TITEL)
        #inhaltBedarf = NodeIllustration(titel=InhaltBedarfIllustration.TITEL, image_name=InhaltBedarfIllustration.IMAGE_NAME)

        modullhandbuch_source = NodeSourceOnline(titel_of_the_document=Modullhandbuch.TITEL_OF_THE_DOCUMENT,
                                                 source_author=Modullhandbuch.AUTHOR,
                                                 year_of_publication=Modullhandbuch.YEAR_OF_PUBLICATION,
                                                 titel_of_the_website=Modullhandbuch.TITEL_OF_THE_WEBSITE,
                                                 URL=Modullhandbuch.URL,
                                                 date_of_access=Modullhandbuch.DATE_OF_ACCESS)
        # Knoten verbinden
        self.how_to_node.connect(modullhandbuch_source)

        # Knoten im Graphen einfügen
        graph.add_new_node_to_graph(self.how_to_node)
        graph.add_new_node_to_graph(modullhandbuch_source)
