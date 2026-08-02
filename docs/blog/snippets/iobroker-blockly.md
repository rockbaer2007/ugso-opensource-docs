---
title: ioBroker Blockly
description: Blockly-Beispiele für den ioBroker-JavaScript-Adapter mit importierbarem XML und erzeugtem JavaScript.
---

# ioBroker Blockly

Hier werden Blockly-Skripte für den **ioBroker-JavaScript-Adapter** veröffentlicht.

Zu jedem Beispiel können folgende Inhalte gezeigt werden:

- Beschreibung der Aufgabe
- benötigte Objekt-IDs
- Screenshot des Blockly-Aufbaus
- importierbarer Blockly-XML-Code
- erzeugtes JavaScript
- Hinweise zur Anpassung

::: info
Blockly ist im ioBroker-JavaScript-Adapter die grafische Alternative zum direkten Schreiben eines JavaScript-Skripts. Für den Austausch ist besonders der exportierte Blockly-XML-Code geeignet.
:::

## Offizielle Quellen

Die vollständige und aktuelle Dokumentation befindet sich im offiziellen Repository des ioBroker-JavaScript-Adapters:

- [ioBroker.javascript – offizielles GitHub-Repository](https://github.com/ioBroker/ioBroker.javascript)
- [Deutsche Dokumentation](https://github.com/ioBroker/ioBroker.javascript/tree/master/docs/de)
- [Offizielle Blockly-Dokumentation](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md)

Die Beispiele auf dieser Seite sind Ergänzungen aus der Praxis. Bei Fragen zu verfügbaren Blöcken, Adapterfunktionen oder Änderungen ist das offizielle Repository die maßgebliche Quelle.

## Datenpunkt bei Änderung überwachen

### Blockly-Aufbau

```text
Trigger:
  Objekt-ID: sensor.0.beispiel.temperatur
  Änderung: wurde geändert

Dann:
  Log-Ausgabe mit dem neuen Wert
```

### Erzeugtes JavaScript

```javascript
on(
  {
    id: 'sensor.0.beispiel.temperatur',
    change: 'ne'
  },
  async (obj) => {
    const value = obj.state.val;
    console.log(`Neue Temperatur: ${value}`);
  }
);
```

## Blockly-XML veröffentlichen

Für Besucher ist der exportierte XML-Code besonders nützlich, da er wieder in Blockly importiert werden kann.

````md
```xml
<xml xmlns="https://developers.google.com/blockly/xml">
  <!-- exportierter ioBroker-Blockly-Code -->
</xml>
```
````

## Schalter abhängig von einem Wert setzen

Wenn die Temperatur größer als 25 °C ist, wird ein Schalter eingeschaltet. Andernfalls wird er ausgeschaltet.

```javascript
on(
  {
    id: 'sensor.0.beispiel.temperatur',
    change: 'ne'
  },
  async (obj) => {
    const temperatur = Number(obj.state.val);

    if (temperatur > 25) {
      setState('javascript.0.beispiel.luefter', true);
    } else {
      setState('javascript.0.beispiel.luefter', false);
    }
  }
);
```

## Datenpunkt lesen

```javascript
const value = getState('sensor.0.beispiel.temperatur').val;

console.log(`Aktueller Wert: ${value}`);
```

## Datenpunkt schreiben

```javascript
setState('javascript.0.beispiel.status', 'Bereit');
```

Mit Bestätigung:

```javascript
setState('javascript.0.beispiel.status', 'Bereit', true);
```

## Verzögert schalten

```javascript
setState('switch.0.beispiel.relay', true);

setTimeout(() => {
  setState('switch.0.beispiel.relay', false);
}, 30 * 1000);
```

## Zeitplan

### Jeden Tag um 09:00 Uhr

```javascript
schedule('0 9 * * *', async () => {
  setState('javascript.0.beispiel.tagesaktion', true);
});
```

### Alle fünf Minuten

```javascript
schedule('*/5 * * * *', async () => {
  console.log('Der Zeitplan wurde ausgeführt.');
});
```

## Mehrere Bedingungen

```javascript
const freigabe =
  getState('javascript.0.beispiel.freigabe').val === true;

const leistung =
  Number(getState('sensor.0.beispiel.solarleistung').val);

if (freigabe && leistung > 500) {
  setState('switch.0.beispiel.pumpe', true);
} else {
  setState('switch.0.beispiel.pumpe', false);
}
```

## Eigene Datenpunkte anlegen

```javascript
createState(
  'javascript.0.beispiel.status',
  'Unbekannt',
  {
    name: 'Beispielstatus',
    type: 'string',
    role: 'text',
    read: true,
    write: true
  }
);
```

## Nachricht an einen Adapter senden

```javascript
sendTo(
  'telegram.0',
  'send',
  {
    text: 'Die Automation wurde ausgeführt.'
  }
);
```

## Veröffentlichung mit Screenshot

Lege Screenshots unter diesem Pfad ab:

```text
docs/public/images/blog/
```

Im Beitrag bindest du das Bild so ein:

```md
![ioBroker Blockly](/images/blog/mein-blockly.png)
```

::: warning
Die gezeigten Objekt-IDs sind Beispiele. Vor dem Einsatz müssen sie durch die tatsächlichen IDs des eigenen ioBroker-Systems ersetzt werden.
:::
