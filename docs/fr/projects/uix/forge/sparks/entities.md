---
title: Entities Spark
description: Filtrer des entités pour remplir une carte ou collecter des IDs réutilisables.
---

# Entities Spark

::: info Disponible à partir de 9.2.0-beta.3
Fonction de développement ; base stable 9.1.0. Synthèse française avec exemples canoniques inchangés.
:::

Le Spark remplit une carte Entities, crée des Tiles ou collecte des IDs pour d'autres Sparks. Il utilise les règles du [fork auto-entities de Lint Free Technology](https://github.com/Lint-Free-Technology/lovelace-auto-entities).

## Créer des cartes sans enveloppe auto-entities {#create-cards-without-an-auto-entities-wrapper}

Ce Grid crée une Tile par entité de `bedroom`, hors `unavailable`. Adaptez la zone. `path: /cards` remplit la liste et le Spark `element` définit chaque carte ; Forge renseigne `entity`.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: entities
      path: /cards
      element:
        type: tile
      filter:
        include:
          - area: bedroom
        exclude:
          - state: unavailable
element:
  type: grid
  columns: 2
  square: false
  cards: []
```


![Tiles générées par Entities Spark](/projects/uix/assets/page-assets/forge/entities-spark-grid.png)

## Options {#spark-options}

| Option | Description |
| --- | --- |
| `type` | Valeur obligatoire `entities`. |
| `id` / `spark_id` | Identifiant réutilisable ; obligatoire sans `path`. |
| `path` | JSON Pointer dans `element`, par exemple `/entities` ou `/cards`. Le parent doit exister ; sans chemin, collecte seule. |
| `mode` | `append` par défaut, `prepend` ou `replace`. Première occurrence de chaque ID conservée. |
| `entities` | IDs explicites ajoutés avant les filtres ; les exclusions restent applicables. |
| `filter.include` | Ajouter les entités correspondant à au moins un filtre ; `[{}]` sélectionne toutes les entités accessibles. |
| `filter.exclude` | Retirer les correspondances après les inclusions. |
| `sort` | Mapping ou liste pour trier, grouper ou limiter. |
| `element` | Configuration copiée par entité ; sans elle, écrire les IDs seuls. |
| `entity_path` | Chemin de l'ID dans chaque copie, `/entity` par défaut. |

Avec append/prepend, les entrées existantes doivent être du même format : chaînes ou mappings avec le même `entity_path`. Les lignes divider/section sont acceptées. `mode: replace` remplace toute la liste.

### Filtres {#filters}

Les inclusions sont combinées par OU, puis les exclusions retirées. Toutes les règles d'un même filtre doivent correspondre. Seules les entités dont HA fournit un état à l'utilisateur sont examinées. Texte exact, jokers entre guillemets, expressions régulières entre `/`, comparaisons comme `">= 20"` et motifs JSON préfixés `$$` sont acceptés. Le champ doit avoir une valeur : `area: "*"` exige une zone. Le format `active_choice` de l'éditeur auto-entities est reconnu.

| Règle | Comparaison |
| --- | --- |
| `domain` | Domaine avant le point de l'ID. |
| `entity_id` | ID complet. |
| `name` | Nom convivial. |
| `state` | État, liste de conditions ou comparaison avec une autre entité. |
| `state_translated` | État traduit dans HA ; utiliser `state` pour les nombres. |
| `attributes` | Tous les attributs doivent correspondre ; `:` pour les chemins imbriqués. |
| `group` | Membres directs d'un groupe. |
| `group_expanded` | Membres, sous-groupes développés. |
| `area` | Nom/ID de zone, y compris celle héritée du dispositif. |
| `floor` | Nom/ID d'étage depuis la zone propre ou héritée. |
| `level` | Niveau numérique de l'étage. |
| `device` | ID, nom attribué ou nom initial du dispositif. |
| `device_manufacturer` / `device_model` | Fabricant ou modèle. |
| `label` | Nom/ID de label sur l'entité ou le dispositif. |
| `integration` | Nom d'intégration ou ID d'une entrée de configuration. |
| `hidden_by` | Masqué par `user` ou `integration` ; l'état doit rester disponible. |
| `entity_category` | Catégorie de registre, par exemple config/diagnostic. |
| `last_changed` / `last_updated` / `last_triggered` | Temps depuis changement, mise à jour ou déclenchement ; `"< 15"` signifie moins de 15 minutes, `"< 2 h ago"` moins de deux heures. |
| `and` | Tous les sous-filtres. |
| `or` | Au moins un sous-filtre. |
| `not` | Le sous-filtre ne doit pas correspondre. |

Exemple : batteries de Garage, hors indisponibles.

```yaml
filter:
  include:
    - area: Garage
      attributes:
        device_class: battery
  exclude:
    - state: unavailable
