---
title: flex-table-card data sources
description: Read data from entities, attributes, actions and static data.
---
<a id="flex-table-card-data-sources"></a>
<a id="current-focus"></a>

# Data sources {#datenquellen}

## Data from entities {#daten-aus-entitaten}

The value at `data` determines what is displayed in a column.

```yaml
columns:
  - name: Name
    data: name
  - name: Entity-ID
    data: entity_id
  - name: Status
    data: state
  - name: Icon
    data: icon
```

Commonly used selectors:

| selector | Meaning |
| --- | --- |
| `name` | friendly name |
| `object_id` | Entity ID without domain |
| `entity_id` | complete entity ID |
| `state` | current status |
| `icon` | Entity icon |
| `area` | Range if available |
| `floor` | floor if available |
| `device` | Device name if available |
| `platform` | Domain, for example `sensor` |

## Nested attributes {#verschachtelte-attribute}

Nested objects are read using dot notation.

```yaml
columns:
  - name: Status
    data: sendungsdetails.sendungsverlauf.status
  - name: Nummer
    data: sendungsdetails.sendungsnummern.sendungsnummer
```

## Multiple values in one column {#mehrere-werte-in-einer-spalte}

Multiple selectors can be combined with comma.

```yaml
columns:
  - name: Raum und Geraet
    data: area,device
    multi_delimiter: " / "
```

## Static data {#statische-daten}

`static_data` can be used for tables without home assistant entities.

```yaml
type: custom:flex-table-card
title: AQI-Stufen
entities: []
columns:
  - name: AQI
    data: aqi.level
  - name: Kategorie
    data: aqi.category
  - name: Hinweis
    data: aqi.concerns
static_data:
  aqi:
    - level: 0-50
      category: Gut
      concerns: Kaum Risiko.
    - level: 51-100
      category: Moderat
      concerns: Fuer empfindliche Personen moeglichweise relevant.
```

Original sample image: [AirQualityIndex.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/AirQualityIndex.png)
