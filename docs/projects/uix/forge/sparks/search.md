---
title: Search Spark
---
# Search Spark

Der Search Spark sucht innerhalb eines Containers nach Elementen und wendet kleine Mutationen an. Er kann Klassen oder Attribute setzen und Text ersetzen, voranstellen oder anhaengen.

## Grundnutzung

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: search
      for: element
      query: ".event"
      text: "Birthday"
      actions:
        add_class:
          - birthday-event
element:
  type: calendar
  entities:
    - calendar.family
```

## Konfiguration

| Schluessel | Typ | Pflicht | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `type` | `string` | ja | - | Muss `search` sein. |
| `for` | `string` | nein | `element` | UIX-Selektor fuer den Container, in dem gesucht wird. `$` wechselt in Shadow Roots. |
| `query` | `string` | ja | - | CSS-Selektor fuer `querySelectorAll` auf dem Container. Alle Treffer erhalten die Aktionen. |
| `text` | `string` | nein | - | Regulaerer Ausdruck. Wenn gesetzt, werden nur Elemente bearbeitet, deren kompletter Textinhalt passt. |
| `actions` | `object` | nein | `{}` | Mutationen fuer jeden Treffer. |

!!! tip
    Nutze zuerst einen engen `query`-Selektor und erst danach `text`, wenn du weiter filtern musst.

## Aktionen

| Schluessel | Typ | Beschreibung |
| --- | --- | --- |
| `add_class` | `list[string]` | Klassen, die jedem Treffer hinzugefuegt werden. |
| `remove_class` | `list[string]` | Klassen, die von jedem Treffer entfernt werden. |
| `add_attribute` | `list[{attribute, value}]` | HTML-Attribute setzen. Jeder Eintrag braucht `attribute` und `value`. |
| `remove_attribute` | `list[string]` | HTML-Attribute entfernen. |
| `replace_text` | `string` oder `{find, replace}` | RegEx-basierter Textersatz in allen Textknoten des Elements. Ein String entfernt Treffer, ein Objekt ersetzt `find` durch `replace`. |
| `prepend_text` | `string` | Text vor jeden Textknoten setzen. |
| `append_text` | `string` | Text an jeden Textknoten anhaengen. |

## Beispiele

### CSS-Klasse fuer passende Kalenderereignisse setzen

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: search
      for: element
      query: ".event"
      text: "Geburtstag"
      actions:
        add_class:
          - event-birthday
element:
  type: calendar
  entities:
    - calendar.family
uix:
  style: |
    .event-birthday {
      color: var(--accent-color);
      font-weight: 600;
    }
```

### Attribut aus allen Treffern entfernen

```yaml
forge:
  sparks:
    - type: search
      for: element
      query: "[title]"
      actions:
        remove_attribute:
          - title
```

### Text voranstellen und anhaengen

```yaml
forge:
  sparks:
    - type: search
      for: element
      query: ".secondary"
      actions:
        prepend_text: "["
        append_text: "]"
```

### Text in Kind-Elementen matchen

```yaml
forge:
  sparks:
    - type: search
      for: element
      query: ".row"
      text: "Fenster"
      actions:
        add_class:
          - contains-window
```

!!! note
    `text` prueft den gesamten Textinhalt inklusive Kind-Elementen. Dadurch kann ein Treffer auch entstehen, wenn der sichtbare Text aus mehreren DOM-Knoten zusammengesetzt ist.
