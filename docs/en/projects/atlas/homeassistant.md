# ATLAS and Home Assistant

ATLAS includes its own `@atlas/homeassistant` package for Home-Assistant-oriented
integration. The current focus is an editor and export workflow for Home
Assistant cards, live entities and later HACS-oriented usage.

The detailed user and feature documentation for the editor now lives on the
dedicated [Home Assistant Card Editor](./card-editor) page.

## Current Scope

- ATLAS Status Preview with Theme and Renderer integration
- local and live Home Assistant entities
- connection through the Home Assistant WebSocket API
- token management in Atlas Administration with handoff and optional auto-connect to the active editor session
- loading entities through `get_states`
- loading Lovelace resources through `lovelace/resources`
- shared entity catalog for type filters and search
- card targets for built-in Home Assistant cards, Mushroom Template and Bubble Card
- Expert editor with 12-column grid, drag and drop, resizing and container cards
- container cards for `vertical-stack`, `horizontal-stack` and `custom:tabbed-card-v2`
- card import through JSON/YAML, file upload, clipboard and HACS bundles
- detection of `card_mod` and `uix` styles during import
- `single`, `horizontal-stack`, `vertical-stack`, `grid`, `conditional` and `tabbed-card-v2` layouts
- JSON and YAML export for Home Assistant cards
- Atlas Card Packages and HACS-oriented bundles for editor roundtrips
- import summaries for imported cards

## Working Shortcuts

Short chat commands are used during ongoing ATLAS editor work to trigger
repeated actions quickly:

| Shortcut | Meaning |
|---|---|
| `??` | answer only, do not implement |
| `>>` | implement the described step completely |
| `>>!` | execute and provide a short summary |
| `<<` | undo the last change |
| `!!B` / `!!b` | create a backup of the current state |
| `!!D` / `!!d` | update the open-source documentation |

Shortcuts can be combined. For example, `!!D !!B` means that the current state
is backed up and the public documentation is updated where appropriate.

## Supported Card Targets

| Selection | Home Assistant type | Dependency |
|---|---|---|
| Entities | `entities` | built into Home Assistant |
| Mushroom Template | `custom:mushroom-template-card` | Mushroom |
| Bubble Button | `custom:bubble-card` | Bubble Card |
| Tabbed Card V2 | `custom:tabbed-card-v2` | ATLAS Tabbed Card V2 |

## Entity Picker and Search

ATLAS now includes a reusable entity catalog in the `@atlas/homeassistant`
package. The catalog combines local demo entities, saved groups and live Home
Assistant entities.

The catalog provides:

- unique and sorted entity IDs
- domain detection such as `sensor`, `binary_sensor`, `switch` or `light`
- preferred shortcut ordering for common domains
- labels from live entities, for example friendly names
- search by entity ID or label, including partial terms such as `Hyper`

This keeps the entity picker from being demo-only code and makes it a shared
foundation for the later Home Assistant frontend integration.

## HACS and Resource Hints

ATLAS stores the expected resource paths directly in the export metadata. The
demo can therefore show whether a custom card is already registered in Home
Assistant or which path is still missing.

| Card target | HACS hint | Expected resource path |
|---|---|---|
| Entities | not required | built into Home Assistant |
| Mushroom Template | HACS > Frontend > Mushroom | `/hacsfiles/lovelace-mushroom/mushroom.js` |
| Bubble Button | HACS > Frontend > Bubble Card | `/hacsfiles/Bubble-Card/bubble-card.js` |

All expected Home Assistant and HACS resource paths are checked with exact
casing. For Bubble Card, the path is intentionally stored like this:

```text
/hacsfiles/Bubble-Card/bubble-card.js
```

Home Assistant often runs on Linux. Path casing matters for every resource
there.

ATLAS can also create a copy-ready Lovelace resource snippet for Mushroom and
Bubble Card. The combined snippet includes the ATLAS frontend resource and,
when needed, the selected card dependency. In YAML format, ATLAS server plus
Bubble Card looks like this:

```yaml
- url: "/local/atlas/atlas-homeassistant-panel.js"
  type: "module"
- url: "/hacsfiles/Bubble-Card/bubble-card.js"
  type: "module"
```

