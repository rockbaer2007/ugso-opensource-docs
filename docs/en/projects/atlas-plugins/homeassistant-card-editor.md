# Home Assistant Card Editor

The Home Assistant Card Editor is the first official ATLAS reference plugin. It shows how plugin lifecycle, discovery, Administration, Hub display, import/export and package building work together.

## Purpose

The plugin provides an editor for Home Assistant cards. It supports Simple and Expert workflows, entity selection, resource checks, YAML/JSON import, HACS-oriented bundle exports and multilingual card packages.

In the Expert workflow, the background grid stays square. The number of columns is controlled by a horizontal slider above the surface, while the number of rows is controlled by a vertical slider on the left. The previous stretch behavior is now represented as a controlled grid size from `12` to `17` cells per axis.

## Extension Points

The editor currently uses these ATLAS extension points:

- `homeassistant.card-editor`
- `homeassistant.card-target`
- `homeassistant.entity-picker`
- `homeassistant.exporter`
- `atlas.plugin.package-builder`

## Package

`createHomeAssistantCardEditorPluginInstallPackage()` creates the first install package for this reference plugin. It includes a plugin manifest, a README and an example Home Assistant card configuration.

## Hub Description

Hub and Administration can display localized descriptions from the plugin repository. When German is selected, `descriptions.de` is preferred. English remains the fallback.
