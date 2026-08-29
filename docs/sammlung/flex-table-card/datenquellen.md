---
title: flex-table-card Datenquellen
description: Daten aus Entitäten, Attributen, Aktionen und statischen Daten lesen.
---
# Datenquellen

## Daten aus Entitäten

Der Wert bei `data` bestimmt, was in einer Spalte angezeigt wird.

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

Häufig nutzbare Selektoren:

| Selektor | Bedeutung |
| --- | --- |
| `name` | freundlicher Name |
| `object_id` | Entity-ID ohne Domain |
| `entity_id` | komplette Entity-ID |
| `state` | aktueller Status |
| `icon` | Icon der Entität |
| `area` | Bereich, falls verfügbar |
| `floor` | Etage, falls verfügbar |
| `device` | Gerätename, falls verfügbar |
| `platform` | Domain, zum Beispiel `sensor` |

## Verschachtelte Attribute

Verschachtelte Objekte werden per Punktnotation gelesen.

```yaml
columns:
  - name: Status
    data: sendungsdetails.sendungsverlauf.status
  - name: Nummer
    data: sendungsdetails.sendungsnummern.sendungsnummer
```

## Mehrere Werte in einer Spalte

Mehrere Selektoren können mit Komma kombiniert werden.

```yaml
columns:
  - name: Raum und Geraet
    data: area,device
    multi_delimiter: " / "
```

## Statische Daten

Für Tabellen ohne Home-Assistant-Entitäten kann `static_data` genutzt werden.

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

Original-Beispielbild: [AirQualityIndex.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/AirQualityIndex.png)

