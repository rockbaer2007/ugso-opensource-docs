# Architektur

ATLAS wird als modulares TypeScript-Monorepo entwickelt.

## Pakete

| Paket | Aufgabe |
|---|---|
| `core` | Zentrale Verträge und grundlegende Typen |
| `foundation` | Allgemeine Basiskomponenten und gemeinsame Infrastruktur |
| `runtime` | Laufzeitumgebung, Services und Service-Container |
| `renderer` | Darstellungsschicht und Renderer-Abstraktionen |
| `homeassistant` | Geplante Integration mit Home Assistant |
| `theme` | Gemeinsame Theme- und Design-Grundlagen |
| `devtools` | Diagnose- und Entwicklungswerkzeuge |

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

## Geplante Nutzung

ATLAS soll später als Basis dienen für:

- Home-Assistant-Werkzeuge
- Dashboard-Komponenten
- Diagnoseanwendungen
- Plugin-basierte Desktop- oder Webanwendungen
- die geplante **Lovelace UV Card**
