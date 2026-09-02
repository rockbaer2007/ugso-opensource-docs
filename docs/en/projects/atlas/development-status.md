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
- Atlas Administration with plugin management, capability approvals,
  Home Assistant connection settings, add-on update hints and the prepared
  sidebar helper
- Plugin Hub with startup behavior for 0, 1 or multiple active plugins,
  dynamic plugin URLs and URL or `panel_iframe` copy actions
- Home Assistant Card Editor with Simple/Expert workflows, HACS-oriented
  export, problem reporting, a three-column import/entity area and separate
  `X`, `Y` and Zoom controls for the square Expert grid
- external documentation in the UGSo Open Source docs site
- ATLAS File Studio as the second plugin with `/config` by default, optional
  `/addons` approval, YAML validation, upload/download, backups, history with
  comparison and restore, search filters, multi-select actions, drag-and-drop
  upload, trash restore, favorites, file-type icons and secret-free problem
  reports with GitHub issue links

## Current Focus

The current development focus is:

```text
ATLAS File Studio and Home Assistant App/Add-on workflow
```

The work currently expands safe Home Assistant file workflows, versioned
add-on releases and traceable plugin updates.
The current Home Assistant App/Add-on version is `0.1.119`.

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
9. Continue expanding ATLAS File Studio as an installable plugin, especially later real Home Assistant reload actions.
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
