---
title: Home Assistant YAML
description: Code snippets for Home Assistant automations, templates and dashboards.
---

# Home Assistant YAML

## Frequency Alarm Outside the Allowed Range

```yaml
alias: Frequency alarm
description: Alarm when grid frequency is below 48.8 Hz or above 50.3 Hz

triggers:
  - trigger: state
    entity_id: sensor.shellypro3em_34987a45f234_phase_a_frequenz

conditions:
  - condition: template
    value_template: >
      {% set frequency =
        states('sensor.shellypro3em_34987a45f234_phase_a_frequenz')
        | float(0)
      %}
      {{ frequency < 48.8 or frequency > 50.3 }}

actions:
  - action: input_boolean.turn_on
    target:
      entity_id: input_boolean.frequenzalarm

mode: single
```

## Add Two Solar Values

```yaml
alias: Solar ground floor - update daily max
description: Stores the maximum sum of both solar inputs

triggers:
  - trigger: state
    entity_id:
      - sensor.hyper_2000_eg_1_solar_input_power
      - sensor.hyper_2000_eg_2_solar_input_power

variables:
  total_power: >
    {{
      states('sensor.hyper_2000_eg_1_solar_input_power') | float(0)
      +
      states('sensor.hyper_2000_eg_2_solar_input_power') | float(0)
    }}

conditions:
  - condition: template
    value_template: >
      {{ total_power > states('input_number.solar_eg_max') | float(0) }}

actions:
  - action: input_number.set_value
    target:
      entity_id: input_number.solar_eg_max
    data:
      value: "{{ total_power | round(0) }}"

  - action: input_text.set_value
    target:
      entity_id: input_text.solar_eg_max_zeit
    data:
      value: "{{ now().strftime('%H:%M') }}"

mode: single
```

## Template with Output

```jinja
{% set temperature = states('sensor.aussentemperatur') | float(0) %}

{% if temperature < 0 %}
  Frost
{% elif temperature < 15 %}
  Cool
{% else %}
  Warm
{% endif %}
```
