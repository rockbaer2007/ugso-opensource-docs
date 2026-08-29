---
title: Foundries
description: Wiederverwendbare UIX-Forge-Konfigurationen mit Global Foundries, YAML-Dateien und Billets
---
# Foundries

Foundries sind wiederverwendbare Forge-Vorlagen. Eine Foundry beschreibt ein Muster aus `forge`, `element`, `uix`, Makros und Billets. Einzelne Forge-Instanzen koennen diese Vorlage verwenden und gezielt Werte ueberschreiben.

## Global Foundries

Global Foundries stehen dashboardweit zur Verfuegung. Sie eignen sich fuer wiederkehrende Kacheln, Standardstile, Lock-Muster, Badge-Layouts oder Kombinationen aus Sparks.

## Foundries verwalten

### UI Foundries

UI Foundries werden in der Home-Assistant-Oberflaeche gepflegt. Sie sind bequem fuer kleinere Vorlagen und schnelle Anpassungen.

### YAML File Foundries

YAML File Foundries liegen in Dateien und sind besser fuer groessere oder versionierte Konfigurationen geeignet.

#### Dateiformat

```yaml
foundries:
  living_room_tile:
    forge:
      mold: card
    element:
      type: tile
      entity: "&#123;&#123; entity &#125;&#125;"
    billets:
      entity: light.living_room
```

#### YAML-Anker

YAML-Anker koennen gemeinsame Teile wiederverwenden.

```yaml
defaults: &tile_defaults
  forge:
    mold: card
  element:
    type: tile

foundries:
  light_tile:
    <<: *tile_defaults
    billets:
      entity: light.living_room
```

::: warning YAML-Merge-Keys sind flach
YAML-Merge-Keys mergen nur die aktuelle Ebene. Verschachtelte Maps werden nicht tief zusammengefuehrt. Fuer tiefe Kombinationen nutze lieber Foundry-Merge-Verhalten.

:::
#### Datei registrieren

Eine YAML-Datei muss in UIX registriert werden, damit ihre Foundries geladen werden. Der genaue Ort haengt von deiner Home-Assistant-Konfiguration ab, typisch ist ein Pfad unter `/config/uix/`.

#### Dateien neu laden

Nach Aenderungen an YAML-Dateien muessen die Foundries neu geladen werden. Danach greifen neue Forge-Instanzen auf die aktualisierte Vorlage zu.

#### Registrierung entfernen

Nicht mehr benoetigte Dateien koennen aus der Foundry-Registrierung entfernt werden. Bereits konfigurierte Dashboards sollten danach keine Foundries aus dieser Datei mehr referenzieren.

#### Vorrang

Wenn Foundries denselben Namen verwenden, entscheidet die UIX-Ladereihenfolge. Halte Namen eindeutig, damit keine unbeabsichtigte Vorlage eine andere ueberschreibt.

## Foundry verwenden

```yaml
type: custom:uix-forge
forge:
  foundry: living_room_tile
```

Mit Ueberschreibung:

```yaml
type: custom:uix-forge
forge:
  foundry: living_room_tile
  billets:
    entity: light.kitchen
```

## Struktur einer Foundry-Konfiguration

```yaml
foundries:
  my_foundry:
    forge:
      mold: card
      sparks: []
    element:
      type: tile
      entity: "&#123;&#123; entity &#125;&#125;"
    uix:
      style: |
        ha-card {
          border: 1px solid var(--primary-color);
        }
    macros: {}
    billets:
      entity: light.living_room
```

## Externe Dateien und Secrets einbinden

::: warning Quotes in UI Foundries erforderlich
In UI Foundries muessen `!include` und `!secret` als String gequotet werden. In YAML File Foundries koennen sie als YAML-Tags geschrieben werden.

:::
### `!include`

```yaml
# /config/uix/my_forge_styles.yaml
style: |
  ha-card {
    border-radius: 12px;
  }
```

```yaml
# In einer YAML File Foundry - keine Quotes noetig
uix: !include /config/uix/my_forge_styles.yaml
```

```yaml
# In einer UI Foundry - Quotes erforderlich
uix: "!include /config/uix/my_forge_styles.yaml"
```

### `!secret`

```yaml
# /config/secrets.yaml
my_pin: 1234
```

```yaml
# In einer YAML File Foundry - keine Quotes noetig
pin: !secret my_pin
```

```yaml
# In einer UI Foundry - Quotes erforderlich
pin: "!secret my_pin"
```

## Merge-Verhalten

Foundry-Konfigurationen werden mit der Instanzkonfiguration zusammengefuehrt. Dadurch kannst du Defaults in der Foundry definieren und nur die abweichenden Werte im Dashboard setzen.

