---
title: Interaction Anchors
description: Das Element auswählen, das UIX Broker standardmäßig für Regeln und Direktiven nutzt.
---
# Interaction Anchors

::: info Verfügbar ab UIX 8.2.0-beta.2
UIX Broker gehört zum aktuellen Entwicklungszweig.
:::

Ein Interaction Anchor wählt das Element aus, das Host-Element-Regeln prüfen und Direktiven standardmäßig verwenden. Browser- und Shortcut-Interaktionen können aus dem composed path des auslösenden Events wählen oder einen UIX-`select_tree`-Pfad nutzen. Server-Interaktionen verwenden ausschließlich `select_tree`.

Für kompaktes YAML wird `anchor` meist in Kurzform geschrieben.

| `anchor:` | Methode |
| --- | --- |
| `target` | Nutzt Event-Pfad-Auswahl und verweist auf das Ziel eines `browser`- oder `shortcut`-Events. Im `server`-Realm nicht verfügbar. |
| `<`, `<$`, `<selector> <$`, `<selector> <$$` | Nutzt Event-Pfad-Auswahl. Im `server`-Realm nicht verfügbar. |
| String mit `&` am Anfang | Nutzt `select_tree` ab `document`. In allen Realms verfügbar. |
| `{ select_tree: <path> }` | Lange `select_tree`-Form ab `document`. In allen Realms verfügbar. |

## Event-Pfad-Anchors

Event-Pfad-Ausdrücke werden von rechts nach links ausgehend von `target` ausgewertet. `target` ist das innerste Element aus [`event.composedPath()`](https://developer.mozilla.org/en-US/docs/Web/API/Event/composedPath).

| Anchor | Ergebnis |
| --- | --- |
| `target` | Ursprüngliches innerstes Event-Ziel. In anderen Formen ist `target` optional. |
| `< [target]` | Das Elternelement von `target`. |
| `<$ [target]` | Der erste Shadow-Root-Host oberhalb von `target`. |
| `<selector> <$ [target]` | Das erste passende Element im Light DOM dieses ersten Shadow Hosts. |
| `<selector> <$$ [target]` | Das erste passende Element beim Weg nach außen durch den composed path inklusive Shadow-Root-Grenzen. |

::: info
Event-Pfad-Anchors werden synchron aufgelöst und können mit der Direktive [`block`](./directives#block) verwendet werden.
:::

```yaml
# Nächster Shadow Host des Event-Ziels
anchor: "<$"

# Passendes ha-automation-row-Element im Light DOM des Ziel-Hosts
anchor: "ha-automation-row <$"

# Erstes passendes ha-automation-row-Element nach außen über Shadow-Root-Grenzen
anchor: "ha-automation-row <$$"
```

`<` und `<$` können `target` rechts ausdrücklich enthalten, aber kompakter ist die Kurzform ohne `target`. `<$$` benötigt einen Selektor.

## Select-tree-Anchors

Nutze einen normalen UIX-`select_tree`-Pfad, wenn ein Anchor nicht aus dem Event-Pfad bestimmt wird. Das gilt immer für Server-Interaktionen.

```yaml
# Kompakte absolute Form
anchor: "&home-assistant $ hui-dialog-create-card"

# Lange Form, immer absolut ab document
anchor:
  select_tree: "home-assistant $ home-assistant-main $ ha-panel-lovelace $ hui-root"
```

Bei Interaktionen ohne `block` versucht UIX Broker einen fehlenden `select_tree`-Anchor alle 50 ms bis zu zwei Sekunden lang erneut zu finden. Das ist nützlich für Oberflächen wie Dialoge, die erst nach dem auslösenden Event montiert werden.

## Anchors in Regeln und Direktiven

Regeln und Direktiven verwenden standardmäßig den Interaction Anchor. Sie können aber eigene `anchor`-Konfigurationen setzen: kompakt relativ, kompakt absolut mit `&` oder als lange `select_tree`-Form.

```yaml
- type: property
  anchor: "$ ha-dialog div.body hui-card-picker $ div#content>ha-expansion-panel:nth-of-type(1)"
  set: expanded
  value: false
```

```yaml
- type: call
  anchor: "&home-assistant $ ha-more-info-dialog"
  method: closeDialog
```

```yaml
- type: call
  anchor:
    select_tree: "home-assistant $ ha-more-info-dialog"
  method: closeDialog
```

## Pfade in der Browser-Konsole finden

Um einen absoluten Anchor-Pfad zu finden, wähle ein Element im Browser-Inspector aus und führe aus:

```javascript
uix_broker_absolute_path($0)
```

Für einen Direktiven- oder Regel-Anchor relativ zu einem zuvor aufgelösten Interaction Anchor nutze:

```javascript
uix_broker_path($0)
```

Wenn mehrere Interaktionen überlappen, kann der Anchor explizit als zweites Argument angegeben werden:

```javascript
uix_broker_path($0, $1)
```
