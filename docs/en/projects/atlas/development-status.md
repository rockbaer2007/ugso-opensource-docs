# Development Status

## Tested hardware variants

| Variant | Test environment |
| --- | --- |
| amd64 | Home Assistant in a virtual machine on Proxmox |
| ARM64 | Home Assistant on a physical Raspberry Pi 5 with 8 GB RAM |

These entries describe the tested installations; the scope and remaining checks
are documented in the development status below.

## Current State

**As of 2026-10-22 · HA App 0.1.332 · HACS integration 0.1.306.**
App and integration version numbers are maintained independently.

**App 0.1.332 adds the searchable draft overview.** Project, script filename,
save time, explicit tab association and source identifier simplify selection.
Multi-term search, result counts, empty results and selection restoration when
clearing the filter are available in DE/EN/FR. Stored sources are neither rewritten
nor deleted; recovery remains explicit.
Native .68 qualification passes with 32 byte-identical original sources, duplicate
names, independent recoveries and preserved data. Three full backups remain;
.177 is untouched. Real mobile qualification remains open.

**Browser termination during repeated file import passes on .68.** Forced Chrome
process termination after the local record write, before the tab pointer update,
preserves newer A with an explicit recovery offer and B's independent source.
Cancelling preview changes nothing; new A, predecessor A and B recover identical
content and settings (apply selects the first card). All 20 old test-profile
sources remain byte-identical, original Editors and global configuration are
restored including after reload. Fixture files are in trash and three full backups
remain on .68; .177 is untouched. This qualifies one controlled boundary between
writes, not power loss or interruption inside the atomic Storage operation.
No new App version is needed.

**App 0.1.331 saves file imports as independent tab drafts.** Confirmed JSON
whole-configuration imports no longer need a previously opened shared project.
Another import creates a new source and retains its predecessor. Reload selects
the matching source; preview and backed-up apply remain explicit. The global
workspace is separate and can show the last import. Settings import and distinct
local/session error notices are retained. This corrects the 0.1.330 fresh-profile
finding; its source files and 46 earlier sources were preserved. Details:
[Card Editor](card-editor.md).

The .68 update (HA 2026.10.2) and native import/reload qualification pass in both
orders, with repeat import, cancellation/invalid input and blocked local/session
writes followed by safe retries. Complete export comparisons and all 48 old
sources pass; original states/data are retained, fixtures cleaned and three full
backups kept. .177 untouched. Applying the preselected draft remains explicit.

**Combined two-tab qualification passes:** On .68 with blocked session methods,
two distinct drafts remain editable/exportable during a real HA restart.
Automatic reconnection, explicit separate recovery after reload and confirmed
subsequent saves pass with complete export comparisons. All 40 previous sources
and existing data are preserved, both original Editors restored, owned fixtures
cleaned and three full backups retained. .177 untouched. App 0.1.330 is unchanged;
see [Card Editor](card-editor.md) for instructions and qualification boundaries.

**App 0.1.330 fixes the missing session-failure notice.** After a local write,
both recovery intent and tab pointer are confirmed. If this fails, a separate
DE/EN/FR notice says the draft is saved locally but tab recovery is not secured:
export before reloading/closing, then select the matching draft manually. Language
changes and project-list refreshes preserve the notice; only a fully confirmed
save clears it. A blocked session getter no longer disables local saving.
Local record errors remain distinct. This fixes the finding from the 0.1.329
qualification with 20 preserved sources. See [Card Editor](card-editor.md).

Native requalification on .68 (HA 2026.10.2) passes with full session storage,
blocked methods/getter, export and manual recovery. Language/list refreshes keep
the notice; a fully confirmed subsequent save clears it. Local errors remain
distinct. All 31 old draft sources are byte-identical; five original Editors and
existing data are restored. Owned fixtures are cleaned, three full backups kept,
.177 untouched. No further process crash or operating-system disk-fill test;
see the Card Editor section for boundaries.

