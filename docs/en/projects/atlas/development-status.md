# Development Status

## Tested hardware variants

| Variant | Test environment |
| --- | --- |
| amd64 | Home Assistant in a virtual machine on Proxmox |
| ARM64 | Home Assistant on a physical Raspberry Pi 5 with 8 GB RAM |

These entries describe the tested installations; the scope and remaining checks
are documented in the development status below.

## Current State

**Expert bundle correction in 0.1.297:** Generated card scripts and HACS bundles now preserve the structured Expert layout instead of showing only an entity list. Home Assistant card helpers create the embedded Core/Community cards; configured entities are replaced and live state updates are forwarded without rebuilding cards. Existing projects and legacy script exports stay compatible. Publishing a HACS repository with release distribution remains a separate step.

**Native HA/HACS check on 2026-10-14:** Pi 5 and Proxmox run ATLAS 0.1.296 after updates with the HA backup option enabled. After HACS/Bubble/Mushroom installation on Pi, unchanged ATLAS YAML exports with Core/Bubble/Mushroom execute on both systems in the real unsaved HA card preview without configuration errors. An additional Mushroom Jinja preview on Pi evaluates actual HA state. Original projects and Administration exports then match exactly except for export timestamps; all six plugins remain active. Test dashboards are removed after confirmation. These previews do not verify full bundle installation, physical control actions or performance under load.

**Renderer/themes in 0.1.296:** blocked and pending states remain red and yellow in dark mode, and Expert field rows/delete controls remain readable in both themes. An isolated Chrome check with 36 prepared Entity/Button/Sensor/Thermostat/Bubble/Mushroom previews verifies DE/EN/FR, light/dark/auto, reload and four viewport sizes without overlapping fields or page horizontal overflow. Field objects and surface dimensions remain unchanged. System theme events are simulated; native HA/HACS execution and diverse user projects remain separate A5 checks.

The deferred Docker checks on 2026-10-14 pass for standalone and HA-package Linux amd64 images: build, real Administration/Card Editor runtime, health checks, container restart and plugin update/restoration with isolated data. Nine backend/origin regression checks also pass inside the Linux image. This does not replace native Supervisor/Ingress, ARM64 or browser verification; existing HA installations were not changed.

**A5 follow-up on 2026-10-14:** 0.1.295 also respects the browser-held Administration status when opening direct plugin launch links. Disabled or not-yet-active plugins do not launch through this route. This is a UI preference, not access control for plugin files. Isolated tests of the real app server verify installation, rejected updates, replacement, restart, uninstall and package restoration while retaining other catalog entries and fixture data. These tests do not replace native HA verification. A5 remains open for Renderer/Theme compatibility, diverse projects, native load and closed-transport recovery.

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

0.1.292 removes the remaining start-mode selector from HA configuration and
Administration and treats older Simple preferences as Expert.

A5 has started: **0.1.293** fixes snapshot/live-event ordering and failure status
when replacing a socket. An isolated PC check with mock HA verifies 100 rendered
test cards, 2001 entities, three reconnects, 150 live updates, theme changes and
DE/EN/FR project roundtrips. All 162 HA tests pass. These measurements are synthetic.

The native A5 follow-up loads 100 compact and 24 larger entity cards without
overlaps on both Pi 5 and Proxmox. Theme changes, reloads and DE/EN/FR preserve
the fields. Real backup-state changes arrive live on Pi; Proxmox initially
loads 3711 entities and 143 Lovelace resources. The observed VM CPU value stays
constant, so a changing live value is not established there. Local encrypted
HA backups are created first. The original editor and Admin configurations
are restored exactly, excluding export timestamps; all six plugins remain
active. Following a user-initiated Proxmox restart, the editor reconnects and
the original project remains unchanged.

These checks use prepared entity layouts in a desktop browser. Diverse user
projects, native backend load measurements, recovery after native transport closure and broader
plugin lifecycle checks remain open in A5. Desktop rendering is not a Pi
performance benchmark; native restart verification and simulated socket
closures are separate evidence.

**0.1.294** fixes recovery after longer network outages: the editor continues
beyond the previous three retries, with a delay capped at 30 seconds.
Authentication and protocol failures stop automatic retries until the
connection is corrected. An isolated eight-second unreachable-endpoint test
confirms recovery without reloading and preserves the project. During the real
LAN test, the Pi cable was disconnected for about twelve seconds. All 100 test
fields remained and live data resumed without reloading. The observed socket
stayed connected; this does not demonstrate a new native socket connection.
Both systems run 0.1.294. Final exports confirm unchanged Admin settings,
encryption metadata, active plugin IDs and original projects. Only the
deliberately updated external Icon Studio has a new version. An isolated
Docker build and /health also verify the combined Administration/editor runtime.
The user also confirms functional operation in a macOS Ventura VM directly on Proxmox, but reports
very sluggish behavior. This is functional evidence with a performance
limitation; the cause has not been measured or established.

As of **2026-10-13**: framework **0.2.0-alpha.88**, HA app **0.1.294**. All four
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
The current Home Assistant App/Add-on version is `0.1.297`. Administration and
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
