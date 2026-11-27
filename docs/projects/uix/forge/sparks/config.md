---
title: Configuration Spark
description: Forge-Konfigurationen und die Ausgabe von Dashboard-Strategien vor der Darstellung ändern.
---

# Configuration Spark

::: info Verfügbar ab UIX 9.2.0-beta.3
Diese Funktion gehört zum Entwicklungsstand; stabile Basis dieser Dokumentation bleibt 9.1.0.
:::

Mit dem Configuration Spark ergänzt du Karten in erzeugten Dashboards, entfernst unerwünschte Abschnitte oder änderst Optionen, bevor Home Assistant sie darstellt. Jede Änderung ist ein **Patch**. Ergänze unter `forge.sparks` einen Spark mit `type: config` und liste seine Patches in der gewünschten Reihenfolge auf.

Hier erzeugt die HA-Ansichtsstrategie `original-states` die üblichen Karten. `prepend` setzt eine Markdown-Karte über die volle Breite an den Anfang der `cards`-Liste.

![Configuration Spark ergänzt eine Karte in einer HA-Ansichtsstrategie](/projects/uix/assets/page-assets/forge/config-spark-strategy.png)

```yaml
title: Forge strategy configuration
views:
  - path: overview
    strategy:
      type: custom:uix-forge
      forge:
        mold: strategy
        sparks:
          - type: config
            patches:
              - op: prepend
                path: /cards
                value:
                  type: markdown
                  content: "## Added by Forge"
                  grid_options:
                    columns: full
      element:
        type: original-states
```


## Pfade und Operationen {#paths-and-operations}