**App 0.1.329 offers the newer draft after interrupted saving.** A tab-scoped
write intent stored beforehand identifies the complete record if its tab-pointer
update is missed. Preview and backed-up recovery remain explicit; the workspace
is never replaced automatically. Other tabs, predecessors and older sources remain
available. Invalid markers do not change selection; older versions still require
manual source selection. See [Card Editor](card-editor.md) for use and limits.

The update and targeted interruption after the record write/before the tab pointer
pass on .68 with HA 2026.10.2: DE/EN/FR offer/preview, cancellation without changes,
exact confirmed recovery and no confusion with a newer foreign draft. All 13
existing sources and both original Editors are unchanged; data comparison passes,
owned test objects are cleaned and three full backups retained. .177 untouched.
This run uses a controlled exception at the write boundary, not another forced
browser-process termination.

**Draft collision fixed in App 0.1.328 (2026-10-21, .68):** Two tabs save
independently and recover their own drafts after reloading. Full exports match
before/after recovery, including local edits made during a real App outage.
A closed tab's draft can be selected explicitly in a new tab. Old sources and
the legacy shared draft remain available; stale server saves remain blocked.
DE/EN/FR selection and preview pass. See [Card Editor](card-editor.md) for use
and limits. Owned project cleaned, original Editors/captured data preserved,
three full backups on .68; .177 unchanged. The subsequent full Chrome restart
with session restoration also passes: new main process, separate restored tab
pointers, complete draft comparisons and manual source selection. Subsequent
forced termination of all Chrome processes also passes: both complete drafts
including distinct Card titles recover, and four older draft sources are unchanged.
Originals preserved, owned project removed, three full backups retained. The
abort follows completed local saving; interrupted writes, power and disk
failures are not qualified. .177 remains untouched.

A subsequent targeted interruption during local saving, after the record write
and before the tab-pointer update, preserves the complete new draft for manual
selection; the confirmed predecessor stays preselected. Tab B and eight older
sources match their backups. The owned test probe leaves installed App files
unchanged. Original Editors/data are preserved, active test objects cleaned,
three full backups on .68; .177 untouched. This does not interrupt an atomic
native storage call or qualify power/disk failure. See [Card Editor](card-editor.md)
for the recovery steps and test limits.

The [HA compatibility matrix](frontend.md) now also includes HA **2026.10.2**
with integration 0.1.306 and App 0.1.327 on **.68**: embedding, live connection,
local save/reload, byte-identical JSON/YAML HACS roundtrips and automatic
reconnection after an HA restart pass. The original Editor and captured data
are preserved, the Runtime URL is restored and three full backups remain.
.177 was neither accessed nor changed. All three CI versions pass.

**App 0.1.327 bounds HACS checks and runs them off the UI thread.** Fixed budgets
before reads/CRC, a cancellable worker with a 15-second watchdog and explicit
adoption preserve the Editor until confirmation. The identical file can be
selected again after cancellation. All 431 package tests and the workspace build
pass. See the [Card Editor guide](card-editor.md) for limits and behavior.
Native qualification on .177/.68 with HA 2026.10.2 passes after full backups:
20 boundary cases, six cancellations, two same-file retries and two explicit
adoptions. Complete original Editors and captured files, projects and plugins
are preserved; both hosts run 0.1.327.

**Repeated large-project imports with unchanged App 0.1.327.** About 25 minutes
on .177/.68: 60 series adoptions per host, 36 fields with 360/720 nested Cards,
238 cancellations and 116 identical-file retries in total. Four actual HACS
round trips are byte-identical; three reload checkpoints per host and a valid
24-MiB package pass. Original Editors and captured existing data are preserved.
Browser-wide memory is not isolated ATLAS memory evidence; HA rendering is
qualified separately below.

**Large-project HA rendering passes.** On .177/.68 with App 0.1.327 and HA
2026.10.2: original and dynamic 360/720-Card projects, Card-Mod 4.2.1 and UIX
8.4.0 strictly separated. UIX also handles `card_mod`. Light/dark, CSS inheritance,
Mushroom Jinja and eight automatic reconnections pass: 62 snapshots, 33,120
native-reference comparisons, no error Cards. Existing Editors and captured data
are preserved; owned test objects are removed. See the [Card Editor guide](card-editor.md).
The user confirms 720 Cards on both hosts, themes and reconnection: Galaxy Tab
A6, Android 11 / LineageOS, Chrome Mobile 155. Responsive after stopping other
Apps. Owned objects removed, existing data preserved, three full backups each.
This earlier run has no FPS/long-term measurement. See [tablet result](tablet-test.md).

