---
title: Schnellstart
description: Einstieg in UI eXtension für Home Assistant.
---
# Schnellstart

UIX **9.0.0** benötigt **Home Assistant 2026.11.0 oder neuer**. Siehe [Release 9.0.0](https://github.com/Lint-Free-Technology/uix/releases/tag/v9.0.0).

> **Für Card-mod-Nutzer**
> Wenn du von Card-mod kommst, lies zusätzlich die [FAQ](./faq). UIX unterstützt viele Card-mod-Konfigurationen, nutzt aber eigene Schlüssel und bringt zusätzliche Funktionen mit.
>
## Installation

### Marketplace

[![Home Assistant öffnen und UIX im Marketplace anzeigen.](https://my.home-assistant.io/badges/marketplace_repository.svg)](https://my.home-assistant.io/redirect/marketplace_repository/?owner=Lint-Free-Technology&repository=uix&category=integration)

Öffne UI eXtension im [Home Assistant Marketplace](https://www.home-assistant.io/integrations/marketplace/) und wähle **Installieren**. Marketplace übernimmt dabei auch das Hinzufügen als Dienst.
### Manuell

Kopiere den Ordner `custom_components/uix` aus dem Repository in den `custom_components`-Ordner deiner Home-Assistant-Konfiguration. Starte Home Assistant anschließend neu.

#### UI eXtension bei manueller Installation als Dienst hinzufügen {#ui-extension-als-dienst-hinzufugen}

[![Home Assistant öffnen und Integration anzeigen.](https://my.home-assistant.io/badges/integration.svg)](https://my.home-assistant.io/redirect/integration/?domain=uix)

Füge UI eXtension nach dem Neustart unter **Einstellungen → Geräte & Dienste** als Dienst hinzu. Lade danach die Seite neu, damit die Frontend-Ressource aktiv wird.
## Erstes UIX Styling

1. Öffne eine Karte im Home-Assistant-GUI-Editor.
2. Klicke unten im Bearbeitungsdialog auf `Code-Editor anzeigen`.
3. Ergänze im YAML die UIX-Konfiguration.

```yaml
type: tile
entity: light.bed_light
uix:
  style: |
    ha-card {
      background: red;
    }
```

Während der Eingabe sollte sich der Kartenhintergrund rot färben. Außerdem erscheint ein kleines Pinsel-Symbol in der Nähe von `Visuellen Editor anzeigen`. Das zeigt an, dass diese Karte UIX-Code enthält, der im visuellen Editor nicht vollständig dargestellt wird.

![Quick Start](https://raw.githubusercontent.com/Lint-Free-Technology/uix/f9eb8fa571dbce6cd771c53ca11dcf2401c8a933/docs/source/assets/page-assets/quick-start/quick-start-basic.png)

## Erstes UIX Forge

UIX Forge erzeugt ein Home-Assistant-Element aus einer Vorlage. Im Beispiel wird eine Tile-Karte erzeugt, die ausgeblendet wird, wenn `input_boolean.test_boolean` auf `on` steht.

```yaml
type: custom:uix-forge
forge:
  mold: card
  show_error: false
  hidden: "{{ is_state('input_boolean.test_boolean', 'on') }}"
  grid_options:
    columns: "{{ 6 }}"
    rows: 1
element:
  type: tile
  icon: "{{ 'mdi:test-tube' }}"
  entity: "{{ 'sun.sun' }}"
  uix:
    style: |
      ha-card {
        background: red;
      }
```

![First UIX Forge](https://raw.githubusercontent.com/Lint-Free-Technology/uix/f9eb8fa571dbce6cd771c53ca11dcf2401c8a933/docs/source/assets/page-assets/quick-start/basic-first-forge.gif)

## Nächste Schritte

- [UIX Styling](./using/index)
- [UIX Forge](./forge/index)
- [FAQ](./faq)
