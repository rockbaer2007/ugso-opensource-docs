---
title: ATLAS Icon Studio
description: Manage, import, delete and save Home Assistant icon sets with ATLAS Icon Studio.
---
# ATLAS Icon Studio

ATLAS Icon Studio is a separately installed plugin for creating and managing Home Assistant icon sets with the `atlas:` prefix. Version 0.1.15 supports large collections without a fixed icon-count limit; the list renders 24 entries at a time.

## Managing icons

Current plugin version: **0.1.16**. It corrects a startup failure in the export
format selector while preserving saved collections.

The collection is stored in browser-local IndexedDB. Older local data is
adopted; export the collection as JSON before changing browser or address.

## Drawing and image previews

A separate drawing area supports colored SVGs with shapes, freehand and text,
layer ordering and up to ten undo/redo steps. Save as exports SVG, PNG or WebP,
optionally with a transparent background. Raster images can be previewed and
optionally traced, but do not directly become `atlas:` icons; HA icon sets need
SVG paths. File Studio can hand supported images directly to Icon Studio on the
same ATLAS server. Downloads are not automatically copied to HA.

## Editing a collection

Select an icon in the collection and use **Delete icon** to remove it. Icon Studio automatically selects the next deletable icon, so you can remove several icons in succession without selecting each one again. The reference icon `atlas:home` is protected and cannot be deleted. At least one icon remains in the collection.

Search, keyboard navigation and export cover the full collection, even when only a small portion is visible. Collections can be backed up and restored as JSON; name conflicts can be replaced, skipped or renamed automatically.

## Home Assistant

Icon sets can be exported locally as `atlas-iconset.js` or read directly from `/config/www/atlas-iconset.js` through File Studio. When saving, you can replace the existing file; File Studio creates a backup first. Alternatively, Icon Studio creates a new numbered file and displays its `/local/...` resource path for registration in Home Assistant. Direct access requires `/config/www` to be approved in File Studio.

See the [plugin README](https://github.com/rockbaer2007/atlas-icon-studio-plugin#readme) for installation, format and path details.
