---
title: Home Assistant Card Editor
description: Dedicated documentation for the ATLAS Home Assistant Card Editor with the Expert editor, import, export, resource checks and Home Assistant connection.
---

# Home Assistant Card Editor

::: info Bounded, cancellable HACS import with App 0.1.327
The fixed ZIP limit is **32 MiB**, checked before reading. Inventory budgets
are **2,048 entries**, **8 MiB per entry**, **24 MiB total content** and
**1,024 UTF-8 bytes per path**. Metadata budgets precede CRC work, including
declared expanded sizes. Compressed entries remain unsupported; CRC32 is not
an authenticity signature.

Reading and validation run in a dedicated worker. **Cancel import** terminates
it during reading/checking and also discards an already checked result.
A 15-second watchdog stops the job, subject to browser timer scheduling.
Worker/load errors never fall back to synchronous import. The Editor stays
unchanged until **Apply checked package**; final confirmed adoption is not
another cancellable validation step. After cancelling, the identical file can
be selected again without reload. Split larger projects into smaller packages;
these budgets cannot be disabled.
Cancel stays in the same position when validation completes and Apply appears.
:::

::: info Repeated large-project imports on .177/.68
Checked for about 25 minutes on 19 October 2026 with App 0.1.327 and HA 2026.10.2:
60 series adoptions per host, with 36 fields and 360 or 720 nested Core/Bubble/
Mushroom Cards. Across both hosts, 238 cancellations during reading/checking or
after validation preserve the loaded draft; 116 identical-file retries pass.
Four actual HACS round trips are byte-identical. A valid package with 24 MiB of
total content completes validation. Three reload checkpoints per host pass;
original Editors and captured existing data are preserved.

This qualifies import in Windows Chrome. Browser-wide process memory includes
other tabs and does not establish isolated ATLAS memory stability. Actual HA
rendering of all 720 Cards and longer operation remain separate scopes.
Each confirmed import creates a local group; test groups were removed by
restoring the original complete configuration.
:::

::: warning Historical size finding with App 0.1.324
Checked on 19 October 2026 with App 0.1.324 and HA 2026.10.2 on .177/.68:
24 actual imports, including 16 valid adoptions at 112/112 and eight rejections.
Up to 30,008 files, 64 MiB of extra stored content and a 16-MiB README are
accepted. Deflate archives with 128 MiB of content or an almost 4-GiB declared
entry size, and truncated ZIPs, are rejected. Compression rejection is not a
size limit or a claim of zip-bomb protection.

Explicit byte/file-count limits and reliable cancellation of an active import
were missing in 0.1.324; the worker flow above now applies.
That old implementation reads the complete file before synchronous UI-thread
validation. Reload immediately after file selection preserves the original
draft in one attempt per host, but does not prove cancellation during CRC work.
Both complete original Editors and checked existing data are preserved.
Testing uses Windows Chrome, not a browser running on the Pi.
:::

::: info Safe HACS package adoption from App 0.1.324
Multiple embedded ATLAS projects or scripts are rejected before package selection.
HACS, package and Editor plan script filenames must agree; resource filenames,
custom element and Card types are cross-checked. Legacy resource prefixes remain
valid when they identify the same script file. Both the Reader and actual Editor
handler require fully approved readiness. A blocked or incomplete report cannot
overwrite the Editor. Valid JSON/YAML, root/dist layouts and single-word filenames
such as temperature.js remain supported. All 418 package tests, including 40 new
shipped-handler regressions, pass. Existing stored data is not migrated or rewritten.

Updates on .177/.68 with HA 2026.10.2 pass after fresh full backups: 60 actual
imports, 52 correct rejections and eight valid controls at 112/112. All 14 earlier
incorrect adoptions are blocked. After every case, reload and complete original
Editor exports match the backups; checked existing data, seven projects and six
plugins per host remain intact.
:::

::: warning Historical finding: ambiguous HACS packages through App 0.1.323
Native qualification on .177/.68 with HA 2026.10.2 finds 14 incorrect adoptions
among 46 imports. Six packages per host with multiple projects or extra scripts
are adopted despite a blocked report at 111/112. With same-identity projects,
ZIP entry order selects the content. A conflicting script name in the Editor
plan is even accepted at 112/112 on each host and copied into the Editor.
These cases are fixed from 0.1.324.

Exact duplicate paths, root/dist aliases and direct HACS/script mismatches are
correctly rejected: 26 rejections total; six valid controls remain importable.
CRC checks and accurate ZIP failure diagnostics remain intact. A blocked report
alone currently does not protect the Editor from these ambiguities. Use only
unambiguous exports; restore an overwritten draft from its original or backup.
Tests restore complete original Editors after every case and preserve checked
existing data. That earlier qualification kept ATLAS at 0.1.323.
:::

::: info Accurate ZIP failure diagnostics from App 0.1.323
CRC, header and ZIP readability errors make ZIP verification the first blocker.
A discarded inventory no longer produces invented missing-file claims. Dependent
file/content checks remain explicitly unverified until an intact archive is
available. Import stays blocked and the Editor state is unchanged. Actually
missing files in verified ZIPs still produce errors. The stable list retains
112 checks; all 378 package tests, including 54 integrity cases, pass.

Updates on .177/.68 with HA 2026.10.2 pass after fresh full backups: 60 rejections
and four valid JSON/YAML controls succeed. All 26 cases with unavailable ZIP
inventories show the ZIP cause first without invented missing-file claims.
Actually missing files remain detectable. Complete Editor configurations match
their backups after rejection/reload and after restoring valid import controls.
Checked existing data, seven projects and six plugins per host remain unchanged.
:::

::: info ZIP integrity checks from App 0.1.322
Before HACS adoption, ATLAS validates every stored ZIP entry's CRC32, including
README, locales and extra files. Local and central headers must agree on names,
flags, method, CRC and sizes; directory bounds, counts and overlapping entries
are checked. Corrupted archives expose no importable package data to the Editor.
All 52 new integrity cases and 376 package tests pass. Valid original archives
remain byte-identical, preserving empty names and outer whitespace. Native
updates from 0.1.321 to 0.1.322 pass on .177/.68 with HA 2026.10.2 after full
backups: 30 corrupt/invalid packages per host are rejected and two valid JSON/YAML
originals each pass at 112/112. After each rejection and reload, the complete
Editor configuration stays unchanged. The original CRC failure is rejected.
Original Editors and existing data, including seven projects and six plugins
per host, remain intact.

