from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from GraphModel.Nodes.NodeSourceOnline import NodeSourceOnline
from Structured_Main_Knowledge_Graph.GraphContent.Modulabfolge import (K0_ModulabfolgeData,
                                                                       K1_EinstiegOrientierung,K1_1_EPI,K1_2_Programmierung,K1_3_EinstiegTheoriePraxis,K1_4_Einstiegslast,
                                                                       K2_Grundlagenphase, K2_1_Mathe, K2_3_EBR, K2_2_TI, K2_4_AP, K2_5_Mathe2,
                                                                       K3_Vertiefung, K3_1_ALG_PP, K3_2_DBS, K3_3_ST, K3_4_Bundelung,
                                                                       K4_Kontextmodule, K4_1_BWL, K4_2_IUP, K4_3_IUG, K4_4_PM,
                                                                       K5_Praxissemester, K5_1_PS_nach_Vertiefung, K5_2_Vorbereitung, K5_3_Rückkehr,
                                                                       K6_Abschluss,K6_1_WPF, K6_2,K6_3, K6_4,
                                                                       K7_FlexVerlauf, K7_1_AlternativeVerlauf, K7_2_Herausforderungen, K7_3_Abweichungen, K7_4_Erwerb)




class ModulabfolgeSubGraph:
    modulabfolge_node: NodeKnowledge  # Instanzattribut: Wir spezifizieren hier explizit den Typ (NodeKnowledge) damit Python weiß welche Methoden und Attribute bereitgestellt werden.

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        """
        Hier wird self genutzt damit der modulabfolge_node (siehe oben) als Instanzattribut bereitsteht.
        Dies ermöglicht es uns in der Klasse StructuredDemoGraph in der Methode connect_sub_graphs diesen Knoten
        zu referenzieren und Verbindungen zu Knoten anderer Subgraphen herzustellen.
        """
        # Knoten anlegen
        self.modulabfolge_node = NodeKnowledge(description=K0_ModulabfolgeData.CONTENT,
                                         titel=K0_ModulabfolgeData.TITEL)

        modulabfolge_source = NodeSourceOnline(titel_of_the_document="TITEL_OF_THE_DOCUMENT",
                                                      source_author="AUTHOR",
                                                      year_of_publication="YEAR_OF_PUBLICATION",
                                                      titel_of_the_website="TITEL_OF_THE_WEBSITE",
                                                      URL="URL",
                                                      date_of_access="DATE_OF_ACCESS")

        einstieg_node = NodeKnowledge(description=K1_EinstiegOrientierung.CONTENT,titel=K1_EinstiegOrientierung.TITEL)
        e1 = NodeKnowledge(description=K1_1_EPI.CONTENT,titel=K1_1_EPI.TITEL)
        e2 = NodeKnowledge(description=K1_2_Programmierung.CONTENT,titel=K1_2_Programmierung.TITEL)
        e3 = NodeKnowledge(description=K1_3_EinstiegTheoriePraxis.CONTENT,titel=K1_3_EinstiegTheoriePraxis.TITEL)
        e4 = NodeKnowledge(description=K1_4_Einstiegslast.CONTENT,titel=K1_4_Einstiegslast.TITEL)

        grundlagen_node = NodeKnowledge(description=K2_Grundlagenphase.CONTENT,titel=K2_Grundlagenphase.TITEL)
        g1 = NodeKnowledge(description=K2_1_Mathe.CONTENT,titel=K2_1_Mathe.TITEL)
        g2 = NodeKnowledge(description=K2_2_TI.CONTENT,titel=K2_2_TI.TITEL)
        g3 = NodeKnowledge(description=K2_3_EBR.CONTENT,titel=K2_3_EBR.TITEL)
        g4 = NodeKnowledge(description=K2_4_AP.CONTENT,titel=K2_4_AP.TITEL)
        g5 = NodeKnowledge(description=K2_5_Mathe2.CONTENT,titel=K2_5_Mathe2.TITEL)

        vertiefungsphase_node = NodeKnowledge(description=K3_Vertiefung.CONTENT,titel=K3_Vertiefung.TITEL)
        v1 = NodeKnowledge(description=K3_1_ALG_PP.CONTENT,titel=K3_1_ALG_PP.TITEL)
        v2 = NodeKnowledge(description=K3_2_DBS.CONTENT,titel=K3_2_DBS.TITEL)
        v3 = NodeKnowledge(description=K3_3_ST.CONTENT,titel=K3_3_ST.TITEL)
        v4 = NodeKnowledge(description=K3_4_Bundelung.CONTENT,titel=K3_4_Bundelung.TITEL)

        kontext_node = NodeKnowledge(description=K4_Kontextmodule.CONTENT,titel=K4_Kontextmodule.TITEL)
        k1 = NodeKnowledge(description=K4_1_BWL.CONTENT,titel=K4_1_BWL.TITEL)
        k2 = NodeKnowledge(description=K4_2_IUP.CONTENT,titel=K4_2_IUP.TITEL)
        k3 = NodeKnowledge(description=K4_3_IUG.CONTENT,titel=K4_3_IUG.TITEL)
        k4 = NodeKnowledge(description=K4_4_PM.CONTENT,titel=K4_4_PM.TITEL)

        praxissemester_node = NodeKnowledge(description=K5_Praxissemester.CONTENT,titel=K5_Praxissemester.TITEL)
        p1 = NodeKnowledge(description=K5_1_PS_nach_Vertiefung.CONTENT,titel=K5_1_PS_nach_Vertiefung.TITEL)
        p2 = NodeKnowledge(description=K5_2_Vorbereitung.CONTENT,titel=K5_2_Vorbereitung.TITEL)
        p3 = NodeKnowledge(description=K5_3_Rückkehr.CONTENT,titel=K5_3_Rückkehr.TITEL)

        spezialisierung_node = NodeKnowledge(description=K6_Abschluss.CONTENT,titel=K6_Abschluss.TITEL)
        s1 = NodeKnowledge(description=K6_1_WPF.CONTENT,titel=K6_1_WPF.TITEL)
        s2 = NodeKnowledge(description=K6_2.CONTENT,titel=K6_2.TITEL)
        s3 = NodeKnowledge(description=K6_3.CONTENT,titel=K6_3.TITEL)
        s4 = NodeKnowledge(description=K6_4.CONTENT,titel=K6_4.TITEL)

        flex_node = NodeKnowledge(description=K7_FlexVerlauf.CONTENT,titel=K7_FlexVerlauf.TITEL)
        f1 = NodeKnowledge(description=K7_1_AlternativeVerlauf.CONTENT,titel=K7_1_AlternativeVerlauf.TITEL)
        f2 = NodeKnowledge(description=K7_2_Herausforderungen.CONTENT,titel=K7_2_Herausforderungen.TITEL)
        f3 = NodeKnowledge(description=K7_3_Abweichungen.CONTENT,titel=K7_3_Abweichungen.TITEL)
        f4 = NodeKnowledge(description=K7_4_Erwerb.CONTENT,titel=K7_4_Erwerb.TITEL)

        # Knoten verbinden

        self.modulabfolge_node.connect(einstieg_node)
        einstieg_node.connect(e1)
        einstieg_node.connect(e2)
        einstieg_node.connect(e3)
        einstieg_node.connect(e4)

        self.modulabfolge_node.connect(grundlagen_node)
        grundlagen_node.connect(g1)
        grundlagen_node.connect(g2)
        grundlagen_node.connect(g3)
        grundlagen_node.connect(g4)
        grundlagen_node.connect(g5)

        self.modulabfolge_node.connect(vertiefungsphase_node)
        vertiefungsphase_node.connect(v1)
        vertiefungsphase_node.connect(v2)
        vertiefungsphase_node.connect(v3)
        vertiefungsphase_node.connect(v4)

        self.modulabfolge_node.connect(kontext_node)
        kontext_node.connect(k1)
        kontext_node.connect(k2)
        kontext_node.connect(k3)
        kontext_node.connect(k4)

        self.modulabfolge_node.connect(praxissemester_node)
        praxissemester_node.connect(p1)
        praxissemester_node.connect(p2)
        praxissemester_node.connect(p3)

        self.modulabfolge_node.connect(spezialisierung_node)
        spezialisierung_node.connect(s1)
        spezialisierung_node.connect(s2)
        spezialisierung_node.connect(s3)
        spezialisierung_node.connect(s4)

        self.modulabfolge_node.connect(flex_node)
        flex_node.connect(f1)
        flex_node.connect(f2)
        flex_node.connect(f3)
        flex_node.connect(f4)

        # Knoten im Graphen einfügen
        graph.add_new_node_to_graph(self.modulabfolge_node)

        graph.add_new_node_to_graph(einstieg_node)
        graph.add_new_node_to_graph(e1)
        graph.add_new_node_to_graph(e2)
        graph.add_new_node_to_graph(e3)
        graph.add_new_node_to_graph(e4)

        graph.add_new_node_to_graph(grundlagen_node)
        graph.add_new_node_to_graph(g1)
        graph.add_new_node_to_graph(g2)
        graph.add_new_node_to_graph(g3)
        graph.add_new_node_to_graph(g4)
        graph.add_new_node_to_graph(g5)

        graph.add_new_node_to_graph(vertiefungsphase_node)
        graph.add_new_node_to_graph(v1)
        graph.add_new_node_to_graph(v2)
        graph.add_new_node_to_graph(v3)
        graph.add_new_node_to_graph(v4)

        graph.add_new_node_to_graph(kontext_node)
        graph.add_new_node_to_graph(k1)
        graph.add_new_node_to_graph(k2)
        graph.add_new_node_to_graph(k3)
        graph.add_new_node_to_graph(k4)

        graph.add_new_node_to_graph(praxissemester_node)
        graph.add_new_node_to_graph(p1)
        graph.add_new_node_to_graph(p2)
        graph.add_new_node_to_graph(p3)

        graph.add_new_node_to_graph(spezialisierung_node)
        graph.add_new_node_to_graph(s1)
        graph.add_new_node_to_graph(s2)
        graph.add_new_node_to_graph(s3)
        graph.add_new_node_to_graph(s4)

        graph.add_new_node_to_graph(flex_node)
        graph.add_new_node_to_graph(f1)
        graph.add_new_node_to_graph(f2)
        graph.add_new_node_to_graph(f3)
        graph.add_new_node_to_graph(f4)