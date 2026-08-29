---
title: flex-table-card Sortierung
description: Sortierung, strict mode und Zeilenbegrenzung in der flex-table-card.
---
# Sortierung

## Einfach sortieren

Sortiert wird ueber `sort_by`. Am besten bekommt die Spalte dafuer eine stabile `id`.

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

`+` sortiert aufsteigend, `-` sortiert absteigend.

## Nach mehreren Spalten sortieren

```yaml
sort_by:
  - battery+
  - name-
```

Alternativ geht auch die Kurzform:

```yaml
sort_by: [battery+, name-]
```

## Strict Mode

Mit `strict: true` werden nur Zeilen angezeigt, in denen alle Spalten einen passenden Wert finden.

```yaml
strict: true
```

Das ist besonders nuetzlich, wenn ein `include` viele Entitaeten findet, aber nur ein Teil davon wirklich alle benoetigten Attribute besitzt.

## Sortierung trotz modify

Normalerweise sortiert die Karte nach dem Wert, der nach `modify` entsteht. Wenn das nicht passt, kann mit `sort_unmodified: true` der urspruengliche Wert fuer die Sortierung genutzt werden.

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

Das ist vor allem bei Datumswerten wichtig: Ein ISO-Datum sortiert korrekt, ein lokal formatierter String oft nicht.

Original-Beispielbilder:

- [SortModified.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/SortModified.png)
- [SortUnmodified.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/SortUnmodified.png)

