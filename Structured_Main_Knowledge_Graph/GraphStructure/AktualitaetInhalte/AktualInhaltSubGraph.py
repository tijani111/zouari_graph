from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from GraphModel.Nodes.NodeSourceOnline import NodeSourceOnline
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import AktualitaetInhalteData
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import Mathematik
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import ALGO
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import AP
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import BS
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import BWL
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import DatenbankenEins
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import DatenbankenZwei
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import EBR
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import EPI
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import IRG
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import IuP
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import KI
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import PM
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import PP
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import Praxissemester
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import ST
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import ST2
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import TI
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import Trends
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import WPF
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import Bewertung
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Paper import MCI
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Quelle import AIACT
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Quelle import Jetbrains
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Quelle import StackOverflowSurvey
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Quelle import TrendsSource
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Quelle import UniKoeln
from Structured_Main_Knowledge_Graph.GraphContent.AktualitaetInhalte.Quelle import VibeCoding



class AktualitaetSubGraph:
    introduction_knowledge_node: NodeKnowledge  # Instanzattribut: Wir spezifizieren hier explizit den Typ (NodeKnowledge) damit Python weiß welche Methoden und Attribute bereitgestellt werden.

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        """
        Hier wird self genutzt damit der how_to_node (siehe oben) als Instanzattribut bereitsteht.
        Dies ermöglicht es uns in der Klasse StructuredDemoGraph in der Methode connect_sub_graphs diesen Knoten
        zu referenzieren und Verbindungen zu Knoten anderer Subgraphen herzustellen.
        """

        # Knoten anlegen
        self.introduction_knowledge_node = NodeKnowledge(description=AktualitaetInhalteData.CONTENT,
                                                         titel=AktualitaetInhalteData.TITEL)

        EPI_ = NodeKnowledge(description=EPI.CONTENT,
                            titel=EPI.TITEL)

        Mathe = NodeKnowledge(description=Mathematik.CONTENT,
                            titel=Mathematik.TITEL)

        Algorithmik = NodeKnowledge(description=ALGO.CONTENT,
                              titel=ALGO.TITEL)

        Programmieren = NodeKnowledge(description=AP.CONTENT,
                              titel=AP.TITEL)

        Beetriebssysteme = NodeKnowledge(description=BS.CONTENT,
                              titel=BS.TITEL)

        BeWL = NodeKnowledge(description=BWL.CONTENT,
                              titel=BWL.TITEL)

        Datenbanken1 = NodeKnowledge(description=DatenbankenEins.CONTENT,
                              titel=DatenbankenEins.TITEL)

        Datenbanken2 = NodeKnowledge(description=DatenbankenZwei.CONTENT,
                              titel=DatenbankenZwei.TITEL)

        EBR_ = NodeKnowledge(description=EBR.CONTENT,
                              titel=EBR.TITEL)

        IRG_ = NodeKnowledge(description=IRG.CONTENT,
                              titel=IRG.TITEL)

        IuP_ = NodeKnowledge(description=IuP.CONTENT,
                              titel=IuP.TITEL)

        KI_ = NodeKnowledge(description=KI.CONTENT,
                              titel=KI.TITEL)

        PM_ = NodeKnowledge(description=PM.CONTENT,
                              titel=PM.TITEL)

        PP_ = NodeKnowledge(description=PP.CONTENT,
                              titel=PP.TITEL)

        Praxis_ = NodeKnowledge(description=Praxissemester.CONTENT,
                              titel=Praxissemester.TITEL)

        ST_ = NodeKnowledge(description=ST.CONTENT,
                              titel=ST.TITEL)

        ST2_ = NodeKnowledge(description=ST2.CONTENT,
                              titel=ST2.TITEL)

        TI_ = NodeKnowledge(description=TI.CONTENT,
                              titel=TI.TITEL)

        Trends_ = NodeKnowledge(description=Trends.CONTENT,
                              titel=Trends.TITEL)

        WPF_ = NodeKnowledge(description=WPF.CONTENT,
                              titel=WPF.TITEL)

        Bewerte = NodeKnowledge(description=Bewertung.CONTENT,
                                titel=Bewertung.TITEL)

        _MCI = NodeKnowledge(description=MCI.CONTENT,
                                titel=MCI.TITEL)

        SourceRoot = NodeKnowledge(description="",
                             titel="QUELLEN")

        SourceAI = NodeSourceOnline(titel_of_the_document=AIACT.TITEL_OF_THE_DOCUMENT,
                                                      source_author=AIACT.AUTHOR,
                                                      year_of_publication=AIACT.YEAR_OF_PUBLICATION,
                                                      titel_of_the_website=AIACT.TITEL_OF_THE_WEBSITE,
                                                      URL=AIACT.URL,
                                                      date_of_access=AIACT.DATE_OF_ACCESS)

        Jetbrains_ = NodeSourceOnline(titel_of_the_document=Jetbrains.TITEL_OF_THE_DOCUMENT,
                                    source_author=Jetbrains.AUTHOR,
                                    year_of_publication=Jetbrains.YEAR_OF_PUBLICATION,
                                    titel_of_the_website=Jetbrains.TITEL_OF_THE_WEBSITE,
                                    URL=Jetbrains.URL,
                                    date_of_access=Jetbrains.DATE_OF_ACCESS)

        Stack_ = NodeSourceOnline(titel_of_the_document=StackOverflowSurvey.TITEL_OF_THE_DOCUMENT,
                                      source_author=StackOverflowSurvey.AUTHOR,
                                      year_of_publication=StackOverflowSurvey.YEAR_OF_PUBLICATION,
                                      titel_of_the_website=StackOverflowSurvey.TITEL_OF_THE_WEBSITE,
                                      URL=StackOverflowSurvey.URL,
                                      date_of_access=StackOverflowSurvey.DATE_OF_ACCESS)

        _Trends_ = NodeSourceOnline(titel_of_the_document=TrendsSource.TITEL_OF_THE_DOCUMENT,
                                  source_author=TrendsSource.AUTHOR,
                                  year_of_publication=TrendsSource.YEAR_OF_PUBLICATION,
                                  titel_of_the_website=TrendsSource.TITEL_OF_THE_WEBSITE,
                                  URL=TrendsSource.URL,
                                  date_of_access=TrendsSource.DATE_OF_ACCESS)

        UniK_ = NodeSourceOnline(titel_of_the_document=UniKoeln.TITEL_OF_THE_DOCUMENT,
                                   source_author=UniKoeln.AUTHOR,
                                   year_of_publication=UniKoeln.YEAR_OF_PUBLICATION,
                                   titel_of_the_website=UniKoeln.TITEL_OF_THE_WEBSITE,
                                   URL=UniKoeln.URL,
                                   date_of_access=UniKoeln.DATE_OF_ACCESS)

        VibeCoding_ = NodeSourceOnline(titel_of_the_document=VibeCoding.TITEL_OF_THE_DOCUMENT,
                                 source_author=VibeCoding.AUTHOR,
                                 year_of_publication=VibeCoding.YEAR_OF_PUBLICATION,
                                 titel_of_the_website=VibeCoding.TITEL_OF_THE_WEBSITE,
                                 URL=VibeCoding.URL,
                                 date_of_access=VibeCoding.DATE_OF_ACCESS)




        # Knoten verbinden
        self.introduction_knowledge_node.connect(EPI_)
        self.introduction_knowledge_node.connect(Mathe)
        self.introduction_knowledge_node.connect(Algorithmik)
        self.introduction_knowledge_node.connect(Programmieren)
        self.introduction_knowledge_node.connect(Beetriebssysteme)
        self.introduction_knowledge_node.connect(BeWL)
        self.introduction_knowledge_node.connect(Datenbanken1)
        self.introduction_knowledge_node.connect(Datenbanken2)
        self.introduction_knowledge_node.connect(EBR_)
        self.introduction_knowledge_node.connect(IRG_)
        self.introduction_knowledge_node.connect(IuP_)
        self.introduction_knowledge_node.connect(KI_)
        self.introduction_knowledge_node.connect(PM_)
        self.introduction_knowledge_node.connect(PP_)
        self.introduction_knowledge_node.connect(Praxis_)
        self.introduction_knowledge_node.connect(ST_)
        self.introduction_knowledge_node.connect(ST2_)
        self.introduction_knowledge_node.connect(TI_)
        self.introduction_knowledge_node.connect(Trends_)
        self.introduction_knowledge_node.connect(WPF_)
        self.introduction_knowledge_node.connect(Bewerte)
        self.introduction_knowledge_node.connect(_MCI)
        self.introduction_knowledge_node.connect(SourceRoot)
        SourceRoot.connect(SourceAI)
        SourceRoot.connect(Jetbrains_)
        SourceRoot.connect(Stack_)
        SourceRoot.connect(_Trends_)
        SourceRoot.connect(UniK_)
        SourceRoot.connect(VibeCoding_)

        # Knoten im Graphen einfügen
        graph.add_new_node_to_graph(self.introduction_knowledge_node)
        graph.add_new_node_to_graph(EPI_)
        graph.add_new_node_to_graph(Mathe)
        graph.add_new_node_to_graph(Algorithmik)
        graph.add_new_node_to_graph(Programmieren)
        graph.add_new_node_to_graph(Beetriebssysteme)
        graph.add_new_node_to_graph(BeWL)
        graph.add_new_node_to_graph(Datenbanken1)
        graph.add_new_node_to_graph(Datenbanken2)
        graph.add_new_node_to_graph(EBR_)
        graph.add_new_node_to_graph(IRG_)
        graph.add_new_node_to_graph(IuP_)
        graph.add_new_node_to_graph(KI_)
        graph.add_new_node_to_graph(PM_)
        graph.add_new_node_to_graph(Praxis_)
        graph.add_new_node_to_graph(ST_)
        graph.add_new_node_to_graph(ST2_)
        graph.add_new_node_to_graph(TI_)
        graph.add_new_node_to_graph(Trends_)
        graph.add_new_node_to_graph(WPF_)
        graph.add_new_node_to_graph(PP_)
        graph.add_new_node_to_graph(Bewerte)
        graph.add_new_node_to_graph(_MCI)
        graph.add_new_node_to_graph(SourceRoot)
        graph.add_new_node_to_graph(SourceAI)
        graph.add_new_node_to_graph(Jetbrains_)
        graph.add_new_node_to_graph(Stack_)
        graph.add_new_node_to_graph(_Trends_)
        graph.add_new_node_to_graph(UniK_)
        graph.add_new_node_to_graph(VibeCoding_)

