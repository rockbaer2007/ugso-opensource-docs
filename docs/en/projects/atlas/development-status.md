# Development Status

## Tested hardware variants

| Variant | Test environment |
| --- | --- |
| amd64 | Home Assistant in a virtual machine on Proxmox |
| ARM64 | Home Assistant on a physical Raspberry Pi 5 with 8 GB RAM |

These entries describe the tested installations; the scope and remaining checks
are documented in the development status below.

## Current State

**A2 and A3 are complete (2026-10-13).** The user accepts the current ARM64/mobile
verification scope. Physical iOS/Safari devices were not tested; Chrome simulator
checks are documented separately. The Card Editor remains Expert-only.
Simple mode and its switch will not return; supported legacy project imports
remain available.

0.1.290 shortens the tablet card list to a scrollable window with two cards side
by side and arranges its action buttons in two columns.

0.1.291 collapses Grid & zoom by default on mobile and puts tablet title
controls in one row; phone title buttons share a row below the field.
All values are preserved.

As of **2026-10-13**: framework **0.2.0-alpha.88**, HA app **0.1.291**. All four
agreed stabilization items are complete. Acceptance checks cover 870 workspace
tests, five additional tests, all type checks and builds, and 15 isolated browser
checkpoints in DE/EN/FR. The tested migration preserves older Admin preferences,
repositories, theme and active plugin IDs while moving secrets into encrypted
storage.

A1 has been verified on the real HA installation: Supervisor upgrade from
0.1.287 to 0.1.288, a separate restart and Ingress for all six installed plugins.
Administration settings, active plugins and the complete editor configuration
match before and after the upgrade and restart, excluding export timestamps.
A local encrypted HA backup was created first. Version 0.1.288 fixes the
Administration runtime version display; HA options and plugin contracts remain
unchanged. The editor reconnects and loads real entities and Lovelace resources.
The existing Expert canvas was empty; larger populated projects remain A5.
Hardware actions, mobile browsers, ARM64 and every plugin-owned project format
have not been verified. The Card Editor is the integrated ATLAS reference
plugin; standalone plugins are maintained separately.

A2 is verified in emulation: amd64 and ARM64 HA images plus a mobile Chromium
touch context at 360×800, 390×844, 844×390 and 768×1024 in DE/EN/FR. Version
0.1.289 fixes Administration/editor overflow and fits problem-report, YAML-import
and export dialogs to narrow screens. Settings, populated test projects and
plugin data survive locale changes, JSON/HACS imports and restart. ARM64 is
emulated on an x86 host; native Raspberry Pi performance, Android/iOS,
touch drag/resize, virtual keyboards and native file/download dialogs remain
open. The real HA installation is not modified for these isolated checks.

The native A2 check on a **Raspberry Pi 5 / rpi5-64** also passes: HA OS 18.3,
ATLAS 0.1.289, `aarch64` and Node `arm64`. All six plugin surfaces open through
Ingress; Terminal, approved File Studio paths and the MDI catalog work. A local
encrypted HA backup is created before restarting ATLAS. Administration
settings, plugin metadata and the complete editor export match afterwards,
excluding export timestamps. The editor reconnects with 27 real entities.
The existing canvas is empty. Desktop Chrome views at 390×844 and 844×390
fit the real Pi Ingress without page overflow. Physical mobile browsers,
larger populated projects and load/performance are not established by this
check; no ARM64 Supervisor upgrade is performed on this fresh installation.

The user additionally confirms on a **physical Android tablet**: Hub and
Administration work in portrait and landscape and in DE/EN/FR. Changing the
HA URL from `homeassistant.local:80` to the reachable IP address restores the
connection; the YAML dialog and Problem report are also reported as OK.
This is user-reported evidence, not an automated device test.
[Mobile connection advice](./homeassistant#connecting-from-tablets-and-phones).
Touch drag/resize, virtual keyboards, native file/download dialogs and iOS
were not independently verified on every device. A2 is nevertheless complete
with user acceptance; these limits are not open A2 tasks.

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
  dynamic plugin URLs, URL or `panel_iframe` copy actions and capability lists
  plus sidebar URLs collapsed by default on every plugin card; Card Editor,
  Administration and plugin assets run through ATLAS app routes that preserve
  Home Assistant Ingress paths instead of requiring direct access to separate
  development ports
- Home Assistant Card Editor with a direct Expert workflow, HACS-oriented
  export, problem reporting, a three-column import/entity area and separate
  `X`, `Y` and Zoom controls for the square Expert grid
- external documentation in the UGSo Open Source docs site
- ATLAS File Studio as the second plugin with `/config` by default, optional
  `/addons` approval, YAML validation, upload/download, backups, history with
  comparison and restore, search filters, multi-select actions, drag-and-drop
  upload, trash restore, favorites, file-type icons and secret-free problem
  reports with GitHub issue links
- ATLAS Automation Exporter / Editor as an independent GitHub-installable
  plugin with system `automations.yaml`, YAML upload, timestamped exports,
  export overview, File Studio handoff and analysis hints for missing or
  duplicate ids/aliases, missing triggers/actions and disabled automations;
  service calls are detected from both `service:` and modern
  `action: domain.service` syntax, detail YAML is shown with highlighting and
  long automation lists scroll internally

## Current Focus

The current development focus is:

```text
ATLAS Card Editor, Runtime and preservation of existing settings and plugins
```

The next priority is A5: production readiness with larger real projects,
live updates, reconnection and plugin compatibility.
The current Home Assistant App/Add-on version is `0.1.291`. Administration and
Plugin Hub support German, English and French, and share the saved language
preference across their separate app ports.

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

Open ATLAS priorities:

1. **A5 – Production readiness:** verify and expand Renderer, Theme and plugin APIs with larger real projects, live updates, reconnection and compatibility.
2. **A6 – French documentation:** complete unfinished FR pages and align DE/EN/FR structure and content.
3. **A7 – Further deployment paths:** prepare a Linux/systemd installer and native ATLAS HA/HACS integration using the same runtime.

**A1 – Real HA verification and A4 – Roadmap cleanup are complete.** Finished features remain documented in
history and are not open tasks. Standalone plugins maintain their implementation
backlogs in their own projects.
The authoritative open list is the [ATLAS roadmap](https://github.com/rockbaer2007/atlas/blob/main/ROADMAP.md).

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
