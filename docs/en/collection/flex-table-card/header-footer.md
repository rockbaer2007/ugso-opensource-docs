---
title: flex-table-card header and footer
description: Column headers, icons and summary lines in the flex-table-card.
---
<a id="flex-table-card-header-and-footer"></a>
<a id="current-focus"></a>

# Headers and footers {#header-und-footer}

## Column headings {#spaltenuberschriften}

The card determines the heading of a column in this order:

1.`name`
2.`id`
3.`data`

```yaml
columns:
  - name: Geraet
    data: name
  - id: battery
    data: state
  - data: area
```

An empty heading is possible:

```yaml
columns:
  - name: ""
    data: icon
```

## Icons in the header {#icons-im-header}

```yaml
columns:
  - name: Batterie
    icon: mdi:battery
    data: state
    align: right
```

The alignment of the cells also affects the alignment of the header.

## Activate footer {#footer-aktivieren}

```yaml
display_footer: true
```

You can then specify for each column what is calculated or displayed in the footer.

| Value | Meaning |
| --- | --- |
| `sum` | Total |
| `average` | Average |
| `count` | Number |
| `max` | highest value |
| `min` | lowest value |
| `text` | fixed text |

## Example with totals line {#beispiel-mit-summenzeile}

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

## Design footer using CSS {#footer-per-css-gestalten}

```yaml
css:
  tfoot th: "text-align: right; font-weight: 700;"
  tfoot *: "border-style: solid none none none;"
```

Original example image: [FlexTableFooterExample.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/FlexTableFooterExample.png)
