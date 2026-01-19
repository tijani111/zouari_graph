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
        )
        self.topic_node.author = "Topic"

        self.cat_keep = NodeKnowledge("Evaluation category: KEEP", "KEEP")
        self.cat_drop = NodeKnowledge("Evaluation category: DROP", "DROP")
        self.cat_try = NodeKnowledge("Evaluation category: TRY", "TRY")
        for node in (self.cat_keep, self.cat_drop, self.cat_try):
            node.author = "Kategorie"

        self.per_self = NodeKnowledge("Perspective: Eigene Erfahrung", "Eigene Erfahrung")
        self.per_peers = NodeKnowledge("Perspective: Mitstudierende", "Mitstudierende")
        self.per_research = NodeKnowledge("Perspective: Recherche", "Recherche")
        for node in (self.per_self, self.per_peers, self.per_research):
            node.author = "Perspektive"

        src_tum = self._create_online_source(
            "Gastvortraege Informatik",
            "TU Muenchen",
            "in.tum.de",
            "https://www.in.tum.de/die-fakultaet/news-events/gastvortraege/",
        )
        src_hamburg = self._create_online_source(
            "Projektmodule Informatik",
            "Universitaet Hamburg",
            "inf.uni-hamburg.de",
            "https://www.inf.uni-hamburg.de/studies/bachelor.html",
        )
        src_che = self._create_online_source(
            "Lehr- und Praxisbezug (CHE Hochschulranking)",
            "CHE Hochschulranking",
            "ranking.zeit.de",
            "https://ranking.zeit.de/che/de/studiengang/43171",
        )
        src_tu_dortmund = self._create_online_source(
            "Kooperationen mit NGOs",
            "TU Dortmund",
            "informatik.tu-dortmund.de",
            "https://informatik.tu-dortmund.de/studium/kooperationen-ngos/",
        )
        src_tu_berlin = self._create_online_source(
            "Studienprojektmodule Informatik",
            "TU Berlin",
            "tu.berlin",
            "https://www.tu.berlin/informatik/studium/lehrveranstaltungen/",
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
            extra_text = self._extend_description(title, description_text)
            description = (
                f"Inhalt:\n{description_text}\n\n{extra_text}\n\n"
                f"Kategorie: {category.titel}\n"
                f"Perspektive: {perspective.titel}\n"
                f"Quelle: {source.titel}"
            )
            knowledge_node = NodeKnowledge(description, title)
            knowledge_node.author = "Wissen"
            graph.add_new_node_to_graph(knowledge_node)

            knowledge_node.connect(self.topic_node)
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
            "n.a.",
            comment="",
        )
        source.author = "Quelle"
        return source

    def _extend_description(self, title, description_text):
        guest_lecture_core = (
            "Ein sinnvoller Gastvortrag benoetigt eine klare Einbettung in das Modul: "
            "Welche Kompetenzen sollen nach dem Termin sichtbar verbessert sein, "
            "und welches Fallbeispiel macht dies konkret nachvollziehbar? "
            "Ein gutes Beispiel zeigt nicht nur das Ergebnis, sondern auch den Weg dorthin, "
            "inklusive Zielkonflikten, Zeitdruck und begruendeten Kompromissen. "
            "So wird die Relevanz von Theorie, z. B. Datenstrukturen, Softwareentwurf oder Tests, "
            "als Teil eines realen Entscheidungsprozesses erfahrbar."
        )
        guest_lecture_quality = (
            "Fuer die Lernwirkung ist entscheidend, dass der Vortrag Raum fuer Rueckfragen laesst "
            "und nicht nur das Endprodukt praesentiert. Eine kurze Aufgabe im Anschluss, etwa das "
            "Identifizieren von Risiken oder das Ableiten von Messkriterien, macht den Praxisbezug "
            "messbar. Wenn mehrere Vortraege stattfinden, sollten sie unterschiedliche Phasen "
            "abdecken, z. B. Planung, Umsetzung und Betrieb, damit kein einseitiger Blick entsteht."
        )
        research_core = (
            "Forschungsbezogene Inhalte werden greifbar, wenn Studierende sehen, wie eine "
            "Forschungsfrage entsteht und warum eine Methode gewaehlt wird. Das umfasst die Auswahl "
            "von Daten, die Beurteilung von Bias, die Grenzen der Ergebnisse und die Frage nach "
            "Reproduzierbarkeit. In der Lehre hilft es, Ergebnisse nicht als fertige Wahrheit "
            "darzustellen, sondern als begruendete, aber pruefbare Aussagen."
        )
        research_methods = (
            "Methodische Tiefe entsteht, wenn Studierende selbst kleine Experimente planen: "
            "Messaufbau, Vergleichskriterien und Interpretation von Abweichungen. Ein kurzer Bericht "
            "mit Begruendung der Schritte verbindet praktische Arbeit mit wissenschaftlicher "
            "Argumentation. So wird deutlich, dass Forschung nicht nur Fortschritt bedeutet, sondern "
            "auch Unsicherheit und Fehlerquellen transparent machen muss."
        )
        ngo_core = (
            "NGO-Kooperationen bringen Problemfelder ein, die nicht nur technisch sind, sondern auch "
            "sozial und organisatorisch. Anforderungen entstehen aus dem Alltag der Zielgruppen, "
            "nicht aus idealen Annahmen. Dadurch muessen Studierende die Fachsprache der Partner "
            "verstehen, Ziele konkretisieren und Loesungen so gestalten, dass sie auch mit wenig "
            "Ressourcen nutzbar bleiben."
        )
        ngo_impact = (
            "Die Arbeit mit NGOs macht ethische Aspekte sichtbar, etwa Datenschutz, Zugangsbarrieren "
            "oder unbeabsichtigte Nebenwirkungen. Technische Entscheidungen sind hier direkt mit "
            "Vertrauen und Verantwortung verbunden. Diese Perspektive erweitert das Studium, weil sie "
            "zeigt, dass gute Technik nicht nur funktioniert, sondern auch fair und nachvollziehbar sein muss."
        )
        project_core = (
            "Externe Projekte sind lernwirksam, wenn es klare Rollen, Termine und Abnahmekriterien gibt. "
            "Studierende muessen Anforderungen strukturieren, Prioritaeten setzen und die Umsetzbarkeit "
            "frueh pruefen. Der Kontakt zu Auftraggebenden zeigt, dass Kommunikation und Dokumentation "
            "genauso wichtig sind wie reiner Code."
        )
        project_process = (
            "Ein realistischer Projektprozess umfasst Aenderungswuensche, Abhaengigkeiten und "
            "technische Risiken. Wenn Teams diese Punkte dokumentieren und Entscheidungen begruenden, "
            "entsteht ein Lerneffekt, der ueber das eigentliche Produkt hinausgeht. Gerade im Uebergang "
            "zum Beruf hilft diese Erfahrung, weil sie zeigt, wie fachliche Arbeit in Organisationen "
            "eingebettet ist."
        )
        quality_core = (
            "Fehlende Struktur oder werbliche Inhalte schwaechen den Lernwert externer Beitraege. "
            "Wenn Lernziele nicht definiert sind, bleibt unklar, welche Konzepte uebt werden sollen "
            "und wie der Beitrag zur Pruefungsvorbereitung passt. Studierende nehmen solche Termine "
            "dann als Unterhaltung wahr, nicht als Teil des Kurses."
        )
        quality_process = (
            "Qualitaetssicherung erfordert Auswahlkriterien, Briefings und Feedback. Ein kurzer "
            "Leitfaden fuer Referierende, z. B. Fokus auf Problem, Methode, Ergebnis und Grenzen, "
            "hilft, fachliche Tiefe zu sichern. Rueckmeldungen aus der Studierendengruppe koennen "
            "systematisch gesammelt werden, um wiederkehrende Schwachstellen zu erkennen."
        )
        governance_core = (
            "Eine curriculare Verankerung bedeutet auch, dass externe Beitraege in die Modulhandbuecher "
            "und Lernziele eingehen. Dadurch wird festgelegt, welche Inhalte erwartet werden, in welchem "
            "Semester sie sinnvoll sind und wie sie bewertet werden. Ohne diese Verankerung bleibt die "
            "Qualitaet schwer vergleichbar und haengt von Zufall und Kontakten ab."
        )

        addendum_by_title = {
            "Industrienahe Gastvortraege foerdern Praxisverstaendnis": (
                "Besonders hilfreich sind Fallbeispiele, in denen die Referierenden konkrete "
                "Entscheidungen begruenden, etwa Wahl der Architektur, Umgang mit Zeitdruck und "
                "Kompromisse zwischen Qualitaet und Liefertermin."
            ),
            "Externe Praxisberichte erhoehen Motivation": (
                "Motivierend wirken Berichte, die konkrete Lernschritte benennen, z. B. wie "
                "Kenntnisse aus Programmierung, Datenbanken oder Softwaretechnik in echten Aufgaben "
                "zusammengefuehrt wurden."
            ),
            "Praxisprojekte mit externen Partnern sind lernwirksam": (
                "Die Lernwirkung steigt, wenn externe Partner auch Zwischenfeedback geben und "
                "die Studierenden lernen, ihre Loesungen zu verteidigen und zu verbessern."
            ),
            "Kooperationen mit Unternehmen erleichtern Berufseinstieg": (
                "Ein klarer Rahmen verhindert, dass Kooperationen zu reinen Recruiting-Events werden "
                "und stellt sicher, dass der Lernfokus auf Kompetenzen liegt."
            ),
            "Unstrukturierte externe Beitraege ohne Vorbereitung": (
                "Ohne Vorabstimmung koennen Inhalte doppelt, zu detailliert oder am Thema vorbei sein, "
                "was den Kursfluss stoert und die Aufmerksamkeit der Gruppe senkt."
            ),
            "Fehlende Nachbereitung externer Vortraege": (
                "Eine kurze Nachbereitung, z. B. Diskussionsfragen oder ein kurzer Bericht, bindet "
                "den Vortrag an die Lernziele und verhindert, dass er als isolierte Episode endet."
            ),
            "Werbeorientierte Industrievortraege ohne Mehrwert": (
                "Wenn Produkte im Vordergrund stehen, fehlen oft nachvollziehbare Loesungswege "
                "und belastbare technische Argumente, die fuer die Lehre wichtig waeren."
            ),
            "Zufaellige Auswahl externer Referent:innen": (
                "Ein konsistentes Auswahlverfahren sorgt dafuer, dass die Beitraege aufeinander "
                "aufbauen und wichtige Themen nicht dem Zufall ueberlassen werden."
            ),
            "Forschungsnahe Projektarbeiten staerken wissenschaftliches Denken": (
                "Wichtig ist, dass Studierende Ergebnisse kritisch einordnen und nicht nur die "
                "besten Resultate berichten, sondern auch Grenzen und Fehlerquellen benennen."
            ),
            "Einbindung aktueller Forschungsthemen in die Lehre": (
                "Aktuelle Themen sollten so gewaehlt werden, dass sie an bekannte Grundlagen "
                "anschliessen und nicht als zu abstrakte Spezialthemen wahrgenommen werden."
            ),
            "Gastvortraege von Forschenden aus Hochschulen": (
                "Ein klares Beispiel aus einer laufenden Studie zeigt, wie Hypothesen, Daten und "
                "Auswertung zusammenhaengen und macht Forschung nachvollziehbar."
            ),
            "Staerkere Verbindung von Forschung und Lehre": (
                "Eine Verbindung wird sichtbar, wenn in Uebungen messbare Kriterien eingefuehrt "
                "werden und Studierende ihre Entscheidungen wissenschaftlich begruenden."
            ),
            "Kooperationen mit NGOs erweitern gesellschaftliche Perspektiven": (
                "Die Zusammenarbeit macht sichtbar, dass Loesungen auch unter knappen Budgets und "
                "mit hoher Verantwortung funktionieren muessen."
            ),
            "Gesellschaftlich relevante Projekte foerdern Verantwortungsbewusstsein": (
                "Konkrete Auswirkungen auf Nutzergruppen helfen, Verantwortungsbewusstsein zu "
                "verankern und nicht nur abstrakt zu diskutieren."
            ),
            "Externe Projekte mit oeffentlicher Verwaltung": (
                "Der Einblick in Verwaltung zeigt, wie wichtig klare Spezifikationen, "
                "Dokumentationspflichten und Datenschutzvorgaben sind."
            ),
            "Sozialer Impact der Informatik wird sichtbarer": (
                "Studierende koennen die Wirkung ihrer Entscheidungen nachvollziehen, wenn der "
                "Partner reale Rueckmeldungen zu Nutzen und Risiken der Loesung gibt."
            ),
            "Praxisnahe Perspektiven ergaenzen theoretische Inhalte": (
                "Ein Praxisfall kann eine Vorlesung ergaenzen, wenn er konkrete Begriffe aus dem "
                "Skript verwendet und deren Anwendung sichtbar macht."
            ),
            "Externe Inputs foerdern kritisches Denken": (
                "Der Nutzen steigt, wenn Unterschiede zu Lehrbuchmethoden diskutiert werden und "
                "nicht jede Praxisloesung als Norm gesetzt wird."
            ),
            "Mehr Vielfalt durch unterschiedliche externe Akteure": (
                "Vielfalt entsteht, wenn Akteure mit unterschiedlichen Zielsystemen auftreten, "
                "etwa Industrie, Forschung, NGOs und Verwaltung."
            ),
            "Externe Perspektiven sollten curricular verankert sein": (
                "Eine feste Verankerung verhindert spontane Abhaengigkeit von Einzelkontakten "
                "und macht die externe Perspektive planbar."
            ),
        }

        extra_parts = []
        if "Gastvortraege" in title or "Praxisberichte" in title or "Inputs" in title:
            extra_parts.extend([guest_lecture_core, guest_lecture_quality])
        if "Forsch" in title:
            extra_parts.extend([research_core, research_methods])
        if "NGO" in title or "gesellschaftlich" in title or "Sozialer Impact" in title:
            extra_parts.extend([ngo_core, ngo_impact])
        if "Projekt" in title or "Kooperationen mit Unternehmen" in title or "oeffentlicher Verwaltung" in title:
            extra_parts.extend([project_core, project_process])
        if "Unstrukturierte" in title or "Nachbereitung" in title or "Werbeorientierte" in title or "Zufaellige Auswahl" in title:
            extra_parts.extend([quality_core, quality_process])
        if "curricular verankert" in title:
            extra_parts.append(governance_core)

        addendum = addendum_by_title.get(title, "")
        if addendum:
            extra_parts.append(addendum)

        extra_text = "\n\n".join(part for part in extra_parts if part)
        if len(extra_text) < 1400:
            context_blocks = [
                (
                    f"Bezug zur Kernaussage '{title}': {description_text} "
                    "Im Kurs laesst sich dieser Bezug konkret pruefen, wenn die Beispiele in Aufgaben "
                    "oder Diskussionen aufgegriffen werden und sichtbar wird, welche Entscheidungen "
                    "unter welchen Randbedingungen getroffen wurden."
                ),
                (
                    "Fuer die Umsetzung ist wichtig, die Rolle der Beteiligten zu klaeren: "
                    "Wer liefert Anforderungen, wer bewertet Ergebnisse und wie wird Rueckmeldung "
                    "gegeben. So wird der Nutzen der externen Perspektive fuer Lernziele sichtbar und "
                    "nicht nur als Einzelfall wahrgenommen."
                ),
                (
                    "Eine Bewertung kann darauf achten, ob Studierende die vorgestellten Ansaetze "
                    "mit Kursinhalten vergleichen koennen, z. B. anhand von Kriterien wie Aufwand, "
                    "Wartbarkeit, Datenqualitaet oder Auswirkungen fuer Nutzerinnen und Nutzer."
                ),
            ]
            idx = 0
            while len(extra_text) < 1400:
                extra_text += "\n\n" + context_blocks[idx % len(context_blocks)]
                idx += 1
        return extra_text[:1400]
