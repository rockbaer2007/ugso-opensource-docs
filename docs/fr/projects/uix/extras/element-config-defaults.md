---
title: Valeurs par défaut de configuration des éléments
description: Appliquer des valeurs statiques par défaut aux éléments correspondants des tableaux de bord Home Assistant.
---
> Adapté de la documentation anglaise UIX de [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Vérifié le 08/11/2026 jusqu’à `dev e28976f`, aperçu **9.1.0-beta.1**. Base stable : **9.0.0 / Home Assistant 2026.11.0 minimum**.

# Valeurs par défaut de configuration des éléments

UIX peut ajouter des valeurs statiques par défaut aux éléments correspondants sans modifier le tableau de bord. Les noms d’appareil et d’entité de Home Assistant 2026.11 constituent un exemple : une valeur par défaut peut limiter l’affichage à la partie entité du nom. Il est également possible de compléter des clés ou des chemins d’objet manquants, comme `state_color` ou `group_config.name`.

## Configurer la liste des règles

Ouvrez **Paramètres → Appareils et services → UI eXtension → Configurer**, puis sélectionnez **Configure element defaults**. Choisissez **Configure using UI** pour ajouter des valeurs par défaut avec les champs du formulaire.

Créez une entrée pour chaque clé manquante à compléter. Un élément correspondant peut recevoir plusieurs valeurs par défaut, par exemple pour `name` et `state_color`.

Choisissez **Configure using YAML** pour coller ou modifier la configuration canonique complète. Les deux éditeurs lisent et écrivent les mêmes règles ; vous pouvez passer de l’un à l’autre à tout moment.

```yaml
element_config:
  - uix_type: row
    element_type: entity
    config_key: name
    value:
      type: entity
```

Chaque règle possède quatre clés :

| Clé | Description |
| --- | --- |
| `uix_type` | La limite de configuration UIX : `card`, `badge`, `heading-badge`, `row`, `glance` ou `element`. |
| `element_type` | Le `type` de configuration Home Assistant à reconnaître, par exemple `tile` ou `entity`. |
| `config_key` | Une clé manquante ou un chemin d’objet séparé par des points. Les indices de tableau ne sont pas pris en charge. |
| `value` | La valeur statique à utiliser. |

Collez par exemple cette configuration complète dans **Configure using YAML** pour que les cartes Tile, les lignes d’entité, les entités Glance et les badges d’entité correspondants utilisent uniquement la partie entité du nom affiché :

```yaml
element_config:
  - uix_type: card
    element_type: tile
    config_key: name
    value: { type: entity }
  - uix_type: row
    element_type: entity
    config_key: name
    value: { type: entity }
  - uix_type: glance
    element_type: entity
    config_key: name
    value: { type: entity }
  - uix_type: badge
    element_type: entity
    config_key: name
    value: { type: entity }
```

## Comportement et limites

UIX ajoute une valeur uniquement lorsque la clé est absente. Toute valeur explicite prévaut sur la valeur globale par défaut, y compris `null`, `false`, une chaîne vide, une liste vide ou une map vide.

Les chemins séparés par des points créent les maps d’objet manquantes sans remplacer une valeur existante. Par exemple, `config_key: group_config.name` ajoute `name` si `group_config` est absent ou contient un objet ; il ne fait rien si `group_config` vaut `null`, contient un scalaire ou un tableau. Les règles visant le même type UIX et le même type d’élément ne peuvent pas se chevaucher : configurez soit `group_config`, soit `group_config.name`, pas les deux.

Cet exemple définit un nom par défaut pour chaque enfant d’une Fold Entity Row tout en conservant un réglage `group_config.secondary_info` existant :

```yaml
element_config:
  - uix_type: row
    element_type: custom:fold-entity-row
    config_key: group_config.name
    value: { type: entity }
```

Les lignes d’entité et les entités Glance acceptent la forme mapping normale et la forme compacte sous forme de chaîne de Home Assistant. Pour une règle correspondante `row`/`entity` ou `glance`/`entity`, `- sensor.kitchen_temperature` est temporairement transmis à Home Assistant sous forme de mapping d’entité avec la valeur configurée. La source du tableau de bord conserve la chaîne compacte.

Les valeurs sont statiques. UIX ne traite pas les modèles Jinja, les modèles UIX, les macros ou les billets dans ces valeurs par défaut. Les règles s’appliquent aux limites directes de configuration des cartes, badges, badges d’en-tête, lignes de cartes Entities, entités Glance et éléments Picture Elements, y compris les éléments natifs correspondants rendus par UIX Forge. Les chemins ajoutent des données uniquement dans une configuration correspondante ; ils ne sélectionnent pas d’autres limites d’éléments imbriqués. À l’exception des entités Glance, les dialogues, fonctionnalités de carte, marqueurs de carte géographique et autres limites d’éléments imbriqués ne sont pas inclus.

Les changements s’appliquent aux tableaux de bord connectés à réception de la mise à jour de configuration UIX. UIX reconstruit uniquement la limite de configuration concernée à partir de la configuration d’origine du tableau de bord ; les valeurs générées ne sont pas enregistrées dans celui-ci.
