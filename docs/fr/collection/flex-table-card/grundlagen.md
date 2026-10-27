---
title: Bases de `flex-table-card`
description: 'Principe fondamental de `flex-table-card` : lignes, colonnes et sélecteurs.'
---
<a id="flex-table-card-bases"></a>
<a id="orientation-actuelle"></a>

# Bases {#grundlagen}

La configuration repose essentiellement sur deux étapes :

1. `entities` sélectionne les lignes disponibles. 2. `columns` définit quelles valeurs, parmi celles présentes sur chaque ligne, doivent être affichées sous forme de colonnes.

## Exemple minimal {#minimales-beispiel}

```yaml
type: custom:flex-table-card
title: Z-Wave Uebersicht
entities:
  include: zwave.*
  exclude: zwave.unknown_node*
columns:
  - name: Node
    data: node_id
  - name: Name
    data: name
  - name: Status
    data: state
```

## Inclusion et exclusion {#include-und-exclude}

`include` et `exclude` peuvent être des expressions uniques ou des listes.

```yaml
type: custom:flex-table-card
title: Mehrere Filter
entities:
  include:
    - sensor.*
    - binary_sensor.tuer_*
  exclude:
    - sensor.unbenutzt
    - sensor.test_*
columns:
  - name: Name
    data: name
  - name: Wert
    data: state
```

Une entité est incluse si au moins un élément de `include` correspond. Elle est exclue dès qu'un élément de `exclude` correspond.

## Tri et limitation {#sortierung-und-begrenzung}

```yaml
type: custom:flex-table-card
title: Batterie niedrig
entities:
  include: sensor.*_battery*
sort_by: battery+
max_rows: 20
columns:
  - name: Name
    data: name
  - name: Batterie
    id: battery
    data: state
    fmt: number
    suffix: "%"
    align: right
```

`sort_by` utilise l'identifiant de la colonne. `+` permet un tri par ordre croissant, tandis que `-` permet un tri par ordre décroissant.
