---
title: Übersicht
---
# UI eXtension für Home Assistant

::: info Stand geprüft am 20.11.2026 – UIX 9.1.0 stabil
Alle **66** kanonischen Seiten wurden mit `dev fb36536` und der Dokumentation von **v9.1.0** verglichen. Seit dem letzten Abgleich wurden vier Seiten geändert und 62 sind unverändert. [Lock Spark](./forge/sparks/lock) sperrt auch den gestalteten Rahmen; veraltete Beta-Hinweise bei [Kontexten](./concepts/context), [Seitenleisten-Verknüpfungen](./extras/custom-sidebar-panels) und [Footer-Konfiguration](./forge/forge#footer) sind entfernt. Die zwei offenen Sprachprüfhinweise zu Kontexten und Seitenleisten-Verknüpfungen werden durch diesen Inhaltsabgleich behoben.
:::

> **Unabhängige Übersetzung**
> Diese Dokumentation ist eine unabhängige deutsche Übersetzung und wird von UGSo Software gepflegt. Sie ist nicht die offizielle Dokumentation des UIX-Projekts. Maßgeblich bleibt die englische Originaldokumentation unter https://uix.lf.technology/.
>
> Basis ist GitHub-Release [`v9.1.0`](https://github.com/Lint-Free-Technology/uix/releases/tag/v9.1.0). Benötigt **Home Assistant 2026.11.0 oder neuer**. Original-Repository [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), Release-Stand [`ca36726`](https://github.com/Lint-Free-Technology/uix/commit/ca3672619a11858bbc7f9165db999c0aaa7cef00).
> Der aktuelle Dokumentationsabgleich verwendet `dev fb36536` vom 20.11.2026. Einzelheiten und Prüfgrenzen stehen im [Übersetzungsstatus](./translation-status).
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

## Funktionen der UIX-9.x-Versionen

- [Eigene Seitenleisten-Verknüpfungen](./extras/custom-sidebar-panels) öffnen HA-Seiten und externe Webseiten. Die Desktop-Tab-Option unterscheidet sich je nach Version, Ziel und Client; die Anleitung beschreibt die aktuellen Einschränkungen und die Companion-App.
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
> Aktueller Quellenabgleich: 20.11.2026, UIX 9.1.0 und `dev fb36536`. Bei Unklarheiten gilt die englische Originaldokumentation. Der frühere Abgleich vom 05.11.2026 ist ein historischer Prüfstand.
