---
title: Examples
description: UIX-Broker-Beispiele.
---
# Beispiele

::: info Verfügbar ab UIX 8.2.0-beta.2
UIX Broker gehört zum aktuellen Entwicklungszweig.
:::

## Card-Tab im Add-Card-Dialog als Standard setzen

Ergebnis:

- Der Card-Tab wird ausgewählt, wenn der Add-Card-Dialog geöffnet wird.
- Der erste Expander, Suggested oder Favorites, wird geöffnet.
- Alle anderen Expander werden geschlossen.

Methode:

- Auf `show-dialog` im `browser`-Realm lauschen.
- Die Regel passt nur, wenn `dialogTag` den Wert `hui-dialog-create-card` hat.
- Ein absoluter Kurzform-Interaction-Anchor findet den Dialog `hui-dialog-create-card`.
- Direktiven setzen `_currTab` auf `card` und steuern anschließend die `expanded`-Properties der Expander.

```yaml
uix_broker:
  - realm: browser
    listen: show-dialog
    anchor: '&home-assistant $ hui-dialog-create-card'
    debug: true
    rules:
      - '@captured.dialogTag': hui-dialog-create-card
    directives:
      - type: property
        set: _currTab
        value: card
        wait: 1000
      - type: property
        anchor: >-
          $ ha-dialog div.body hui-card-picker $ div#content div:nth-of-type(1)
          ha-expansion-panel
        set: expanded
        value: true
      - type: property
        anchor: >-
          $ ha-dialog div.body hui-card-picker $
          div#content>ha-expansion-panel:nth-of-type(1)
        set: expanded
        value: false
      - type: property
        anchor: >-
          $ ha-dialog div.body hui-card-picker $
          div#content>ha-expansion-panel:nth-of-type(2)
        set: expanded
        value: false
      - type: property
        anchor: >-
          $ ha-dialog div.body hui-card-picker $
          div#content>ha-expansion-panel:nth-of-type(3)
        set: expanded
        value: false
```

::: tip
Speichere das YAML als neue Datei im Home-Assistant-Konfigurationsverzeichnis oder einem Unterordner und registriere sie über den UIX-Optionsdialog.
:::

## Automation Sidebar und YAML-Modus

### Automation-Editor-Sidebar standardmäßig im YAML-Modus öffnen

Dieses Beispiel setzt die Automation Sidebar auf YAML-Modus. Allein genutzt sperrt es die Sidebar praktisch auf YAML-Modus.

```yaml
- realm: browser
  listen: open-sidebar
  reentrant: false
  anchor: manual-automation-editor <$$ target
  rules:
    - '{!.uixBlockAutoYamlMode}'
    - anchor: $ ha-automation-sidebar $$ ha-automation-sidebar-card
      match: '{.yamlMode=false}'
  directives:
    - anchor: $ ha-automation-sidebar
      method: _toggleYamlMode
      type: call
```

### Umschalten des YAML-Modus im Automation Editor erlauben

Das Menüelement **Toggle YAML Mode** löst `toggle-yaml-mode` aus. Ohne Koordination würde das vorherige Beispiel sofort wieder YAML erzwingen. Dieses Beispiel blockiert das Event, setzt eine Guard-Property, ruft die Funktion direkt auf und entfernt danach die Guard-Property wieder.

```yaml
- realm: browser
  listen: toggle-yaml-mode
  anchor: manual-automation-editor <$$ target
  directives:
    - type: block
    - type: property
      set: uixBlockAutoYamlMode
      value: true
    - anchor: $ ha-automation-sidebar
      method: _toggleYamlMode
      type: call
    - type: property
      clear: uixBlockAutoYamlMode
```

### YAML-Modus per Tastenkürzel umschalten

```yaml
- realm: shortcut
  enabled: true
  listen: $mod+Shift+Y
  anchor: '&home-assistant $$ manual-automation-editor'
  directives:
    - type: property
      set: uixBlockAutoYamlMode
      value: true
    - anchor: $ ha-automation-sidebar
      method: _toggleYamlMode
      type: call
    - type: property
      clear: uixBlockAutoYamlMode
```

::: details Vollständiges YAML für die drei Automation-Sidebar-Beispiele

