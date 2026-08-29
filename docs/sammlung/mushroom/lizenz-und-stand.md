---
title: Mushroom Lizenz und Quellenstand
description: Quellen, Lizenzhinweise und Aenderungspruefung fuer die Mushroom-Doku.
---
# Lizenz Und Quellenstand

| Feld | Wert |
| --- | --- |
| Originalprojekt | [piitaya/lovelace-mushroom](https://github.com/piitaya/lovelace-mushroom) |
| Gepruefter Commit | [`6f8f1eaed3dc5cff94cd7ac5de64d921c6fb4101`](https://github.com/piitaya/lovelace-mushroom/commit/6f8f1eaed3dc5cff94cd7ac5de64d921c6fb4101) |
| Mushroom-Version | `5.2.2` laut `package.json` |
| Lizenzhinweis | `LICENSE` nennt Apache-2.0, `package.json` nennt ISC |
| Doku-Status | Inoffizielle deutsche Arbeitsuebersetzung und Praxisdoku |

## Kennzeichnung

Diese Seiten sind keine offizielle Mushroom-Dokumentation. Sie sind eine deutschsprachige Lesehilfe und Praxisdokumentation.

Das Originalprojekt und die englischen Originaldateien bleiben massgeblich.

## Aenderungspruefung

Die GitHub Action `Check Mushroom docs upstream` prueft regelmaessig, ob sich relevante Dateien im Original-Repository geaendert haben.

Ueberwacht werden:

- `README.md`
- `docs/cards/*.md`
- `docs/badges/*.md`
- `package.json`
- `LICENSE`

Wenn sich relevante Dateien aendern, erstellt die Action ein Issue mit Vergleichslink und Dateiliste.
