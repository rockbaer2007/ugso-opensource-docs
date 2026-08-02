---
title: JavaScript-Snippets
description: JavaScript-Beispiele für Webseiten, Lovelace und Bubble-Card.
---

# JavaScript

## Farbe anhand eines Sensorwerts bestimmen

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

## Sicher auf eine Home-Assistant-Entität zugreifen

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

## Ereignislistener für eine Webseite

```javascript
const button = document.querySelector('#start-button');

button?.addEventListener('click', () => {
  console.log('Start wurde angeklickt');
});
```

## JSON sicher einlesen

```javascript
function parseJsonSafe(value) {
  try {
    return JSON.parse(value);
  } catch (error) {
    console.error('Ungültiges JSON:', error);
    return null;
  }
}
```
