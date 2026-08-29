---
title: Home Assistant Automation Exporter
description: Deutsche Dokumentation zum Windows-Tool für den Export einzelner Home-Assistant-Automationen aus automations.yaml.
---
# Home Assistant Automation Exporter

Der **Home Assistant Automation Exporter** ist ein portables Windows-Tool, mit dem eine Home-Assistant-Datei `automations.yaml` eingelesen und in einzelne YAML-Dateien exportiert werden kann.

Das ist hilfreich, wenn Automationen getrennt gesichert, weitergegeben, dokumentiert oder später einzeln wieder in Home Assistant importiert werden sollen.

![Home Assistant Automation Exporter](/images/ha-automation-exporter/automations-exporter.png)

## Projekt

| Eintrag | Link |
| --- | --- |
| GitHub-Repository | [rockbaer2007/ha-automation-exporter](https://github.com/rockbaer2007/ha-automation-exporter) |
| Aktuelles Release | [v0.3.4 herunterladen](https://github.com/rockbaer2007/ha-automation-exporter/releases/tag/v0.3.4) |
| Plattform | Windows |
| Basis | C# / .NET 9 |

## Funktionen

- Öffnet eine Windows-Oberfläche ohne Kommandozeile.
- Zeigt die Programmversion im Fenstertitel.
- Liest eine Home-Assistant-`automations.yaml` ein.
- Sucht Automationen nach Alias, ID, Dateiname oder YAML-Inhalt.
- Zeigt alle Automationen in einer Tabelle mit Auswahlfeldern.
- Öffnet Detailansichten mit erkannten Entitäten und vollständigem YAML-Code.
- Exportiert ausgewählte Automationen als einzelne `.yaml`-Dateien.
- Öffnet den gewählten Exportordner direkt im Windows Explorer.
- Speichert Einstellungen portabel neben der EXE in `HaAutomationExporter.settings.json`.

## Voraussetzungen

Für die Nutzung als fertiges Release:

- Windows
- Download der aktuellen Release-Datei aus GitHub

Für Entwicklung oder Start aus dem Quellcode:

- Windows
- .NET 9 SDK
- Repository lokal geklont

```powershell
dotnet run --project .\HaAutomationExporter.csproj
```

## Bedienung

1. Programm starten.
2. Die Home-Assistant-Datei `automations.yaml` auswählen.
3. Optional den Exportordner in den Einstellungen ändern.
4. Automationen in der Tabelle auswählen.
5. Über `Details` einzelne Automationen prüfen.
6. Ausgewählte Automationen exportieren.
7. Die erzeugten YAML-Dateien bei Bedarf in Home Assistant importieren.

## Detailansicht

In der Detailansicht kann eine Automation vor dem Export geprüft werden. Das ist besonders nützlich, wenn viele Automationen ähnliche Namen haben oder Vorlagen und Entitäten kontrolliert werden sollen.

![Automation Details: Entitäten](/images/ha-automation-exporter/details-entities.png)

Der Tab **Entitäten** zeigt erkannte Home-Assistant-Entitäten mit Quelle, Zeilennummer und Kontext. Template-Treffer werden heuristisch erkannt.

![Automation Details: YAML](/images/ha-automation-exporter/details-yaml.png)

Der Tab **YAML** zeigt den vollständigen Automation-Code und enthält eine Kopieren-Funktion.

## Export für Home Assistant

Die exportierten Dateien werden so vorbereitet, dass sie sich besser einzeln in Home Assistant verwenden lassen.

Der Exporter entfernt die führende oberste `id:`-Zeile und normalisiert unterschiedliche YAML-Schreibweisen:

| Ausgang | Export |
| --- | --- |
| `triggers` | `trigger` |
| `conditions` | `condition` |
| `actions` | `action` |
| `- trigger: ...` | `- platform: ...` |
| Service-Aktionen | `- service: domain.service` |

Dadurch können Automationen aus verschiedenen Home-Assistant-Versionen, GitHub-Beispielen oder Forenbeiträgen einheitlicher exportiert werden.

## Sprachen

Die Oberfläche unterstützt:

- System
- Deutsch
- Englisch
- Französisch
- Spanisch
- Polnisch
- Russisch

Die Option `System` erkennt die Windows-Sprache für `de`, `en`, `fr`, `es`, `pl` und `ru`. Nicht unterstützte Systemsprachen fallen auf Englisch zurück.

## Kommandozeile

Das Projekt ist als Windows-Anwendung gebaut, damit es ohne Konsolenfenster startet. Intern können trotzdem Argumente verarbeitet werden.

```powershell
HaAutomationExporter.exe C:\path\automations.yaml C:\path\export
HaAutomationExporter.exe C:\path\automations.yaml C:\path\export pool
```

Für normale Nutzung ist die grafische Oberfläche vorgesehen.

## Hinweise

- Vor dem Import in Home Assistant sollte jede exportierte Automation kurz geprüft werden.
- Automationen mit komplexen Templates können manuelle Kontrolle benötigen.
- Die Originaldatei `automations.yaml` wird nur gelesen und nicht verändert.
- Der Exportordner sollte außerhalb der produktiven Home-Assistant-Konfiguration liegen, bis die Dateien geprüft sind.
