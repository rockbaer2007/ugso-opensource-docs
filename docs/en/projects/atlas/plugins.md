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
2. Define a minimal example plugin.
3. Add manifest and lifecycle examples.
4. Document Home Assistant-specific plugin extensions.
5. Prepare a publishing checklist.
