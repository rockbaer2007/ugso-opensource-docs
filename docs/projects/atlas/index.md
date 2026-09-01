---
layout: home

hero:
  name: ATLAS
  text: Modular Application Framework
  tagline: Ein modulares TypeScript-Framework für wiederverwendbare Anwendungen, Plugins und Home-Assistant-nahe Werkzeuge.
  actions:
    - theme: brand
      text: Architektur
      link: /projects/atlas/übersicht
    - theme: alt
      text: Entwicklungsstand
      link: /projects/atlas/entwicklungsstand
    - theme: alt
      text: Home Assistant
      link: /projects/atlas/homeassistant
    - theme: alt
      text: ATLAS Plugins
      link: /projects/atlas-plugins/

features:
  - icon: 🧱
    title: Modulare Architektur
    details: Klare Trennung von Core, Foundation, Runtime, Renderer, Home Assistant, Theme und Devtools.

  - icon: ⚙️
    title: Runtime Foundation
    details: Services, Dependency Injection, Events und weitere Laufzeitgrundlagen.

  - icon: 🧩
    title: Pluginfähig
    details: ATLAS stellt die Plattform bereit; Plugin-Autoren finden ihre eigene Rubrik in der ATLAS-Plugin-Dokumentation.

  - icon: 🏠
    title: Home-Assistant-nah
    details: Status-Panels, Entitätenauswahl, HA-Card-Export und Lovelace-Ressourcenprüfung werden Schritt für Schritt ausgebaut.

  - icon: 🧪
    title: Testbar
    details: Klare Verträge, Referenzimplementierungen und automatisierte Tests bilden die Grundlage.

  - icon: 📦
    title: Monorepo
    details: Verwaltung der Pakete über pnpm Workspaces mit klar getrennten Verantwortlichkeiten.
---

## Projektstatus

ATLAS befindet sich aktuell in aktiver Entwicklung.

Der derzeitige Schwerpunkt liegt auf der **Runtime Foundation** und dem Ausbau der grundlegenden Architektur.

::: warning Entwicklungsprojekt
ATLAS ist noch nicht für den produktiven Einsatz freigegeben. APIs, Paketstrukturen und interne Verträge können sich noch ändern.
:::

## Ziel

ATLAS soll eine gemeinsame technische Grundlage für mehrere UGSo-Projekte schaffen.

Dazu gehören unter anderem:

- wiederverwendbare Services
- EventBus
- Dependency Injection
- modulare Plugins
- Diagnose- und Entwicklungswerkzeuge
- Home-Assistant-Anbindungen
- gemeinsame Theme- und Renderer-Strukturen
