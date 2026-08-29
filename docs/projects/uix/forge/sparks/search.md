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

## `replace_text` als String

Wenn `replace_text` ein String ist, wird dieser String als regulaerer Ausdruck gesucht und durch einen leeren Wert ersetzt.

```yaml
forge:
  sparks:
    - type: search
      for: element
      query: ".event"
      actions:
        replace_text: "^Home Assistant: "
```

## `replace_text` mit `find` und `replace`

```yaml
forge:
  sparks:
    - type: search
      for: element
      query: ".event"
      actions:
        replace_text:
          find: "Birthday"
          replace: "Geburtstag"
```

## Attribute setzen

```yaml
forge:
  sparks:
    - type: search
      for: element
      query: ".calendar-event"
      text: "Arzt"
      actions:
        add_attribute:
          - attribute: data-kind
            value: appointment
          - attribute: aria-label
            value: Termin
```

## Klassen kombinieren

```yaml
forge:
  sparks:
    - type: search
      for: element
      query: ".row"
      text: "Warnung|Fehler|Alarm"
      actions:
        add_class:
          - important-row
        remove_class:
          - muted-row
```

## Mit UIX-Styling verbinden

Der Search Spark ist oft nur der erste Schritt. Danach werden die gesetzten Klassen mit UIX gestylt.

```yaml
uix:
  style: |
    .important-row {
      color: var(--error-color);
      font-weight: 600;
    }
    [data-kind="appointment"] {
      border-left: 3px solid var(--accent-color);
      padding-left: 8px;
    }
```

## Hinweise zu RegEx

`text` und `replace_text` verwenden regulaere Ausdruecke. Sonderzeichen wie `.` oder `[` haben deshalb eine besondere Bedeutung und muessen bei Bedarf escaped werden.

| Gewuenscht | Beispiel |
| --- | --- |
| Enthält Wort | `Fenster` |
| Anfang des Textes | `^Fenster` |
| Ende des Textes | `offen$` |
| Mehrere Begriffe | `Fenster|Tuer|Tor` |
| Punkt als Zeichen | `\\.` |

## Performance

Suche nicht unnoetig im gesamten Elementbaum. Ein genauer `for`-Container und ein enger `query`-Selektor sind schneller und stabiler.
