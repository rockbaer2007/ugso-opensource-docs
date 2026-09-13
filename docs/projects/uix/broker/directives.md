---
title: Directives
description: Deklarative UIX-Broker-Operationen auf ein ausgewähltes Element anwenden.
---
# Directives

Direktiven laufen nacheinander, nachdem alle Regeln einer Interaktion passen. Jede Direktive führt eine konfigurierte Operation aus und nutzt standardmäßig den Interaction Anchor oder, falls unterstützt, einen ausdrücklich gesetzten Direktiven-Anchor. Außer `block` kann eine Direktive eigene `rules` haben; sie läuft dann nur, wenn alle Regeln passen. Andernfalls überspringt Broker sie und fährt mit der nächsten Direktive fort.

- [Block](#block): Standardaktion und Propagation des auslösenden Browser-Events verhindern.
- [Property](#property): JavaScript-Objekt-Property setzen oder entfernen.
- [Event](#event): Ein `CustomEvent` auslösen.
- [Call](#call): Eine Element-Methode aufrufen.
- [Button](#button): Einen interaktiven Home-Assistant-Button einfügen.
- [Tile icon](#tile-icon): Ein interaktives Home-Assistant-Tile-Icon einfügen.
- [Tooltip](#tooltip): Einen gestalteten Tooltip an ein Element hängen.
- [Action](#action): Home-Assistant-, Frontend- oder UIX-Action ausführen.
- [Template](#template): Ein Jinja2-Template einmal rendern und das Ergebnis speichern.
- [JavaScript](#javascript): JavaScript synchron auswerten und den Rückgabewert speichern.
- [Wait](#wait): Die nächste Direktive verzögern.

## Direktiven-Regeln

Füge `rules` zu jeder Direktive außer `block` hinzu, um nur diese Direktive zu konditionieren. Die Syntax entspricht den [Interaktionsregeln](./rules). Bei `property`, `event`, `call`, `button`, `tile-icon` und `tooltip` prüfen Host-Element-Regeln standardmäßig den aufgelösten Direktiven-Anchor. Bei `action` und `wait` prüfen sie den Interaction Anchor. Ein eigener `anchor` innerhalb einer Regel bleibt relativ zu diesem Standard-Anchor oder kann wie gewohnt absolut sein.

```yaml
directives:
  - type: property
    set: config.mode
    value: advanced
  - type: call
    method: openAdvancedEditor
    rules:
      - type: captured
        path: allow_advanced
        match: true
```

`panel`-Regeln lesen den aktuellen Panel-Zustand, wenn die Direktive erreicht wird. So kann eine frühere Direktive unabhängig vom aktuellen Panel laufen, während eine spätere Direktive nur bei passendem Panel ausgeführt wird.

`block` akzeptiert keine Direktiven-Regeln. Lege die Bedingung in die `rules` der Interaktion, damit das Event nur dann synchron blockiert wird, wenn die komplette Interaktion passt.

## Block

`block` ruft `preventDefault()` und `stopImmediatePropagation()` auf dem auslösenden Browser-Event auf.

```yaml
- type: block
```

`block` ist nur in den Realms `browser` und `shortcut` verfügbar. Interaction Anchor und Host-Element-Regel-Anchors müssen synchron auflösbar sein. Ist ein benötigter `select_tree`-Anchor nicht sofort vorhanden, überspringt UIX Broker die komplette Interaktion. Eine `block`-Direktive wird vor den übrigen Direktiven angewendet, auch wenn sie später in der Liste steht.

## Direktiven-Anchors

`property`, `event`, `call`, `button`, `tile-icon` und `tooltip` nutzen standardmäßig den Interaction Anchor. Jede dieser Direktiven kann den Standard mit eigener `anchor`-Konfiguration überschreiben. Ein einfacher String ist relativ zum Interaction Anchor, ein String mit `&` am Anfang ist ein kompakter absoluter `select_tree`-Pfad ab `document`, und `{ select_tree: ... }` ist die entsprechende lange absolute Form.

```yaml
directives:
  - type: property
    anchor: "$ ha-dialog"
    set: withoutHeader
    value: true
  - type: event
    anchor: "&home-assistant $$ ha-automation-sidebar"
    name: broker-sidebar-event
  - type: call
    anchor:
      select_tree: "home-assistant $ ha-more-info-dialog"
    method: closeDialog
```

Nutze den Konsolenhelfer `uix_broker_path($0)`, um im Browser einen relativen Direktiven-Anchor-Pfad zu finden.

Siehe [Interaction Anchors](./interaction-anchors#anchors-in-regeln-und-direktiven) für die Auswahlformate.

Siehe [Pfade in der Browser-Konsole finden](./interaction-anchors#pfade-in-der-browser-konsole-finden) für weitere Informationen zu den verfügbaren Konsolenhelfern.

## Property

Die `property`-Direktive verändert das JavaScript-Objekt des gewählten Anchors. `set` nimmt einen dot-separierten Property-Pfad, erzeugt fehlende Zwischenebenen als einfache Objekte und weist den Wert der letzten Property zu. `clear` nimmt denselben Pfadtyp und löscht nur die letzte Property; übergeordnete Objekte bleiben erhalten.

```yaml
- type: property
  set: config.heading
  value: New title
- type: property
  clear: config.icon
```

Werte können Captured Data oder ein vorheriges `template`- oder `javascript`-Ergebnis referenzieren. `@captured` steht für das komplette Captured-Data-Objekt, `@captured.path` für einen Wert an diesem dot-separierten Pfad. Array-Indizes können dot notation (`items.0`) oder Klammern (`items[0]`) nutzen; für Objekt-Properties mit Satzzeichen funktionieren quoted bracket keys wie `settings['icon-color']`. Die Referenz wird vor dem Setzen ersetzt und muss in YAML in Anführungszeichen stehen, weil sie mit `@` beginnt.

```yaml
- type: property
  set: config.entity
  value: "@captured.entity_id"
```

`template`- und `javascript`-Direktiven speichern ihren Wert unter ihrer `id`. Eine spätere Direktive kann `@id` oder eine Property wie `@id.path` verwenden; der Wert behält seinen ursprünglichen Typ, einschließlich Objekten und Arrays. Referenzen belegen einen kompletten YAML-Wert. Broker interpoliert sie nicht in längere Strings.

## Event

`event` löst ein `CustomEvent` aus. `target` ist standardmäßig `anchor`, also der gewählte Direktiven-Anchor oder der Interaction Anchor, wenn kein Direktiven-Anchor gesetzt ist. Setze `target: window` oder `target: document`, um global auszulösen; diese Ziele verwenden und lösen keinen event-spezifischen Direktiven-Anchor auf. `bubbles` und `composed` sind standardmäßig `false`, passend zur DOM-API.

```yaml
- type: event
  name: broker-demo-event
  bubbles: true
  composed: true
  data:
    entity: light.bed_light
```

```yaml
- type: event
  target: window
  name: broker-window-event
  data:
    source: uixBroker
- type: event
  target: document
  name: broker-document-event
```

Mit `capture_data: true` werden Captured Data in das neue Event übernommen. Das ausgehende `detail` beginnt mit den Captured Data der auslösenden Interaktion und überschreibt sie anschließend flach mit Werten aus `data`. `capture_data` ist nur für die `event`-Direktive verfügbar.

```yaml
- type: event
  name: broker-forwarded-event
  capture_data: true
  data:
    source: uixBroker
```

Setze `capture_data: deep`, wenn verschachtelte einfache Objekte zusammengeführt werden sollen. Direktiven-`data` gewinnt bei Konflikten; Arrays und nicht einfache Objekte werden vollständig ersetzt. `capture_data: true` bleibt unverändert.

```yaml
- type: event
  name: broker-forwarded-event
  capture_data: deep
  data:
    params:
      source: uixBroker
```

## Call

`call` ruft eine Methode auf dem gewählten Anchor auf. `method` akzeptiert einen sicheren dot-separierten Methodenpfad und erhält das `this`-Binding des Methodenobjekts. `args` muss, falls vorhanden, ein Array sein und unterstützt Captured-Data-Ersetzung.

```yaml
- type: call
  method: focus
- type: call
  method: setSelectionRange
  args: [0, 5]
```

## Button

`button` fügt einen Home-Assistant-`ha-button` neben dem Direktiven-Anchor ein. Er nutzt dieselbe Button-Konfiguration und Action-Verarbeitung wie der [Forge button spark](../forge/sparks/button). Standardmäßig wird der Button nach dem Direktiven-Anchor eingefügt.

Nutze `after` oder `before`, um ein anderes Referenzelement zu wählen. Diese Pfade sind relativ zum aufgelösten Direktiven-Anchor und unterstützen die übliche UIX-`select_tree`-Syntax. Der Button wird weiterhin als Geschwisterelement des gefundenen Referenzelements eingefügt.

```yaml
- type: button
  label: Toggle
  entity: light.living_room
  tap_action:
    action: toggle
```

```yaml
- type: button
  anchor: "$ ha-dialog"
  before: "div.header"
  label: Toggle
  entity: light.living_room
  tap_action:
    action: toggle
```

Nutze `style` für ein flaches Mapping von CSS-Property-Namen und Werten. Die Properties werden inline auf dem erzeugten `ha-button` gesetzt. Das ist hilfreich für Button-Größen und Abstände, die nicht über Dashboard-Konfiguration gestylt werden können.

```yaml
- type: button
  anchor: "$ div.menu div.title"
  icon: mdi:hammer
  color: red
  size: s
  tap_action:
    action: navigate
    navigation_path: /config/tools
  style:
    "--ha-button-box-shadow": rgba(0, 0, 0, 0.1) 0px 4px 12px
    "--ha-icon-button-size": 32px
```

Nutze `uix` für UIX-Styling, einschließlich Styles innerhalb des Shadow Root des Buttons. Sein UIX-Typ ist `uix-broker-button`; die aufgelösten Button-Einstellungen sind in UIX-Templates als `config` verfügbar, und Ergebnisse vorheriger `template`- oder `javascript`-Direktiven sind als `directive` verfügbar.

::: info Verfügbar ab UIX 8.3.0-beta.3
`button`-UIX-Styling ist ab UIX 8.3.0-beta.3 verfügbar.
:::

```yaml
- type: button
  entity: light.living_room
  label: Toggle
  uix:
    style: |
      :host {
        --uix-button-margin: {{ '6px' if is_state(config.entity, 'on') else '0px' }};
      }
```

| Schlüssel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `after` | `string` | Direktiven-Anchor | Relativer Selektor für das Referenzelement. Der Button wird danach eingefügt. |
| `before` | `string` | - | Relativer Selektor für das Referenzelement. Der Button wird davor eingefügt. |
| `entity` | `string` | - | Entity-ID für entity-basierte Actions. |
| `icon` | `string` | - | MDI-Icon im Label-Slot des Buttons. Hat Vorrang vor `label`. |
| `color` | `string` | - | Icon-Farbe für einen reinen Icon-Button. |
| `label` | `string` | `""` | Button-Beschriftung. |
| `start_icon` / `end_icon` | `string` | - | MDI-Icon vor oder nach dem Label. |
| `variant` | `string` | Home-Assistant-Standard | `brand`, `neutral`, `danger`, `warning` oder `success`. Reine Icon-Buttons verwenden standardmäßig `neutral`. |
| `appearance` | `string` | Home-Assistant-Standard | `accent`, `filled`, `outlined` oder `plain`. Reine Icon-Buttons verwenden standardmäßig `plain`. |
| `size` | `string` | - | `s` (small) oder `m` (medium). |
| `style` | object | - | Flaches Mapping von CSS-Property-Namen und String- oder Zahlenwerten, inline auf `ha-button` gesetzt. |
| `uix` | object | - | UIX-Konfiguration für den erzeugten Button als Typ `uix-broker-button`. |
| `tap_action` / `hold_action` / `double_tap_action` | action | - | Home-Assistant-Action, die vom Button ausgeführt wird. |

::: note
- Setze höchstens eines von `after` und `before`.
- Button-Klicks werden vom Action-Handler des Referenzelements isoliert.
- Pointer-, Mouse-, Touch- und Click-Events stoppen am erzeugten Button. Dadurch reagiert kein umgebendes Element mit Ripple oder Action-Handler, während die eigene Button-Action erhalten bleibt.
- Dieselbe CSS-Variable `--uix-button-margin` wie beim Forge button spark gilt auch hier. Der Standardabstand ist `-6px` für einen Button mit Label und `0px` für einen reinen Icon-Button.
- Weitere CSS-Variablen des Forge button spark gelten ebenfalls.
:::

## Tile icon

::: info Verfügbar ab UIX 8.3.0-beta.3
Die `tile-icon`-Direktive ist ab UIX 8.3.0-beta.3 verfügbar.
:::

`tile-icon` fügt ein Home-Assistant-`ha-tile-icon` neben dem Direktiven-Anchor ein. Es nutzt dieselbe Icon-Darstellung und Action-Verarbeitung wie der [Forge tile-icon spark](../forge/sparks/tile-icon). Standardmäßig wird das Tile-Icon nach dem Direktiven-Anchor eingefügt.

Nutze `after` oder `before`, um ein anderes Referenzelement zu wählen. Diese Pfade sind relativ zum aufgelösten Direktiven-Anchor und unterstützen die übliche UIX-`select_tree`-Syntax. Das Tile-Icon wird als Geschwisterelement des gefundenen Referenzelements eingefügt.

```yaml
- type: tile-icon
  entity: light.living_room
  tap_action:
    action: toggle
```

```yaml
- type: tile-icon
  anchor: "$ ha-dialog"
  before: "div.header"
  entity: light.living_room
  icon: mdi:star
  color: orange
  tap_action:
    action: more-info
```

Nutze `style` für ein flaches Mapping von CSS-Property-Namen und Werten. Die Properties werden inline auf dem erzeugten `ha-tile-icon` gesetzt. Das ist hilfreich, um Position und Größe des Icons dort zu steuern, wo Dashboard-Styling nicht greift.

```yaml
- type: tile-icon
  entity: light.living_room
  style:
    margin-inline-start: 8px
    "--tile-icon-size": 28px
    z-index: 1
```

Nutze `uix` für UIX-Styling, einschließlich Styles innerhalb des Shadow Root des Tile-Icons. Sein UIX-Typ ist `broker-tile-icon`; die aufgelösten Tile-Icon-Einstellungen sind in UIX-Templates als `config` verfügbar, und Ergebnisse vorheriger `template`- oder `javascript`-Direktiven sind als `directive` verfügbar.

```yaml
- type: tile-icon
  entity: light.living_room
  uix:
    style: |
      :host {
        --tile-icon-size: {{ '32px' if is_state(config.entity, 'on') else '24px' }};
      }
```

| Schlüssel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `after` | `string` | Direktiven-Anchor | Relativer Selektor für das Referenzelement. Das Tile-Icon wird danach eingefügt. |
| `before` | `string` | - | Relativer Selektor für das Referenzelement. Das Tile-Icon wird davor eingefügt. |
| `entity` | `string` | - | Entity, deren Status-Icon gerendert wird. Liefert die Standard-Tap-Action: `toggle` für schaltbare Entities, sonst `none`. |
| `icon` | `string` | - | MDI-Icon. Mit `entity` überschreibt es das normale Status-Icon der Entity. |
| `icon_path` | `string` | - | SVG-Pfad, der als `iconPath` an `ha-tile-icon` übergeben wird. |
| `image_url` | `string` | - | Bild-URL, die als `imageUrl` an `ha-tile-icon` übergeben wird. |
| `color` | CSS-Farbe | - | Tile-Icon-Farbe. Mit `entity` wird sie angewendet, während die Entity aktiv ist. |
| `style` | object | - | Flaches Mapping von CSS-Property-Namen und String- oder Zahlenwerten, inline auf `ha-tile-icon` gesetzt. |
| `uix` | object | - | UIX-Konfiguration für das erzeugte Tile-Icon als Typ `broker-tile-icon`. |
| `tap_action` / `hold_action` / `double_tap_action` | action | - | Home-Assistant-Action, die vom Tile-Icon ausgeführt wird. |

::: note
- Setze höchstens eines von `after` und `before`.
- Gib eine Icon-Quelle mit `icon`, `icon_path`, `image_url` oder `entity` an.
- Entity-basierte Tile-Icons aktualisieren sich bei Home-Assistant-Statusänderungen.
- Pointer-, Mouse-, Touch- und Click-Events stoppen am erzeugten Icon. Dadurch reagiert kein umgebendes Element mit Ripple oder Action-Handler, während die eigene Tile-Icon-Action erhalten bleibt.
- Broker ergänzt jedes erzeugte Tile-Icon mit dem Attribut `data-uix-broker-tile-icon`, damit es aus UIX-Styling selektiert werden kann.
:::

## Tooltip

::: info Verfügbar ab UIX 8.3.0-beta.5
Die `tooltip`-Direktive wurde in beta.5 ergänzt; `trigger`, `open` und das Scroll-/Hover-Verhalten folgen in beta.8.
:::

`tooltip` fügt Home Assistants `wa-tooltip` als Geschwisterelement des gewählten Ziels ein. Optionen und CSS-Variablen entsprechen dem [Forge Tooltip Spark](../forge/sparks/tooltip). Standardmäßig ist `for` der aufgelöste Direktiven-Anchor. Ein Selektor ist relativ zu diesem Anchor und verwendet die normale UIX-`select_tree`-Syntax. Das Ziel muss ein Element sein, kein abschließender Shadow Root.

```yaml
- type: tooltip
  content: Steuerung der Wohnzimmerbeleuchtung öffnen
  placement: bottom
```

Mit `for: previous` direkt nach einer UI-Direktive erhält deren erzeugtes Element den Tooltip. Das funktioniert mit `button` und `tile-icon` und ist für spätere elementerzeugende Direktiven vorbereitet.

```yaml
- type: button
  icon: mdi:lightbulb
  tap_action:
    action: toggle
- type: tooltip
  for: previous
  content: Licht umschalten
  placement: bottom
```

```yaml
- type: tooltip
  for: "$ ha-dialog ha-icon-button"
  content: Schließen
  without_arrow: true
```

`style` ist ein flaches Mapping von CSS-Eigenschaften. Damit lassen sich insbesondere `--uix-tooltip-*`-Variablen direkt auf dem erzeugten Tooltip setzen:

```yaml
- type: tooltip
  for: previous
  content: Licht umschalten
  style:
    "--uix-tooltip-background-color": var(--primary-color)
    "--uix-tooltip-content-color": white
    "--uix-tooltip-max-width": 24ch
```

`trigger` akzeptiert die durch Leerzeichen getrennten Web-Awesome-Aktivierungsarten `hover`, `focus`, `click` und `manual`. Bei `hover` bleibt der Tooltip geöffnet, wenn der Zeiger vom Ziel in seinen Inhalt bewegt wird; begrenzte Inhalte können dadurch gescrollt werden. `manual` aktiviert ihn nicht automatisch. `open` setzt den Zustand beim Ausführen der Direktive.

```yaml
- type: tooltip
  for: previous
  trigger: manual
  open: true
  content: Dieser Tooltip wird durch die Direktive geöffnet
```

| Schlüssel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `for` | string | Direktiven-Anchor | Zielselektor oder `previous` für die vorherige elementerzeugende Direktive. |
| `content` | string | `""` | HTML-Inhalt des Tooltips. |
| `placement` | string | `"top"` | `top`, `top-start`, `top-end`, `bottom`, `bottom-start`, `bottom-end`, `left`, `left-start`, `left-end`, `right`, `right-start` oder `right-end`. |
| `distance` | number | `8` | Abstand zwischen Tooltip und Ziel in Pixeln. |
| `skidding` | number | `0` | Versatz entlang der Zielachse in Pixeln. |
| `show_delay` | number | `150` | Wartezeit bis zum Anzeigen in Millisekunden. |
| `hide_delay` | number | `150` | Wartezeit bis zum Ausblenden in Millisekunden. |
| `trigger` | string | `"hover focus"` | Aktivierungsarten `hover`, `focus`, `click` oder `manual`, durch Leerzeichen getrennt. |
| `open` | boolean | `false` | Öffnungszustand beim Ausführen setzen; besonders für `trigger: manual`. |
| `without_arrow` | boolean | `false` | Richtungspfeil ausblenden. |
| `style` | object | — | Flaches Mapping von CSS-Eigenschaften auf String- oder Zahlenwerte, inline auf `wa-tooltip` gesetzt. |

Da der Tooltip neben dem Ziel liegt, müssen vererbte CSS-Variablen auf dem Eltern- oder einem Vorfahrenelement gesetzt werden. Siehe [CSS-Variablen des Tooltip Sparks](../forge/sparks/tooltip#css-variablen).

## Action

`action` führt einen Home-Assistant-Service-Call, eine Standard-Frontend-Action oder eine UIX-Broker-spezifische Action aus.

```yaml
- type: action
  action: light.turn_on
  target:
    entity_id: light.example

- type: action
  action: fire-dom-event
  uix:
    action: toast
    data:
      message: Done
```

### JavaScript-Action

`action: javascript` ist eine UIX-Broker-Action. Der Code steht in `data.code`. UIX Broker übergibt automatisch `hass`, `anchor`, `event` und `captured` als Variablen. `hass` ist das aktive Home-Assistant-Objekt, `anchor` der aufgelöste Interaction-Anchor, `event` das auslösende Event und `captured` die Captured Data.

```yaml
- type: action
  action: javascript
  data:
    code: |
      console.log(anchor, event, captured)
```

Nutze JavaScript nur aus vertrauenswürdigen UIX-Konfigurationen.

## Template

`template` rendert ein Home-Assistant-Jinja2-Template einmal über die Template-API; es erzeugt keine Template-Subscription. Das String-Ergebnis wird unter `id` für die übrigen Direktiven dieser Interaktion gespeichert.

Jedes nicht gecachte Rendern ist ein Roundtrip zum Home-Assistant-Server. Vermeide das bei Interaktionen, die häufig laufen können. Setze `cache` auf eine positive Anzahl Millisekunden, wenn ein leicht veralteter Wert akzeptabel ist:

```yaml
- type: template
  id: example
  cache: 5000
  template: "{{ states('sensor.example') }}"
```

Der Cache liegt im Browser und wird von Template-Direktiven mit demselben Template-Text und denselben vorherigen Direktiven-Ergebnissen geteilt. Ein gecachter Wert wird nur genutzt, wenn er jünger als die `cache`-Dauer der Direktive ist; `cache: 0` oder ein fehlender `cache` rendert immer neu. Der Cache speichert nur erfolgreiche Ergebnisse, wird beim Neuladen der Broker-Konfiguration geleert und beobachtet während der Cache-Dauer keine Template-Änderungen. Wenn `cache` aktiv ist, müssen vorherige Direktiven-Ergebnisse JSON-serialisierbar sein, weil sie Teil des Cache-Schlüssels werden; zirkuläre Objekte können nicht gecacht werden.

```yaml
- type: template
  id: log_provider_url
  template: "/config/logs?provider={{ states('input_select.log_provider') }}"
- type: button
  after: "&home-assistant $ home-assistant-main $ ha-config-system-navigation $ ha-config-navigation-list $ ha-list-item-button:nth-of-type(4) $ a#item div.content"
  icon: mdi:open-in-new
  color: var(--primary-color)
  tap_action:
    action: url
    url_path: "@log_provider_url"
```

`id` muss mit einem Buchstaben oder Unterstrich beginnen und darf danach Buchstaben, Zahlen, Unterstriche und Bindestriche enthalten. Der Name `captured` ist für `@captured`-Event-Daten reserviert und kann nicht als ID genutzt werden. Verwende dot oder bracket array paths, um einen gespeicherten Objekt- oder Array-Wert auszuwählen, genau wie bei `@captured`. Quoted bracket keys funktionieren ebenfalls, zum Beispiel `@config_path['icon-color']` oder `@config_path["icon-color"]`.

Templates erhalten vorherige Direktiven-Ergebnisse in der Top-Level-Variable `directive`. Eine vorherige Direktive mit `id: provider` ist zum Beispiel als <code v-pre>{{ directive.provider }}</code> verfügbar. Dieser Namespace enthält nur Ergebnisse früherer Direktiven derselben Interaktion.

## JavaScript

`javascript` wertet `code` einmal aus und speichert den synchronen Rückgabewert unter `id`. Der Code erhält `hass`, `anchor`, `event`, `captured` und `directive`; `directive` enthält vorherige Direktiven-Ergebnisse derselben Interaktion. Gib einen skalaren Wert, ein Objekt oder ein Array zurück; folgende Direktiven können ihn ohne Konvertierung als `@id` verwenden.

```yaml
- type: javascript
  id: config_path
  code: |
    const provider = hass.states['input_select.log_provider'].state;
    return {
      path: `/config/logs?provider=${provider}`,
      label: `Open ${provider.charAt(0).toUpperCase() + provider.slice(1)} logs`,
    };
- type: button
  icon: mdi:open-in-new
  label: "@config_path.label"
  tap_action:
    action: url
    url_path: "@config_path.path"
```

Nutze JavaScript nur aus vertrauenswürdigen UIX-Konfigurationen.

## Wait

Nutze `wait`, um eine Direktiven-Sequenz ohne weitere Operation zu pausieren. Der Wert muss eine nicht negative Zahl in Millisekunden sein.

```yaml
directives:
  - type: wait
    wait: 500
  - type: action
    action: light.turn_on
    target:
      entity_id: light.example
```

Jede Direktive akzeptiert außerdem `wait`, eine nicht negative Zahl in Millisekunden. In dieser Form wartet UIX Broker nach dem Anwenden der Direktive, bevor die nächste Direktive startet. Eine `block`-Direktive läuft immer synchron, kann aber `wait` enthalten, um spätere Direktiven zu verzögern.

```yaml
directives:
  - type: event
    name: broker-started-event
    wait: 250
  - type: action
    action: light.turn_on
```
