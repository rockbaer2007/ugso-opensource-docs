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
