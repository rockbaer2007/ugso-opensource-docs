---
title: ATLAS Icon Library
description: Search Home Assistant icon sets, browse icons and copy their names.
---
# ATLAS Icon Library

ATLAS Icon Library is a standalone plugin for searching and browsing icon sets. Icons appear in a grid of up to 20 columns; for large sets, the interface renders only the visible portion. Click an icon to copy its full name, such as `mdi:home` or `atlas:home`.

The MDI catalog is bundled with the plugin and is identified as an integrated source in the source field, rather than as a Home Assistant file path. SVG icons use the accent color by default, and the interface follows the browser's light or dark color scheme.

## Loading icon sets

The plugin package includes the MDI catalog. Icon Studio collections and supported static Home Assistant icon sets can be imported as JavaScript files from the computer or loaded through File Studio from `/config/www/`. The scanner also searches subfolders, including `/config/www/community/` (available in Home Assistant as `/local/community/`). It considers supported JavaScript icon sets when “icon” appears in a filename or folder name, and combines files that use the same prefix. Examples include Hue, Selfh.st, BHA, Yandex, Custom Icons, KNX, Thermal Comfort and Custom Brand Icons. JavaScript files are parsed as data and never executed. Imported collections are stored locally in the browser.

Some legacy Home Assistant icon sets expose icon names through `window.customIcons` and can be displayed this way. The newer `window.customIconsets` interface has no general mechanism for listing every icon name in an arbitrary set. Such sets can only be displayed when they also provide a readable name list.

File Studio must grant access to `/config/www/`. The plugin does not need a Home Assistant token for this access.

## Installation and source code

Add this external repository in the ATLAS Plugin Manager:

```text
https://raw.githubusercontent.com/rockbaer2007/atlas-icon-library-plugin/main/repository.json
```

ATLAS 0.1.248 or newer is required because that release fixes external package installation.

See the [GitHub repository](https://github.com/rockbaer2007/atlas-icon-library-plugin) for source code and development notes.
