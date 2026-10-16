# Repository Format

ATLAS uses its own repository format for installable plugins. A repository is intentionally not a Home Assistant add-on repository: it must identify itself with ATLAS metadata so Administration does not accidentally accept arbitrary Home Assistant repositories as plugin sources.

## Reference

- Demo repository: `https://github.com/rockbaer2007/atlas-plugin-repository-demo`
- Repository file: `https://raw.githubusercontent.com/rockbaer2007/atlas-plugin-repository-demo/main/repository.json`
- Installation transition page: `https://rockbaer2007.github.io/atlas-plugin-repository-demo/install.html`
- Official plugin template: [atlas-plugin-template](https://github.com/rockbaer2007/atlas-plugin-template) (GitHub **Use this template**)

The template includes a working example plugin, manifest, catalog, artwork,
package builder and validation. After editing the manifest, `npm run build`
generates the installable package and synchronizes catalog metadata;
`npm run check` validates consistency. GitHub Actions runs both checks.

The App server installs validated packages persistently and serves their static
web files. JavaScript runs when opened in the browser; Node modules and Runtime
hooks are not automatically registered. Installation is not a sandbox; see the
[Runtime contract](./developers/runtime).

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

Schema example for an own plugin, not the current bundled Card Editor version.
Keep the ID stable after publication.

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
      "id": "atlas.plugin.example",
      "atlas": {
        "type": "plugin",
        "schemaVersion": 1
      },
      "name": "Example Plugin",
      "version": "0.1.0",
      "description": "Example static ATLAS web plugin.",
      "descriptions": {
        "de": "Statisches ATLAS-Beispielplugin.",
        "en": "Static ATLAS example plugin."
      },
      "icon": "plugins/example/icon.svg",
      "preview": "plugins/example/preview.png",
      "package": "plugins/example/package.atlas-plugin.json",
      "manifest": "plugins/example/atlas-plugin.json",
      "capabilities": ["atlas.example"],
      "compatibility": {
        "atlas": ">=0.1.312 <0.2.0",
        "host": ["docker", "linux", "homeassistant"]
      }
    }
  ]
}
```
