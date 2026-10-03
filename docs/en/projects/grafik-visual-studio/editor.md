---
title: Editor and keyboard shortcuts
---

# Editor and keyboard shortcuts

## Getting started

From **0.1.184**, background colors distinguish palette sets: **Interactive** is olive green, **Special** blue and **Data Flow** violet. **Basic** keeps its existing appearance. Additional installed sets each receive their own color. These colors apply to palette selection buttons; inserted widgets retain their independently configured appearance.

![Olive green entries in the Interactive widget set](/images/grafik-visual-studio/palette-set-colors.png)

Starting with Studio **0.1.115**, right-click a widget, group label or empty editor surface to open a context menu: **Select**, **Group widgets**, **Ungroup**, **Edit group**, **Copy**, **Cut**, **Paste** and **Delete**. **More** provides duplication, front/back ordering, lock/unlock, undo/redo and widget import/export. Unavailable actions are disabled; Escape closes the menu and up/down arrows navigate it. Select offers all widgets and widgets under the pointer.

Groups retain freely positioned members and move together when dragging a member or the group label. They persist in project data; copies and multi-widget exports receive independent groups when pasted or imported. **Edit group** enables individual member editing; **Finish editing group** or clicking the group label restores group selection. Ungroup preserves positions and dimensions. Undo/redo includes grouping and movement. Groups are flat; SVG connection lines cannot be grouped, and groups containing locked members cannot be dragged. Runtime shows neither group outlines nor editor menus. Grouping does not create tab contents or import VIS2 widgets.

Create a project under **Projekte** and choose a page under **Seiten**. Set the page size, open **Widgets**, and add an item from the palette. **Search widgets** at the top of the palette filters available widgets by name or type; matching groups open during the search without changing their previous expanded state. Clicking a widget selects it and shows its properties on the right. Use **Runtime** to check the view. **Speichern** saves manually; auto-save and its delay are under **Settings → General**. Starting with version 0.1.80, **Widget packages** can install a local `.wg.zip`. The initial API 0.1 supports validated text widgets with editable properties; installed packages appear as separate palette sets. Since 0.1.83, widget and package images may be validated SVG or PNG files; widgets without an image use the built-in SVG text symbol. Removal is blocked while a package widget is used by any project. Since 0.1.82, the **Tools** tab installs local `.tp.zip` packages. The first declarative tool previews and changes the current page background after confirmation; **Undo** can revert it. Tool images may also be SVG or PNG; Studio action buttons continue to use SVG icons. GitHub installation and updates will follow.

The widget selector in the top bar lets you select several widgets or clear the selection. The action bar provides cut, copy, paste, duplicate, delete and up to 50 undo/redo steps. The ten alignment actions work on multiple selected normal widgets; the first selected widget is the reference. Pressing **Breite** or **Höhe** for about 0.6 seconds opens an exact pixel-size input.

Runtime centers a page when it fits entirely inside the browser window. Larger pages start at the top-left corner; horizontal and vertical scrollbars keep the whole page reachable without changing widget coordinates.

## Widget selection, copying and deletion

![Widget selector in front of the editor](/images/grafik-visual-studio/widget-menu.png)

The checked rows select the same widgets on the canvas. The list stays in front of them; **Copy** and **Delete** act on all checked widgets.

![Multiple pasted widgets moved together](/images/grafik-visual-studio/multi-move.png)

Drag any selected widget to move the entire selection, including after copying and pasting. Selected connections and intermediate points move with it; locked widgets prevent the joint move. Undo reverts the drag as one step.

![Delete confirmation with five-minute suppression option](/images/grafik-visual-studio/delete-dialog.png)

**Cancel** or Escape stops deletion. The checkbox suppresses further prompts for five minutes in this editor session. Deleted widgets can still be restored with Undo.

## Files and image selection

![File search below the Studio root folder](/images/grafik-visual-studio/files-search.png)

The root is **/config/www/studio**. Studio creates it when possible; missing write permissions produce a message. Widget image selection uses this folder too, and public paths start with **/local/studio/**. Search includes all subfolders and matches file names and paths regardless of case; an empty query returns to the open folder. Images, including GIF, can be selected. The up-folder action stays within this root.

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

Enable **Andockpunkte** in a target widget's properties. All points start off on new widgets. **All points** switches the twelve positions together; each point can then be adjusted individually. The group checkbox enables or disables the entire section. Drag SVG connection endpoints onto active points. An intermediate point splits the path into additional segments; only an explicitly enabled **Sammelpunkt** can be selected as a connection by another line. A simple crossing does not connect lines. Available settings include line and zigzag/multi-point paths, colors, width, arrowheads, animation and z-index.

## Visibility and filters

**Generell** and **Sichtbarkeit** exist on every widget and are disabled by default. “Generell” includes name, comment, CSS class, filter word and lock controls. The editor filter can hide matching widgets or show only matching ones. Runtime visibility can evaluate a Home Assistant state with a condition and comparison value; group evaluation remains unfinished.
