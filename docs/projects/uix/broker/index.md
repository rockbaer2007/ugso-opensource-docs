---
title: UIX Broker
description: Deklarative Frontend-Interaktionen für Home Assistant mit UIX Broker.
---
# UIX Broker

::: info Versionsstand
UIX Broker gehört zur stabilen Basis 8.2.0. Zusätzliche Funktionen bis 8.3.0-beta.8 sind auf den jeweiligen Referenzseiten gekennzeichnet.
:::

UIX Broker wandelt Browser-Events, Tastenkürzel und Home-Assistant-Event-Bus-Events in deklarative Interaktionen um. Eine Interaktion wählt ein Browser-Element aus, prüft optionale Regeln und führt anschließend die Direktiven in der konfigurierten Reihenfolge aus.

```text
Realm -> Listen -> Interaction Anchor -> Rules (optionale Anchors) -> Directives (optionale Anchors)
```

Nutze UIX Broker, wenn ein Verhalten konfiguriert werden kann, ohne dafür eine eigene Karte, ein Script oder einen Patch zu schreiben. Broker kann zum Beispiel auf Klicks reagieren, Events vor dem erneuten Auslösen anpassen, Elemente fokussieren, Objekt-Properties setzen, sichere Methoden eines Elements aufrufen oder JavaScript-Actions mit Interaktionsvariablen ausführen.

```yaml
uix_broker:
  - realm: browser
    listen: click
    anchor: target
    rules:
      - ".action-button"
    directives:
      - type: block
      - type: event
        name: another-action
        data:
          source: action-button
```

## UIX-Broker-Seiten

- [Broker](./broker): Struktur, Konfigurationsquellen, Lebenszyklus und Debugging.
- [Realms](./realms): Browser-Events, Tastenkürzel und Home-Assistant-Event-Bus-Events.
- [Interaction Anchors](./interaction-anchors): Auswahl von Elementen über Event-Pfad und `select_tree`.
- [Rules](./rules): Host-Element-, Captured-Data-, Browser-, Benutzer-, URL- und Panel-Regeln.
- [Directives](./directives): `block`, `property`, `event`, `call`, `button`, `tile-icon`, `tooltip`, Actions, Templates, JavaScript und Wartezeiten.
- [Examples](./examples): Beispiele. Weitere ausführliche Beispiele können zusätzlich in den UIX Guides veröffentlicht werden.

::: info
Für Browser-Identity-Matching wird [Browser Mod](https://github.com/thomasloven/hass-browser_mod) benötigt.
:::

## Geplante Funktionen

UIX Broker ist aktiv in Entwicklung. Bisherige Funktionen und Beispiele entstanden aus Nutzerideen aus dem Community-Forum. Neue Ideen sollten als [GitHub Discussion](https://github.com/Lint-Free-Technology/uix/discussions) gestartet werden. Funktionen mit ausreichend Interesse können später als Feature Request in den UIX-Issue-Tracker wandern.

Geplante Erweiterungen sind unter anderem:

- **JavaScript-Regel**: Führt JavaScript mit dem aktuellen Interaktionszustand als Variablen aus und gibt `{result: <truthy>, [optional] namedObject: <object data>}` zurück. Optionale `namedObject`-Daten stehen späteren Regeln und Direktiven zur Verfügung.
- **Erweiterte JavaScript-Action-Direktive**: Gibt `{continue: <truthy>, [optional] namedObject: <object data>}` zurück. Bei falschem `continue` werden keine weiteren Direktiven ausgeführt; optionale Objektdaten stehen den übrigen Direktiven zur Verfügung.
- **Jinja2-Template-Regel**: Rendert ein einmaliges Jinja2-Template und kann ein Wahr/Falsch-Ergebnis sowie optionale Objektdaten liefern.
