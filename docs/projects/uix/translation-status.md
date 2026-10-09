---
title: Übersetzungsstatus
description: Status der deutschen UIX-Dokumentation gegenüber der englischen Originaldokumentation.
---
# Übersetzungsstatus

Diese Seite dokumentiert den aktuellen Abgleich der deutschen UIX-Dokumentation mit der englischen Originaldokumentation.

## Abgleich vom 09.10.2026: stabile Basis 8.4.0, Vorschau 9.0.0-beta.0

Die kanonischen Meldungen zu `2db023d236c9`, `c800e607f23d`, `9b5858f57678` und `22f8d93f0131` wurden in Deutsch und Französisch abgeglichen. Der geprüfte `dev`-Stand ist [`e2e0701`](https://github.com/Lint-Free-Technology/uix/commit/e2e070193b3f77b251dcfe05104a4d791a8e9a03), Version **9.0.0-beta.0**. Das Original nennt weiterhin **8.4.0** als stabile Version auf `master`; Release-Link, Footer und stabile Metadaten behalten diesen Stand.

- Veraltete Beta-Hinweise in Broker-Direktiven, Popover-Aktion, Form Spark, App-Panels und Theme-Schriften entfernt.
- FAQ zur nicht unterdrückbaren Reload-Meldung und zum automatischen Neuladen nach 60 Sekunden ergänzt. Die neue Auslieferung der beim Home-Assistant-Start geladenen Version ist als Vorschau gekennzeichnet.
- Forge-Referenz, Foundries und Übersicht um die geschichtete Konfiguration ergänzt: `element_base`, Forge-Overlay `element`, lokale `element_disabled_paths`, Merge-Regeln, native Sichtbarkeit und Template-Kontexte. Verfügbarkeit ausdrücklich ab **9.0.0-beta.0**, nicht 8.4.0 oder 8.4.1.
- Die Originalanimation `forge-auto-entities.gif` aus `9b5858f57678` für DE/FR übernommen. Die stabile `source_revision` bleibt unverändert; Vorschauversion, Branch und Revision werden separat in den Metadaten erfasst.

## Stand: UIX 8.4.0

- Abgleich am **08.10.2026** gegen den stabilen Release [`v8.4.0`](https://github.com/Lint-Free-Technology/uix/releases/tag/v8.4.0) vom 07.10.2026, Revision [`71b8ccd`](https://github.com/Lint-Free-Technology/uix/commit/71b8ccd38202257c070ae9970a7aac12a68a6389).
- Benötigt **Home Assistant 2026.10.0 oder neuer**.
- `git diff c70d1275f1fb08514291feb4c9181a748408b798 v8.4.0 -- docs/source docs/mkdocs.yml` zeigt keine Änderungen. Der zuletzt abgeglichene kanonische Dokumentationsstand ist damit auch der Stand des stabilen Releases.
- Berücksichtigt sind Form Spark, Popover-Aktion, interne Frame-Laufzeit, `uix-fonts`, Entitätsbild-Overrides in Kartenübersichten und Broker-Ergebnisreferenzen. Die Frame-Option bleibt experimentell und standardmäßig aus.
- Die bislang fehlende [Badge-Spark-Referenz](./forge/sparks/badge) wurde ergänzt. Deutsch und Französisch haben nun Gegenstücke zu allen 64 kanonischen Markdown-Pfaden sowie eine eigene Statusseite. Die Badge-Seite ist eine kompakte Referenz mit vollständigen Options- und CSS-Tabellen; weitere Originalbeispiele sind verlinkt.
- Übersicht, Footer, Release-Link, JSON-Metadaten und `llms.txt` nennen 8.4.0. Versionshinweise auf einzelnen Seiten kennzeichnen die Einführung der Funktionen; frühere Prüfberichte unten sind historische Stände.
- In Französisch wurden 17 englische Kompatibilitäts-Anchors ergänzt und damit 36 bestehende Abschnittslinks repariert; französische Titel und Abschnittsadressen bleiben erhalten.
- Die Prüfung umfasst Quellenvergleich, Seitenabdeckung, Build, Links, Sprachverweise und kopierbare Beispiele. Sie ersetzt keine erneute Satz-für-Satz-Prüfung aller Altübersetzungen und keine Home-Assistant-Laufzeittests.

## Historischer Stand: UIX 8.3.1

- Alle 61 Markdown-Seiten des abgeglichenen englischen Stands haben deutsche Gegenstücke.
- Geprüft gegen den stabilen UIX-Release `8.3.1` vom 22.09.2026, Revision [`add5557`](https://github.com/Lint-Free-Technology/uix/commit/add5557c0ee13a98c9fe249bed06d215606f2507).
- Die Release-Korrekturen sind berücksichtigt: Die Map-Spark-Seite nennt den Fix für Home Assistant 2026.9.0; außerdem dokumentiert diese Statusseite den Kompatibilitätsfix für das Laden von Web Awesome auf älteren Geräten, einschließlich iOS 15.
- Die zuvor abgeglichenen Ergänzungen aus UIX `8.3.0-beta.8` sind nun Bestandteil der stabilen 8.3-Reihe; Hinweise auf Beta-Versionen bleiben dort erhalten, wo sie die Einführung einzelner Funktionen beschreiben.
- Frühere `8.2.0-beta`-Hinweise wurden mit dem stabilen Release `8.2.0` zusammengeführt.
- Die Seiten [Icons](./using/icons) und [Bilder](./using/images) wurden gezielt näher an die englische Originaldokumentation angeglichen, da diese Bereiche bei der externen Prüfung aufgefallen sind.
- Die Seite [Button Spark](./forge/sparks/button) enthält die mit UIX `8.2.0` veröffentlichte `outlined`-Darstellung.
- Lizenz- und Footer-Hinweise nennen die CC-BY-4.0-Lizenz der originalen UIX-Dokumentation.
- Die deutsche Fassung wird weiter mit dem englischen Original abgeglichen, sobald neue UIX-Änderungen im Original-Repository verfügbar sind.

## Broker-Abgleich vom 05.10.2026

Die Seiten [Directives](./broker/directives#direktiven-regeln) und [Rules](./broker/rules#kompakte-captured-data-form) wurden gezielt mit den kanonischen Änderungen [`105b8cd`](https://github.com/Lint-Free-Technology/uix/commit/105b8cd446ea082553be627530efe8a752d57dec) und [`04d8e14`](https://github.com/Lint-Free-Technology/uix/commit/04d8e14b006f24e795997c68191f9fde3652bd22) abgeglichen. Ergänzt sind Ergebnisreferenzen `@<directive-id>`, das unveränderte YAML-Beispiel und der Hinweis auf UIX `8.4.0-beta.9`. Diese Referenzen sind nur in Direktiven-Regeln verfügbar. Die entsprechenden französischen Seiten wurden ebenfalls aktualisiert; die stabile Basis bleibt UIX `8.3.1`.

## Aktualisierung vom 24.09.2026

Der Dokumentationsstand wurde gegen den stabilen UIX-Release `8.3.1` geprüft. Das Release nennt zwei Fehlerbehebungen: Die Map-Spark-Funktion wurde nach Änderungen an Home Assistant 2026.9.0 wiederhergestellt, und ein Ladeproblem von Web Awesome auf älteren Geräten (darunter iOS 15) wird umgangen. Diese Punkte sind Release-Änderungen; sie führen keine neue Konfigurationsoption ein.

## Abgleich vom 30.09.2026

Die deutschen Seiten zu [Entitäten](./using/entities) und [Bildern](./using/images) wurden mit der kanonischen Dokumentationsrevision [`7d7c95a`](https://github.com/Lint-Free-Technology/uix/commit/7d7c95acb449c1222d8a338e3d9423f91ff0f2a2) abgeglichen. Ergänzt wurden die CSS-Parts für Map-Marker ab Home Assistant 2026.10.0 sowie `hui-map-overview` und der Hinweis auf Entity-spezifische Bildüberschreibungen. Die stabile Basis bleibt UIX `8.3.1`; der Footer weist zusätzlich auf die abgeglichenen Dokumentationsänderungen bis UIX `8.4.0-beta.3` hin.

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

## Abgleich vom 08.10.2026

Die Änderungen der englischen Dokumentation in Revision [`c70d1275f1fb`](https://github.com/Lint-Free-Technology/uix/commit/c70d1275f1fb08514291feb4c9181a748408b798), Branch `master`, wurden mit Deutsch und Französisch abgeglichen.

- Neuer [Form Spark](./forge/sparks/form) mit Schema, Markdown, Submit/Clear, Dichte, CSS-Variablen und Formularwerten in Aktionen.
- Neue [Popover-Aktion](./extras/uix-actions#popover), einschließlich Karten, Header-Icons, Footer-Buttons, Formularintegration und Originalbeispielen.
- Broker: synchrones `block`, Regel-Anchors, wiederverwendeter Panel-Zustand, Tooltip-Referenz `previous`, JavaScript-Promises und Styling-Lebenszyklus-Events korrigiert. Veraltete geplante Funktionen entfernt.
- Navigation, Forge-Übersichten und FAQ ergänzt; sechs neue oder geänderte Originalmedien übernommen.
- Die bereits vorhandenen Änderungen an Frame-/App-Panels wurden erneut verglichen. Ergänzt wurden die Änderungen an Entitätsbildern, Kartenmarkern und Theme-Schriften.

Dieser Abgleich betrifft die gemeldeten Dokumentationsänderungen. Die stabile Metadatenbasis bleibt `8.3.1`; er ersetzt keine vollständige Prüfung sämtlicher Seiten gegen eine spätere stabile Veröffentlichung. YAML-/JavaScript-Beispiele und Medien des neuen Form-Sparks und der Popover-Aktion stammen unverändert aus der englischen Quelle. Der Doku-Build und die Linkprüfung überprüfen die Veröffentlichung; sie führen keine Home-Assistant-Laufzeittests aus.
