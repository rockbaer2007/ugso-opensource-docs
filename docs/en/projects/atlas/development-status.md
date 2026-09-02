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
- ATLAS File Studio as the second plugin with `/config` by default, optional
  `/addons` approval, YAML validation, upload/download, backups, history,
  search previews and secret-free problem reports

## Current Focus

The current development focus is:

```text
ATLAS File Studio and Home Assistant App/Add-on workflow
```

The work currently expands safe Home Assistant file workflows, versioned
add-on releases and traceable plugin updates.

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
6. Prepare separate plugin documentation for authoring, lifecycle, extension APIs, examples and publishing.
7. Continue the Home Assistant integration.
8. Expand Renderer and Theme layers.
9. Continue expanding ATLAS File Studio as an installable plugin, especially restore from history, more specific HA YAML assistance and GitHub-linked problem reports.
10. Plan Automation Extractor as another plugin, starting read-only and later adding a safe export path.

## Long-Term Perspective

After the runtime foundations are stable, ATLAS should serve as a technical
basis for additional UGSo projects.

Planned follow-up projects include:

- **Lovelace UV Card**: a Home Assistant/Lovelace card for UV index, protection
  status, thresholds and visual dashboard output. `filipnet/haos-uv-index` is
  noted as inspiration for UV-index sensor handling, color-coded risk levels,
  WHO-style protection recommendations, Mushroom-compatible presentation and
  optional notification automations. The implementation should remain an
  original UGSo/ATLAS card.

::: info Note
The roadmap may change during development. This page describes the current
planning state.
:::