Import supports stored ZIP entries (STORE). Compressed entries, encryption, data
descriptors, multi-disk and ZIP64 are rejected. Normal ZIP comments remain valid.
CRC32 detects corruption; it does not authenticate a package or its source.
In 0.1.322, discarded inventories could produce misleading missing-file notices
after CRC failures. From 0.1.323, these dependent checks are marked unverified.
:::

::: warning Historical CRC finding through App 0.1.321
After fresh full backups, 21 actual Editor imports per host are checked on
.177/.68 with HA 2026.10.2. Missing, empty, whitespace-only or conflicting names
in HACS/package manifests, seven missing required files including declared
locales, unreadable/truncated ZIPs and broken manifest/package JSON are correctly
rejected in 19 cases per host. After each rejection and reload, the complete
Editor configuration is unchanged except its export timestamp. The valid control
package passes at 112/112 on both hosts.

A ZIP with modified README bytes and an invalid stored CRC is nevertheless
accepted at 112/112 on both hosts and replaces the local Editor state. An
independent ZIP reader confirms the CRC error. Readiness in 0.1.321 did not prove
complete ZIP integrity. CRC validation is corrected from 0.1.322 and confirmed on .177/.68; regenerate damaged
packages from an intact original. Both original Editors were restored exactly
from backups; existing files, projects, plugins and trash remain intact.
:::

::: info HACS title checks from App 0.1.321
Both title-presence checks now use the same package identity as manifest/script
consistency checks. An empty or whitespace-only first Entity name no longer
causes a false title failure. Original names and archives stay unchanged. All
324 local package tests pass, including 28 new JSON/YAML, standalone, stack,
Conditional and invalid-manifest checks. The four saved failing ZIPs and four
control packages pass unchanged at 112/112 and reexport byte-identically. Missing
or mismatched manifest names remain rejected. Native updates from 0.1.320 to
0.1.321 pass on .177/.68 with HA 2026.10.2 after fresh full backups. The four
original failing JSON/YAML ZIPs without a control card each reach 112/112 in the
actual Editor and reexport byte-identically. All eight cards retain exact names
and Conditional conditions after import and reload. Existing data, seven projects
and six plugins per host, and both original local Editors remain intact. This
check supplements the earlier HA rendering comparison; it creates no new HA
resources or dashboards.
:::

::: info Literal Entity names from App 0.1.320
Explicit Entity names remain unchanged during import: `name: ''`, whitespace-only
names and outer spaces/tabs. Only a missing name retains the previous fallback.
All 296 local package tests pass, including 37 new checks against the unparsed
original source, JSON/YAML, nested Conditionals, draft restoration, Card packages
and HACS. Deliberate renaming and entity selection remain available. Stored data
is not rewritten; recover previously normalized names from the original or backup.
Native updates from 0.1.319 to 0.1.320 pass on .177/.68 with HA 2026.10.2 after
full backups: 64 JSON/YAML file/paste cases with 128 captured outputs after import
and reload, plus 16 actual Card package roundtrips, retain original values exactly,
including nested Conditionals. Existing data and both original local Editors
remain unchanged. The subsequent native HACS check on both hosts passes with a
named control card before the eight name cases: four JSON/YAML ZIP roundtrips,
112/112 checks each and byte-identical reexports. Seventy-two exported/native HA
pairs match before and after reload (144 rendered card samples). DOM text retains
outer spaces/tabs; normal HA CSS visually collapses them, matching native cards.
Scripts and locales are loaded unchanged from the actual ZIPs; no new HACS
repository installation is included.
:::

::: warning HACS readiness gap through App 0.1.320
When the package starts with an empty Entity name, readiness reports 110/112:
`package-title-present` and `import-summary-title-present` fail despite a named
package. A whitespace-only first name also fails the title check. Name data stays
intact, but readiness is unreliable here. A named control card before the same
eight cases passes. The title check is fixed from 0.1.321 and confirmed natively
on .177/.68 with the original ZIPs. The native empty-string failure on 0.1.320 is reproduced;
the whitespace case follows from `trim()` in the check implementation.
:::

::: info Standalone Card correction from App 0.1.319
Conditional cards become complete Expert fields with their conditions and nested
cards intact. Standalone Entity cards retain their custom names; explicit renaming
and entity selection still work. All 259 local package tests pass, including 19
new checks of the actual Editor conversion, draft restoration and JSON/YAML/HACS
export. Stored data is unchanged. Recover previously lost content by reimporting
its original source or backup. Native updates on .177/.68 pass with HA 2026.10.2
after full backups: 32 cases retain original structure through JSON/YAML file/paste
imports and reload. Eight actual Card packages pass export, reimport and reload.
Existing data and both original local Editor configurations remain unchanged.
:::

::: warning Boundary through App 0.1.319
The parser still replaces `name: ''` with `Imported entity card` and trims outer
whitespace from Entity names. Sixteen additional controls confirm this behavior
on both hosts; they do not prove literal source-name preservation. Earlier local
tests compared values only after normalization. Normal custom names and Conditional
conditions pass on 0.1.319, correcting the corresponding 0.1.318 losses. This
increment includes no new native HACS ZIP or HA rendering test.
:::

::: info Import preview from App 0.1.318
Preview now uses the actual import parser, including nested cards and package/
export payload contents. Unsupported Markdown cards are rejected before the
Editor state changes; Markdown support is not added. Supported standalone
Entity and Conditional cards are also recognized as JSON, and YAML is checked
structurally. All 240 local package tests pass, including 27 new parity tests.
Native updates on .177/.68 pass after full backups:24 Markdown rejections through
file/paste import retain Editor code, and eight nested JSON/YAML imports preserve
structure. Existing data and original local Editors are preserved, including
after reload. The earlier standalone losses pass retesting on 0.1.319;
name normalization is fixed from 0.1.320 and passes native qualification on .177/.68.
:::

