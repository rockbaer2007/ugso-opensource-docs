# Automation Extractor

Automation Extractor ist als weiteres eigenständiges ATLAS-Plugin vorgemerkt. Die Idee basiert auf dem bisherigen Windows-Werkzeug zum Aufteilen von `automations.yaml`, soll aber direkt in die ATLAS-Plugin-Architektur wandern.

## Ziel

Das Plugin soll Home-Assistant-Automationen zuerst sicher analysieren und später kontrolliert exportieren oder umstrukturieren können.

- `automations.yaml` einlesen
- Automationen aus Paketen und Includes erkennen
- ID, Alias, Beschreibung, Trigger, Conditions und Actions anzeigen
- beteiligte Entitäten, Scripts, Szenen, Helfer und Benachrichtigungsziele sichtbar machen
- einzelne Automationen als YAML-Dateien exportieren
- spätere Refactoring-Schritte nur mit Backup, Prüfung und Vorschau ausführen

## Sicherheitslinie

Der erste Schritt soll lesend bleiben. Schreibende Änderungen an Home-Assistant-Dateien gehören erst in eine spätere Stufe, wenn Backup, YAML-Prüfung, Diff-Vorschau und Wiederherstellungspfad vorhanden sind.

## Einordnung

Automation Extractor ergänzt File Studio: File Studio ist die sichere Dateioberfläche, Automation Extractor wird die fachliche Analyse- und Exportoberfläche für Automationen.
