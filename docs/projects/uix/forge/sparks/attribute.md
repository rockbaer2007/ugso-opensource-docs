---
title: Attribute Spark
---
# Attribute Spark

Der Attribute Spark setzt, ersetzt oder entfernt ein HTML-Attribut an einem Element innerhalb eines Forge-Elements. Das ist praktisch für native Tooltips, ARIA-Attribute, Titel oder kleine Datenattribute.

## Konfiguration

| Schlüssel | Typ | Pflicht | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `type` | `string` | ja | - | Muss `attribute` sein. |
| `attribute` | `string` | ja | - | Name des HTML-Attributs, z. B. `title`. |
| `for` | `string` | nein | `element`, bei Blank Card `uix-forge-blank-card $ div.content` | CSS/UIX-Selektor für das Ziel. `$` wechselt in Shadow Roots. |
| `action` | `string` | nein | `replace` | `replace` setzt einen neuen Wert, `remove` entfernt das Attribut komplett. |
| `value` | `string` | nein | `""` | Neuer Attributwert. Wird nur bei `action: replace` genutzt und unterstuetzt Jinja2-Templates. |

::: tip
Wenn du nur einen Tooltip anzeigen willst, ist oft der [Tooltip Spark](./tooltip) besser. Der Attribute Spark ist sinnvoll, wenn wirklich das HTML-Attribut selbst geändert werden soll.

:::
## Nutzung

### Native Tooltip entfernen

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: attribute
      for: hui-tile-card $ ha-tile-icon
      attribute: title
      action: remove
element:
  type: tile
  entity: light.living_room
```

### `title` ersetzen

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: attribute
      for: hui-tile-card $ ha-tile-icon
      attribute: title
      value: Wohnzimmer-Licht
element:
  type: tile
  entity: light.living_room
```

### Template als Wert nutzen

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: attribute
      for: hui-tile-card
      attribute: data-state
      value: "&#123;&#123; states(config.element.entity) &#125;&#125;"
element:
  type: tile
  entity: light.living_room
```

::: note
Der Spark wirkt auf das erste Element, das vom Selektor gefunden wird. Bei mehreren gleichen Elementen musst du den Pfad genauer machen.
:::
