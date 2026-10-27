---
title: Extraits de code JavaScript
description: Exemples JavaScript pour les pages web, Lovelace et Bubble-Card.
---
<a id="javascript-snippets"></a>
<a id="statut"></a>


# JavaScript {#javascript}

## Déterminer une couleur en fonction de la valeur d'un capteur {#farbe-anhand-eines-sensorwerts-bestimmen}

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

## Accéder en toute sécurité à une entité Home Assistant {#sicher-auf-eine-home-assistant-entitat-zugreifen}

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

## Écouteur d'événements pour une page web {#ereignislistener-fur-eine-webseite}

```javascript
const button = document.querySelector('#start-button');

button?.addEventListener('click', () => {
  console.log('Start wurde angeklickt');
});
```

## Lire du JSON en toute sécurité {#json-sicher-einlesen}

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
