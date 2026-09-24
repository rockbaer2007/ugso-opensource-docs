---
title: Übersetzungsstatus
description: Status der deutschen UIX-Dokumentation gegenüber der englischen Originaldokumentation.
---
# Übersetzungsstatus

Diese Seite dokumentiert den aktuellen Abgleich der deutschen UIX-Dokumentation mit der englischen Originaldokumentation.

## Stand

- Alle 61 Markdown-Seiten des abgeglichenen englischen Stands haben deutsche Gegenstücke.
- Geprüft gegen den stabilen UIX-Release `8.3.1` vom 22.09.2026, Revision [`add5557`](https://github.com/Lint-Free-Technology/uix/commit/add5557c0ee13a98c9fe249bed06d215606f2507).
- Die Release-Korrekturen sind berücksichtigt: Die Map-Spark-Seite nennt den Fix für Home Assistant 2026.9.0; außerdem dokumentiert diese Statusseite den Kompatibilitätsfix für das Laden von Web Awesome auf älteren Geräten, einschließlich iOS 15.
- Die zuvor abgeglichenen Ergänzungen aus UIX `8.3.0-beta.8` sind nun Bestandteil der stabilen 8.3-Reihe; Hinweise auf Beta-Versionen bleiben dort erhalten, wo sie die Einführung einzelner Funktionen beschreiben.
- Frühere `8.2.0-beta`-Hinweise wurden mit dem stabilen Release `8.2.0` zusammengeführt.
- Die Seiten [Icons](./using/icons) und [Bilder](./using/images) wurden gezielt näher an die englische Originaldokumentation angeglichen, da diese Bereiche bei der externen Prüfung aufgefallen sind.
- Die Seite [Button Spark](./forge/sparks/button) enthält die mit UIX `8.2.0` veröffentlichte `outlined`-Darstellung.
- Lizenz- und Footer-Hinweise nennen die CC-BY-4.0-Lizenz der originalen UIX-Dokumentation.
- Die deutsche Fassung wird weiter mit dem englischen Original abgeglichen, sobald neue UIX-Änderungen im Original-Repository verfügbar sind.

## Aktualisierung vom 24.09.2026

Der Dokumentationsstand wurde gegen den stabilen UIX-Release `8.3.1` geprüft. Das Release nennt zwei Fehlerbehebungen: Die Map-Spark-Funktion wurde nach Änderungen an Home Assistant 2026.9.0 wiederhergestellt, und ein Ladeproblem von Web Awesome auf älteren Geräten (darunter iOS 15) wird umgangen. Diese Punkte sind Release-Änderungen; sie führen keine neue Konfigurationsoption ein.

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

## Abgleich vom 24.09.2026

Die UIX-Änderungen bis zur englischen Revision [`8c6fb83`](https://github.com/Lint-Free-Technology/uix/commit/8c6fb830d75477b30f035323161bac8d41599a78) wurden für Deutsch und Französisch geprüft. Dabei wurden die Änderungen aus [`a43f3e2`](https://github.com/Lint-Free-Technology/uix/commit/a43f3e2bf03edb808c0ea8d83af426d06626181e) und [`8711f1e`](https://github.com/Lint-Free-Technology/uix/commit/8711f1eb4a2a479a2a43d748c0b26f94b040e87a) mitberücksichtigt.

| Bereich | Abgeglichene Inhalte |
| --- | --- |
| Extras | Die frühere Seite zum Styling von Custom Panels im iframe wurde durch [Frame-Panels stylen](./extras/style-frame-panels) ersetzt. Sie beschreibt die experimentelle, interne Laufzeit, die Aktivierung, unterstützte gleichursprüngliche Frames und die Framework-Kompatibilität. |
| UIX Styling | [Custom Panels](./using/custom-panels) unterscheidet nun zwischen direkt geladenen Panels, Panel-Frames und App-Frames. [App- und Ingress-Panels](./using/apps) dokumentiert die Theme-Schlüssel, Slug-Auflösung und den Geltungsbereich von `uix-app`. |
| Navigation und Medien | Deutsche Seitenleiste und Übersichtsseiten verweisen auf die neuen Seiten; das App-Panel-Beispielbild wurde auf den kanonischen Stand aktualisiert. |

Die App-Frame-Funktion ist laut Original ab UIX `3.4.0-beta.1` verfügbar. Die experimentelle Option für Frame-Panels ist standardmäßig deaktiviert. Die stabile Metadatenbasis der deutschen Übersetzung bleibt davon unberührt.

Die stabile Versionsangabe in `uix-docs.json` ist auf `8.3.1` / `add5557` aktualisiert.

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
