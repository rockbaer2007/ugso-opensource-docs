---
title: Entities Spark
description: Entitätslisten mit Filtern erzeugen oder IDs für andere Sparks und Templates sammeln.
---

# Entities Spark

::: info Verfügbar ab UIX 9.2.0-beta.3
Entwicklungsfunktion; stabile Basis dieser Dokumentation bleibt 9.1.0.
:::

Der Entities Spark füllt eine Entities-Karte mit gefilterten Entitäten, erzeugt ein Tile-Raster für einen Raum oder sammelt IDs für einen anderen Spark. Die Regeln stammen aus dem [Lint-Free-Technology-Fork von auto-entities](https://github.com/Lint-Free-Technology/lovelace-auto-entities).

## Karten ohne auto-entities-Hülle erzeugen {#create-cards-without-an-auto-entities-wrapper}

Das Grid zeigt für jede Entität im Schlafzimmer eine Tile-Karte und überspringt den Zustand `unavailable`. Ersetze `bedroom` durch einen eigenen Bereich. `path: /cards` füllt die Grid-Liste `cards`; das Spark-`element` liefert die Tile-Konfiguration. Forge setzt jeweils deren `entity`.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: entities
      path: /cards
      element:
        type: tile
      filter:
        include:
          - area: bedroom
        exclude:
          - state: unavailable
element:
  type: grid
  columns: 2
  square: false
  cards: []
```


![Entities Spark erzeugt native Tile-Karten](/projects/uix/assets/page-assets/forge/entities-spark-grid.png)

## Spark-Optionen {#spark-options}

| Option | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `type` | Zeichenfolge | — | Pflichtwert `entities`. |
| `id` / `spark_id` | Zeichenfolge | — | Spark-ID für Foundries, Untersuchung und [Abfrageergebnisse](#reuse-a-query-result). Ohne `path` erforderlich. |
| `path` | [JSON Pointer](config.md#paths-and-operations) | — | Zielliste in Forge-`element`, etwa `/entities` oder `/cards`. Forge erzeugt die Liste, wenn deren übergeordnetes Objekt existiert. Für reine ID-Abfragen weglassen. |
| `mode` | `append`, `prepend`, `replace` | `append` | Einträge hinten, vorne oder anstelle vorhandener Einträge einsetzen. Pro Entitäts-ID gewinnt der erste Eintrag. |
| `entities` | Liste von Entitäts-IDs | — | Explizite IDs vor den Einschlussfiltern hinzufügen. Ausschlussfilter können auch diese IDs entfernen. |
| `filter.include` | Filterliste | — | Entitäten hinzufügen, die mindestens einen Filter erfüllen. `[{}]` beginnt mit allen für den Benutzer verfügbaren Entitäten. |
| `filter.exclude` | Filterliste | — | Nach expliziten IDs und Einschlussfiltern passende Entitäten entfernen. |
| `sort` | Mapping oder Mapping-Liste | — | Einträge sortieren, gruppieren oder begrenzen; siehe [Gruppierung](#group-entity-rows). |
| `element` | Mapping | — | Für jede gewählte Entität zu kopierende Konfiguration. Ohne diesen Wert werden reine IDs geschrieben. |
| `entity_path` | JSON Pointer | `/entity` | Stelle für die ID innerhalb jeder Kopie des Spark-`element`. |

Bei `mode: append` oder `mode: prepend` müssen vorhandene Einträge zum erzeugten Format passen: Zeichenfolgen zu Zeichenfolgen, Mappings zu Mappings. Bei Mappings muss die ID unter demselben `entity_path` liegen. Vorhandene Trennlinien und Abschnittszeilen werden unterstützt.

`mode: replace` ersetzt die gesamte Liste.

### Filter {#filters}

`filter.include` fügt Entitäten hinzu, die mindestens einen Einschlussfilter erfüllen. `filter.exclude` entfernt danach alle zu einem Ausschlussfilter passenden Entitäten. Innerhalb eines Eintrags müssen alle Regeln passen. Gesucht wird nur unter Entitäten, für die HA dem aktuellen Benutzer einen Zustand bereitstellt.

Textregeln unterstützen genaue Namen, Platzhalter in Anführungszeichen wie `entity_id: "sensor.*_battery"` und reguläre Ausdrücke zwischen Schrägstrichen. Numerische Vergleiche stehen ebenfalls in Anführungszeichen, etwa `">= 20"`. `$$` vor einem Muster vergleicht den Wert als JSON, etwa ein Listenattribut. Textregeln passen nur, wenn das Feld einen Wert hat: `area: "*"` wählt Entitäten mit Bereichszuordnung. Auch das `active_choice`-Format des auto-entities-Editors ist möglich.

| Regel | Vergleich |
| --- | --- |
| `domain` | Teil der ID vor dem Punkt, etwa `light` in `light.kitchen`. |
| `entity_id` | Vollständige Entitäts-ID. |
| `name` | Anzeigename der Entität. |
| `state` | Aktueller Zustand. Liste für mehrere Zustandsbedingungen oder Mapping zum Vergleich mit einer anderen Entität. |
| `state_translated` | Zustand in der HA-Sprache. Für Zahlenvergleiche `state` verwenden. |
| `attributes` | Mapping aus Attributnamen und Werten; alle müssen passen. `:` adressiert verschachtelte Attribute. |
| `group` | Direkte Gruppenmitglieder, etwa `group.office` oder eine Lichtgruppe. |
| `group_expanded` | Gruppenmitglieder einschließlich aufgelöster Untergruppen. |
| `area` | Bereichsname oder -ID einschließlich vom Gerät geerbter Bereiche. |
| `floor` | Etagenname oder -ID anhand des eigenen oder geerbten Bereichs. |
| `level` | Numerische Etagenebene, etwa `">= 1"`. |
| `device` | Geräte-ID, benutzerdefinierter oder ursprünglicher Gerätename. |
| `device_manufacturer` / `device_model` | Hersteller oder Modell des zugeordneten Geräts. |
| `label` | Labelname oder -ID an Entität oder Gerät. |
| `integration` | Integrationsname, etwa `browser_mod`, oder ID eines bestimmten Konfigurationseintrags. |
| `hidden_by` | Von `user` oder `integration` ausgeblendet. Ein Zustand muss trotzdem vorhanden sein. |
| `entity_category` | Kategorie im Entitätsregister, etwa `config` oder `diagnostic`. |
| `last_changed` / `last_updated` / `last_triggered` | Zeit seit Änderung, Aktualisierung oder Automation. `"< 15"` bedeutet weniger als 15 Minuten, `"< 2 h ago"` weniger als zwei Stunden. |
| `and` | Alle verschachtelten Filter müssen passen. |
| `or` | Mindestens ein verschachtelter Filter muss passen. |
| `not` | Der eine verschachtelte Filter darf nicht passen. |

Beispiel: Batterieentitäten der Garage einschließen und `unavailable` ausschließen.

```yaml
filter:
  include:
    - area: Garage
      attributes:
        device_class: battery
  exclude:
    - state: unavailable
```


Dieser Einschlussfilter zeigt Batteriesensoren unter 20 %. Statt `value` lässt sich `operator: "<"` mit `entity_id: input_number.battery_threshold` verwenden, um den Grenzwert aus einem Helfer zu lesen.

```yaml
filter:
  include:
    - attributes:
        device_class: battery
        unit_of_measurement: "%"
      state:
        operator: "<"
        value: 20
```


Nach einer für die Liste relevanten Aktualisierung wartet Forge 500 ms und bündelt nahe beieinanderliegende Änderungen. Zeitregeln werden bei HA-Aktualisierungen geprüft. Für Strategien gelten die [Strategie-Aktualisierungsregeln](../forge.md#strategies).

Beim Umstieg von auto-entities kommen die Entitätsregeln nach `filter` und das Listenziel nach `path`. Das Spark-`element` enthält Einstellungen für jeden erzeugten Eintrag. Für unterschiedlich konfigurierte oder sortierte Gruppen separate Sparks verwenden.

## Entitätszeilen ohne auto-entities erzeugen {#generate-entity-rows-without-auto-entities}

Für eine gewöhnliche gefilterte Entities-Karte das Spark-`element` weglassen. Forge schreibt die ausgewählten IDs direkt in die Kartenliste `entities`.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: entities
      path: /entities
      filter:
        include:
          - attributes:
              device_class: battery
        exclude:
          - state: unavailable
      sort:
        method: name
element:
  type: entities
  title: Batteries
  entities: []
```


Beim Umstieg von `auto-entities` liegt der Filter jetzt im Spark; die Kartenoptionen stehen im äußeren Forge-`element`.

## Entitäts-IDs an anderer Stelle schreiben {#write-entity-ids-at-another-path}

Speichert das Schema die ID nicht unter `/entity`, setze `entity_path` als JSON Pointer relativ zu jedem erzeugten Mapping.

```yaml
- type: entities
  path: /some_list
  element:
    target: {}
  entity_path: /target/entity_id
  filter:
    include:
      - area: Garage
```


## Entitätszeilen gruppieren {#group-entity-rows}

`sort.method` legt eine Sortierung fest; eine Liste erlaubt mehrere Stufen nach Priorität. Methoden: `none`, `domain`, `entity_id`, `name`, `friendly_name`, `device`, `area`, `state`, `attribute`, `last_changed`, `last_updated`, `last_triggered`. Bei `method: attribute` zusätzlich den Attributpfad setzen.

Jede Stufe unterstützt `reverse`, `ignore_case`, `ip` und `numeric`. `numeric: nan_first` beziehungsweise `numeric: nan_last` ordnet nichtnumerische Werte vorne oder hinten ein. `count: 5` auf der ersten Stufe begrenzt auf fünf Treffer. `first` überspringt vorher Einträge. Diese Optionen begrenzen die erzeugte Liste; benannte Abfrageergebnisse enthalten weiterhin alle gewählten IDs.

`divider: true` fügt Trennlinien zwischen Gruppen ein. `section: true` fügt vor jeder Gruppe einschließlich der ersten eine Überschrift ein und hat an derselben Stelle Vorrang. Für Listen mit Entitätszeilen verwenden, etwa Entities-Karten oder `custom:fold-entity-row`. Beim Gruppieren das Spark-`element` weglassen.

### Trennlinien zwischen Gruppen {#add-dividers-between-groups}

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: entities
      path: /entities
      filter:
        include:
          - domain: sensor
      sort:
        - method: area
          divider: true
        - method: name
element:
  type: entities
  title: Sensors by area
  entities: []
```


Forge fügt `{ type: divider }` zwischen Bereichsgruppen ein, entfernt doppelte IDs sowie führende, abschließende und aufeinanderfolgende Trennlinien beim Zusammenführen mit selbst definierten Einträgen.

### Überschrift vor jeder Gruppe {#add-a-heading-above-each-group}

Ohne `label` verwendet eine Überschrift den Sortierwert der Gruppe. Mit `label` wählst du Namensbestandteile der ersten Entität: `entity`, `device`, `area`, `floor` oder wörtlichen `text`. `separator` bestimmt den Text zwischen den Teilen.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: entities
      path: /entities
      filter:
        include:
          - domain: sensor
      sort:
        - method: area
          section: true
          label:
            - type: text
              text: "Area: "
            - area
          separator: ""
        - method: name
element:
  type: entities
  title: Sensors by area
  entities: []
```


So entsteht `{ type: section, label: "Area: Kitchen" }` vor der Küchensensorgruppe. Forge entfernt Trennlinien neben Überschriften und fasst benachbarte gleiche Überschriften zusammen, erhält aber Überschriften am Listenanfang und -ende.

## Abfrageergebnis wiederverwenden {#reuse-a-query-result}

Um IDs für andere Sparks oder Templates zu sammeln, vergib eine eindeutige `id` und lasse `path` weg. Dieser Spark dient **nur der Abfrage**: Er akzeptiert `entities` und `filter` und verändert die Forge-Konfiguration nicht. Schreibeinstellungen `mode`, `sort`, `element` und `entity_path` weglassen.

| Ziel für die IDs | Verwendung |
| --- | --- |
| [Configuration Spark](config.md#select-and-where-matchers) | `$in_entities: <id>` mit einem benannten Entities Spark derselben Forge. Dieser darf auch nach `path` schreiben. |
| [Home Summary Spark](home-summary.md#reuse-an-entities-spark-filter) | `$in_entities: <id>` mit einem reinen Abfrage-Spark derselben Card Forge. |
| Forge-Element- oder Hüllen-Styling-Template | `uixForge.entities["<id>"]` eines reinen Abfrage-Sparks derselben Forge lesen. |

### Abfrageergebnis in Templates verwenden {#use-a-query-result-in-templates}

Die Shortcut-Karte zeigt die Anzahl der Entitäten mit dem Label `excluded_from_maintenance`. Ihre Beschreibung wird bei Listenänderungen aktualisiert. Eckige Klammern funktionieren auch für IDs mit Bindestrichen.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: entities
      id: excluded_from_maintenance
      filter:
        include:
          - label: excluded_from_maintenance
element:
  type: shortcut
  label: Maintenance exclusions
  description: >-
    {{ uixForge.entities["excluded_from_maintenance"] | count }} excluded entities
```


Forge wertet Spark-Einstellungen aus, bevor Abfrageergebnisse für Element- und Hüllen-Styling-Templates bereitstehen. Jede Abfrage braucht eine eindeutige ID, damit Forge die Referenz auflösen kann.

### Foundry-Abfrage in einem anderen Element verwenden {#reuse-an-entities-foundry-query-in-another-element}

Speichere den Filter einmal in der [Foundry](../foundries.md) `maintenance-exclusions`. Lasse `path` weg, damit jede Forge selbst über die Verwendung entscheidet.

```yaml
# Foundry: maintenance-exclusions
forge:
  sparks:
    - type: entities
      id: excluded_from_maintenance
      filter:
        include:
          - label: excluded_from_maintenance
```


Das [gefilterte Wartungsdashboard](config.md#wrap-generated-cards) verwendet diese Foundry und ihr reines Abfrageergebnis mit `$in_entities`. Für eine Entities-Karte denselben Spark-`type` und dieselbe `id` wiederholen und im Karten-Forge `path: /entities` ergänzen.

```yaml
type: custom:uix-forge
foundry: maintenance-exclusions
forge:
  mold: card
  sparks:
    - type: entities
      id: excluded_from_maintenance
      path: /entities
      mode: replace
element:
  type: entities
  title: Excluded from Maintenance
  entities: []
```


Forge führt die beiden Spark-Definitionen anhand von Typ und ID zusammen. Die Karte führt den gemeinsamen Filter aus und schreibt das Ergebnis nach `/entities`. Andere Forges führen ihre eigene reine Abfrage aus derselben Foundry aus.

## Liste untersuchen {#inspect-a-list}

`uix_entities_inspect` in der Browserkonsole zeigt ausgewählte Entitäten und die erzeugte Liste. Der letzte Bericht liegt auf `window.uix_inspect.entities`: `ids` enthält IDs, `entries` die erzeugten Einträge und `counts` die Treffer je Einschlussfilter vor Ausschlüssen. Siehe [Entities-Inspektor](../../concepts/dom.md#uix_entities_inspectforge-spark-entities-spark-helper).

Für sichtbare Forge-Elemente deren `<uix-forge>` in DevTools unter **Elements** auswählen und die Befehle in **Console** ausführen. `$0` bezeichnet die Auswahl.

```js
await uix_entities_inspect($0);
window.uix_inspect.entities.ids;
```


Bei mehreren Entities Sparks dessen `id` oder `spark_id` als zweites Argument übergeben, etwa `await uix_entities_inspect($0, "excluded_from_maintenance")`. Alternativ eine Position ab `0` für den ersten Entities Spark angeben.

Für eine Strategie deren Forge-Einstellungen als JavaScript-Objekt übergeben, beginnend mit `type: custom:uix-forge` innerhalb von `strategy:` im Dashboard-YAML. Hier die Wartungsstrategie des [gefilterten Home-Dashboards](config.md#wrap-generated-cards), wenn die Foundry bereits existiert.

```js
await uix_entities_inspect({
  type: "custom:uix-forge",
  foundry: "maintenance-exclusions",
  forge: { mold: "strategy" },
  element: { type: "maintenance" },
}, "excluded_from_maintenance");
window.uix_inspect.entities.ids;
```


Die Untersuchung liest nur. Zum Ausprobieren von Patches mit diesen IDs siehe [Strategie-Patches testen](config.md#test-a-patch).




> Deutsche Bearbeitung der [kanonischen UIX-Dokumentation von Lint-Free-Technology](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Quelle: `dev` / **9.2.0-beta.3**, Revision [6a2bad2](https://github.com/Lint-Free-Technology/uix/commit/6a2bad250e1af75b058353a22371154df23474c8), geprüft am 2026-11-27. Stabile Basis **9.1.0**, HA ab **2026.11.0**. Maßgeblich bleibt das [englische Original](https://uix.lf.technology/).
