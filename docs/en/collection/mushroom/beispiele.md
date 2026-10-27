---
title: Mushroom examples
description: Practical examples for Mushroom Cards in Home Assistant.
---
<a id="mushroom-examples"></a>
<a id="current-focus"></a>

# Examples {#beispiele}

## Light card {#lichtkarte}

```yaml
type: custom:mushroom-light-card
entity: light.wohnzimmer
name: Wohnzimmer
show_brightness_control: true
show_color_temp_control: true
use_light_color: true
```

## Climate card {#klima-karte}

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

## Chips At The Top Of The Dashboard {#chips-oben-im-dashboard}

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

## Template Card {#template-card}

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

## Title Card As a section {#title-card-als-abschnitt}

```yaml
type: custom:mushroom-title-card
title: Wohnzimmer
subtitle: Licht, Klima und Medien
```

## Combination In One Stack {#kombination-in-einem-stack}

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