This snippet is intended for the resource registration in a Home Assistant
dashboard. With the built-in Entities card, only the ATLAS frontend resource is
copied.

## Export Model

ATLAS separates the HA card export into three layers:

1. **Card configuration**: the actual Home Assistant card object.
2. **Export manifest**: filename, format, MIME type, target, layout and
   dependency.
3. **Export payload**: manifest plus serialized JSON or YAML content.

This allows copy and download flows to use the same verified content.

## Atlas Card Packages

In addition to direct YAML/JSON export, ATLAS can create a portable JSON
package. This package is intended for later editor and HACS-oriented workflows.
When a package is exported from Expert mode, it also includes the editor plan.
On a later import, ATLAS can restore the placed fields and switch back to
Expert mode automatically.
The demo UI now exposes a dedicated HACS script filename field for that package
flow. Names such as `Energy Kitchen` are normalized to `energy-kitchen.js`,
stored in the embedded editor plan and restored into the field when an Atlas
Card Package is imported again.
The same package plan can now generate a custom-card JavaScript source. That
script carries the normalized filename, the matching `custom:<name>` card type,
the `/hacsfiles/atlas/...` resource path, a `getStubConfig()` default with safe
demo entities and the replacement hint users should see before wiring their own
Home Assistant entities.
In the demo, this `.js` source can also be downloaded directly through the card
script export so the artifact can be reviewed separately before a full HACS
bundle is produced.
The next packaging step creates a dependency-free `.hacs.zip` archive. The
archive contains the files for a later frontend repository: `hacs.json`, the
generated JavaScript card, a README, an example Lovelace card and the original
Atlas Card Package for later editing.
The demo can recognize those `.hacs.zip` files again through the HA card import
control. It reads the ZIP structure, reports missing bundle files and imports
the embedded `atlas/*.atlas-card.json` back into the Simple or Expert editor.
This enables the first HACS bundle roundtrip.

```json
{
  "version": 1,
  "kind": "atlas.homeassistant.card",
  "manifest": {
    "name": "Office Light",
    "filename": "office-light-bubble-single.yaml",
    "format": "yaml",
    "mimeType": "text/yaml",
    "target": "bubble",
    "layout": "single"
  },
  "content": "type: \"custom:bubble-card\"\n..."
}
```

In the demo, these files end with:

```text
.atlas-card.json
```

The same import can read raw Home Assistant cards as JSON/YAML and Atlas Card
Packages.

Before the actual import, ATLAS can inspect and classify artifacts:

- ATLAS Card Package
- raw Home Assistant card as JSON or YAML
- possible external card-builder export
- unknown content

External card-builder-shaped files are not imported automatically. They first
need an explicit compatibility mapping and license review.

The inspection becomes an import decision for the UI:

- **Import**: supported ATLAS or Home Assistant artifacts.
- **Review**: external card-builder-shaped artifacts.
- **Reject**: unknown content or content without a safe import path.

For the review case, ATLAS already returns structured review items: license
boundary, detected visual blocks, detected entity slots and the next schema
mapping step. A host UI can later turn this into a dialog before converting an
external artifact into ATLAS fields.

ATLAS can also create a mapping preview. Common external block types are mapped
to ATLAS templates: state-like blocks to State Buttons, switch-like blocks to
Switch Buttons and horizontal or vertical layout blocks to matching stack
templates. Unknown blocks stay visible and require manual review.

From a mapping preview, ATLAS can also create a reviewed field preview for the
expert surface. The fields are placed on the grid, keep empty entities at first
and remain review-required. This lets the UI show a conversion result without
silently importing it.

The card editor demo now uses this inspection before HA-card imports. Supported
ATLAS packages and raw Home Assistant cards are imported, external
card-builder-shaped files show a review output, and unknown artifacts are
rejected before parsing.
The ATLAS Status Preview remains available as a renderer, theme and entity
smoke test, but it now lives in a collapsible Diagnostics panel and no longer
sits in the main card-editor flow. The Diagnostics open state is saved with the
local demo configuration.

The demo now includes the visual Expert editor. It uses the shared template
palette, lets users select a card family, places fields by click or drag and
drop on the bounded 12-column grid, and renders nested Home Assistant card code
from that model. Fields can be selected, moved, removed and resized in edit
mode. During drops, ATLAS looks for a free grid position so new or moved fields
do not land on already occupied tiles.

