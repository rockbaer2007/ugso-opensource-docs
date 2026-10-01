---
title: Widget catalog
---

# Widget catalog

The current catalog has **45 widgets in three groups**. Names match the editor palette. Some widgets still use sample values or change state only locally; full live Home Assistant binding is not yet available. An entity ID field does not imply that the entity can already be controlled.

VIS2-inspired widget names remain in English regardless of the interface language. Former German palette names still work as search terms. Existing custom widget names remain unchanged.

## HA Grafik – Basis (43)

| Widget | Current behavior |
| --- | --- |
| link | Formatted HTML content linking to a URL. |
| Note | Note with text or HTML and an optional folded corner. |
| Screen Resolution | Displays the current window resolution. |
| Red Number | Number displayed as a colored circle or pin with adjustable radius. |
| Bool SVG | Selects one of two SVG drawings according to a sample Boolean state. |
| SVG shape | Draws an SVG shape with color, stroke, rotation and scaling. |
| Input val | Local text or number input with display and input options. |
| View in widget | Embeds a project page while preventing recursive embedding. |
| View in widget 8 | Selects one of up to 50 pages using a sample index value. |
| iFrame | Embeds a URL if the target permits it; offers frame, scrolling and refresh settings. |
| iFrame 8 | Selects one of up to 20 configured frames using a sample index. |
| Image 8 | Selects one of up to 50 images using a sample index. |
| AckFlag HTML | Displays two configurable HTML states; Home Assistant has no native ioBroker `ack` flag. |
| Schaltfläche (Icon Ein/Aus) | Button with separate on/off images; state changes are local for now. |
| Switch | On/off switch; state changes are local for now. |
| Bool Checkbox | On/off checkbox; state changes are local for now. |
| Bulb on/off | Lamp with separate on/off images; state changes are local for now. |
| Slider | Range slider with minimum, maximum and step; value changes are local for now. |
| Number | Number with unit, multiplier, decimal places, prefix and suffix; separate from the graphical Red Number widget. |
| String | Text value with optional icon and HTML before or after the value. |
| String (unescaped) | Displays an HTML sample value with prefix and suffix. |
| String img src | Displays an image from a URL in the sample value. |
| TimesValue | Formats a time from the sample state. |
| Timestamp Value | Formats a timestamp from the sample state. |
| Timestamp | Formats the stored last-updated time. |
| Last change Timestamp | Formats the stored last-changed time. |
| ValueList Text | Displays a selected list entry as text. |
| ValueList HTML | Displays a selected list entry as HTML. |
| ValueList HTML Style | Displays an HTML list entry with its CSS style. |
| Bool HTML | Displays one of two HTML contents for a sample Boolean state. |
| Bool Select | On/off select control with configurable labels. |
| Bool HTML (control) | Clickable on/off HTML display; changes are local for now. |
| HTML State | Custom HTML with optional click link and value placeholder. |
| Table | Table from sample JSON with row selection and print action. |
| Full Screen | Button toggling fullscreen mode for the interface. |
| Bar | Horizontal or vertical bar based on a sample value. |
| HTML | Custom HTML content. |
| HTML navigation | Button or link to a project page, URL or Home Assistant path. |
| filter - dropdown | Filters runtime widgets by their “Filterwort” property in “Generell”. |
| Text | Free text field without entity binding. |
| Border | Frame with title, title position, header area and colors. |
| Messanzeige | Simple value gauge with unit. |
| Image | Displays a configured image source; live camera binding is not yet available. |

## HA Grafik – Interaktiv (1)

| Widget | Current behavior |
| --- | --- |
| Zustands-Element | Up to five sample states, each with an icon, image, text or HTML; switch, button, display-only and navigation modes. Local runtime interaction works, but Home Assistant writes are not yet available. |

## HA Grafik – Spezial (1)

| Widget | Current behavior |
| --- | --- |
| [SVG-Verbindungslinie (drawing)](./zeichnen) | Draws and animates links between widgets with docking points, manual multi-point paths and intentional collector-point joins. |