::: info Extended Conditional rendering checked on 2026-10-18
With ATLAS 0.1.317 and HA 2026.10.2, native references and scripts exported
from JSON and YAML agree in 1,008 visibility decisions: 14 variants, six state
cases and browser widths of 898 and 2560 CSS pixels on the two approved test
systems. Coverage includes implicit AND, nested AND/OR/NOT, `state`/`state_not`
lists, `entity_id`, strict numeric bounds including zero and entity references,
screen/user conditions and nested Conditional cards. Saving and reopening retain
JSON and YAML exactly. User checks cover the actual signed-in user and an excluded
test ID. Both formats also pass actual HACS reimport on both hosts: 112/112 package
checks each and byte-identical re-export. Original local Editors and captured
existing data are preserved; owned test artifacts are cleaned up and test files
remain recoverable in trash. This does not qualify every card or condition type:
this matrix uses Core
Entity leaves. An actual import rejected a Markdown leaf even though its preview
reported it as importable. New network tests are restricted to 192.168.178.177
and 192.168.178.68; earlier reports involving other hosts are historical evidence.
:::

## Report a problem (since 0.1.287)

Report a problem first creates a local preview. Copy report copies the reviewed
text; if clipboard access fails, the preview remains available for manual copying.
The GitHub button opens only the issue form with instructions. The report is
neither sent automatically nor embedded in the GitHub URL.

The filter removes credentials from structured fields, quoted JSON/YAML, URL
userinfo and token fragments, and removes the known HA session token from other
report text. Cookies and browser storage are not read; configured-key flags
contain only booleans. Still review card text, entities and personal information
before sharing. Opening the report does not change projects, settings or plugins.

The **ATLAS Home Assistant Card Editor** is the first visible reference
application in the ATLAS environment. It is used to design Home Assistant cards
visually, import existing YAML cards and prepare exportable card packages or
HACS-oriented bundles.

Since HA app **0.1.286**, reload and JSON/HACS import preserve template IDs and
resize reference dimensions. HACS bundles can be reimported when the project
name differs from the first card title: the two package manifest names are
compared. Card contents and existing settings remain intact.

The Administration → Plugin Hub → HA connection → Expert editor → export/import
workflow was verified in DE/EN/FR using a mock HA endpoint, an isolated browser
profile and a test plugin, including reload and container restart. This does
not replace verification against a live Home Assistant installation. Additional
native checks on Pi 5 and Proxmox are now complete; scope and remaining limits are recorded in
[Development Status](/en/projects/atlas/development-status).

The local demo uses:

```text
http://127.0.0.1:4174/
```

Connection settings are managed through Atlas Administration:

```text
http://127.0.0.1:4175/
```

## Expert Workflow

The editor now opens directly in the Expert workflow. The former visible
Simple mode and the Simple/Expert switch have been removed. Import, HA card
import, YAML paste, resource debug and entity selection remain available as
tools.

Cards are placed from the left card list onto a Home-Assistant-like grid
surface. They can be moved, edited, nested and exported as Home Assistant YAML.

## Home Assistant Connection

The Card Editor can receive a Home Assistant URL and access token from Atlas
Administration. The token is not written permanently into the editor; it is only
used as a session handoff.

The editor currently supports:

- connection through the Home Assistant WebSocket API
- loading entities through `get_states`
- local cache for entities and entity domains
- synchronization status below the connection state
- search and filtering by domain, name or entity ID
- Lovelace resource checks through the browser WebSocket and Admin WebSocket proxy

The resource debug panel can be enabled through `Show resource debug`. It shows
whether the browser WebSocket, the Admin WebSocket proxy or a fallback is stuck.

## Card List

The Expert card list contains Core cards and detected Community cards. It can
show local templates, known HACS resources and scan-only resources.

Supported base cards include:

- Entity
- Entities
- Overview / Glance
- Button
- Grid
- Sensor
- Vertical stack
- Horizontal stack
- Thermostat
- Link
- Webpage
- Mushroom Template
- Bubble Card
- Tabbed Card V2

Scan-only entries are registered Lovelace resources for which ATLAS does not
yet include a built-in card mapping. They can be mapped locally to the matching
`custom:*` Lovelace card type. After that mapping, they become active custom
cards in the palette, can be placed through drag and drop and keep their
resource path when resource snippets are exported.
Palette entries that are not useful as cards, such as JavaScript helper
resources, can be marked as hidden locally. Hidden cards disappear from the
normal list, remain visible in the full list and can be restored from there.
The import tools also include an opt-in automatic card type mapping option. It
tries to derive a `custom:*` card type for unknown registered resources from the
JavaScript filename and therefore carries a red safety warning.

## Container Cards

Expert mode supports container cards for:

- `vertical-stack`
- `horizontal-stack`
- `custom:tabbed-card-v2`

Cards can be placed into these containers through drag and drop. Tabbed Card V2
manages tabs and the cards contained in each tab. Stack cards keep their
contained cards as separate elements and show them as a text list in the info
box.

## Import

The editor can import Home Assistant card configurations from:

- YAML files
- YAML from the clipboard
- JSON
- ATLAS Card Packages
- HACS bundles with embedded `atlas/*.atlas-card.json`

During import, ATLAS detects `card_mod` and `uix` styles. Entity styles are
assigned to the matching entities; global styles remain visible as their own
style block. The original YAML should stay as close as possible to the imported
source and only change when the user edits the card.

Hand-written `custom:tabbed-card-v2` cards with `tabs[].card`, nested
`horizontal-stack`/`vertical-stack` sections and raw custom cards are detected
and opened directly in Expert mode as a container structure.

## Export

The editor can create several artifact types:

- Home Assistant YAML
- Expert HA card YAML
- Card script
- Card package
- HACS-oriented bundle
- resource list

When exporting an HA card, users can choose whether styles are written as
`card_mod` or `uix`. Export filenames receive a Windows-style counter when a
name already exists.

### Verified HACS bundle round trip

App **0.1.307** qualifies a mixed Core/Bubble/Mushroom project with isolated
HA Core **2026.10.1**: ZIP import, actual browser download, reimport and re-export
preserve fields, grid metadata and card configuration. The re-exported ZIP is
byte-identical in this test. Bundle checks compare the project name with the
verified package name; distinct child-card names no longer cause false conflicts.

