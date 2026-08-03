# ATLAS and Home Assistant

ATLAS includes its own `@atlas/homeassistant` package for Home-Assistant-oriented
integration. The current focus is an editor and export workflow for Home
Assistant cards, live entities and later HACS-oriented usage.

## Current Scope

- ATLAS Status Preview with Theme and Renderer integration
- local and live Home Assistant entities
- connection through the Home Assistant WebSocket API
- loading entities through `get_states`
- loading Lovelace resources through `lovelace/resources`
- shared entity catalog for type filters and search
- card targets for Entities, Mushroom Template and Bubble Card
- `single`, `horizontal-stack` and `vertical-stack` layouts
- JSON and YAML export for Home Assistant cards
- Atlas Card Packages for editor roundtrips
- import summaries for imported cards

## Supported Card Targets

| Selection | Home Assistant type | Dependency |
|---|---|---|
| Entities | `entities` | built into Home Assistant |
| Mushroom Template | `custom:mushroom-template-card` | Mushroom |
| Bubble Button | `custom:bubble-card` | Bubble Card |

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

For Bubble Card, the HACS resource path is intentionally stored exactly like
this:

```text
/hacsfiles/Bubble-Card/bubble-card.js
```

Home Assistant often runs on Linux. Path casing matters there.

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

## Planned Card Layout Editor

ATLAS is intended to grow into a visual editor where users can build a Home
Assistant card layout by drag and drop. The visible card name and the generated
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

From the editor plan, ATLAS can later derive the card targets that are actually
used. In a mixed expert layout, this lets ATLAS detect whether Mushroom and
Bubble Card are required as HACS resources while pure Entities fields do not
need an additional custom-card resource.

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
http://127.0.0.1:4173/
```

In the Codex workspace, port `4174` has often been used recently:

```text
http://127.0.0.1:4174/
```

## Roadmap

The Home Assistant integration targets two usage modes:

- ATLAS as a standalone server or editor
- ATLAS as a Home Assistant frontend integration, later close to HACS

The current Card Packages are an intermediate step toward an installable and
re-importable HA card editor.