**UIX tablet soak completed:** The user confirms 60 minutes per host with 720
Cards, themes and reconnection on .177/.68, UIX 8.4.0 alone. Owned objects and
temporary UIX are removed, existing data comparisons pass and three full backups
remain per host. No independent FPS/memory/leak measurement is claimed.
See the [soak result](tablet-uix-dauertest.md).

**Historical size finding with App 0.1.324.**
24 actual import cases on .177/.68: 16 adoptions at 112/112 up to 30,008 files
or 64 MiB of extra stored content, and eight correct rejections of compressed
or truncated archives. Original Editors and checked existing data are preserved.
Reload directly after file selection retains both originals; this does not
qualify cancellable synchronous processing or general UI responsiveness.
See the [Card Editor guide](card-editor.md) for scope and remaining gaps.

**App 0.1.324 fixes ambiguous HACS adoption.** Project/script cardinality, all
declared script identities and complete readiness gate actual Editor adoption.
All 418 package tests and 40 new handler/identity regressions pass. Valid exports
and existing stored data remain intact.
Native updates on .177/.68 with HA 2026.10.2 pass after full backups: 60 cases,
52 correct rejections, eight valid imports at 112/112 and all 14 earlier incorrect
adoptions blocked. Complete original Editors and checked existing data remain intact.

**Historical finding in 0.1.323: ambiguous HACS packages.** On .177/.68 with HA 2026.10.2,
46 actual imports produce 26 correct rejections, six valid controls and
14 incorrect adoptions. Multiple projects/scripts may be adopted despite a
blocked report; a conflicting Editor plan script name even passes 112/112.
Selection can depend on ZIP order. Original Editors are restored and checked
existing data is unchanged; that qualification kept App 0.1.323 unchanged. Fixed from 0.1.324;
see [Card Editor](./card-editor).

App 0.1.322 validates every stored ZIP entry's CRC32 and header/directory
consistency before HACS adoption. Corrupt or unsupported archives stay outside
the Editor. All 376 package tests, including 52 new integrity cases, and four
byte-identical original archive roundtrips pass. Native updates on .177/.68 with
HA 2026.10.2 pass after full backups: 60 correct rejections preserve complete
Editors through reload, and four valid JSON/YAML controls pass at 112/112.
Original Editors and existing data remain unchanged. App 0.1.323 then corrects
generic missing-file follow-up notices: ZIP errors block first and dependent
file/content checks remain unverified. Actual missing files in verified ZIPs
remain errors. All 378 package tests pass; see
[Card Editor](./card-editor).

Native 0.1.323 qualification on .177/.68 passes after fresh full backups:
64 package cases, including 26 unverifiable ZIPs without misleading missing-file
claims, 60 safe rejections and four valid imports at 112/112. Complete original
Editors and checked existing data remain intact.

Native HACS negative qualification on .177/.68 is complete with 21 packages per
host after full backups: 38 correct rejections preserve complete Editor states
through reload, and two valid controls pass. App 0.1.321 had a CRC gap: a damaged README
inside the ZIP is falsely accepted at 112/112 twice and replaces local Editor
state. Both original Editors are restored exactly and existing data is unchanged.
This was not complete integrity qualification for 0.1.321; the finding is fixed
from 0.1.322. See [Card Editor](./card-editor).

App 0.1.321 fixes false HACS title failures with an empty first Entity name,
without modifying names. Both checks use package identity. All 324 local package
tests pass; the eight saved original/control archives pass unchanged at 112/112
and reexport byte-identically. Invalid manifest names remain rejected. Native
updates from 0.1.320 to 0.1.321 pass on .177/.68 with HA 2026.10.2 after full
backups: four original failing JSON/YAML ZIPs without a control card each reach
112/112 and reexport byte-identically. Original names and conditions remain exact
after import and reload; existing data and original local Editors stay unchanged.
See [Card Editor](./card-editor) for scope.

