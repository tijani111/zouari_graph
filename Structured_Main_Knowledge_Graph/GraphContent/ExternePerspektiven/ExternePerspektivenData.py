TOPIC_TITEL = "Einbindung externer Perspektiven"
TOPIC_CONTENT = "Topic for this section of the knowledge graph."

CATEGORIES = {
    "keep": "Evaluation category: KEEP",
    "drop": "Evaluation category: DROP",
    "try": "Evaluation category: TRY",
}

PERSPECTIVES = {
    "self": "Perspective: Eigene Erfahrung",
    "peers": "Perspective: Mitstudierende",
    "research": "Perspective: Recherche",
}

SOURCES = {
    "tum": {
        "title": "Gastvortraege Informatik",
        "author": "TU Muenchen",
        "website": "in.tum.de",
        "url": "https://www.in.tum.de/die-fakultaet/news-events/gastvortraege/",
    },
    "hamburg": {
        "title": "Projektmodule Informatik",
        "author": "Universitaet Hamburg",
        "website": "inf.uni-hamburg.de",
        "url": "https://www.inf.uni-hamburg.de/studies/bachelor.html",
    },
    "che": {
        "title": "Lehr- und Praxisbezug (CHE Hochschulranking)",
        "author": "CHE Hochschulranking",
        "website": "ranking.zeit.de",
        "url": "https://ranking.zeit.de/che/de/studiengang/43171",
    },
    "tu_dortmund": {
        "title": "Kooperationen mit NGOs",
        "author": "TU Dortmund",
        "website": "informatik.tu-dortmund.de",
        "url": "https://informatik.tu-dortmund.de/studium/kooperationen-ngos/",
    },
    "tu_berlin": {
        "title": "Studienprojektmodule Informatik",
        "author": "TU Berlin",
        "website": "tu.berlin",
        "url": "https://www.tu.berlin/informatik/studium/lehrveranstaltungen/",
    },
}

