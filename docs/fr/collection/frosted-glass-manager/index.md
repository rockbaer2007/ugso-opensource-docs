---
title: Gestionnaire de thème « Frosted Glass »
description: Informations concernant le gestionnaire de thème « Frosted Glass » et la variante d'interface utilisateur (UIX) testée.
---
<a id="frosted-glass-theme-gestionnaire"></a>
<a id="orientation-actuelle"></a>

# Gestionnaire de thème « Frosted Glass » {#frosted-glass-theme-manager}

Le « Frosted Glass Theme Manager » est une intégration personnalisée pour Home Assistant, conçue pour générer des fichiers de thèmes de type « verre dépoli » (frosted glass). Les couleurs et les images d'arrière-plan peuvent être définies via l'interface de Home Assistant.

::: warning Note non officielle
Cette page ne constitue pas une documentation officielle du projet. Le dépôt (repository) original demeure la référence.
:::

| Champ | Valeur |
| --- | --- |
| Projet original | [wessamlauf/frosted-glass-manager](https://github.com/wessamlauf/frosted-glass-manager) |
| Fork avec variante de test UIX | [rockbaer2007/frosted-glass-manager](https://github.com/rockbaer2007/frosted-glass-manager/tree/experiment/uix-theme-manager) |
| Pull Request | [wessamlauf/frosted-glass-manager#15](https://github.com/wessamlauf/frosted-glass-manager/pull/15) |
| Catégorie | Intégrations HA |

## Gestionnaire original {#original-manager}

Le gestionnaire original génère des fichiers de thèmes de type « verre dépoli » destinés à une utilisation standard avec « card-mod ».

[![Ouvrir Frosted Glass Theme Manager dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=wessamlauf&repository=frosted-glass-manager&category=integration)

Dépôt :

- [wessamlauf/frosted-glass-manager](https://github.com/wessamlauf/frosted-glass-manager)

## Variante de test UIX {#uix-testvariante}

Pour les installations utilisant UIX au lieu de card-mod, une version fonctionnelle basée sur UIX est disponible sous forme de « fork ».

[![Ouvrir Frosted Glass UIX Theme Manager dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=rockbaer2007&repository=frosted-glass-manager&category=integration)

Dépôt :

- [Frosted Glass UIX Theme Manager](https://github.com/rockbaer2007/frosted-glass-manager/tree/experiment/uix-theme-manager)

La variante de test UIX utilise son propre identifiant d'intégration pour Home Assistant :

- `frosted_glass_uix_manager`

Elle génère ses propres fichiers de thème, évitant ainsi tout conflit avec les noms de fichiers habituels de Frosted Glass :

- `Frosted Glass UIX Custom.yaml`
- `Frosted Glass UIX Custom Lite.yaml`

Les arrière-plans par défaut sont fournis localement et copiés dans Home Assistant au démarrage :

- `config/www/frosted-glass-uix/frosted-glass-light-background.jpg`
- `config/www/frosted-glass-uix/frosted-glass-dark-background.jpg`

Dans les thèmes générés, ils sont intégrés via `/local/frosted-glass-uix/...`. Ainsi, l'apparence par défaut ne dépend pas d'un CDN externe.

## Remarque {#hinweis}

La variante de test UIX a fait l'objet de tests pratiques, mais elle demeure une version expérimentale. Pour toute question générale concernant le projet original, veuillez continuer à utiliser le dépôt (repository) d'origine.
