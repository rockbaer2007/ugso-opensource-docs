---
title: Theme Spark
---
# Theme Spark

Der Theme Spark wendet ein Home-Assistant-Frontend-Theme auf das Forge-Element oder auf ein bestimmtes Unterelement an. Das ist nuetzlich, wenn nur ein Teil einer Karte anders aussehen soll.

## Konfiguration

| Schluessel | Typ | Pflicht | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `type` | string | ja | - | Muss `theme` sein. |
| `for` | string | nein | `element`, bei Blank Card `uix-forge-blank-card $ div.content` | UIX-Selektor fuer das Element, auf das das Theme angewendet wird. |
| `theme` | string | nein | - | Name des anzuwendenden Themes. Unterstuetzt Templates. |

!!! tip
    Der Theme Spark setzt ein Home-Assistant-Theme auf ein konkretes Element. Fuer globale UIX-Theme-Styles nutze die normale [Theme-Konfiguration](../../using/themes).

## Beispiel - einfach

Theme:

```yaml
Wohnzimmer Rot:
  primary-color: "#d32f2f"
  card-background-color: "#2b1717"
```

Forge:

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: theme
      theme: Wohnzimmer Rot
element:
  type: tile
  entity: light.living_room
```

## Beispiel - Template

Theme-Auswahl nach Zustand:

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: theme
      theme: "&#123;&#123; 'Alarm Theme' if is_state('binary_sensor.window', 'on') else 'Normal Theme' &#125;&#125;"
element:
  type: tile
  entity: binary_sensor.window
```

Nur ein Unterelement themen:

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: theme
      for: hui-tile-card $ ha-tile-icon
      theme: Icon Theme
element:
  type: tile
  entity: light.living_room
```

!!! tip
    Wenn sich das Theme nicht sichtbar aendert, pruefe, ob das Ziel wirklich im DOM vorhanden ist und ob die verwendeten Theme-Variablen von diesem Home-Assistant-Element gelesen werden.
