---
title: Widget package interface
description: Create and install local widget packages for HA Grafik Visual Studio.
---

# Widget package interface

From Studio 0.1.187, **interface 0.2** adds declarative charts alongside 0.1 text widgets. The optional [Weather and Heating](weather-heating.md) set uses this extension. External sets automatically receive an unused palette color separated from existing hues. Assignments remain in this browser across reloads, removal and reinstallation; Basic and built-in sets retain their colors.

## Interface 0.1: text

Starting with Studio 0.1.89, you can install ZIP-based packages ending in `.wg`. Existing `.wg.zip` files remain supported; the extension and manifest must both identify a widget package.

Under **Settings → Widget packages**, you can install a local `*.wg.zip`. Interface 0.1 accepts validated, declarative text widgets. After reloading the app, they appear as a separate set in the palette and work in both editor and runtime. Installation does not execute package code.

## Interface 0.2: chart

The manifest uses `apiVersion: "0.2"` and `render: {"kind":"chart","valueKey":"headline"}`. Declare `headline` as a text field with a default. Instances save definition version 0.2. Manifest and validated icons remain the only allowed package files; Studio uses its own SVG renderer.

The fixed property keys and limits are listed in the [chart contract](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/widget-rules.md#widget-paket-schnittstelle-02). It supports up to ten JSON series, line/bar charts, left/right axes, time/category axes and read-only HA state/attribute bindings. Executable formatters and write actions are excluded. Existing 0.1 text packages remain supported.

## Build a package

The ZIP contains a UTF-8 `manifest.json` at its root and optionally referenced SVG or PNG images under `icons/`. No other files are allowed. Package IDs use dot-separated parts, such as `example.widgets`; widget types use the package namespace, such as `example.widgets/label`. Package versions have the form `x.y.z`. A package contains 1 to 30 widgets; each appears as its own entry in the package's palette set.

```json
{
  "format": "ha-grafik-widget-package",
  "apiVersion": "0.1",
  "id": "example.widgets",
  "name": "Example Widgets",
  "version": "1.0.0",
  "license": "MIT",
  "widgets": [{
    "type": "example.widgets/label",
    "label": "Label",
    "defaults": { "text": "Hello" },
    "propertyGroups": [{
      "label": "Content",
      "fields": [{ "key": "text", "label": "Text", "type": "text" }]
    }],
    "render": { "kind": "text", "valueKey": "text" }
  }]
}
```

`valueKey` points to an editable text or number field. Property field types are `text`, `number`, `checkbox`, `color`, `range` and `select`. Each property needs a matching value in `defaults`. The Studio supplies the shared **General** and **Visibility** groups. A package or widget may also specify `"icon": "icons/name.svg"` or `.png`; the referenced image must be included in the ZIP. Widgets without an image use the built-in SVG text symbol.

The ZIP limit is 2 MB, the manifest limit is 200 KB, and each image is limited to 50 KB. PNG images are limited to 1024 × 1024 pixels; SVG files are checked for inert shapes and attributes. Package and widget images may be SVG or PNG, while Studio action buttons retain their SVG symbols.

## Install and manage

From Studio 0.1.190, interface 0.2 also supports `render: {"kind":"room-table","valueKey":"tablePreview"}`. The host reads `entityId` and optional `tableAttribute`, or uses the declared preview value without a binding. It rebuilds passive HTML table elements and selected formatting; executable content and external resources are removed. This mode requires Studio 0.1.190 or later. The optional [Weather and Heating](weather-heating.md) package is the reference implementation.

1. Create a ZIP named, for example, `my-package.wg` with the files above. `my-package.wg.zip` remains supported.
2. Select the local ZIP under **Settings → Widget packages**.
3. Review its package ID, version, API version, widget count and license. Use **Reload** to make the set appear in the palette.

From Studio 0.1.188, the local import may install a higher package version if its identity and all existing widget definitions remain exactly unchanged. It may add new widgets even while existing package widgets are used. Saved projects are not modified. Changes to existing definitions, identical versions and downgrades are rejected. **Remove** remains blocked while any project uses a widget type from that package. GitHub installation and automatic updates are not available yet. Custom scripts, Home Assistant state binding and write actions remain outside interface 0.1.

Later extensions should preserve existing widget behavior. See the complete [widget rules in the source repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/widget-rules.md).
