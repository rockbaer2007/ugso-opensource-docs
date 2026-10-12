---
title: Widget languages, HA sources and Climate
description: DE/EN/FR, attribute sources, units and optional Climate controls from Studio 0.1.296.
---

# Widget languages, HA sources and Climate

From **Studio 0.1.296**, the remaining **62 widget types** (Special, gauges, data flow and seven bundled packages) offer widget properties and runtime messages in **DE/EN/FR**. The overall Studio shell remains DE/EN. [Deutsch](/projects/grafik-visual-studio/ha-quellen-climate) · [Français](/fr/projects/grafik-visual-studio/ha-quellen-climate).

## Choose a language

**Widget language** in project settings defines the default. The widget group with the same name may override it. Calendar+, Energy, Industrial, Printer, Solar, Technic and Weather/Heating work with existing package versions. User labels, entity IDs and saved keys are not translated or rewritten.

## Check an HA source

Bound read sources offer the initially disabled **HA sources and units** group. An empty attribute reads the state; otherwise enter an attribute. **Check source** refreshes the value, discovers attribute names and reports its unit, missing data or incompatible conversion. Structured values receive a JSON structure hint. The attribute must match the widget’s expected schema.

Automatic conversion is optional. For an Energy source it replaces the legacy factor without deleting the setting. Fixed displays/calculations follow their widget unit: Solar W/°C/%, battery energy kWh, Climate native temperature unit. Their target-unit field is locked. Configurable sources support compatible power, energy, temperature, price, length, volume, speed and pressure units. Missing metadata or incompatible units result in unknown values. Native HA write targets remain unchanged.

Energy can read selected numeric Recorder attributes; missing attributes create gaps. Different history attributes of one entity require separate history widgets. Offset-based C/F conversion is not applied to Energy history. The separate thermostat history view retains its native HA sources; source options affect its live display. Recorder is not the complete native Energy dashboard or long-term statistics.

## Climate controls

Enable **Climate controls** on **Technic Thermostat – Temperature**, then select the required options:

- Heating/cooling range with two targets and a shared Apply button.
- HVAC mode and preset.
- Fan mode, vertical and horizontal swing.
- Target humidity and power.

Runtime only offers capabilities/values reported by the device. Limits and step sizes are rechecked server-side. The existing single target remains available; range-only devices use the range controls. Editor mode, read-only settings and unavailable states disable controls. Enlarge widgets with many controls; the additional section scrolls in small widgets.

New groups start disabled. Existing projects, groups and factors remain valid. A successful service call means submission to HA, not physical confirmation. Real devices, Ingress/Companion, external embedding and notification delivery require installation testing.

[HA Climate](https://www.home-assistant.io/integrations/climate/) · [Device capabilities](https://developers.home-assistant.io/docs/core/entity/climate/) · [Audit report](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/remaining-widget-audit-2026-10-12.md)