The import path now also accepts nested Home Assistant cards. A real-world
`vertical-stack` card can contain `horizontal-stack` rows, `grid` containers,
`conditional` cards and regular cards; ATLAS keeps the supported structure and
extracts the involved entities. Bubble header or separator cards without an
entity are accepted as well, as are hand-built Bubble switch columns and
`empty-column` cards. Advanced Bubble Card details such as `modules`, `styles`,
`grid_options`, sliders and sub-buttons are planned as a later preservation
layer.

## Card Layout Editor

ATLAS is growing into a visual editor where users can build a Home Assistant
card layout by drag and drop. The visible card name and the generated
JavaScript filename should remain separate: for example, a user can name a card
`Energy Kitchen` and later export an installable `energy-kitchen.js` file
instead of being limited to a fixed name such as `atlas-card.js`.

For the later HACS card package export, ATLAS should also include safe demo
entities such as `binary_sensor.atlas_status` and
`sensor.atlas_temperature`. The UI should clearly tell users to replace these
demo entities with their own Home Assistant entities.

The editor should offer two workflows:

- **Simple**: fast button stacks for regular card exports.
- **Expert**: a free editor surface where fields can be positioned manually.
  Each field should be able to choose its own card target, for example
  Entities, Bubble Card or Mushroom Template.

From the editor plan, ATLAS derives the card targets that are actually used. In
a mixed expert layout, this lets ATLAS detect whether Mushroom and Bubble Card
are required as HACS resources while pure Entities fields do not need an
additional custom-card resource.

An editor plan can be projected into a Home Assistant card
configuration. Simple mode uses the selected target card directly. Expert mode
sorts populated fields by row and column. Multiple fields on the same row
become a `horizontal-stack`; multiple rows are wrapped by a `vertical-stack`.
A single field can also be marked as its own `horizontal-stack` or
`vertical-stack` and contain several child card entries. `custom:tabbed-card-v2`
is supported as its own container: tabs are configured in a popup, selected and
then filled with cards. Containers intentionally start without an entity and
without an automatically generated first card. When created, they receive
technical, incrementing titles such as `Tabbed 1`, `Vertical 1` or
`Horizontal 1`; cards inside the container keep their own titles. If an expert
plan does not contain populated fields yet, ATLAS falls back to the safe demo
entities.

In the demo UI, Expert mode hides the simple card-layout selector and the
regular HA card code block. Export, package export, copy and resource-copy
actions then use the Expert HA card code from the editor surface. In Expert
mode, resource copy includes all placed Mushroom and Bubble dependencies
together with the ATLAS frontend resource.
`Panel group`, `Group name`, `Card target`, `Card layout` and the group action
buttons are hidden in Expert mode as well because the editor surface directly
defines the card structure that will be exported. Expert mode uses its own
`Expert card name` field for copy, export and package filenames.

