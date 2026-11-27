---
title: Configuration Spark
description: Modifier la configuration Forge ou la sortie d'une stratégie avant son affichage.
---

# Configuration Spark

::: info Disponible à partir de 9.2.0-beta.3
Fonction de développement ; la base stable reste 9.1.0. Cette page est une synthèse française avec les exemples canoniques inchangés. La référence anglaise détaille chaque option.
:::

Ajoutez un Spark `type: config` dans `forge.sparks`. Chaque modification est un patch ; l'ordre de la liste est l'ordre d'application. Le Spark peut ajouter une carte, retirer une section ou changer une option avant le rendu HA. Ici, `original-states` crée les cartes et `prepend` ajoute une carte Markdown pleine largeur au début de `cards`.

![Carte ajoutée à une stratégie de vue](/projects/uix/assets/page-assets/forge/config-spark-strategy.png)

```yaml
title: Forge strategy configuration
views:
  - path: overview
    strategy:
      type: custom:uix-forge
      forge:
        mold: strategy
        sparks:
          - type: config
            patches:
              - op: prepend
                path: /cards
                value:
                  type: markdown
                  content: "## Added by Forge"
                  grid_options:
                    columns: full
      element:
        type: original-states
```


## Chemins et opérations {#paths-and-operations}

`path` est un [JSON Pointer](https://www.rfc-editor.org/rfc/rfc6901) : `/cards` désigne la liste, `/cards/0` sa première carte, `""` la configuration entière. Échappez `/` et `~` dans les clés avec `~1` et `~0`. Contrairement à JSONPath, un pointeur donne une adresse exacte. Utilisez `select` pour trouver un élément susceptible de changer de position.

| Opération | Effet |
| --- | --- |
| `merge` | Fusionner un mapping sans supprimer ses autres clés ; une liste, un scalaire ou `null` remplace la valeur. |
| `replace` | Remplacer une valeur ou toute la configuration. |
| `remove` | Supprimer une clé ou un élément existant. |
| `remove_matching` | Supprimer les éléments correspondant à `where`. |
| `wrap_strategy` | Envelopper une stratégie enfant en préservant sa configuration. |
| `wrap_card` | Envelopper une carte générée en préservant sa configuration. |
| `append` / `prepend` | Ajouter en fin / début de liste. |
| `insert_before` / `insert_after` | Insérer à côté d'un élément choisi. |

### Champs des patches {#patch-fields}

`op` définit l'opération. Chaque patch choisit exactement une cible : `path` pour une adresse, `select` pour un élément, ou `all` pour toutes les listes portant un nom. `all` s'utilise avec `remove_matching` et `wrap_card` ; `value` contient les données à écrire, `where` filtre les éléments. Pour `wrap_card` avec `all`, `required: false` autorise zéro carte.

### Sélecteurs et filtres {#select-and-where-matchers}

Sous `select`, `in` désigne la liste, `match` identifie un seul élément, `path` désigne éventuellement un champ de cet élément. Sans ce dernier, la cible est l'élément lui-même. `required` vaut `true` ; `false` ignore l'absence de résultat, mais pas plusieurs résultats.

`select.match` et `where` utilisent les mêmes règles : correspondance partielle de mappings (`type: tile`), `$contains: [...]` exigeant un élément distinct par règle, et `$in_entities: no_favs` faisant référence aux IDs d'un Entities Spark de la même Forge. Ce patch supprime les cartes dont le propre `entity` correspond, indépendamment du type.

```yaml
- op: remove_matching
  all: cards
  where:
    entity:
      $in_entities: no_favs
```


Ajoutez `type: tile` dans `where` pour limiter la suppression aux Tiles.

```yaml
- op: remove_matching
  all: cards
  where:
    type: tile
    entity:
      $in_entities: no_favs
```


`all: cards` visite aussi les listes dans les piles et sections ; `all: entities` visite les listes d'entités. Seuls les éléments directs sont comparés, pas leurs cibles de service, conditions ou références imbriquées. Un template dans `value` peut retourner un objet ou une liste JSON avec `| tojson`.

## Stratégies {#strategies}

Un patch s'applique à la sortie de la [stratégie Forge](../forge.md#strategies) : `/views` pour un dashboard, `/cards` ou `/sections` pour une vue. Vérifiez cette sortie avec l'[inspecteur](#inspect-generated-strategies).

### Envelopper une stratégie enfant {#wrap-a-generated-child-strategy}

La stratégie `home` produit des vues, dont Overview utilisant `home-overview` pour générer ses cartes plus tard. `wrap_strategy` sur le champ `strategy` de cette vue permet de modifier ces cartes sans changer les autres vues. `path` ou `select.path` vise ce champ ; `value` apporte notamment `forge.mold: strategy` ou sa Foundry. Forge ajoute `type: custom:uix-forge` et conserve la configuration initiale sous `element_base`.

### Ajouter une carte des personnes {#wrap-the-overview-strategy-to-add-a-people-map}

Cet exemple ajoute People après les résumés tout en conservant les sous-vues des zones. Remplacez les deux trackers ; utilisez le YAML complet à la création et vérifiez [la partie à coller lors d'une modification](#create-or-edit-the-dashboard).

```yaml
title: My Home
views: []
strategy:
  type: custom:uix-forge
  forge:
    mold: strategy
    sparks:
      - type: config
        patches:
          - op: wrap_strategy
            select:
              in: /views
              match:
                strategy:
                  type: home-overview
              path: /strategy
            value:
              forge:
                mold: strategy
                sparks:
                  - type: config
                    patches:
                      - op: insert_after
                        select:
                          in: /sections
                          match:
                            type: grid
                            cards:
                              $contains:
                                - type: home-summary
                        value:
                          type: grid
                          column_span: 4
                          cards:
                            - type: heading
                              heading: People
                              icon: mdi:account-multiple
                              tap_action:
                                action: navigate
                                navigation_path: /map
                            - type: map
                              entities:
                                - device_tracker.phone
                                - device_tracker.tablet
                              grid_options:
                                columns: full
  element:
    type: home
    favorite_entities:
      - light.bed_light
```


![Section People après les résumés](/projects/uix/assets/page-assets/forge/config-spark-people-map.png)

Le patch externe trouve Overview dans `/views`, enveloppe `/strategy` et conserve `favorite_entities`. Le patch interne ajoute People après la section contenant une carte Home Summary. Sur grand écran, les résumés peuvent rester dans la barre latérale, People dans la zone principale. Son en-tête ouvre la carte HA.

### Envelopper les cartes générées {#wrap-generated-cards}

`wrap_card` crée une Card Forge et conserve les paramètres sous `element_base`. Placez les ajouts dans `value`. `path` ou `select` vise une carte ; `all: cards` et `where` visent toutes les cartes correspondantes. `required: false` accepte zéro résultat.

#### Filtrer Maintenance et sa destination {#filter-maintenance-on-home-and-on-the-page-it-opens}

Les développeurs HA préparent un filtrage standard dans la stratégie Home. En attendant, partagez un filtre entre le résumé Maintenance et une sous-vue filtrée. Créez le label `excluded_from_maintenance`, affectez-le aux entités à exclure et gardez le résumé activé. Créez la [Foundry](../foundries.md) `maintenance-exclusions` ci-dessous, puis le dashboard. Adaptez `/filtered-home-maintenance` dans `navigation_path` en conservant `/maintenance` à la fin.

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




```yaml
title: Filtered Home Maintenance
views: []
strategy:
  type: custom:uix-forge
  forge:
    mold: strategy
    sparks:
      - type: config
        patches:
          - op: wrap_strategy
            select:
              in: /views
              match:
                strategy:
                  type: home-overview
              path: /strategy
            value:
              forge:
                mold: strategy
                sparks:
                  - type: config
                    patches:
                      - op: wrap_card
                        all: cards
                        where:
                          type: home-summary
                          summary: maintenance
                        value:
                          foundry: maintenance-exclusions
                          forge:
                            mold: card
                            sparks:
                              - type: home-summary
                                exclude:
                                  - $in_entities: excluded_from_maintenance
                          element:
                            tap_action:
                              action: navigate
                              # Replace this dashboard URL path if different.
                              navigation_path: /filtered-home-maintenance/maintenance
          - op: append
            path: /views
            value:
              title: Maintenance
              path: maintenance
              subview: true
              strategy:
                type: custom:uix-forge
                foundry: maintenance-exclusions
                forge:
                  mold: strategy
                  sparks:
                    - type: config
                      patches:
                        - op: remove_matching
                          all: cards
                          where:
                            entity:
                              $in_entities: excluded_from_maintenance
                element:
                  type: maintenance
  element:
    type: home
```


Le [Home Summary Spark](home-summary.md) filtre le compteur ; `tap_action` ouvre la sous-vue ajoutée.

![Résumé Maintenance filtré](/projects/uix/assets/page-assets/forge/config-spark-maintenance-shortcut.png)

La sous-vue exécute la stratégie Maintenance et réutilise le même filtre pour retirer les cartes dont `entity` correspond. L'élément Carbon dioxide marqué manque ainsi sur l'image. `subview: true` masque l'onglet.

![Sous-vue Maintenance filtrée](/projects/uix/assets/page-assets/forge/config-spark-maintenance-exclusion.png)

::: warning
Le panneau Maintenance natif conserve sa liste initiale. Seule la sous-vue Forge est filtrée, même si les deux utilisent `maintenance`.
:::

Le même principe s'applique aux résumés Lumières ou Sécurité et à leurs stratégies de vue.

### Retirer des suggestions Favorites {#remove-labelled-favorites-suggestions}

Le label `no_favs` permet d'exclure des cartes de Favorites. Cet exemple retire aussi Other areas. Une [requête Entities](entities.md#reuse-a-query-result) collecte les IDs ; deux patches trouvent les sections par leur titre.

```yaml
title: My Home
views: []
strategy:
  type: custom:uix-forge
  forge:
    mold: strategy
    sparks:
      - type: config
        patches:
          - op: wrap_strategy
            select:
              in: /views
              match:
                strategy:
                  type: home-overview
              path: /strategy
            value:
              forge:
                mold: strategy
                sparks:
                  - type: entities
                    id: no_favs
                    filter:
                      include:
                        - label: no_favs
                  - type: config
                    patches:
                      - op: remove_matching
                        select:
                          in: /sections
                          required: false
                          match:
                            cards:
                              $contains:
                                - type: heading
                                  heading: Favorites
                          path: /cards
                        where:
                          entity:
                            $in_entities: no_favs
                      - op: remove
                        select:
                          in: /sections
                          required: false
                          match:
                            type: grid
                            cards:
                              $contains:
                                - type: heading
                                  heading: Other areas
  element:
    type: home
```


Le premier patch cible `/cards` de la section et retire les cartes de tout type avec un `entity` correspondant. Le second retire la section entière. L'absence de section peut être ignorée. Si HA utilise une autre langue, inspectez les titres générés et utilisez leur texte réel.

### Créer ou modifier le dashboard {#create-or-edit-the-dashboard}

Dans l'éditeur complet, collez tout le YAML à partir de `title`, `views` et `strategy`.

::: warning Vérifiez l'éditeur ouvert
Après enregistrement, HA peut ouvrir uniquement la stratégie. Si l'éditeur commence par `type: custom:uix-forge`, collez seulement le contenu de `strategy:` en retirant deux espaces. Sinon, une seconde stratégie imbriquée entraîne « No strategy type found ».
:::

## Examiner les stratégies générées {#inspect-generated-strategies}

Ouvrez Home puis la console DevTools. Les inspecteurs enregistrent leur dernier rapport sur `window.uix_inspect`.

### Trouver la configuration {#find-the-generated-config}

`uix_dashboard_inspect()` fournit `rawConfig` (sauvegarde), `generatedConfig` (rendu) et `strategy` (stratégie racine). Copiez cette dernière dans `element` pour reprendre les options Home. Voir l'[inspecteur dashboard](../../concepts/dom.md#uix_dashboard_inspect-current-dashboard-helper).

```js
uix_dashboard_inspect();
window.uix_inspect.dashboard.strategy;
```


`uix_strategy_inspect(scope, element)` enregistre la sortie dans `window.uix_inspect.strategy.config`. Utilisez `"dashboard"`, `"view"` ou `"section"` et les options prévues pour `element`. Générez d'abord Home puis inspectez son `home-overview` pour conserver les options héritées. Voir l'[inspecteur stratégie](../../concepts/dom.md#uix_strategy_inspectscope-element-strategy-config-helper).

```js
await uix_strategy_inspect("dashboard", window.uix_inspect.dashboard.strategy);
await uix_strategy_inspect(
  "view",
  window.uix_inspect.strategy.config.views.find(
    (view) => view.strategy?.type === "home-overview",
  ).strategy,
);
```


`paths(term)` cherche dans les chemins et valeurs d'aperçu ; `get(path)` lit une valeur précise. Examinez les sections avant de choisir une liste de cartes.

```js
window.uix_inspect.strategy.paths("home-summary");
window.uix_inspect.strategy.paths("Favorites");
window.uix_inspect.strategy.get("/sections");
```


### Essayer un patch {#test-a-patch}

`window.uix_inspect.strategy.test(patches, entitySets?)` applique la liste à une copie et journalise résultat ou erreur, sans modifier le dashboard. Ici, on essaie d'ajouter une carte à la section principale des résumés.

```js
window.uix_inspect.strategy.test([
  {
    op: "append",
    select: {
      in: "/sections",
      match: {
        cards: { $contains: [{ type: "home-summary", summary: "light" }] },
      },
      path: "/cards",
    },
    value: { type: "tile", entity: "light.kitchen" },
  },
]);
```


Le résumé Lumières doit être activé. Sinon, utilisez le `summary` d'une carte trouvée avec `paths("home-summary")`. Pour [exclure des favoris](#remove-labelled-favorites-suggestions), collectez les IDs avec l'[inspecteur Entities](entities.md#inspect-a-list), puis passez-les sous le nom utilisé par `$in_entities`. Conservez le rapport Overview des étapes précédentes.

```js
await uix_entities_inspect({
  type: "custom:uix-forge",
  forge: {
    mold: "strategy",
    sparks: [{
      type: "entities",
      id: "no_favs",
      filter: { include: [{ label: "no_favs" }] },
    }],
  },
  element: { type: "home-overview" },
}, "no_favs");
```




```js
window.uix_inspect.strategy.test(
  [{
    op: "remove_matching",
    select: {
      in: "/sections",
      required: false,
      match: { cards: { $contains: [{ type: "heading", heading: "Favorites" }] } },
      path: "/cards",
    },
    where: { entity: { $in_entities: "no_favs" } },
  }],
  { no_favs: window.uix_inspect.entities.ids },
);
```


### Tester les JSON Pointers visuellement {#try-paths-in-a-json-pointer-tester}

Copiez la configuration depuis DevTools. Dans le [testeur JsonKit](https://jsonkit.com/jsonpath-tester), choisissez JSON Pointer et essayez `/sections/0/cards`. Retirez les données personnelles avant tout collage sur un site externe.

```js
copy(JSON.stringify(window.uix_inspect.strategy.config, null, 2));
```


Utilisez cet outil pour les pointeurs exacts, puis [`test()`](#test-a-patch) pour les règles Forge.

## Erreurs et sortie optionnelle {#safe-failure-and-optional-output}

Un chemin invalide, un type incompatible ou une sélection incorrecte produit une erreur plutôt qu'un résultat partiellement modifié. `select.required: false` ignore un élément absent si sa liste existe ; plusieurs résultats restent une erreur.

```yaml
- op: remove
  select:
    in: /badges
    match:
      type: entity
      entity: sensor.optional_status
    required: false
```







> Synthèse française de [UIX / Lint-Free-Technology](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source `dev` / **9.2.0-beta.3**, révision [6a2bad2](https://github.com/Lint-Free-Technology/uix/commit/6a2bad250e1af75b058353a22371154df23474c8), vérifiée le 2026-11-27. Base stable **9.1.0**, HA **2026.11.0** minimum. La [documentation anglaise](https://uix.lf.technology/) fait autorité.
