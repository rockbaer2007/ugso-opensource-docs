# Plugin Documentation

ATLAS is intended to become an extensible platform. The plugin documentation therefore covers the full path from an idea to a distributable extension, not only a single API.

::: warning Planning status
The plugin interfaces are still in progress. This page defines the target scope and will be expanded as the contracts become stable.
:::

## Goal

Plugins should extend ATLAS without directly changing core packages or existing applications.

Planned use cases include:

- Home Assistant-oriented tools such as card editors, diagnostics surfaces and Lovelace helpers
- standalone UGSo projects such as the planned UGSo Thread Monitor
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

## First Reference Plugin

The Home Assistant Card Editor is treated as the first official ATLAS reference plugin. It is therefore more than a demo: it proves that plugin lifecycle, discovery, administration, import/export and package building work together.

In the Atlas code, `createHomeAssistantCardEditorPlugin()` exposes the editor as a `RuntimePlugin`. During activation, the plugin registers a service with card targets, editor templates, Bubble button types and capabilities that can later be shown in Atlas Administration.

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

## Atlas Administration

A dedicated Atlas Administration web surface is planned for plugin management. It should show installed plugins and support the full plugin workflow.

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
5. Describe Atlas Administration for plugin management and package building.
6. Prepare a publishing checklist.
