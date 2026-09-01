# Plugin Documentation

ATLAS is intended to become an extensible platform. The plugin documentation therefore covers the full path from an idea to a distributable extension, not only a single API.

::: warning Planning status
The plugin interfaces are still in progress. This page defines the target scope and will be expanded as the contracts become stable.
:::

## Goal

Plugins should extend ATLAS without directly changing core packages or existing applications.

Planned use cases include:

- Home Assistant-oriented tools such as card editors, diagnostics surfaces and Lovelace helpers
- standalone UGSo projects such as the planned Lovelace UV Card
- reusable providers, renderers, themes and Devtools extensions
- optional community extensions with clear contracts

## Plugin Lifecycle

A plugin should later follow a clear lifecycle:

1. Read the manifest.
2. Check dependencies.
3. Register the plugin.
4. Provide services, commands or UI surfaces.
5. Activate the plugin.
6. Report diagnostics and status data.
7. Deactivate or remove it cleanly.

The documentation will add examples for these steps once the contracts are stable.

## Current Technical Anchor

The first technical step is a Runtime adapter. A `RuntimePlugin` can be translated into an existing ATLAS Runtime module with `createRuntimeModuleFromPlugin()`. This lets a plugin use the same startup, diagnostics and shutdown path as other Runtime modules.

The adapter preserves plugin metadata, extension points and provided capabilities. Optional plugin hooks such as `deactivate()` and `dispose()` run through Runtime shutdown.

`RuntimePluginCatalog` also provides the first discovery surface. It registers plugins by id, exposes descriptive metadata and can find plugins by extension point or provided capability.

`createRuntimePluginAdministrationView()` prepares the future Atlas Administration surface. It turns Plugin Catalog data into a management view with statuses such as `available`, `active` and `disabled`, plus actions such as `inspect`, `activate`, `deactivate` and `export-package`.

`createRuntimePluginInstallPackage()` adds the first package contract. It creates a package description with `atlas-plugin.json`, `README.md` and optional additional files that can later be emitted as an installable package by the administration surface or an archive builder.

`parseRuntimePluginInstallPackage()` reads that package description back as a validated descriptor. It does not execute plugin code. This lets Administration safely display, inspect, re-export and remove imported packages from the local import list. Activation states are remembered in the local demo Administration so plugin lists survive reloads.

Administration also has a first ATLAS repository installation flow. A custom `repository.json` can be loaded, available plugins are shown, and packages can be installed from `package` or `manifest` URLs into the local Administration plugin store. Each repository plugin compares its installed version with the repository version so Administration can offer `Install`, `Update` and `Remove`. This first step is browser-/Administration-local; a later host installer can derive real filesystem or add-on installation from the same metadata.

## First Reference Plugin

The Home Assistant Card Editor is treated as the first official ATLAS reference plugin. It is therefore more than a demo: it proves that plugin lifecycle, discovery, administration, import/export and package building work together.

In the Atlas code, `createHomeAssistantCardEditorPlugin()` exposes the editor as a `RuntimePlugin`. During activation, the plugin registers a service with card targets, editor templates, Bubble button types and capabilities that can later be shown in Atlas Administration.

`createHomeAssistantCardEditorPluginInstallPackage()` also creates the first install package for this reference plugin. It includes a plugin manifest, a README and an example Home Assistant card configuration.

As a reference plugin, the editor uses these extension points:

- `homeassistant.card-editor`
- `homeassistant.card-target`
- `homeassistant.entity-picker`
- `homeassistant.exporter`
- `atlas.plugin.package-builder`

This creates a real example for future plugins: visible in Atlas Administration, activatable through the plugin catalog and exportable as an installable package.

## Planned Extension Surfaces

The first extension surfaces should align with the existing ATLAS packages:

| Area | Planned extension |
|---|---|
| Runtime | Services, lifecycle hooks and activation rules |
| Home Assistant | Card targets, entity selection, resource checks and export paths |
| Renderer | Render adapters and target surfaces |
| Theme | Tokens, theme variants and visual presets |
| Devtools | Diagnostics panels, inspectors and development helpers |

## Plugin Documentation Structure

A complete plugin documentation area should later contain:

- plugin fundamentals
- manifest and metadata
- lifecycle and activation
- service registration
- extension APIs
- Home Assistant-specific extensions
- examples
- tests
- versioning
- publishing and HACS/package notes

## Repository Format and Demo Template

ATLAS uses its own repository format for installable plugins. A repository is intentionally not a Home Assistant add-on repository: it must identify itself with ATLAS metadata so Administration does not accidentally accept arbitrary Home Assistant repositories as plugin sources.

Reference repository:

- Demo repository: `https://github.com/rockbaer2007/atlas-plugin-repository-demo`
- Repository file: `https://raw.githubusercontent.com/rockbaer2007/atlas-plugin-repository-demo/main/repository.json`
- Installation transition page: `https://rockbaer2007.github.io/atlas-plugin-repository-demo/install.html`

Recommended structure:

```text
repository.json
plugins/
  example-plugin/
    plugin.atlas-plugin.json
    icon.png
    preview.png
    README.md
```

The `repository.json` contains at least these fields:

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

Example:

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

The demo repository is both a test source and a template. Later, a generator can use it to create a new ATLAS plugin with the correct folder structure, manifest, icon, optional preview image and README.

## Atlas Administration

A dedicated Atlas Administration web surface is planned for plugin management. It should show installed plugins and support the full plugin workflow.

The first visible step is a dedicated minimal administration surface on port `4175`, separate from the Home Assistant Card Editor on port `4174`. It reads the Runtime plugin catalog, shows the Home Assistant Card Editor as the first reference plugin, displays status, version, extension points and capabilities, and exposes first actions such as inspect, activate, deactivate, export package and import package.

Administration is also the central place for sensitive connection settings. Home Assistant tokens should be managed there and can be stored locally through `Save settings`. The local Admin server exposes saved connection settings to the Card Editor so reloads and direct editor opens still work. The Card Editor receives the token only as a handoff to the active browser session and can optionally connect automatically after that handoff. Plugins should later receive only approved context such as the Home Assistant URL, WebSocket path, allowed resource paths and declared capabilities, but never the raw access token.

Planned capabilities include:

- viewing, enabling and disabling installed plugins
- checking plugin status, versions, dependencies and diagnostics
- creating new plugins through a wizard or template
- editing plugin manifests and extension points
- importing and exporting plugins
- generating installable packages such as ZIP or HACS-oriented bundles
- including demo data, example configurations and README files in packages

In the long term, the administration surface should become the central place for plugin management, package building and quality checks.

## Example Direction

A simple plugin could later:

- provide a manifest
- register a service
- offer a Home Assistant card type
- describe resource dependencies
- include example entities or demo data

This keeps an extension installable, testable and understandable.

## Publishing Rules

Publishable plugins should provide:

- clear package and plugin names
- explicit versions
- documented dependencies
- safe demo or fallback data
- traceable build and export artifacts
- notes for Home Assistant, HACS or standalone ATLAS usage

## Next Steps

The next documentation steps are:

1. Stabilize plugin contracts in the Atlas repo.
2. Model the Home Assistant Card Editor as the first reference plugin.
3. Add manifest and lifecycle examples.
4. Document Home Assistant-specific plugin extensions.
5. Define the repository format with a demo repository.
6. Describe Atlas Administration for plugin management and package building.
7. Derive a plugin template and later generator from the demo repository.
8. Prepare a publishing checklist.
