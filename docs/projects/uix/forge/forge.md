---
title: UIX Forge
description: Deutsche Referenz für UIX Forge, Molds, Templates, Billets, Styling und Sparks
---
# UIX Forge

UIX Forge erzeugt Home-Assistant-Frontend-Elemente aus YAML und erweitert sie optional mit Sparks. Damit kannst du Karten, Zeilen, Badges, Picture-Elements, Sections, Footer und Card-Features erzeugen, ohne eine eigene Custom Card schreiben zu müssen.

::: tip In UIX Forge einhüllen
Forge ist besonders nützlich, wenn eine bestehende Karte fast passt, aber ein Button, Tooltip, Lock, Hintergrund, More-info-Bereich oder ein anderes Zusatzverhalten fehlt.

:::
## Visueller Editor – Karten und Badges {#visual-editor-cards-and-badges}

::: info Vorschau ab UIX 9.0.0-beta.2
Laut [kanonischer Revision `1badf70`](https://github.com/Lint-Free-Technology/uix/blob/1badf70befb9c9d3d7b06c0eced75af7d552aff1/docs/source/forge/forge.md) ist der visuelle Forge-Editor ab **9.0.0-beta.2** verfügbar. Diese Zusammenfassung beschreibt die Vorschau, nicht die stabile Dokumentationsbasis 8.4.0.
:::

Wähle eine HA-Karte oder ein Badge, bearbeite es im normalen HA-Editor und ergänze Forge-Templates, Sparks, UIX-Styling und Foundries. Ohne Auswahl verwendet Forge seine integrierte leere Karte bzw. sein leeres Badge. Diese automatische Typwahl und der ausgewählte Editor-Reiter werden nicht in der Dashboard-Konfiguration gespeichert.

### Native

**Choose/Change native element** wählt oder ersetzt das native Element ausdrücklich und erhält die Forge-Templatewerte. Abbrechen im Auswahlfenster wählt nichts aus; nach einer Auswahl stehen der normale HA-Abbruch und Dashboard-Rückgängig zur Verfügung. Die unvollständige Auswahl **Manual** wird erst mit einem konkreten Typ gespeichert. Der Wechsel Code/visuell ist ohne passenden visuellen HA-Editor deaktiviert.

Der eingeklappte Styling-Bereich bearbeitet den Inhalt von `element_base.uix`, ohne äußeren Schlüssel `uix:`. Äußere HA-Sichtbarkeits- und Layoutregler sind bei Karten gesperrt; verwende `forge.hidden` und `forge.grid_options`. Eine vorhandene Karte lässt sich über HA kopieren und mit **Paste configuration** im nativen Forge-Auswahldialog übernehmen. Ihre vollständige Konfiguration einschließlich eigener Templates und UIX-Stile bleibt in `element_base`; nur durch Forge veränderte Werte gehören nach `element`.

### Forge

Die vollständige Forge-YAML-Konfiguration bleibt im Code-Editor verfügbar. Die visuelle Ansicht enthält:

- **General:** auf `card`/`badge` festgelegtes `mold`, `hidden` und Grid-Zeilen/-Spalten. Templates bleiben Quelltext, Zahlen und boolesche Literale behalten ihren Typ. Ein Template für ganz `grid_options` bleibt bis zum ausdrücklichen Ersetzen durch Zeilen-/Spaltenwerte erhalten. **Control** enthält `show_error`, `template_nesting`, `delayed_hass`; der Styling-Bereich bearbeitet den Inhalt von `forge.uix`.
- **Billets:** lokale Namen mit skalaren Werten; `~` bedeutet `null`. Aufgelöste Foundry-Billets werden separat angezeigt und können überschrieben werden. Zuordnungen und Listen bleiben im Code-Editor.
- **Macros:** Name, Rückgabestatus, Parameter mit optionalen skalaren Standardwerten und Templatequelle. Zahlen, boolesche Werte und `null` bleiben erhalten. `custom_templates`-Importe bleiben im Code-Editor; aufgelöste Foundry-Makros werden separat angezeigt.
- **Sparks:** registrierten Spark und unterstützte Optionen wählen. Quellen bleiben Template-/Code-Text, YAML-Objekt/-Liste oder ausdrücklich `null`. Neue Optionen beginnen als `null`; vor dem Ersetzen vorhandener Quellen durch eine Objektzuordnung oder `null` wird nachgefragt. Vollständige Konfiguration und Entfernen bleiben im Code-Editor möglich.

Forge-, Native- und Styling-YAML-Editoren behalten den eingegebenen Text einschließlich Kommentaren und vorübergehend ungültigem YAML. Ungültiges YAML wird nicht in die Konfiguration übernommen.

### Element

Dieser Reiter bearbeitet die Überlagerung `element`; die native Basis bleibt in `element_base`. Die Pfadtabelle bietet Bearbeiten, Aktivieren/Deaktivieren und Entfernen. Neue benutzerdefinierte Pfade beginnen als aktives `null`. Der eigene Styling-Bereich bearbeitet den Inhalt von `element.uix`.

**Apply** übernimmt einen gültigen Entwurf, aktiviert ein deaktiviertes Template und lässt den Editor offen. **Apply & exit** übernimmt Änderungen und kehrt zur Tabelle zurück; ohne Änderungen kehrt es direkt zurück. **Exit** fragt bei nicht übernommenen Änderungen nach. Ungültiges YAML bleibt bearbeitbar, sperrt aber beide Übernahmeaktionen. Zeichenketten-Templates verwenden den HA-Templateeditor samt Testfunktion; die Quelle ohne zusätzliche YAML-Anführungszeichen eingeben.

**Convert to object mapping** beginnt nach Bestätigung eine leere Objektzuordnung. **Set to null** löscht den entsprechenden Basiswert ausdrücklich. Für „Basiswert verwenden“ stattdessen **Disable** oder **Remove** wählen. Eine leere Zeichenkette ist ein eigener Ersatzwert und weder `null` noch Entfernen. Deaktivieren erhält die Quelle in `element` und speichert den Pfad in `element_disabled_paths`. Ein deaktivierter Elternpfad unterdrückt den Teilbaum und bewahrt die gespeicherten Kinderzustände. Arrays und strukturerzeugende Templates werden als ganze Ersatzwerte bearbeitet.

Bei vorhandener Basis ist der oberste `type` kein Templatefeld. Aktivieren/Deaktivieren erfordert eine native Elementauswahl; gültige geerbte deaktivierte Pfade bleiben erhalten. Die Konvertierung bestehender direkter Karten-/Badge-Forges verschiebt nur `element.type` nach `element_base.type`.

### Foundry

Die Auswahl zeigt den aufgelösten `forge.mold` und `element.type`. Ein abweichender Mold ist rot, gesperrt und zuletzt gelistet. Ein abweichender Elementtyp erfordert Bestätigung und leert dann die lokale native Konfiguration; Elementwerte bleiben erhalten. Fehlerhafte, fehlende oder zyklische Vererbungsketten werden ausgelassen. Dynamische oder nicht als Zeichenkette definierte Typen sowie geerbtes `element_base` bleiben im YAML-Editor.

Eine schreibgeschützte, 200 Pixel hohe YAML-Ansicht zeigt die aufgelöste benannte Foundry einschließlich benannter Vorfahren, aber ohne globale Foundries oder lokale Kartenwerte. Ein konkreter Foundry-Typ setzt und sperrt den nativen Typ. Für einen anderen Typ die Foundry ändern oder entfernen. Globale Typanker werden ebenfalls geschützt; eine Änderung, die einen inkompatiblen globalen Typ freilegen würde, wird abgelehnt.

Ein Hinweis unter den Reitern nennt die aktive Foundry. Direkte `config.entity`-Referenzen in Forge-/Element-Templates oder der ausgewählten Foundry zeigen **Global Forge entity (in use)** für die äußere Forge-Entität. Sie wird nicht an das umhüllte Element weitergereicht. Nur über Makros erreichbare Referenzen sind nicht erkennbar; dafür die äußere `entity` in YAML setzen.

### Export

Der Reiter liefert kopierbares Foundry-YAML und erhält `foundry: <name>`, die lokale native Basis `element_base` und aktive Elementwerte einschließlich unveränderter nativer Templates. Er wertet keine Templates aus und speichert keine Foundry. Globale Foundries, äußere `entity` und deaktivierte Pfade sind ausgeschlossen; eine leere `forge.sparks`-Liste entfällt. Für Foundries `element_base` nur aus diesem Export übernehmen, nicht von Hand erzeugen. Geerbte Forge-Arrays lassen sich im visuellen Editor nicht leeren.

Zeilen, Picture-Elements, Card-Features, Cross-Context-Molds, dynamische Typen und nicht sicher visuell darstellbare Konfigurationen erfordern weiterhin YAML. Die vollständige englische Referenz steht in der oben verlinkten Revision.

## Grundstruktur

```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: tile
  entity: light.living_room
```

`forge` beschreibt, wie und in welchem Kontext das Element erzeugt wird. `element` enthält die eigentliche Home-Assistant-Konfiguration. Optional kann `uix` Styling für das erzeugte Element enthalten.

## Forge-Optionen

| Schlüssel | Typ | Templates | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `mold` | string | nein | Pflicht | Art des erzeugten Elements. Standard-Molds: `card`, `badge`, `row`, `picture-element`, `section`, `footer`, `card-feature`. Cross-Context-Molds: `card_as_row`, `card_as_badge`, `row_as_card`, `row_as_badge`, `badge_as_card`, `badge_as_row`, `badge_as_picture_element`. |
| `macros` | mapping | nein | - | Template-Makros, die allen Templates in der Forge-Konfiguration zur Verfügung stehen. Sie werden auch an `uix`-Konfigurationen in Forge und erzeugtem Element weitergegeben. |
| `billets` | mapping | nein | - | Benannte YAML-Werte als Template-Konstanten für alle Templates in der Forge-Konfiguration. |
| `hidden` | boolean | ja | `false` | Blendet das Element aus, wenn der Wert wahr ist. |
| `grid_options` | mapping | ja | - | Lovelace-Grid-Optionen wie `rows` und `columns`, nur für `mold: card`. |
| `show_error` | boolean | nein | `false` | Bei `true` wird bei Fehlern die Lovelace-Fehlerkarte angezeigt, statt das Element zu verstecken. |
| `template_nesting` | string | nein | `"<<>>"` | Vier Zeichen zum Escapen verschachtelter Templates. Standard: `<<...>>` für <code v-pre>{{...}}</code> und `<%...%>` für <code v-pre>{%...%}</code>. |
| `sparks` | list | ja | `[]` | Liste von [Spark-Konfigurationen](./sparks/), die an das erzeugte Element angehängt werden. |
| `delayed_hass` | boolean | nein | - | Verzögert die Übergabe des `hass`-Objekts, bis die Karte geladen ist. Hilft bei manchen Custom Cards, z. B. ApexCharts. |

::: warning
Nicht jede Option ist in jedem Mold sinnvoll. `grid_options` wird zum Beispiel nur bei `mold: card` beachtet.

:::
## Element-Konfiguration

Ohne Schichten enthält `element` die vollständige YAML-Konfiguration des Home-Assistant-Elements. Forge verarbeitet deren Zeichenketten als Templates. In der [geschichteten Konfiguration](#layered-configuration) enthält `element` dagegen nur die von Forge verarbeitete Überlagerung; die elementeigene Basis steht in `element_base`.

::: details Forge-Beispiel
```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: tile
  entity: sensor.outdoor_temperature
```

:::
Bei `mold: card` entspricht `element` einer normalen Lovelace-Karte. Bei `mold: row` entspricht es einer Entity-Row. Bei `mold: badge` entspricht es einem Badge.

### Entity-Konfiguration im Element

Viele Home-Assistant-Elemente erwarten `entity`. Forge reicht diese Konfiguration unverändert weiter.

```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: tile
  entity: light.kitchen
  name: Kueche
```

### Blank-Card-Konfiguration

Eine Blank Card ist nützlich, wenn du ein leeres Ziel für Sparks oder UIX-Styling brauchst.

```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: custom:uix-forge-blank-card
```

Mit Inhalt:

```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: custom:uix-forge-blank-card
  cards:
    - type: tile
      entity: light.living_room
    - type: tile
      entity: sensor.living_room_temperature
```

Mit Sparks:

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: grid
      columns: 2
      gap: 8
element:
  type: custom:uix-forge-blank-card
  cards:
    - type: tile
      entity: light.living_room
    - type: tile
      entity: light.kitchen
```

::: tip
Bei Blank Cards zeigen viele Sparks standardmäßig auf `uix-forge-blank-card $ div.content`.

:::
### Blank-Badge-Konfiguration {#blank-badge-config}

In der Vorschau mit `mold: badge` und ohne Elementtyp verwendet Forge automatisch `uix-forge-blank-badge`. `element.icon` und `element.label` liefern den Inhalt; nur ein Icon ergibt ein Badge ohne Beschriftung. Ohne beides erscheint ein Hinweis zum Ergänzen von Icon, Label oder `forge.sparks`. Bei konfigurierten Sparks entfällt der Hinweis; sie adressieren eine leere `div` im Standard-Slot. Die automatisch gewählte Typangabe wird nicht im Dashboard gespeichert.

<a id="layered-configuration"></a>
<a id="keep-the-elements-configuration-in-element_base"></a>
## Geschichtete Konfiguration

::: info Vorschau: verfügbar ab UIX 9.0.0-beta.0
Diese Funktion gehört zum aktuellen `dev`-Stand und nicht zur stabilen Version 8.4.0.
:::

Die geschichtete Konfiguration bettet ein Element ein, das eigene Templates besitzt. Sie funktioniert mit allen Forge-Molds und benötigt keinen visuellen Editor. Sobald die aufgelöste Konfiguration `element_base` enthält, verwendet Forge diesen Modus.

Die aktuelle Vorschau 9.0.0-beta.2 präzisiert die Typregel: Ein konkreter **geerbter** Foundry-`element.type` darf als Typanker dienen, wenn die lokale `element_base.type` exakt dieselbe Zeichenkette ist. Forge entfernt diesen passenden geerbten Typ vor dem Auflegen der übrigen Werte. Ein lokales `element.type`, dynamische Typen oder Abweichungen bleiben ungültig. Entfernen eines Element-Templates fragt vor dem Löschen der Quelle nach.

`element_base` enthält die vollständige elementeigene Basis. Forge reicht ihre Template-Zeichenketten unverändert weiter, ohne sie zu erkennen, auszuwerten, umzuschreiben oder Escape-Zeichen zu verlangen. `element` enthält die Forge-Überlagerung; deren aktive Werte werden nach den üblichen Forge-Template-Regeln verarbeitet.

```yaml
type: custom:uix-forge
entity: light.kitchen
forge:
  mold: card
element_base:
  type: markdown
  # Dieses Template gehört der Markdown-Karte.
  content: |
    ## Temp: {{ states('sensor.kitchen_sensor') }}
element:
  title: "{{ config.entity }}"
```

Mappings in `element` werden rekursiv über `element_base` gelegt. Skalare und Arrays ersetzen den Wert an ihrem Pfad. `null` ist ein normaler Wert und kein Löschbefehl; ein leeres Array leert das Basis-Array ausdrücklich. `type` gehört in `element_base` und darf nicht überschrieben werden. Ein Forge-Template, das ein Objekt oder Array zurückgibt, ersetzt sein vollständiges Ziel, statt es mit der Basis zusammenzuführen. Für strukturelle Ergebnisse gib JSON aus, beispielsweise mit `| tojson`.

| Schlüssel auf oberster Ebene | Rolle im Schichtenmodus |
| --- | --- |
| `element_base` | Erforderliche elementeigene Basis mit `type`; ihre Templates gehen unverändert an das eingebettete Element. |
| `element` | Optionale Forge-Überlagerung als Mapping. Aktive Zeichenketten werden als Forge-Templates verarbeitet und über die Basis gelegt. Sie darf `type` nicht setzen. |
| `element_disabled_paths` | Optionale, nur lokal erlaubte Liste inaktiver Overlay-Pfade. Sie erhält Quellen für die UI-Bearbeitung und ist in Foundries nicht erlaubt. |

::: tip Native Sichtbarkeits-Templates
Lege die native `visibility`-Konfiguration einer Karte in `element_base` ab. Ihre Template-Bedingungen gehen unverändert an Home Assistant und benötigen weder Nesting noch Ignore-Markierungen. Das ist unabhängig von `forge.hidden`.
:::

```yaml
element_base:
  type: entities
  entities:
    - light.kitchen
    - light.dining_room
element:
  # Das Template-Ergebnis ersetzt das komplette Array.
  entities: "{{ integration_entities('light') | list | tojson }}"
```

### Deaktivierte Overrides

Alle `element`-Werte sind standardmäßig aktiv. `element_disabled_paths` erhält einen Quellwert, ohne ihn anzuwenden. Jeder Pfad ist eine Liste von Mapping-Schlüsseln; dadurch bleiben Schlüssel mit `.` eindeutig. Ein deaktivierter Elternpfad deaktiviert den ganzen Teilbaum. Gespeicherte Kind-Auswahlen wirken wieder, sobald der Elternpfad aus der Liste entfernt wird.

```yaml
element:
  name: "{{ states('sensor.room_label') }}"
  tap_action:
    action: more-info
    confirmation:
      text: Confirm
element_disabled_paths:
  - [name]
  - [tap_action, action]
```

Die Quellen bleiben erhalten, das erzeugte Element verwendet aber `name` und `tap_action.action` aus der Basis. Das aktive Mapping `tap_action.confirmation` wird weiterhin mit der Basis zusammengeführt. Jeder deaktivierte Pfad muss auf einen Wert im aufgelösten Overlay zeigen. Array-Einträge sind Ersetzungseinheiten und können nicht einzeln deaktiviert werden.

### Foundries und Template-Kontext

Foundries dürfen `element_base` und `element` bereitstellen, niemals `element_disabled_paths`. Globale und benannte Foundries folgen derselben Reihenfolge:

```text
global → global_<mold> → geerbte/benannte Foundry → lokale Konfiguration
```

Foundry- und lokale `element_base`-Fragmente ergeben die aufgelöste Basis; ihre `element`-Fragmente ergeben separat die aufgelöste Forge-Überlagerung. Die lokalen `element_disabled_paths` werden erst danach angewendet. So kann eine Karte einen Foundry-Wert deaktivieren, ohne die Foundry zu ändern.

```yaml
uix_foundries:
  kitchen_tile:
    forge:
      mold: card
    element:
      type: markdown
      title: "{{ config.entity }}"

# Dashboard-Karte: native Einstellungen lokal, Forge-Werte aus der Foundry.
type: custom:uix-forge
foundry: kitchen_tile
element_base:
  type: markdown
  content: |
    ## {{ states('sensor.room_label') }}
element:
  entity: light.kitchen
```

In Forge-Templates enthält `config.element_base` die aufgelöste Basis und `config.element` die aufgelöste Overlay-Quelle vor der Auswertung. Forge setzt daraus die endgültige Elementkonfiguration zusammen. Die `uix`-Mappings beider Schichten werden dabei zusammengeführt; UIX Styling verarbeitet ihre Templates anschließend nach seinen üblichen Regeln.

## Template-Variablen und Makros

| Kontext | Template-Variablen |
| --- | --- |
| Templates in Forge und ungeschichtetem `element`, außer `uix`-Styling | Forge-Konfiguration: `config.forge`; Element-Konfiguration: `config.element`; `config.entity`, falls in globaler `uix-forge`-Konfiguration enthalten. |
| Templates im geschichteten `element`, außer `uix`-Styling | `config.forge`; aufgelöste Basis: `config.element_base`; Overlay-Quelle: `config.element`; `config.entity`, falls enthalten. |
| Templates im Forge-`uix`-Styling | `config.forge`; `config.element` ist die vollständige aufgelöste Elementkonfiguration oder im Schichtenmodus die aufgelöste Forge-Überlagerung; im Schichtenmodus zusätzlich `config.element_base`; `config.entity`, falls enthalten. |
| Templates im `uix`-Styling des Elements | Forge-Konfiguration nicht verfügbar; Element-Konfiguration als `config`; `config.entity`, falls enthalten. |

::: tip
Makros eignen sich für wiederholte CSS- oder YAML-Schnipsel, etwa Farben, Zustandslabels oder DOM-Pfade.

:::
::: warning
In VitePress muss Jinja-Syntax in Markdown-Beispielen escaped werden. In echtem Home-Assistant-YAML schreibst du natürlich normale Jinja-Klammern.

:::
### Vollbeispiel mit Makro

```yaml
type: custom:uix-forge
forge:
  mold: card
  macros:
    state_color: |
      {% macro state_color(entity) -%}
      {{ 'var(--success-color)' if is_state(entity, 'on') else 'var(--disabled-color)' }}
      {%- endmacro %}
element:
  type: tile
  entity: light.living_room
uix:
  style: |
    ha-card {
      border-color: {{ state_color(config.element.entity) }};
    }
```

### Billets

Billets sind benannte YAML-Werte, die in Templates als Konstanten genutzt werden können. Sie sind praktisch für Defaults, Farben, Entity-IDs oder Textbausteine.

::: warning
Billets sind Konfiguration, keine sichere Geheimnisablage. Für sensible Werte nutze Home-Assistant-Secrets oder passende Backend-Mechanismen.

:::
```yaml
type: custom:uix-forge
forge:
  mold: card
  billets:
    main_entity: light.living_room
    accent_color: var(--primary-color)
element:
  type: tile
  entity: "{{ main_entity }}"
uix:
  style: |
    ha-card {
      border-color: {{ accent_color }};
    }
```

#### Billet-Typen

| YAML-Typ | Beispiel | Jinja2-Typ | Nutzung im Template |
| --- | --- | --- | --- |
| Leer (`~` oder `null`) | `my_billet: ~` | `none` | <code v-pre>{{ my_billet }}</code> ergibt leer |
| String | `my_billet: hello` | `str` | <code v-pre>{{ my_billet }}</code> ergibt `hello` |
| Zahl | `my_billet: 42` | `int` oder `float` | <code v-pre>{{ my_billet + 1 }}</code> ergibt `43` |
| Boolean | `my_billet: true` | `bool` | <code v-pre>{% if my_billet %}...{% endif %}</code> |
| Liste | `my_billet: [1, 2, 3]` | `list` | <code v-pre>{{ my_billet &#124; join(', ') }}</code> |
| Mapping | `my_billet: {a: 1}` | `dict` | <code v-pre>{{ my_billet.a }}</code> |

#### Billet-Interpolation

Billets können andere Billets referenzieren.

```yaml
forge:
  billets:
    room: living_room
    entity: "light.{{ room }}"
element:
  type: tile
  entity: "{{ entity }}"
```

Mehrere Werte können zusammengesetzt werden:

```yaml
forge:
  billets:
    domain: sensor
    object_id: outdoor_temperature
    entity: "{{ domain }}.{{ object_id }}"
```

::: note Zirkuläre Referenzen
Billets dürfen sich nicht gegenseitig endlos referenzieren. Halte Abhängigkeiten einfach und eindeutig.

:::
#### Billets und Foundries

Foundries können Billets definieren, die einzelne Forge-Instanzen überschreiben. Das ist der bevorzugte Weg für wiederverwendbare Kartenmuster.

## Templates im Element ignorieren

Manche erzeugten Elemente enthalten selbst Jinja-ähnliche Syntax. Ohne Schichten oder im Forge-Overlay musst du diese Templates ignorieren oder verschachteln, damit Forge sie nicht zu früh auswertet. In `element_base` gehen native Templates unverändert weiter und benötigen weder `template_nesting` noch Ignore-Markierungen.

```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: markdown
  content: |
    << states('sensor.outdoor_temperature') >>
```

::: warning Templates ignorieren und mehrere Forge-Schichten
Wenn mehrere Forge-Schichten ineinander liegen, braucht jede zusätzliche Ebene ein weiteres Paar Nesting-Zeichen.

:::
### Template-Nesting

Mit `template_nesting` legst du fest, welche Zeichen für verschachtelte Jinja-Ausdrücke verwendet werden.

```yaml
forge:
  template_nesting: "<<>>"
element:
  type: markdown
  content: "<< states('sensor.outdoor_temperature') >>"
```

#### Mehrere Verschachtelungsebenen

Bei zwei Ebenen nutzt du ein weiteres Klammerpaar, zum Beispiel `<<< ... >>>` für den inneren Ausdruck.

#### Template-Nesting und Makros

Makros können ebenfalls verschachtelte Templates ausgeben. Wichtig ist, dass die Ebene, die das Template auswerten soll, die Syntax erkennt.

::: tip
Wenn ein Template zu früh ausgewertet wird, ist das fast immer ein Nesting-Problem.

:::
#### Billets in verschachtelten Templates

Billets stehen auch in verschachtelten Templates zur Verfügung, sofern sie auf der auswertenden Ebene sichtbar sind.

::: note Von decluttering-card kommend?
Forge deckt viele Muster ab, die sonst mit `decluttering-card` gebaut werden. Der wichtigste Unterschied: Forge erzeugt echte Home-Assistant-Elemente und kann zusätzlich Sparks anwenden.

:::
```yaml
type: custom:uix-forge
forge:
  mold: card
  billets:
    entity: light.living_room
element:
  type: tile
  entity: "{{ entity }}"
```

```jinja
{% if is_state(entity, 'on') %}
  eingeschaltet
{% endif %}
```

::: tip
Halte Vorlagen klein. Wenn ein Template schwer lesbar wird, lagere wiederholte Teile in Makros oder Foundries aus.

:::
### Nutzung mit Auto-Entities

Forge kann mit `custom:auto-entities` kombiniert werden, wenn automatisch gefundene Entities als erzeugte Karten, Reihen oder Badges eingesetzt werden sollen.

```yaml
type: custom:auto-entities
card:
  type: vertical-stack
card_param: cards
filter:
  include:
    - domain: light
      options:
        type: custom:uix-forge
        forge:
          mold: card
        element:
          type: tile
          entity: this.entity_id
```

::: tip
Bei Auto-Entities ist es besonders wichtig, mit Fallbacks zu arbeiten, weil nicht jede Entity dieselben Attribute besitzt.

:::
Die aktualisierte Originalanimation zeigt eine Auto-Entities-Karte mit Forge und Tooltip:

![Originalbeispiel für Forge mit Auto-Entities](../assets/page-assets/forge/forge-auto-entities.gif)

## UIX-Styling

Forge kann sowohl die erzeugte Karte als auch deren innere Elemente mit UIX stylen.

Mit `forge.uix` stylst du den Forge-Wrapper. Seine Templates erhalten `config.forge`, `config.element` und `uixForge`. Im Schichtenmodus ist `config.element` die aufgelöste Forge-Überlagerung und `config.element_base` die aufgelöste Basis; ansonsten enthält `config.element` die vollständige aufgelöste Elementkonfiguration. `uixForge` enthält die Spark-Variablen. Im `uix`-Styling des erzeugten Elements steht dagegen die endgültige Elementkonfiguration als `config` bereit.

```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: tile
  entity: light.living_room
uix:
  style: |
    ha-card {
      border: 1px solid var(--primary-color);
    }
```

### Element-Styling

`uix` auf oberster Ebene stylt das Forge-Ergebnis. `uix` innerhalb von `element` gehört zur eigentlichen Elementkonfiguration.

::: warning
Die verfügbaren Template-Variablen unterscheiden sich je nach Ebene. Im Element-`uix` ist die Elementkonfiguration als `config` sichtbar, nicht als `config.element`.

:::
```yaml
type: custom:uix-forge
forge:
  mold: card
element:
  type: tile
  entity: light.living_room
  uix:
    style: |
      ha-card {
        color: var(--primary-text-color);
      }
```

### Theme-Styling

UIX-Themes können Forge-Molds gezielt stylen. Nutze die bekannten Variablen wie `uix-card`, `uix-row`, `uix-badge` oder spezifischere Klassen.

## Sections

Forge kann Sections für die neue Dashboard-Section-Ansicht erzeugen.

```yaml
type: custom:uix-forge
forge:
  mold: section
element:
  type: heading
  heading: Wohnzimmer
```

```yaml
# Nur Hauptkonfiguration fuer Sections. Visibility wird nicht unterstuetzt.
type: custom:uix-forge
forge:
  mold: section
element:
  type: grid
  cards:
    - type: tile
      entity: light.living_room
```

::: warning
Section-Konfiguration folgt den Home-Assistant-Regeln für Sections. Nicht jede Kartenoption ist dort gültig.

:::
## Footer

Mit `mold: footer` kann Forge einen Footer erzeugen, der unten im Viewport sitzt.

::: note
Footer sind für kompakte, dauerhaft sichtbare Bedienelemente gedacht. Sie sollten nicht zu viel Inhalt aufnehmen.

:::
| Schlüssel | Typ | Templates | Standard | Beschreibung |
| --- | --- | --- | --- | --- |
| `max_width` | string | nein | `600` | Maximale Breite des Footers in Pixeln. |

```yaml
type: custom:uix-forge
forge:
  mold: footer
  max_width: 600
element:
  type: horizontal-stack
  cards:
    - type: button
      entity: light.living_room
    - type: button
      entity: light.kitchen
```

Footer-Variablen:

| Variable | Standard | Beschreibung |
| --- | --- | --- |
| `--uix-forge-footer-border-width` | `1px` | Rahmenbreite der erzeugten Karte im Footer. |
| `--uix-forge-footer-bottom` | `var(--ha-space-2)` | Abstand vom unteren Viewport-Rand. |
| `--uix-forge-footer-padding` | `0 var(--ha-space-2)` | Padding des Footer-Containers. |

### Visibility

```yaml
type: custom:uix-forge
forge:
  mold: footer
  hidden: "{{ is_state('input_boolean.hide_footer', 'on') }}"
element:
  type: button
  entity: input_boolean.hide_footer
```

## Card Features

Mit `mold: card-feature` können Card-Feature-Elemente erzeugt werden, die in Cards verwendet werden.

```yaml
type: custom:uix-forge
forge:
  mold: card-feature
element:
  type: toggle
```

In einer Tile Card:

```yaml
type: tile
entity: light.living_room
features:
  - type: custom:uix-forge
    forge:
      mold: card-feature
    element:
      type: toggle
```

## Cross-Context-Molds

Cross-Context-Molds erzeugen ein Element in einem Kontext, lassen es aber in einem anderen Kontext auftreten.

| Mold | Erzeugt | Verhält sich wie |
| --- | --- | --- |
| `card_as_row` | `hui-card` | Row in `entities` oder `fold-entity-row` |
| `card_as_badge` | `hui-card` | Badge in einem Badge-Container |
| `row_as_card` | Row-Element | Karte im Kartengrid |
| `row_as_badge` | Row-Element | Badge in einem Badge-Container |
| `badge_as_card` | `hui-badge` | Karte im Kartengrid |
| `badge_as_row` | `hui-badge` | Row in `entities` oder `fold-entity-row` |
| `badge_as_picture_element` | `hui-badge` | Picture-Element in einer Picture-Elements-Karte |

### `card_as_row`: Karte als Zeile einbetten

```yaml
type: entities
entities:
  - type: custom:uix-forge
    forge:
      mold: card_as_row
    element:
      type: tile
      entity: light.living_room
```

### Badge als Picture-Element einbetten

```yaml
type: picture-elements
image: /local/floorplan.png
elements:
  - type: custom:uix-forge
    forge:
      mold: badge_as_picture_element
    element:
      type: entity
      entity: light.living_room
    style:
      top: 40%
      left: 60%
```

::: tip Visibility
Wenn Sichtbarkeit benötigt wird, prüfe zuerst, ob Home Assistant sie in diesem Kontext direkt unterstützt. Forge kann Elemente ausblenden, aber manche Container erwarten trotzdem bestimmte Elementformen.

:::
## Praxis: welche Mold für welchen Zweck?

| Ziel | Geeignete Mold | Typischer Einsatz |
| --- | --- | --- |
| Normale Dashboard-Karte | `card` | Tile, Entities, Markdown, Map, Custom Cards |
| Zeile in Entities-Karte | `row` | Entity-Row, Template-Entity-Row, Fold-Entity-Row |
| Badge im Kopfbereich | `badge` | Entity-Badge, Status-Badge, Shortcut-Badge |
| Element in Picture-Elements | `picture-element` | Marker, Badge, Button auf Grundriss |
| Abschnitt in Sections View | `section` | Heading, Grid oder Section-Inhalt |
| Fester unterer Bereich | `footer` | Schnellaktionen, Navigation, Raumumschalter |
| Feature in Tile Card | `card-feature` | Toggle, Slider oder andere Feature-Elemente |

Cross-Context-Molds nutzt du nur, wenn Home Assistant ein Element in einem anderen Kontext erwartet als die Karte, die du eigentlich erzeugen möchtest. Das ist mächtig, aber auch empfindlicher gegen Änderungen im Frontend.

## Komplettes Forge-Beispiel

Dieses Beispiel kombiniert Template, Billets, Sparks und UIX-Styling:

```yaml
type: custom:uix-forge
forge:
  mold: card
  grid_options:
    columns: 8
    rows: 1
  billets:
    entity: light.living_room
    label: Wohnzimmer
  sparks:
    - type: tooltip
      for: hui-tile-card $ ha-tile-icon
      content: "{{ label }}: {{ states(entity) }}"
    - type: button
      after: hui-tile-card $ ha-tile-info
      label: Umschalten
      entity: "{{ entity }}"
      tap_action:
        action: toggle
    - type: overlay-icon
      for: hui-tile-card $ ha-tile-icon
      icon: "{{ 'mdi:check' if is_state(entity, 'on') else 'mdi:minus' }}"
      icon_background: "{{ 'var(--success-color)' if is_state(entity, 'on') else 'var(--disabled-color)' }}"
element:
  type: tile
  entity: "{{ entity }}"
  name: "{{ label }}"
uix:
  style: |
    ha-card {
      border: 1px solid var(--divider-color);
    }
    ha-button {
      margin-left: auto;
    }
```

## Fehleranzeige und Fehlersuche

Mit `show_error: true` zeigt Forge bei Problemen die Lovelace-Fehlerkarte. Das ist beim Entwickeln hilfreich, weil falsche Molds, ungültiges YAML oder fehlende Entities sonst nur als verschwundenes Element wirken können.

```yaml
type: custom:uix-forge
forge:
  mold: card
  show_error: true
element:
  type: tile
  entity: sensor.does_not_exist
```

Nach dem Debuggen kannst du `show_error` wieder entfernen oder auf `false` setzen.

## `hidden` mit Templates

`hidden` kann als Boolean oder Template genutzt werden.

```yaml
type: custom:uix-forge
forge:
  mold: card
  hidden: "{{ not is_state('input_boolean.show_lights', 'on') }}"
element:
  type: tile
  entity: light.living_room
```

Bei Template-Ausdrücken sollte das Ergebnis klar wahr oder falsch sein. Nutze einfache Bedingungen und Fallbacks.

## `grid_options`

`grid_options` wird an Lovelace weitergegeben, wenn Forge eine Karte erzeugt.

```yaml
type: custom:uix-forge
forge:
  mold: card
  grid_options:
    columns: 6
    rows: 2
element:
  type: tile
  entity: sensor.energy_today
```

Das beeinflusst die Position und Größe der Karte in Home Assistants Grid-Layout, nicht das interne Layout der Karte. Für internes Layout ist der [Grid Spark](./sparks/grid) gedacht.

## `delayed_hass`

Einige Custom Cards reagieren empfindlich, wenn `hass` sehr früh gesetzt wird. `delayed_hass` wartet, bis die Karte geladen ist.

```yaml
type: custom:uix-forge
forge:
  mold: card
  delayed_hass: true
element:
  type: custom:apexcharts-card
  graph_span: 24h
  series:
    - entity: sensor.energy_today
```

Setze diese Option nur, wenn du sie wirklich brauchst, zum Beispiel bei Konsolenfehlern oder fehlerhaft initialisierten Custom Cards.

## Sparks kombinieren

Sparks werden in der Reihenfolge verarbeitet, in der sie in `forge.sparks` stehen. Wenn ein Spark ein Element erzeugt und ein anderer Spark dieses Element verwenden soll, muss der erzeugende Spark vorher stehen.

```yaml
forge:
  mold: card
  sparks:
    - type: button
      after: hui-tile-card $ ha-tile-info
      label: Mehr
      entity: light.living_room
      tap_action:
        action: more-info
    - type: tooltip
      for: hui-tile-card $ ha-button
      content: Details oeffnen
```

## Forge mit Reihen

`mold: row` erzeugt eine Zeile für Karten, die Row-Elemente erwarten.

```yaml
type: entities
entities:
  - type: custom:uix-forge
    forge:
      mold: row
      sparks:
        - type: tooltip
          content: Direkte UIX-Zeile
    element:
      type: custom:template-entity-row
      entity: light.living_room
      name: Wohnzimmer
```

## Forge mit Badges

`mold: badge` erzeugt ein Badge für den Dashboard-Kopfbereich.

```yaml
badges:
  - type: custom:uix-forge
    forge:
      mold: badge
      sparks:
        - type: tooltip
          content: Haustuerstatus
    element:
      type: entity
      entity: binary_sensor.front_door
```

## Forge mit Picture-Elements

```yaml
type: picture-elements
image: /local/floorplan.png
elements:
  - type: custom:uix-forge
    forge:
      mold: picture-element
      sparks:
        - type: lock
          locks:
            - confirmation: Licht schalten?
    element:
      type: state-icon
      entity: light.living_room
    style:
      top: 45%
      left: 55%
```

## Empfehlungen

- Starte mit einer minimalen Forge-Konfiguration und füge danach Sparks hinzu.
- Nutze `show_error: true`, solange du an einer neuen Forge-Struktur arbeitest.
- Halte DOM-Selektoren so genau wie nötig und so kurz wie möglich.
- Verwende Billets für Werte, die pro Instanz austauschbar bleiben sollen.
- Verwende Foundries, sobald du dieselbe Forge-Struktur mehrfach brauchst.
- Nutze Cross-Context-Molds nur dort, wo Home Assistant wirklich einen anderen Kontext verlangt.

## Verwandte Seiten

- [Foundries](./foundries) für wiederverwendbare Forge-Vorlagen.
- [Sparks](./sparks/) für optionale Verhalten.
- [DOM-Navigation](../concepts/dom) für Selektoren mit Shadow-DOM-Wechseln.
- [Templates](../using/templates) für Jinja-Variablen, Makros und Hash-Werte.

## Präzisierungen zum englischen Referenzmodell

- Die Standard-Molds sind `card`, `badge`, `row`, `picture-element`, `section`, `footer` und `card-feature`. Kontextwechsel unterstützen `card_as_row`, `card_as_badge`, `row_as_card`, `row_as_badge`, `badge_as_card`, `badge_as_row` und `badge_as_picture_element`. Sie ersetzen fragile Konstruktionen mit `custom:hui-element` bzw. `custom:hui-xxx-card`; `forge.hidden` funktioniert auch mit `card_as_row`.
- `grid_options.rows` und `grid_options.columns` behalten numerische Literale als Zahlen. Ganze Templates für `grid_options` bleiben bis zum ausdrücklichen Ersetzen erhalten. Theme-Makros gelten nur für UIX-Styling; global verfügbare Forge-Makros gehören in `forge.macros` einer globalen Foundry.
- Bei Blank Cards zeigt `element.title` nur den Titel; `element.clear` macht die Karte transparent. Ohne Spark-Inhalt hat der Inhaltscontainer die Höhe `var(--row-height, 56px)`; ein vorhandenes, aber leeres Geschwisterelement kann sie auf `0px` reduzieren. `--uix-forge-blank-card-height` überschreibt die Höhe ausdrücklich.
- Billets gehören zu `forge.billets` und werden mit ihrem nativen YAML-/Jinja2-Typ injiziert. Der Kommentar <code v-pre>{# uix-forge.ignore #}</code> lässt Forge das betreffende Template unverändert durchreichen. Billet-Interpolation mit `{billet_name}` ist nur in Billet-Wertstrings erlaubt, nicht als Ersatz für Jinja2-Ausdrücke innerhalb von `<<...>>`.
- Bei `auto-entities` als äußerer Erzeuger wird eine übergebene `entities`-Liste an die Karte durchgereicht, steht aber nicht in `config.element.entities`. Bei Forge als einzelner Entity-Karte steht die übergebene ID in `config.entity`; sie muss bei Bedarf ausdrücklich im Element-Template eingesetzt werden.
- Bei einer geschmiedeten Section stehen `row_span`, `column_span` und `background` direkt an der Konfigurationswurzel; diese drei Werte unterstützen **keine Templates**. Sichtbarkeit wird über `forge.hidden` gesteuert. Im visuellen Dashboard-Editor zeigt ein roter gestrichelter Rahmen die YAML-konfigurierte Section an; ihre Karten sind dort nur Vorschauen und werden über YAML bearbeitet. Der Footer verwendet dagegen ein fixiertes `<hui-view-footer>` und `display: contents`; er belegt keinen Grid-Platz. Seine Zentrierung bezieht sich auf das Fenster. Asymmetrisches `--uix-forge-footer-padding` gleicht das bei Bedarf aus.
