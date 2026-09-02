# ATLAS Plugins

This section collects everything that describes installable extensions rather than the ATLAS core itself: plugin contracts, repository format, publishing, update behavior and individual plugin pages.

::: warning Development status
The plugin interfaces are still in progress. These pages document the current ATLAS state and will be expanded as the contracts become more stable.
:::

## Start Here

- [Repository Format](./repository-format): `repository.json` structure, required fields, ATLAS marker and example.
- [Home Assistant Card Editor](./homeassistant-card-editor): the first official ATLAS reference plugin.
- [ATLAS File Studio](./file-studio): second independent ATLAS plugin for approved Home Assistant file paths.
- [Automation Extractor](./automation-extractor): planned plugin for analyzing and later splitting Home Assistant automations.
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

Atlas Administration can also prepare Home Assistant sidebar entries. The dialog lists current plugins dynamically, shows name, URL, version, status and icon suggestion, and copies the values for a Home Assistant dashboard of type `Webpage`. The actual entry is created in Home Assistant: add a dashboard, choose Webpage, paste the values and enable **Show in sidebar**.

The Plugin Hub now points to this option as well and shows the direct sidebar URL for launchable plugins. For ATLAS File Studio, that is the plugin URL under `/plugin-assets/file-studio/index.html` on the ATLAS app port or through the matching Home Assistant Ingress/Webpage address.

## Publishing Rules

Publishable plugins need clear names, explicit versions, documented dependencies, safe demo or fallback data, traceable build artifacts and notes for ATLAS, Home Assistant or HACS-oriented usage.

## Planned Plugins

The next noted plugin candidate is Automation Extractor. It should bring the earlier Windows idea into ATLAS and start read-only: detect automations, show dependencies and prepare safe export or refactoring steps.
