"""
Copyright (C) 2023 TH Köln – University of Applied Sciences

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from GraphModel.Nodes.NodeSourceBook import NodeSourceBook
from GraphModel.Nodes.NodeSourceOnline import NodeSourceOnline
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Root.Root import TITEL as RootTITEL, CONTENT as RootCONTENT
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Sources import SourceQ1, SourceQ2
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Cluster31.Cluster31 import TITEL as Cluster31TITEL, CONTENT as Cluster31CONTENT
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Cluster31.content import (
    MathematikI_II,
    TheoretischeInformatikI_II,
    Algorithmik
)
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Cluster32.Cluster32 import TITEL as Cluster32TITEL, CONTENT as Cluster32CONTENT
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Cluster32.content import (
    AP1_AP2,
    BetriebssystemeRechnerarchitektur,
    Datenbanken,
    SoftwaretechnikI_II,
    KommunikationstechnikNetze,
    ParadigmenProgrammierung
)
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Cluster33.Cluster33 import TITEL as Cluster33TITEL, CONTENT as Cluster33CONTENT
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Cluster33.content import (
    EinführungsprojektInformatik,
    Projektmanagement,
    Praxissemester,
    PraxisprojektSeminar
)
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Cluster34.Cluster34 import TITEL as Cluster34TITEL, CONTENT as Cluster34CONTENT
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Cluster34.content import (
    KünstlicheIntelligenz,
    MenschComputerInteraktion
)
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Cluster35.Cluster35 import TITEL as Cluster35TITEL, CONTENT as Cluster35CONTENT
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Cluster35.content import (
    TeamDivergenzMatheHürde,
    TeamDivergenzProgrammiersprachen,
    SzenarioTheorieTurbo,
    SzenarioPraxisDualesModell
)
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Cluster36.Cluster36 import TITEL as Cluster36TITEL, CONTENT as Cluster36CONTENT
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Cluster36.content import (
    ZusammenfassungReakkreditierung
)
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.TheorieSchwerpunkt.TheorieSchwerpunkt import TITEL as TheorieSchwerpunktTITEL, CONTENT as TheorieSchwerpunktCONTENT
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.TheorieSchwerpunkt.content import (
    TheoretischeInformatik,
    Komplexitätstheorie,
    FormaleMethoden
)
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.AnwendungsSchwerpunkt.AnwendungsSchwerpunkt import TITEL as AnwendungsSchwerpunktTITEL, CONTENT as AnwendungsSchwerpunktCONTENT
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.AnwendungsSchwerpunkt.content import (
    SoftwareEngineering,
    PraktischeProjekte,
    Industriekooperationen
)
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.BalancePerspektiven.BalancePerspektiven import TITEL as BalancePerspektivenTITEL, CONTENT as BalancePerspektivenCONTENT
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.BalancePerspektiven.content import (
    Studierendenperspektive,
    Industrieanforderungen,
    WissenschaftlicheRelevanz,
    DidaktischeHerausforderungen
)
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Modulbeispiele.Modulbeispiele import TITEL as ModulbeispieleTITEL, CONTENT as ModulbeispieleCONTENT
from Structured_Main_Knowledge_Graph.GraphContent.TheorieAnwendung.Modulbeispiele.content import (
    AlgorithmikTheorieAnwendung,
    DatenbankenPraxis,
    KünstlicheIntelligenzBalance,
    NetzwerktechnikBalance
)


class TheorieAnwendungSubGraph:
    """
    Subgraph für das Verhältnis von Theorieanteil zu Anwendungsbezug im anwendungsorientierten 
    Informatik-Bachelor der TH Köln. Basierend auf dem Modulhandbuch mit 20 Detailknoten.
    """
    root_node: NodeKnowledge  # Hauptknoten (1.0 Ebene)

    def __init__(self, graph: Graph):
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        """
        Baut den Subgraph mit allen Knoten und Verbindungen auf.
        Struktur: Root -> 4 Kategorien + 6 Cluster -> Detailknoten + 2 Quellenknoten
        """
        # 1.0 Ebene: Root-Knoten
        self.root_node = NodeKnowledge(
            description=RootCONTENT,
            titel=RootTITEL
        )

        # Quellenknoten (Q1, Q2)
        source_q1 = NodeSourceBook(
            titel_of_the_book=SourceQ1.TITEL_OF_THE_BOOK,
            source_author=SourceQ1.AUTHOR,
            year_of_publication=SourceQ1.YEAR_OF_PUBLICATION,
            place_of_publication=SourceQ1.PLACE_OF_PUBLICATION,
            publisher=SourceQ1.PUBLISHER,
            ISBN=SourceQ1.ISBN,
            comment=SourceQ1.COMMENT
        )

        source_q2 = NodeSourceOnline(
            titel_of_the_document=SourceQ2.TITEL_OF_THE_DOCUMENT,
            source_author=SourceQ2.AUTHOR,
            year_of_publication=SourceQ2.YEAR_OF_PUBLICATION,
            titel_of_the_website=SourceQ2.TITEL_OF_THE_WEBSITE,
            URL=SourceQ2.URL,
            date_of_access=SourceQ2.DATE_OF_ACCESS,
            comment=SourceQ2.COMMENT
        )

        # 2.0 Ebene: Kategorie-Knoten (TheorieSchwerpunkt, AnwendungsSchwerpunkt, BalancePerspektiven, Modulbeispiele)
        theorie_schwerpunkt = NodeKnowledge(
            description=TheorieSchwerpunktCONTENT,
            titel=TheorieSchwerpunktTITEL
        )

        anwendungs_schwerpunkt = NodeKnowledge(
            description=AnwendungsSchwerpunktCONTENT,
            titel=AnwendungsSchwerpunktTITEL
        )

        balance_perspektiven = NodeKnowledge(
            description=BalancePerspektivenCONTENT,
            titel=BalancePerspektivenTITEL
        )

        modulbeispiele = NodeKnowledge(
            description=ModulbeispieleCONTENT,
            titel=ModulbeispieleTITEL
        )

        # 2.0 Ebene: Cluster-Knoten (3.1 - 3.6)
        cluster31 = NodeKnowledge(
            description=Cluster31CONTENT,
            titel=Cluster31TITEL
        )

        cluster32 = NodeKnowledge(
            description=Cluster32CONTENT,
            titel=Cluster32TITEL
        )

        cluster33 = NodeKnowledge(
            description=Cluster33CONTENT,
            titel=Cluster33TITEL
        )

        cluster34 = NodeKnowledge(
            description=Cluster34CONTENT,
            titel=Cluster34TITEL
        )

        cluster35 = NodeKnowledge(
            description=Cluster35CONTENT,
            titel=Cluster35TITEL
        )

        cluster36 = NodeKnowledge(
            description=Cluster36CONTENT,
            titel=Cluster36TITEL
        )

        # 3.0 Ebene: Detailknoten Cluster 3.1
        mathematik_node = NodeKnowledge(
            description=MathematikI_II.CONTENT,
            titel=MathematikI_II.TITEL
        )

        theoretische_informatik_node = NodeKnowledge(
            description=TheoretischeInformatikI_II.CONTENT,
            titel=TheoretischeInformatikI_II.TITEL
        )

        algorithmik_node = NodeKnowledge(
            description=Algorithmik.CONTENT,
            titel=Algorithmik.TITEL
        )

        # 3.0 Ebene: Detailknoten Cluster 3.2
        ap1_ap2_node = NodeKnowledge(
            description=AP1_AP2.CONTENT,
            titel=AP1_AP2.TITEL
        )

        betriebssysteme_node = NodeKnowledge(
            description=BetriebssystemeRechnerarchitektur.CONTENT,
            titel=BetriebssystemeRechnerarchitektur.TITEL
        )

        datenbanken_node = NodeKnowledge(
            description=Datenbanken.CONTENT,
            titel=Datenbanken.TITEL
        )

        softwaretechnik_node = NodeKnowledge(
            description=SoftwaretechnikI_II.CONTENT,
            titel=SoftwaretechnikI_II.TITEL
        )

        kommunikationstechnik_node = NodeKnowledge(
            description=KommunikationstechnikNetze.CONTENT,
            titel=KommunikationstechnikNetze.TITEL
        )

        paradigmen_node = NodeKnowledge(
            description=ParadigmenProgrammierung.CONTENT,
            titel=ParadigmenProgrammierung.TITEL
        )

        # 3.0 Ebene: Detailknoten Cluster 3.3
        einführungsprojekt_node = NodeKnowledge(
            description=EinführungsprojektInformatik.CONTENT,
            titel=EinführungsprojektInformatik.TITEL
        )

        projektmanagement_node = NodeKnowledge(
            description=Projektmanagement.CONTENT,
            titel=Projektmanagement.TITEL
        )

        praxissemester_node = NodeKnowledge(
            description=Praxissemester.CONTENT,
            titel=Praxissemester.TITEL
        )

        praxisprojekt_node = NodeKnowledge(
            description=PraxisprojektSeminar.CONTENT,
            titel=PraxisprojektSeminar.TITEL
        )

        # 3.0 Ebene: Detailknoten Cluster 3.4
        ki_node = NodeKnowledge(
            description=KünstlicheIntelligenz.CONTENT,
            titel=KünstlicheIntelligenz.TITEL
        )

        mci_node = NodeKnowledge(
            description=MenschComputerInteraktion.CONTENT,
            titel=MenschComputerInteraktion.TITEL
        )

        # 3.0 Ebene: Detailknoten Cluster 3.5
        team_divergenz_mathe_node = NodeKnowledge(
            description=TeamDivergenzMatheHürde.CONTENT,
            titel=TeamDivergenzMatheHürde.TITEL
        )

        team_divergenz_sprachen_node = NodeKnowledge(
            description=TeamDivergenzProgrammiersprachen.CONTENT,
            titel=TeamDivergenzProgrammiersprachen.TITEL
        )

        szenario_theorie_turbo_node = NodeKnowledge(
            description=SzenarioTheorieTurbo.CONTENT,
            titel=SzenarioTheorieTurbo.TITEL
        )

        szenario_praxis_dual_node = NodeKnowledge(
            description=SzenarioPraxisDualesModell.CONTENT,
            titel=SzenarioPraxisDualesModell.TITEL
        )

        # 3.0 Ebene: Detailknoten Cluster 3.6
        zusammenfassung_node = NodeKnowledge(
            description=ZusammenfassungReakkreditierung.CONTENT,
            titel=ZusammenfassungReakkreditierung.TITEL
        )

        # 3.0 Ebene: Detailknoten TheorieSchwerpunkt
        theoretische_informatik_theorie_node = NodeKnowledge(
            description=TheoretischeInformatik.CONTENT,
            titel=TheoretischeInformatik.TITEL
        )

        komplexitätstheorie_node = NodeKnowledge(
            description=Komplexitätstheorie.CONTENT,
            titel=Komplexitätstheorie.TITEL
        )

        formale_methoden_node = NodeKnowledge(
            description=FormaleMethoden.CONTENT,
            titel=FormaleMethoden.TITEL
        )

        # 3.0 Ebene: Detailknoten AnwendungsSchwerpunkt
        software_engineering_node = NodeKnowledge(
            description=SoftwareEngineering.CONTENT,
            titel=SoftwareEngineering.TITEL
        )

        praktische_projekte_node = NodeKnowledge(
            description=PraktischeProjekte.CONTENT,
            titel=PraktischeProjekte.TITEL
        )

        industriekooperationen_node = NodeKnowledge(
            description=Industriekooperationen.CONTENT,
            titel=Industriekooperationen.TITEL
        )

        # 3.0 Ebene: Detailknoten BalancePerspektiven
        studierendenperspektive_node = NodeKnowledge(
            description=Studierendenperspektive.CONTENT,
            titel=Studierendenperspektive.TITEL
        )

        industrieanforderungen_node = NodeKnowledge(
            description=Industrieanforderungen.CONTENT,
            titel=Industrieanforderungen.TITEL
        )

        wissenschaftliche_relevanz_node = NodeKnowledge(
            description=WissenschaftlicheRelevanz.CONTENT,
            titel=WissenschaftlicheRelevanz.TITEL
        )

        didaktische_herausforderungen_node = NodeKnowledge(
            description=DidaktischeHerausforderungen.CONTENT,
            titel=DidaktischeHerausforderungen.TITEL
        )

        # 3.0 Ebene: Detailknoten Modulbeispiele
        algorithmik_theorie_anwendung_node = NodeKnowledge(
            description=AlgorithmikTheorieAnwendung.CONTENT,
            titel=AlgorithmikTheorieAnwendung.TITEL
        )

        datenbanken_praxis_node = NodeKnowledge(
            description=DatenbankenPraxis.CONTENT,
            titel=DatenbankenPraxis.TITEL
        )

        ki_balance_node = NodeKnowledge(
            description=KünstlicheIntelligenzBalance.CONTENT,
            titel=KünstlicheIntelligenzBalance.TITEL
        )

        netzwerktechnik_balance_node = NodeKnowledge(
            description=NetzwerktechnikBalance.CONTENT,
            titel=NetzwerktechnikBalance.TITEL
        )

        # Verbindungen: Root zu Quellen
        self.root_node.connect(source_q1)
        self.root_node.connect(source_q2)

        # Verbindungen: Root zu Kategorien
        self.root_node.connect(theorie_schwerpunkt)
        self.root_node.connect(anwendungs_schwerpunkt)
        self.root_node.connect(balance_perspektiven)
        self.root_node.connect(modulbeispiele)

        # Verbindungen: Root zu Clustern
        self.root_node.connect(cluster31)
        self.root_node.connect(cluster32)
        self.root_node.connect(cluster33)
        self.root_node.connect(cluster34)
        self.root_node.connect(cluster35)
        self.root_node.connect(cluster36)

        # Verbindungen: Cluster 3.1 zu Detailknoten
        cluster31.connect(mathematik_node)
        cluster31.connect(theoretische_informatik_node)
        cluster31.connect(algorithmik_node)

        # Verbindungen: Cluster 3.2 zu Detailknoten
        cluster32.connect(ap1_ap2_node)
        cluster32.connect(betriebssysteme_node)
        cluster32.connect(datenbanken_node)
        cluster32.connect(softwaretechnik_node)
        cluster32.connect(kommunikationstechnik_node)
        cluster32.connect(paradigmen_node)

        # Verbindungen: Cluster 3.3 zu Detailknoten
        cluster33.connect(einführungsprojekt_node)
        cluster33.connect(projektmanagement_node)
        cluster33.connect(praxissemester_node)
        cluster33.connect(praxisprojekt_node)

        # Verbindungen: Cluster 3.4 zu Detailknoten
        cluster34.connect(ki_node)
        cluster34.connect(mci_node)

        # Verbindungen: Cluster 3.5 zu Detailknoten
        cluster35.connect(team_divergenz_mathe_node)
        cluster35.connect(team_divergenz_sprachen_node)
        cluster35.connect(szenario_theorie_turbo_node)
        cluster35.connect(szenario_praxis_dual_node)

        # Verbindungen: Cluster 3.6 zu Detailknoten
        cluster36.connect(zusammenfassung_node)

        # Verbindungen: TheorieSchwerpunkt zu Detailknoten
        theorie_schwerpunkt.connect(theoretische_informatik_theorie_node)
        theorie_schwerpunkt.connect(komplexitätstheorie_node)
        theorie_schwerpunkt.connect(formale_methoden_node)

        # Verbindungen: AnwendungsSchwerpunkt zu Detailknoten
        anwendungs_schwerpunkt.connect(software_engineering_node)
        anwendungs_schwerpunkt.connect(praktische_projekte_node)
        anwendungs_schwerpunkt.connect(industriekooperationen_node)

        # Verbindungen: BalancePerspektiven zu Detailknoten
        balance_perspektiven.connect(studierendenperspektive_node)
        balance_perspektiven.connect(industrieanforderungen_node)
        balance_perspektiven.connect(wissenschaftliche_relevanz_node)
        balance_perspektiven.connect(didaktische_herausforderungen_node)

        # Verbindungen: Modulbeispiele zu Detailknoten
        modulbeispiele.connect(algorithmik_theorie_anwendung_node)
        modulbeispiele.connect(datenbanken_praxis_node)
        modulbeispiele.connect(ki_balance_node)
        modulbeispiele.connect(netzwerktechnik_balance_node)

        # Querverbindungen zwischen verwandten Knoten
        mathematik_node.connect(theoretische_informatik_node)
        theoretische_informatik_node.connect(algorithmik_node)
        algorithmik_node.connect(ap1_ap2_node)
        softwaretechnik_node.connect(einführungsprojekt_node)
        einführungsprojekt_node.connect(projektmanagement_node)
        praxissemester_node.connect(praxisprojekt_node)
        ki_node.connect(mci_node)

        # Querverbindungen: TheorieSchwerpunkt mit Clustern
        theoretische_informatik_theorie_node.connect(theoretische_informatik_node)
        komplexitätstheorie_node.connect(algorithmik_node)
        formale_methoden_node.connect(softwaretechnik_node)

        # Querverbindungen: AnwendungsSchwerpunkt mit Clustern
        software_engineering_node.connect(softwaretechnik_node)
        praktische_projekte_node.connect(einführungsprojekt_node)
        praktische_projekte_node.connect(praxisprojekt_node)
        industriekooperationen_node.connect(praxissemester_node)

        # Querverbindungen: Modulbeispiele mit Clustern
        algorithmik_theorie_anwendung_node.connect(algorithmik_node)
        datenbanken_praxis_node.connect(datenbanken_node)
        ki_balance_node.connect(ki_node)
        netzwerktechnik_balance_node.connect(kommunikationstechnik_node)

        # Querverbindungen: BalancePerspektiven mit anderen Knoten
        studierendenperspektive_node.connect(team_divergenz_mathe_node)
        industrieanforderungen_node.connect(software_engineering_node)
        wissenschaftliche_relevanz_node.connect(theoretische_informatik_theorie_node)
        didaktische_herausforderungen_node.connect(modulbeispiele)

        # Alle Knoten zum Graphen hinzufügen
        # Root und Quellen
        graph.add_new_node_to_graph(self.root_node)
        graph.add_new_node_to_graph(source_q1)
        graph.add_new_node_to_graph(source_q2)

        # Kategorien
        graph.add_new_node_to_graph(theorie_schwerpunkt)
        graph.add_new_node_to_graph(anwendungs_schwerpunkt)
        graph.add_new_node_to_graph(balance_perspektiven)
        graph.add_new_node_to_graph(modulbeispiele)

        # Cluster
        graph.add_new_node_to_graph(cluster31)
        graph.add_new_node_to_graph(cluster32)
        graph.add_new_node_to_graph(cluster33)
        graph.add_new_node_to_graph(cluster34)
        graph.add_new_node_to_graph(cluster35)
        graph.add_new_node_to_graph(cluster36)

        # Detailknoten Cluster 3.1
        graph.add_new_node_to_graph(mathematik_node)
        graph.add_new_node_to_graph(theoretische_informatik_node)
        graph.add_new_node_to_graph(algorithmik_node)

        # Detailknoten Cluster 3.2
        graph.add_new_node_to_graph(ap1_ap2_node)
        graph.add_new_node_to_graph(betriebssysteme_node)
        graph.add_new_node_to_graph(datenbanken_node)
        graph.add_new_node_to_graph(softwaretechnik_node)
        graph.add_new_node_to_graph(kommunikationstechnik_node)
        graph.add_new_node_to_graph(paradigmen_node)

        # Detailknoten Cluster 3.3
        graph.add_new_node_to_graph(einführungsprojekt_node)
        graph.add_new_node_to_graph(projektmanagement_node)
        graph.add_new_node_to_graph(praxissemester_node)
        graph.add_new_node_to_graph(praxisprojekt_node)

        # Detailknoten Cluster 3.4
        graph.add_new_node_to_graph(ki_node)
        graph.add_new_node_to_graph(mci_node)

        # Detailknoten Cluster 3.5
        graph.add_new_node_to_graph(team_divergenz_mathe_node)
        graph.add_new_node_to_graph(team_divergenz_sprachen_node)
        graph.add_new_node_to_graph(szenario_theorie_turbo_node)
        graph.add_new_node_to_graph(szenario_praxis_dual_node)

        # Detailknoten Cluster 3.6
        graph.add_new_node_to_graph(zusammenfassung_node)

        # Detailknoten TheorieSchwerpunkt
        graph.add_new_node_to_graph(theoretische_informatik_theorie_node)
        graph.add_new_node_to_graph(komplexitätstheorie_node)
        graph.add_new_node_to_graph(formale_methoden_node)

        # Detailknoten AnwendungsSchwerpunkt
        graph.add_new_node_to_graph(software_engineering_node)
        graph.add_new_node_to_graph(praktische_projekte_node)
        graph.add_new_node_to_graph(industriekooperationen_node)

        # Detailknoten BalancePerspektiven
        graph.add_new_node_to_graph(studierendenperspektive_node)
        graph.add_new_node_to_graph(industrieanforderungen_node)
        graph.add_new_node_to_graph(wissenschaftliche_relevanz_node)
        graph.add_new_node_to_graph(didaktische_herausforderungen_node)

        # Detailknoten Modulbeispiele
        graph.add_new_node_to_graph(algorithmik_theorie_anwendung_node)
        graph.add_new_node_to_graph(datenbanken_praxis_node)
        graph.add_new_node_to_graph(ki_balance_node)
        graph.add_new_node_to_graph(netzwerktechnik_balance_node)
