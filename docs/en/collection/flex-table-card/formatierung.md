---
title: flex-table-card formatting
description: Format cells of the flex-table-card and adjust values.
---
<a id="flex-table-card-formatting"></a>
<a id="current-focus"></a>

# Formatting {#formatierung}

## Automatic formatting {#automatische-formatierung}

With `auto_format: true`, the card uses home assistant formatting such as unit and precision.

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

Automatic formatting can be switched off for individual columns.

```yaml
columns:
  - name: Min.
    data: min_temp
    suffix: " °C"
    no_auto_format: true
```

## Prefix, suffix and alignment {#prefix-suffix-und-ausrichtung}

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

## Format helper {#format-helfer}

`fmt` uses built-in formatters.

| Format | Purpose |
| --- | --- |
| `number` | Convert value to number |
| `duration` | Show seconds as time duration |
| `duration_h` | show longer duration with days |
| `icon` | Show MDI icon |
| `full_datetime` | Convert date string to timestamp |
| `hours_passed` | past hours since date |
| `hours_mins_passed` | past hours and minutes |
| `time_passed` | past time with rough readability |

```yaml
columns:
  - name: Batterie
    data: state
    fmt: number
    suffix: "%"
    align: right
```

## Modify {#modify}

`modify` is JavaScript and gets the read cell value as `x`.

```yaml
columns:
  - name: Richtung
    data: sendungsinfo.sendungsrichtung
    modify: x == "ANKOMMEND" ? "zu mir" : "von mir"
```

::: danger safety
`modify` executes JavaScript. Only use it with data whose source you trust.
:::
