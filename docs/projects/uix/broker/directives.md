---
title: Directives
description: Deklarative UIX-Broker-Operationen auf ein ausgewähltes Element anwenden.
---
# Directives

::: info Verfügbar ab UIX 8.2.0-beta.2
UIX Broker gehört zum aktuellen Entwicklungszweig.
:::

Direktiven laufen nacheinander, nachdem alle Regeln einer Interaktion passen. Jede Direktive führt eine konfigurierte Operation aus und nutzt standardmäßig den Interaction Anchor oder, falls unterstützt, einen ausdrücklich gesetzten Direktiven-Anchor.

- [Block](#block): Standardaktion und Propagation des auslösenden Browser-Events verhindern.
- [Property](#property): JavaScript-Objekt-Property setzen oder entfernen.
- [Event](#event): Ein `CustomEvent` auslösen.
- [Call](#call): Eine Element-Methode aufrufen.
- [Action](#action): Home-Assistant-, Frontend- oder UIX-Action ausführen.
- [Wait](#wait): Die nächste Direktive verzögern.

## Block

`block` ruft `preventDefault()` und `stopImmediatePropagation()` auf dem auslösenden Browser-Event auf.

```yaml
- type: block
```

`block` ist nur in den Realms `browser` und `shortcut` verfügbar. Interaction Anchor und Host-Element-Regel-Anchors müssen synchron auflösbar sein. Ist ein benötigter `select_tree`-Anchor nicht sofort vorhanden, überspringt UIX Broker die komplette Interaktion. Eine `block`-Direktive wird vor den übrigen Direktiven angewendet, auch wenn sie später in der Liste steht.

## Direktiven-Anchors

`property`, `event` und `call` nutzen standardmäßig den Interaction Anchor. Jede dieser Direktiven kann den Standard mit eigener `anchor`-Konfiguration überschreiben. Ein einfacher String ist relativ zum Interaction Anchor, ein String mit `&` am Anfang ist ein kompakter absoluter `select_tree`-Pfad ab `document`, und `{ select_tree: ... }` ist die entsprechende lange absolute Form.

```yaml
directives:
  - type: property
    anchor: "$ ha-dialog"
    set: withoutHeader
    value: true
  - type: event
    anchor: "&home-assistant $$ ha-automation-sidebar"
    name: broker-sidebar-event
  - type: call
    anchor:
      select_tree: "home-assistant $ ha-more-info-dialog"
    method: closeDialog
```

Nutze den Konsolenhelfer `uix_broker_path($0)`, um im Browser einen relativen Direktiven-Anchor-Pfad zu finden.

## Property

Die `property`-Direktive verändert das JavaScript-Objekt des gewählten Anchors. `set` nimmt einen dot-separierten Property-Pfad, erzeugt fehlende Zwischenebenen als einfache Objekte und weist den Wert der letzten Property zu. `clear` nimmt denselben Pfadtyp und löscht nur die letzte Property.

```yaml
- type: property
  set: config.heading
  value: New title
- type: property
  clear: config.icon
```

Werte können Captured Data referenzieren. `@captured` steht für das komplette Captured-Data-Objekt, `@captured.path` für einen Wert an diesem dot-separierten Pfad. Da der Wert mit `@` beginnt, muss er in YAML in Anführungszeichen stehen.

```yaml
- type: property
  set: config.entity
  value: "@captured.entity_id"
```

## Event

`event` löst ein `CustomEvent` auf dem gewählten Anchor aus. `bubbles` und `composed` sind standardmäßig `false`, passend zur DOM-API.

```yaml
- type: event
  name: broker-demo-event
  bubbles: true
  composed: true
  data:
    entity: light.bed_light
```

Mit `capture_data: true` werden Captured Data in das neue Event übernommen. Das ausgehende `detail` beginnt mit den Captured Data der auslösenden Interaktion und überschreibt sie anschließend mit Werten aus `data`. `capture_data` ist nur für die `event`-Direktive verfügbar.

```yaml
- type: event
  name: broker-forwarded-event
  capture_data: true
  data:
    source: uixBroker
```

## Call

`call` ruft eine Methode auf dem gewählten Anchor auf. `method` akzeptiert einen sicheren dot-separierten Methodenpfad und erhält das `this`-Binding des Methodenobjekts. `args` muss, falls vorhanden, ein Array sein und unterstützt Captured-Data-Ersetzung.

```yaml
- type: call
  method: focus
- type: call
  method: setSelectionRange
  args: [0, 5]
```

## Action

`action` führt einen Home-Assistant-Service-Call, eine Standard-Frontend-Action oder eine UIX-Broker-spezifische Action aus.

```yaml
- type: action
  action: light.turn_on
  target:
    entity_id: light.example

- type: action
  action: fire-dom-event
  uix:
    action: toast
    data:
      message: Done
```

### JavaScript-Action

`action: javascript` ist eine UIX-Broker-Action. Der Code steht in `data.code`. UIX Broker übergibt automatisch `hass`, `anchor`, `event` und `captured` als Variablen. `hass` ist das aktive Home-Assistant-Objekt, `anchor` der aufgelöste Interaction-Anchor, `event` das auslösende Event und `captured` die Captured Data.

```yaml
- type: action
  action: javascript
  data:
    code: |
      console.log(anchor, event, captured)
```

Nutze JavaScript nur aus vertrauenswürdigen UIX-Konfigurationen.

## Wait

Jede Direktive akzeptiert `wait`, eine nicht negative Zahl in Millisekunden. UIX Broker wartet nach der Direktive so lange, bevor die nächste Direktive startet. Eine `block`-Direktive läuft immer synchron, kann aber `wait` enthalten, um spätere Direktiven zu verzögern.

```yaml
directives:
  - type: event
    name: broker-started-event
    wait: 250
  - type: action
    action: light.turn_on
```
