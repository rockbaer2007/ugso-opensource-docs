---
title: flex-table-card external data
description: Auto entities, actions, scripts and CSV files as data sources.
---
<a id="flex-table-card-externe-daten"></a>
<a id="current-focus"></a>

# External data {#externe-daten}

## Auto entities {#auto-entities}

The card can be combined with `custom:auto-entities`. Auto-Entities then takes care of the filtering, flex-table-card the tabular output.

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

Original example image: [Auto-Entities Result](https://user-images.githubusercontent.com/16034687/78148053-a98e0600-7434-11ea-8e75-16e942d277f5.png)

## Data from Home Assistant actions {#daten-aus-home-assistant-aktionen}

Home Assistant moves many larger data structures from attributes into action responses. The flex-table-card can use such answers as a data source.

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

Important: The card updates when a specified entity changes. For action data, there should therefore be a suitable entity under `entities`.

Original example image: [WeatherServiceExample.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/WeatherServiceExample.png)

## Data from scripts {#daten-aus-skripten}

A script can also provide an answer.

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

Example script:

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

If `entities: []` is used, the top level of the response must directly contain the list structure, for example `family`.

Original example image: [ScriptExample.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/ScriptExample.png)

## CSV files via command line sensor {#csv-dateien-uber-command-line-sensor}

The flex-table-card does not read files directly. The usual way is a home assistant sensor that converts the file into JSON attributes.

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

Matching card:

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

Original example image: [WaterTank.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/WaterTank.png)