For the UI, a sidebar template palette is planned. It can offer visual building
blocks such as Entity List, State Button, Switch Button, `vertical-stack` and
`horizontal-stack`. In the demo this is already a left-hand palette with a
Simple/Expert mode switch: the user can click a building block or drag it into
the editor surface. Added fields appear as movable tiles on the grid surface.
The surface uses a visible 12-column grid that is closer to Home Assistant.
Moving existing fields snaps against the real inner grid and
preserves the point where the tile was grabbed, so fields can move upward
without sideways jumps. The visible grid now sits on the same inner surface as
the draggable tiles, with a smaller tile gap for closer vertical stacking.
Focused tiles can also be nudged by one grid cell with the arrow keys; while
edit mode is active, Shift plus an arrow resizes the selected field by one cell.
Each block in the left palette can define its own columns from 1 to 12 or `full`,
plus rows `auto` or 1 to 8. Entity List, State Button, Switch Button,
`horizontal-stack` and `vertical-stack` start with the same default footprint;
horizontal-stack drops can grow wider when multiple stack entities are
selected. The palette can use loaded Lovelace resources to mark custom card
families as installed, missing or unchecked. When a block is placed on the
expert surface, ATLAS clamps column, row and size to the allowed grid bounds so
elements cannot be dropped outside the valid area.
Placed fields can be selected and then adjusted through edit mode. The
bottom-right handle appears only while edit mode is active for the selected
field, and resizes the field inside the 12-column grid.
Placed field titles are editable. New fields first receive an automatically
counted title by type, for example `Entity 1`, `Bubble 1`, `Mushroom 1`,
`Tabbed 1`, `Vertical 1` or `Horizontal 1`. The title is exported as the
Entities title, Bubble button name or Mushroom primary text. An apply button
writes a manually edited title to the selected field. The existing copy button
can still use the currently selected Home Assistant entity name as the field
title.
In Expert mode, selecting an entity from the picker or entity list assigns that
entity to the currently selected editor field and prefills the title from the
entity name.
For Bubble fields, ATLAS also shows a Bubble button type dropdown. The currently
supported values are `state`, `switch`, `slider` and `name`; the selected value
is written as `button_type` in the generated Bubble Card code.
The left Expert palette separates Core and Community cards. Individual cards
can be marked as favorites with a checkbox and saved through `Save favorites`.
When saved favorites exist, ATLAS hides the remaining cards. `Show all cards`
opens the complete list again without deleting saved favorites, so several
favorites can be selected later and saved together. `Scan HA cards` reads the
currently registered Lovelace resources from Home Assistant and adds recognized
Community cards such as Mushroom and Bubble Card to the palette. Home Assistant
does not expose a complete option registry for every custom card through this
resource list, but installed resources can be detected as a starting point.
Other registered Lovelace resources are shown as scanned-only entries until
ATLAS knows a safe card mapping for them. Mapped resources are deduplicated so
they do not appear again as scanned-only copies. Saved favorites hide every
non-selected card, including scanned `/hacsfiles/` entries, until `Show all
cards` or `Reset favorites` is used. Scanned-only HACS and HA resources can also
be marked as favorites, even before ATLAS has a draggable card mapping for them.
Helper resources such as card tools, dashboards, strategies, navigation helpers,
icon packs and known non-card resources are hidden during the palette scan.
The Core list now includes Entity, Entities, Overview / Glance, Button, Grid,
Sensor, Vertical stack, Horizontal stack, Thermostat, Link and Webpage. Webpage
exports use the Home Assistant `iframe` card type. The Overview / Glance
template starts without a demo entity, receives automatic names such as
`Glance 1` or `Glance 2`, and is populated through its own entity editing
dialog.
When Home Assistant connects, ATLAS requests the Lovelace resource list
automatically. The temporary resource check has an optional debug panel. Enable
`Show resource debug` to inspect the browser WebSocket request, the Admin
WebSocket proxy and fallback status when a resource scan stalls. The Home
Assistant entity catalog is cached locally in the
browser. On startup, the last known catalog is immediately available to filters
and pickers; once Home Assistant is connected, ATLAS synchronizes the live list
and shows below the connection state whether the catalog is cached,
synchronizing, finished or failed. The status also reports newly added and
removed entities.
The palette itself is scrollable and uses compact two-column template rows:
card name and favorite state stay on the left, while layout details and sizing
controls sit on the right. Template column and row choices are saved with the
local demo configuration and can be restored to their defaults with
`Reset sizes`. Selected editor fields can be resized with the mouse or through
the Width and Height controls in one-cell steps, up to five grid cells beyond
their template default size. The editor surface itself has a
visible bottom-right resize handle and can grow by up to five grid steps in
both directions while keeping the current size as the default. A reset button
returns the editor surface to the default footprint.
The selected Simple/Expert mode, placed Expert fields, selected field and
resized editor surface are saved in local browser storage and restored after a
reload.
The demo UI is now bilingual: the language switcher in the header toggles
between English and German. The selected language is saved locally and restored
the next time the editor opens. Static labels, entity picker feedback, stack
summaries, dependency hints and key import/export status messages all use the
same translation table.
The Expert summary reports fields, populated fields, empty placeholders,
occupied rows, current surface span, overlaps, card targets and layout types
before the generated HA card code is copied or exported. Overlapping editor
fields are marked directly on the surface.
`Auto arrange` repacks fields into the first available free grid slots in row
and column order, reducing overlaps without changing card content. During
regular drops and moves, ATLAS also searches for a free target position if the
requested grid slot is already occupied.
The selected entity list below the editor is collapsible. It remains open by
default in Simple mode and collapsed by default in Expert mode, but can still be
opened when needed.

