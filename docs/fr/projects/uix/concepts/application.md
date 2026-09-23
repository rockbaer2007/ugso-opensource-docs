---
description: Découvrez comment UI eXtension intervient sur les éléments d'interface de Home Assistant.
---
# Application UIX

UIX prend en charge presque toutes les cartes standard du frontend Home Assistant, ainsi que les cartes personnalisées qui n'utilisent pas le conteneur de rendu moderne de Home Assistant.

::: info Definitions
1. **patch / patching** : UIX injecte du code dans la classe de l'élément.
2. **application / applying** : UIX applique un `<uix-node>` à l'élément, généralement dans son `shadowRoot`, ainsi qu'aux éléments enfants indiqués par les sélecteurs.
3. **ignore / ignoring** : le code d'intervention de UIX sur l'élément ne fait rien lorsqu'il s'exécute à ce niveau.

:::
## Structure d'une carte standard

::: example
- Exemple avec la carte `tile`.
- UIX n'intervient pas au niveau de la carte (`tile`), car cela nécessiterait de nombreuses règles CSS et rendrait les thèmes difficiles à gérer.
- Les styles CSS de base s'appliquent via `:host { }` ; ceux de la carte, via `ha-card { }`.

:::
```console
hui-card           ⇐ UIX patches here
  ↳ tile           ⇐ c'est `:host` pour UIX, et la classe UIX y est définie
    ↳ shadowRoot   ⇐ UIX applique les styles ici ; `ha-card` se trouve dans le DOM léger
      ↳ ha-card    ⇐ UIX v4 intervient également ici, mais ignore cet élément car sa structure standard est connue
```

## Structure d'une carte personnalisée - button-card comme exemple

::: example
- `button-card` place un `div` avant `ha-card` ; sa structure n'est donc pas standard.
- La carte (`button-card`) faisant tout de même l'objet d'une intervention, vous pouvez utiliser des variables CSS via `:host { }`.
- Vous pouvez également utiliser des chemins de sélecteurs YAML, comme indiqué plus bas.
- L'intervention et l'application historiques de `ha-card` se font au niveau de `ha-card` ; `ha-card { }` fonctionne donc ici.

:::
```console
hui-card                 ⇐ UIX patches here
  ↳ button-card          ⇐ c'est `:host` pour UIX, et la classe UIX y est définie
    ↳ shadowRoot         ⇐ UIX applique les styles ici
      ↳div
        ↳ ha-card        ⇐ UIX intervient et applique les styles ici, car cette structure n'est pas standard. La classe UIX est également définie ici.
          ↳ shadowRoot
```

## Structure d'une carte personnalisée - streamline-card avec tuile

::: example
- La carte hôte faisant toujours l'objet d'une intervention, vous pouvez appliquer des variables CSS via `:host { }`.
- Vous pouvez également utiliser des chemins de sélecteurs YAML, comme indiqué plus bas.
- L'intervention et l'application historiques sur la carte chargée se font au niveau de `ha-card` ; `ha-card { }` fonctionne donc ici.

:::
```console
hui-card                 ⇐ UIX patches here
  ↳ streamline-card      ⇐ c'est `:host` pour UIX ; la classe UIX de la carte personnalisée hôte est définie selon sa configuration UIX
    ↳ shadowRoot         ⇐ UIX applique les styles ici pour la carte personnalisée hôte
      ↳ tile
        ↳ shadowRoot
          ↳ ha-card      ⇐ UIX patches and applies here for card loaded by custom card, does not ignore as it is not a standard structure. UIX class is set here for card loaded by host custom card from the loaded card's UIX config
            ↳ shadowRoot
```

___
::: note Remarques
- Les cartes personnalisées conteneurs, comme `streamlined-card`, peuvent envelopper chaque carte dans `<hui-card>`. Les utilisateurs bénéficient alors des options `visibility` et du modèle de la nouvelle option de configuration `disabled`. Ces fonctions sont pleinement prises en charge lorsque `<hui-card>` sert de conteneur. C'est désormais le cas de `expander-card`, qui fonctionne ainsi correctement. _Remarque : si une carte d'historique ne se met pas à jour au premier chargement, cela peut venir de l'absence de cette approche._
- La variable de thème `UIX-card` s'applique aux interventions récentes sur `<hui-card>` et aux interventions historiques sur `<ha-card>`.
- Si une carte est chargée directement et aussi par une carte personnalisée comme `layout-card`, utilisez deux sélecteurs CSS dans vos thèmes pour cibler les deux cas.
- Si vous savez qu'une intervention parente `<hui-card>` existe, adaptez vos thèmes en conséquence. Par exemple, pour `streamlined-card`, l'exemple ci-dessous intervient depuis `<hui-card>` ; `*` correspond au type de carte inconnu de UIX dans la structure de `streamlined-card`.
- Les exemples montrent l'application de UIX à une carte. Le même principe s'applique aux thèmes.

:::
::: example Deux sélecteurs CSS
Le sélecteur `:host(.my-class) ha-card` cible les cartes chargées par le frontend. `ha-card.myclass` cible les cartes personnalisées à la structure différente ou chargées par d'autres cartes personnalisées.
```yaml
uix:
  style: |
    :host(.my-class) ha-card,
    ha-card.myclass {
      background-color: red !important;
    }
```

:::
::: example Exemples de structure pour streamlined-card
```yaml
uix:
  style:
    "* $": |
      ha-card {
        --card-background-color: red;
      }
```
OR
```yaml
uix:
  style:
    "* $ ha-card": |
      :host {
        --card-background-color: red;
      }
```
:::
