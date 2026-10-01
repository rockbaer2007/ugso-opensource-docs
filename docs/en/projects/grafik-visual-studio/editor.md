---
title: Editor and keyboard shortcuts
---

# Editor and keyboard shortcuts

## Getting started

Create a project under **Projekte** and choose a page under **Seiten**. Set the page size, open **Widgets**, and add an item from the palette. **Search widgets** at the top of the palette filters available widgets by name or type; matching groups open during the search without changing their previous expanded state. Clicking a widget selects it and shows its properties on the right. Use **Runtime** to check the view. **Speichern** saves manually; auto-save and its delay are under **Settings → General**. The **Widget packages** and **Tools** tabs currently show empty lists; package installation will follow later.

The widget selector in the top bar lets you select several widgets or clear the selection. The action bar provides cut, copy, paste, duplicate, delete and up to 50 undo/redo steps. The ten alignment actions work on multiple selected normal widgets; the first selected widget is the reference. Pressing **Breite** or **Höhe** for about 0.6 seconds opens an exact pixel-size input.

## Interface language

Open **Settings → General → Language → App language**, choose an option, then click **Save**:

| Option | Display language |
| --- | --- |
| **Automatic (Home Assistant)** | German when Home Assistant is set to German; English for any other HA language. If the HA language is unavailable, the browser language is used with the same German/English fallback. |
| **German** | Keep the interface in German. |
| **English** | Keep the interface in English. |

The choice is stored only in this browser and survives a reload. Other users and browsers keep their own choice. It translates interface text such as menus, dialogs, the widget palette and properties; user-defined project and widget names and widget content are not translated.

## Keyboard and mouse

| Action | Control |
| --- | --- |
| Undo | `Ctrl+Z` (macOS: `⌘+Z`) |
| Redo | `Ctrl+Y` or `Ctrl+Shift+Z` (macOS: `⌘+Y` or `⌘+Shift+Z`) |
| Add or remove a widget from a multi-selection | Hold `Ctrl+Shift` and click the widget |
| Move a free connection endpoint | Drag the endpoint; use arrow keys on a focused endpoint for 1-pixel steps |
| Move a connection endpoint faster | Hold `Shift` with an arrow key for 10-pixel steps |
| Detach a connected endpoint | Hold `Ctrl` and drag it; `Ctrl` plus an arrow key also works |
| Move an entire connection line | Press and drag the line; this detaches its existing docked endpoints |
| Add an intermediate or collector point | Click the line, choose “Intermediate point” or “Collector point”, then confirm with **OK** |

Undo/redo shortcuts apply when focus is outside input, text area and select controls. Cut, copy and paste are available as buttons; global `Ctrl+X/C/V` shortcuts are not currently implemented.

## Connection lines and docking points

Enable **Andockpunkte** in a target widget's properties. Individual edge points can be enabled; clearing the group checkbox disables them all. Drag SVG connection endpoints onto active points. An intermediate point splits the path into additional segments; only an explicitly enabled **Sammelpunkt** can be selected as a connection by another line. A simple crossing does not connect lines. Available settings include line and zigzag/multi-point paths, colors, width, arrowheads, animation and z-index.

## Visibility and filters

**Generell** and **Sichtbarkeit** exist on every widget and are disabled by default. “Generell” includes name, comment, CSS class, filter word and lock controls. The editor filter can hide matching widgets or show only matching ones. Runtime visibility can evaluate a Home Assistant state with a condition and comparison value; group evaluation remains unfinished.
