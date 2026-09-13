---
title: Übersetzungsstatus
description: Status der deutschen UIX-Dokumentation gegenüber der englischen Originaldokumentation.
---
# Übersetzungsstatus

Diese Seite dokumentiert den aktuellen Abgleich der deutschen UIX-Dokumentation mit der englischen Originaldokumentation.

## Stand

- Alle 61 Markdown-Seiten des abgeglichenen englischen Stands haben deutsche Gegenstücke.
- Die stabile Basis der deutschen Dokumentation ist UIX `8.2.0`.
- Letzter Änderungsabgleich: **13.09.2026**, englische Revision [`c33ff79`](https://github.com/Lint-Free-Technology/uix/commit/c33ff7995b757d5e7ead0cf8fd5fd85ed4d791ab), enthalten in **8.3.0-beta.8**.
- Alle 21 automatischen Übersetzungshinweise vom 04. bis 13.09.2026 wurden berücksichtigt. Neue 8.3-Funktionen sind als Vorabfunktionen gekennzeichnet.
- Frühere `8.2.0-beta`-Hinweise wurden mit dem stabilen Release `8.2.0` zusammengeführt.
- Die Seiten [Icons](./using/icons) und [Bilder](./using/images) wurden gezielt näher an die englische Originaldokumentation angeglichen, da diese Bereiche bei der externen Prüfung aufgefallen sind.
- Die Seite [Button Spark](./forge/sparks/button) enthält die mit UIX `8.2.0` veröffentlichte `outlined`-Darstellung.
- Lizenz- und Footer-Hinweise nennen die CC-BY-4.0-Lizenz der originalen UIX-Dokumentation.
- Die deutsche Fassung wird weiter mit dem englischen Original abgeglichen, sobald neue UIX-Änderungen im Original-Repository verfügbar sind.

## Aktualisierung vom 13.09.2026

| Bereich | Abgeglichene Inhalte |
| --- | --- |
| Broker-Direktiven | `tooltip`, `for: previous`, `trigger`, `open`, Inline-Styles, Regeln und Anchors; bestehender `directive`-Templatekontext |
| Tooltip Spark | HA-Standardwerte, Textfarben-Fallback, manuelle Aktivierung, Hover über dem Inhalt, begrenzte Höhe und Scrollen, korrigiertes Styling-Beispiel |
| Regeln | `user`, `user_is_admin`, `hash`, `search`, `panel`, Property-Pfade und Grenzen von `block` |
| Actions | `locked_action`, Sperreinträge, Code-Dialog, Fehlversuche und Hinweis auf die Grenze des Frontend-Schutzes |
| DOM und Beispiele | Broker-Konsolenhelfer, Property-Existenz, vollständiges Sidebar-YAML einschließlich Button und Filter für Entity-Trigger |
| Bilder und Navigation | Entity-Badge mit `show_entity_picture`, Broker als dritter Bereich und Verweise auf experimentelle Extras |
| Veröffentlichung | Englische/deutsche Sprachverweise im HTML, Metadatenvertrag und Vorabversions-Kompatibilität beschrieben |
| Kopierbare Beispiele | Maskierte Jinja-Klammern auf 17 Seiten durch echte Template-Begrenzer ersetzt, einschließlich eines zusätzlich gefundenen verschachtelten Codeblocks; Inline-Code und defekte Abschnittslinks korrigiert |

Die stabile Metadatenbasis in `uix-docs.json` bleibt `8.2.0` / `f9eb8fa`. Dieser zusätzliche Änderungsabgleich ist kein Wechsel auf eine stabile Version 8.3.0. Eine Vorabversion ist als solche zu behandeln.

Die Dokumentation wird mit VitePress gebaut. Die ergänzende Prüfung `python scripts/check-uix-docs.py` kontrolliert nach dem Build die gerenderten Codebeispiele, UIX-Linkziele und Sprachverweise. Home-Assistant-Laufzeittests sämtlicher Beispiele sind damit nicht abgedeckt.

## Redaktionelle Prüfung

Die Änderungen aus den genannten Benachrichtigungen sind abgeglichen. Eine unabhängige Satz-für-Satz-Prüfung sämtlicher bestehender Langseiten bleibt davon getrennt; besonders umfangreich sind folgende Seiten:

| Bereich | Seiten |
| --- | --- |
| Konzepte | `concepts/application`, `concepts/dom` |
| Styling | `using/entities`, `using/templates`, `using/themes`, `using/view-backgrounds` |
| Forge | `forge/forge`, `forge/foundries` |
| Sparks | `background`, `button`, `event`, `grid`, `lock`, `map`, `more-info`, `overlay-icon`, `search`, `state-badge`, `tile-icon`, `tooltip` |
| Extras | `uix-actions`, `frontend-states-throttling`, `dialog-styling-delay` |

## Maßgebliche Quelle

Die englische Originaldokumentation bleibt die maßgebliche Quelle:

[https://uix.lf.technology/](https://uix.lf.technology/)
