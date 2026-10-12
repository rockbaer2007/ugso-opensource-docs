---
title: Basic widgets
---

# Basic widgets

**Studio 0.1.293** extends the 48 Basic entries following the VIS-2 review. These are independent HA implementations. Existing projects retain IDs, property-group keys, values, CSS and previous modes. New appearance modes change old widgets only when explicitly selected.

**Basic language** follows Studio or independently selects DE/EN/FR for properties, guidance and new Basic runtime messages. User text and entity values are unchanged. The complete Studio shell remains DE/EN.

## Values and actions

Number offers thousands separators, automatic decimals, a quality entity and CSS classes. Reference mode explicitly uses numeric-prefix parsing and singular selection after formatting; the previous mode remains. Bool HTML/control add on/off sentinels, HTML additions and extra HA targets. The server checks supported entities, availability and limits. Main and extra actions are not atomic; an extra-write failure prevents the subsequent extra URL action.

AckFlag HTML uses an explicitly selected acknowledgment entity or attribute. HA has no ioBroker ACK flag. Old projects keep their old state source; missing acknowledgment is never displayed as confirmed.

Links select a target window. Notes optionally show sanitized HTML; the dialog still writes only text to an available input_text helper without an attribute. New widgets use inert formatting; existing markup and previous modes remain without rewriting saved data. Use iFrame for complex pages. Executable ioBroker bindings are not imported.

## Appearance and navigation

Additional control offers main target plus extra action or separate target only. The second mode writes exclusively to the separate target; an unconfigured direction stays disabled without falling back to the main target.

Checkbox, Select and Bar offer previous/native/modern appearance. Tables add classic tclass hooks and a modern sticky-header layout while retaining JSON, events, selection, acknowledgment, details and columns. Custom VIS CSS may need adaptation; markup is not pixel-identical.

New fullscreen widgets use state-following icons, notice Escape and are disabled in the editor; old text buttons remain. HTML navigation can replace a View-in-widget subview without leaving the main page. Screen Resolution can show project/page details. Grouping uses the existing Studio model.

Localized time supports auto, date/time tokens, month/weekday names, 12-hour clocks, milliseconds and `[literals]`. Select seconds or milliseconds explicitly for numeric timestamps; auto uses a size heuristic. Relative time updates every second. TimesValue and Timestamp Value intentionally remain separate entries sharing their source.

## Speech, runtime exit and groups

Speech to Text starts only on a click and supports single/start-stop/continuous recognition, DE/EN/FR recognition languages, keywords, five status icons and colors. Output stays local or goes to available input_text. Browser support, microphone permission and usually HTTPS are required; browser recognition may need internet.

HTML logout leaves runtime for a return URL or tries to close a script-opened window. **It does not sign out the HA account.**

Group visibility accepts HA IDs such as `system-admin` and `system-users`, separated by semicolons. Only active viewers confirmed by the Ingress proxy receive groups; unknown/local viewers have none. Hide/disable applies when the group or state condition fails. This controls presentation, not API authorization.

[Detailed DE/EN/FR guide](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/basic-widgets-0.1.293.md) · [Previous-state VIS-2 review](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/vis2-basic-audit-2026-10-12.md) · [Deutsch](/projects/grafik-visual-studio/basic) · [Français](/fr/projects/grafik-visual-studio/basic).
