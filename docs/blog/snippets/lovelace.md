---
title: Lovelace und Bubble-Card
description: Code-Snippets für Home-Assistant-Dashboards und Bubble-Card.
---

# Lovelace und Bubble-Card

## Dynamische Icon-Farbe

```yaml
type: custom:bubble-card
card_type: button
button_type: state
entity: binary_sensor.wlan_2_4_ghz_status
name: 2,4 GHz
icon: mdi:wifi
show_state: true
modules:
  - liquid_glass_2

styles: |
  .bubble-icon {
    color: ${
      entity?.state === 'on'
        ? '#4CAF50'
        : entity?.state === 'off'
          ? '#F44336'
          : '#9E9E9E'
    } !important;
  }
```

## Transparenter Hintergrund

```yaml
styles: |
  .bubble-button-card-container {
    background: transparent !important;
  }
```

## Karte nur bei eingeschalteter Entität anzeigen

```yaml
type: conditional
conditions:
  - condition: state
    entity: input_boolean.wassersensor_alarm
    state: "on"

card:
  type: custom:bubble-card
  card_type: button
  button_type: state
  entity: input_boolean.wassersensor_alarm
  name: Wasser-Alarm
  icon: mdi:water-alert
```

## Slider-Farbe anhand des Temperaturwerts

```yaml
styles: |
  .bubble-range-fill {
    background-color: ${
      (() => {
        const value = Number.parseFloat(entity?.state);

        if (Number.isNaN(value)) return '#9E9E9E';
        if (value < -20) return '#87CEFA';
        if (value < -5) return '#4CAF50';
        if (value < 0) return '#FFEB3B';

        return '#F44336';
      })()
    } !important;
  }
```
