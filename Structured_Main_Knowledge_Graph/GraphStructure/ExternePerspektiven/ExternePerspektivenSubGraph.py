from GraphModel.Graph import Graph
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge
from GraphModel.Nodes.NodeSourceOnline import NodeSourceOnline
from Structured_Main_Knowledge_Graph.GraphContent.ExternePerspektiven import (
    TOPIC_TITEL,
    TOPIC_CONTENT,
    CATEGORIES,
    PERSPECTIVES,
    SOURCES,
    NODES,
)


class ExternePerspektivenSubGraph:
    def __init__(self, graph: Graph):
        self.topic_node = None
        self.categories = {}
        self.perspectives = {}
        self.sources = {}
        self.build_graph(graph)

    def build_graph(self, graph: Graph):
        self.topic_node = NodeKnowledge(description=TOPIC_CONTENT, titel=TOPIC_TITEL)
        self.topic_node.author = "Topic"

        for key, label in CATEGORIES.items():
            node = NodeKnowledge(description=label, titel=label.split(": ")[-1])
            node.author = "Kategorie"
            self.categories[key] = node

        for key, label in PERSPECTIVES.items():
            node = NodeKnowledge(description=label, titel=label.split(": ")[-1])
            node.author = "Perspektive"
            self.perspectives[key] = node

        for key, src in SOURCES.items():
            node = NodeSourceOnline(
                titel_of_the_document=src["title"],
                source_author=src["author"],
                year_of_publication="n.d.",
                titel_of_the_website=src["website"],
                URL=src["url"],
                date_of_access="n.a.",
                comment="",
            )
            node.author = "Quelle"
            self.sources[key] = node

        graph.add_new_node_to_graph(self.topic_node)
        for node in self.categories.values():
            graph.add_new_node_to_graph(node)
        for node in self.perspectives.values():
            graph.add_new_node_to_graph(node)
        for node in self.sources.values():
            graph.add_new_node_to_graph(node)

        for entry in NODES:
            category = self.categories[entry["category"]]
            perspective = self.perspectives[entry["perspective"]]
            source = self.sources[entry["source"]]

            extra_text = self._extend_description(entry["title"], entry["content"])
            description = (
                f"Inhalt:\n{entry['content']}\n\n{extra_text}\n\n"
                f"Kategorie: {category.titel}\n"
                f"Perspektive: {perspective.titel}\n"
                f"Quelle: {source.titel}"
            )
            knowledge_node = NodeKnowledge(description=description, titel=entry["title"])
            knowledge_node.author = "Wissen"
            graph.add_new_node_to_graph(knowledge_node)

            knowledge_node.connect(self.topic_node)
            knowledge_node.connect(category)
            knowledge_node.connect(perspective)
            knowledge_node.connect(source)

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
