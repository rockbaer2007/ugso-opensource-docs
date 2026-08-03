---
title: JavaScript Snippets
description: JavaScript examples for websites, Lovelace and Bubble Card.
---

# JavaScript

## Determine Color from a Sensor Value

```javascript
const value = Number.parseFloat(entity?.state);

if (Number.isNaN(value)) {
  return '#9E9E9E';
}

if (value < -20) {
  return '#87CEFA';
}

if (value < -5) {
  return '#4CAF50';
}

if (value < 0) {
  return '#FFEB3B';
}

return '#F44336';
```

## Safely Access a Home Assistant Entity

```javascript
const entityId = 'binary_sensor.wlan_2_4_ghz_status';
const state = hass.states[entityId]?.state ?? 'unknown';

const color =
  state === 'on'
    ? '#4CAF50'
    : state === 'off'
      ? '#F44336'
      : '#9E9E9E';
```

## Event Listener for a Website

```javascript
const button = document.querySelector('#start-button');

button?.addEventListener('click', () => {
  console.log('Start was clicked');
});
```

## Safely Parse JSON

```javascript
function parseJsonSafe(value) {
  try {
    return JSON.parse(value);
  } catch (error) {
    console.error('Invalid JSON:', error);
    return null;
  }
}
```
