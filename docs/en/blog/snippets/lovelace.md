---
title: Lovelace and Bubble Card
description: Code snippets for Home Assistant dashboards and Bubble Card.
---

# Lovelace and Bubble Card

## Dynamic Icon Color

```yaml
type: custom:bubble-card
card_type: button
button_type: state
entity: binary_sensor.wlan_2_4_ghz_status
name: 2.4 GHz
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

## Transparent Background

```yaml
styles: |
  .bubble-button-card-container {
    background: transparent !important;
  }
```

## Show Card Only When Entity Is On

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
  name: Water alarm
  icon: mdi:water-alert
```

## Slider Color Based on Temperature

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
