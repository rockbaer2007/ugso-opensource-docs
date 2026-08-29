---
title: flex-table-card Formatierung
description: Zellen der flex-table-card formatieren und Werte anpassen.
---
# Formatierung

## Automatische Formatierung

Mit `auto_format: true` nutzt die Karte Home-Assistant-Formatierungen wie Einheit und Genauigkeit.

```yaml
type: custom:flex-table-card
title: Temperatur
entities:
  include: sensor.outdoor_sensor_air_temperature
auto_format: true
columns:
  - name: Temperatur
    data: state
```

Für einzelne Spalten kann die automatische Formatierung abgeschaltet werden.

```yaml
columns:
  - name: Min.
    data: min_temp
    suffix: " °C"
    no_auto_format: true
```

## Prefix, Suffix und Ausrichtung

```yaml
type: custom:flex-table-card
title: Verbrauch
entities:
  include: sensor.*_energy*
sort_by: power-
columns:
  - name: Name
    data: name
  - name: Leistung
    id: power
    data: power_consumption
    modify: parseFloat(x)
    suffix: " W"
    align: right
  - name: Energie
    data: state
    modify: parseFloat(x).toFixed(1)
    suffix: " kWh"
    align: right
```

## Format-Helfer

`fmt` nutzt eingebaute Formatierer.

| Format | Zweck |
| --- | --- |
| `number` | Wert in Zahl umwandeln |
| `duration` | Sekunden als Zeitdauer anzeigen |
| `duration_h` | längere Dauer mit Tagen anzeigen |
| `icon` | MDI-Icon anzeigen |
| `full_datetime` | Datumsstring in Timestamp umwandeln |
| `hours_passed` | vergangene Stunden seit Datum |
| `hours_mins_passed` | vergangene Stunden und Minuten |
| `time_passed` | vergangene Zeit mit grober Lesbarkeit |

```yaml
columns:
  - name: Batterie
    data: state
    fmt: number
    suffix: "%"
    align: right
```

## Modify

`modify` ist JavaScript und bekommt den gelesenen Zellwert als `x`.

```yaml
columns:
  - name: Richtung
    data: sendungsinfo.sendungsrichtung
    modify: x == "ANKOMMEND" ? "zu mir" : "von mir"
```

::: danger Sicherheit
`modify` fuehrt JavaScript aus. Nutze es nur mit Daten, deren Quelle du vertraust.
:::

