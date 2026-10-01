---
title: Widget package interface
description: Create and install local widget packages for HA Grafik Visual Studio.
---

# Widget package interface 0.1

Under **Settings → Widget packages**, you can install a local `*.wg.zip`. Interface 0.1 accepts validated, declarative text widgets. After reloading the app, they appear as a separate set in the palette and work in both editor and runtime. Installation does not execute package code.

## Build a package

The ZIP contains a UTF-8 `manifest.json` at its root and optionally referenced SVG or PNG images under `icons/`. No other files are allowed. Package IDs use dot-separated parts, such as `example.widgets`; widget types use the package namespace, such as `example.widgets/label`. Package versions have the form `x.y.z`. A package contains 1 to 30 widgets.

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

1. Create a ZIP named, for example, `my-package.wg.zip` with the files above.
2. Select the local ZIP under **Settings → Widget packages**.
3. Review its package ID, version, API version, widget count and license. Use **Reload** to make the set appear in the palette.

An already installed package is not overwritten. **Remove** is blocked while any project uses a widget type from that package. GitHub installation and package updates are not available yet. Custom scripts, Home Assistant state binding and write actions are also outside interface 0.1.

Later extensions should preserve existing widget behavior. See the complete [widget rules in the source repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/widget-rules.md).
