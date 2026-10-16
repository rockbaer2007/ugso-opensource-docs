---
title: Home Assistant Card Editor
description: Dedicated documentation for the ATLAS Home Assistant Card Editor with the Expert editor, import, export, resource checks and Home Assistant connection.
---

# Home Assistant Card Editor

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
not replace verification against a live Home Assistant installation. A5 adds
native checks on Pi 5 and Proxmox; scope and limits are recorded in
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
Pi 5 and Proxmox remain unchanged at 0.1.310 during this qualification.

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

The Card Editor is in active development. Expert workflow, import/export,
entity selection, resource checks, container cards and local custom-card
mappings for scanned Lovelace resources are already testable. Additional
reviewed custom-card mappings will be added step by step.
