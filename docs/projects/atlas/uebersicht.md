# Architektur

ATLAS wird als modulares TypeScript-Monorepo entwickelt.

## Pakete

| Paket | Aufgabe |
|---|---|
| `core` | Zentrale Verträge und grundlegende Typen |
| `foundation` | Allgemeine Basiskomponenten und gemeinsame Infrastruktur |
| `runtime` | Laufzeitumgebung, Services und Service-Container |
| `renderer` | Darstellungsschicht und Renderer-Abstraktionen |
| `homeassistant` | Integration und Workflows für Home Assistant |
| `theme` | Gemeinsame Theme- und Design-Grundlagen |
| `devtools` | Diagnose- und Entwicklungswerkzeuge |
| `kernel` | Modulverträge, Dienstcontainer und Infrastruktur |
| `workspace` | Verträge zur Bereitschaft von Arbeitsumgebungen |
| `file-studio` | Interne File-Studio-Verträge und Runtime-Adapter; das installierbare Webplugin bleibt extern |
| `notifyarchive` | Interne Verträge für Benachrichtigungsarchive |

## Architekturprinzipien

ATLAS folgt mehreren festen Grundsätzen:

- klare Trennung von Verträgen und Implementierungen
- kleine, austauschbare Module
- testbare Komponenten
- Abhängigkeiten über definierte Schnittstellen
- Referenzimplementierungen für zentrale Dienste
- langfristig erweiterbare Plugin-Architektur

## Events

Die Event-Schicht umfasst unter anderem:

- `Event`
- `EventBus`
- `Handler`
- `Subscription`
- `Filter`
- `Publisher`
- `Subscriber`

Der `DefaultEventBus` dient als Referenzimplementierung.

## Services und Dependency Injection

Die Runtime Foundation enthält die Grundlagen für:

- Service-Beschreibungen
- Service-Registrierung
- Dependency Injection
- Service-Container
- kontrollierte Auflösung von Abhängigkeiten

## Nutzung und Ausblick {#geplante-nutzung}

Bereits verfügbar sind die Administration und der Home Assistant Card Editor als Referenzplugin. Weitere Werkzeuge und Diagnosen werden über Plugins eingebunden. ATLAS dient als Basis für:

- Home-Assistant-Werkzeuge
- Dashboard-Komponenten
- Diagnoseanwendungen
- Plugin-basierte Desktop- oder Webanwendungen
- die geplante **Lovelace UV Card**

Die Verträge sind noch in Entwicklung; diese Architektur ist keine Zusage einer
stabilen Plugin-API. Siehe [Entwicklungsstand](/projects/atlas/entwicklungsstand).
