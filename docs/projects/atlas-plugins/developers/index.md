---
title: Plugin-Entwicklung
description: Technischer Einstieg für Entwickler eigener ATLAS-Plugins.
---
# Plugin-Entwicklung

Dieser Bereich führt durch den Entwicklungsweg für eigenständige ATLAS-Plugins: vom Beispielprojekt über Manifest und Runtime bis zur Veröffentlichung. Die Plugin-Verträge entwickeln sich noch; prüfe vor einer Veröffentlichung die aktuelle Vorlage und das Repository-Format.

## Empfohlener Ablauf

1. Erstelle ein eigenes Repository mit der [offiziellen Plugin-Vorlage](../plugin-template).
2. Definiere eine eindeutige, nach der Veröffentlichung stabile ID und pflege Name, Version, Beschreibung, Assets und benötigte Fähigkeiten im Manifest.
3. Entwickle die Plugin-Oberfläche zunächst eigenständig. Die aktuelle Vorlage enthält eine einfache HTML/CSS/JavaScript-Beispielseite.
4. Baue Paket und Katalog mit `npm run build` und prüfe beide mit `npm run check`.
5. Teste den Katalog im ATLAS-Demo-Repository beziehungsweise in der Administration und veröffentliche Änderungen mit einer erhöhten Plugin-Version.

## Leitfäden

- [Manifest und Fähigkeiten](./manifest): Metadaten, IDs, Versionen, Assets und Deklarationen.
- [Runtime und Lebenszyklus](./runtime): Runtime-Plugin-Vertrag sowie Aktivieren, Deaktivieren und Aufräumen.
- [Bauen, prüfen und veröffentlichen](./publishing): Paketgenerator, Katalog, GitHub Actions und Release-Checkliste.
- [Plugin-Vorlage](../plugin-template): Schritt-für-Schritt-Anleitung für das GitHub-Starterprojekt.
- [Repository-Format](../repository-format): Katalogfelder und installierbares Paketformat.

## Sicherheitsgrenzen

Deklariere nur Fähigkeiten, die dein Plugin wirklich verwendet. Eine Deklaration dokumentiert den Zweck des Plugins; sie ist keine Sandbox und gewährt keinen automatischen Zugriff auf Home Assistant oder Atlas-Interna. Fordere Zugangsdaten nicht in Plugin-Dateien an und veröffentliche keine Tokens oder API-Schlüssel.

Der generische Repository-Installer speichert Paketdateien aktuell lokal und führt beliebigen heruntergeladenen Code nicht automatisch aus. Behandle Tests und Veröffentlichungen entsprechend als Paket- und Integrationsprüfung, nicht als Nachweis einer isolierten Ausführungsumgebung.