```


Pour les batteries sous 20 %, utilisez ce filtre. Le seuil peut provenir d'un helper : remplacez `value` par `entity_id: input_number.battery_threshold` avec `operator: "<"`.

```yaml
filter:
  include:
    - attributes:
        device_class: battery
        unit_of_measurement: "%"
      state:
        operator: "<"
        value: 20
```


Forge attend 500 ms après une mise à jour pertinente pour regrouper les changements. Les conditions temporelles sont revérifiées lors des mises à jour HA. Les stratégies suivent leurs [règles de génération](../forge.md#strategies). Pour migrer auto-entities, placez les règles dans `filter`, le chemin de sortie dans `path`, les options par entrée dans le Spark `element`. Utilisez plusieurs Sparks pour des groupes ayant des réglages différents.

## Lignes Entities sans auto-entities {#generate-entity-rows-without-auto-entities}

Omettez le Spark `element` pour écrire directement les IDs dans la liste `entities`.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: entities
      path: /entities
      filter:
        include:
          - attributes:
              device_class: battery
        exclude:
          - state: unavailable
      sort:
        method: name
element:
  type: entities
  title: Batteries
  entities: []
```


Le filtre `auto-entities` appartient maintenant au Spark ; les options de carte vont dans le `element` externe.

## Écrire les IDs ailleurs {#write-entity-ids-at-another-path}

Si le schéma n'utilise pas `/entity`, définissez `entity_path` relatif à chaque mapping généré.

```yaml
- type: entities
  path: /some_list
  element:
    target: {}
  entity_path: /target/entity_id
  filter:
    include:
      - area: Garage
```


## Grouper les lignes {#group-entity-rows}

`sort.method` accepte une méthode ou une liste par priorité : `none`, `domain`, `entity_id`, `name`, `friendly_name`, `device`, `area`, `state`, `attribute`, `last_changed`, `last_updated`, `last_triggered`. Avec attribute, précisez son chemin. Options : `reverse`, `ignore_case`, `ip`, `numeric`, dont `nan_first`/`nan_last`. `count: 5` au premier niveau limite à cinq ; `first` saute des entrées avant cette limite. Les requêtes nommées conservent tous les IDs.

`divider: true` ajoute des séparations. `section: true` ajoute un titre avant chaque groupe, y compris le premier, et prime sur divider. Réservé aux listes de lignes Entities ou `custom:fold-entity-row`, sans Spark `element`.

### Séparateurs {#add-dividers-between-groups}

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: entities
      path: /entities
      filter:
        include:
          - domain: sensor
      sort:
        - method: area
          divider: true
        - method: name
element:
  type: entities
  title: Sensors by area
  entities: []
```


Forge ajoute `{ type: divider }` entre les zones, retire les IDs dupliqués et les séparateurs initiaux, finaux ou consécutifs lors de la fusion.

### Titres de groupe {#add-a-heading-above-each-group}

Sans `label`, le titre reprend la valeur de tri. Sinon, composez-le avec `entity`, `device`, `area`, `floor` ou `text` depuis la première entité. `separator` définit leur séparateur.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: entities
      path: /entities
      filter:
        include:
          - domain: sensor
      sort:
        - method: area
          section: true
          label:
            - type: text
              text: "Area: "
            - area
          separator: ""
        - method: name
element:
  type: entities
  title: Sensors by area
  entities: []
```