NODES = [
    {
        "title": "Industrienahe Gastvortraege foerdern Praxisverstaendnis",
        "content": (
            "Industriebezogene Gastvortraege stellen Praxisfaelle und Berufsbilder vor und "
            "unterstuetzen damit ein besseres Verstaendnis der Anforderungen in der beruflichen Praxis. "
            "Sie machen sichtbar, wie theoretische Inhalte in realen Projekten angewendet werden, "
            "und erhoehen die Anschlussfaehigkeit an die Arbeitswelt."
        ),
        "category": "keep",
        "perspective": "self",
        "source": "tum",
    },
    {
        "title": "Externe Praxisberichte erhoehen Motivation",
        "content": (
            "Praxisberichte externer Referentinnen und Referenten vermitteln greifbare "
            "Anwendungsbeispiele und koennen die Motivation durch nachvollziehbare Berufswege staerken. "
            "Sie helfen, den Nutzen einzelner Module konkret zu verorten und Lernziele besser nachzuvollziehen."
        ),
        "category": "keep",
        "perspective": "peers",
        "source": "tum",
    },
    {
        "title": "Praxisprojekte mit externen Partnern sind lernwirksam",
        "content": (
            "Projektmodule mit externen Partnern verknuepfen Studieninhalte "
            "mit realen Aufgabenstellungen und foerdern anwendungsbezogene Kompetenzen. "
            "Durch konkrete Anforderungen werden Teamarbeit, Planung und fachliche Umsetzung trainiert."
        ),
        "category": "keep",
        "perspective": "peers",
        "source": "hamburg",
    },
    {
        "title": "Kooperationen mit Unternehmen erleichtern Berufseinstieg",
        "content": (
            "Kooperationen im Rahmen von Projektmodulen ermoeglichen fruehe "
            "Kontakte zu Unternehmen und koennen den Einstieg in Praktika und den Beruf erleichtern. "
            "Zudem entstehen Einblicke in typische Arbeitsablaeufe und Erwartungshaltungen."
        ),
        "category": "keep",
        "perspective": "self",
        "source": "hamburg",
    },
    {
        "title": "Unstrukturierte externe Beitraege ohne Vorbereitung",
        "content": (
            "Unstrukturierte externe Beitraege ohne didaktische Vorbereitung koennen die Lehrziele "
            "unterlaufen und die Qualitaet der Lehre beeintraechtigen. "
            "Ohne klare Lernziele entsteht Unklarheit, welche Kompetenzen entwickelt werden sollen."
        ),
        "category": "drop",
        "perspective": "self",
        "source": "che",
    },
    {
        "title": "Fehlende Nachbereitung externer Vortraege",
        "content": (
            "Ohne systematische Nachbereitung bleiben die Lernwirkungen externer Vortraege gering "
            "und verfehlen die angestrebten Lernziele. "
            "Erst Reflexion und Uebertragung auf Kursinhalte sichern den nachhaltigen Nutzen."
        ),
        "category": "drop",
        "perspective": "peers",
        "source": "che",
    },
    {
        "title": "Werbeorientierte Industrievortraege ohne Mehrwert",
        "content": (
            "Werbeorientierte Industrievortraege bieten haeufig keinen fachlich belastbaren Mehrwert "
            "und verfehlen damit die Erwartungen an qualitaetsgesicherte Lehre. "
            "Sie koennen zudem die Aufmerksamkeit von fachlichen Lernzielen ablenken."
        ),
        "category": "drop",
        "perspective": "peers",
        "source": "che",
    },
    {
        "title": "Zufaellige Auswahl externer Referent:innen",
        "content": (
            "Eine zufaellige Auswahl externer Referentinnen und Referenten fuehrt zu inkonsistenter "
            "Qualitaet und erschwert eine systematische Qualitaetssicherung. "
            "Eine abgestimmte Auswahl wuerde Inhalte zielgerichteter auf das Curriculum beziehen."
        ),
        "category": "drop",
        "perspective": "self",
        "source": "che",
    },
    {
        "title": "Forschungsnahe Projektarbeiten staerken wissenschaftliches Denken",
        "content": (
            "Forschungsnahe Projektarbeiten staerken wissenschaftliches Denken, indem "
            "Studierende methodisches Arbeiten und kritische Reflexion im Kontext aktueller Forschung "
            "einueben. Dies foerdert ein tieferes Verstaendnis von Fragestellungen, Methoden und Grenzen."
        ),
        "category": "try",
        "perspective": "research",
        "source": "tu_berlin",
    },
    {
        "title": "Einbindung aktueller Forschungsthemen in die Lehre",
        "content": (
            "Die Einbindung aktueller Forschungsthemen in die Lehre spiegelt den aktuellen Stand "
            "des Fachgebiets wider und erhoeht die Forschungsnaehe des Curriculums. "
            "Sie macht sichtbar, welche Fragen offen sind und wo neues Wissen entsteht."
        ),
        "category": "try",
        "perspective": "research",
        "source": "tu_berlin",
    },
    {
        "title": "Gastvortraege von Forschenden aus Hochschulen",
        "content": (
            "Gastvortraege von Forschenden aus Hochschulen ermoeglichen Einblicke in laufende "
            "Forschungsarbeiten und foerdern den wissenschaftlichen Austausch. "
            "Sie ergaenzen die Lehre durch aktuelle Perspektiven und methodische Tiefe."
        ),
        "category": "try",
        "perspective": "research",
        "source": "tu_berlin",
    },
    {
        "title": "Staerkere Verbindung von Forschung und Lehre",
        "content": (
            "Eine staerkere Verbindung von Forschung und Lehre erhoeht den Anspruch des Curriculums "
            "und die wissenschaftliche Tiefe der Ausbildung. "
            "Studierende lernen, Erkenntnisse zu bewerten und systematisch zu begruenden."
        ),
        "category": "try",
        "perspective": "research",
        "source": "tu_berlin",
    },
    {
        "title": "Kooperationen mit NGOs erweitern gesellschaftliche Perspektiven",
        "content": (
            "Kooperationen mit NGOs bringen gesellschaftliche Problemstellungen in die Lehre ein "
            "und erweitern die Perspektive ueber rein technische Aspekte hinaus. "
            "Dadurch werden ethische, soziale und organisationale Folgen staerker sichtbar."
        ),
        "category": "try",
        "perspective": "research",
        "source": "tu_dortmund",
    },
    {
        "title": "Gesellschaftlich relevante Projekte foerdern Verantwortungsbewusstsein",
        "content": (
            "Gesellschaftlich relevante Projekte in Kooperation mit NGOs foerdern ein reflektiertes "
            "Verantwortungsbewusstsein fuer die Auswirkungen informatischer Systeme. "
            "Sie verdeutlichen, dass technische Entscheidungen stets gesellschaftliche Effekte haben."
        ),
        "category": "try",
        "perspective": "research",
        "source": "tu_dortmund",
    },
    {
        "title": "Externe Projekte mit oeffentlicher Verwaltung",
        "content": (
            "Externe Projekte mit oeffentlicher Verwaltung zeigen Anforderungen und "
            "Rahmenbedingungen oeffentlicher IT. "
            "Sie machen sichtbar, welche rechtlichen und organisatorischen Vorgaben umzusetzen sind."
        ),
        "category": "try",
        "perspective": "research",
        "source": "tu_dortmund",
    },
    {
        "title": "Sozialer Impact der Informatik wird sichtbarer",
        "content": (
            "Durch Kooperationen mit NGOs und externen Partnern wird der soziale Impact der Informatik "
            "sichtbarer und in der Lehre nachvollziehbar verankert. "
            "Dies hilft, technische Loesungen in ihren gesellschaftlichen Kontext einzuordnen."
        ),
        "category": "try",
        "perspective": "research",
        "source": "tu_dortmund",
    },
    {
        "title": "Praxisnahe Perspektiven ergaenzen theoretische Inhalte",
        "content": (
            "Praxisnahe Perspektiven aus Gastvortraegen ergaenzen theoretische Inhalte durch "
            "Erfahrungen aus dem Berufsalltag und der Projektpraxis. "
            "Sie helfen, abstrakte Konzepte mit konkreten Anwendungsfaellen zu verbinden."
        ),
        "category": "keep",
        "perspective": "self",
        "source": "tum",
    },
    {
        "title": "Externe Inputs foerdern kritisches Denken",
        "content": (
            "Externe Inputs durch Gastvortraege foerdern Diskussionen und schaerfen kritisches "
            "Denken durch den Vergleich verschiedener Praxisansaetze. "
            "So entstehen differenzierte Bewertungen von Methoden, Tools und Entscheidungen."
        ),
        "category": "keep",
        "perspective": "peers",
        "source": "tum",
    },
    {
        "title": "Mehr Vielfalt durch unterschiedliche externe Akteure",
        "content": (
            "Unterschiedliche externe Akteure erhoehen die Vielfalt der Blickwinkel in der Lehre. "
            "Dies erweitert das Spektrum an Meinungen, Branchen und technischen Loesungen."
        ),
        "category": "try",
        "perspective": "research",
        "source": "tu_dortmund",
    },
    {
        "title": "Externe Perspektiven sollten curricular verankert sein",
        "content": (
            "Externe Perspektiven sollten curricular verankert sein, um die Qualitaet der Lehre "
            "kontinuierlich zu sichern. "
            "Eine feste Verankerung sorgt fuer Planbarkeit, Vergleichbarkeit und klare Lernziele."
        ),
        "category": "try",
        "perspective": "self",
        "source": "che",
    },
]
