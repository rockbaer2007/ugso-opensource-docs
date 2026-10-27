---
title: Exemples Mushroom
description: Exemples concrets d'utilisation des cartes Mushroom dans Home Assistant.
---
<a id="mushroom-exemples"></a>
<a id="orientation-actuelle"></a>

# Exemples {#beispiele}

## Carte d'éclairage {#lichtkarte}

```yaml
type: custom:mushroom-light-card
entity: light.wohnzimmer
name: Wohnzimmer
show_brightness_control: true
show_color_temp_control: true
use_light_color: true
```

## Carte de climatisation {#klima-karte}

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

## Puces (Chips) en haut du tableau de bord {#chips-oben-im-dashboard}

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

## Carte modèle (Template Card) {#template-card}

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

## Carte de titre en tant que section {#title-card-als-abschnitt}

```yaml
type: custom:mushroom-title-card
title: Wohnzimmer
subtitle: Licht, Klima und Medien
```

## Combinaison dans un empilement (Stack) {#kombination-in-einem-stack}

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
