---
title: Widget catalog
---

# Widget catalog

The current catalog has **51 widgets in four groups**. Names match the editor palette. Entity-bound widgets read the current Home Assistant state at runtime; unbound widgets use preview values or explicitly configured docking inputs. Writes are limited to the widget and entity types listed below. External state changes are currently polled every five seconds. A local slider change immediately affects bound Number and SVG-Line widgets while the write request is sent to Home Assistant.

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
| Bool HTML | Displays one of two HTML contents for the current Boolean state, with optional prepended/appended HTML. |
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

### Migration hints

Use **Settings → General → Show migration hints** to enable or disable the hints centrally. The choice is saved per project and defaults to enabled. Hints appear directly below relevant editor fields and explain compatible HA switch targets or helpers, JSON/index sources and extra controls that are not connected yet. Read-only display does not require an additional write helper. Text uses 10px regular type, light red on dark editor backgrounds and dark red on light backgrounds. Hints do not appear in the runtime.

### Table

**Static JSON (ohne ID)** contains an array of row objects. A bound HA entity supplies its JSON state in the runtime instead. For `[{"Title":"first","Value":1,"_Description":"Value1"},{"Title":"second","Value":2,"_Description":"Value2"}]`, the visible columns are **Title** and **Value**. Underscore attributes are hidden metadata; `_btn…` creates an acknowledgment button. Cells support sanitized HTML.

**Kolumnanzahl** exposes column title, CSS width and attribute settings. Explicit attribute mappings can expose metadata. **Kein Header**, **Zeige Scrollbar**, and **Maximale Zeilenanzahl** control presentation. New tables have CSS groups disabled. A print button appears only when **btn_print** has a caption; **view_for_print** optionally selects the print page.

**Ereignis ID** reads individual JSON rows. Its initial state is not collected as a new event. Changes add event rows; matching `_id` values replace existing event rows. **Neues Ereignis am Anfang** affects the event list without reversing the base table. Events and selection last for the current runtime session.

Selecting a row writes its JSON to **Ausgewählt ID** (`input_text`) and displays `_detail` in **Detailed widget**. Acknowledgment buttons write `_ack_id` or the row JSON to **Bestätigung ID**. HA targets must be available, compatible number/text helpers; their type and length limits still apply. The editor does not write HA values.

### Bool Select

The dropdown has two entries configured through **Text bei 'false'** and **Text bei 'true'**. It reads Boolean and numeric states: `0` is false, other numbers are true. HA states `off`/`on` are normalized accordingly. Prepended/appended HTML and autofocus are supported; autofocus applies only in the runtime.

A selection writes `0` or `1` to a compatible `input_number` or `input_text` helper. For `switch`, `light`, and `input_boolean`, it sends the corresponding HA switch command. Unsupported or unavailable targets are disabled. Without an entity, a local runtime preview is possible; the editor does not write values. New widgets start with empty text/HTML fields, autofocus disabled, and all CSS groups disabled. Existing captions are preserved.

### Bool Checkbox

The checkbox displays the bound Home Assistant entity state. In the runtime it can control `switch`, `light`, and `input_boolean`; it is disabled without an available, supported entity. In the editor it is a preview only.

**HTML voranstellen** and **HTML anhängen** add text or HTML before and after the checkbox. **Autofokus** applies only in the runtime. New widgets start with empty HTML fields, autofocus disabled, and all CSS groups disabled. Existing settings are preserved.

### Bool HTML

From **0.1.146**, prepended HTML, appended HTML, **HTML for 'false'** and **HTML for 'true'** all offer HTML-editor controls. The entity state selects the content; without an entity, the test state supplies a preview. Boolean `true`, number `1` and the strings `true`, `on`, `ein`, `yes` and `1` select the true content; other states select false. Prepended and appended HTML appear for either state. Studio HTML sanitization applies to all four fields.

New widgets start with empty HTML fields and disabled CSS groups. Existing configured content is preserved. **Bool HTML** only displays a state and does not switch an entity; use **Bool HTML (control)** for that purpose.

### ValueList HTML

From **0.1.144**, **Test value (editor only)** selects an index from the available entries. **Live value / preview state** also shows the normal widget state in the editor. Selecting a test index changes neither the stored preview state nor the HA value; runtime always uses the bound entity state or the unbound preview state.

Separate entries with semicolons or newlines: `Test;test2;test3` provides indices 0, 1 and 2. Commas remain part of the text: `Test, test2, test3` is one entry. Write a semicolon inside an HTML entry as `§§`, for example in a CSS style or HTML entity. Prepended and appended HTML surround the selected entry; HTML follows Studio sanitization rules. Missing, invalid or out-of-range states display no list entry. New ValueList HTML widgets start with all CSS groups disabled; existing settings are preserved.

### ValueList HTML Style

From **0.1.145**, individual **Value [0]** through **Value [n]** sections provide HTML content and a CSS style. The configured count is the highest index: `2` provides three entries and `0` provides one. Studio supports up to index 50. Legacy list fields remain available as fallback values.

**Test value (editor only)** selects an entry for preview only. Runtime reads the index from the bound entity or unbound preview state; `true` and `false` correspond to 1 and 0. This is an index, not a measurement range: with entries `10`, `20`, `30`, state `2` displays `30`; state `30` is outside a list ending at index 2 and displays no entry.

Entry styles also apply to prepended and appended HTML. Use complete CSS declarations, such as `font-weight: bold; color: #29c8b5; font-size: 20px;`. Plain `bold` has no effect. Studio accepts its approved presentation styles without external CSS URLs. General CSS groups start disabled on new widgets; individual entry styles remain independently usable.

## HA Grafik – Interaktiv (1)

| Widget | Current behavior |
| --- | --- |
| State Element | Up to five states, each with an icon, image, text or HTML; switch, button, display-only and navigation modes. Reads a bound entity and can write to suitable entities in switch/button mode. |

## HA Grafik – Data flow (3)

| Widget | Current functionality |
| --- | --- |
| [Value connection](./datenfluss) | Directed internal value transfer; simple editor line, invisible in runtime. |
| [Value converter](./datenfluss) | Converts numbers, text, switch states and units with a dedicated dialog and type preview; invisible in runtime. |
| [Value calculation](./datenfluss) | Same four calculations as SVG LineBox Math; invisible in runtime by default. |

## HA Grafik – Spezial (3)

| Widget | Current behavior |
| --- | --- |
| [SVG-Line](./svg-line) | Draws and animates links between widgets with docking points, manual multi-point paths and intentional collector-point joins. |
| [SVG LineBox Math](./svg-linebox-math) | Visible square with 16 ports A–P. Custom formulas or occupied-input averages; multiple connections sum per port. Internal output without an additional HA entity. |
| [SVG LineBox](./svg-linebox) | Visible in the editor: sums incoming line values and passes the result to outgoing lines and optionally a Home Assistant number helper. A configurable circle covers joined line ends at runtime. |
