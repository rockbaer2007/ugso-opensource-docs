---
title: Übersicht
---
# UI eXtension für Home Assistant

> **Unabhängige Übersetzung**
> Diese Dokumentation ist eine unabhängige deutsche Übersetzung und wird von UGSo Software gepflegt. Sie ist nicht die offizielle Dokumentation des UIX-Projekts. Maßgeblich bleibt die englische Originaldokumentation unter https://uix.lf.technology/.
>
> Basis: GitHub-Release [`v8.4.0`](https://github.com/Lint-Free-Technology/uix/releases/tag/v8.4.0) vom 07.10.2026. Benötigt **Home Assistant 2026.10.0 oder neuer**. Original-Repository [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), Release-Stand [`71b8ccd`](https://github.com/Lint-Free-Technology/uix/commit/71b8ccd38202257c070ae9970a7aac12a68a6389).
> Die Übersetzungen wurden mit dem bis zu diesem Release abgeglichenen Dokumentationsstand geprüft. Einzelheiten und bekannte Grenzen stehen im [Übersetzungsstatus](./translation-status).
>
> Vielen Dank an das UIX-Projekt für die durchdachte Umsetzung und die sehr gute englische Originaldokumentation, auf der diese deutsche Arbeitsfassung basiert.
>
> Die originale UIX-Dokumentation ist von [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix) und steht unter [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code des UIX-Projekts bleibt separat unter MIT lizenziert.


![UIX Logo](https://raw.githubusercontent.com/Lint-Free-Technology/uix/f9eb8fa571dbce6cd771c53ca11dcf2401c8a933/docs/source/assets/images/mixed.png)

## Was ist UI eXtension?

> **Für Card-mod-Nutzer**
> Wenn du von Card-mod wechselst, lies zuerst die [FAQ](./faq). Dort sind die wichtigsten Unterschiede, Migrationspunkte und typischen Stolperstellen zusammengefasst.
>
UI eXtension, kurz UIX, ist eine Home-Assistant-Integration für Anpassungen an der Oberfläche. Sie erweitert Karten, Zeilen, Badges, Dialoge und andere Frontend-Elemente mit CSS, Templates und zusätzlichen UI-Verhalten.

UIX besteht aus drei großen Bereichen:

- [UIX Styling](./using/index) für CSS-Anpassungen an Home-Assistant-Frontend-Elementen.
- [UIX Forge](./forge/index) für dynamisch erzeugte Elemente, wiederverwendbare Vorlagen und erweiterte Sparks.
- [UIX Broker](./broker/index) für deklarative Interaktionen: Browser-Events, Tastenkürzel und Home-Assistant-Events wählen ein Element aus, prüfen Regeln und führen Direktiven in ihrer Reihenfolge aus.

## Neu in UIX 8.4.0

- [Form Spark](./forge/sparks/form) und [Popover-Aktion](./extras/uix-actions#popover) für Formulare und eingeblendete Inhalte.
- [Frame-Panels stylen](./extras/style-frame-panels) mit interner Frame-Laufzeit; diese experimentelle Option bleibt standardmäßig deaktiviert.
- [Theme-Schriften mit `uix-fonts`](./using/themes) und [Entitätsbilder in Kartenübersichten](./using/images), einschließlich der Anpassung an Home Assistant 2026.10.
- [Broker-Direktiven-Regeln](./broker/directives#direktiven-regeln) können Ergebnisse früherer JavaScript- oder Template-Direktiven verwenden.

Die zuvor beschriebenen 8.4-Beta-Ergänzungen gehören damit zur stabilen Version. Historische Versionshinweise kennzeichnen weiterhin die Einführung einzelner Funktionen.

## Schnell loslegen

Der beste Einstieg ist der [Schnellstart](./quick-start). Dort findest du Installation, Einrichtung als Home-Assistant-Dienst und je ein erstes Beispiel für UIX Styling und UIX Forge.

## Wichtige Bereiche

- [UIX Styling verwenden](./using/index)
- [UIX Forge verwenden](./forge/index)
- [UIX Broker verwenden](./broker/index)
- [Konzepte verstehen](./concepts/index)
- [Debugging](./debugging/index)
- [FAQ](./faq)

> **Stand dieser deutschen Doku**
> Am 08.10.2026 mit dem Dokumentationsstand von UIX `8.4.0` abgeglichen. Bei Unklarheiten gilt immer die englische Originaldokumentation.
