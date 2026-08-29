---
title: Event Spark
---
# Event Spark

Der Event Spark verbindet Forge-Elemente ueber `fire-dom-event`. Daten aus passenden Events werden in `uixForge.event` abgelegt und koennen danach in Templates verwendet werden.

## Konfiguration

| Schluessel | Typ | Pflicht | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `type` | `string` | ja | - | Muss `event` sein. |
| `forge_id` | `string` | nein | - | ID dieses Forge-Elements. Daten aus `fire-dom-event`-Events mit gleicher `forge_id` werden direkt nach `uixForge.event` uebernommen. |
| `other_forge_ids` | Liste von Strings | nein | - | IDs anderer Forge-Elemente, auf deren Events gehoert werden soll. Daten sind unter `uixForge.event.<id>` verfuegbar. |

## Template-Variablen

| Variable | Beschreibung |
| --- | --- |
| `uixForge.event.<key>` | Daten aus Events mit passender eigener `forge_id`, direkt unter `uixForge.event`. |
| `uixForge.event.<other_id>.<key>` | Daten eines anderen Forge-Elements aus `other_forge_ids`, verschachtelt unter dessen ID. |

## Event ausloesen

Ein Event wird typischerweise ueber eine Home-Assistant-Aktion `fire-dom-event` ausgeloest. Die Payload muss eine `forge_id` enthalten, damit der Event Spark sie zuordnen kann.

```yaml
tap_action:
  action: fire-dom-event
  browser_mod:
    service: browser_mod.sequence
    data:
      sequence:
        - service: browser_mod.javascript
          data:
            code: |
              this.dispatchEvent(new CustomEvent("uix-forge-event", {
                bubbles: true,
                composed: true,
                detail: {
                  forge_id: "demo",
                  selected: "light.living_room"
                }
              }));
```

## Nutzung

### Button aktualisiert eine Karte

Sender:

```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: button
  name: Wohnzimmer
  tap_action:
    action: fire-dom-event
    uix_forge:
      forge_id: room_picker
      room: living_room
```

Empfaenger:

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: event
      forge_id: room_picker
element:
  type: tile
  entity: "light.&#123;&#123; uixForge.event.room | default('living_room') &#125;&#125;"
```

### Auf Events eines anderen Forge-Elements hoeren

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: event
      other_forge_ids:
        - room_picker
element:
  type: tile
  entity: "light.&#123;&#123; uixForge.event.room_picker.room | default('living_room') &#125;&#125;"
```

### Eigene und fremde IDs kombinieren

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: event
      forge_id: detail_card
      other_forge_ids:
        - room_picker
        - mode_picker
element:
  type: tile
  entity: "light.&#123;&#123; uixForge.event.room_picker.room | default('living_room') &#125;&#125;"
```

### Daten an mehrere Forge-Elemente senden

Wenn mehrere Forge-Elemente dieselbe `forge_id` beobachten, erhalten sie dieselbe Event-Payload. Das ist nuetzlich fuer gemeinsame Filter, Auswahlkarten oder Shortcut-Badges.

```yaml
tap_action:
  action: fire-dom-event
  uix_forge:
    forge_id: shared_filter
    value: climate
```

### Shortcut-Badge fuer Expander-Zustaende

```yaml
type: custom:uix-forge
forge:
  mold: badge
  sparks:
    - type: event
      forge_id: expander_shortcut
element:
  type: entity
  entity: input_boolean.show_energy
```

!!! note
    Der Event Spark ist fuer lokale UI-Kommunikation gedacht. Er ersetzt keine Home-Assistant-Entitaet und speichert keine Werte dauerhaft.
