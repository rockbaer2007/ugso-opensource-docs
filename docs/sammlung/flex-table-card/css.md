---
title: flex-table-card CSS
description: Tabellenlayout und Farben der flex-table-card per CSS anpassen.
---
# CSS

Die flex-table-card kann über den Abschnitt `css` direkt gestaltet werden. Der CSS-Selektor steht als Schlüssel, der CSS-Inhalt als Wert.

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

## Ersetzen oder Erweitern

Ohne `+` wird der vorhandene Stil für den Selektor ersetzt.

```yaml
css:
  table: "border: 0;"
```

Mit `+` wird der Stil ergänzt.

```yaml
css:
  table+: "border: 0;"
```

## Spalten gezielt ansprechen

```yaml
css:
  "thead th:nth-child(1)": "width: 120px;"
  "tbody tr td:nth-child(1)": "font-weight: 600;"
  "tbody tr td:nth-child(3)": "text-align: right;"
```

## Schriftgröße in Tabellenzeilen

```yaml
css:
  "tbody tr td": "font-size: 12px; line-height: 1.25;"
```

## Auswahl von Text erlauben

```yaml
css:
  "tbody tr+": "user-select: text;"
```

