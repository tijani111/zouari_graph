from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from GraphModel.Nodes.NodeSourcePaper import NodeSourcePaper
from GraphModel.Nodes.NodeSourceOnline import NodeSourceOnline  # todo
from GraphModel.Nodes.NodeSourceBook import NodeSourceBook
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf import InhaltBedarfIllustration
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.AnwendungVertiefungsphase import \
    AnwendungVertiefungsphase
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.AnwendungVertiefungsphase.DatenbankenKernkompetenz import \
    DatenbankenKernkompetenz
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.AnwendungVertiefungsphase.DatenbankenKernkompetenz.content import \
    ModerneDatenbanktechnologien, AnwendungsorientierungDatenbanken
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.AnwendungVertiefungsphase.FehlendeKompetenzen import \
    FehlendeKompetenzen
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.AnwendungVertiefungsphase.FehlendeKompetenzen.content import \
    SoftSkillsNichttechnisch, TechnologietrendsAktualitaet
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.AnwendungVertiefungsphase.GesamtbewertungStudierende import \
    GesamtbewertungStudierende
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.AnwendungVertiefungsphase.SoftwareEngineeringProjekt import \
    SoftwareEngineeringProjekt
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.AnwendungVertiefungsphase.SoftwareEngineeringProjekt.content import \
    TeamarbeitRealeProjekte, RealitaetsnaeheProjekte
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.AnwendungVertiefungsphase.WahlpflichtSpezialisierung import \
    WahlpflichtSpezialisierung
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.AnwendungVertiefungsphase.WahlpflichtSpezialisierung.content import \
    PassungKarriereziele, TransparenzKompetenzziele
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.GrundlagenPhase import GrundlagenPhase
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.GrundlagenPhase.AlgorithmenDatenstrukturen.content import \
    Transferfähigkeit
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.GrundlagenPhase.EinführungProgrammierung import \
    EinführungProgrammierung
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.GrundlagenPhase.EinführungProgrammierung.content import \
    DidaktischeProgression, Programmiersprachen
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.GrundlagenPhase.MathematischeGrundlagen import \
    MathematischenGrundlagen
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.GrundlagenPhase.MathematischeGrundlagen.content import \
    RelevanzMathematischerInhalte, WahrnehmungForderungen
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.KernInformatik import Kerninformatik
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.KernInformatik.AlgorithmenDatenstrukturen import \
    AlgorithmenDatenstrukturen
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.KernInformatik.AlgorithmenDatenstrukturen.content import \
    Praxisrelevanz
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.KernInformatik.RechnerarchitekturBetriebssysteme import \
    RechnerarchitekturBetriebssysteme
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.KernInformatik.RechnerarchitekturBetriebssysteme.content import \
    PraxisnäheInhalt, RelevanzSWE
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.KernInformatik.TheoretischeInformatik import \
    TheoretischeInformatik
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.KernInformatik.TheoretischeInformatik.content import \
    KompetenzGewinnAbstraktDenken, WahrgenommenerNutzenPraxis

# Root + Inhalte (Beispiele, bitte alle deine Content-Dateien hier importieren)


# Referenzen
from Structured_Main_Knowledge_Graph.GraphContent.InhaltBedarf.references import (
    literatur_ACMCC2020,
    literatur_Gromov2020,
    literatur_Silva2024,
    literatur_Tripathi2025,
    literatur_Clem2025,
    literatur_Sathya2022,
    literatur_Koseda2025,
    literatur_Wing2006,
    literatur_Tanenbaum2021,
    # Biggs2011, Sudkamp2018, SoftSkillsIT2025, NoSQLReview2025 etc. kannst du analog ergänzen
)


