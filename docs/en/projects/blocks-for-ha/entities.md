---
title: Home Assistant entities
description: Load, search and select HA entities in Blocks.
---
# Select entities

Since **0.1.17**, entity fields in existing blocks open a search dialog. The HA app loads the current entity list when the editor opens. **Entitäten laden** in the toolbar and **Neu laden** in the dialog refresh it.

![Entity picker with a search result](/assets/blocks-for-ha/entity-picker.png)

The image uses simulated test entities. The editor UI remains German; entity names come from your HA installation.

## Usage

1. Click the entity ID inside a block.
2. Search by name or ID. All search words must match. The first 150 matches are displayed; narrow the search for larger lists.
3. Choose a result and press **Übernehmen** (Apply). Only applying changes the block. **Abbrechen** (Cancel) or Escape preserves the previous value.
4. Alternatively enter an ID such as `light.living_room` manually. This also works offline or for entities missing from the list.

Results show the name, ID and current state with unit. States are a **snapshot**, not continuous monitoring or sensor-value blocks for an automation.

| Block | Selection |
| --- | --- |
| State/numeric triggers and conditions | All loaded entities |
| Light with colour/brightness | `light` only |
| HA script | `script` only |
| Helper | Current helper type: `input_boolean`, `counter` or `timer` |
| On/off/toggle, refresh entity, generic HA action | All loaded entities; still check action support in HA |

An empty target is allowed only for the generic HA action. The dialog selects one entity ID. Area/device selection, multiple targets and live selection of installed actions remain future work. Changing an ID does not rewrite manually entered references in Jinja or JSON data.

## HA app and data

Refresh the repository in the HA app store, install **0.1.17** and restart the app. The app requires `homeassistant_api: true` and uses the server-side `SUPERVISOR_TOKEN` for a read request to `http://supervisor/core/api/states`. No token entry is required in the editor. [Official HA app communication](https://developers.home-assistant.io/docs/apps/communication/), [REST API](https://developers.home-assistant.io/docs/api/rest/).

The browser receives only ID, display name, domain, state and unit. Other attributes, credentials and HA configuration are not forwarded. The endpoint only reads the entity list and executes no HA actions. The server does not follow redirects carrying credentials.

The list comes from HA states, not the complete entity registry. Disabled or not-yet-available entities without a state may be absent. `unknown`/`unavailable` states are displayed when present. A refresh failure clears the previous list; existing block IDs remain intact.

JSON projects and YAML still contain only the selected ID. The catalog, names, state previews and credentials are not persisted in browser storage or exported. There are still 111 block types. Download your browser project through **Projekt sichern** before updating; a source backup does not include browser sessions.

## Local development

`npm run dev` alone uses manual IDs. For a connection, additionally start Python 3 with `npm run entities`. Set `BLOCKS_HA_URL` (base address without `/api`, for example `http://homeassistant.local:8123`) and `BLOCKS_HA_TOKEN` only in the server environment. Vite at `127.0.0.1:4180` proxies requests to the bridge at `127.0.0.1:9001`. Never put credentials in source or project files.

Docker starts the bridge and frontend together. Outside HA, bind locally or use an authenticated frontend when credentials are configured; standalone user authentication is not included yet. HA ingress protects access inside HA.

## Verification

Project/YAML compatibility, search, filters, cancel, manual entry, failure handling, mobile layout and the complete Docker chain were verified against a simulated HA server. A practical test in a real HA installation remains pending. Entity selection does not confirm that a particular device supports an action.
