---
title: Spark Badge
description: Badges texte et icône avec couleurs du thème, animation et placement facultatif.
---
# Spark Badge

Le spark `badge` insère un `uix-badge` avant ou après un élément créé par Forge. Il utilise la base Web Awesome adaptée par Home Assistant et suit les couleurs du thème. UIX n'enregistre pas de composant global `wa-badge`.

Cette référence compacte est adaptée de la [page originale de la version 8.4.0](https://github.com/Lint-Free-Technology/uix/blob/v8.4.0/docs/source/forge/sparks/badge.md), sous [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), par Lint-Free-Technology/uix. D'autres exemples illustrés figurent dans la [documentation anglaise](https://uix.lf.technology/forge/sparks/badge/).

## Utilisation de base

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: badge
      after: hui-tile-card $ ha-tile-icon
      content: 3
      variant: danger
      pill: true
element:
  type: tile
  entity: light.bed_light
```

## Configuration

| Clé | Type | Valeur par défaut | Description |
| --- | --- | --- | --- |
| `type` | string, obligatoire | — | `badge` |
| `after` | string | Blank Card : `uix-forge-blank-card $ div.content`, sinon `""` | Élément de référence ; insertion après. Fournir `after` ou `before`, sauf si la valeur Blank Card s'applique. |
| `before` | string | — | Élément de référence ; insertion avant. |
| `content` | string / number | `""` | Texte affiché, pas du HTML. |
| `variant` | string | `brand` | `brand`, `neutral`, `success`, `warning`, `danger` |
| `appearance` | string | `accent` | `accent`, `filled`, `outlined`, `filled-outlined` |
| `pill` | boolean | `false` | Forme entièrement arrondie. |
| `attention` | string | `none` | `none`, `pulse`, `bounce`. Pour `pulse`, `accent`/`filled` utilisent la couleur de remplissage, les autres apparences celle de la bordure. |
| `placement` | string | Automatique sur `ha-button`/`ha-tile-icon` : `top-end` ; sinon absent | Position sur l'élément ou son parent, voir ci-dessous. |
| `start_icon` / `end_icon` | string | — | Icône MDI avant/après le contenu. |
| `style` | object | — | Table plate de propriétés CSS et valeurs texte ou numériques, appliquées directement au badge. |

Seul le premier élément correspondant au sélecteur est utilisé. Dans une Tile Card, ciblez `ha-tile-icon` pour le coin ; `ha-tile-info` occupe le reste de la largeur de la ligne.

## Placement

Le placement automatique concerne uniquement `ha-button` et `ha-tile-icon`, au coin supérieur de fin logique (`top-end`). Sur `ha-button`, le badge est inséré dans le bouton. Sur `ha-tile-icon`, il utilise le slot par défaut documenté et les décalages compacts de Home Assistant. Ici, `after`/`before` choisit la cible, pas l'ordre d'insertion.

UIX reconnaît le wrapper `display: contents` d'un spark Button et place le badge sur son `ha-button`. La Button Card intégrée `hui-button-card` ne contient pas de `ha-button` et n'a pas de placement automatique.

Pour les autres cibles, sans `placement`, le badge reste un élément voisin. Avec `placement`, il est placé au bord du **parent**. UIX ne mesure ni ne modifie la cible. Si plusieurs enfants sont visibles, la position se rapporte au parent entier.

Valeurs acceptées : `top`, `top-start`, `top-end`, `bottom`, `bottom-start`, `bottom-end`, `left`, `left-start`, `left-end`, `right`, `right-start`, `right-end`.

Un badge placé utilise par défaut `var(--ha-font-size-xs)` et un padding `0.25em 0.5em`. Les décalages acceptent longueurs et pourcentages. Pour `right`, `top-end` ou `bottom-end`, `--uix-badge-offset-x: -50%` annule le chevauchement d'une demi-largeur ; pour `left`, `top-start` ou `bottom-start`, utilisez `50%`. Des expressions comme `calc(-50% - 20px)` sont possibles.

## Variables CSS

À définir sur le badge, un ancêtre ou dans sa table `style`. Ces variables fonctionnent aussi pour les badges Broker.

| Variable | Valeur par défaut | Effet |
| --- | --- | --- |
| `--uix-badge-font-size` | `max(var(--wa-font-size-3xs, var(--ha-font-size-xs)), 0.75em)` ; placé : `var(--ha-font-size-xs)` | Taille du texte. |
| `--uix-badge-font-weight` | `var(--wa-font-weight-semibold)` | Graisse du texte/des icônes. |
| `--uix-badge-padding` | `0.375em 0.625em` ; placé : `0.25em 0.5em` | Espacement intérieur. |
| `--uix-badge-min-width` | Placé : `calc(1.5em + 2px)` | Largeur minimale, bordure de 1 px de chaque côté comprise. |
| `--uix-badge-max-width` | `none` | Largeur maximale. |
| `--uix-badge-overflow` | `visible` | Débordement ; avec largeur maximale, utiliser par exemple `hidden` ou `clip`. |
| `--uix-badge-color` | Remplissage Web Awesome | Couleur du fond. |
| `--uix-badge-content-color` | Couleur Web Awesome | Couleur du texte/des icônes. |
| `--uix-badge-border` | Bordure Web Awesome | Bordure CSS complète, par exemple `1px solid rgb(255 255 255 / 50%)`. |
| `--uix-badge-border-color` | Couleur de bordure Web Awesome | Utilise `--uix-badge-color` si cette variable est définie. |
| `--uix-badge-box-shadow` | `none` | Ombre statique. |
| `--uix-badge-attention-color` | Couleur de remplissage ou de bordure de l'apparence | Couleur de l'anneau pulsant. |
| `--uix-badge-color-hover` | Couleur de fond normale | Fond au survol. |
| `--uix-badge-content-color-hover` | Couleur de contenu normale | Texte/icônes au survol. |
| `--uix-badge-border-color-hover` | Couleur de bordure normale | Bordure au survol. |
| `--uix-badge-attention-color-hover` | Couleur d'attention normale | Anneau au survol. |
| `--uix-badge-pointer-events` | Placé : `auto` | `none` laisse passer les événements du pointeur et désactive le survol. |
| `--uix-badge-z-index` | `auto` ; placé : `1` | Ordre de superposition. |
| `--uix-badge-offset-x` | `0px` | Décalage horizontal ; positif vers la droite. |
| `--uix-badge-offset-y` | `0px` | Décalage vertical ; positif vers le bas. |

Les variables de couleur acceptent les valeurs CSS transparentes `rgba()` ou `rgb()` modernes. Avec `attention: pulse`, l'ombre statique reste présente et UIX ajoute l'anneau expansif. Le survol d'un badge placé n'agit que lorsque le pointeur se trouve sur le badge lui-même.

## Exemple : placement sur une Button Card

La Button Card remplit ici son parent. Le `placement` explicite positionne le badge sur ce conteneur sans modifier le DOM interne de la carte.

```yaml
type: custom:uix-forge
forge:
  mold: card
  sparks:
    - type: badge
      after: hui-button-card
      content: 3
      variant: danger
      pill: true
      placement: top-end
      style:
        "--uix-badge-offset-x": -6px
        "--uix-badge-offset-y": 6px
        "--uix-badge-font-size": 24px
element:
  type: button
  entity: light.bed_light
```

Les autres exemples originaux présentent un badge d'état voisin de `ha-tile-info` avec `flex: 1`, une animation pilotée par template, un badge sur un spark Button et une Blank Card centrée.
