# Home Assistant Card Editor

The Home Assistant Card Editor is the first official ATLAS reference plugin. It shows how plugin lifecycle, discovery, Administration, Hub display, import/export and package building work together.

## Purpose

As of 2026-10-16: reference plugin **0.2.0-alpha.108** in App **0.1.312**.
It updates with ATLAS, not by replacement as an external plugin. See the
[Editor guide](../atlas/card-editor) and [App/Runtime projects](../atlas/frontend)
for shared projects and complete HACS Card export/import instructions.

Product decision on 2026-10-13: the editor remains Expert-only. Simple mode and
its switch will not return. Supported legacy project imports remain compatible.

Starting with HA app **0.1.292**, the start-mode selector is also removed from
HA app configuration and Administration. Older saved Simple values are treated
as Expert; credentials and other settings are preserved.

The plugin provides an editor for Home Assistant cards. It supports the Expert workflow, entity selection, resource checks, YAML/JSON import, HACS-oriented bundle exports and multilingual card packages. The former visible Simple mode has been removed; the editor now opens directly in the Expert workflow.

In the Expert workflow, the background grid stays square. The number of columns is controlled by a horizontal slider above the surface, while the number of rows is controlled by a vertical slider on the left. A separate Zoom slider changes only the cell size and scales width and height together. The previous stretch behavior is now split into field count and zoom.

## Card list on tablets

Starting with HA app **0.1.290**, editor widths from 521 to 1180 pixels show
two cards side by side in a scrollable window. Its height follows the first
card row and is capped on short screens. Scroll to reach the remaining cards.
The action buttons above the list also use two equal-width columns. Narrow
phones keep one column; the desktop sidebar remains unchanged. The embedded
editor width determines the layout, not the device name. Existing projects,
favorites and settings are preserved.

## Mobile grid and title controls

Starting with HA app **0.1.291**, Grid & zoom is collapsed by default at editor
widths up to 1180 pixels. Tap to show the X, Y and zoom sliders; opening or
closing the group changes no values or cards. Switching to desktop width shows
the sliders directly again.

On tablets, the title field, Apply title and Use entity name share one row.
On narrow phones, the title field sits above the two equal-width buttons.
This layout applies in DE/EN/FR.

## Live connection with large entity catalogs

Starting with HA app **0.1.293**, ATLAS processes entity snapshots and live
events in arrival order. An ongoing snapshot can no longer finish after a
subsequently received event and overwrite it with older values. Queued messages
from a closed connection are ignored; a failed replacement socket reports its
own failure status. Saved cards, positions and credentials remain unchanged.

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

Hub and Administration can display localized descriptions from the plugin repository. The selected language prefers `descriptions.de`, `descriptions.en` or
`descriptions.fr` when available. English remains the fallback.