The exported script renders in real HA with Bubble **3.4.2** and Mushroom
**5.2.3**, including live state changes. HA uses generated stacks; preserved grid
metadata does not guarantee identical pixel geometry. The isolated resources
were served through `/local/`; this does not qualify HACS repository downloads.

### Language files in the exported script

From App **0.1.308**, generated Card scripts load `locales/en.json` and the
selected language relative to their own script URL. Deploy JavaScript and its
sibling `locales/` folder together on the same HA origin; register the Lovelace
resource as type `module`. Cards follow the HA language. Override it with
`language: de` or `language: fr` in the Card configuration; regional values such
as `de-DE` and `fr-FR` use their base language.

The title, demo-entity hint and script-owned error message use the locale file.
Missing, invalid or partial translations fall back per field to `en.json`, then
embedded EN. The script also works without language files. A distinct explicit
`title` or `replacement_hint` takes priority. Authored field names and entity IDs
remain unchanged; HA translates HA/community labels. Each language loads once
per page visit. Reload after editing files; after script updates, use a new
version query on the resource URL if necessary.

EN/DE/FR exports are independent of the editor language. Without an executed
translation adapter, DE/FR contain marked English fallbacks requiring translation
and review.

### Combined HACS delivery from 0.1.309

The export ZIP contains root `hacs.json`, with script and languages under
`dist/`, for example `dist/energy-kitchen.js` and `dist/locales/en.json`.
Extract the complete ZIP into a dedicated GitHub repository named
`energy-kitchen` and add it to HACS as a Dashboard repository. Match the
repository name to the script filename without `.js`; use a separate repository
from the ATLAS integration.

HACS installs `dist/` contents into `www/community/energy-kitchen/`. The module
resource is `/hacsfiles/energy-kitchen/energy-kitchen.js`, with JSON files in its
sibling `locales/` folder. HACS registers the module in storage mode; in YAML
mode, add the resource documented in the bundle yourself.

Do not also place the script at repository root or attach a standalone JavaScript
release asset: HACS can prefer it over `dist/`. The export ZIP is not a
`zip_release` installation asset. HACS 2.0.5 can omit language files when the
script filename begins with `dist`; ATLAS blocks that export with a message.
Choose another HACS script filename. Existing projects remain intact.

The real GitHub/HACS flow is also verified in isolated HA 2026.10.1 with
HACS 2.0.5: user-approved GitHub device authorization, custom Dashboard
repository registration and download from `main`. The script and EN/DE/FR
install with exact GitHub bytes; HACS registers the module automatically.
Legacy ATLAS bundles remain importable.

