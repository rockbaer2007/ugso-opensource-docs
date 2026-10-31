---
title: À propos
---
# UI eXtension pour Home Assistant

::: info État vérifié le 31 octobre 2026
Base stable : **UIX 8.4.0**, nécessite **Home Assistant 2026.10.0 ou ultérieur**. Les **65** pages sources anglaises ont été comparées à la révision `dev` **e6fb84d / 9.0.0-beta.6** ; DE/FR ont été complétées avec les changements. Les fonctions d’aperçu sont indiquées séparément. Voir le [rapport](./translation-status).
:::

> **Traduction indépendante** — Cette documentation française est maintenue par UGSo Software et n'est pas la documentation officielle du projet UIX. La documentation anglaise reste la référence. Base comparée à la version stable [`UIX 8.4.0`](https://github.com/Lint-Free-Technology/uix/releases/tag/v8.4.0) du 7 octobre 2026, révision [`71b8ccd`](https://github.com/Lint-Free-Technology/uix/commit/71b8ccd38202257c070ae9970a7aac12a68a6389). **Home Assistant 2026.10.0 ou ultérieur est requis.**

![light-logo-icon](./assets/images/mixed.png)

## Qu'est-ce que UI eXtension ?

::: note Utilisateurs de Card-mod
    Si vous migrez depuis Card-mod, consultez la [FAQ](./faq), qui répond à la plupart des questions. Pour toute autre question, utilisez les [discussions GitHub](https://github.com/Lint-Free-Technology/uix/discussions).

:::
Avec un ensemble de fonctions qui dépasse les cartes et les tableaux de bord, UI eXtension (UIX) a été créé pour étendre les possibilités du CSS personnalisé dans l'interface Home Assistant. UIX s'inscrit dans la continuité de [card-mod](https://github.com/thomasloven/lovelace-card-mod), créé par [@thomasloven](https://github.com/thomasloven).

UI eXtension comprend [UIX Styling](./using/index.md), [UIX Forge](./forge/index.md) et [UIX Broker](./broker/index.md). [UIX Styling](./using/index.md) permet d'appliquer du CSS à presque tous les éléments de l'interface Home Assistant. [UIX Forge](./forge/index.md) permet de créer des éléments Home Assistant (cartes, badges, lignes, etc.) avec des modèles pour toute leur configuration et des extensions avancées grâce aux [Sparks UIX Forge](./forge/sparks/index.md). UIX Broker transforme les événements du navigateur, les raccourcis clavier et les événements du bus Home Assistant en interactions déclaratives. Une interaction sélectionne un élément, vérifie des règles optionnelles, puis exécute ses directives dans l'ordre configuré.

## Nouveautés de UIX 8.4.0

::: info Aperçu : UIX 9.0.0-beta.6
Les [raccourcis personnalisés dans la barre latérale](./using/custom-sidebar-panels) sont disponibles à partir de **9.0.0-beta.6**. L’[éditeur visuel Forge](./forge/forge#visual-editor-cards-and-badges), disponible depuis **9.0.0-beta.2**, propose **Convert to visual editor** pour les Forges directes de carte ou de badge existantes. La base stable reste **8.4.0**.
:::

- [Spark Formulaire](./forge/sparks/form) et [action Popover](./extras/uix-actions#popover) pour les formulaires et les contenus superposés.
- [Style des panneaux intégrés dans un frame](./extras/style-frame-panels) avec un runtime interne ; cette option expérimentale reste désactivée par défaut.
- [Polices de thème avec `uix-fonts`](./using/themes) et [images d'entité dans les aperçus de carte](./using/images), avec adaptation à Home Assistant 2026.10.
- Les [règles de directive Broker](./broker/directives#regles-de-la-directive) peuvent utiliser les résultats de directives JavaScript ou template précédentes.

Les ajouts précédemment décrits pour les versions bêta 8.4 font désormais partie de la version stable. Les mentions historiques indiquent toujours la version d'introduction des fonctions.

## 🚀 Démarrage rapide

Consultez le [Démarrage rapide](./quick-start.md) pour l'installation et un premier exemple de UIX Styling et UIX Forge.

## ➡️ Continuer

- [Utiliser UIX Styling](./using/index.md)
- [Utiliser UIX Forge](./forge/index.md)
- [FAQ](./faq)
