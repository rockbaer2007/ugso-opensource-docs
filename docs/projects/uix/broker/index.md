---
title: UIX Broker
description: Deklarative Frontend-Interaktionen für Home Assistant mit UIX Broker.
---
# UIX Broker

::: info Versionsstand
UIX Broker gehört zur stabilen Basis 8.2.0. Zusätzliche Funktionen bis 8.3.0-beta.8 sind auf den jeweiligen Referenzseiten gekennzeichnet. Eine Ausnahme ist `block`: Diese Direktive blockiert das auslösende Event synchron, bevor die übrigen Direktiven laufen.
:::

UIX Broker wandelt Browser-Events, Tastenkürzel und Home-Assistant-Event-Bus-Events in deklarative Interaktionen um. Eine Interaktion wählt ein Browser-Element aus, prüft optionale Regeln und führt anschließend die Direktiven in der konfigurierten Reihenfolge aus.

```text
Realm -> Listen -> Interaction Anchor -> Rules (optionale Anchors) -> Directives (optionale Anchors)
```

Nutze UIX Broker, wenn sich ein Oberflächenverhalten konfigurieren lässt. Broker kann auf Klicks reagieren, Events vor dem erneuten Auslösen verändern, Elemente fokussieren, Objekteigenschaften aktualisieren und sichere Elementmethoden aufrufen. Es kann Buttons, Badges, Text, Tile-Icons, Tooltips und Entsperr-Abfragen ergänzen, Home-Assistant-Aktionen binden oder ausführen, Templates rendern, JavaScript auswerten und zwischen Operationen pausieren.

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
- [Rules](./rules): Host-Elemente, Captured Data, Browser-Identität, Benutzer, Administratorstatus, URL-Fragment, Suchparameter und Panels prüfen.
- [Directives](./directives): `block`, `property`, `event`, `call`, `button`, `badge`, `text-content`, `tile-icon`, `tooltip`, `lock`, `action-handler`, `action`, `template`, `javascript`, `wait`.
- [Examples](./examples): Beispiele. Weitere ausführliche Beispiele können zusätzlich in den UIX Guides veröffentlicht werden.

::: info
Für Browser-Identity-Matching wird [Browser Mod](https://github.com/thomasloven/hass-browser_mod) benötigt.
:::
