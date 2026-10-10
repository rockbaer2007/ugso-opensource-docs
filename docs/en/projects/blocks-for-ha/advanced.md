---
title: Extended HA automations and Jinja
description: Triggers, conditions, targets, action groups and experimental Jinja recognition.
---

# Extended HA automations and Jinja

Since **0.1.39**, there are 148 block types. **HA extended** and **Jinja (experimental)** complement the simple blocks. Simple imported steps retain their existing shapes. Additional fields appear as editable JSON in extended blocks. Import checks the supported structure; verify integrations, device IDs, templates and execution in Home Assistant.

## Triggers and conditions

| Area | Supported additions |
| --- | --- |
| State | Multiple entities; `from`, `to`, `not_from`, `not_to`, lists and `null`; attributes and `for`. |
| Numbers | Both bounds, helper entities as bounds, attributes, `value_template`, duration and multiple entities. |
| Time | Times and lists, time helpers/sensors, time source with offset, weekdays and time patterns. |
| Sun and HA | Sunrise/sunset with offset; startup and shutdown. |
| More triggers | MQTT, template, webhook, zone, device, tag, conversation, geolocation, event and classic calendar. |
| Integrations | `calendar.event_started/ended`, `temperature.changed`, `power.changed`, `motion.detected`, `timer.finished`. Device, area, floor and label targets are also supported. |
| Conditions | Time/weekday, state with lists/attribute/duration/`match`, numeric bounds, sun, zone, device, trigger ID, template and nested AND/OR/NOT. Template shorthand is preserved. |

The integration block provides a dropdown for power, motion and timers. Enter targets and options separately. Changing the integration replaces unchanged example values; custom values remain. Extended JSON triggers support `alias`, `enabled`, `id` and trigger variables. Unknown types and unsupported fields are rejected with a message.

## Targets, variables and options

**HA action with target type** offers `entity_id`, `device_id`, `area_id`, `floor_id` and `label_id`. Enter an ID, JSON list or HA template. Use **HA step (extended)** for multiple target types together. Action data may be an object or a complete HA template; import preserves either form.

Variables also support lists and nested objects. Common step options `alias`, `enabled` and `continue_on_error` are preserved, as are response variables and metadata. Extended blocks provide JSON fields for these. `enabled` accepts a Boolean or HA template; `continue_on_error` accepts a Boolean.

Under **Projekt & Beschreibung → HA options**, edit `variables`, `trigger_variables`, `initial_state`, `trace.stored_traces` and `max_exceeded`. **Apply** accepts valid options only. Omitted options are removed; `{}` removes every option managed by this field. Name and execution mode remain separate. An automation without `alias` can be imported; its filename falls back to `automation.yaml`. The surrounding app controls currently remain German.

## Waiting and action groups

- **Wait for trigger** connects a trigger chain and offers `timeout` / `continue_on_timeout` in its options field.
- **Action group** generates a native `sequence` with connectable steps.
- **Parallel** starts native parallel branches. **+ / −** allows 1–100 branches. Removing an occupied branch leaves its contents disconnected; reconnect or delete them.
- **Continue only if** generates a condition as an action step. Event, Assist response and scene have dedicated blocks.
- Repeats also support literal lists/objects for `for_each`; delays accept combined units and fractions. Extended or mixed branch shapes remain JSON steps.

These blocks export native HA flows. Execution takes place in HA; there is no local script engine.

## Jinja (experimental)

**Jinja einlesen** above the workspace opens a dialog. Paste the template, check the preview, optionally choose **Als Bedingung**, then click **Block erstellen**. The new block appears beside the automation and must be connected. Alternatively, drag value/condition blocks from the category. Imported template values and conditions also use Jinja blocks unless a more specific simple shape matches.

![Experimental Jinja value block](/assets/blocks-for-ha/blocks/en/ugso_jinja_value.png)

Analysis recognizes common patterns: entity states and attributes, date/time, variables, filter chains, `if/else` and `for`. The block shows recognized entities and filters. Comments, string literals and `raw` sections are skipped when searching for references. The preview flags incomplete control structures.

::: warning Recognition limits
This is conservative pattern analysis, not a complete Jinja parser, automatic decomposition into executable sub-blocks or a syntax guarantee. Unknown functions and complex templates retain their editable original text. Text is neither rewritten nor executed locally. Test in HA. Within a composed expression, only a single Jinja expression is supported; complete `if/for` templates belong in a standalone value block.
:::

Blockly projects also retain shapes and positions. YAML → Blockly → export preserves supported values, including omitted optional fields. Limits: 100 chain entries/branches, 10 flow/condition nesting levels and bounded data/template sizes. Integration-specific device options are not exhaustive; rejected fields are never silently removed.

## Original sources and licenses

Original UGSo implementation based on public specifications, without copying ioBroker’s execution engine. Blockly/plugin licenses appear under **Über & Lizenzen**; the app uses Apache-2.0.

- [HA triggers](https://www.home-assistant.io/docs/automation/trigger/), [conditions](https://www.home-assistant.io/docs/scripts/conditions/), [script building blocks](https://www.home-assistant.io/docs/scripts/) and [automation YAML](https://www.home-assistant.io/docs/automation/yaml/).
- [Power changed](https://www.home-assistant.io/triggers/power.changed/), [motion detected](https://www.home-assistant.io/triggers/motion.detected/), [timer finished](https://www.home-assistant.io/triggers/timer.finished/).
- [Jinja templates](https://jinja.palletsprojects.com/en/stable/templates/) and [HA templates](https://www.home-assistant.io/docs/configuration/templating/).
- [Blockly custom blocks](https://docs.blockly.com/guides/create-custom-blocks/overview/) and [UGSo source](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/blocks_for_ha).