Bei `path` bezeichnet ein [JSON Pointer](https://www.rfc-editor.org/rfc/rfc6901) die genaue Stelle: `/cards` ist die gesamte Kartenliste, `/cards/0` ihre erste Karte und `""` die gesamte Konfiguration. Enthält ein Schlüssel `/` oder `~`, schreibe dafür `~1` beziehungsweise `~0`.

::: details Warum JSON Pointer statt JSONPath?
Ein JSON Pointer gibt eine genaue Adresse an, etwa `/cards/0` für die erste Karte. JSONPath kann mehrere Ergebnisse suchen. Wenn sich die Position einer erzeugten Karte oder Section ändern kann, suche sie mit `select` anhand ihres Inhalts und verwende anschließend einen Pointer für ein Feld darin.
:::

| Operation | Wirkung |
| --- | --- |
| `merge` | Mapping ändern und andere Schlüssel erhalten. |
| `replace` | Wert oder gesamte Konfiguration ersetzen. |
| `remove` | Vorhandenen Mapping-Schlüssel oder Listeneintrag entfernen. |
| `remove_matching` | Zu `where` passende Elemente aus einer Liste oder allen mit `all` benannten Listen entfernen. |
| `wrap_strategy` | Erzeugte untergeordnete Strategie erweitern, ohne ihre Quellkonfiguration zu kopieren. |
| `wrap_card` | Erzeugte Karte erweitern, ohne ihre Quellkonfiguration zu kopieren. |
| `append` / `prepend` | Eintrag hinten beziehungsweise vorne an eine Liste anhängen. |
| `insert_before` / `insert_after` | Neben einem ausgewählten oder indizierten Eintrag einfügen. |

`merge` aktualisiert passende Schlüssel innerhalb von Mappings und erhält die übrigen. Eine Liste, ein Einzelwert oder `null` ersetzt den vorherigen Wert dieses Schlüssels.

### Patch-Felder {#patch-fields}

| Feld | Verwendet von | Bedeutung |
| --- | --- | --- |
| `op` | Jeder Patch | Operation aus der obigen Tabelle. |
| `path` | Jede Operation | Exakte Zieladresse als JSON Pointer. |
| `select` | Jede Operation | Einen Eintrag anhand seines Inhalts finden. |
| `all` | `remove_matching`, `wrap_card` | Jede Liste mit genau diesem Schlüssel besuchen, etwa `cards` oder `entities`. `all: cards` sucht Karten in allen Kartenlisten. |
| `value` | `merge`, `replace`, `wrap_strategy`, `wrap_card`, `append`, `prepend`, `insert_before`, `insert_after` | Zu schreibende Daten. |
| `where` | `remove_matching`, `wrap_card` mit `all` | Jeden Eintrag der Zielliste prüfen. |
| `required` | `wrap_card` mit `all` | `false` erlaubt, dass keine Karte passt. |

Jeder Patch hat genau eine Zielangabe: `path` für eine genaue Adresse, `select` für einen Eintrag oder `all` für Listen mit einem bestimmten Schlüssel.

### Auswahlregeln für `select` und `where` {#select-and-where-matchers}

Verwende `select`, wenn du den Inhalt eines Eintrags kennst, seine Position aber wechseln kann. Suche beispielsweise die Section mit der Überschrift Favorites und bearbeite deren `cards`-Liste.

| Feld unter `select` | Inhalt |
| --- | --- |
| `in` | JSON Pointer auf die zu durchsuchende Liste, etwa `/sections`. |
| `match` | Felder, die genau einen Eintrag dieser Liste identifizieren. |
| `path` | Optionaler JSON Pointer innerhalb dieses Eintrags, etwa `/cards`. Ohne ihn wird der Eintrag selbst adressiert oder daneben eingefügt. |
| `required` | Standard `true`; `false` überspringt den Patch, wenn kein Eintrag passt. |

`select.match` identifiziert ein Ziel. `where` prüft jeden Eintrag einer Zielliste. Beide verstehen dieselben Regeln einschließlich Forge-Operatoren mit `$`.

| Regel | Bedeutung |
| --- | --- |
| `type: tile` | Direkter Schlüssel-/Wertvergleich. Mappings werden teilweise verglichen; nicht angegebene Schlüssel sind unerheblich. |
| `$contains: [...]` | Die Liste enthält für jede Regel einen eigenen passenden Eintrag, etwa eine bestimmte Karte in einer Section. |
| `$in_entities: no_favs` | Der Wert ist eine Entitäts-ID aus dem Entities Spark `no_favs` derselben Forge. |

Der folgende Patch entfernt Karten unabhängig vom Kartentyp, wenn deren eigenes `entity` zur Abfrage passt.

```yaml
- op: remove_matching
  all: cards
  where:
    entity:
      $in_entities: no_favs
```


Ergänze `type: tile` unter `where`, um nur Tiles zu entfernen.

```yaml
- op: remove_matching
  all: cards
  where:
    type: tile
    entity:
      $in_entities: no_favs
```


`all: cards` besucht alle Listen mit dem Namen `cards`, auch innerhalb von Stacks und Sections. `all: entities` besucht entsprechend die `entities`-Listen. Geprüft werden jeweils deren direkte Einträge. Serviceziele, Bedingungen und andere Entitätsreferenzen innerhalb dieser Einträge werden nicht mitgeprüft.

Ein Template in `value` kann mit `| tojson` ein JSON-Objekt oder eine Liste zurückgeben. Forge verwendet dieses Mapping oder diese Liste als Patch-Wert.

## Strategien {#strategies}

Verwende den Spark in der [Forge-Strategie](../forge.md#strategies), die den zu ändernden Teil erzeugt. Eine Dashboard-Strategie kann `/views`, eine Ansichtsstrategie `/cards` oder `/sections` erzeugen. Patch-Pfade beziehen sich auf diese Ausgabe. Der [Strategie-Inspektor](#inspect-generated-strategies) zeigt die tatsächlich erzeugten Listen und Felder.

### Erzeugte untergeordnete Strategie einhüllen {#wrap-a-generated-child-strategy}

Die Dashboard-Strategie `home` erzeugt Ansichten einschließlich einer Übersicht, deren eigene Strategie `home-overview` ihre Karten erst später erzeugt. Um diese Karten zu ändern, verwende `wrap_strategy` am `strategy`-Eintrag der Ansicht und hinterlege die Karten-Patches innerhalb dieser Hülle. Die anderen Ansichten bleiben wie von Home erzeugt.

Richte `path` oder `select.path` auf den verschachtelten Schlüssel `strategy`. Hinterlege in `value` die zusätzlichen Einstellungen einschließlich `forge.mold: strategy` oder einer Foundry, die dies bereitstellt. Forge ergänzt `type: custom:uix-forge` und bewahrt die ursprünglichen Strategieeinstellungen als `element_base`. Eine bereits vorhandene Forge-Strategie kannst du direkt ändern.

### Übersicht um eine Personenkarte erweitern {#wrap-the-overview-strategy-to-add-a-people-map}

Das Beispiel ergänzt unter den Zusammenfassungen eine People-Section mit Karte im Hauptlayout und erhält die Bereichs-Unteransichten von Home. Ersetze die beiden Tracker durch eigene Personen oder Gerätetracker. Zum Einrichten das vollständige YAML verwenden; beim späteren Bearbeiten beachten, [welcher Teil einzufügen ist](#create-or-edit-the-dashboard).

```yaml
title: My Home
views: []
strategy:
  type: custom:uix-forge
  forge:
    mold: strategy
    sparks:
      - type: config
        patches:
          - op: wrap_strategy
            select:
              in: /views
              match:
                strategy:
                  type: home-overview
              path: /strategy
            value:
              forge:
                mold: strategy
                sparks:
                  - type: config
                    patches:
                      - op: insert_after
                        select:
                          in: /sections
                          match:
                            type: grid
                            cards:
                              $contains:
                                - type: home-summary
                        value:
                          type: grid
                          column_span: 4
                          cards:
                            - type: heading
                              heading: People
                              icon: mdi:account-multiple
                              tap_action:
                                action: navigate
                                navigation_path: /map
                            - type: map
                              entities:
                                - device_tracker.phone
                                - device_tracker.tablet
                              grid_options:
                                columns: full
  element:
    type: home
    favorite_entities:
      - light.bed_light
```


![Personenkarte hinter den Zusammenfassungen der Home-Übersicht](/projects/uix/assets/page-assets/forge/config-spark-people-map.png)

Der äußere Patch findet die Übersicht in `/views` und hüllt deren `/strategy` ein. Home-Einstellungen wie `favorite_entities` bleiben erhalten. Der innere Patch findet die Hauptsection mit einer Home-Summary-Karte und fügt People dahinter ein. Auf breiten Bildschirmen kann Home die Zusammenfassungen in der Seitenleiste anzeigen, während People im Hauptlayout bleibt. Die People-Überschrift öffnet die HA-Kartenseite.

### Erzeugte Karten einhüllen {#wrap-generated-cards}

`wrap_card` macht eine Karte zu einer Card Forge und erhält ihre ursprünglichen Einstellungen als `element_base`. Zusätze gehören nach `value`.

- `path` oder `select` hüllt eine Karte ein.
- `all: cards` mit `where` hüllt alle passenden Karten ein. `required: false` erlaubt null Treffer.

#### Wartung auf Home und der geöffneten Unterseite filtern {#filter-maintenance-on-home-and-on-the-page-it-opens}

::: info
Die HA-Entwickler arbeiten an einer standardisierten Entitätsfilterung in der Home-Dashboard-Strategie. Sobald sie verfügbar ist, lassen sich Entitäten möglicherweise direkt dort ausschließen.
:::

Verwende eine gemeinsame Ausschlussliste für die Wartungszusammenfassung und ihre Zielseite. Das Beispiel hüllt die Wartungskarten im Hauptlayout und in der Seitenleiste ein und verknüpft beide mit einer gefilterten Wartungs-Unteransicht des erzeugten Dashboards.

1. Lege in HA das Label `excluded_from_maintenance` an und weise es auszuschließenden Entitäten zu. Lass die Wartungszusammenfassung in Home aktiviert, damit Forge eine Karte einhüllen kann.
2. Erstelle in UIX die [Foundry](../foundries.md) `maintenance-exclusions` mit dem folgenden YAML. Sie hält den Filter für Karten und Unteransicht.
3. Verwende danach das Dashboard-YAML. Passe `/filtered-home-maintenance` in `navigation_path` an deinen Dashboard-Pfad an und behalte `/maintenance` am Ende. Siehe [Dashboard erstellen und bearbeiten](#create-or-edit-the-dashboard).

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




```yaml
title: Filtered Home Maintenance
views: []
strategy:
  type: custom:uix-forge
  forge:
    mold: strategy
    sparks:
      - type: config
        patches:
          - op: wrap_strategy
            select:
              in: /views
              match:
                strategy:
                  type: home-overview
              path: /strategy
            value:
              forge:
                mold: strategy
                sparks:
                  - type: config
                    patches:
                      - op: wrap_card
                        all: cards
                        where:
                          type: home-summary
                          summary: maintenance
                        value:
                          foundry: maintenance-exclusions
                          forge:
                            mold: card
                            sparks:
                              - type: home-summary
                                exclude:
                                  - $in_entities: excluded_from_maintenance
                          element:
                            tap_action:
                              action: navigate
                              # Replace this dashboard URL path if different.
                              navigation_path: /filtered-home-maintenance/maintenance
          - op: append
            path: /views
            value:
              title: Maintenance
              path: maintenance
              subview: true
              strategy:
                type: custom:uix-forge
                foundry: maintenance-exclusions
                forge:
                  mold: strategy
                  sparks:
                    - type: config
                      patches:
                        - op: remove_matching
                          all: cards
                          where:
                            entity:
                              $in_entities: excluded_from_maintenance
                element:
                  type: maintenance
  element:
    type: home
```


Auf Overview schließt der [Home Summary Spark](home-summary.md) markierte Entitäten von der nativen Wartungszählung aus. `tap_action` öffnet die ergänzte Unteransicht.

![Native Wartungszusammenfassung durch Forge gefiltert und umgeleitet](/projects/uix/assets/page-assets/forge/config-spark-maintenance-shortcut.png)

Die Unteransicht verwendet die HA-Wartungsstrategie und denselben Foundry-Filter, um erzeugte Karten mit passendem `entity` zu entfernen. Im Bild fehlt der markierte Kohlendioxid-Eintrag. `subview: true` hält die Unteransicht aus der Tableiste heraus.

![Gefilterte Wartungs-Unteransicht im Home-Dashboard](/projects/uix/assets/page-assets/forge/config-spark-maintenance-exclusion.png)

::: warning
Das eingebaute Wartungspanel verwendet weiterhin die ursprüngliche HA-Liste. Es und die erzeugte Unteransicht verwenden zwar die Ansichtsstrategie `maintenance`, aber nur die Forge-Unteransicht filtert Entitäten.
:::

Dasselbe Muster funktioniert für Licht oder Sicherheit: die passende Zusammenfassung einhüllen und eine Unteransicht für deren Strategie erstellen.

### Markierte Favoritenvorschläge entfernen {#remove-labelled-favorites-suggestions}

Das HA-Label `no_favs` hält Karten aus den erzeugten Favoriten heraus. Das Beispiel entfernt zusätzlich die gesamte Section Other areas. Es hüllt Overview ein, sammelt IDs über eine [Entities-Abfrage](entities.md#reuse-a-query-result) und findet die erzeugten Sections mit zwei Patches anhand ihrer Überschrift.

```yaml
title: My Home
views: []
strategy:
  type: custom:uix-forge
  forge:
    mold: strategy
    sparks:
      - type: config
        patches:
          - op: wrap_strategy
            select:
              in: /views
              match:
                strategy:
                  type: home-overview
              path: /strategy
            value:
              forge:
                mold: strategy
                sparks:
                  - type: entities
                    id: no_favs
                    filter:
                      include:
                        - label: no_favs
                  - type: config
                    patches:
                      - op: remove_matching
                        select:
                          in: /sections
                          required: false
                          match:
                            cards:
                              $contains:
                                - type: heading
                                  heading: Favorites
                          path: /cards
                        where:
                          entity:
                            $in_entities: no_favs
                      - op: remove
                        select:
                          in: /sections
                          required: false
                          match:
                            type: grid
                            cards:
                              $contains:
                                - type: heading
                                  heading: Other areas
  element:
    type: home
```


Der Favorites-Patch adressiert `/cards` der passenden Section und entfernt unabhängig vom Kartentyp Karten mit passendem `entity`. Der Other-areas-Patch adressiert die Section selbst. Beide können eine fehlende Section überspringen. Bei einer anderen Dashboard-Sprache zuerst die erzeugten Überschriften prüfen und deren tatsächlichen Text verwenden.

### Dashboard erstellen oder bearbeiten {#create-or-edit-the-dashboard}

Zeigt der Rohkonfigurationseditor das gesamte Dashboard, füge das vollständige Beispiel ab `title`, `views` und `strategy` ein.

::: warning Geöffneten Editor prüfen
Nach dem Speichern kann HA einen Editor nur für die Strategie öffnen. Beginnt er mit `type: custom:uix-forge`, kopiere ausschließlich den Inhalt unter `strategy:` und entferne zwei Einrückungszeichen, sodass `type` links beginnt. Das vollständige Dashboard würde eine zweite `strategy:` verschachteln und „No strategy type found“ verursachen.
:::

## Erzeugte Strategien untersuchen {#inspect-generated-strategies}

Prüfe die Ausgabe in der DevTools-**Console**, bevor du ein Patch-Ziel wählst. Öffne für Home das native Home-Dashboard und führe die Befehle der Reihe nach aus. Jeder Inspektor speichert seinen letzten Bericht für den nächsten Befehl auf `window.uix_inspect`.

### Erzeugte Konfiguration finden {#find-the-generated-config}

`uix_dashboard_inspect()` liest das geöffnete Dashboard. `rawConfig` enthält die gespeicherte Konfiguration, `generatedConfig` die von HA dargestellte und `strategy` die oberste Strategie. Kopiere `window.uix_inspect.dashboard.strategy` nach Forge-`element`, um mit denselben Home-Einstellungen zu starten. Siehe [Dashboard-Inspektor](../../concepts/dom.md#uix_dashboard_inspect-current-dashboard-helper).

```js
uix_dashboard_inspect();
window.uix_inspect.dashboard.strategy;
```


`uix_strategy_inspect(scope, element)` führt eine Strategie aus und speichert die Ausgabe als `window.uix_inspect.strategy.config`. Übergebe den Bereich (`"dashboard"`, `"view"`, `"section"`) und die für Forge-`element` vorgesehenen Einstellungen. Erzeuge für die übernommenen Home-Overview-Optionen zuerst das Dashboard und übergebe dann dessen erzeugte `home-overview`-Strategie. Siehe [Strategie-Inspektor](../../concepts/dom.md#uix_strategy_inspectscope-element-strategy-config-helper).

```js
await uix_strategy_inspect("dashboard", window.uix_inspect.dashboard.strategy);
await uix_strategy_inspect(
  "view",
  window.uix_inspect.strategy.config.views.find(
    (view) => view.strategy?.type === "home-overview",
  ).strategy,
);
```


`paths(term)` durchsucht den aktuellen Bericht nach Pfad oder Vorschauwert. `get(path)` liest einen exakten Wert. Prüfe hier zuerst die Sections, bevor du eine Kartenliste auswählst.

```js
window.uix_inspect.strategy.paths("home-summary");
window.uix_inspect.strategy.paths("Favorites");
window.uix_inspect.strategy.get("/sections");
```


### Patch ausprobieren {#test-a-patch}

`window.uix_inspect.strategy.test(patches, entitySets?)` übernimmt die für `patches:` bestimmte Liste. Die Änderungen laufen auf einer Kopie der untersuchten Ausgabe, protokollieren Ergebnis oder Fehler und ändern das Dashboard nicht. Das Beispiel prüft das Einfügen einer Karte in die Hauptsection mit Zusammenfassungen der untersuchten Übersicht.

```js
window.uix_inspect.strategy.test([
  {
    op: "append",
    select: {
      in: "/sections",
      match: {
        cards: { $contains: [{ type: "home-summary", summary: "light" }] },
      },
      path: "/cards",
    },
    value: { type: "tile", entity: "light.kitchen" },
  },
]);
```


Das Beispiel setzt eine aktivierte Lichtzusammenfassung voraus. Ist sie ausgeblendet, verwende das `summary` einer mit `paths("home-summary")` gefundenen Karte.

Für den [Favoritenausschluss](#remove-labelled-favorites-suggestions) zuerst IDs mit dem [Entities-Inspektor](entities.md#inspect-a-list) sammeln. Übergebe sie unter demselben Namen wie die `$in_entities`-Referenz des Patches. Lass den Overview-Bericht aus den vorherigen Schritten geladen.

```js
await uix_entities_inspect({
  type: "custom:uix-forge",
  forge: {
    mold: "strategy",
    sparks: [{
      type: "entities",
      id: "no_favs",
      filter: { include: [{ label: "no_favs" }] },
    }],
  },
  element: { type: "home-overview" },
}, "no_favs");
```




```js
window.uix_inspect.strategy.test(
  [{
    op: "remove_matching",
    select: {
      in: "/sections",
      required: false,
      match: { cards: { $contains: [{ type: "heading", heading: "Favorites" }] } },
      path: "/cards",
    },
    where: { entity: { $in_entities: "no_favs" } },
  }],
  { no_favs: window.uix_inspect.entities.ids },
);
```


### Pfade mit einem JSON-Pointer-Werkzeug ausprobieren {#try-paths-in-a-json-pointer-tester}

Für ein visuelles Werkzeug die erzeugte Konfiguration aus DevTools kopieren. Öffne den [JSON-Pointer-Tester von JsonKit](https://jsonkit.com/jsonpath-tester), wähle **JSON Pointer** und füge JSON im Eingabefeld ein. `/sections/0/cards` zeigt die Karten der ersten Section. Entferne persönliche Angaben, bevor du die Konfiguration auf einer externen Seite einfügst.

```js
copy(JSON.stringify(window.uix_inspect.strategy.config, null, 2));
```


Verwende das Werkzeug für genaue Pointer und anschließend [`test()`](#test-a-patch) für Forge-Auswahlregeln und Patches.

## Sicheres Fehlerverhalten und optionale Ausgabe {#safe-failure-and-optional-output}

Bei ungültigem Pfad, ungeeignetem Zieltyp oder fehlgeschlagener Auswahl zeigt Forge einen Fehler statt eines teilweise geänderten Ergebnisses.

`select.required: false` überspringt einen optionalen Eintrag, wenn die Liste existiert, aber kein Eintrag passt. Hier wird ein optionales Statusbadge entfernt, falls es vorhanden ist. Mehrere Treffer bleiben ein Fehler.

```yaml
- op: remove
  select:
    in: /badges
    match:
      type: entity
      entity: sensor.optional_status
    required: false
```







> Deutsche Bearbeitung der [kanonischen UIX-Dokumentation von Lint-Free-Technology](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Quelle: `dev` / **9.2.0-beta.3**, Revision [6a2bad2](https://github.com/Lint-Free-Technology/uix/commit/6a2bad250e1af75b058353a22371154df23474c8), geprüft am 2026-11-27. Stabile Basis **9.1.0**, HA ab **2026.11.0**. Maßgeblich bleibt das [englische Original](https://uix.lf.technology/).
