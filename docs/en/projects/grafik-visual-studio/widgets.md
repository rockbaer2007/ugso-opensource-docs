---
title: Widget catalog
---

# Widget catalog

The current catalog has **48 widgets in three groups**. Names match the editor palette. Entity-bound widgets read the current Home Assistant state at runtime; unbound widgets use preview values. Writes are limited to the widget and entity types listed below. External state changes are currently polled every five seconds. A local slider change immediately affects bound Number and SVG-Line widgets while the write request is sent to Home Assistant.

VIS2-inspired widget names remain in English regardless of the interface language. Former German palette names still work as search terms. Existing custom widget names remain unchanged.

From Studio 0.1.135, technical widget names stay in the editor interface. The canvas and runtime show only custom captions; new widgets start with an empty title. This central policy also covers future widget packages and LineBox. Loading an older project removes previous stock titles once. Custom captions remain; you can then explicitly enter a former stock caption again.

**Writable widgets:** Switch, Icon Toggle Button, Bool Checkbox, Bool Select, Bool SVG, and Bool HTML (control) can control bound `switch`, `light`, or `input_boolean` entities. Bulb on/off controls those entities or sets an `input_number` helper to its configured minimum/maximum. Slider writes only `input_number`; Input val writes `input_number` or `input_text`. In switch mode, State Element writes on/off; in button mode it writes the next configured value to a suitable switchable entity or number/text helper. Controls are disabled for unsupported or unavailable entities. Other widgets do not write HA state.

## HA Grafik – Basis (44)

| Widget | Current behavior |
| --- | --- |
| Tabs | Starting with Studio 0.1.116: 1–20 horizontal or vertical tabs; horizontal variants are standard, centered or full width. Each tab has a title, icon or image, icon size/color and X/Y overflow settings. Content is an owned widget surface or an existing project page. Runtime embeds only the active content and remembers the selection locally in the browser. |

### Editing Tabs

From Studio 0.1.122, the main **Tabs** settings include **Dim inactive tabs (%)**, ranging from 0 to 90. At 0, colors remain unchanged; at 90, 10% brightness remains. Inactive header backgrounds, text and icons are dimmed together; the active header and tab content stay unchanged. This applies to horizontal and vertical layouts and is saved with the project.

From Studio 0.1.121, the main **Tabs** settings offer separate **Active text color** and **Inactive text color**. They apply to all tab labels according to the current selection. Empty values use the existing **Tab color**. Per-tab icon colors remain independent; Tab color still controls the active marker.

From Studio 0.1.120, **Overflow X** and **Overflow Y** offer `none`, `visible`, `hidden`, `scroll`, `auto`, `initial` and `inherit`. `none` removes the explicit CSS override, `visible` shows overflowing content, `hidden` clips it, `scroll` enables scrollbars and `auto` shows them when needed. `initial` uses the CSS initial value; `inherit` takes the parent element's setting. Without a saved selection, `auto` remains the default. CSS can affect both axes together, particularly when `visible` is combined with a scrollable other axis.

From Studio 0.1.119, each **Tab [n]** offers an independent **Tab background color**. It colors that tab header in horizontal and vertical layouts; the active tab marker remains visible.

Add **Tabs** from the palette and configure width and height once on the owner widget. Choose the content source under **Tab [1]**, **Tab [2]**, etc. **Edit tab surface** opens the owned surface with the normal widget palette or opens the referenced project page. **Back to Tabs widget** returns to the owner. Owned content dimensions follow the owner minus 44 px for horizontal tabs or up to 120 px for vertical tabs (at most half the widget width). Owned surfaces belong to the widget and are not separate project pages. Existing pages remain shared references; changes affect all embeddings.

From Studio 0.1.124, active tab contents render directly from the open project, without an iframe or reloading when switching tabs. Clicking the content area opens it for editing; returning immediately shows unsaved edits too. Continue saving before opening a separate runtime, especially with Auto-Save disabled. Runtime state polling includes active tab contents. Larger existing pages are shown without automatic scaling; X/Y overflow controls scrolling. Reducing the tab count preserves hidden owned contents, which reappear when the count is increased. Copying, grouping and export/import preserve owned contents; copies receive new widget and group IDs. Cyclic page embeddings are blocked. Nested Tabs widgets within owned surfaces are not supported yet. This is an original implementation and does not provide VIS2 import.

### Other basic widgets