The public [Card export repository](https://github.com/rockbaer2007/atlas-hacs-delivery-card)
is explicitly a test example. In the HACS main menu, open **Custom repositories**,
enter that GitHub address, select **Dashboard** and choose **Add**. Open
**Locale test card**, confirm **Download**, then reload the browser. Its resource is
`/hacsfiles/atlas-hacs-delivery-card/atlas-hacs-delivery-card.js`.
In `v0.1.0`, DE/FR are marked English fallbacks. `v0.1.1` contains manually
translated test strings: “Wohnzimmer 0.1.1” and “Salon 0.1.1”. This does not
demonstrate automatic translation. Bubble Card and Mushroom are additionally
required for its mixed example Card.

The tagged cycle `v0.1.0` → `v0.1.1` → `v0.1.0` is also verified in isolated
HA 2026.10.1/HACS 2.0.5. Save a full backup first. In the repository menu, choose
**Update information**. HACS detects the new version as a pending update;
use **Redownload** to install the offered version, then reload the browser.
For the verified manual reinstallation of the old version, open **Redownload**,
expand **Need a different version?**, choose `v0.1.0` under **Release**,
download and reload again. HACS explicitly recommends restoring a backup rather
than using this version selector to roll back. Reinstallation replaces Card
files; it does not restore migrated data from a backup.

Both releases use `dist/` without a standalone JavaScript release asset.
The script and all three locale files match the selected tag exactly after
each step. The module resource retains its ID; HACS changes its `hacstag`.
Other resources, settings, projects and dependencies remain intact. The old
version also works after restarting the test system.
HACS still offers `v0.1.1` as an update afterwards; selecting the old version
does not permanently pin it.

This is custom registration, not inclusion in the central HACS default list.
Pi 5 and Proxmox were unchanged.

### Failed and interrupted updates

From ATLAS **0.1.310**, newly generated Card scripts check EN and all languages
selected for export, including inactive languages. Missing, unreadable or invalid
JSON files with mismatched language metadata produce a compact notice listing
the affected paths. Its EN/DE/FR repair text is embedded independently of those
files. Cards and live states remain usable with the existing language fallback.

In HACS, redownload the complete Card package and reload the browser; restore
your backup if needed. The notice disappears after successful repair and reload.
Existing installed scripts need re-exporting and redistribution. This detects
missing/unreadable files.

From **0.1.311**, newly exported scripts and locales also share a deterministic
package marker (`_meta.packageId` in locale files). A different or missing marker
also triggers the repair notice; affected text is ignored, retaining EN or embedded
English fallback. Keep the marker when translating. Do not copy markers between
packages to suppress warnings. This detects accidental mixed exports, not tampering
or text changes retaining the marker; it is not a signature. Identical exports
have the same marker. Old scripts are not retroactively changed. There is no
automatic repair or recovery.
The new package check is first verified in isolated HA 2026.10.1/HACS 2.0.5:
mixed EN/FR, missing markers, continued Card rendering and repair after reload.
Pi 5 and Proxmox remained at 0.1.310 during that isolated qualification.

The App update and package check are subsequently tested on both hosts with
0.1.311: own `/local/` Cards, mixed EN/FR, missing FR marker and repair after
reload. Existing settings, projects and checked files remain intact. Separate
historical finding: File Studio trash lived in the replaceable App container.
Only our previous test folders existed there; they were reconstructed from PC
copies with original metadata. App 0.1.312 corrects storage, with isolated
container replacement and backup recovery verified. Before the first update,
copy the legacy stores inside the old container and back up the prepared data;
see [File Studio](../atlas-plugins/file-studio.md). Subsequent native legacy
adoption and the 0.1.312 upgrade also pass on Pi 5 and Proxmox with data preserved.
This is not another native HACS repository installation test.

The 0.1.310 update and this check are also tested on Proxmox and Pi 5 after fresh
backups: separate newly generated test Cards, missing FR and EN, then restoration
after reload, with settings, projects and external plugins preserved. Native
verification uses separate `/local/` test resources, not another GitHub/HACS
installation. Temporary read failures can also trigger the notice; an initial
preview notice on Proxmox cleared after a fresh reload. A notice alone does not
prove permanent file corruption.

Failures were injected into a dedicated isolated HA 2026.10.1/HACS 2.0.5 clone:
the new script was really downloaded from GitHub and written, then locale
downloads reported failure or the process was killed before they completed.
Only this HACS test clone contained the test instrumentation.

On a reported download error, HACS shows an error and automatically restores
the old Card including EN/DE/FR. A hard process interruption instead leaves the
new script with missing locale files, even after restart. HACS can still show
the old installed version. Embedded EN fallback can keep the Card visible;
rendering and the version label alone do not prove a complete installation.

After removing the fault, **Redownload** with the known old release was verified
successfully. Reload the browser afterwards and check the script, every locale
file, resource registration and rendering. A separate full Docker HA configuration
snapshot was also restored into a new empty test volume: all 2,500 saved files
matched before startup; HACS, Cards and live states worked again afterwards.
Settings, dashboard and dependencies remained intact.

The temporary HACS backup does not replace your own backup. Automatic repair
after process interruption is not guaranteed. This is a controlled fault test
and Docker volume restoration, not proof for every network/storage failure,
HAOS backup restoration or other HACS versions.

## Tabbed Card V2

Tabbed Card V2 is handled as its own ATLAS card and exports as:

```yaml
type: custom:tabbed-card-v2
```

Expected resource:

```text
/hacsfiles/tabbed-card-v2/tabbed-card-v2.js
```

Export prerequisite: **ATLAS Tabbed Card V2** must be installed in Home
Assistant. It belongs to the ATLAS plugin/card line and is provided through the
ATLAS repository:

`https://github.com/rockbaer2007/atlas`

The editor notes that Tabbed Card V2 is its own card. It is inspired by the
original `kinghat/tabbed-card`, but maintained as a separate ATLAS variant.

The built-in Home Assistant editor for the card accepts YAML or JSON directly.
Multi-line YAML blocks such as `>-` and `|-` stay multi-line values, so Mushroom
template chips, Jinja expressions and `card_mod` styles are not destroyed when
the code is applied.

Opacity values for active and inactive tab backgrounds are rendered as stable
color values before switching tab content. This keeps transparent tab
backgrounds consistent after moving between tabs.

### Tabbed Card V2 Styling

Tabbed Card V2 keeps the Material tab variables and adds dedicated variables
for tab backgrounds, radii and spacing:

| Name | Default | Description |
| --- | --- | --- |
| `--mdc-theme-primary` | `--primary-color` | Active tab text, indicator and accent color. |
| `--mdc-tab-text-label-color-default` | `--secondary-text-color` | Inactive tab text color. Use an `rgba(...)` value with alpha when transparency is needed. |
| `--mdc-typography-button-font-size` | `14px` | Tab label font size. |
| `--tabbed-card-v2-card-background` | Home Assistant card background | Background of the outer card. Use `transparent` for a glass/overlay layout. |
| `--tabbed-card-v2-card-border` | Home Assistant card border | Border of the outer card. |
| `--tabbed-card-v2-card-border-radius` | Home Assistant card radius | Border radius of the outer card. |
| `--tabbed-card-v2-content-padding-side` | `0` | Equal left and right spacing inside the card content area. |
| `--tabbed-card-v2-content-padding-bottom` | `0` | Bottom spacing inside the card content area. |
| `--tabbed-card-v2-tabbar-background` | `transparent` | Background of the whole tab bar. |
| `--tabbed-card-v2-active-background` | `transparent` | Background of the active tab. |
| `--tabbed-card-v2-active-background-opacity` | `100` | Active tab background opacity from `0` to `100`. |
| `--tabbed-card-v2-inactive-background` | `transparent` | Background of inactive tabs. |
| `--tabbed-card-v2-inactive-background-opacity` | `100` | Inactive tab background opacity from `0` to `100`. |
| `--tabbed-card-v2-hover-background` | `--secondary-background-color` | Background while hovering or focusing a tab. |
| `--tabbed-card-v2-tab-border-radius-top` | `0` | Top-left and top-right radius for each tab. |
| `--tabbed-card-v2-tab-border-radius-bottom` | `0` | Bottom-left and bottom-right radius for each tab. |
| `--tabbed-card-v2-tabs-padding-left` | `0` | Space before the first tab. |
| `--tabbed-card-v2-tabs-padding-top` | `0` | Space above the tab row. |
| `--tabbed-card-v2-tabs-gap` | `0` | Space between tabs. |
| `--tabbed-card-v2-indicator-inset` | `0` | Horizontal inset for the active tab indicator. |
| `--tabbed-card-v2-indicator-border-radius` | `0` | Border radius for the active tab indicator. |

![Tabbed Card V2 styling in the Home Assistant editor](/images/atlas/tabbed-card-v2-0.1.7.png)

![Tabbed Card V2 result with rounded tabs](/images/atlas/tabbed-card-v2-result-0.1.7.png)

Example:

```yaml
type: custom:tabbed-card-v2
styles:
  --mdc-theme-primary: "#ff9800"
  --mdc-tab-text-label-color-default: "rgba(255,255,255,0.75)"
  --tabbed-card-v2-card-background: "transparent"
  --tabbed-card-v2-card-border: "0.2px solid var(--primary-color)"
  --tabbed-card-v2-card-border-radius: "12px"
  --tabbed-card-v2-content-padding-side: "16px"
  --tabbed-card-v2-content-padding-bottom: "16px"
  --tabbed-card-v2-tabbar-background: "rgba(0,0,0,0.18)"
  --tabbed-card-v2-active-background: "#ff9800"
  --tabbed-card-v2-active-background-opacity: 35
  --tabbed-card-v2-inactive-background: "#ffffff"
  --tabbed-card-v2-inactive-background-opacity: 8
  --tabbed-card-v2-hover-background: "rgba(255,255,255,0.12)"
  --tabbed-card-v2-tab-border-radius-top: "12px"
  --tabbed-card-v2-tab-border-radius-bottom: "6px"
  --tabbed-card-v2-tabs-padding-left: "8px"
  --tabbed-card-v2-tabs-padding-top: "8px"
  --tabbed-card-v2-tabs-gap: "6px"
  --tabbed-card-v2-indicator-inset: "10px"
  --tabbed-card-v2-indicator-border-radius: "999px"
tabs:
  - attributes:
      label: Light
    card:
      type: button
      entity: light.bed_light
```

## Current Status

::: info Native 0.1.317 update and combined project verified on Proxmox and Pi 5
Following fresh HA backups, both native updates and the nested Core/Bubble/
Mushroom project pass save/reopen, YAML/JSON, actual HACS re-import and
byte-identical re-export with 112/112 package checks per host. Missing numeric
Conditional bounds are rejected; `above: -1`, Jinja and CSS survive. Conditional
rows hide at -2 and return at 18. Text, SVG icons and colors change live.
756 computed-CSS comparisons match native reference cards. Two light/dark
switches per host preserve all 19 observed instances without reload. Editors
reconnect automatically after ordered HA Core restarts; fresh Jinja updates work
without reload. The Pi's brief intermediate connection state was not sampled;
its subsequent connection and updates are verified. Scope: Chrome on the PC,
HA 2026.10.1, Mushroom 5.2.3, existing UIX 8.4.0/Bubble 3.4.2 on Proxmox and
separate temporary Card-Mod 4.2.1/Bubble 3.4.1 on Pi. Regular card views provide
the CSS reference; HA panel views may override radii. Original local Editor
states and default themes are restored; test files remain recoverable in Trash.
Regenerate earlier exported scripts to include the correction.
:::

::: info Combined project qualification passes in isolation with 0.1.317
Conditional imports retain complete condition data, including numeric bounds
such as `above: -1` and `below: 0`, state lists and nested logical conditions,
through YAML/JSON and HACS. Missing or invalid numeric bounds block import and
package readiness with an explanation. The combined project passes save/reopen,
actual HACS re-import with byte-identical re-export, dynamic Jinja text/icons/
colors, conditional hide/show, eight live theme transitions and 972 CSS
comparisons. Both Editors reconnect without page reload after HA shutdown/start;
fresh template updates work. Card-Mod 4.2.1 and UIX 8.4.0 are tested separately
with HA 2026.10.1, Bubble 3.4.2 and Mushroom 5.2.3 in Chrome on the PC. Existing
data is preserved; that isolated check left Pi 5 and Proxmox at 0.1.316. Previously lost
bounds require the original source/backup; regenerate existing scripts.
This is not a complete validator for every HA condition type.
:::

::: info Live theme switches verified on Proxmox and Pi 5 on 2026-10-17
After fresh HA backups, switches without reload also pass on both hosts with
ATLAS 0.1.316 and HA 2026.10.1: Card-Mod 4.2.1 and UIX 8.4.0 separately,
Mushroom 5.2.3, Bubble 3.4.2 on Proxmox or 3.4.1 on Pi. Twelve native/generated
Core, Bubble and Mushroom cards per host/engine make seven custom/default
theme transitions. 1,920 computed-CSS comparisons pass; document and Card
instances remain unchanged. Inherited colors/radii follow the theme while
fixed overrides remain intact. Fixture buttons use HA's native theme handler.
Setup and engine changes are outside the measured sequences without reload.
Original default themes and extension configuration are restored; existing
files, projects and plugins remain intact. Native checks use passive sensors
and Chrome on the PC, not an ARM64 browser benchmark.
:::

::: info Live theme switches qualified in isolation on 2026-10-17
With ATLAS 0.1.316 and HA 2026.10.1, mounted Core, Bubble and Mushroom cards
switch between light and dark without reloading or rebuilding the cards.
Card-Mod 4.2.1 and UIX 8.4.0 are tested separately with Bubble 3.4.2 and
Mushroom 5.2.3: seven transitions per engine across custom/default themes,
960 computed-CSS comparisons in total. Inherited colors/radii change while
explicit child overrides stay fixed. Native references and generated scripts
match; document and Card identities remain stable throughout.
Isolated fixture controls use HA's native theme handler; profile navigation
and reload are outside the measurement sequence. Existing data, nine projects
and original files remain intact. Pi 5 and Proxmox were neither queried nor
changed. Other themes, browsers and versions need separate checks; this does
not repeat the actual Editor/HACS UI roundtrip.
:::

::: info Bubble CSS and UIX inheritance fixed in 0.1.316
0.1.315 dropped Bubble CSS supplied as a string under `styles: |` on normal
YAML/JSON import. 0.1.316 preserves the text, whitespace, newlines and empty
strings through single/nested cards, HACS export and reimport. Existing `styles`
objects remain supported.

Newly generated scripts use the native Home Assistant card wrapper for roots
with `uix`/`card_mod`. UIX can then style a root stack without its own `ha-card`
and its CSS variables reach child cards. Style blocks are neither flattened
nor copied onto unrelated cards.

Isolated verification: HA 2026.10.1, Bubble 3.4.2, Mushroom 5.2.3, UIX 8.4.0.
Core/Bubble/Mushroom match native references in light/dark and after reload
(180 computed-CSS comparisons). Distinct green/purple parent accents now
inherit correctly instead of falling back to a different color. Bubble overrides
retain background, 3-px border and 9-px radius. Save/reopen and HACS UI
reimport/re-export pass; 112/112 package checks and byte-identical ZIPs supplement
the visible verification.

**Existing Cards:** after updating, export the original project again and replace
the script together with its matching locales. Reimport previously lost Bubble
CSS from the original YAML/JSON or a backup; the update cannot reconstruct
discarded content. Stored projects/files are not rewritten automatically.
After fresh HA backups, the 0.1.315 to 0.1.316 update also passes on Proxmox
and Pi 5: six Core/Bubble/Mushroom cards per host with UIX 8.4.0, HA 2026.10.1,
Mushroom 5.2.3 and Bubble 3.4.2 (Proxmox) or 3.4.1 (Pi). 240 computed-CSS
comparisons including reload pass. YAML/JSON styles are preserved; HACS
re-exports are byte-identical and each passes 112/112 package checks.
Original complete local Editor configurations are restored. Native checks use
the existing dark theme and passive sensors. Other HA/styling versions need
separate checks. Isolated mounted-Card theme switches are documented above.
:::

::: info Native CSS qualification on Proxmox and Pi 5, 2026-10-17
After fresh HA backups and additional ATLAS file copies, Card-Mod 4.2.1 and
UIX 8.4.0 were also tested separately on both real hosts: HA 2026.10.1,
Mushroom 5.2.3, ATLAS App 0.1.315. Generated ATLAS scripts match native
references for dynamic Jinja colors/borders, 3px shadow DOM spacing, background
and radii. Colors change at natural minute boundaries without reload. Only
passive sensors and separate test cards are used; no devices are controlled.

UIX applies the 17px radius and prefers `uix` when both blocks exist (37px
instead of 31px). Card-Mod ignores `uix`. Neither engine applies the 7px padding
in `uix_style`. Reload passes with both extensions. Existing browser scaling
may round computed border widths to physical pixels; export and reference
remain identical.

Switching engines requires HA restarts. Existing Proxmox UIX is re-enabled
afterward; the additional Pi integration and separate test resources are
removed after qualification; own test files remain in recoverable trash.
Settings, original files, four existing ATLAS
projects per host and six plugins are preserved. There is no new ATLAS release.
This covers the named versions and rules, not arbitrary CSS or every theme.
:::

::: info CSS rendering checked in isolation, 2026-10-17
With App 0.1.315, HA 2026.10.1 and Mushroom 5.2.3, **Card-Mod 4.2.1** and
**UIX 8.4.0** were tested in separate HA instances. Generated ATLAS scripts
match the computed styles of equivalent native cards: Jinja color and a 4px
border change blue → red → blue without reload; shadow DOM letter spacing is
3px. The UIX radius is 17px. A Core reference confirms background, a 6px border
and a 23px radius. Reload and restart pass; unstyled cards sharing the entity
remain unaffected. Pi 5 and Proxmox were not changed for this check.

**Limits:** imported `uix_style` data is preserved but has no CSS effect in
these versions. Use `uix: { style: ... }` for UIX. When both `card_mod` and
`uix` exist, UIX prefers `uix`; ATLAS does not merge them. Card-Mod does not
execute `uix`. The UIX export choice converts structure, not CSS selectors or
Jinja variables. The earlier fixture name “UIX legacy” was only a card label,
not evidence of a supported alias.

Use `config.entity` in these extensions' **CSS templates**; Mushroom's own
text/icon/color templates can use `entity`. `mushroom-state-info$` does not
match this Mushroom version. The tested selector is `ha-tile-info$`; internal
DOM structures can change.

```yaml
type: custom:mushroom-template-card
entity: input_boolean.your_test_entity
primary: "{{ 'On' if is_state(entity, 'on') else 'Off' }}"
card_mod: # Use uix: with UIX instead
  style:
    .: |
      ha-card {
        border: 4px solid {{ 'red' if is_state(config.entity, 'on') else 'blue' }};
      }
    ha-tile-info$: |
      .info { letter-spacing: 3px; }
```

Load Card-Mod as a frontend module. Install UIX as an integration, add it under
**Devices & services**, then reload the page. Do not load both extensions:
see [UIX migration](https://github.com/Lint-Free-Technology/uix/blob/v8.4.0/docs/source/faq.md),
[UIX setup](https://github.com/Lint-Free-Technology/uix/blob/v8.4.0/docs/source/quick-start.md)
and [Card-Mod](https://github.com/thomasloven/lovelace-card-mod/tree/v4.2.1).
This covers the stated rules, not arbitrary CSS or every theme. Original
templates and existing data are backed up; only separate fixture copies were
adjusted. No ATLAS runtime code change was needed.
:::

::: info Native 0.1.315 update verified on Proxmox and Pi 5, 2026-10-17
After fresh HA backups, both hosts pass the 0.1.313 to 0.1.315 update and
export/re-import checks: YAML/Card-Mod and JSON with UIX export each achieve
112/112 package checks and byte-identical re-export. Root and card styles,
multiline CSS, shadow DOM selectors, Jinja and `uix_style` retain their exact
ownership. Style objects in the generated script match package contents.

Existing settings, files, three previous server projects per host, six active
plugins, trash and history are preserved. Complete local Editor configurations
are restored exactly; new test projects remain separate. Direct Hub and embedded
Runtime panel still show six active plugins. HA remains 2026.10.1 and the
integration 0.1.306. No HA dashboards, resources or device tests were created.
Arbitrary CSS execution by Card-Mod/UIX remains separate qualification against
the installed styling extensions.
:::

::: info Imported Card-Mod/UIX styles from 0.1.315, checked in isolation on 2026-10-17
Imported `card_mod`, `uix` and `uix_style` objects remain on their own cards
in the Editor, YAML/JSON, HACS package and generated script. Nested cards,
multiline CSS, shadow DOM selectors and Jinja values survive. Cards sharing an
entity do not receive each other's styles. YAML and JSON HACS roundtrips pass
112/112 checks and byte-identical re-export; direct JSON single-card import
also passes in the browser.

The **uix:** export choice converts `card_mod` properties structurally to `uix`,
including JSON and scripts. Existing `uix`/`uix_style` objects are preserved.
If a card already has `uix`, both blocks are retained without overwriting or
merging. **card-mod** preserves imported keys; it does not convert UIX back.
This verifies data preservation, not arbitrary CSS execution in every
Card-Mod/UIX version. Configure the required styling extension in HA.

Existing files, projects and plugins remain unchanged. Styles already discarded
by older versions require re-importing the original file or a backup.
That isolated check left Pi 5 and Proxmox untouched; the subsequent native
qualification is documented separately above.
:::

::: info YAML/JSON HACS roundtrip from 0.1.314, checked in isolation on 2026-10-17
Choose YAML or JSON under **Card format**, export the HACS bundle, then import
the complete `.hacs.zip` through **Import HA card**. Both formats pass the same
112 package checks. The selected format, Editor fields and Mushroom text, icon
and color templates, including multiline values, survive; re-exporting produces
identical bytes within each format.

The `atlas/*.atlas-card.json` envelope and locale files remain JSON;
`manifest.format` describes the enclosed YAML or JSON card source. The generated
script remains JavaScript. Existing valid YAML bundles need no conversion.
The diagnostic code is now `package-format-supported`, replacing
`package-format-json`. Malformed contents and missing locales are still rejected.
The missing imported `card_mod` styles found in that test are fixed from
0.1.315, as described above.
Pi 5 and Proxmox were untouched; their 0.1.314 update remains unqualified.
:::

::: info Mushroom import fix in 0.1.313, checked in isolation on 2026-10-17
Normal YAML/JSON imports preserve `primary`, `secondary`, `icon`, `color` and
legacy `icon_color` for single and nested Mushroom Template Cards. Single cards
retain their Mushroom type. Multiline YAML retains indentation and blank lines;
malformed YAML is rejected.

Saving, reloading and HACS-bundle export/import retain the tested expressions.
In HA 2026.10.1 with Mushroom 5.2.3, exported cards change their text, icons and
colors with fixture states and reconnect automatically after a transport outage.
HA evaluates Jinja; ATLAS preserves its source. Apply title deliberately replaces
`primary`; changing the entity preserves the other templates. Values already
lost through older imports require the original source to recover. Keep original
YAML/JSON files.

This qualifies the named properties and fixtures, not arbitrary Mushroom options
or Jinja programs. Legacy `icon_color` is checked for preservation; runtime tests
use current `color`. No Jinja authoring controls are added. Existing data remains
intact; the isolated correction check left Pi 5 and Proxmox unchanged.
:::

::: info Native 0.1.313 update verified on Proxmox and Pi 5, 2026-10-17
After fresh HA backups and PC file mirrors, all four import paths pass on both
hosts: YAML/JSON, single cards and stacks. Text, icon and color templates retain
their exact source, including blank lines. Save/open and actual HACS export/import
pass; each re-export is byte-identical and JSON package readiness passes 112/112.

Real unsaved HA previews change text, icon glyphs and computed colors on natural
Jinja minute boundaries without reload. Only passive sensor states are read;
no devices are switched. Original 225/229 ATLAS files, two existing server
projects per host, six plugins, settings, trash and history remain intact.
Both complete local Editor configurations with 36 fields are restored exactly
except for the export timestamp. Own test projects remain separate. Integration
stays 0.1.306; this check requires no HA restart. This does not qualify arbitrary
Mushroom options or Jinja programs.
:::

::: info Isolated 60-minute soak on 2026-10-17
ATLAS 0.1.312 with HA 2026.10.1 passed a full hour using 36 distinct local
fixture entities: twelve Core, twelve Bubble and twelve Mushroom cards.
720 update batches made 10,080 successful service calls and requested 25,920
target updates without service failures. Both browser views reconnect
automatically after 15-, 45- and 90-second transport outages without reloading
during the hour. All fields/cards remain; all 36 final HA states match.
Saving, reopening and actual browser export/import pass; both exports are
byte-identical. Original fixture files, projects, plugin settings, trash and
history remain intact. Full ATLAS process-group samples, starting during minute
six, range from 168.1 to 168.6 MiB; HA container samples over the hour range
from 652 to 681 MiB. Chrome was measured globally, including other tabs;
these results do not establish per-card browser memory usage.
The hour uses a generated fixture package; the actual browser export is compared
separately afterwards. Authored dynamic Mushroom Jinja text, ARM64 performance
and production capacity remain outside this check. Pi 5 and Proxmox were
neither queried nor changed.
:::

::: info Native 36-card workflow on Proxmox and Pi 5 on 2026-10-16
After fresh HA backups, ATLAS 0.1.312 and HA 2026.10.1 passed twelve Core,
twelve Bubble and twelve Mushroom cards on each host. Saving, reloading,
reopening and importing the actual browser export retain all 36 fields and
the card configuration. Both exports per host are byte-identical with the same
EN/DE/FR selection. Original local Editor configurations were restored and
compared in full afterwards.
Following a real Proxmox VM reboot and a user-performed Pi LAN interruption,
the existing Editors reconnect without reload; the HA views still show all
36 cards without error cards. This host check uses passive existing sensors,
without the isolated test's 360 synthetic state changes. Chrome on the PC
renders the cards; this is not an ARM64 browser or CPU/RAM benchmark.
Existing ATLAS files, projects, plugins, trash and history remain intact.
A changed HACS query parameter on the existing selfhst resource was separately
observed after the VM reboot and retained.
:::

::: info Larger project qualified in isolation on 2026-10-16
ATLAS 0.1.312 and HA 2026.10.1 passed a 36-field Expert project: twelve each of
Core, Bubble and Mushroom cards using two local fixture entities. Saving,
reloading and opening the server project, plus HACS-bundle export/import, retain
all fields and card configuration. Repeated exports with identical language
options are byte-identical. HA renders all 36 cards without error cards.
During 360 state changes over just above three minutes, the Editor and, for the
longest outage, the HA view reconnect automatically after transport outages of
about 12, 24 and 62 seconds. Existing fixture data remains intact. Pi 5 and
Proxmox were neither queried nor changed. This is a bounded functional test,
not a hardware benchmark or proof of arbitrary project sizes.
The actual browser export was checked as a complete package at a fresh resource
path. Manual replacement at the same URL may mix a cached old script with new
locale files and trigger the repair notice.
:::

The Card Editor is in active development. Expert workflow, import/export,
entity selection, resource checks, container cards and local custom-card
mappings for scanned Lovelace resources are already testable. Additional
reviewed custom-card mappings will be added step by step.
