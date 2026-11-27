---
title: Home Summary Spark
description: Choisir les entités comptées dans une synthèse Home native.
---

# Home Summary Spark

::: info Disponible à partir de 9.2.0-beta.3
Fonction de développement ; la base stable reste 9.1.0.
:::

Choisissez les entités comptées dans Maintenance, Lumières ou Sécurité, par exemple pour exclure la batterie d'une ancienne tablette.

## Filtrer une carte {#filter-one-home-summary-card}

Créez et affectez le label HA aux entités exclues, puis ajoutez cette Card Forge. La logique Maintenance native et les mises à jour des autres entités restent actives.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: home-summary
      exclude:
        - label: excluded_from_maintenance
element:
  type: home-summary
  summary: maintenance
```


Le filtre change le compteur, pas la destination du clic : la page Maintenance standard peut encore montrer les entités exclues. Pour filtrer les deux, utilisez le [dashboard complet](config.md#wrap-generated-cards), qui enveloppe les cartes générées et ouvre une sous-vue filtrée.

## Options {#spark-options}

Une Card Forge accepte un seul Home Summary Spark et doit envelopper `type: home-summary`. Pour une carte générée, utilisez [`wrap_card`](config.md#wrap-generated-cards).

| Option | Valeur et effet |
| --- | --- |
| `type` | Obligatoire : `home-summary`. |
| `include` | Filtres ou références de requêtes ; toutes les entités par défaut. Correspondance avec au moins une entrée ; `include: []` ne compte rien. |
| `exclude` | Filtres ou références, `[]` par défaut. L'exclusion prime sur l'inclusion. |

### Filtres {#filters}

Écrivez les règles directement sous `include`/`exclude`, selon les [filtres Entities](entities.md#filters), par exemple `domain`, `label`, `attributes`. Ici : lumières Browser Mod et entités avec le label d'exclusion.

```yaml
exclude:
  - domain: light
    integration: browser_mod
  - label: excluded_from_maintenance
```


### Partager un filtre Entities {#reuse-an-entities-spark-filter}

Nommez un Entities Spark sans `path` si plusieurs cartes/patches ont besoin de la liste. Home Summary lit `$in_entities` dans la même Card Forge. Le bloc suivant remplace le `forge` du premier exemple.

```yaml
forge:
  mold: card
  sparks:
    - type: entities
      id: excluded_from_maintenance
      filter:
        include:
          - label: excluded_from_maintenance
    - type: home-summary
      exclude:
        - $in_entities: excluded_from_maintenance
```


Pour plusieurs Forges, sauvegardez la requête dans une Foundry ; chacune l'exécute séparément. Voir [partager une Foundry](entities.md#reuse-an-entities-foundry-query-in-another-element).

## Mises à jour {#updates}

Les entités comptées conservent leurs mises à jour en direct. UIX regroupe les changements de filtre sur 500 ms. Le filtre ne concerne que cette carte : autres cartes, destination du clic et actions de service, comme éteindre une zone, restent inchangées.




> Synthèse française de [UIX / Lint-Free-Technology](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source `dev` / **9.2.0-beta.3**, révision [6a2bad2](https://github.com/Lint-Free-Technology/uix/commit/6a2bad250e1af75b058353a22371154df23474c8), vérifiée le 2026-11-27. Base stable **9.1.0**, HA **2026.11.0** minimum. La [documentation anglaise](https://uix.lf.technology/) fait autorité.
