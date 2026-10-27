---
title: Données externes pour flex-table-card
description: Utilisation d'Auto-Entities, d'actions, de scripts et de fichiers CSV comme sources de données.
---
<a id="flex-table-card-externe-daten"></a>
<a id="orientation-actuelle"></a>

# Données externes {#externe-daten}

## Auto-Entities {#auto-entities}

La carte peut être combinée avec `custom:auto-entities`. Auto-Entities se charge alors du filtrage, tandis que flex-table-card assure l'affichage sous forme de tableau.

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

Exemple d'image original : [Résultat Auto-Entities](https://user-images.githubusercontent.com/16034687/78148053-a98e0600-7434-11ea-8e75-16e942d277f5.png)

## Données issues d'actions Home Assistant {#daten-aus-home-assistant-aktionen}

Home Assistant déplace souvent les structures de données volumineuses depuis les attributs vers les réponses aux actions. flex-table-card peut utiliser ces réponses comme source de données.

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

Important : la carte se met à jour lorsqu'une entité spécifiée change. Par conséquent, dans le cas de données issues d'actions, il convient de renseigner une entité appropriée sous `entities`.

Exemple original : [WeatherServiceExample.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/WeatherServiceExample.png)

## Données issues de scripts {#daten-aus-skripten}

Un script peut également fournir une réponse.

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

Exemple de script :

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

Si `entities: []` est utilisé, le niveau supérieur de la réponse doit contenir directement la structure de liste, par exemple `family`.

Exemple original : [ScriptExample.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/ScriptExample.png)

## Fichiers CSV via un capteur en ligne de commande (Command-Line Sensor) {#csv-dateien-uber-command-line-sensor}

La `flex-table-card` ne lit pas les fichiers directement. La méthode habituelle consiste à utiliser un capteur Home Assistant qui convertit le fichier en attributs JSON.

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

Carte correspondante :

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

Exemple original : [WaterTank.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/WaterTank.png)
