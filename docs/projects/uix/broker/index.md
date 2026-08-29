---
title: UIX Broker
description: Deklarative Frontend-Interaktionen für Home Assistant mit UIX Broker.
---
# UIX Broker

::: info Verfügbar ab UIX 8.2.0-beta.2
UIX Broker ist eine neue Funktion aus dem aktuellen UIX-Entwicklungszweig. Die stabile Basis dieser deutschen Doku bleibt weiterhin UIX 8.1.0, bis das nächste stabile Release veröffentlicht ist.
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
- [Rules](./rules): Host-Element-, Captured-Data- und Browser-Identity-Regeln.
- [Directives](./directives): `block`, `property`, `event`, `call` und Home-Assistant-Actions.
- [Examples](./examples): Beispiele. Weitere ausführliche Beispiele können zusätzlich in den UIX Guides veröffentlicht werden.

::: info
Für Browser-Identity-Matching wird [Browser Mod](https://github.com/thomasloven/hass-browser_mod) benötigt.
:::

## Geplante Funktionen

UIX Broker ist aktiv in Entwicklung. Bisherige Funktionen und Beispiele entstanden aus Nutzerideen aus dem Community-Forum. Neue Ideen sollten als [GitHub Discussion](https://github.com/Lint-Free-Technology/uix/discussions) gestartet werden. Funktionen mit ausreichend Interesse können später als Feature Request in den UIX-Issue-Tracker wandern.

Geplante Erweiterungen sind unter anderem:

- **JavaScript-Regel**: Führt JavaScript mit dem aktuellen Interaktionszustand als Variablen aus und gibt ein Ergebnisobjekt zurück.
- **Erweiterte JavaScript-Action-Direktive**: Erlaubt Rückgaben aus der Action, um weitere Direktiven fortzusetzen oder abzubrechen.
- **Jinja2-Template-Regel**: Rendert ein einmaliges Jinja2-Template und kann ein Wahr/Falsch-Ergebnis sowie optionale Objektdaten liefern.
