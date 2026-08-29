---
title: flex-table-card Grundlagen
description: Grundprinzip der flex-table-card mit Zeilen, Spalten und Selektoren.
---
# Grundlagen

Die Konfiguration besteht im Kern aus zwei Schritten:

1. `entities` wählt die möglichen Zeilen aus.
2. `columns` beschreibt, welche Werte pro Zeile als Spalten angezeigt werden.

## Minimales Beispiel

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

## Include und Exclude

`include` und `exclude` können einzelne Ausdrücke oder Listen sein.

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

Eine Entität wird aufgenommen, wenn mindestens ein `include` passt. Sie wird ausgeschlossen, sobald ein `exclude` passt.

## Sortierung und Begrenzung

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

`sort_by` nutzt die Spalten-ID. Mit `+` wird aufsteigend sortiert, mit `-` absteigend.

