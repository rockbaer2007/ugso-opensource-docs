---
title: ATLAS Icon Studio
description: Manage, import, delete and save Home Assistant icon sets with ATLAS Icon Studio.
---
# ATLAS Icon Studio

ATLAS Icon Studio is a separately installed plugin for creating and managing Home Assistant icon sets with the `atlas:` prefix. Version 0.1.15 supports large collections without a fixed icon-count limit; the list renders 24 entries at a time.

## Managing icons

Current plugin version: **0.1.17**. It fixes a missing validator import when
creating drawing text. Version 0.1.16 previously fixed export-selector startup.
Storage formats remain unchanged.

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

## Safe plugin recovery

Back up the collection as JSON, export the iconset and save drawings separately
as SVG. In **Administration → Plugin Manager → Icon Studio → Restore**, select
a backup, review version/compatibility and use the action that backs up the
current plugin and applies the selected version. Cancel leaves it unchanged.

::: info Isolated qualification on 2026-10-16
ATLAS 0.1.312 passed **0.1.16 → 0.1.17** and recovery **0.1.17 → 0.1.16 → saved
0.1.17**, including App restart. All twelve assets matched their actual packages.
A collection of 131 icons and a drawing with two text objects survived on the same
browser origin/profile. Re-exported JSON, iconset JavaScript and SVG were
byte-identical. New text creation, duplicate and undo worked. Test files,
existing iconset, project, another plugin, trash and history remained intact.
Repositories, server data and browser exports were backed up beforehand.
**Pi 5 and Proxmox were neither queried nor changed in this isolated test.**
Data-format migrations remain separate.
:::

::: info Pi 5 and Proxmox qualification on 2026-10-16
After fresh local HA backups, PC file copies and browser exports, Administration
passed **0.1.16 → 0.1.17 → original 0.1.16 → 0.1.17**. All twelve package assets
match; settings, existing files, six active plugins, project, trash and history
remain intact. ATLAS 0.1.312 and HA 2026.10.1 needed no restart. Both hosts finish
with Icon Studio 0.1.17. If a stale update preview is rejected after recovery,
reload Administration and select the update again.
Direct access and HA Ingress were checked on each host: three reference icons
and an empty drawing draft in each context. Collection JSON stays byte-identical,
and the draft is unchanged after reload. Text creation and undo work.
Larger collections and populated drawings were covered by the isolated test.
:::

Package recovery does not restore deleted browser data. IndexedDB and the local
drawing draft belong to the browser profile and origin (scheme, host and port).
HA/server backups do not contain those browser stores. Collection JSON and
iconset JavaScript exclude colored drawings; an exported SVG is not a complete
editable-draft/undo backup. Current draft shapes and filename persist locally;
tool selection, search and undo/redo history belong to the session.
