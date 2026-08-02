---
title: ATLAS – Runtime Foundation
description: Der aktuelle Entwicklungsstand des modularen ATLAS-Frameworks.
date: 2026-08-02
author: UGSo Software
tags:
  - ATLAS
  - TypeScript
  - Architektur
---

# ATLAS – Runtime Foundation

**2. August 2026 · ATLAS**

ATLAS ist ein modulares TypeScript-Framework für wiederverwendbare Anwendungen, Plugins und Home-Assistant-nahe Werkzeuge.

## Aktueller Stand

Die grundlegende Repository- und Dokumentationsstruktur ist fertiggestellt.

Bereits umgesetzt sind:

- Monorepo mit `pnpm` Workspaces
- Governance- und Architektur-Dokumente
- Event- und Contract-Schicht
- öffentliche Event-Verträge
- Referenzimplementierung `DefaultEventBus`
- Tests für die grundlegenden Komponenten

## Nächster Sprint

Der nächste Entwicklungsschritt ist:

```text
Sprint G2.5.3 – Runtime Foundation
```

Dabei liegt der Schwerpunkt auf:

- Service-Container
- Dependency Injection
- Service-Beschreibungen
- kontrollierter Auflösung von Abhängigkeiten
- stabilen Runtime-Verträgen

## Langfristiges Ziel

ATLAS soll eine gemeinsame technische Grundlage für mehrere UGSo-Projekte schaffen.

Ein späteres Projekt ist der **UGSo Thread Monitor**, der ESPHome-Thread-Geräte, Rollen, IPv6-Adressen und Diagnosedaten darstellen soll.

## Mehr erfahren

[ATLAS-Projektseite öffnen](/projects/atlas/)