### Merge-Beispiel

Foundry:

```yaml
foundries:
  base_tile:
    forge:
      mold: card
      sparks:
        - type: tooltip
          content: "&#123;&#123; tooltip &#125;&#125;"
    element:
      type: tile
      entity: "&#123;&#123; entity &#125;&#125;"
    billets:
      tooltip: Details anzeigen
```

Instanz:

```yaml
type: custom:uix-forge
forge:
  foundry: base_tile
  billets:
    entity: light.kitchen
    tooltip: Kuechenlicht
```

Ergebnisgedanke:

```yaml
forge:
  mold: card
  sparks:
    - type: tooltip
      content: Kuechenlicht
element:
  type: tile
  entity: light.kitchen
```

## Verschachtelte Foundries

Foundries koennen auf anderen Foundries aufbauen.

```yaml
foundries:
  base_tile:
    forge:
      mold: card
    element:
      type: tile
```

```yaml
foundries:
  locked_tile:
    forge:
      foundry: base_tile
      sparks:
        - type: lock
          locks:
            - pin: 1234
```

```yaml
type: custom:uix-forge
forge:
  foundry: locked_tile
element:
  entity: light.living_room
```

::: warning Zirkulaere Referenzen
Foundries duerfen sich nicht gegenseitig endlos referenzieren. Achte darauf, dass die Kette eindeutig endet.

:::
## Billets in Foundries

Billets sind der wichtigste Weg, um Foundries flexibel zu halten.

### Muster 1: Defaults in der Foundry definieren, pro Instanz ueberschreiben

```yaml
foundries:
  room_tile:
    billets:
      entity: light.living_room
      name: Wohnzimmer
    element:
      type: tile
      entity: "&#123;&#123; entity &#125;&#125;"
      name: "&#123;&#123; name &#125;&#125;"
```

```yaml
type: custom:uix-forge
forge:
  foundry: room_tile
  billets:
    entity: light.kitchen
    name: Kueche
```

```yaml
element:
  type: tile
  entity: light.kitchen
  name: Kueche
```

### Muster 2: Leere Billet-Slots in der Foundry definieren

```yaml
foundries:
  required_entity_tile:
    billets:
      entity: ~
    element:
      type: tile
      entity: "&#123;&#123; entity &#125;&#125;"
```

```yaml
type: custom:uix-forge
forge:
  foundry: required_entity_tile
  billets:
    entity: sensor.outdoor_temperature
```

```yaml
element:
  type: tile
  entity: sensor.outdoor_temperature
```

::: note UI Foundries: Kommentare werden entfernt
In UI Foundries bleiben YAML-Kommentare nicht erhalten. Wenn Kommentare wichtig sind, nutze eine YAML-Datei im Repository.

:::
## UIX-Styling aus einer Foundry

Foundries koennen eigene `uix`-Styles enthalten. Die Instanz kann diese Styles ergaenzen.

::: tip Styles kombinieren
Lege gemeinsame Struktur und Theme-Variablen in die Foundry und instanzspezifische Abweichungen direkt in die Forge-Instanz.

:::
```yaml
# Foundry: "styled_tile"
foundries:
  styled_tile:
    forge:
      mold: card
    element:
      type: tile
      entity: "&#123;&#123; entity &#125;&#125;"
    uix:
      style: |
        ha-card {
          border: 1px solid var(--primary-color);
        }
```

```yaml
# Forge - fuegt eigenes UIX-Styling hinzu
type: custom:uix-forge
forge:
  foundry: styled_tile
  billets:
    entity: light.living_room
uix:
  style: |
    ha-card {
      box-shadow: var(--ha-card-box-shadow);
    }
```

## Beispiel: Global Foundry mit Makro

::: tip
Makros in Foundries halten wiederkehrende Template-Logik an einer Stelle.

:::
```yaml
foundries:
  state_colored_tile:
    macros:
      active_color: |
        &#123;% macro active_color(entity) -%&#125;
        &#123;&#123; 'var(--success-color)' if is_state(entity, 'on') else 'var(--disabled-color)' &#125;&#125;
        &#123;%- endmacro %&#125;
    billets:
      entity: light.living_room
    forge:
      mold: card
    element:
      type: tile
      entity: "&#123;&#123; entity &#125;&#125;"
    uix:
      style: |
        ha-card {
          border-color: &#123;&#123; active_color(entity) &#125;&#125;;
        }
```

```yaml
type: custom:uix-forge
forge:
  foundry: state_colored_tile
  billets:
    entity: light.kitchen
```
