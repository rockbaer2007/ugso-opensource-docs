---
title: flex-table-card externe Daten
description: Auto-Entities, Aktionen, Skripte und CSV-Dateien als Datenquellen.
---
# Externe Daten

## Auto-Entities

Die Karte kann mit `custom:auto-entities` kombiniert werden. Auto-Entities übernimmt dann die Filterung, flex-table-card die tabellarische Ausgabe.

```yaml
type: custom:auto-entities
filter:
  include:
    - entity_id: "/light.luce_*/"
card:
  type: custom:flex-table-card
  title: Auto-Entities Beispiel
  clickable: true
  columns:
    - name: Name
      data: friendly_name
    - name: Status
      data: state
```

Original-Beispielbild: [Auto-Entities Result](https://user-images.githubusercontent.com/16034687/78148053-a98e0600-7434-11ea-8e75-16e942d277f5.png)

## Daten aus Home-Assistant-Aktionen

Home Assistant verschiebt viele größere Datenstrukturen aus Attributen in Aktionsantworten. Die flex-table-card kann solche Antworten als Datenquelle verwenden.

```yaml
type: custom:flex-table-card
title: Wettervorhersage
action: weather.get_forecasts
action_data:
  type: hourly
entities:
  - weather.home
columns:
  - name: Zeit
    data: forecast.datetime
    modify: new Date(x).toLocaleString()
  - name: Temperatur
    data: forecast.temperature
    suffix: " °C"
  - name: Regen
    data: forecast.precipitation_probability
    suffix: "%"
```

Wichtig: Die Karte aktualisiert sich, wenn sich eine angegebene Entität ändert. Bei Aktionsdaten sollte deshalb eine passende Entität unter `entities` stehen.

Original-Beispielbild: [WeatherServiceExample.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/WeatherServiceExample.png)

## Daten aus Skripten

Auch ein Skript kann eine Antwort liefern.

```yaml
type: custom:flex-table-card
title: Script Beispiel
action: script.test_response
entities: []
columns:
  - name: Name
    data: family.name
  - name: Geburtsjahr
    data: family.year
```

Beispielskript:

```yaml
test_response:
  alias: Test Response
  variables:
    family: >
      {% set myfamily = { "family": [
        { "name": "Emil", "year": 2004 },
        { "name": "Tobias", "year": 2007 },
        { "name": "Linus", "year": 2011 }
      ] } %}
      {{ myfamily }}
  sequence:
    - stop: All Done
      response_variable: family
```

Wenn `entities: []` genutzt wird, muss die oberste Ebene der Antwort direkt die Listenstruktur enthalten, zum Beispiel `family`.

Original-Beispielbild: [ScriptExample.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/ScriptExample.png)

## CSV-Dateien über Command-Line-Sensor

Die flex-table-card liest Dateien nicht direkt. Der übliche Weg ist ein Home-Assistant-Sensor, der die Datei in JSON-Attribute umwandelt.

```yaml
command_line:
  - sensor:
      name: Water Tank Refill Logs
      command: >
        curl -s http://<HA-IP>:8123/local/WaterTank.csv |
        jq --slurp --raw-input --raw-output
        '{refill_logs: split("\r\n") | .[1:] | map(split(",")) | map({"startTime": .[0],"startVolume": .[1],"endVolume": .[2],"litersDelivered": .[3],"duration": .[4]})}'
      json_attributes:
        - refill_logs
      scan_interval: 3600
```

Passende Karte:

```yaml
type: custom:flex-table-card
title: Wasser-Tank Befuellung
entities:
  include: sensor.water_tank_refill_logs
columns:
  - name: Start
    data: refill_logs.startTime
    modify: new Date(x).toLocaleString()
  - name: Startvolumen
    data: refill_logs.startVolume
  - name: Endvolumen
    data: refill_logs.endVolume
  - name: Liter
    data: refill_logs.litersDelivered
  - name: Dauer
    data: refill_logs.duration
    suffix: " s"
```

Original-Beispielbild: [WaterTank.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/WaterTank.png)