Cela produit `{ type: section, label: "Area: Kitchen" }` avant Kitchen. Les séparateurs voisins et titres identiques adjacents sont fusionnés ; les titres de début/fin restent.

## Réutiliser une requête {#reuse-a-query-result}

Attribuez une `id` unique et omettez `path` pour une requête seule. Elle accepte `entities`/`filter` sans modifier la configuration. Omettez `mode`, `sort`, `element`, `entity_path`. Le [Configuration Spark](config.md#select-and-where-matchers) lit `$in_entities: <id>` dans la même Forge, même si le Spark écrit aussi une liste. Le [Home Summary Spark](home-summary.md#reuse-an-entities-spark-filter) exige une requête seule dans la même Card Forge. Les templates lisent `uixForge.entities["<id>"]` depuis une requête seule.

### Résultat dans les templates {#use-a-query-result-in-templates}

La carte Shortcut compte les entités portant `excluded_from_maintenance`. Sa description suit les modifications de liste. Les crochets permettent les IDs avec tirets.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: entities
      id: excluded_from_maintenance
      filter:
        include:
          - label: excluded_from_maintenance
element:
  type: shortcut
  label: Maintenance exclusions
  description: >-
    {{ uixForge.entities["excluded_from_maintenance"] | count }} excluded entities
```


Forge évalue les paramètres des Sparks avant de rendre leurs résultats disponibles aux templates d'élément et de style de l'enveloppe. Chaque requête doit avoir une ID unique.

### Partager une Foundry {#reuse-an-entities-foundry-query-in-another-element}

Enregistrez le filtre dans la [Foundry](../foundries.md) `maintenance-exclusions`, sans `path`, pour que chaque Forge décide de son utilisation.

```yaml
# Foundry: maintenance-exclusions
forge:
  sparks:
    - type: entities
      id: excluded_from_maintenance
      filter:
        include:
          - label: excluded_from_maintenance
```


Le [dashboard Maintenance filtré](config.md#wrap-generated-cards) lit cette requête avec `$in_entities`. Pour une carte Entities, répétez `type`/`id` et ajoutez `path: /entities`.

```yaml
type: custom:uix-forge
foundry: maintenance-exclusions
forge:
  mold: card
  sparks:
    - type: entities
      id: excluded_from_maintenance
      path: /entities
      mode: replace
element:
  type: entities
  title: Excluded from Maintenance
  entities: []
```


Forge fusionne par type et ID. La carte écrit dans `/entities`, tandis que les autres Forges exécutent leur propre requête seule depuis la même Foundry.

## Examiner une liste {#inspect-a-list}

`uix_entities_inspect` enregistre le rapport dans `window.uix_inspect.entities` : `ids` sélectionnés, `entries` générées, `counts` par inclusion avant exclusions. Voir l'[inspecteur Entities](../../concepts/dom.md#uix_entities_inspectforge-spark-entities-spark-helper). Sélectionnez `<uix-forge>` dans Elements puis utilisez `$0` dans Console.

```js
await uix_entities_inspect($0);
window.uix_inspect.entities.ids;
```


Avec plusieurs Sparks, passez `id`/`spark_id` ou une position commençant à `0` en second argument. Pour une stratégie, passez sa configuration JavaScript à partir de `type: custom:uix-forge` sous `strategy:`. Cet exemple suppose la Foundry du [dashboard filtré](config.md#wrap-generated-cards).

```js
await uix_entities_inspect({
  type: "custom:uix-forge",
  foundry: "maintenance-exclusions",
  forge: { mold: "strategy" },
  element: { type: "maintenance" },
}, "excluded_from_maintenance");
window.uix_inspect.entities.ids;
```


Lecture seule. Pour essayer des patches avec ces IDs, voir [le test des patches](config.md#test-a-patch).




> Synthèse française de [UIX / Lint-Free-Technology](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source `dev` / **9.2.0-beta.3**, révision [6a2bad2](https://github.com/Lint-Free-Technology/uix/commit/6a2bad250e1af75b058353a22371154df23474c8), vérifiée le 2026-11-27. Base stable **9.1.0**, HA **2026.11.0** minimum. La [documentation anglaise](https://uix.lf.technology/) fait autorité.
