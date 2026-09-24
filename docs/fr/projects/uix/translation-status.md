---
title: État de la traduction
description: État de la documentation UIX française.
---
# État de la traduction

Cette documentation française est maintenue à partir de la documentation UIX canonique en anglais. Les pages principales, le démarrage rapide et les aperçus de UIX Styling, Forge, Broker et Extras sont déjà disponibles en français. La section complète **UIX Broker** est également disponible en français.

## Référence canonique

La [documentation UIX anglaise](https://uix.lf.technology/) reste la référence pour la syntaxe, le comportement lié à une version et les nouveaux changements. Certaines pages détaillées peuvent encore nécessiter une vérification éditoriale.

## Vérification du 24 septembre 2026

La traduction française a été vérifiée avec la version stable UIX `8.3.1` du 22 septembre 2026, révision [`add5557`](https://github.com/Lint-Free-Technology/uix/commit/add5557c0ee13a98c9fe249bed06d215606f2507). Cette vérification inclut également les révisions documentaires [`a43f3e2`](https://github.com/Lint-Free-Technology/uix/commit/a43f3e2bf03edb808c0ea8d83af426d06626181e), [`8711f1e`](https://github.com/Lint-Free-Technology/uix/commit/8711f1eb4a2a479a2a43d748c0b26f94b040e87a) et [`8c6fb83`](https://github.com/Lint-Free-Technology/uix/commit/8c6fb830d75477b30f035323161bac8d41599a78).

La version 8.3.1 corrige deux problèmes : le Map spark fonctionne de nouveau après les changements de carte de Home Assistant 2026.9.0, et le chargement de Web Awesome est contourné sur les appareils anciens, notamment sous iOS 15. Ces corrections de publication n'ajoutent pas de nouvelle option de configuration.

- La page Extras consacrée au style des panneaux personnalisés dans une iframe a été remplacée par [Styliser les panneaux intégrés dans un frame](./extras/style-frame-panels.md), qui décrit l'option expérimentale, son activation, les frames prises en charge et la compatibilité des frameworks.
- [Panneaux personnalisés](./using/custom-panels.md) distingue désormais les panneaux chargés directement des frames de panneaux et d'applications.
- La nouvelle page [Panneaux d'applications et d'Ingress](./using/apps.md) documente les clés de thème, la résolution des slugs et la portée de `uix-app`.
- La navigation française et les pages d'aperçu ont été mises à jour, ainsi que l'image d'exemple des panneaux d'applications.

Selon la documentation canonique, le style des frames d'applications de même origine est disponible à partir de UIX `3.4.0-beta.1`. L'option expérimentale de style des frames est désactivée par défaut.

## Prochaine étape

La documentation française sera révisée au fil des prochaines modifications de la documentation canonique.