```yaml
uix_broker:
  - realm: browser
    listen: open-sidebar
    reentrant: false
    anchor: manual-automation-editor <$$ target
    rules:
      - '{!.uixBlockAutoYamlMode}'
      - anchor: $ ha-automation-sidebar $$ ha-automation-sidebar-card
        match: '{.yamlMode=false}'
    directives:
      - anchor: $ ha-automation-sidebar
        method: _toggleYamlMode
        type: call
  - realm: browser
    listen: toggle-yaml-mode
    anchor: manual-automation-editor <$$ target
    directives:
      - type: block
      - type: property
        set: uixBlockAutoYamlMode
        value: true
      - anchor: $ ha-automation-sidebar
        method: _toggleYamlMode
        type: call
      - type: property
        clear: uixBlockAutoYamlMode
  - realm: shortcut
    enabled: true
    listen: $mod+Shift+Y
    anchor: '&home-assistant $$ manual-automation-editor'
    directives:
      - type: property
        set: uixBlockAutoYamlMode
        value: true
      - anchor: $ ha-automation-sidebar
        method: _toggleYamlMode
        type: call
      - type: property
        clear: uixBlockAutoYamlMode
```

:::

## Entity Trigger beim Hinzufügen eines Automation-Editor-Elements priorisieren

Ergebnis:

- Beim Hinzufügen eines Automation-Editor-Elements wird direkt zu Entity Triggern gesprungen.

Methode:

- Auf `show-dialog` im `browser`-Realm lauschen.
- Die Regel passt nur, wenn `dialogTag` den Wert `add-automation-element-dialog` hat.
- Der absolute Kurzform-Interaction-Anchor findet den Dialog.
- Direktiven setzen `_tab` auf `groups` und `_selectedGroup` auf `entity`.

```yaml
- realm: browser
  listen: show-dialog
  anchor: '&home-assistant $ add-automation-element-dialog'
  debug: true
  rules:
    - '@captured.dialogTag': add-automation-element-dialog
  directives:
    - type: property
      set: _tab
      value: groups
    - type: property
      set: _selectedGroup
      value: entity
```

## Werkzeug-Button zum Sidebar-Titel hinzufügen

Ergebnis:

- Ein Werkzeug-Button navigiert zu `/config/tools`.

Methode:

- Auf das Event `uix-broker-ready` im `browser`-Realm lauschen.
- Kompakter absoluter Anchor für `ha-sidebar`.
- Die Regel passt nur, wenn die Property `user.is_admin` des `hass`-Objekts auf `home-assistant` `true` ist. Alternativ kann `user.is_owner` genutzt werden, wenn nur der Owner passen soll.
- Eine `button`-Direktive platziert den Button nach dem Titel und nutzt ein einfaches Style-Objekt für Schatten und kleinere Icon-Größe.

```yaml
- realm: browser
  listen: uix-broker-ready
  anchor: "&home-assistant $ home-assistant-main $ ha-sidebar"
  rules:
    - anchor: "&home-assistant"
      match: "{.hass.user.is_admin=true}"
  directives:
    - type: button
      anchor: "$ div.menu div.title"
      icon: mdi:hammer
      color: purple
      size: s
      tap_action:
        action: navigate
        navigation_path: /config/tools
      style:
        "--ha-button-box-shadow": rgba(0, 0, 0, 0.1) 0px 4px 12px
        "--ha-icon-button-size": 32px
```

## Vorgeschlagene Geräte-Entities-Card für Abschnitts-Views auf Entities ändern

Ergebnis:

- Die vorgeschlagene Geräte-Entities-Card für Abschnitts-Views wird zu einer Entities-Card. Das ist nicht dasselbe wie die Vorschläge für andere Views, die auf der Entity-Domain basieren.

Methode:

- Auf das Event `show-dialog` im `browser`-Realm lauschen.
- Die Regel passt nur, wenn `dialogTag` den Wert `hui-dialog-suggest-card` hat.
- Die Interaktion nutzt `reentrant: false`, weil sie selbst wieder `show-dialog` auslöst.
- Der Interaction Anchor ist `&home-assistant`. Da die Direktiven `block` enthalten, muss der Anchor synchron vorhanden sein. Alternativ könnte `anchor: target` als Event-Pfad-Anchor genutzt werden, wenn bei der Event-Direktive `anchor: "&home-assistant"` gesetzt wird.
- Direktiven:
  - Eine `block`-Direktive stoppt die Weitergabe des ursprünglichen Events.
  - Eine `event`-Direktive löst `show-dialog` erneut mit veränderten `dialogParams.sectionConfig` aus und setzt `cards` auf eine einzelne `entities`-Card. `sectionConfig.type` und `sectionConfig.title` werden über `@captured` aus den erfassten Daten kopiert. Damit die restlichen Event-Daten nicht einzeln kopiert werden müssen, führt `capture_data: deep` einen Deep-Merge von `sectionConfig` aus.

