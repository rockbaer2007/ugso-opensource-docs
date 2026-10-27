---
title: Formatage de la `flex-table-card`
description: Formater les cellules de la `flex-table-card` et ajuster les valeurs.
---
<a id="flex-table-card-formatage"></a>
<a id="orientation-actuelle"></a>

# Formatage {#formatierung}

## Formatage automatique {#automatische-formatierung}

Avec `auto_format: true`, la carte utilise les paramètres de formatage de Home Assistant, tels que l'unité et la précision.

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

Le formatage automatique peut être désactivé pour des colonnes spécifiques.

```yaml
columns:
  - name: Min.
    data: min_temp
    suffix: " °C"
    no_auto_format: true
```

## Préfixe, suffixe et alignement {#prefix-suffix-und-ausrichtung}

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

## Assistants de formatage {#format-helfer}

`fmt` utilise des formateurs intégrés.

| Format | Fonction |
| --- | --- |
| `number` | Convertir une valeur en nombre |
| `duration` | Afficher des secondes sous forme de durée |
| `duration_h` | Afficher une durée plus longue incluant les jours |
| `icon` | Afficher une icône MDI |
| `full_datetime` | Convertir une date textuelle en horodatage |
| `hours_passed` | Heures écoulées depuis une date |
| `hours_mins_passed` | Heures et minutes écoulées |
| `time_passed` | Temps écoulé dans un format approximatif lisible |

```yaml
columns:
  - name: Batterie
    data: state
    fmt: number
    suffix: "%"
    align: right
```

## Modification {#modify}

`modify` est du code JavaScript qui reçoit la valeur lue dans la cellule sous le nom `x`.

```yaml
columns:
  - name: Richtung
    data: sendungsinfo.sendungsrichtung
    modify: x == "ANKOMMEND" ? "zu mir" : "von mir"
```

::: danger Sécurité
`modify` exécute du code JavaScript. Ne l'utilisez qu'avec des données provenant de sources en lesquelles vous avez confiance.
:::