App 0.1.320 preserves empty Entity names and outer spaces/tabs literally.
All 296 local package tests pass; 37 new checks compare against the original
unparsed source through JSON/YAML, drafts, Card packages and HACS. Missing names
retain their fallback. Native updates on .177/.68 pass with HA 2026.10.2 after
fresh full backups: 64 import cases, 128 source-exact output samples and 16 actual
Card package roundtrips. Settings, files, seven projects and six plugins per host,
trash and original local Editors remain intact. The subsequent 0.1.321 update is documented above.
See [Card Editor](./card-editor) for scope and limits.

The subsequent native HACS/HA comparison passes with a named control card:
four ZIP roundtrips at 112/112, byte-identical reexports and 72 matching
exported/native pairs before/after reload. That test found a readiness defect:
an empty first Entity name causes two title failures (110/112) despite a named
package. Name data remains intact; this readiness gap is fixed in 0.1.321 and confirmed natively.
See [Card Editor](./card-editor) for scope and CSS behavior.

App 0.1.319 fixes standalone losses in the actual Editor application path:
Conditional conditions and Entity custom names survive. All 259 local package
tests pass, including 19 new Editor/draft/export checks. Stored data is unchanged.
Native updates on .177/.68 with HA 2026.10.2 pass after full backups: 32
source-exact JSON/YAML file/paste cases with reload and eight actual Card package
exports/reimports. Existing data, seven projects and six plugins per host, and
both original local Editors remain intact. Sixteen additional controls exposed a
boundary in 0.1.319: empty Entity names are replaced and outer whitespace is
trimmed. Earlier local tests compared after normalization; their broader claim
has been corrected. See [Card Editor](./card-editor) for scope and limits.

App 0.1.318 aligns import preview with the actual parser, rejecting unsupported
Markdown even inside nested cards. All 240 local package tests pass, including
27 new parity tests. Native updates on .177/.68 with HA 2026.10.2 pass after
full backups:24 Markdown rejections retain the Editor, eight nested imports
preserve structure, and existing data/local Editors remain intact. Findings on 0.1.318:
standalone Conditional cards lose conditions during Editor application, and
standalone Entity cards lose custom names (JSON/YAML on both hosts).

Extended Conditionals pass on the approved .177 and .68 test systems with
HA 2026.10.2: 1,008 visibility decisions, JSON/YAML, save/reopen and byte-identical
HACS roundtrips with 112/112 checks each. Existing data and original local
Editors are preserved. The Markdown preview mismatch is fixed locally in0.1.318; see the
[Card Editor](./card-editor) for scope and limits. New network tests are restricted
to these two addresses; reports below involving other hosts are historical.

