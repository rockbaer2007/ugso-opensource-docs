---
title: Übersicht
---
# UI eXtension für Home Assistant

::: info Stand geprüft am 05.11.2026
Stabile Basis ist **UIX 9.0.0** mit **Home Assistant 2026.11.0 oder neuer**. Alle **65** englischen Quellseiten wurden mit `master f63ebbd` verglichen. `dev ef414d9` enthält dieselbe Dokumentation. Einzelheiten stehen im [Prüfbericht](./translation-status).
:::

> **Unabhängige Übersetzung**
> Diese Dokumentation ist eine unabhängige deutsche Übersetzung und wird von UGSo Software gepflegt. Sie ist nicht die offizielle Dokumentation des UIX-Projekts. Maßgeblich bleibt die englische Originaldokumentation unter https://uix.lf.technology/.
>
> Basis ist GitHub-Release [`v9.0.0`](https://github.com/Lint-Free-Technology/uix/releases/tag/v9.0.0) vom 04.11.2026. Benötigt **Home Assistant 2026.11.0 oder neuer**. Original-Repository [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), Release-Stand [`cec1191`](https://github.com/Lint-Free-Technology/uix/commit/cec1191f6ee703284c75dfd3104dba9bb4419200).
> Die Dokumentation wurde mit `master f63ebbd` abgeglichen. Einzelheiten stehen im [Übersetzungsstatus](./translation-status).
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

## Neu in UIX 9.0.0

- [Eigene Seitenleisten-Verknüpfungen](./extras/custom-sidebar-panels) können HA-Seiten und externe Webseiten öffnen, auch in einem neuen Tab.
- Der [visuelle Forge-Editor](./forge/forge#visual-editor-cards-and-badges) bearbeitet Karten und Badges. `element_base` erhält die native Konfiguration mit ihren Templates.
- [Popover-Timeouts](./extras/uix-actions#popover) schließen eingeblendete Inhalte automatisch.

- [Form Spark](./forge/sparks/form) und [Popover-Aktion](./extras/uix-actions#popover) für Formulare und eingeblendete Inhalte.
- [Frame-Panels stylen](./extras/style-frame-panels) mit interner Frame-Laufzeit; diese experimentelle Option bleibt standardmäßig deaktiviert.
- [Theme-Schriften mit `uix-fonts`](./using/themes) und [Entitätsbilder in Kartenübersichten](./using/images), einschließlich der Anpassung an Home Assistant 2026.10.
- [Broker-Direktiven-Regeln](./broker/directives#direktiven-regeln) können Ergebnisse früherer JavaScript- oder Template-Direktiven verwenden.

Die [Installation über Marketplace](./quick-start) richtet UIX automatisch als Dienst ein. Bei der [Deinstallation](./faq) werden auch Foundries, Seitenleisten-Verknüpfungen und weitere Diensteinstellungen entfernt.

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
> Am 05.11.2026 gegen UIX `9.0.0` und den Dokumentationsstand `master f63ebbd` geprüft. Bei Unklarheiten gilt die englische Originaldokumentation.
