---
title: DOM
description: Home-Assistant-DOM prüfen und UIX-Selektoren sicher finden.
---
# DOM-Navigation

Home Assistant nutzt intensiv [Shadow DOM](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_shadow_DOM). Dadurch lassen sich Komponenten wie `<ha-card>` oder `<ha-icon>` gut wiederverwenden. Für CSS-Styling bedeutet es aber, dass Elemente in einem `#shadow-root` nicht einfach von außen gestylt werden können.

Wenn du Karten im Element-Inspector des Browsers untersuchst, siehst du oft Einträge wie `#shadow-root (open)`. Elemente darin erben nicht automatisch Styles aus dem äußeren DOM.

Um Elemente innerhalb eines `#shadow-root` zu stylen, muss `style:` als Dictionary geschrieben werden, nicht nur als String. Jeder Dictionary-Schlüssel wählt ein oder mehrere Elemente über eine angepasste `querySelector()`-Suche aus. Der Wert wird dann in diese Elemente injiziert.

::: tip
Die angepasste `querySelector()`-Funktion ersetzt ein Dollarzeichen `$` durch einen `#shadow-root` im Selektor.
:::

Der Prozess ist rekursiv. Der Wert eines Eintrags kann also wieder ein Dictionary sein. Ein Schlüssel `.` wählt das aktuelle Element.

::: details Beispiel: Markdown-Karte

Ziel: Alle Überschriften dritter Ebene `###` in einer Markdown-Karte violett färben und den Kartenhintergrund ändern.

```yaml
type: markdown
content: |-
  # Example
  ## A teal markdown card where h3 tags are purple
  ### Like this
```

Das `<ha-card>`-Element ist die Basis. Von dort muss ein Shadow Root innerhalb von `<ha-markdown>` durchquert werden. Der Selektor ist:

```yaml
ha-markdown $:
```

Für den Hintergrund soll direkt auf das Basiselement geschrieben werden:

```yaml
.:
```

Das vollständige UIX-Styling:

```yaml
uix:
  style:
    ha-markdown $: |
      h3 {
        color: purple;
      }
    .: |
      ha-card {
        background: teal;
      }
```

