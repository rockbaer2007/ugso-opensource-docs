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
