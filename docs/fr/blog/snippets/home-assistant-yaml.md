---
title: Home Assistant YAML
description: Extraits de code pour les automatisations, les modèles (templates) et les tableaux de bord Home Assistant.
---
<a id="accueil-assistant-yaml"></a>
<a id="statut"></a>


# Home Assistant YAML {#home-assistant-yaml}

## Alarme de fréquence : hors de la plage autorisée {#frequenzalarm-außerhalb-des-erlaubten-bereichs}

```yaml
alias: Frequenzalarm
description: Alarm bei Netzfrequenz unter 48,8 Hz oder über 50,3 Hz

triggers:
  - trigger: state
    entity_id: sensor.shellypro3em_34987a45f234_phase_a_frequenz

conditions:
  - condition: template
    value_template: >
      {% set frequenz =
        states('sensor.shellypro3em_34987a45f234_phase_a_frequenz')
        | float(0)
      %}
      {{ frequenz < 48.8 or frequenz > 50.3 }}

actions:
  - action: input_boolean.turn_on
    target:
      entity_id: input_boolean.frequenzalarm

mode: single
```

## Additionner deux valeurs solaires {#zwei-solarwerte-addieren}

```yaml
alias: Solar EG – Tagesmax aktualisieren
description: Speichert die maximale Summe beider Solar-Eingänge

triggers:
  - trigger: state
    entity_id:
      - sensor.hyper_2000_eg_1_solar_input_power
      - sensor.hyper_2000_eg_2_solar_input_power

variables:
  gesamtleistung: >
    {{
      states('sensor.hyper_2000_eg_1_solar_input_power') | float(0)
      +
      states('sensor.hyper_2000_eg_2_solar_input_power') | float(0)
    }}

conditions:
  - condition: template
    value_template: >
      {{ gesamtleistung > states('input_number.solar_eg_max') | float(0) }}

actions:
  - action: input_number.set_value
    target:
      entity_id: input_number.solar_eg_max
    data:
      value: "{{ gesamtleistung | round(0) }}"

  - action: input_text.set_value
    target:
      entity_id: input_text.solar_eg_max_zeit
    data:
      value: "{{ now().strftime('%H:%M') }}"

mode: single
```

## Modèle (Template) avec sortie {#template-mit-ausgabe}

```jinja
{% set temperatur = states('sensor.aussentemperatur') | float(0) %}

{% if temperatur < 0 %}
  Frost
{% elif temperatur < 15 %}
  Kühl
{% else %}
  Warm
{% endif %}
```
