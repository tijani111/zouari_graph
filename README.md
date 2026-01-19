# EPI Knowledge Graph - POW 2025 (Team tijani)

Dieses Repository enthaelt das Python/Pygame-Projekt fuer den EPI-POW-Wissensgraphen.
Der Graph dient der persoenlichen Evaluation des Studiengangs Informatik (BA) im
Kontext der Reakkreditierung anhand von Keep / Drop / Try.

## Ziel des Projekts
- Visualisierung von Wissensknoten und ihren Zusammenhaengen.
- Abbildung von Quellen als eigene Knoten.
- Strukturierte Erweiterbarkeit fuer die Teamarbeit.
- Export/Import der Graphen zur spaeteren Zusammenfuehrung.

## Anforderungen (Kurzfassung)
- Teamname im Code setzen.
- Pro Teammitglied mindestens 20 Wissensknoten mit Quellen (Quellenzaehlen nicht).
- Inhalte sollen ausreichend detailliert sein.
- Konsistente Struktur fuer spaetere Zusammenfuehrung aller Teams.

## Projektstruktur
- `main.py`: Einstiegspunkt der Anwendung.
- `Structured_Demo_Knowledge_Graph/StructuredDemoGraph.py`: Aufbau des strukturierten Demo-Graphen.
- `GraphModel/`: Datenmodell fuer Knoten, Kanten und Graph.
- `GraphController/`: Layout, Import/Export und Interaktionen.
- `View/`: Pygame-UI (Rendern, Menues, Node-Details).
- `Resources/`: Icons und Bilder.

## Installation
Voraussetzung: Python 3.13 (empfohlen)

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Start
```bash
python main.py
```

## Graph-Aufbau (Kurzbeschreibung)
Der strukturierte Demo-Graph erzeugt:
- einen Themenknoten (Topic),
- Kategorien (KEEP / DROP / TRY),
- Perspektiven (Eigene Erfahrung / Mitstudierende / Recherche),
- Quellenknoten (Online-Quellen),
- Wissensknoten mit Textinhalt, die mit Topic, Kategorie, Perspektive und Quelle verbunden sind.

Die Kanten zeigen so pro Wissensknoten: Worum es geht, wie es bewertet wird, aus welcher Perspektive
es stammt und welche Quelle es stuetzt.

## Export / Import
Ueber das Menue der Anwendung kann der Graph als ZIP exportiert werden. Der Export enthaelt
auch Bilder aus `Resources/Images`. Der Import erlaubt das Laden exportierter Graphen
ohne Aenderung am Import-Code (wichtig fuer Teamzusammenfuehrung).

## Team
Branch: `tijani`
GitHub: `tijani111`

## Hinweise zur Teamarbeit
- Einheitliche Knotenstruktur zwischen Teammitgliedern einhalten.
- Quellen immer als eigene Knoten modellieren und verbinden.
- Inhalte deutlich als Keep/Drop/Try kennzeichnen.
