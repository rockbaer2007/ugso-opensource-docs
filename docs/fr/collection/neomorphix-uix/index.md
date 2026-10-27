---
title: NeoMorphix UIX
description: Brève présentation du thème Home Assistant « NeoMorphix UIX ».
---
<a id="orientation-actuelle"></a>

# NeoMorphix UIX {#neomorphix-uix}

NeoMorphix UIX est une variante UIX du thème Home Assistant « NeuMorphix ». Il mise sur des ombres douces, des formes arrondies et un aspect légèrement en relief pour les tableaux de bord.

::: warning Remarque non officielle
Cette page ne constitue pas une documentation officielle du projet. Elle résume en français les principales instructions d'installation et d'utilisation. Le dépôt (repository) original demeure la référence.
:::

| Champ | Valeur |
| --- | --- |
| Projet original | [yakidd/NeumorphixHome](https://github.com/yakidd/NeumorphixHome) |
| Commit vérifié | [`269c298e47b02faaac4f08c8c9dfccf49d70d860`](https://github.com/yakidd/NeumorphixHome/commit/269c298e47b02faaac4f08c8c9dfccf49d70d860) |
| Version | [`1.0.3`](https://github.com/yakidd/NeumorphixHome/releases/tag/1.0.3) |
| Fork UIX | [rockbaer2007/NeoMorphix-UIX](https://github.com/rockbaer2007/NeoMorphix-UIX/tree/experiment/uix-theme-variant) |
| Licence | selon le fichier README : MIT |
| Catégorie | Tableau de bord HA -> Thèmes |

## Installation {#installation}

NeoMorphix UIX est basé sur NeuMorphix et est conçu pour être utilisé comme thème dans HACS.

[![Ouvrir NeoMorphix UIX dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=rockbaer2007&repository=NeoMorphix-UIX&category=theme)

1. Installez HACS, si ce n'est pas déjà fait.
2. Installez <a href="https://uix.lf.technology/quick-start/" target="_blank" rel="noopener noreferrer">UIX</a>.
3. Installez le fork NeoMorphix-UIX en tant que thème via HACS.
4. Redémarrez Home Assistant.
5. Sélectionnez une variante de NeoMorphix-UIX dans le profil utilisateur ou dans les paramètres du tableau de bord.

L'intégration des thèmes doit être activée dans Home Assistant :

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

La version originale de NeoMorphix utilise `card-mod`. Pour NeoMorphix UIX, c'est `UIX` qui est requis à la place.

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

## Variantes {#varianten}

Le projet original fournit deux fichiers de thème :

- `themes/neumorphix.yaml`
- `themes/neumorphix-inset.yaml`

Ils contiennent six variantes de thème :

- `neumorphix-light`
- `neumorphix-dark`
- `neumorphix-claude`
- `neumorphix-light-inset`
- `neumorphix-dark-inset`
- `neumorphix-claude-inset`

`Raised` donne l'impression d'une surface en relief (surélevée). `Inset` donne plutôt l'impression d'être enfoncée ou incrustée dans la surface.

## Variante UIX {#uix-variante}

Une branche complémentaire a été créée pour UIX ; elle ne remplace pas les fichiers `card-mod` originaux, mais ajoute des fichiers de thème UIX supplémentaires :

- [Branche UIX dans le fork](https://github.com/rockbaer2007/NeoMorphix-UIX/tree/experiment/uix-theme-variant)
- [Pull Request vers le projet original](https://github.com/yakidd/NeumorphixHome/pull/4)

La branche UIX ajoute :

- `themes/NeoMorphix UIX.yaml`
- `themes/NeoMorphix UIX Inset.yaml`

Les noms des thèmes supplémentaires sont :

- `NeoMorphix UIX Light`
- `NeoMorphix UIX Dark`
- `NeoMorphix UIX Claude`
- `NeoMorphix UIX Light Inset`
- `NeoMorphix UIX Dark Inset`
- `NeoMorphix UIX Claude Inset`

Sur le plan technique, les fichiers supplémentaires ont été associés à des clés de thème UIX :

- `card-mod-theme` -> `uix-theme`
- `card-mod-root-yaml` -> `uix-root-yaml`
- `card-mod-sidebar-yaml` -> `uix-drawer-yaml`

## Remarques {#hinweise}

- Le projet original indique la licence MIT dans son fichier README, mais ne contient pas de fichier `LICENSE` distinct dans le dépôt.
- La variante UIX est conçue comme un complément. Les fichiers `card-mod` existants demeurent inchangés. - Avec les variantes « Inset », la page de configuration principale de Home Assistant peut se comporter différemment, car cette interface est rendue d'une manière distincte des tableaux de bord (dashboards) classiques.