```yaml
- realm: browser
  listen: show-dialog
  debug: true
  reentrant: false
  anchor: "&home-assistant"
  rules:
    - "@captured.dialogTag": hui-dialog-suggest-card
  directives:
    - type: block
    - type: event
      name: show-dialog
      bubbles: true
      composed: true
      capture_data: deep
      data:
        dialogParams:
          sectionConfig:
            type: "@captured.dialogParams.sectionConfig.type"
            title: "@captured.dialogParams.sectionConfig.title"
            cards:
              - type: entities
                entities: "@captured.dialogParams.entities"
```

## Light-Button am Home-Dashboard-Menüpunkt der Sidebar

Ergebnis:

- Ähnlich wie bei [Werkzeug-Button zum Sidebar-Titel hinzufügen](#werkzeug-button-zum-sidebar-titel-hinzufuegen) fügt dieses Beispiel dem Home-Menüpunkt in der Sidebar einen Toggle-Button für ein Licht hinzu. Damit der aktuelle Zustand des Lichts sichtbar bleibt, nutzt es zusätzlich eine Hilfsinteraktion vom Server-Realm zum Browser-Realm. Dadurch läuft die Hauptinteraktion erneut, wenn sich der Entity-Status ändert.

Methode für die Sidebar-Interaktion:

- Im `browser`-Realm auf `uix-broker-ready` und `uix-update-sidebar` lauschen. `uix-update-sidebar` ist ein eigenes Event; der Name ist frei wählbar, solange er zur Hilfsinteraktion passt.
- Kompakter absoluter Anchor für `ha-sidebar`.
- Direktiven:
  - Eine `javascript`-Direktive setzt Objektparameter für die spätere `button`-Direktive. `icon` und `color` werden aus dem Entity-Status abgeleitet.
  - Eine `button`-Direktive platziert den Button nach dem Home-Menüpunkt. Ein einfaches Style-Objekt setzt Schatten, Icon-Größe und Abstand. Die Aktion schaltet das Licht um. Konfiguration und Verhalten des Buttons folgen dem [UIX Forge Button Spark](../forge/sparks/button); die Entity wird hier nur für die Aktion eingebunden.

```yaml
- realm: browser
  listen:
    - uix-broker-ready
    - uix-update-sidebar # eigenes Event aus der Server-Realm-Hilfsinteraktion
  anchor: "&home-assistant $ home-assistant-main $ ha-sidebar"
  directives:
    - type: javascript
      id: button_config
      code: |
        const entity = 'light.bed_light';
        const state = hass.states[entity].state;
        return {
          entity: entity,
          icon: state === 'on' ? 'mdi:lightbulb-on' : 'mdi:lightbulb-off',
          color: state === 'on' ? 'var(--state-active-color)' : 'var(--state-inactive-color)'
        };
    - type: button
      anchor: "$ ha-list-item-button#sidebar-panel-home $ a#item div.content"
      icon: "@button_config.icon"
      color: "@button_config.color"
      entity: "@button_config.entity"
      size: s
      tap_action:
        action: toggle
      style:
        "--ha-button-box-shadow": rgba(0, 0, 0, 0.1) 0px 4px 12px
        "--ha-icon-button-size": 32px
        "--uix-button-margin": 6px
```

Methode für die Hilfsinteraktion:

Ergebnis:

- Ein eigenes Browser-Event wird ausgelöst, wenn sich der Entity-Status ändert. Dadurch reagiert die obige Beispielinteraktion auf Statusänderungen von `light.bed_light`.

Methode:

- Im Server-Realm auf das Event `state_changed` lauschen.
- Anchor auf das `home-assistant`-Element mit kompakter absoluter Anchor-Form setzen.
- Eine `event`-Direktive löst das eigene Browser-Event `uix-update-sidebar` aus, wenn die geänderte `entity_id` `light.bed_light` ist. Das Beispiel löst auch bei `light.other_light` aus, um die Nutzung von `or:` in `match` zu zeigen. Das ist nützlich, wenn du weitere Button-Direktiven in die Interaktion oben aufnimmst.

```yaml
- realm: server
  listen: state_changed
  anchor: "&home-assistant"
  directives:
    - type: event
      name: uix-update-sidebar
      rules:
        - type: captured
          path: data.entity_id
          match:
            or:
              - light.bed_light
              - light.other_light
```

![Button-Direktive als Light-Toggle-Beispiel](../assets/page-assets/broker/broker-button-light-directive.gif)
