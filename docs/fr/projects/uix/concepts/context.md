---
description: Définir un comportement structuré pour certaines zones de l’interface Home Assistant avec les contextes UIX.
---

> Traduit de la [documentation anglaise d’UIX](https://github.com/Lint-Free-Technology/uix/blob/509b2c2475ce6b574876a8353f88aedf87e7b2e3/docs/source/concepts/context.md) de Lint-Free-Technology/uix sous [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source vérifiée **9.1.0-beta.2**. Base stable **9.0.0**, Home Assistant **2026.11.0** minimum.

# Contextes UIX

::: info Disponibilité
Les contextes UIX et le contexte de nom d’entité sont disponibles depuis la version **9.0.0-beta.3**.
:::

Les contextes UIX définissent un comportement structuré pour un hôte UIX et tous ses descendants. Les éléments peuvent ainsi tenir compte de leur emplacement dans l’interface sans que chacun ait besoin de ses propres règles de sélection.

## Définir un contexte

Les liaisons de thème utilisent `uix-<thing>-context-yaml` sur n’importe quelle cible UIX. La valeur est une liste YAML de liaisons. `anchor` détermine la portée de la liaison avec la même [syntaxe de sélection hôte/élément](dom.md#selection-de-chemin-hote-element) que les styles UIX. La première liaison correspondante s’applique.

Un élément qui accepte déjà `uix:` peut définir directement un contexte avec `uix.context`. Sur un même hôte, la configuration directe prime sur une liaison de thème correspondante.

Un contexte s’applique aussi aux descendants de son hôte. Le contexte d’une vue atteint donc ses cartes et ses lignes. Une carte ou une ligne peut définir un contexte plus précis pour sa propre branche.

## Contexte de nom d’entité

`entity_name` détermine les composants des noms d’entité générés automatiquement. Un nom d’affichage personnalisé par l’utilisateur est conservé.

### Exemple pour le tableau de bord Énergie

```yaml
my-uix-theme:
  uix-theme: my-uix-theme
  uix-root-context-yaml: |
    - anchor: "&ha-panel-energy"
      entity_name:
        rules:
          - when:
              request: [parent_device, device]
            use: [entity]
```

Dans le tableau de bord Énergie, cet exemple remplace les composants du nom correspondant à l’appareil parent et à l’appareil par le seul nom d’entité.

### Exemple pour une vue

Une vue peut utiliser la cible `view` pour masquer les noms d’appareil répétés dans ses cartes. Une demande de nom d’appareil et d’entité renvoie alors uniquement le nom d’entité.

```yaml
my-uix-theme:
  uix-theme: my-uix-theme
  uix-view-context-yaml: |
    - anchor: "&hui-view"
      entity_name:
        rules:
          - when:
              request: [device, entity]
            use: [entity]
```

Une carte peut définir une exception plus précise avec `uix.context` lorsqu’une entité a besoin de son nom d’appareil.

### Exemple pour une carte

Une carte peut utiliser la cible `card` pour masquer les noms d’appareil répétés dans ses lignes. Une demande de nom d’appareil et d’entité renvoie alors uniquement le nom d’entité. Ici, seules les cartes d’entités portant la classe UIX `type-entities` correspondent.

```yaml
  uix-card-context-yaml: |
    - anchor: "&.type-entities"
      entity_name:
        rules:
          - when:
              - request: default
              - request: [device, entity]
            use: [entity]
```

### Exemple de configuration directe d’une carte

Vous pouvez ajouter un contexte directement à une carte.

```yaml
uix:
  context:
    entity_name:
      rules:
        - when:
            - request: default
            - request:
                - device
                - entity
          use:
            - entity
```

### Règles

`when.request` vaut `default` ou contient la liste exacte des composants demandés. `when` peut regrouper plusieurs demandes dans une liste lorsqu’elles partagent le même résultat. `use` accepte la même forme abrégée sous forme de liste. Les valeurs autorisées sont `floor`, `area`, `parent_device`, `device` et `entity`.

```yaml
entity_name:
  rules:
    - when:
        - request: default
        - request: [device, entity]
      use: [entity]
```

Cet exemple utilise le nom d’entité pour une demande par défaut comme pour une demande de nom d’appareil et d’entité.

```yaml
entity_name:
  rules:
    - when:
        request: [parent_device, device]
      use:
        - type: device
        - type: text
          text: "-"
        - type: entity
```

Home Assistant sépare normalement les composants du nom par des espaces. L’exemple produit donc `Device - Entity`. Pour contrôler précisément la ponctuation, utilisez la forme objet et définissez explicitement le séparateur.

```yaml
entity_name:
  rules:
    - when:
        request: [parent_device, device]
      use:
        items:
          - type: device
          - type: text
            text: " — "
          - type: entity
        options:
          separator: ""
```

### Configuration directe

Un élément qui accepte déjà `uix:` peut définir directement un contexte de nom d’entité.

```yaml
uix:
  context:
    entity_name:
      rules:
        - when:
            request: default
          use: [entity]
```

## Débogage

Sélectionnez un élément concerné dans l’inspecteur du navigateur, puis exécutez `uix_context($0)` dans la console. Le résultat affiche les contextes hérités et propose une fonction `format()` pour vérifier une demande de nom précise.

```js
uix_context($0).format("sensor.sun_next_dusk", [
  { type: "device" },
  { type: "entity" },
]);
```

Définissez `debug: true` pendant la configuration du contexte pour journaliser le contexte appliqué et la première correspondance pour chaque règle de nom d’entité.

```yaml
uix:
  context:
    debug: true
    entity_name:
      rules:
        - when:
            request: default
          use: [entity]
```
