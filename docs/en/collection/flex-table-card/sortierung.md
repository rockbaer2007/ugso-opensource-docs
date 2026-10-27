---
title: flex-table-card sorting
description: Sorting, strict mode and line limits in the flex-table-card.
---
<a id="flex-table-card-sorting"></a>
<a id="current-focus"></a>

# Sorting {#sortierung}

## Sort easily {#einfach-sortieren}

Sorting is done via `sort_by`. It is best to give the column a stable `id`.

```yaml
type: custom:flex-table-card
title: Batterielevel
entities:
  include: sensor.*_battery*
strict: true
sort_by: battery+
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

`+` sorts ascending, `-` sorts descending.

## Sort by multiple columns {#nach-mehreren-spalten-sortieren}

```yaml
sort_by:
  - battery+
  - name-
```

Alternatively, the short form also works:

```yaml
sort_by: [battery+, name-]
```

## Strict Mode {#strict-mode}

With `strict: true`, only rows in which all columns find a matching value are displayed.

```yaml
strict: true
```

This is particularly useful when a `include` finds many entities, but only some of them actually have all the required attributes.

## Sorting despite modify {#sortierung-trotz-modify}

Normally the card sorts by the value that arises after `modify`. If that doesn't work, the original value can be used for sorting with `sort_unmodified: true`.

```yaml
columns:
  - name: Ausgeloest
    id: last_triggered
    data: last_triggered
    sort_unmodified: true
    modify: |-
      if (x) {
        new Date(x).toLocaleString()
      } else {
        "-"
      }
```

This is especially important for date values: an ISO date sorts correctly, a locally formatted string often does not.

Original example images:

- [SortModified.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/SortModified.png)
- [SortUnmodified.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/SortUnmodified.png)
