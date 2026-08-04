---
title: ATLAS - Runtime Foundation
description: The current development state of the modular ATLAS framework.
date: 2026-08-02
author: UGSo Software
tags:
  - ATLAS
  - TypeScript
  - Architecture
---

# ATLAS - Runtime Foundation

**August 2, 2026 · ATLAS**

ATLAS is a modular TypeScript framework for reusable applications, plugins and
Home-Assistant-oriented tools.

## Current State

The basic repository and documentation structure has been completed.

Already implemented:

- monorepo with `pnpm` workspaces
- governance and architecture documents
- event and contract layer
- public event contracts
- `DefaultEventBus` reference implementation
- tests for the fundamental components

## Next Sprint

The next development step is:

```text
Sprint G2.5.3 - Runtime Foundation
```

The focus is on:

- service container
- dependency injection
- service descriptors
- controlled dependency resolution
- stable runtime contracts

## Long-Term Goal

ATLAS is intended to create a shared technical foundation for several UGSo
projects.

Later projects include the **UGSo Thread Monitor** for ESPHome Thread devices,
roles, IPv6 addresses and diagnostic data, plus the **Lovelace UV Card** for UV
index, protection status and visual Home Assistant dashboards.

## Learn More

[Open the ATLAS project page](/en/projects/atlas/)
