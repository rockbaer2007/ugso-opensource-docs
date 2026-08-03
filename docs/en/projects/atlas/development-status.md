# Development Status

## Current State

The basic repository and documentation structure is in place.

Completed work includes:

- monorepo structure with `pnpm` workspaces
- governance and architecture documents
- cleanup of the events and contracts layer
- public event contracts
- `DefaultEventBus` reference implementation
- heartbeat and EventBus foundations
- Home Assistant status demo with entity selection and card export
- external documentation in the UGSo Open Source docs site

## Current Focus

The current development focus is:

```text
ATLAS Home Assistant editor workflow
```

The work currently expands the Home Assistant card editor, entity picker,
Lovelace resource checks and export package model.

## Prepared Architecture Decisions

Prepared topics include:

- Kernel contracts
- Service container
- Dependency injection
- Service descriptors
- Event contracts
- reference implementations
- Home Assistant frontend and HACS-oriented workflows

## Next Goals

Planned next goals:

1. Stabilize the Runtime Foundation.
2. Define service lifecycles.
3. Complete dependency injection flows.
4. Expand diagnostics and error paths.
5. Prepare plugin contracts.
6. Continue the Home Assistant integration.
7. Expand Renderer and Theme layers.

## Long-Term Perspective

After the runtime foundations are stable, ATLAS should serve as a technical
basis for additional UGSo projects.

One planned follow-up project is the **UGSo Thread Monitor**. It is intended to
display ESPHome Thread devices, roles, IPv6 addresses, status values and
diagnostic data as an ATLAS-based plugin.

::: info Note
The roadmap may change during development. This page describes the current
planning state.
:::
