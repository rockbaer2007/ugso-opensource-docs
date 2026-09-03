# ATLAS Plugins

This section collects everything that describes installable extensions rather than the ATLAS core itself: plugin contracts, repository format, publishing, update behavior and individual plugin pages.

::: warning Development status
The plugin interfaces are still in progress. These pages document the current ATLAS state and will be expanded as the contracts become more stable.
:::

## Start Here

- [Repository Format](./repository-format): `repository.json` structure, required fields, ATLAS marker and example.
- [Home Assistant Card Editor](./homeassistant-card-editor): the first official ATLAS reference plugin.
- [ATLAS File Studio](./file-studio): second independent ATLAS plugin for approved Home Assistant file paths.
- [ATLAS Automation Exporter / Editor](./automation-extractor): new plugin for analyzing, exporting and later editing Home Assistant automations.
- [Demo Repository](./demo-repository): public test repository for Administration, Hub and install flow.

## Goal

ATLAS plugins should extend the platform without directly changing core packages. This includes Home Assistant-oriented tools, card editors, diagnostics surfaces, renderers, themes, providers and later community extensions.

## Lifecycle

A plugin should be installable, inspectable, activatable, updatable and removable in a traceable way:

1. Read the manifest.
2. Check dependencies.
3. Register the plugin.
4. Provide services, commands or UI surfaces.
5. Activate the plugin.
6. Report diagnostics and status data.
7. Deactivate or remove it cleanly.

## Current Technical Anchor

The current entry point is the Runtime adapter. A `RuntimePlugin` can be translated into an ATLAS Runtime module with `createRuntimeModuleFromPlugin()`. `RuntimePluginCatalog` provides discovery, while Administration makes plugins visible, compares versions and prepares local installs.

The Plugin Hub now follows a clear start rule: if no plugins are installed, it points to Administration. With exactly one active plugin, ATLAS opens that plugin directly. With two or more active plugins, ATLAS shows the selection page. Planned or disabled plugins may be visible, but they are not started automatically.

The Plugin Hub can also prepare Home Assistant sidebar entries. The dialog lists current plugins dynamically, shows name, URL, version, status and icon suggestion, and copies either the URL alone or a ready-to-use `panel_iframe` block for `configuration.yaml`. The URL copy action is intended for Home Assistant dashboards of type `Webpage`. Long capability lists and sidebar URLs stay collapsed by default on plugin cards so the Hub remains compact with many plugins.

In Add-on mode, Card Editor, Administration and local plugin assets are served through ATLAS app routes. This preserves Home Assistant Ingress base paths in Hub and sidebar URLs, and other network clients do not need direct access to the separate development ports.

For ATLAS File Studio, the Hub uses the plugin URL under `/plugin-assets/file-studio/index.html` on the ATLAS app port or through the matching Home Assistant Ingress/Webpage address. This URL is prepared even when older saved plugin state does not yet include a launch URL.

New local plugins also receive an automatic launch URL when their plugin folder contains an `index.html` and the manifest does not define `entry`. ATLAS then exposes `/plugin-assets/<plugin-folder>/index.html`, so users can choose between the Hub and a Home Assistant sidebar entry from the start.

## Publishing Rules

Publishable plugins need clear names, explicit versions, documented dependencies, safe demo or fallback data, traceable build artifacts and notes for ATLAS, Home Assistant or HACS-oriented usage.

## Planned Plugins

The next plugin candidate has started as ATLAS Automation Exporter / Editor. It brings the earlier Windows idea into ATLAS: detect automations, show dependencies, export individual timestamped YAML files and prepare further editing through File Studio.
