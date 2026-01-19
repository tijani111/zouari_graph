from GraphModel.Graph import Graph
from Structured_Main_Knowledge_Graph.GraphStructure.AktualitaetInhalte.AktualInhaltSubGraph import AktualitaetSubGraph
from Structured_Main_Knowledge_Graph.GraphStructure.HowToSubGraph import HowToSubGraph
from Structured_Main_Knowledge_Graph.GraphStructure.InhaltBedarf.InhaltBedarfSubGraph import InhaltBedarfSubGraph
from Structured_Main_Knowledge_Graph.GraphStructure.TheorieAnwendung.TheorieAnwendungSubGraph import TheorieAnwendungSubGraph
from Structured_Main_Knowledge_Graph.GraphStructure.Modulabfolge.ModulabfolgeSubGraph import ModulabfolgeSubGraph


class StructuredMainGraph:
    """
    Diese Klasse hat die Verantwortlichkeit einen Graphen aus Subgraphen aufzubauen
    und Knoten der Subgraphen nach Bedarf zu verbinden.
    """

    aktualitaet_subgraph: AktualitaetSubGraph


    how_to_subgraph: HowToSubGraph
    modulabfolge_subgraph: ModulabfolgeSubGraph
    inhalt_bedarf_subgraph: InhaltBedarfSubGraph
    theorie_anwendung_subgraph: TheorieAnwendungSubGraph




    def __init__(self, graph: Graph):
        self.assemble_graph(graph)
        self.connect_sub_graphs()

    def assemble_graph(self, graph: Graph):
        """
        Subgraphen anlegen und dem Graphen hinzufügen.
        """


        self.aktualitaet_subgraph = AktualitaetSubGraph(graph)
        self.theorie_anwendung_subgraph = TheorieAnwendungSubGraph(graph)

        self.how_to_subgraph = HowToSubGraph(graph)

        self.modulabfolge_subgraph = ModulabfolgeSubGraph(graph)
         #Subgraph für „2.0 Passung zwischen Studieninhalten und tatsächlichem Kompetenzbedarf“
        self.inhalt_bedarf_subgraph = InhaltBedarfSubGraph(graph)
        
        
    def connect_sub_graphs(self):

        self.how_to_subgraph.how_to_node.connect(self.modulabfolge_subgraph.modulabfolge_node)
        self.how_to_subgraph.how_to_node.connect(
            self.inhalt_bedarf_subgraph.inhaltBedarf
        )
        self.how_to_subgraph.how_to_node.connect(
            self.aktualitaet_subgraph.introduction_knowledge_node
        )
        self.how_to_subgraph.how_to_node.connect(
            self.theorie_anwendung_subgraph.root_node
        )





