---
title: Widget catalog
---

# Widget catalog

The current catalog has **46 widgets in three groups**. Names match the editor palette. Entity-bound widgets read the current Home Assistant state at runtime; unbound widgets use preview values. Writes are limited to the widget and entity types listed below. External state changes are currently polled every five seconds. A local slider change immediately affects bound Number and SVG-Line widgets while the write request is sent to Home Assistant.

VIS2-inspired widget names remain in English regardless of the interface language. Former German palette names still work as search terms. Existing custom widget names remain unchanged.

**Writable widgets:** Switch, Icon Toggle Button, Bool Checkbox, Bool Select, Bool SVG, and Bool HTML (control) can control bound `switch`, `light`, or `input_boolean` entities. Bulb on/off controls those entities or sets an `input_number` helper to its configured minimum/maximum. Slider writes only `input_number`; Input val writes `input_number` or `input_text`. In switch mode, State Element writes on/off; in button mode it writes the next configured value to a suitable switchable entity or number/text helper. Controls are disabled for unsupported or unavailable entities. Other widgets do not write HA state.

## HA Grafik – Basis (43)

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
| Slider | Range slider with minimum, maximum and step; min/max labels are optional via checkbox. The limits should match the helper, for example `-200` to `200`. A selected `input_number` helper supplies the current value. Dragging immediately updates dependent Number and SVG-Line widgets; releasing writes to Home Assistant. Without an entity changes stay local. |
| Number | Without an entity, previews its title, unit, multiplier, decimal places, prefix and suffix. With a selected HA entity, editor and runtime show only the formatted current numeric value; missing values display `--`. Separate from the graphical Red Number widget. |
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

## HA Grafik – Spezial (2)

| Widget | Current behavior |
| --- | --- |
| [SVG-Line](./zeichnen) | Draws and animates links between widgets with docking points, manual multi-point paths and intentional collector-point joins. |
| [Linebox](./zeichnen#linebox-as-an-invisible-distributor) | Visible in the editor: sums incoming line values and passes the result to outgoing lines and optionally a Home Assistant number helper. A configurable circle covers joined line ends at runtime. |
