---
title: Manifest and Capabilities
description: IDs, versions, metadata and capabilities for an ATLAS plugin.
---
# Manifest and Capabilities

The plugin manifest describes its identity, display metadata and entry point. In the [official template](../plugin-template), the example is `plugins/atlas-plugin/atlas-plugin.json`.

## Example

```json
{
  "id": "atlas.plugin.lights",
  "name": "Light Controls",
  "nameI18n": { "de": "Lichtsteuerung", "en": "Light Controls" },
  "version": "1.0.0",
  "description": "Controls selected lights.",
  "status": "active",
  "order": 100,
  "entry": "/plugin-assets/atlas-plugin/index.html",
  "icon": "icon.svg",
  "logo": "logo.svg",
  "preview": "preview.svg",
  "capabilities": ["homeassistant.entities.read"]
}
```

## Fields

- `id`: globally unique plugin identifier. Keep it stable after publication; the template uses lowercase, dot-separated IDs.
- `name` and `nameI18n`: default and optional localized names.
- `version`: published plugin version. Increment it for every published change.
- `description` and `descriptionI18n`: short default and localized descriptions.
- `status` and `order`: status and sort hints for the catalog and UI.
- `entry`: relative plugin entry URL. Local plugins containing `index.html` can receive an automatic launch URL in Atlas when `entry` is omitted.
- `icon`, `logo`, `preview`: relative asset paths used in the catalog and Administration.
- `capabilities`: documents which features the plugin needs. Declare only capabilities actually used.

The manifest in a plugin package is distinct from `repository.json`: the catalog also contains per-plugin fields such as package URL, manifest fallback, compatibility and catalog descriptions. See [Repository Format](../repository-format).

## Keep capabilities narrow

Capabilities should be specific and justified. Do not add placeholder or broad administrator permissions. The current installation does not execute downloaded plugin code, so a capability declaration is not an access-control boundary or sandbox.
