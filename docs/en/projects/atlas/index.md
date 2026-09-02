---
layout: home

hero:
  name: ATLAS
  text: Modular Application Framework
  tagline: A modular TypeScript framework for reusable applications, plugins and Home-Assistant-oriented tools.
  actions:
    - theme: brand
      text: Architecture
      link: /en/projects/atlas/overview
    - theme: alt
      text: Development Status
      link: /en/projects/atlas/development-status
    - theme: alt
      text: Home Assistant
      link: /en/projects/atlas/homeassistant
    - theme: alt
      text: ATLAS Plugins
      link: /en/projects/atlas-plugins/

features:
  - icon: modules
    title: Modular Architecture
    details: Clear separation between Core, Foundation, Runtime, Renderer, Home Assistant, Theme and Devtools.

  - icon: gear
    title: Runtime Foundation
    details: Services, dependency injection, events and other runtime fundamentals.

  - icon: plugin
    title: Plugin Ready
    details: ATLAS provides the platform; plugin authors have a dedicated ATLAS plugin documentation area.

  - icon: home
    title: Close to Home Assistant
    details: Status panels, entity selection, HA card export and Lovelace resource checks are being expanded step by step.

  - icon: test
    title: Testable
    details: Clear contracts, reference implementations and automated tests form the foundation.

  - icon: package
    title: Monorepo
    details: Packages are managed through pnpm workspaces with clearly separated responsibilities.
---

## Project Status

ATLAS is currently in active development.

The current focus is the **Home-Assistant-oriented ATLAS app** with
Administration, Plugin Hub, Card Editor and File Studio.

::: warning Development project
ATLAS is not released for production use yet. APIs, package structures and
internal contracts may still change.
:::

## Goal

ATLAS is intended to become a shared technical foundation for several UGSo
projects.

This includes:

- reusable services
- EventBus
- dependency injection
- modular plugins
- diagnostics and development tools
- Home Assistant integrations
- Administration and Plugin Hub
- File Studio for approved Home Assistant file paths
- Card Editor with Simple and Expert workflows
- shared theme and renderer structures