| Widget | Current behavior |
| --- | --- |
| link | Formatted HTML content linking to a URL. |
| Note | Note with text or HTML and an optional folded corner. |
| Screen Resolution | Displays the current window resolution. |
| Red Number | Number displayed as a colored circle or pin with adjustable radius. |
| Bool SVG | Selects one of two SVG drawings according to the current state; can control a switchable entity. |
| SVG shape | Draws an SVG shape with color, stroke, rotation and scaling. |
| Input val | Bordered text or number input. At runtime it reads and writes a selected `input_number` or `input_text` helper; without an entity it stays local. Auto-set writes after a short typing pause, while withEnter writes only on Enter. |
| View in widget | Embeds a project page while preventing recursive embedding. |
| View in widget 8 | Selects one of up to 50 pages using the index state. |
| iFrame | Embeds a URL if the target permits it; offers frame, scrolling and refresh settings. |
| iFrame 8 | Selects one of up to 20 configured frames using the index state. |
| Image 8 | Selects one of up to 50 images using the index state. |
| AckFlag HTML | Displays two configurable HTML states; Home Assistant has no native ioBroker `ack` flag. |
| Icon Toggle Button | Button with separate on/off images; can control a switchable entity. |
| Switch | On/off switch; can control a switchable entity. |
| Bool Checkbox | On/off checkbox; can control a switchable entity. |
| Bulb on/off | Lamp with separate on/off images; controls a switchable entity or number helper. |
| Slider | Range slider with minimum, maximum and step; min/max labels are optional via checkbox. The limits should match the helper, for example `-200` to `200`. A selected `input_number` helper supplies the current value. Dragging immediately updates dependent Number and SVG-Line widgets; releasing writes to Home Assistant. Without an entity changes stay local. Starting with Studio 0.1.114, track color, active color, thickness and rounding are configurable separately from thumb color, size and rounding. Track fill supports Normal (minimum to value), Inverted (value to maximum) or no active fill. Track and thumb have independent shadows with X/Y offsets, blur, spread and CSS/RGBA color. Rounding: 0% square, 100% fully rounded; all-zero shadow dimensions disable the shadow. Scale marks remain available above/below with optional numbers. |
| Number | Shows the formatted numeric value with multiplier and decimal places; missing entity values display `--`. From Studio 0.1.125, **HTML prefix** and **HTML suffix (singular/plural)** also appear for bound HA entities in editor and runtime and survive immediate state updates. Singular applies when the scaled numeric value equals 1, otherwise plural; an empty HTML suffix falls back to the configured unit. The preview title is shown without an entity. Separate from the graphical Red Number widget. |
| String | Text value with optional icon and HTML before or after the value. |
| String (unescaped) | Displays an HTML value with prefix and suffix. |
| String img src | Displays an image from a URL in the state. |
| TimesValue | Formats a time from the state. |
| Timestamp Value | Formats a timestamp from the state. |
| Timestamp | Formats the last Home Assistant update time. |
| Last change Timestamp | Formats the last Home Assistant state change time. |
| ValueList Text | Displays a list entry selected by the index state as text. |
| ValueList HTML | Displays a list entry selected by the index state as HTML. |
| ValueList HTML Style | Displays an HTML list entry with its CSS style. |
| Bool HTML | Displays one of two HTML contents for the current Boolean state. |
| Bool Select | On/off select control with configurable labels; can control a switchable entity. |
| Bool HTML (control) | Clickable on/off HTML display; can control a switchable entity. |
| HTML State | Custom HTML with optional click link and value placeholder. |
| Table | Table from JSON with row selection and print action; a bound HA state must contain JSON rows. |
| Full Screen | Button toggling fullscreen mode for the interface. |
| Bar | Horizontal or vertical bar based on a numeric value. |
| HTML | Custom HTML content. |
| HTML navigation | Button or link to a project page, URL or Home Assistant path. |
| filter - dropdown | Filters runtime widgets by their “Filterwort” property in “Generell”. |
| Text | Free text field without entity binding. |
| Border | Frame with title, title position, header area and colors. |
| Gauge | Simple value gauge with unit. |
| Image | Displays a configured image source or a URL from the entity state; live camera binding is not yet available. |

## HA Grafik – Interaktiv (1)

| Widget | Current behavior |
| --- | --- |
| State Element | Up to five states, each with an icon, image, text or HTML; switch, button, display-only and navigation modes. Reads a bound entity and can write to suitable entities in switch/button mode. |

## HA Grafik – Spezial (3)

| Widget | Current behavior |
| --- | --- |
| [SVG-Line](./svg-line) | Draws and animates links between widgets with docking points, manual multi-point paths and intentional collector-point joins. |
| [SVG LineBox Math](./svg-linebox-math) | Visible square with 16 ports A–P. Custom formulas or occupied-input averages; multiple connections sum per port. Internal output without an additional HA entity. |
| [SVG LineBox](./svg-linebox) | Visible in the editor: sums incoming line values and passes the result to outgoing lines and optionally a Home Assistant number helper. A configurable circle covers joined line ends at runtime. |
