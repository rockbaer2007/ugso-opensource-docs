---
title: flex-table-card Header und Footer
description: Spaltenköpfe, Icons und Zusammenfassungszeilen in der flex-table-card.
---
# Header und Footer

## Spaltenüberschriften

Die Karte bestimmt die Überschrift einer Spalte in dieser Reihenfolge:

1. `name`
2. `id`
3. `data`

```yaml
columns:
  - name: Geraet
    data: name
  - id: battery
    data: state
  - data: area
```

Eine leere Überschrift ist möglich:

```yaml
columns:
  - name: ""
    data: icon
```

## Icons im Header

```yaml
columns:
  - name: Batterie
    icon: mdi:battery
    data: state
    align: right
```

Die Ausrichtung der Zellen beeinflusst auch die Ausrichtung des Headers.

## Footer aktivieren

```yaml
display_footer: true
```

Danach kann pro Spalte festgelegt werden, was im Footer berechnet oder angezeigt wird.

| Wert | Bedeutung |
| --- | --- |
| `sum` | Summe |
| `average` | Durchschnitt |
| `count` | Anzahl |
| `max` | höchster Wert |
| `min` | niedrigster Wert |
| `text` | fester Text |

## Beispiel mit Summenzeile

```yaml
type: custom:flex-table-card
title: Werte nach Land
entities: []
display_footer: true
columns:
  - name: Land
    data: rows.country
    footer_type: text
    footer_text: "Gesamt:"
  - name: Wert
    data: rows.value
    fmt: number
    align: right
    footer_type: sum
    footer_modify: x.toFixed(0)
static_data:
  rows:
    - country: Deutschland
      value: 120
    - country: Frankreich
      value: 90
```

## Footer per CSS gestalten

```yaml
css:
  tfoot th: "text-align: right; font-weight: 700;"
  tfoot *: "border-style: solid none none none;"
```

Original-Beispielbild: [FlexTableFooterExample.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/FlexTableFooterExample.png)

