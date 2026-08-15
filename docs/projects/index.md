# Open-Source-Projekte

Auf dieser Seite werden die veröffentlichten Projekte von UGSo Software gesammelt.

## HADash

**HADash – Home Assistant Dashboard Toolkit**

HADash ist eine portable Windows-Anwendung zum Einlesen, Sichern und Exportieren von Home-Assistant-Dashboards und einzelnen Ansichten.

- [HADash-Dokumentation öffnen](./hadash/)
- [HADash auf GitHub öffnen](https://github.com/rockbaer2007/HADash)

## Home Assistant Automation Exporter

**Home Assistant Automation Exporter**

Der Home Assistant Automation Exporter ist eine portable Windows-Anwendung zum Aufteilen einer `automations.yaml` in einzelne YAML-Dateien. Die kompakte Oberfläche listet alle Automationen mit Checkboxen auf, bietet einen eigenen Einstellungsdialog für Export-Ordner und Sprache und exportiert nur die ausgewählten Automationen.

![Home Assistant Automation Exporter](/images/ha-automation-exporter/automations-exporter.png)

Über **Details** oder per Doppelklick auf eine Automation öffnet der Exporter ein Detailfenster mit zwei Tabs:

- **Entitäten** zeigt erkannte Home-Assistant-Entitäten mit Quelle, Zeilennummer und Kontext. Entitäten aus Templates werden heuristisch erkannt und entsprechend markiert.
- **YAML** zeigt den vollständigen Code der ausgewählten Automation und bietet einen Kopierbutton.

Export-Ordner und Sprache werden im Einstellungsdialog gepflegt, damit die Hauptansicht kompakt bleibt. Die Oberfläche unterstützt **Deutsch**, **Englisch**, **Französisch**, **Spanisch**, **Polnisch** und **Russisch**. Die Sprache kann automatisch über die Einstellung **System** anhand der Windows-UI-Sprache erkannt oder manuell ausgewählt werden; nicht unterstützte Systemsprachen fallen auf Englisch zurück.

Für Beispiele aus GitHub, Foren und anderen Open-Source-Projekten berücksichtigt der Exporter unterschiedliche Home-Assistant-YAML-Schreibweisen. Ältere und neuere Automationsdefinitionen wie `trigger`/`triggers`, `condition`/`conditions`, `action`/`actions`, `- trigger: state` und `- action: switch.turn_on` werden beim Export automatisch in ein importfreundliches Einzel-Automationsformat normalisiert.

![Automation-Details mit Entitäten](/images/ha-automation-exporter/details-entities.png)

![Automation-Details mit YAML-Code](/images/ha-automation-exporter/details-yaml.png)

- [Automation Exporter auf GitHub öffnen](https://github.com/rockbaer2007/ha-automation-exporter)
- [Aktuelles Release v0.3.3 herunterladen](https://github.com/rockbaer2007/ha-automation-exporter/releases/tag/v0.3.3)

## Ultimate Timer

**Ultimate Timer V3.2.4 FINAL CLEAN**

Ein leistungsstarker Hybrid-Timer-Blueprint für Home Assistant mit zuverlässiger STOP-Logik, dauerhaftem DONE-Status und optionaler MQTT-Unterstützung.

- [Ultimate-Timer-Dokumentation öffnen](./ultimate-timer/)
- [Repository auf GitHub öffnen](https://github.com/rockbaer2007/ha-ultimate-timer-blueprint)

## ATLAS

**ATLAS – Modular Application Framework**

ATLAS ist ein modulares TypeScript-Framework für wiederverwendbare Anwendungen, Plugins und Home-Assistant-nahe Werkzeuge.

Das Projekt befindet sich aktuell in aktiver Entwicklung. Der Schwerpunkt liegt auf der Runtime Foundation, Events, Services und Dependency Injection.

- [ATLAS-Projektseite öffnen](./atlas/)
- [Architektur ansehen](./atlas/uebersicht)
- [Entwicklungsstand ansehen](./atlas/entwicklungsstand)

## Weitere Projekte

Weitere Dokumentationen zu ESPHome, Lovelace-Komponenten und der geplanten Lovelace UV Card folgen.
