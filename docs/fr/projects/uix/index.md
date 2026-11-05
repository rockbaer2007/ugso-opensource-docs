---
title: À propos
---
# UI eXtension pour Home Assistant

::: info État vérifié le 5 novembre 2026
La base stable est **UIX 9.0.0**, qui nécessite **Home Assistant 2026.11.0 ou ultérieur**. Les **65** pages sources ont été comparées à `master f63ebbd`. `dev ef414d9` contient la même documentation. Voir le [rapport](./translation-status).
:::

> Cette traduction française est maintenue par UGSo Software. La documentation anglaise reste la référence. La base est la version stable [`UIX 9.0.0`](https://github.com/Lint-Free-Technology/uix/releases/tag/v9.0.0) du 4 novembre 2026, révision [`cec1191`](https://github.com/Lint-Free-Technology/uix/commit/cec1191f6ee703284c75dfd3104dba9bb4419200). **Home Assistant 2026.11.0 ou ultérieur est requis.**

![light-logo-icon](./assets/images/mixed.png)

## Qu'est-ce que UI eXtension ?

::: note Utilisateurs de Card-mod
    Si vous migrez depuis Card-mod, consultez la [FAQ](./faq), qui répond à la plupart des questions. Pour toute autre question, utilisez les [discussions GitHub](https://github.com/Lint-Free-Technology/uix/discussions).

:::
Avec un ensemble de fonctions qui dépasse les cartes et les tableaux de bord, UI eXtension (UIX) a été créé pour étendre les possibilités du CSS personnalisé dans l'interface Home Assistant. UIX s'inscrit dans la continuité de [card-mod](https://github.com/thomasloven/lovelace-card-mod), créé par [@thomasloven](https://github.com/thomasloven).

UI eXtension comprend [UIX Styling](./using/index.md), [UIX Forge](./forge/index.md) et [UIX Broker](./broker/index.md). [UIX Styling](./using/index.md) permet d'appliquer du CSS à presque tous les éléments de l'interface Home Assistant. [UIX Forge](./forge/index.md) permet de créer des éléments Home Assistant (cartes, badges, lignes, etc.) avec des modèles pour toute leur configuration et des extensions avancées grâce aux [Sparks UIX Forge](./forge/sparks/index.md). UIX Broker transforme les événements du navigateur, les raccourcis clavier et les événements du bus Home Assistant en interactions déclaratives. Une interaction sélectionne un élément, vérifie des règles optionnelles, puis exécute ses directives dans l'ordre configuré.

## Nouveautés de UIX 9.0.0

- Les [raccourcis personnalisés de barre latérale](./extras/custom-sidebar-panels) ouvrent des pages Home Assistant et des sites externes, y compris dans un nouvel onglet.
- L’[éditeur visuel Forge](./forge/forge#visual-editor-cards-and-badges) prend en charge les cartes et les badges. `element_base` conserve la configuration native et ses modèles.
- Les [délais des popovers](./extras/uix-actions#popover) ferment automatiquement le contenu affiché.

- [Spark Formulaire](./forge/sparks/form) et [action Popover](./extras/uix-actions#popover) pour les formulaires et les contenus superposés.
- [Style des panneaux intégrés dans un frame](./extras/style-frame-panels) avec un runtime interne ; cette option expérimentale reste désactivée par défaut.
- [Polices de thème avec `uix-fonts`](./using/themes) et [images d'entité dans les aperçus de carte](./using/images), avec adaptation à Home Assistant 2026.10.
- Les [règles de directive Broker](./broker/directives#regles-de-la-directive) peuvent utiliser les résultats de directives JavaScript ou template précédentes.

L’[installation via le Marketplace](./quick-start) ajoute automatiquement UIX comme service. La [désinstallation](./faq) supprime aussi les Foundries, les raccourcis de barre latérale et les autres réglages du service.

## 🚀 Démarrage rapide

Consultez le [Démarrage rapide](./quick-start.md) pour l'installation et un premier exemple de UIX Styling et UIX Forge.

## ➡️ Continuer

- [Utiliser UIX Styling](./using/index.md)
- [Utiliser UIX Forge](./forge/index.md)
- [FAQ](./faq)