## YAML Import and Styles

The editor can read raw Home Assistant card configurations as YAML or JSON.
YAML can be pasted into an input dialog, inserted from the clipboard or loaded
from files with extensions such as `.yaml`, `.yml` or `.txt`. The imported YAML
code remains largely original in the HA card code view; Atlas only adds or
changes content where the user actually edits something in the editor.

During import, ATLAS detects `card_mod` and `uix` styles. Entity-level styles
are assigned to the imported entities in the preview and shown through a compact
style popup. In the Overview / Glance entity editor, detected entity styles are
also shown directly below the matching entity as collapsible style code. Global
card styles remain visible separately. Expert export keeps assigned entity
styles attached to the matching entity blocks. During HA card export, the user
can choose whether styles should be kept as `card_mod` or written as `uix`.

## External Reference: Home Assistant Card Builder

The
[`studiobts/home-assistant-card-builder`](https://github.com/studiobts/home-assistant-card-builder)
project is an important external reference for visual Home Assistant card
editors. It already provides a drag-and-drop builder, a block system, a Home
Assistant panel and a renderer.

ATLAS does not copy source code from that project at this stage. The project is
licensed under AGPL-3.0, so a real fork or derivative use would require clear
license and attribution handling. The planned ATLAS path is to keep building
independent contracts and UI models, name the original project clearly, and
later evaluate optional import/export compatibility or an explicitly marked
fork.

The interoperability plan separates three paths:

- **Inspiration**: public product ideas and documented behavior can inform
  independent ATLAS contracts.
- **Import/export compatibility**: ATLAS can later inspect documented artifacts
  and provide its own mappings without copying source code.
- **Fork/derivative**: only as an explicit decision with AGPL-3.0 compliance,
  visible attribution and a full license review.

## Import Summary

On import, ATLAS normalizes the card into a summary:

- title
- entities
- format
- target
- layout
- dependency
- whether the source was an Atlas Card Package

This keeps the actual editor logic in the `@atlas/homeassistant` package rather
than spreading it throughout the UI.

## Lovelace Resource Check

When ATLAS is connected to Home Assistant, the demo can load Lovelace resources
and check whether Mushroom or Bubble Card is registered.

Possible states:

- `not-required`: the Entities card does not require a custom card resource
- `unchecked`: not checked yet
- `installed`: expected resource found
- `missing`: expected resource missing

## ATLAS as a Home Assistant Frontend

ATLAS now also models the resource that makes ATLAS itself available inside
Home Assistant. This is separate from the selected card dependency.

| Usage mode | Purpose | Expected resource path |
|---|---|---|
| ATLAS server | self-hosted ATLAS editor or panel | `/local/atlas/atlas-homeassistant-panel.js` |
| ATLAS HACS | planned HACS frontend integration | `/hacsfiles/atlas/atlas-homeassistant-panel.js` |

The integration plan can therefore check these things together:

- whether the ATLAS frontend resource is registered
- whether the selected card resource is installed
- whether Mushroom or Bubble Card still need additional HACS paths
- whether the whole export is ready for Home Assistant
- which JSON or YAML resources should be registered in Home Assistant

This prepares the next step toward using ATLAS directly in Home Assistant or as
a HACS-oriented integration.

## Current Demo

In the ATLAS repository, the demo can be started after a build:

```sh
pnpm build
node examples/status-demo/server.mjs
```

Default address:

```text
http://127.0.0.1:4174/
```

On wide screens the demo uses compact two- and three-column grids for
connection, card configuration and entity-picker controls so related inputs sit
next to each other instead of stretching across the full page width.

## Roadmap

The Home Assistant integration targets two usage modes:

- ATLAS as a standalone server or editor
- ATLAS as a Home Assistant frontend integration, later close to HACS

The current Card Packages are an intermediate step toward an installable and
re-importable HA card editor.

When exporting Card Packages and HACS bundles, the Card Editor asks for Card
languages separately from the Atlas UI language. This affects only the exported
Card, not Atlas itself. `en` is always included as the required fallback, and
additional European languages plus `ru` for Russian-speaking users can be
selected with checkboxes. Until automatic translation is available, ATLAS
generates English fallback files for additional languages and marks the
corresponding `locales/*.json` files as needing translation and review before
publishing.

Atlas Administration owns the planned translation module choice. The first
options are `none`, `chatgpt`, `gemini`, `deepl-free`, `deepl-pro` and
`custom-ai`. The selection should use a clear radio-list layout with API-key
fields for each provider. In the Card Editor, automatic translation can be
requested during export with a checkbox and a visible progress indicator. Until
real provider adapters and API keys are connected, exported files remain
explicitly marked as fallbacks so untranslated files are not mistaken for
completed machine translations. A later real automatic translation option must
clearly state that it requires an internet connection.
For DeepL, `https://www.deepl.com/de/pro#api` is kept as the reference for
Free/Pro API options.
The prepared DeepL translate endpoint is `https://api.deepl.com/v2/translate`;
request details are tracked through
`https://developers.deepl.com/api-reference/translate/request-translation`.
This endpoint is internal configuration and should not appear as a normal Atlas
Administration input field.
For Gemini, `https://ai.google.dev/gemini-api/docs/api-key` is kept as the
API-key and security reference. Provider API keys belong to Atlas
Administration or later backend adapters; the Card Editor should receive
provider, endpoint and key-configured status only.
ChatGPT/OpenAI is the first connected adapter path. The Card Editor calls Atlas
Administration through `/api/card-translation`, and the Admin server uses the
server-held OpenAI key for the OpenAI Responses API. Successfully generated
locale files are marked as `machine` and still need review before publishing.
The server-side model name can be overridden with
`ATLAS_OPENAI_TRANSLATION_MODEL`.
After reloading Atlas Administration, the Admin page restores the Home
Assistant token and provider API keys from an encrypted long-term Admin cookie.
The browser-side decryption key stays in local Admin storage, so the cookie
itself does not contain raw provider keys or a raw token. The Admin page can
also refresh secrets from the running local Admin server through
`GET /api/admin-connection?includeSecrets=1`. Raw keys and the raw token still
are not written to the shared handoff cookie or Card Editor handoff payloads.
For backups, Administration can export `atlas-admin-settings.json`: normal
settings stay readable, while the token and provider API keys are stored in an
AES-GCM-encrypted `encryptedSecrets` block.
Those encrypted secrets are also bound to the local Atlas Administration
installation. The Admin server creates an installation identity in local user
data outside the repository, or uses `ATLAS_INSTANCE_ID` when a Docker or server
deployment needs an explicit stable identity. If only the server folder or an
exported settings file is copied to another environment, the secrets are treated
as invalid. Normal settings can remain migratable later; secrets need an
explicit transfer or passphrase flow for deliberate moves.

The Lovelace UV Card is planned as a later follow-up project. For this card,
`filipnet/haos-uv-index` is noted as an inspiration source. The relevant point
is not code reuse, but product direction: UV-index sensor handling,
color-coded risk display, WHO-style protection recommendations,
Mushroom-compatible presentation and optional notification automations.

The Home Assistant Card Editor is treated as the first official ATLAS reference
plugin. It should later show how a plugin combines entity selection, card
targets, import/export, HACS-oriented packages and administration in a real
workflow.

In the Atlas package, this step is already prepared through
`createHomeAssistantCardEditorPlugin()`. This lets the editor activate through
the Runtime plugin contract and become discoverable through the Plugin Catalog.
`createHomeAssistantCardEditorPluginInstallPackage()` also creates a first
install package with manifest, README and example configuration.

This plugin step is already visible: the minimal Atlas Administration runs as a
dedicated surface on port `4175`, separate from the Card Editor on port `4174`.
It shows the Card Editor as an installed reference plugin and exports the plugin
package as `.atlas-plugin.json`. The admin surface also marks the intended
security boundary: tokens and connection settings belong to Atlas centrally.
The editor receives the token only as a session handoff from Administration,
while plugins receive only approved paths, URLs and capabilities.
