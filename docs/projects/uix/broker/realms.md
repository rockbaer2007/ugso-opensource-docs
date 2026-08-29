---
title: Realms
description: Festlegen, wo eine UIX-Broker-Interaktion auf Events lauscht.
---
# Realms

::: info Verfügbar ab UIX 8.2.0-beta.2
UIX Broker gehört zum aktuellen Entwicklungszweig.
:::

Der `realm` einer Interaktion legt fest, wo Broker lauscht und wie `listen` interpretiert wird.

| Realm | `listen` | Event-Quelle | Anchor-Unterstützung |
| --- | --- | --- | --- |
| `browser` | DOM-Event wie `click` oder `show-dialog` | Browser-Events auf `window` in der Capture-Phase | Event-Pfad-Ausdrücke aus dem composed path und `select_tree` |
| `shortcut` | [Tinykeys](https://jamiebuilds.github.io/tinykeys/)-Tastenkürzel wie `"$mod+Shift+K"` | Browser-Keyboard-Event | Event-Pfad-Ausdrücke und `select_tree` |
| `server` | Home-Assistant-Event-Bus-Event wie `state_changed`, `component_loaded` oder `call_service` | Aktive Frontend-Verbindung | Nur `select_tree` |

Alle Realms unterstützen [Regeln](./rules) und [Direktiven](./directives). Der gewählte [Interaction Anchor](./interaction-anchors) befindet sich immer im aktuellen Browser. Auch ein Event aus dem `server`-Realm kann daher ein Browser-Element aktualisieren oder ein Event darauf auslösen.

## Browser

`browser` lauscht auf `window` während der Capture-Phase. Nutze ihn für DOM-Events wie `click`, `change`, `show-dialog` und benutzerdefinierte Home-Assistant-Browser-Events.

```yaml
- realm: browser
  listen: show-dialog
  anchor: '&home-assistant $ hui-dialog-create-card'
  debug: true
  rules:
    - '@captured.dialogTag': hui-dialog-create-card
  directives:
    - type: property
      set: _currTab
      value: card
```

Das `detail`-Objekt des Browser-Events ist die Wurzel der Captured Data. Siehe [Captured-Data-Regeln](./rules#captured-data-regeln) und [Event-Direktive](./directives#event).

## Shortcut

`shortcut` nutzt [Tinykeys](https://jamiebuilds.github.io/tinykeys/) und registriert ein Tastenkürzel auf `window`. `$mod` bedeutet `Meta` auf macOS und `Control` unter Windows und Linux.

```yaml
- realm: shortcut
  listen: "$mod+Shift+Y"
  anchor: target
  directives:
    - type: call
      method: focus
```

Tastenkürzel können Tasten, Codes, Modifikatoren und Sequenzen nutzen. Home Assistant nutzt ebenfalls Tinykeys. Verwende daher Kombinationen, die nicht mit Home Assistant, dem Browser oder dem Betriebssystem kollidieren. Home-Assistant-Tastenkürzel können für den Browser deaktiviert werden; UIX Broker kann seine Tastenkürzel dann weiterhin registrieren.

Das auslösende `KeyboardEvent` steht JavaScript-Actions als `event` zur Verfügung. Sein composed path kann auch von [Interaction Anchors](./interaction-anchors) genutzt werden.

## Server

`server` abonniert den Home-Assistant-Event-Bus über die aktive Frontend-Verbindung. Es gibt kein Browser-Event-Ziel, daher muss der Interaction Anchor `select_tree` nutzen.

```yaml
- realm: server
  listen: state_changed
  anchor: "&home-assistant $$ dynamic-custom-card"
  rules:
    - type: captured
      path: data.entity_id
      match: light.kitchen
  directives:
    - type: property
      set: customCardProperty
      value: "@captured.data.entity_id"
```

Bei Server-Interaktionen enthält Captured Data unter `data` die Home-Assistant-Eventdaten, zum Beispiel `data.entity_id` oder `data.new_state.state`. In Regeln und Direktiven kann mit `"@captured.data..."` darauf verwiesen werden. Die Anführungszeichen sind in YAML wegen `@` erforderlich.

## Blocking

Die Direktive `block` ist in den Realms `browser` und `shortcut` verfügbar. Anchor und Host-Element-Regeln werden synchron aufgelöst. Wenn ein `select_tree`-Anchor nicht sofort gefunden wird, wird die ganze Interaktion übersprungen. Server-Events können nicht blockiert werden.

::: info
Tinykeys ignoriert Tastendrücke in `input`, `textarea`, `select` und `contenteditable`. Ein `shortcut`-Realm mit `block` läuft dort daher nicht. Um Tasten in solchen Bereichen zu blockieren, nutze den `browser`-Realm mit `listen: keydown`.
:::

## Templates

UIX Broker stellt bewusst keinen Realm bereit, der direkt Jinja2-Templates abonniert. Nutze stattdessen ein Script, eine Automation oder eine Template-Entität mit Trigger, löse ein eigenes Home-Assistant-Event aus und lausche im `server`-Realm darauf.

::: tip
Die Integration `custom_event` kann eigene Events auf dem Home-Assistant-Event-Bus auslösen, auf die UIX Broker im `server`-Realm reagieren kann.
:::
