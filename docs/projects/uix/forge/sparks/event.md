---
title: Event Spark
---
# Event Spark

Der Event Spark verbindet Forge-Elemente über `fire-dom-event`. Daten aus passenden Events werden in `uixForge.event` abgelegt und können danach in Templates verwendet werden.

## Konfiguration

| Schlüssel | Typ | Pflicht | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `type` | `string` | ja | - | Muss `event` sein. |
| `forge_id` | `string` | nein | - | ID dieses Forge-Elements. Daten aus `fire-dom-event`-Events mit gleicher `forge_id` werden direkt nach `uixForge.event` übernommen. |
| `other_forge_ids` | Liste von Strings | nein | - | IDs anderer Forge-Elemente, auf deren Events gehört werden soll. Daten sind unter `uixForge.event.<id>` verfügbar. |

## Template-Variablen

| Variable | Beschreibung |
| --- | --- |
| `uixForge.event.<key>` | Daten aus Events mit passender eigener `forge_id`, direkt unter `uixForge.event`. |
| `uixForge.event.<other_id>.<key>` | Daten eines anderen Forge-Elements aus `other_forge_ids`, verschachtelt unter dessen ID. |

## Event auslösen

Ein Event wird typischerweise über eine Home-Assistant-Aktion `fire-dom-event` ausgelöst. Die Payload muss eine `forge_id` enthalten, damit der Event Spark sie zuordnen kann.

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

Empfänger:

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: event
      forge_id: room_picker
element:
  type: tile
  entity: "light.{{ uixForge.event.room | default('living_room') }}"
```

### Auf Events eines anderen Forge-Elements hören

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
  entity: "light.{{ uixForge.event.room_picker.room | default('living_room') }}"
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
  entity: "light.{{ uixForge.event.room_picker.room | default('living_room') }}"
```

### Daten an mehrere Forge-Elemente senden

Wenn mehrere Forge-Elemente dieselbe `forge_id` beobachten, erhalten sie dieselbe Event-Payload. Das ist nützlich für gemeinsame Filter, Auswahlkarten oder Shortcut-Badges.

```yaml
tap_action:
  action: fire-dom-event
  uix_forge:
    forge_id: shared_filter
    value: climate
```

### Shortcut-Badge für Expander-Zustände

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

::: note
Der Event Spark ist für lokale UI-Kommunikation gedacht. Er ersetzt keine Home-Assistant-Entität und speichert keine Werte dauerhaft.

:::
## Payload-Struktur

Die Event-Payload sollte klein bleiben und nur Werte enthalten, die das empfangende Forge-Element wirklich für Templates braucht.

```yaml
tap_action:
  action: fire-dom-event
  uix_forge:
    forge_id: room_picker
    room: kitchen
    label: Kueche
    icon: mdi:silverware-fork-knife
```

Im Empfänger:

```yaml
element:
  type: tile
  entity: "light.{{ uixForge.event.room | default('living_room') }}"
  name: "{{ uixForge.event.label | default('Wohnzimmer') }}"
```

## Defaults in Templates

Da Events erst nach einer Nutzeraktion eintreffen, sollten Templates immer Default-Werte haben.

```yaml
entity: "light.{{ uixForge.event.room | default('living_room') }}"
icon: "{{ uixForge.event.icon | default('mdi:lightbulb') }}"
```

Ohne Default kann eine Karte beim ersten Rendern leer oder fehlerhaft sein.

## Mehrere Empfänger

Mehrere Forge-Elemente können dieselbe `forge_id` verwenden. Dadurch lassen sich ein Detailbereich, ein Badge und ein Button gleichzeitig aktualisieren.

```yaml
forge:
  mold: card
  sparks:
    - type: event
      forge_id: shared_room
```

```yaml
forge:
  mold: badge
  sparks:
    - type: event
      forge_id: shared_room
```

## Eigene ID und fremde IDs

`forge_id` ist für Events gedacht, die dieses Element direkt betreffen. `other_forge_ids` ist für externe Steuerquellen gedacht.

```yaml
forge:
  sparks:
    - type: event
      forge_id: detail_panel
      other_forge_ids:
        - room_picker
        - floor_picker
```

Dann kannst du beides getrennt auslesen:

```yaml
name: "{{ uixForge.event.title | default('Details') }}"
entity: "light.{{ uixForge.event.room_picker.room | default('living_room') }}"
```

## Einsatzgrenzen

| Fall | Empfehlung |
| --- | --- |
| Wert soll Neustarts überleben | Home-Assistant-Helper nutzen |
| Wert gilt nur für aktuelle UI-Auswahl | Event Spark verwenden |
| Mehrere Dashboards sollen synchron bleiben | Entity, Helper oder Automatisierung verwenden |
| Nur eine Karte soll reagieren | `forge_id` eindeutig halten |

## Event-Daten anzeigen

Zum Debuggen kann ein Markdown-Element die empfangenen Daten anzeigen.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: event
      forge_id: debug_event
element:
  type: markdown
  content: |
    ```json
    {{ uixForge.event | tojson }}
    ```
```

## Namenskonventionen

Halte `forge_id` eindeutig und sprechend.

| Muster | Beispiel |
| --- | --- |
| Raum-Auswahl | `room_picker` |
| Detailkarte | `detail_card` |
| Filter | `entity_filter` |
| Gemeinsame Auswahl | `shared_selection` |

Vermeide sehr generische IDs wie `main` oder `test`, sobald mehrere Forge-Elemente auf einer Seite liegen.

## Zusammenspiel mit Templates

Events werden erst nach dem ersten Rendern verfügbar. Deshalb sind Default-Filter wichtig.

```yaml
name: "{{ uixForge.event.name | default('Keine Auswahl') }}"
```

Für verschachtelte Daten:

```yaml
name: "{{ uixForge.event.room_picker.name | default('Wohnzimmer') }}"
```

## Fehlersuche

| Problem | Prüfung |
| --- | --- |
| Empfänger reagiert nicht | Stimmen Eventname und `forge_id`? |
| Template ist beim Laden leer | Default-Wert ergänzen |
| Falsches Element reagiert | IDs eindeutiger machen |
| Daten liegen unter anderem Pfad | `other_forge_ids` oder eigene `forge_id` prüfen |
