---
title: Foundries
description: Wiederverwendbare Forge-Konfigurationen, native Basis, Vererbung, YAML-Dateien, Billets und Styling.
---
# Foundries

Eine **Foundry** ist eine benannte Forge-Konfiguration in Home Assistant. Definiere `forge`, `element` und bei vom Forge-Editor exportierten nativen Einstellungen optional `element_base` einmal und verwende sie mit dem obersten Schlüssel `foundry:` mehrfach. Lokale Werte überschreiben die Vorlage.

::: info Versionsstand
Abgeglichen mit [UIX dev `26e54e6`](https://github.com/Lint-Free-Technology/uix/blob/26e54e6d4973231a393933e6479ed1b03cc86cd3/docs/source/forge/foundries.md), 9.0.0-beta.2. Native Basis und visueller Editor gehören zur Vorschau; die stabile Basis dieser Dokumentation bleibt 8.4.0.
:::

## Global Foundries {#global-foundries}

Die reservierte Foundry `global` wird automatisch auf alle Forges angewendet. Danach folgt `global_<mold>`, etwa `global_card`, `global_badge` oder `global_row`. Der Mold ergibt sich aus der lokalen Konfiguration oder der ausdrücklich ausgewählten Foundry. Damit lassen sich gemeinsame Makros, Sparks und Standardstile festlegen, ohne jede Karte mit einer Foundry-Referenz zu versehen.

## Foundries verwalten

### UI Foundries

Öffne **Einstellungen → Geräte & Dienste → UI eXtension → Konfigurieren → UI-Foundries verwalten**. Dort kannst du Foundries hinzufügen, bearbeiten oder nach Bestätigung löschen. Vergib einen eindeutigen Namen und ein YAML-Konfigurationsobjekt. Eine einzelne UI Foundry enthält direkt `forge`, `element` usw., keinen Dateicontainer `uix_foundries`.

### YAML File Foundries

Dateien im oder erreichbar vom HA-Konfigurationsverzeichnis eignen sich für größere Sammlungen, Versionsverwaltung, Texteditoren, YAML-Anker, `!include` und `!secret`. Sie werden mit dem nativen HA-YAML-Loader geladen.

#### Dateiformat

Der Dateicontainer heißt **`uix_foundries`**, nicht `foundries`. Sein Wert ist eine Zuordnung von Namen auf Konfigurationen:

```yaml
uix_foundries:
  light_tile:
    forge:
      mold: card
    element:
      type: tile
      entity: light.bed_light
  switch_tile:
    forge:
      mold: card
    element:
      type: tile
      entity: switch.living_room
```

#### YAML-Anker

Anker `&name` und Merge-Keys `<<: *name` können Optionen auf derselben Ebene teilen, etwa Formatierungen mehrerer Entity-Zeilen. YAML-Merge-Keys sind **flach**: am Foundry-Wurzelobjekt würden sie ein komplettes `element` ersetzen. Für die tiefe Kombination von `forge` und `element` verwende [verschachtelte Foundries](#verschachtelte-foundries).

#### Datei registrieren

Unter **Konfigurieren → Foundry-Dateien verwalten → Datei hinzufügen** den Pfad angeben, beispielsweise `/config/uix/foundries.yaml`. Ein Pfad relativ zum Konfigurationsverzeichnis funktioniert ebenfalls.

Vor dem Speichern prüft UIX Existenz, YAML-Syntax und den erforderlichen Schlüssel `uix_foundries`; Fehler verhindern die Registrierung.

#### Dateien neu laden

Nach Dateiänderungen **Foundry-Dateien neu laden** wählen. UIX lädt die registrierten Dateien erneut und aktualisiert die Konfiguration; ein HA-Neustart ist nicht erforderlich.

Dateien werden beim ersten Abruf durch den Browser und bei Foundry-Aktualisierungen gelesen. Das Neuladen aktualisiert alle verbundenen Browser. Bei YAML-Dashboards liest auch der normale **Aktualisieren**-Button über `config-refresh` die Dateien neu. Im YAML-Reiter der Home-Assistant-Entwicklerwerkzeuge gibt es außerdem **UIX Foundries** zum Neuladen mit Fehleranzeige.

#### Registrierung entfernen

**Datei entfernen** entfernt die Registrierung und die aus dieser Datei geladenen Foundries, nicht die Datei auf dem Datenträger. Karten, die solche Foundries referenzieren, müssen danach angepasst werden.

#### Vorrang

Bei gleichem Namen gewinnt eine UI Foundry gegenüber einer Datei-Foundry. Bei mehreren Dateien gewinnt die später geladene Definition. Verwende eindeutige Namen, um unbeabsichtigte Überschreibungen zu vermeiden.

## Foundry verwenden

`foundry` steht neben `type`, nicht innerhalb von `forge`:

```yaml
type: custom:uix-forge
foundry: light_tile
element:
  entity: light.kitchen
```

Die Foundry-Fragmente werden angewendet, als stünden sie direkt in der Forge-Konfiguration. Lokale Werte haben Vorrang.

## Struktur einer Foundry-Konfiguration

Eine Foundry kann `foundry`, `forge`, `element` und optional `element_base` enthalten. `element` enthält die von Forge verarbeiteten Werte. Foundry-`element_base` wird durch die Vererbung und dann mit einer lokalen Basis zusammengeführt; ihre Templates verarbeitet HA bzw. das eingebettete Element, nicht Forge. Erzeuge oder aktualisiere diese native Quelle über das YAML des **Export**-Reiters und erhalte sie für künftige Unterstützung im visuellen Editor. `element_disabled_paths` bleibt ausschließlich lokal; auch `global` und `global_<mold>` dürfen es nicht setzen.

### Foundry-Typ mit dem nativen Editor verwenden

Eine Foundry kann einen konkreten `element.type` liefern. Ohne native Basis bleibt das eine gewöhnliche vollständige Forge-Konfiguration. Für den Native-Editor muss die lokale Basis denselben konkreten Typ wiederholen:

```yaml
# Foundry room_tile
forge:
  mold: card
element:
  type: tile
  name: "{{ config.entity }}"
```

```yaml
# Dashboard-Karte
type: custom:uix-forge
foundry: room_tile
element_base:
  type: tile
  entity: light.kitchen
```

Die beiden Typen müssen dieselbe konkrete Zeichenkette sein. Dynamische oder abweichende Typen und ein lokales `element.type` sind bei vorhandener Basis ungültig. Nur der passende **geerbte** Typ wird als nativer Anker verwendet und vor dem Zusammensetzen aus der Überlagerung entfernt. Siehe [native Basis](./forge#keep-the-elements-configuration-in-element_base).

## Externe Dateien und Secrets einbinden

In UI Foundries müssen `!include` und `!secret` gequotete Strings sein, weil HA ihre Konfiguration als JSON speichert. In YAML-Dateien sind es normale ungequotete YAML-Tags. Beide Varianten werden vor Template-Auswertung und Merge aufgelöst; eingebundene Dateien können weitere Includes enthalten.

```yaml
# YAML-Datei
forge:
  uix: !include /config/uix/styles.yaml
```

```yaml
# Entsprechende UI Foundry
forge:
  uix: "!include /config/uix/styles.yaml"
```

```yaml
# In secrets.yaml: gate_pin: "1234"
forge:
  billets:
    gate_pin: !secret gate_pin
```

In einer UI Foundry schreibe stattdessen `gate_pin: "!secret gate_pin"`. Achte darauf, Secrets nicht versehentlich in öffentliche Beispiele zu übernehmen.

## Merge-Verhalten

Die Reihenfolge lautet **`global` → `global_<mold>` → geerbte Foundries → benannte Foundry → lokale Konfiguration**. Objekte werden rekursiv zusammengeführt; lokale Arrays und Skalare ersetzen geerbte Werte. Foundry-`element_base` wird vor lokaler Basis aufgelöst; danach wird `element` unter Beachtung der Typregel aufgelegt.

Für `forge.sparks` gelten Ausnahmen:

- Lokale Einträge werden standardmäßig angehängt.
- Gleiche `id` oder `spark_id` **und gleicher Spark-`type`** erlauben gezieltes Überschreiben/Zusammenführen.
- `forge.sparks: []` leert geerbte Sparks ausdrücklich. Der visuelle Editor bietet dieses Leeren geerbter Arrays nicht an; dafür YAML verwenden.

### Merge-Beispiel

Liefert `weather_tile` ein `weather-forecast` mit `show_current: true` und `show_forecast: false`, behält die folgende Instanz die aktuelle Anzeige und ersetzt nur Vorschau und Entität:

```yaml
type: custom:uix-forge
foundry: weather_tile
element:
  entity: weather.home
  show_forecast: true
```

<a id="verschachtelte-foundries"></a>
## Verschachtelte Foundries {#nested-foundries}

Eine Foundry kann mit dem eigenen obersten `foundry`-Schlüssel eine andere referenzieren. Beispiel für `light_tile`, das `base_tile` erweitert:

```yaml
foundry: base_tile
element:
  vertical: false
  features_position: inline
  features:
    - type: light-brightness
```

Eine Karte mit `foundry: light_tile` erhält dann `base_tile` → `light_tile` → lokale Werte. Zirkuläre Referenzen werden erkannt und erzeugen einen Fehler; die Kette muss eindeutig enden.

## Billets in Foundries {#billets-in-foundries}

[Billets](./forge#billets) sind benannte Slots unter **`forge.billets`**, nicht direkt an der Foundry-Wurzel. Zwei Muster ergänzen sich:

### Muster 1: Defaults in der Foundry definieren, pro Instanz überschreiben

Foundry `accent_tile`:

```yaml
forge:
  mold: card
  billets:
    accent: teal
element:
  type: tile
  entity: "{{ config.entity }}"
  uix:
    style: |
      ha-card {
        --tile-color: {{ accent }} !important;
      }
```

```yaml
type: custom:uix-forge
foundry: accent_tile
entity: light.bed_light
forge:
  billets:
    accent: blue
```

Ohne lokale Überschreibung bleibt `teal` erhalten.

### Muster 2: Leere Billet-Slots in der Foundry definieren

Eine Foundry kann `accent: ~` und `label: ~` unter `forge.billets` definieren. Ihre Templates müssen den `none`-Fall behandeln, etwa mit `or`, `default()` oder `{% if %}`. Beispiel für die Beschriftung:

```yaml
element:
  name: "{{ label or state_attr(config.entity, 'friendly_name') }}"
```

Instanzen setzen nur benötigte Werte unter `forge.billets`. Aussagekräftige Namen wie `accent_color` und `card_label` erleichtern die Pflege: UI Foundries verlieren YAML-Kommentare bei der JSON-Speicherung; Datei-Foundries behalten sie.

## UIX-Styling aus einer Foundry

`forge.uix` gestaltet den Forge-Wrapper. Lokales `forge.uix` wird mit der Foundry zusammengeführt und gewinnt bei gleichem Schlüssel. Für Root- und Shadow-Root-Stile eine YAML-Selektorzuordnung verwenden; Root-Stile stehen im Schlüssel `.`. Ein reiner Textwert für `style` ersetzt dagegen die ganze geerbte Zuordnung.

```yaml
type: custom:uix-forge
foundry: styled_tile
forge:
  uix:
    style:
      .: |
        :host { --ha-card-border-radius: 20px; }
element:
  entity: light.bed_light
```

## Beispiel: Global Foundry mit Makro {#example-global-foundry-using-macro}

Ein boolesches Makro benötigt das Format `returns`; gewöhnliche Makros liefern Strings und können sonst unerwartet als wahr ausgewertet werden. Foundry mit dem Namen `global`:

```yaml
forge:
  macros:
    is_festive_day:
      returns: true
      template: "{% do returns(is_state('input_boolean.festive_day','on')) %}"
```

Eine Forge-Picture-Karte kann damit das Bild wählen:

```yaml
type: custom:uix-forge
forge:
  mold: card
  grid_options:
    columns: full
    rows: 4
element:
  type: picture
  image:
    media_content_id: |
      media-source://media_source/local/{{ 'birthday.jpg' if is_festive_day() else 'kitchen.jpg' }}
```

## Weitere vollständige Konfigurationsbeispiele

Die folgenden Beispiele ergänzen die zuvor verkürzten Muster. YAML-Kommentare und technische Bezeichner sind wie im englischen Original belassen.

### YAML-Anker innerhalb einer Entity-Liste

Der erste Entity-Eintrag definiert `&width`; der zweite übernimmt die Formatierung mit `<<: *width`. Das ist ein flacher YAML-Merge, kein Ersatz für die rekursive Foundry-Vererbung.

```yaml
uix_foundries:
  browser_multiple_entity_anchors:
    forge:
      mold: row
      billets:
        id: my_browser_id
    element:
      type: custom:multiple-entity-row
      entity: binary_sensor.{{ id }}
      entities:
        - entity: sensor.{{ id }}_browser_battery
          <<: &width                    # define anchor inline on first use
            format: precision2
            styles:
              text-align: center
        - entity: sensor.{{ id }}_browser_height
          <<: *width                    # reuse the same formatting options
```

### Vollständige Foundry-Struktur

`forge.uix` gestaltet den Wrapper, während `element` den erzeugten Kartentyp und seine Eigenschaften festlegt.

```yaml
forge:
  mold: card
  uix:
    style:
      hui-tile-card $: |
        ha-card {
          --tile-color: red !important;
        }
element:
  type: tile
  entity: "{{ 'sun.sun' }}"
```

### Inhalt der eingebundenen Styling-Datei

Die eingebundene Datei liefert den vollständigen Wert für den Schlüssel, den `!include` ersetzt. Im Beispiel ist das die Zuordnung mit `style`.

```yaml
# /config/uix/my_forge_styles.yaml
style: "ha-card { background: teal; }"
```

### Include in einer Datei-Foundry

Datei-Foundries verwenden den nativen Home-Assistant-YAML-Loader; `!include` benötigt dort keine Anführungszeichen.

```yaml
# In a YAML File Foundry — no quoting needed
uix_foundries:
  my_tile:
    forge:
      mold: card
    element:
      type: tile
      entity: "{{ config.entity }}"
      uix: !include uix/my_forge_styles.yaml
```

### Secrets als Ausgangsdatei

Die Datei `secrets.yaml` liegt im HA-Konfigurationsverzeichnis. Die hier gezeigten Werte sind nur Demonstrationswerte.

```yaml
# /config/secrets.yaml
accent_colour: teal
lock_pin: "1234"
```

### Secret in einer Datei-Foundry

Die Datei-Foundry liest `accent_colour` mit einem ungequoteten `!secret`-Tag in ein Billet ein. In einer UI Foundry muss der Tag dagegen als String gequotet sein.

```yaml
# In a YAML File Foundry — no quoting needed
uix_foundries:
  my_tile:
    forge:
      mold: card
      billets:
        accent: !secret accent_colour
    element:
      type: tile
      entity: "{{ config.entity }}"
```

### Ausgangs-Foundry für das Merge-Beispiel

Die Foundry definiert Makroimport, Kartentyp und Standardwerte.

```yaml
forge:
  mold: card
  macros:
    entity_color: "my_macros.jinja"
element:
  type: weather-forecast
  show_current: true
  show_forecast: false
```

### Aufgelöstes Merge-Ergebnis

Die lokale Entität und `show_forecast` überschreiben die Vorlage; `show_current` und der Makroimport bleiben erhalten.

```yaml
forge:
  mold: card
  macros:
    entity_color: "my_macros.jinja"
element:
  type: weather-forecast
  entity: weather.home        # from element
  show_current: true          # from foundry
  show_forecast: true         # overridden by element
```

### Basis einer verschachtelten Foundry

`base_tile` enthält das gemeinsame Styling und den Kartentyp; die oben gezeigte Foundry `light_tile` erweitert diese Basis.

```yaml
forge:
  mold: card
  uix:
    style:
      hui-tile-card $: |
        ha-card {
          border-radius: 20px;
        }
element:
  type: tile
```

### Billet-Standard unverändert übernehmen

Ohne lokales Billet bleibt der in `accent_tile` definierte Wert `teal` erhalten.

```yaml
type: custom:uix-forge
foundry: accent_tile
entity: light.bed_light
```

![Billet-Standard unverändert übernehmen](/projects/uix/assets/page-assets/forge/foundries-billets.png)

### Vollständige Foundry mit leeren Slots

`~` definiert leere Billets. Der Name verwendet einen Fallback; das Styling wird nur bei gesetztem `accent` ausgegeben.

```yaml
forge:
  mold: card
  billets:
    accent: ~          # empty slot — instance is expected to override this
    label: ~           # optional label, templates handle none gracefully
element:
  type: tile
  entity: "{{ config.entity }}"
  name: "{{ label or state_attr(config.entity, 'friendly_name') }}"
  uix:
    style: |
      ha-card {
        {%- if accent %}
        --tile-color: {{ accent }} !important;
        {%- endif %}
      }
```

### Nur den Akzent setzen

Die Instanz belegt den Akzent, lässt `label` leer und verwendet damit den Friendly Name der Entität.

```yaml
type: custom:uix-forge
foundry: flexible_tile
entity: light.bed_light
forge:
  billets:
    accent: teal
```

![Nur den Akzent setzen](/projects/uix/assets/page-assets/forge/foundries-billets-empty.png)

### Akzent und Beschriftung setzen

Beide Slots werden lokal belegt; die Foundry selbst bleibt unverändert.

```yaml
type: custom:uix-forge
foundry: flexible_tile
entity: light.bed_light
forge:
  billets:
    accent: pink
    label: Bed sconce
```

![Akzent und Beschriftung setzen](/projects/uix/assets/page-assets/forge/foundries-billets-empty2.png)

### Styling-Basis für styled_tile

Die Foundry liefert die Selektorzuordnung. Das bereits gezeigte lokale Styling im Schlüssel `.` ergänzt diese Basis.

```yaml
# Foundry: "styled_tile"
forge:
  mold: card
  uix:
    style:
      hui-tile-card $: |
        ha-card {
          --tile-color: red !important;
        }
element:
  type: tile
```
