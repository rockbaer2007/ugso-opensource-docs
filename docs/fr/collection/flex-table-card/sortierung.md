---
title: Tri dans `flex-table-card`
description: Tri, mode strict et limitation du nombre de lignes dans `flex-table-card`.
---
<a id="flex-table-card-tri"></a>
<a id="orientation-actuelle"></a>

# Tri {#sortierung}

## Tri simple {#einfach-sortieren}

Le tri s'effectue via `sort_by`. Il est recommandé d'attribuer une `id` stable à la colonne concernée.

```yaml
type: custom:flex-table-card
title: Batterielevel
entities:
  include: sensor.*_battery*
strict: true
sort_by: battery+
columns:
  - name: Name
    data: name
  - name: Batterie
    id: battery
    data: state
    fmt: number
    suffix: "%"
    align: right
```

`+` effectue un tri croissant, tandis que `-` effectue un tri décroissant.

## Trier selon plusieurs colonnes {#nach-mehreren-spalten-sortieren}

```yaml
sort_by:
  - battery+
  - name-
```

Une forme abrégée est également possible :

```yaml
sort_by: [battery+, name-]
```

## Mode strict {#strict-mode}

Avec `strict: true`, seules les lignes pour lesquelles toutes les colonnes présentent une valeur correspondante sont affichées.

```yaml
strict: true
```

Cela s'avère particulièrement utile lorsqu'une opération `include` identifie de nombreuses entités, mais que seule une partie d'entre elles possède réellement tous les attributs requis.

## Tri malgré une modification (`modify`) {#sortierung-trotz-modify}

Par défaut, le tri s'effectue sur la base de la valeur obtenue après l'opération `modify`. Si cela ne convient pas, il est possible d'utiliser `sort_unmodified: true` pour baser le tri sur la valeur d'origine.

```yaml
columns:
  - name: Ausgeloest
    id: last_triggered
    data: last_triggered
    sort_unmodified: true
    modify: |-
      if (x) {
        new Date(x).toLocaleString()
      } else {
        "-"
      }
```

C'est particulièrement important pour les dates : une date au format ISO permet un tri correct, contrairement à une chaîne de caractères formatée selon une convention locale.

Exemples d'images :

- [SortModified.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/SortModified.png)
- [SortUnmodified.png](https://raw.githubusercontent.com/custom-cards/flex-table-card/master/images/SortUnmodified.png)
