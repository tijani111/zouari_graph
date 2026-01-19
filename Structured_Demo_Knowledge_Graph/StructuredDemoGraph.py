from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from GraphModel.Nodes.NodeSourceOnline import NodeSourceOnline


class StructuredDemoGraph:
    def __init__(self, graph: Graph):
        self.create_structured_demo_graph(graph)

    def create_structured_demo_graph(self, graph: Graph):
        topic_node = NodeKnowledge(
            "Topic for this section of the knowledge graph.",
            "Einbindung externer Perspektiven"
        )
        topic_node.author = "Meta"

        cat_keep = NodeKnowledge("Evaluation category: KEEP", "KEEP")
        cat_drop = NodeKnowledge("Evaluation category: DROP", "DROP")
        cat_try = NodeKnowledge("Evaluation category: TRY", "TRY")
        for node in (cat_keep, cat_drop, cat_try):
            node.author = "Meta"

        per_self = NodeKnowledge("Perspective: Eigene Erfahrung", "Eigene Erfahrung")
        per_peers = NodeKnowledge("Perspective: Mitstudierende", "Mitstudierende")
        per_research = NodeKnowledge("Perspective: Recherche", "Recherche")
        for node in (per_self, per_peers, per_research):
            node.author = "Meta"

        src_tum = self._create_online_source(
            "Gastvortraege Informatik",
            "TU Muenchen",
            "in.tum.de",
            "https://www.in.tum.de/die-fakultaet/news-events/gastvortraege/"
        )
        src_hamburg = self._create_online_source(
            "Projektmodule Informatik",
            "Universitaet Hamburg",
            "inf.uni-hamburg.de",
            "https://www.inf.uni-hamburg.de/studies/bachelor.html"
        )
        src_che = self._create_online_source(
            "Lehr- und Praxisbezug (CHE Hochschulranking)",
            "CHE Hochschulranking",
            "ranking.zeit.de",
            "https://ranking.zeit.de/che/de/studiengang/43171"
        )
        src_tu_dortmund = self._create_online_source(
            "Kooperationen mit NGOs",
            "TU Dortmund",
            "informatik.tu-dortmund.de",
            "https://informatik.tu-dortmund.de/studium/kooperationen-ngos/"
        )
        src_tu_berlin = self._create_online_source(
            "Studienprojektmodule Informatik",
            "TU Berlin",
            "tu.berlin",
            "https://www.tu.berlin/informatik/studium/lehrveranstaltungen/"
        )

        knowledge_nodes = [
            (
                "Industrienahe Gastvortraege foerdern Praxisverstaendnis",
                "Industriebezogene Gastvortraege stellen Praxisfaelle und Berufsbilder vor und "
                "unterstuetzen damit ein besseres Verstaendnis der Anforderungen in der beruflichen Praxis.",
                cat_keep,
                per_self,
                src_tum,
            ),
            (
                "Externe Praxisberichte erhoehen Motivation",
                "Praxisberichte externer Referentinnen und Referenten vermitteln greifbare "
                "Anwendungsbeispiele und koennen die Motivation durch nachvollziehbare Berufswege staerken.",
                cat_keep,
                per_peers,
                src_tum,
            ),
            (
                "Praxisprojekte mit externen Partnern sind lernwirksam",
                "Projektmodule mit externen Partnern verknuepfen Studieninhalte "
                "mit realen Aufgabenstellungen und foerdern anwendungsbezogene Kompetenzen.",
                cat_keep,
                per_peers,
                src_hamburg,
            ),
            (
                "Kooperationen mit Unternehmen erleichtern Berufseinstieg",
                "Kooperationen im Rahmen von Projektmodulen ermoeglichen fruehe "
                "Kontakte zu Unternehmen und koennen den Einstieg in Praktika und den Beruf erleichtern.",
                cat_keep,
                per_self,
                src_hamburg,
            ),
            (
                "Unstrukturierte externe Beitraege ohne Vorbereitung",
                "Unstrukturierte externe Beitraege ohne didaktische Vorbereitung koennen die Lehrziele "
                "unterlaufen und die Qualitaet der Lehre beeintraechtigen.",
                cat_drop,
                per_self,
                src_che,
            ),
            (
                "Fehlende Nachbereitung externer Vortraege",
                "Ohne systematische Nachbereitung bleiben die Lernwirkungen externer Vortraege gering "
                "und verfehlen die angestrebten Lernziele.",
                cat_drop,
                per_peers,
                src_che,
            ),
            (
                "Werbeorientierte Industrievortraege ohne Mehrwert",
                "Werbeorientierte Industrievortraege bieten haeufig keinen fachlich belastbaren Mehrwert "
                "und verfehlen damit die Erwartungen an qualitaetsgesicherte Lehre.",
                cat_drop,
                per_peers,
                src_che,
            ),
            (
                "Zufaellige Auswahl externer Referent:innen",
                "Eine zufaellige Auswahl externer Referentinnen und Referenten fuehrt zu inkonsistenter "
                "Qualitaet und erschwert eine systematische Qualitaetssicherung.",
                cat_drop,
                per_self,
                src_che,
            ),
            (
                "Forschungsnahe Projektarbeiten staerken wissenschaftliches Denken",
                "Forschungsnahe Projektarbeiten staerken wissenschaftliches Denken, indem "
                "Studierende methodisches Arbeiten und kritische Reflexion im Kontext aktueller Forschung "
                "einueben.",
                cat_try,
                per_research,
                src_tu_berlin,
            ),
            (
                "Einbindung aktueller Forschungsthemen in die Lehre",
                "Die Einbindung aktueller Forschungsthemen in die Lehre spiegelt den aktuellen Stand "
                "des Fachgebiets wider und erhoeht die Forschungsnaehe des Curriculums.",
                cat_try,
                per_research,
                src_tu_berlin,
            ),
            (
                "Gastvortraege von Forschenden aus Hochschulen",
                "Gastvortraege von Forschenden aus Hochschulen ermoeglichen Einblicke in laufende "
                "Forschungsarbeiten und foerdern den wissenschaftlichen Austausch.",
                cat_try,
                per_research,
                src_tu_berlin,
            ),
            (
                "Staerkere Verbindung von Forschung und Lehre",
                "Eine staerkere Verbindung von Forschung und Lehre erhoeht den Anspruch des Curriculums "
                "und die wissenschaftliche Tiefe der Ausbildung.",
                cat_try,
                per_research,
                src_tu_berlin,
            ),
            (
                "Kooperationen mit NGOs erweitern gesellschaftliche Perspektiven",
                "Kooperationen mit NGOs bringen gesellschaftliche Problemstellungen in die Lehre ein "
                "und erweitern die Perspektive ueber rein technische Aspekte hinaus.",
                cat_try,
                per_research,
                src_tu_dortmund,
            ),
            (
                "Gesellschaftlich relevante Projekte foerdern Verantwortungsbewusstsein",
                "Gesellschaftlich relevante Projekte in Kooperation mit NGOs foerdern ein reflektiertes "
                "Verantwortungsbewusstsein fuer die Auswirkungen informatischer Systeme.",
                cat_try,
                per_research,
                src_tu_dortmund,
            ),
            (
                "Externe Projekte mit oeffentlicher Verwaltung",
                "Externe Projekte mit oeffentlicher Verwaltung zeigen Anforderungen und "
                "Rahmenbedingungen oeffentlicher IT.",
                cat_try,
                per_research,
                src_tu_dortmund,
            ),
            (
                "Sozialer Impact der Informatik wird sichtbarer",
                "Durch Kooperationen mit NGOs und externen Partnern wird der soziale Impact der Informatik "
                "sichtbarer und in der Lehre nachvollziehbar verankert.",
                cat_try,
                per_research,
                src_tu_dortmund,
            ),
            (
                "Praxisnahe Perspektiven ergaenzen theoretische Inhalte",
                "Praxisnahe Perspektiven aus Gastvortraegen ergaenzen theoretische Inhalte durch "
                "Erfahrungen aus dem Berufsalltag und der Projektpraxis.",
                cat_keep,
                per_self,
                src_tum,
            ),
            (
                "Externe Inputs foerdern kritisches Denken",
                "Externe Inputs durch Gastvortraege foerdern Diskussionen und schaerfen kritisches "
                "Denken durch den Vergleich verschiedener Praxisansaetze.",
                cat_keep,
                per_peers,
                src_tum,
            ),
            (
                "Mehr Vielfalt durch unterschiedliche externe Akteure",
                "Unterschiedliche externe Akteure erhoehen die Vielfalt der Blickwinkel in der Lehre.",
                cat_try,
                per_research,
                src_tu_dortmund,
            ),
            (
                "Externe Perspektiven sollten curricular verankert sein",
                "Externe Perspektiven sollten curricular verankert sein, um die Qualitaet der Lehre "
                "kontinuierlich zu sichern.",
                cat_try,
                per_self,
                src_che,
            ),
        ]

        meta_nodes = [topic_node, cat_keep, cat_drop, cat_try, per_self, per_peers, per_research]
        source_nodes = [src_tum, src_hamburg, src_che, src_tu_dortmund, src_tu_berlin]

        for node in meta_nodes + source_nodes:
            graph.add_new_node_to_graph(node)

        for title, description_text, category, perspective, source in knowledge_nodes:
            description = (
                f"Inhalt:\n{description_text}\n\n"
                f"Kategorie: {category.titel}\n"
                f"Perspektive: {perspective.titel}"
            )
            knowledge_node = NodeKnowledge(description, title)
            knowledge_node.author = "Knowledge"
            graph.add_new_node_to_graph(knowledge_node)

            knowledge_node.connect(topic_node)
            knowledge_node.connect(category)
            knowledge_node.connect(perspective)
            knowledge_node.connect(source)

    def _create_online_source(self, title, author, website, url):
        source = NodeSourceOnline(
            title,
            author,
            "n.d.",
            website,
            url,
            "n.a."
        )
        source.author = "Source"
        return source
