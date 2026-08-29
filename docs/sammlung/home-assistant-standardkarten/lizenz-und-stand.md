---
title: Lizenz und Quellenstand
description: Lizenzhinweise und Aenderungspruefung fuer die deutsche Home-Assistant-Standardkarten-Doku.
---
# Lizenz Und Quellenstand

Diese Dokumentation basiert auf der offiziellen Home-Assistant-Webseitendokumentation.

| Feld | Wert |
| --- | --- |
| Original-Repo | [home-assistant/home-assistant.io](https://github.com/home-assistant/home-assistant.io) |
| Originalseite | [Dashboard cards](https://www.home-assistant.io/dashboards/cards/) |
| Gepruefter Commit | [`c6308203e9f65a14786667294c29c1488a4733ac`](https://github.com/home-assistant/home-assistant.io/commit/c6308203e9f65a14786667294c29c1488a4733ac) |
| Home-Assistant-Version | Stabil: `2026.8.3`, Beta verfuegbar: `2026.9.0b3` |
| Lizenz | [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://github.com/home-assistant/home-assistant.io/blob/current/LICENSE.md) |

## Kennzeichnung

Dies ist keine offizielle Home-Assistant-Dokumentation. Es handelt sich um eine inoffizielle deutsche Arbeitsuebersetzung und Einordnung fuer deutschsprachige Nutzer.

Die englische Originaldokumentation bleibt massgeblich. Bei Abweichungen, Fehlern oder veralteten Inhalten gilt die Originalseite.

## Aenderungspruefung

Die GitHub Action `Check Home Assistant cards upstream` prueft regelmaessig, ob sich die ueberwachten Quelldateien im Original-Repository seit dem gespeicherten Commit geaendert haben.

Der angegebene Home-Assistant-Versionsstand wird manuell mitgepflegt. Entscheidend fuer die Doku-Pruefung ist der gespeicherte Commit des offiziellen Dokumentations-Repositories.

Ueberwacht werden:

- `source/dashboards/cards.markdown`
- `source/dashboards/actions.markdown`
- `source/dashboards/features.markdown`
- `source/dashboards/header-footer.markdown`
- `source/dashboards/views.markdown`
- `source/_dashboards/*.markdown`

Wenn sich relevante Dateien aendern, erstellt die Action ein Issue mit Vergleichslink und Dateiliste.
