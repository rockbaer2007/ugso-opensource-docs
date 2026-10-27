---
title: flex-table-card CSS
description: Adjust the table layout and colors of the flex-table-card using CSS.
---
<a id="flex-table-card-css"></a>
<a id="current-focus"></a>

# CSS {#css}

The flex-table-card can be designed directly using the `css` section. The CSS selector is the key, the CSS content is the value.

```yaml
type: custom:flex-table-card
title: Tabelle
entities:
  include: sensor.*
columns:
  - name: Name
    data: name
  - name: Wert
    data: state
css:
  table: "border-collapse: collapse; width: 100%;"
  thead th: "font-weight: 700; font-size: 13px;"
  tbody tr td: "font-size: 12px; padding: 6px 8px;"
  "tbody tr:nth-child(odd)": "background-color: rgba(255,255,255,0.04);"
  "tbody tr:nth-child(even)": "background-color: rgba(255,255,255,0.08);"
```

## Replace or Expand {#ersetzen-oder-erweitern}

Without `+`, the existing style for the selector is replaced.

```yaml
css:
  table: "border: 0;"
```

The style is completed with `+`.

```yaml
css:
  table+: "border: 0;"
```

## Target columns {#spalten-gezielt-ansprechen}

```yaml
css:
  "thead th:nth-child(1)": "width: 120px;"
  "tbody tr td:nth-child(1)": "font-weight: 600;"
  "tbody tr td:nth-child(3)": "text-align: right;"
```

## Font size in table rows {#schriftgroße-in-tabellenzeilen}

```yaml
css:
  "tbody tr td": "font-size: 12px; line-height: 1.25;"
```

## Allow selection of text {#auswahl-von-text-erlauben}

```yaml
css:
  "tbody tr+": "user-select: text;"
```
