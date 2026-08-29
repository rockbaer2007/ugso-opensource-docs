---
title: Mushroom Beispiele
description: Praxisbeispiele fuer Mushroom Cards in Home Assistant.
---
# Beispiele

## Lichtkarte

```yaml
type: custom:mushroom-light-card
entity: light.wohnzimmer
name: Wohnzimmer
show_brightness_control: true
show_color_temp_control: true
use_light_color: true
```

## Klima-Karte

```yaml
type: custom:mushroom-climate-card
entity: climate.wohnzimmer
name: Wohnzimmer
show_temperature_control: true
hvac_modes:
  - heat
  - auto
  - 'off'
```

## Chips Oben Im Dashboard

```yaml
type: custom:mushroom-chips-card
chips:
  - type: entity
    entity: person.uwe
  - type: weather
    entity: weather.home
  - type: entity
    entity: sensor.briefkasten
```

## Template Card

```yaml
type: custom:mushroom-template-card
primary: Wohnzimmer
secondary: '{{ states("sensor.wohnzimmer_temperatur") }} °C'
icon: mdi:sofa
icon_color: >-
  {% if is_state('light.wohnzimmer', 'on') %}
    amber
  {% else %}
    grey
  {% endif %}
tap_action:
  action: toggle
entity: light.wohnzimmer
```

## Title Card Als Abschnitt

```yaml
type: custom:mushroom-title-card
title: Wohnzimmer
subtitle: Licht, Klima und Medien
```

## Kombination In Einem Stack

```yaml
type: vertical-stack
cards:
  - type: custom:mushroom-title-card
    title: Wohnzimmer
  - type: custom:mushroom-light-card
    entity: light.wohnzimmer
    show_brightness_control: true
  - type: custom:mushroom-climate-card
    entity: climate.wohnzimmer
    show_temperature_control: true
```
