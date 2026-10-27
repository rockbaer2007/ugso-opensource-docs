---
title: Thème Frosted Glass
description: Brève note en français sur le thème Frosted Glass pour Home Assistant.
---
<a id="orientation-actuelle"></a>

# Thème « Verre dépoli » (Frosted Glass) {#frosted-glass-theme}

Le thème « Verre dépoli » (Frosted Glass) est un thème moderne pour Home Assistant. Il se caractérise par des cartes transparentes, un effet de flou, des surfaces aux angles arrondis, des variantes claires et sombres, ainsi que des versions « Lite » (allégées) sans effet de flou, destinées aux appareils moins puissants.

::: warning Remarque non officielle
Cette page ne constitue pas une documentation officielle du projet. Elle résume en français les principales instructions d'installation et d'utilisation. Le dépôt (repository) original demeure la référence.
:::

| Champ | Valeur |
| --- | --- |
| Projet original | [wessamlauf/homeassistant-frosted-glass-themes](https://github.com/wessamlauf/homeassistant-frosted-glass-themes) |
| Commit vérifié | [`8cb950369e64444bcdc068f7f90283d58f65d80d`](https://github.com/wessamlauf/homeassistant-frosted-glass-themes/commit/8cb950369e64444bcdc068f7f90283d58f65d80d) |
| Version (Release) | [`v1.3`](https://github.com/wessamlauf/homeassistant-frosted-glass-themes/releases/tag/v1.3) |
| Licence | [MIT](https://github.com/wessamlauf/homeassistant-frosted-glass-themes/blob/main/LICENSE) |
| Catégorie | Tableau de bord HA -> Thèmes |

## Installation {#installation}

Ce thème peut être installé via HACS.

1. Installez HACS, si ce n'est pas déjà fait.
2. Installez `card-mod` ou `UIX`.
3. Installez le thème « Frosted Glass » via HACS.
4. Redémarrez Home Assistant.
5. Sélectionnez le thème dans votre profil utilisateur.

Lien direct :

[Ouvrir le thème « Frosted Glass » dans HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=WessamLauf&repository=homeassistant-frosted-glass-themes&category=theme)

::: warning card-mod ou UIX requis
Le thème nécessite `card-mod` ou `UIX` pour que les effets de flou et de style fonctionnent correctement. :::

## Variantes {#varianten}

Le dépôt contient plusieurs fichiers de thème :

- `Frosted Glass.yaml`
- `Frosted Glass Light.yaml`
- `Frosted Glass Dark.yaml`
- `Frosted Glass Lite.yaml`
- `Frosted Glass Light Lite.yaml`
- `Frosted Glass Dark Lite.yaml`

Les variantes « Lite » n'utilisent pas d'effets de flou (blur). Cela est particulièrement utile sur les tablettes plus anciennes, le matériel peu performant, ou lorsque les menus déroulants sont mal affichés en raison de ces effets de flou.

## Gestionnaire de thèmes (Theme Manager) {#theme-manager}

Un projet d'intégration distinct est disponible pour personnaliser les couleurs et les images d'arrière-plan :

- [Gestionnaire de thèmes « Frosted Glass » et variante de test UIX](/fr/collection/frosted-glass-manager/)

## Remarques connues {#bekannte-hinweise}

- Les cartes Markdown contenant uniquement du texte héritent tout de même du style « verre » (frosted glass) et des bordures du thème.
- L'effet de flou peut perturber l'affichage des menus déroulants dans HACS ou dans les menus plus profonds de Home Assistant.
- `stack-in-card` peut s'avérer complexe en raison de styles imbriqués à plusieurs niveaux.
- Sur les appareils peu performants, les versions « Lite » constituent généralement un meilleur choix.

Ajuster une carte Markdown simple via `card_mod` :

```yaml
card_mod:
  style: |
    ha-card {
      background: none !important;
      backdrop-filter: none !important;
      -webkit-backdrop-filter: none !important;
      box-shadow: none !important;
      border: none !important;
    }
    ha-card::before {
      content: none !important;
      background: none !important;
      backdrop-filter: none !important;
      -webkit-backdrop-filter: none !important;
    }
```
