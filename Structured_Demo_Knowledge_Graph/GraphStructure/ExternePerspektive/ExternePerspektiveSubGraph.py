from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from GraphModel.Nodes.NodeSourceOnline import NodeSourceOnline


class ExternePerspektiveSubGraph:
    def __init__(self, graph: Graph):
        self.topic_node = None
        self.cat_keep = None
        self.cat_drop = None
        self.cat_try = None
        self.per_self = None
        self.per_peers = None
        self.per_research = None
        self.sources = []
        self.create_subgraph(graph)

    def create_subgraph(self, graph: Graph):
        self.topic_node = NodeKnowledge(
            "Topic for this section of the knowledge graph.",
            "Einbindung externer Perspektiven",
            150,
            150,
        )
        self.topic_node.author = "Topic"

        self.cat_keep = NodeKnowledge("Evaluation category: KEEP", "KEEP", 40, 90)
        self.cat_drop = NodeKnowledge("Evaluation category: DROP", "DROP", 40, 150)
        self.cat_try = NodeKnowledge("Evaluation category: TRY", "TRY", 40, 210)
        for node in (self.cat_keep, self.cat_drop, self.cat_try):
            node.author = "Kategorie"

        self.per_self = NodeKnowledge("Perspective: Eigene Erfahrung", "Eigene Erfahrung", 260, 90)
        self.per_peers = NodeKnowledge("Perspective: Mitstudierende", "Mitstudierende", 260, 150)
        self.per_research = NodeKnowledge("Perspective: Recherche", "Recherche", 260, 210)
        for node in (self.per_self, self.per_peers, self.per_research):
            node.author = "Perspektive"

        src_tum = self._create_online_source(
            "Gastvortraege Informatik",
            "TU Muenchen",
            "in.tum.de",
            "https://www.in.tum.de/die-fakultaet/news-events/gastvortraege/",
            50,
            300,
        )
        src_hamburg = self._create_online_source(
            "Projektmodule Informatik",
            "Universitaet Hamburg",
            "inf.uni-hamburg.de",
            "https://www.inf.uni-hamburg.de/studies/bachelor.html",
            120,
            300,
        )
        src_che = self._create_online_source(
            "Lehr- und Praxisbezug (CHE Hochschulranking)",
            "CHE Hochschulranking",
            "ranking.zeit.de",
            "https://ranking.zeit.de/che/de/studiengang/43171",
            190,
            300,
        )
        src_tu_dortmund = self._create_online_source(
            "Kooperationen mit NGOs",
            "TU Dortmund",
            "informatik.tu-dortmund.de",
            "https://informatik.tu-dortmund.de/studium/kooperationen-ngos/",
            260,
            300,
        )
        src_tu_berlin = self._create_online_source(
            "Studienprojektmodule Informatik",
            "TU Berlin",
            "tu.berlin",
            "https://www.tu.berlin/informatik/studium/lehrveranstaltungen/",
            330,
            300,
        )
        self.sources = [src_tum, src_hamburg, src_che, src_tu_dortmund, src_tu_berlin]

        knowledge_nodes = [
            (
                "Industrienahe Gastvortraege foerdern Praxisverstaendnis",
                "Industriebezogene Gastvortraege stellen Praxisfaelle und Berufsbilder vor und "
                "unterstuetzen damit ein besseres Verstaendnis der Anforderungen in der beruflichen Praxis. "
                "Sie machen sichtbar, wie theoretische Inhalte in realen Projekten angewendet werden, "
                "und erhoehen die Anschlussfaehigkeit an die Arbeitswelt.",
                self.cat_keep,
                self.per_self,
                src_tum,
            ),
            (
                "Externe Praxisberichte erhoehen Motivation",
                "Praxisberichte externer Referentinnen und Referenten vermitteln greifbare "
                "Anwendungsbeispiele und koennen die Motivation durch nachvollziehbare Berufswege staerken. "
                "Sie helfen, den Nutzen einzelner Module konkret zu verorten und Lernziele besser nachzuvollziehen.",
                self.cat_keep,
                self.per_peers,
                src_tum,
            ),
            (
                "Praxisprojekte mit externen Partnern sind lernwirksam",
                "Projektmodule mit externen Partnern verknuepfen Studieninhalte "
                "mit realen Aufgabenstellungen und foerdern anwendungsbezogene Kompetenzen. "
                "Durch konkrete Anforderungen werden Teamarbeit, Planung und fachliche Umsetzung trainiert.",
                self.cat_keep,
                self.per_peers,
                src_hamburg,
            ),
            (
                "Kooperationen mit Unternehmen erleichtern Berufseinstieg",
                "Kooperationen im Rahmen von Projektmodulen ermoeglichen fruehe "
                "Kontakte zu Unternehmen und koennen den Einstieg in Praktika und den Beruf erleichtern. "
                "Zudem entstehen Einblicke in typische Arbeitsablaeufe und Erwartungshaltungen.",
                self.cat_keep,
                self.per_self,
                src_hamburg,
            ),
            (
                "Unstrukturierte externe Beitraege ohne Vorbereitung",
                "Unstrukturierte externe Beitraege ohne didaktische Vorbereitung koennen die Lehrziele "
                "unterlaufen und die Qualitaet der Lehre beeintraechtigen. "
                "Ohne klare Lernziele entsteht Unklarheit, welche Kompetenzen entwickelt werden sollen.",
                self.cat_drop,
                self.per_self,
                src_che,
            ),
            (
                "Fehlende Nachbereitung externer Vortraege",
                "Ohne systematische Nachbereitung bleiben die Lernwirkungen externer Vortraege gering "
                "und verfehlen die angestrebten Lernziele. "
                "Erst Reflexion und Uebertragung auf Kursinhalte sichern den nachhaltigen Nutzen.",
                self.cat_drop,
                self.per_peers,
                src_che,
            ),
            (
                "Werbeorientierte Industrievortraege ohne Mehrwert",
                "Werbeorientierte Industrievortraege bieten haeufig keinen fachlich belastbaren Mehrwert "
                "und verfehlen damit die Erwartungen an qualitaetsgesicherte Lehre. "
                "Sie koennen zudem die Aufmerksamkeit von fachlichen Lernzielen ablenken.",
                self.cat_drop,
                self.per_peers,
                src_che,
            ),
            (
                "Zufaellige Auswahl externer Referent:innen",
                "Eine zufaellige Auswahl externer Referentinnen und Referenten fuehrt zu inkonsistenter "
                "Qualitaet und erschwert eine systematische Qualitaetssicherung. "
                "Eine abgestimmte Auswahl wuerde Inhalte zielgerichteter auf das Curriculum beziehen.",
                self.cat_drop,
                self.per_self,
                src_che,
            ),
            (
                "Forschungsnahe Projektarbeiten staerken wissenschaftliches Denken",
                "Forschungsnahe Projektarbeiten staerken wissenschaftliches Denken, indem "
                "Studierende methodisches Arbeiten und kritische Reflexion im Kontext aktueller Forschung "
                "einueben. Dies foerdert ein tieferes Verstaendnis von Fragestellungen, Methoden und Grenzen.",
                self.cat_try,
                self.per_research,
                src_tu_berlin,
            ),
            (
                "Einbindung aktueller Forschungsthemen in die Lehre",
                "Die Einbindung aktueller Forschungsthemen in die Lehre spiegelt den aktuellen Stand "
                "des Fachgebiets wider und erhoeht die Forschungsnaehe des Curriculums. "
                "Sie macht sichtbar, welche Fragen offen sind und wo neues Wissen entsteht.",
                self.cat_try,
                self.per_research,
                src_tu_berlin,
            ),
            (
                "Gastvortraege von Forschenden aus Hochschulen",
                "Gastvortraege von Forschenden aus Hochschulen ermoeglichen Einblicke in laufende "
                "Forschungsarbeiten und foerdern den wissenschaftlichen Austausch. "
                "Sie ergaenzen die Lehre durch aktuelle Perspektiven und methodische Tiefe.",
                self.cat_try,
                self.per_research,
                src_tu_berlin,
            ),
            (
                "Staerkere Verbindung von Forschung und Lehre",
                "Eine staerkere Verbindung von Forschung und Lehre erhoeht den Anspruch des Curriculums "
                "und die wissenschaftliche Tiefe der Ausbildung. "
                "Studierende lernen, Erkenntnisse zu bewerten und systematisch zu begruenden.",
                self.cat_try,
                self.per_research,
                src_tu_berlin,
            ),
            (
                "Kooperationen mit NGOs erweitern gesellschaftliche Perspektiven",
                "Kooperationen mit NGOs bringen gesellschaftliche Problemstellungen in die Lehre ein "
                "und erweitern die Perspektive ueber rein technische Aspekte hinaus. "
                "Dadurch werden ethische, soziale und organisationale Folgen staerker sichtbar.",
                self.cat_try,
                self.per_research,
                src_tu_dortmund,
            ),
            (
                "Gesellschaftlich relevante Projekte foerdern Verantwortungsbewusstsein",
                "Gesellschaftlich relevante Projekte in Kooperation mit NGOs foerdern ein reflektiertes "
                "Verantwortungsbewusstsein fuer die Auswirkungen informatischer Systeme. "
                "Sie verdeutlichen, dass technische Entscheidungen stets gesellschaftliche Effekte haben.",
                self.cat_try,
                self.per_research,
                src_tu_dortmund,
            ),
            (
                "Externe Projekte mit oeffentlicher Verwaltung",
                "Externe Projekte mit oeffentlicher Verwaltung zeigen Anforderungen und "
                "Rahmenbedingungen oeffentlicher IT. "
                "Sie machen sichtbar, welche rechtlichen und organisatorischen Vorgaben umzusetzen sind.",
                self.cat_try,
                self.per_research,
                src_tu_dortmund,
            ),
            (
                "Sozialer Impact der Informatik wird sichtbarer",
                "Durch Kooperationen mit NGOs und externen Partnern wird der soziale Impact der Informatik "
                "sichtbarer und in der Lehre nachvollziehbar verankert. "
                "Dies hilft, technische Loesungen in ihren gesellschaftlichen Kontext einzuordnen.",
                self.cat_try,
                self.per_research,
                src_tu_dortmund,
            ),
            (
                "Praxisnahe Perspektiven ergaenzen theoretische Inhalte",
                "Praxisnahe Perspektiven aus Gastvortraegen ergaenzen theoretische Inhalte durch "
                "Erfahrungen aus dem Berufsalltag und der Projektpraxis. "
                "Sie helfen, abstrakte Konzepte mit konkreten Anwendungsfaellen zu verbinden.",
                self.cat_keep,
                self.per_self,
                src_tum,
            ),
            (
                "Externe Inputs foerdern kritisches Denken",
                "Externe Inputs durch Gastvortraege foerdern Diskussionen und schaerfen kritisches "
                "Denken durch den Vergleich verschiedener Praxisansaetze. "
                "So entstehen differenzierte Bewertungen von Methoden, Tools und Entscheidungen.",
                self.cat_keep,
                self.per_peers,
                src_tum,
            ),
            (
                "Mehr Vielfalt durch unterschiedliche externe Akteure",
                "Unterschiedliche externe Akteure erhoehen die Vielfalt der Blickwinkel in der Lehre. "
                "Dies erweitert das Spektrum an Meinungen, Branchen und technischen Loesungen.",
                self.cat_try,
                self.per_research,
                src_tu_dortmund,
            ),
            (
                "Externe Perspektiven sollten curricular verankert sein",
                "Externe Perspektiven sollten curricular verankert sein, um die Qualitaet der Lehre "
                "kontinuierlich zu sichern. "
                "Eine feste Verankerung sorgt fuer Planbarkeit, Vergleichbarkeit und klare Lernziele.",
                self.cat_try,
                self.per_self,
                src_che,
            ),
        ]

        keep_positions = iter([
            (80, 40), (150, 40), (220, 40),
            (80, 80), (150, 80), (220, 80),
        ])
        drop_positions = iter([
            (90, 120), (150, 120), (210, 120), (270, 120),
        ])
        try_positions = iter([
            (70, 200), (130, 200), (190, 200), (250, 200), (310, 200),
            (70, 240), (130, 240), (190, 240), (250, 240), (310, 240),
        ])

        meta_nodes = [
            self.topic_node,
            self.cat_keep,
            self.cat_drop,
            self.cat_try,
            self.per_self,
            self.per_peers,
            self.per_research,
        ]
        for node in meta_nodes + self.sources:
            graph.add_new_node_to_graph(node)

        for title, description_text, category, perspective, source in knowledge_nodes:
            description = (
                f"Inhalt:\n{description_text}\n\n"
                f"Kategorie: {category.titel}\n"
                f"Perspektive: {perspective.titel}\n"
                f"Quelle: {source.titel}"
            )
            if category == self.cat_keep:
                pos_x, pos_y = next(keep_positions)
            elif category == self.cat_drop:
                pos_x, pos_y = next(drop_positions)
            else:
                pos_x, pos_y = next(try_positions)

            knowledge_node = NodeKnowledge(description, title, pos_x, pos_y)
            knowledge_node.author = "Wissen"
            graph.add_new_node_to_graph(knowledge_node)

            knowledge_node.connect(self.topic_node)
            knowledge_node.connect(category)
            knowledge_node.connect(perspective)
            knowledge_node.connect(source)

    def _create_online_source(self, title, author, website, url, x, y):
        source = NodeSourceOnline(
            title,
            author,
            "n.d.",
            website,
            url,
            "n.a.",
            comment="",
            x=x,
            y=y,
        )
        source.author = "Quelle"
        return source