0.1.317 fixes conditional import and blocks numeric conditions without valid
bounds. The isolated combined-project check passes saving, HACS roundtrip,
Jinja, live themes and reconnection, including 972 matching CSS comparisons.
Following fresh backups, the native update also passes on Proxmox and Pi 5:
112/112 package checks each, byte-identical HACS roundtrips, 756 additional CSS
comparisons, Conditional/Jinja, theme switches and automatic connection after
HA Core restarts. This check uses existing UIX on Proxmox and temporary Card-Mod
on Pi. Original local Editor states are restored.
Details: [Card Editor](./card-editor#current-status).

Following fresh backups, live theme switches without reload also pass on Proxmox
and Pi 5: Card-Mod/UIX separately, 28 transitions, 1,920 CSS comparisons and stable
Card/document identities. Original themes and extension settings are restored;
existing data remains intact. See the [Card Editor](./card-editor#current-status).

Live light/dark switches without reload now pass in isolation for Core, Bubble
and Mushroom: Card-Mod 4.2.1 and UIX 8.4.0 tested separately, seven transitions
each, 960 CSS comparisons and stable Card/document identities. Fixed overrides
remain intact while inherited colors/radii follow the theme. Pi 5 and Proxmox
remain untouched in this additional check. See the
[Card Editor](./card-editor#current-status) for scope and version limits.

0.1.316 fixes Bubble CSS import loss and root-stack UIX inheritance in exported
scripts. Following isolated checks, updates on Proxmox and Pi 5 also pass after
fresh HA backups: YAML/JSON, byte-identical HACS roundtrips with 112/112 checks
each and 240 additional CSS comparisons in the existing dark theme including
reload. Original local Editor configurations are restored. Re-export existing
Cards; recover previously lost CSS from original sources or backups.
See [Card Editor](./card-editor#current-status).

After fresh backups, native CSS qualification also passes on Proxmox and Pi 5
with Card-Mod 4.2.1 and UIX 8.4.0: generated scripts match native references
for the tested dynamic and static rules. Engines are tested separately using
passive sensors and no device commands. Original extension configuration is
restored; four existing projects per host and six plugins are preserved. See
the [Card Editor](./card-editor#current-status) for details and version limits.

Actual CSS rendering also passes in isolation with HA 2026.10.1, Mushroom
5.2.3, Card-Mod 4.2.1 and UIX 8.4.0 separately: generated scripts match native
references for dynamic colors/borders, shadow DOM styles and UIX radii.
`uix_style` has no CSS effect; CSS Jinja requires `config.entity`. See the
[Card Editor](./card-editor#current-status) for setup, examples and limits.
Pi 5 and Proxmox remain untouched; there is no new App release.

0.1.315 preserves imported `card_mod`, `uix` and `uix_style` objects in the
Editor, YAML/JSON, HACS packages and scripts. UIX export conversion, style
ownership, re-import and preservation pass in isolation. See the
[Card Editor](./card-editor#current-status) for scope and limits.

After fresh backups, the 0.1.313 → 0.1.315 update also passes on Proxmox and
Pi 5. YAML/Card-Mod and JSON/UIX each pass 112/112 checks and byte-identical
re-export there. Existing data, three previous projects per host and six active
plugins are preserved; complete original local Editor configurations are
restored exactly. CSS execution by installed styling extensions remains a
separate check.

0.1.314 aligns YAML/JSON HACS export, package checks and re-import. Both formats
pass the isolated browser roundtrip with 112/112 checks and byte-identical
re-export. Existing fixture data remain intact. That earlier isolated check
left Pi 5 and Proxmox untouched. The missing style preservation found
then is fixed from 0.1.315.

0.1.313 fixes Mushroom YAML/JSON and single-card import losses, checked in
isolation: text, icon and color templates remain intact. See the
[Card Editor](./card-editor#current-status) for scope. After fresh backups,
the update also passes on Proxmox and Pi 5: all four import paths, live output
and preservation pass. Own test projects remain separate; existing complete
local Editor configurations are restored exactly.

| Work package | Current status |
| --- | --- |
| A5 – Stabilization and verification | Complete within its documented scope. Diverse user projects and longer measurements remain follow-up qualification. |
| A6 – French documentation | Complete; DE/EN/FR are maintained together. Partial external plugin interface translations remain marked separately. |
| A7 – Deployment and compatibility | Linux/systemd and native HA/HACS integration implemented and verified. Further HA versions, platforms and data-format migrations when needed remain open. |

- Linux installation, update, rollback and recovery pass on Debian 12 amd64 LXC
  and Raspberry Pi OS aarch64 on Pi 4. Pi 4 also passes OS reboot, autostart and
  persistent HA connection recovery from 0.1.305.
- Shared plugin management, server projects and HACS integration updates with
  HA restarts pass on Pi 5 and Proxmox. The HA compatibility matrix covers
  2026.10.1, isolated 2026.9.4 and the exact 2026.10.2 combination on .68,
  not every HA release.
- Card export/import, real HACS repository registration, tagged releases,
  updates and recovery pass in isolation. Missing locale files and mixed package
  versions are detected; the 0.1.310/0.1.311 checks also pass on Pi 5 and Proxmox.
- 0.1.312 retains trash and history across App updates; legacy adoption and
  upgrades pass on both hosts. Encrypted full HAOS recovery into fresh separate
  amd64 test instances passes with the same and a changed IP. All 154 checked
  files, project, six plugins, trash and history survive. A new IP requires
  explicit changes to the App HA URL and integration Runtime URL; stored
  addresses are not rewritten automatically.

Details: [ATLAS roadmap](https://github.com/rockbaer2007/atlas/blob/main/ROADMAP.md)
and [recovery guide](/en/projects/atlas-plugins/file-studio).

## Historical checkpoints through 2026-10-14

The following reports retain their original scope. Statements such as “open” or
“next priority” apply to their date. For ongoing work, use the current status
above and next goals below.

**A7 – HA frontend in 0.1.299 (2026-10-14):** The optional [ATLAS Runtime integration](/en/projects/atlas/frontend) is implemented with a HACS-compatible layout, config/options flows and its own administrator sidebar panel. It embeds the existing runtime without forwarding HA credentials and retains the frame during ordinary state updates. Isolated real HA Core 2026.10.1 verifies setup, options, panel registration, reload, restart and unrelated panels remaining unchanged; browser checks verify editor interaction and project preservation. Six frontend and seven Python checks pass, along with HA/app regressions and builds. Existing Pi/VM/LXC installations are unchanged. HACS download/update on the real Pi/Proxmox systems and further HA versions remain the next A7 qualification.

**A7 – Linux/systemd (2026-10-14, ATLAS 0.1.298):** The optional [Linux installer](/en/projects/atlas/linux) is implemented. Native Debian 12 amd64 LXC on Proxmox passes installation, update, rollback, backup, service restart and automatic recovery after an unhealthy update. Configuration, installation identity and plugin/project fixture bytes are preserved; existing disabled FHEM and its files remain unchanged. Administration and the Expert Editor are checked over LAN in DE/EN/FR. All 17 installer and 163 HA tests pass, along with app, workspace, Docker and documentation checks. Native ARM64 Linux installation, other distributions and bare metal are not yet qualified. Native ATLAS HA/HACS frontend integration remains open under A7. Existing HA installations are unchanged.

**A6 – Documentation alignment (2026-10-14):** The 21 ATLAS and plugin documentation pages per language have been reviewed in DE/EN/FR. French placeholders are replaced with guides; navigation, language switching, resource paths, example packages and translation/credential guidance are corrected. Some external plugins still have partial French interfaces, explicitly documented as such. A7 is the next agreed priority: Linux/systemd and native ATLAS HA/HACS frontend integration. Runtime, HA installations and plugin data are unchanged.

**A5 verification phase complete (2026-10-14, HA app 0.1.297):** The final review covers renderer/themes, larger prepared projects, native Core/Bubble/Mushroom execution, live templates, short CPU/RAM observations and recovery within each documented scope. Fresh regressions pass: Runtime 55, Renderer 532, Theme 12, HA 163 and app/lifecycle 11, total 773; workspace and documentation builds pass. This is not production approval or a stable plugin API promise. Open follow-up qualification includes diverse user projects, long/instrumented outage tests under load, stable API/version policy, HACS release distribution and full card locale coverage. A6 is the next agreed priority: reviewing and completing French documentation. The older progress paragraphs below retain their original scope and limits.

**Approximately three-minute network interruption confirmed (2026-10-14):** The user confirms disconnecting Pi LAN and the Proxmox VM network interface for approximately three minutes each. They observe both ATLAS editors reconnecting automatically without reload or manual connection. Independent post-recovery checks confirm fresh HA data retrieval, original projects and Administration exports matching except export timestamps, and six active plugins per host. The planned 100 fixture fields were not loaded before interruption; no Console trace of socket states or retry counts is available. This user-observed three-minute scenario is complete; instrumented repetitions under project load remain a separate verification scope.

**Native CPU/RAM observation (2026-10-14):** Existing Supervisor statistics measure HA Core and ATLAS with 4 baseline, 14 load and 4 recovery samples each. Load comprises 120 real cards and 40 updating clock templates. HA Core medians (baseline → load → recovery): Pi CPU 0.13 → 0.18 → 0.09%, RAM 461.10 → 460.55 → 460.71 MiB; VM CPU 2.50 → 1.71 → 1.92%, RAM 1374.49 → 1390.87 → 1388.90 MiB. The largest observed VM load CPU sample is 21.71%. Running integrations and statistics queries also contribute load; differences cannot be attributed solely to test cards. These are short container observations, not whole-device/browser measurements, hardware comparisons or leak proofs. Original projects and Administration match except export timestamps, with six plugins active per host; own test dashboards are removed.

**40 live templates among 120 real HA cards verified (2026-10-14):** For this native check, the verified ATLAS configuration is extended with 40 distinct Mushroom Jinja outputs for time and sensor state. On Pi and Proxmox all 40 clock outputs change automatically without reload; 40 Core, 40 Bubble and 40 Mushroom cards remain mounted without configuration errors. Previews are discarded, original projects and Administration match except export timestamps, and six plugins remain active per host. This verifies simple server-side template evaluation and live time changes. It is not CPU/RAM benchmarking, a many-changing-entities test or a new ATLAS template-builder feature.

**120 actually rendered HA cards verified (2026-10-14):** The full mixed ATLAS export executes on Pi 5 ARM64 and Proxmox amd64 in the real unsaved HA card preview. After a 30-card stage, the 120-card stage mounts 40 Core, 40 Bubble and 40 Mushroom instances with nonzero dimensions and no configuration error. Entity details remain usable. Previews are discarded and own empty test dashboards removed after confirmation; original projects and Administration match except export timestamps, with six plugins active on each host. This uses Windows Chrome and one shared sensor. Observed rendering actions under one second include browser automation and are not backend or hardware benchmarks. CPU/RAM, diverse entities, expensive live templates and prolonged outages remain open.

**Mixed editor workload with 120 fields (2026-10-14):** On Pi 5 and Proxmox, 40 Core, 40 Bubble and 40 Mushroom fields retain complete data through title editing, reload, DE/EN/FR, light/dark and repeated HA requests. No fields overlap. After restoration, original projects and Administration exports match exactly except timestamps; all six plugins stay active. Editor tiles are not fully rendered Lovelace cards. Observed actions taking roughly one to two seconds include browser automation and are not backend benchmarks. Native CPU/memory measurements, larger rendered dashboards and new actual state transitions under mixed load remain open.

**Closed-transport recovery verified (2026-10-14):** With ATLAS 0.1.297, separate native test tabs on Pi 5 ARM64 and Proxmox amd64 each close the existing HA WebSocket. The user-executed Console check confirms the old socket CLOSED and the editor CONNECTED again without reload. Fresh HA data retrieval succeeds; all 24 fixture fields retain IDs, entities, positions and sizes. After restoration, original projects and Administration exports exactly match backups except export timestamps, with six plugins active on each host. This Windows Chrome check proves a bounded socket closure. Prolonged network outages, native backend load and diverse user projects remain open. Earlier pending closed-connection notes are superseded for this bounded scope.

**Local bundle installation verified:** The script exported from 0.1.297 was installed as a separate HA module resource on Pi 5 and Proxmox. The unchanged ZIP example instantiates the generated custom card and its Core/Bubble/Mushroom cards without configuration errors. Test cards were not saved; own test resources, files and the empty Pi dashboard were removed after confirmation. Administration exports stay identical except timestamps and all six plugins remain active. This verifies manual installation; HACS repository publication, full locale coverage, load and reconnect checks remain separate tasks.

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

The focus is realistic projects, endurance under load and remaining platform
and compatibility qualification.
The current Home Assistant App/Add-on version is `0.1.312`. Administration and
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

1. **Real projects and endurance:** diverse entities, Custom Cards and themes, longer CPU/RAM measurements and instrumented network outages under project load.
2. **Recovery on further hardware:** extend isolated amd64 HAOS recovery to physical or ARM64 hardware using separate test systems and backups.
3. **Further compatibility:** qualify additional HA releases, Linux distributions, plugin/API contracts and data-format migrations when required.

**A1, A4, A5 and A6 are complete; the A7 deployment paths are implemented.** Finished features remain documented in
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