![DOM navigation](https://raw.githubusercontent.com/Lint-Free-Technology/uix/9a0fa57d4afd262a5eaec4f1bfb7c154667bb2c9/docs/source/assets/page-assets/concepts/concepts-markdown.png)

:::

Eine Selektorkette sucht Schritt für Schritt nach Elementen, getrennt durch Leerzeichen oder `$`. Für jeden Zwischenschritt wird nur der erste Treffer gewählt. Beim letzten Selektor einer Dictionary-Ebene werden dagegen **alle** passenden Elemente gewählt.

Ketten, die mit `$` enden, sind ein Komfortfall: Sie wählen die Shadow Roots aller passenden Elemente.

::: details Verkettungsbeispiel

Dieser Pfad wählt `div`-Elemente im ersten Marker einer Map-Karte:

```yaml
ha-map $ ha-entity-marker $ div: |
```

Dieser Pfad wählt `div`-Elemente in allen Map-Markern, weil die Suche bei `ha-entity-marker $` aufgeteilt wird:

```yaml
ha-map $ ha-entity-marker $:
  div: |
```

:::

::: warning Lade-Reihenfolge
Home Assistant optimiert die Lade-Reihenfolge stark. Es ist nicht garantiert, dass zum Zeitpunkt der UIX-Suche alle Elemente bereits existieren. Wenn etwas nur manchmal funktioniert, teile die Kette in mehrere Ebenen auf:

```yaml
ha-map $:
  ha-entity-marker $:
    div: |
```

So kann UIX später ab dem stabileren Zwischenpunkt erneut suchen.
:::

## Express Search Selector `$$`

Für tief verschachtelte Elemente, vor allem Card Features und More-info Controls, wäre ein vollständiger Pfad durch alle Shadow Roots sehr lang. Der Express-Search-Selektor `$$` ist eine Kurzform für eine rekursive, Shadow-DOM-durchdringende Suche durch alle Nachfahren des aktuellen Kontexts.

```text
A $$ B $
```

entspricht sinngemäß:

```text
A $ <zwischen-1> $ <zwischen-2> $ ... B $
```

Die Zwischenstationen werden automatisch gefunden.

::: tip
`$$` ist ein Selektor für die Pfadmitte. Er muss zwischen zwei Selektorschritten stehen und darf nicht am Anfang eines Pfads stehen.
:::

::: details Card Features: vorher und nachher

Ausführlicher Pfad:

```yaml
uix:
  style:
    hui-card-features $:
      hui-card-feature $:
        hui-humidifier-toggle-card-feature $:
          ha-control-select $: |
            .container {
              opacity: 0.8;
            }
```

Mit `$$`:

```yaml
uix:
  style:
    "hui-card-features $$ ha-control-select $": |
      .container {
        opacity: 0.8;
      }
```

:::

::: details Mehrere Card-Feature-Typen

```yaml
uix:
  style:
    "hui-card-features $$ ha-control-number-buttons $": |
      #input::before {
        background: red;
      }
    "hui-card-features $$ ha-control-select-menu $": |
      .select-anchor {
        --control-select-menu-background-color: red !important;
      }
      .select-anchor:hover {
        --control-select-menu-background-color: purple !important;
      }
```

:::

::: warning Performance
Da `$$` das gesamte Shadow-DOM-Teilbaumgebiet durchsucht, ist es langsamer als ein expliziter Pfad. Für performancekritische Fälle ist ein genauer Pfad besser.
:::

::: warning Lade-Reihenfolge und Retries
Das Retry-Verhalten durch Aufteilen von Ketten gilt pro Dictionary-Eintrag. Bei `$$` wird die gesamte Tiefensuche als Einheit wiederholt. Wenn das Ziel sehr spät lädt, ist ein explizit aufgeteilter Pfad stabiler:

```yaml
uix:
  style:
    hui-card-features $:
      "hui-card-feature $$ ha-control-select $": |
        .container { opacity: 0.8; }
```
:::

## Host/Element-Pfad-Auswahl

Ein Pfad kann mit einem `&`-Host/Element als erstem Schritt beginnen. Dieser Schritt filtert das ursprüngliche Element, auf das UIX angewendet wird, bevor Traversal stattfindet.

- Ist das Start-Element ein **ShadowRoot**, wird gegen den **Host** dieses Shadow Roots geprüft.
- Ist das Start-Element ein normales **Element**, wird gegen dieses Element geprüft.

Das wird vor allem in Themes genutzt, um Pfade nur dann anzuwenden, wenn Host oder Element eine bestimmte Klasse, ID, ein Attribut oder eine Property besitzen.

Die Prüfung erfolgt direkt gegen Parent-/Host-Properties, nicht über die CSS-Selector-Engine. Unterstützt werden:

| Token | Prüfung |
| --- | --- |
| `tagname` | `element.localName === 'tagname'` |
| `.classname` | `element.classList.contains('classname')` |
| `#id` | `element.id === 'id'` |
| `[attr]` | `element.hasAttribute('attr')` |
| `[attr=val]` | exakter Attributwert |
| `[attr^=val]` | Wert beginnt mit |
| `[attr$=val]` | Wert endet mit |
| `[attr*=val]` | Wert enthält |
| `[attr~=val]` | Whitespace-getrenntes Wort |
| `[attr\|=val]` | Wert ist gleich oder beginnt als `-`-Subtag |
| `{.prop}` | `element.prop` ist nicht `null` oder `undefined` |
| `{.prop=val}` | `String(element.prop) === val` |
| `{.prop^=val}` | String-Wert beginnt mit `val` |
| `{.prop$=val}` | String-Wert endet mit `val` |
| `{.prop*=val}` | String-Wert enthält `val` |
| `{.prop~=val}` | Whitespace-getrenntes Wort im String-Wert |
| `{.prop\|=val}` | Wert ist gleich oder beginnt als `-`-Subtag |

Tokens können kombiniert werden, zum Beispiel `&ha-dialog.my-class[data-type="video"]`. Alle Tokens müssen passen. Leerzeichen außerhalb von Attributklammern und Property-Klammern teilen den Pfad und sind in einem `&`-Selektor nicht unterstützt. Leerzeichen und `$` innerhalb von `[...]` und `{...}` gelten als normale Zeichen.

Property-Selektoren navigieren echte JavaScript-Properties über dot-separierte Pfade mit optionalem Chaining, zum Beispiel `{.notification.notification_id='1234567'}`. Ganze Zahlen werden bei Arrays als Indizes behandelt, etwa `{.items.0.name}`.

Klassenbasierte Selektoren können zur Lesbarkeit geklammert werden: `&(.my-class)` entspricht `&.my-class`.

::: details Dialog stylen

Nur den Inhalt eines Dialogs vom Typ `type-hui-dialog-web-browser-play-media` stylen:

```yaml
uix-dialog-yaml: |
  "&(.type-hui-dialog-web-browser-play-media) $ ha-dialog-header $": |
    section.header-content {
      display: none;
    }
```

:::

::: details Badge stylen

```yaml
uix-badge-yaml: |
  .: |
    :host(.type-power-total) {
      --ha-card-border-width: 3px;
      --ha-card-border-color: red;
    }
  "&.type-power-total ha-badge $": |
    .badge {
      border-style: double !important;
    }
```

:::

::: details Attribut-Selektoren mit `$=` und Punkten

```yaml
uix-entity-marker-yaml: |
  "&[entity-id$='dev']": |
    :host {
      --uix-image: /local/media/person_grey.png;
    }
    div.marker {
      border-color: red !important;
      border-width: 5px;
    }
```

```yaml
uix-entity-marker-yaml: |
  "&[entity-id='person.dev']": |
    :host {
      --uix-image: /local/media/person_grey.png;
    }
    div.marker {
      border-color: red !important;
      border-width: 5px;
    }
```

:::

::: details Property-Selektoren `{.prop}`

```yaml
uix:
  style:
    "&{.notification}":
      ".": |
        ha-card { opacity: 0.5; }

    "&{.notification.notification_id='1234567'}":
      ".": |
        ha-card { border: 2px solid red; }

    "&{.type^=light}":
      ".": |
        ha-card { background: yellow; }

    "&{.items.0.name='foo'}":
      ".": |
        ha-card { background: teal; }
```

Alle Operatoren wie bei Attribut-Selektoren werden unterstützt: `=`, `~=`, `^=`, `$=`, `*=`, `|=`.

:::

## DOM-Inspektionshelfer

UIX liefert drei Browser-Konsolenhelfer mit, um gültige Style-Pfade, Forge-Spark-Pfade und die UIX-Hierarchie zur Laufzeit zu verstehen. Öffne die DevTools, wähle ein Element im **Elements**-Panel aus, sodass es `$0` ist, und rufe einen der Helfer auf.

### `uix_tree($0)`: allgemeiner Helfer

Zeigt alles, was UIX über den Bereich um das ausgewählte Element weiß.

| Bereich | Inhalt |
| --- | --- |
| **Closest UIX Parent** | Nächstes übergeordnetes Element mit nicht-kindlichem `uix-node`, inklusive Template-Variablen und UIX-Typ. |
| **Active UIX Children** | Pfade, die aktuell als Kinder des UIX-Parents gestylt werden, inklusive aufgelöster DOM-Elemente. |
| **Available YAML Selectors** | Alle erreichbaren YAML-Style-Schlüssel innerhalb des Shadow-DOM-Teilbaums des UIX-Parents. |

```js
uix_tree($0)
```

### `uix_style_path($0)`: spezifischer Style-Helfer

Zeigt den genauen UIX-Pfad zum ausgewählten Element und erzeugt ein YAML-Grundgerüst.

| Bereich | Inhalt |
| --- | --- |
| **Closest UIX Parent** | Wie bei `uix_tree`. |
| **UIX Path to Target** | Exakter Pfad mit `$` für Shadow-Root-Wechsel vom UIX-Parent zu `$0`. |
| **CSS Target** | Tagname, ID, Klassen und vorgeschlagener CSS-Selektor. |
| **Boilerplate UIX YAML** | Einfügbares Karten-YAML, wenn der Typ direkt über `uix:` gestylt werden kann. |
| **Boilerplate Theme YAML** | Einfügbares Theme-YAML; bei Theme-only-Typen ist dies das einzige Grundgerüst. |

```js
uix_style_path($0)
```

`uix_path($0)` ist ein Kurz-Alias für `uix_style_path($0)`.

### `uix_forge_path($0)`: Forge-Helfer

Zeigt den Pfad vom nächsten `uix-forge`-Element zum ausgewählten Element. Der Pfad kann als Wert für `for`, `before` oder `after` in einer Forge-Spark-Konfiguration genutzt werden.

| Bereich | Inhalt |
| --- | --- |
| **Closest UIX Forge Parent** | Nächstes übergeordnetes `uix-forge`-Element. |
| **Forge Path to Target** | Selektorpfad mit `$` für Shadow-Root-Wechsel vom erzeugten Element zu `$0`. |
| **Boilerplate Spark YAML** | Einfügbares Spark-YAML mit dem gefundenen Pfad. |

```js
uix_forge_path($0)
```

::: warning
Wenn du ein Spark-Element desselben Typs hinzufügst, zum Beispiel ein Tile-Icon **before** `ha-tile-icon`, achte besonders auf die Dokumentation dieses Sparks. Der Pfad muss spezifisch genug sein, damit UIX bei Updates nicht das Spark-Element selbst auswählt.
:::
