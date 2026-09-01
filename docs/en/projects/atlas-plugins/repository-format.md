# Repository Format

ATLAS uses its own repository format for installable plugins. A repository is intentionally not a Home Assistant add-on repository: it must identify itself with ATLAS metadata so Administration does not accidentally accept arbitrary Home Assistant repositories as plugin sources.

## Reference

- Demo repository: `https://github.com/rockbaer2007/atlas-plugin-repository-demo`
- Repository file: `https://raw.githubusercontent.com/rockbaer2007/atlas-plugin-repository-demo/main/repository.json`
- Installation transition page: `https://rockbaer2007.github.io/atlas-plugin-repository-demo/install.html`

## Structure

```text
repository.json
plugins/
  example-plugin/
    plugin.atlas-plugin.json
    icon.png
    preview.png
    README.md
```

## Fields

| Field | Purpose |
|---|---|
| `kind` | Must be `atlas.plugin.repository`. |
| `atlas.type` | Must be `plugin-repository`. |
| `atlas.schemaVersion` | Schema version of the ATLAS repository file. |
| `name` | Display name of the repository. |
| `version` | Version of the repository catalog. |
| `homepage` | Optional project or GitHub page. |
| `installPage` | Optional ATLAS transition page for copying the repository URL. |
| `plugins[]` | List of installable plugins. |
| `plugins[].id` | Unique plugin id. |
| `plugins[].atlas.type` | Must be `plugin`. |
| `plugins[].atlas.schemaVersion` | Schema version of the plugin entry. |
| `plugins[].name` | Plugin display name. |
| `plugins[].version` | Published plugin version. |
| `plugins[].description` | Fallback short description. |
| `plugins[].descriptions` | Optional localized descriptions, for example `de` and `en`. |
| `plugins[].icon` | Path or URL to the plugin icon. One icon is enough for Hub and Administration. |
| `plugins[].preview` | Optional path or URL to a preview image. |
| `plugins[].package` | Path or URL to the installable package. |
| `plugins[].manifest` | Fallback path or URL to the manifest. |
| `plugins[].capabilities` | Declared capabilities. |
| `plugins[].compatibility` | ATLAS/host compatibility. |

Relative paths are resolved relative to the loaded `repository.json`. `package` points to the installable plugin package, while `manifest` remains a readable fallback for preview, diagnostics and manual review.

## Example

```json
{
  "kind": "atlas.plugin.repository",
  "atlas": {
    "type": "plugin-repository",
    "schemaVersion": 1
  },
  "name": "ATLAS Plugin Demo Repository",
  "version": "0.1.0",
  "plugins": [
    {
      "id": "atlas-homeassistant-card-editor",
      "atlas": {
        "type": "plugin",
        "schemaVersion": 1
      },
      "name": "Home Assistant Card Editor",
      "version": "0.1.54",
      "description": "Reference plugin for Home Assistant cards.",
      "descriptions": {
        "de": "Referenz-Plugin für Home-Assistant-Cards.",
        "en": "Reference plugin for Home Assistant cards."
      },
      "icon": "plugins/card-editor/icon.svg",
      "preview": "plugins/card-editor/preview.png",
      "package": "plugins/card-editor/atlas-plugin.json",
      "manifest": "plugins/card-editor/plugin.atlas-plugin.json",
      "capabilities": ["homeassistant.card-editor"],
      "compatibility": {
        "atlas": ">=0.1.54",
        "host": ["administration", "hub", "homeassistant-addon"]
      }
    }
  ]
}
```
