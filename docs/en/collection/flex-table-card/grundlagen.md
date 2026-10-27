---
title: flex-table-card basics
description: Basic principle of the flex-table-card with rows, columns and selectors.
---
<a id="flex-table-card-basics"></a>
<a id="current-focus"></a>

# Basics {#grundlagen}

The configuration essentially consists of two steps:

1. `entities` selects the possible rows.
2. `columns` describes which values are displayed as columns per row.

## Minimal example {#minimales-beispiel}

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

## Include and exclude {#include-und-exclude}

`include` and `exclude` can be individual expressions or lists.

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

An entity is included if at least one `include` matches. It is excluded as soon as a `exclude` matches.

## Sorting and limiting {#sortierung-und-begrenzung}

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

`sort_by` uses the column ID. `+` sorts in ascending order, `-` sorts in descending order.