class InhaltBedarfSubGraph:
    """
    Subgraph „2.0 Passung zwischen Studieninhalten und tatsächlichem Kompetenzbedarf“
    mit hierarchisch verbundenen NodeKnowledge-Knoten und zugehörigen Quellen.
    """
    inhaltBedarf: NodeKnowledge  # Instanzattribut

    def __init__(self, graph: Graph):
        self.graph = graph
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        # Wurzelknoten für den Teil „InhaltBedarf“
        self.inhaltBedarf = NodeKnowledge(
            description=InhaltBedarfIllustration.CONTENT,
            titel=InhaltBedarfIllustration.TITEL,
        )

        # Knoten in den Graphen einfügen
        graph.add_new_node_to_graph(self.inhaltBedarf)

        # #todo Koseda2025, Sathya2022, Gromov2020 → je eine Quelle
        source_2_0_koseda = NodeSourcePaper(
            titel_of_the_article=literatur_Koseda2025.TITEL_OF_THE_ARTICLE,
            source_author=literatur_Koseda2025.AUTHOR,
            year_of_publication=literatur_Koseda2025.YEAR_OF_PUBLICATION,
            titel_of_the_journal=literatur_Koseda2025.TITEL_OF_THE_JOURNAL,
            volume_and_issue=literatur_Koseda2025.VOLUME_AND_ISSUE,
            comment=literatur_Koseda2025.COMMENT,
        )
        source_2_0_sathya = NodeSourcePaper(
            titel_of_the_article=literatur_Sathya2022.TITEL_OF_THE_ARTICLE,
            source_author=literatur_Sathya2022.AUTHOR,
            year_of_publication=literatur_Sathya2022.YEAR_OF_PUBLICATION,
            titel_of_the_journal=literatur_Sathya2022.TITEL_OF_THE_JOURNAL,
            volume_and_issue=getattr(literatur_Sathya2022, "VOLUME_AND_ISSUE", ""),
            comment=literatur_Sathya2022.COMMENT,
        )
        source_2_0_gromov = NodeSourcePaper(
            titel_of_the_article=literatur_Gromov2020.TITEL_OF_THE_ARTICLE,
            source_author=literatur_Gromov2020.AUTHOR,
            year_of_publication=literatur_Gromov2020.YEAR_OF_PUBLICATION,
            titel_of_the_journal=literatur_Gromov2020.TITEL_OF_THE_JOURNAL,
            volume_and_issue=getattr(literatur_Gromov2020, "VOLUME_AND_ISSUE", ""),
            comment=literatur_Gromov2020.COMMENT,
        )

        self.inhaltBedarf.connect(source_2_0_koseda)
        graph.add_new_node_to_graph(source_2_0_koseda)
        self.inhaltBedarf.connect(source_2_0_sathya)
        graph.add_new_node_to_graph(source_2_0_sathya)
        self.inhaltBedarf.connect(source_2_0_gromov)
        graph.add_new_node_to_graph(source_2_0_gromov)


        # 2.1 Mathe: #todo Wing2006
        source_2_1_wing = NodeSourcePaper(
            titel_of_the_article=literatur_Wing2006.TITEL_OF_THE_ARTICLE,
            source_author=literatur_Wing2006.AUTHOR,
            year_of_publication=literatur_Wing2006.YEAR_OF_PUBLICATION,
            titel_of_the_journal=literatur_Wing2006.TITEL_OF_THE_JOURNAL,
            volume_and_issue=literatur_Wing2006.VOLUME_AND_ISSUE,
            comment=literatur_Wing2006.COMMENT,
        )

        source_2_1_1_acm = NodeSourcePaper(
            titel_of_the_article=literatur_ACMCC2020.TITEL_OF_THE_ARTICLE,
            source_author=literatur_ACMCC2020.AUTHOR,
            year_of_publication=literatur_ACMCC2020.YEAR_OF_PUBLICATION,
            titel_of_the_journal=literatur_ACMCC2020.TITEL_OF_THE_JOURNAL,
            volume_and_issue=getattr(literatur_ACMCC2020, "VOLUME_AND_ISSUE", ""),
            comment=literatur_ACMCC2020.COMMENT,
        )
        source_2_1_1_sathya = NodeSourcePaper(
            titel_of_the_article=literatur_Sathya2022.TITEL_OF_THE_ARTICLE,
            source_author=literatur_Sathya2022.AUTHOR,
            year_of_publication=literatur_Sathya2022.YEAR_OF_PUBLICATION,
            titel_of_the_journal=literatur_Sathya2022.TITEL_OF_THE_JOURNAL,
            volume_and_issue=getattr(literatur_Sathya2022, "VOLUME_AND_ISSUE", ""),
            comment=literatur_Sathya2022.COMMENT,
        )
        source_2_2_silva = NodeSourcePaper(
            titel_of_the_article=literatur_Silva2024.TITEL_OF_THE_ARTICLE,
            source_author=literatur_Silva2024.AUTHOR,
            year_of_publication=literatur_Silva2024.YEAR_OF_PUBLICATION,
            titel_of_the_journal=literatur_Silva2024.TITEL_OF_THE_JOURNAL,
            volume_and_issue=getattr(literatur_Silva2024, "VOLUME_AND_ISSUE", ""),
            comment=literatur_Silva2024.COMMENT,
        )
        source_2_7_1_triPath = NodeSourcePaper(
            titel_of_the_article=literatur_Tripathi2025.TITEL_OF_THE_ARTICLE,
            source_author=literatur_Tripathi2025.AUTHOR,
            year_of_publication=literatur_Tripathi2025.YEAR_OF_PUBLICATION,
            titel_of_the_journal=literatur_Tripathi2025.TITEL_OF_THE_JOURNAL,
            volume_and_issue=getattr(literatur_Tripathi2025, "VOLUME_AND_ISSUE", ""),
            comment=literatur_Tripathi2025.COMMENT,
        )

        source_2_7_1_Clem = NodeSourcePaper(
            titel_of_the_article=literatur_Clem2025.TITEL_OF_THE_ARTICLE,
            source_author=literatur_Clem2025.AUTHOR,
            year_of_publication=literatur_Clem2025.YEAR_OF_PUBLICATION,
            titel_of_the_journal=literatur_Clem2025.TITEL_OF_THE_JOURNAL,
            volume_and_issue=literatur_Clem2025.VOLUME_AND_ISSUE,
            comment=literatur_Clem2025.COMMENT,
        )


        source_2_5_tanenbaum = NodeSourceBook(
            titel_of_the_book=literatur_Tanenbaum2021.TITEL_OF_THE_ARTICLE,
            source_author=literatur_Tanenbaum2021.AUTHOR,
            year_of_publication=literatur_Tanenbaum2021.YEAR_OF_PUBLICATION,
            publisher=getattr(literatur_Tanenbaum2021, "VOLUME_AND_ISSUE", ""),
            comment=literatur_Tanenbaum2021.COMMENT,
            ISBN="",  # todo
            place_of_publication=""  # todo
        )

        # --- A. Grundlagenphase (2.1 / 2.2) ---
        grundlagenphase = NodeKnowledge(
            description=GrundlagenPhase.CONTENT,
            titel=GrundlagenPhase.TITEL,
        )

        self.inhaltBedarf.connect(grundlagenphase)
        graph.add_new_node_to_graph(grundlagenphase)

        node_2_1 = NodeKnowledge(
            description=MathematischenGrundlagen.CONTENT,
            titel=MathematischenGrundlagen.TITEL,
        )
        grundlagenphase.connect(node_2_1)
        graph.add_new_node_to_graph(node_2_1)


        node_2_1.connect(source_2_1_wing)
        graph.add_new_node_to_graph(source_2_1_wing)

        # 2.1.1 Relevanz mathematischer Inhalte (#todo ACM2020, Sathya2022)
        node_2_1_1 = NodeKnowledge(
            description=RelevanzMathematischerInhalte.CONTENT,
            titel=RelevanzMathematischerInhalte.TITEL,
        )
        node_2_1.connect(node_2_1_1)
        graph.add_new_node_to_graph(node_2_1_1)

        node_2_1_1.connect(source_2_1_1_acm)
        node_2_1_1.connect(source_2_1_1_sathya)
        graph.add_new_node_to_graph(source_2_1_1_acm)
        graph.add_new_node_to_graph(source_2_1_1_sathya)

        # 2.1.2 Wahrgenommene Über-/Unterforderung (#todo Biggs2011 – analog als Book/Paper-Source anlegen)

        node_2_1_2 = NodeKnowledge(
            description=WahrnehmungForderungen.CONTENT,
            titel=WahrnehmungForderungen.TITEL,
        )
        node_2_1.connect(node_2_1_2)
        graph.add_new_node_to_graph(node_2_1_2)
        # hier dann NodeSourceBook/NodeSourcePaper für Biggs2011 anhängen

        # 2.2 Einführung in die Programmierung (#todo Perceptions2024 etc.)
        node_2_2 = NodeKnowledge(
            description=EinführungProgrammierung.CONTENT,
            titel=EinführungProgrammierung.TITEL,
        )
        grundlagenphase.connect(node_2_2)
        graph.add_new_node_to_graph(node_2_2)


        node_2_2.connect(source_2_2_silva)
        graph.add_new_node_to_graph(source_2_2_silva)

        node_2_2_1 = NodeKnowledge(
            description=DidaktischeProgression.CONTENT,
            titel=DidaktischeProgression.TITEL,
        )
        node_2_2.connect(node_2_2_1)
        graph.add_new_node_to_graph(node_2_2_1)

        node_2_2_2 = NodeKnowledge(
            description=Programmiersprachen.CONTENT,
            titel=Programmiersprachen.TITEL,
        )
        node_2_2.connect(node_2_2_2)
        graph.add_new_node_to_graph(node_2_2_2)


        # --- B. Kerninformatik (2.3 – 2.5) ---
        kerninformatik = NodeKnowledge(
            description=Kerninformatik.CONTENT,
            titel=Kerninformatik.TITEL,
        )
        self.inhaltBedarf.connect(kerninformatik)
        graph.add_new_node_to_graph(kerninformatik)

        node_2_3 = NodeKnowledge(
            description=AlgorithmenDatenstrukturen.CONTENT,
            titel=AlgorithmenDatenstrukturen.TITEL,
        )
        kerninformatik.connect(node_2_3)
        graph.add_new_node_to_graph(node_2_3)

        # 2.3 #todo Gromov2020
        #node_2_3.connect(source_2_0_gromov)  # Gromov kann mehrfach referenziert werden

        node_2_3_1 = NodeKnowledge(
            description=Praxisrelevanz.CONTENT,
            titel=Praxisrelevanz.TITEL,
        )
        node_2_3.connect(node_2_3_1)
        graph.add_new_node_to_graph(node_2_3_1)
        # Quelle: Perceptions2024 → Silva2024 wiederverwenden oder eigener SourcePaper

        node_2_3_2 = NodeKnowledge(
            description=Transferfähigkeit.CONTENT,
            titel=Transferfähigkeit.TITEL,
        )
        node_2_3.connect(node_2_3_2)
        graph.add_new_node_to_graph(node_2_3_2)
        # Quelle: Sathya2022 → . source_2_1_1_sathya wiederverwenden

        # 2.4 Theoretische Informatik, 2.4.1, 2.4.2 – analog mit Sudkamp2018, Perceptions2024, Wing2006
        node_2_4 = NodeKnowledge(
            description=TheoretischeInformatik.CONTENT,
            titel=TheoretischeInformatik.TITEL,
        )
        kerninformatik.connect(node_2_4)
        graph.add_new_node_to_graph(node_2_4)

        node_2_4_1 = NodeKnowledge(
            description=KompetenzGewinnAbstraktDenken.CONTENT,
            titel=KompetenzGewinnAbstraktDenken.TITEL,
        )
        node_2_4.connect(node_2_4_1)
        graph.add_new_node_to_graph(node_2_4_1)

        node_2_4_2 = NodeKnowledge(
            description=WahrgenommenerNutzenPraxis.CONTENT,
            titel=WahrgenommenerNutzenPraxis.TITEL,
        )
        node_2_4.connect(node_2_4_2)
        graph.add_new_node_to_graph(node_2_4_2)


        # 2.5 Rechnerarchitektur und Betriebssysteme – mit Tanenbaum2021, Gromov2020 etc.
        node_2_5 = NodeKnowledge(
            description=RechnerarchitekturBetriebssysteme.CONTENT,
            titel=RechnerarchitekturBetriebssysteme.TITEL,
        )
        kerninformatik.connect(node_2_5)
        graph.add_new_node_to_graph(node_2_5)
        node_2_5.connect(source_2_5_tanenbaum)
        graph.add_new_node_to_graph(source_2_5_tanenbaum)

        node_2_5_1 = NodeKnowledge(
            description=PraxisnäheInhalt.CONTENT,
            titel=PraxisnäheInhalt.TITEL,
        )
        node_2_5.connect(node_2_5_1)
        graph.add_new_node_to_graph(node_2_5_1)

        node_2_5_2 = NodeKnowledge(
            description=RelevanzSWE.CONTENT,
            titel=RelevanzSWE.TITEL,
        )
        node_2_5.connect(node_2_5_2)
        graph.add_new_node_to_graph(node_2_5_2)




        #node_2_5.connect(source_2_0_gromov)
        #graph.add_new_node_to_graph(source_2_5_tanenbaum)

        # --- C. Anwendungs- und Vertiefungsphase (2.6 – 2.8) ---
        anwendungVertiefungsphase = NodeKnowledge(
            description=AnwendungVertiefungsphase.CONTENT,
            titel=AnwendungVertiefungsphase.TITEL,
        )
        self.inhaltBedarf.connect(anwendungVertiefungsphase)
        graph.add_new_node_to_graph(anwendungVertiefungsphase)

        # 2.6 Software Engineering und Projektarbeit (ACM2020, Perceptions2024)
        node_2_6 = NodeKnowledge(
            description=SoftwareEngineeringProjekt.CONTENT,
            titel=SoftwareEngineeringProjekt.TITEL,
        )
        anwendungVertiefungsphase.connect(node_2_6)
        graph.add_new_node_to_graph(node_2_6)

        #node_2_6.connect(source_2_1_1_acm)   # ACMCC2020
        #node_2_6.connect(source_2_2_silva)  # Perceptions/Industry Demands



        node_2_6_1 = NodeKnowledge(
            description=TeamarbeitRealeProjekte.CONTENT,
            titel=TeamarbeitRealeProjekte.TITEL,
        )
        node_2_6.connect(node_2_6_1)
        graph.add_new_node_to_graph(node_2_6_1)
       # node_2_6_1.connect(source_2_1_1_acm)

        node_2_6_2 = NodeKnowledge(
            description=RealitaetsnaeheProjekte.CONTENT,
            titel=RealitaetsnaeheProjekte.TITEL,
        )
        node_2_6.connect(node_2_6_2)
        graph.add_new_node_to_graph(node_2_6_2)

        # 2.7 Datenbanken und Informationssysteme, 2.7.1, 2.7.2 (ACM2020, Tripathi, JISE/Clem)
        node_2_7 = NodeKnowledge(
            description=DatenbankenKernkompetenz.CONTENT,
            titel=DatenbankenKernkompetenz.TITEL,
        )
        anwendungVertiefungsphase.connect(node_2_7)
        graph.add_new_node_to_graph(node_2_7)
        #node_2_7.connect(source_2_1_1_acm)

        node_2_7_1 = NodeKnowledge(
            description=ModerneDatenbanktechnologien.CONTENT,
            titel=ModerneDatenbanktechnologien.TITEL,
        )
        node_2_7.connect(node_2_7_1)
        graph.add_new_node_to_graph(node_2_7_1)
        node_2_7_1.connect(source_2_7_1_Clem)
        node_2_7_1.connect(source_2_7_1_triPath)
        graph.add_new_node_to_graph(source_2_7_1_Clem)
        graph.add_new_node_to_graph(source_2_7_1_triPath)


        node_2_7_2 = NodeKnowledge(
            description=AnwendungsorientierungDatenbanken.CONTENT,
            titel=AnwendungsorientierungDatenbanken.TITEL,
        )
        node_2_7.connect(node_2_7_2)
        graph.add_new_node_to_graph(node_2_7_2)
       # node_2_7_2.connect(source_2_0_gromov)

        # 2.8 Wahlpflichtmodule und Spezialisierung (mit Gromov, Sathya etc.)
        node_2_8 = NodeKnowledge(
            description=WahlpflichtSpezialisierung.CONTENT,
            titel=WahlpflichtSpezialisierung.TITEL,
        )
        anwendungVertiefungsphase.connect(node_2_8)
        graph.add_new_node_to_graph(node_2_8)

        node_2_8_1 = NodeKnowledge(
            description=PassungKarriereziele.CONTENT,
            titel=PassungKarriereziele.TITEL,
        )
        node_2_8.connect(node_2_8_1)
        graph.add_new_node_to_graph(node_2_8_1)
        #node_2_8_1.connect(source_2_0_gromov)

        node_2_8_2 = NodeKnowledge(
            description=TransparenzKompetenzziele.CONTENT,
            titel=TransparenzKompetenzziele.TITEL,
        )
        node_2_8.connect(node_2_8_2)
        graph.add_new_node_to_graph(node_2_8_2)
        #node_2_8_2.connect(source_2_0_sathya)

        # --- D. Übergreifende Kompetenzdimensionen (2.9, 2.9.1, 2.9.2, 2.10) ---
        node_2_9 = NodeKnowledge(
            description=FehlendeKompetenzen.CONTENT,
            titel=FehlendeKompetenzen.TITEL,
        )
        self.inhaltBedarf.connect(node_2_9)
        graph.add_new_node_to_graph(node_2_9)
        #node_2_9.connect(source_2_2_silva)

        node_2_9_1 = NodeKnowledge(
            description=SoftSkillsNichttechnisch.CONTENT,
            titel=SoftSkillsNichttechnisch.TITEL,
        )
        node_2_9.connect(node_2_9_1)
        graph.add_new_node_to_graph(node_2_9_1)
       # node_2_9_1.connect(source_2_2_silva)
       # node_2_9_1.connect(source_2_0_sathya)

        node_2_9_2 = NodeKnowledge(
            description=TechnologietrendsAktualitaet.CONTENT,
            titel=TechnologietrendsAktualitaet.TITEL,
        )
        node_2_9.connect(node_2_9_2)
        graph.add_new_node_to_graph(node_2_9_2)
        #node_2_9_2.connect(source_2_0_gromov)

        node_2_10 = NodeKnowledge(
            description=GesamtbewertungStudierende.CONTENT,
            titel=GesamtbewertungStudierende.TITEL,
        )
        self.inhaltBedarf.connect(node_2_10)
        graph.add_new_node_to_graph(node_2_10)
        #node_2_10.connect(source_2_0_gromov)
        #node_2_10.connect(source_2_0_koseda)
