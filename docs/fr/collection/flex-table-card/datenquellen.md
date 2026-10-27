---
title: Sources de données pour flex-table-card
description: Récupérez des données à partir d'entités, d'attributs, d'actions et de données statiques.
---
<a id="flex-table-card-sources-de-donnees"></a>
<a id="orientation-actuelle"></a>

# Sources de données {#datenquellen}

## Données issues d'entités {#daten-aus-entitaten}

La valeur définie pour `data` détermine le contenu affiché dans une colonne.

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

Sélecteurs couramment utilisés :

| Sélecteur | Signification |
| --- | --- |
| `name` | Nom convivial |
| `object_id` | ID d'entité sans domaine |
| `entity_id` | ID d'entité complet |
| `state` | État actuel |
| `icon` | Icône de l'entité |
| `area` | Zone, si disponible |
| `floor` | Étage, si disponible |
| `device` | Nom de l'appareil, si disponible |
| `platform` | Domaine, par exemple `sensor` |

## Attributs imbriqués {#verschachtelte-attribute}

L'accès aux objets imbriqués s'effectue à l'aide de la notation par points.

```yaml
columns:
  - name: Status
    data: sendungsdetails.sendungsverlauf.status
  - name: Nummer
    data: sendungsdetails.sendungsnummern.sendungsnummer
```

## Valeurs multiples dans une seule colonne {#mehrere-werte-in-einer-spalte}

Il est possible de combiner plusieurs sélecteurs à l'aide d'une virgule.

```yaml
columns:
  - name: Raum und Geraet
    data: area,device
    multi_delimiter: " / "
```

## Données statiques {#statische-daten}

Pour les tableaux ne faisant pas appel à des entités Home Assistant, `static_data` peut être utilisé.

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

Exemple d'image original : [AirQualityIndex.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/AirQualityIndex.png)
