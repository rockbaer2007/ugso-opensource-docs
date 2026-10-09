---
title: État de la traduction
description: État de la documentation UIX française.
---
# État de la traduction

Cette documentation française est maintenue à partir de la documentation UIX canonique en anglais. Les pages principales, le démarrage rapide et les aperçus de UIX Styling, Forge, Broker et Extras sont déjà disponibles en français. La section complète **UIX Broker** est également disponible en français.

## Comparaison du 9 octobre 2026 : base stable 8.4.0, aperçu 9.0.0-beta.0

Les notifications canoniques `2db023d236c9`, `c800e607f23d`, `9b5858f57678` et `22f8d93f0131` ont été comparées aux pages allemandes et françaises. La branche `dev` vérifiée est [`e2e0701`](https://github.com/Lint-Free-Technology/uix/commit/e2e070193b3f77b251dcfe05104a4d791a8e9a03), version **9.0.0-beta.0**. La version stable de l'original sur `master` reste **8.4.0** ; les liens de publication, le pied de page et les métadonnées stables restent associés à cette version.

- Suppression des anciennes mentions bêta pour les règles de directive, l'action Popover, le formulaire, les panneaux d'applications et les polices des thèmes.
- FAQ sur le message de rechargement obligatoire et le rechargement automatique après 60 secondes. La nouvelle conservation des fichiers frontend chargés au démarrage de Home Assistant est présentée comme un aperçu.
- Référence Forge, fonderies et aperçu : `element_base`, surcouche `element`, `element_disabled_paths` locaux, fusion, visibilité native et contextes des modèles. Disponibilité explicitement à partir de **9.0.0-beta.0**, pas de 8.4.0 ni de 8.4.1.
- Animation originale `forge-auto-entities.gif` de `9b5858f57678` synchronisée pour DE/FR. La `source_revision` stable reste inchangée ; la version, la branche et la révision d'aperçu sont enregistrées séparément.

## Version actuelle : UIX 8.4.0

- Comparaison le **8 octobre 2026** avec la version stable [`v8.4.0`](https://github.com/Lint-Free-Technology/uix/releases/tag/v8.4.0) du 7 octobre 2026, révision [`71b8ccd`](https://github.com/Lint-Free-Technology/uix/commit/71b8ccd38202257c070ae9970a7aac12a68a6389).
- **Home Assistant 2026.10.0 ou ultérieur est requis.**
- Aucun changement de `docs/source` ni de `docs/mkdocs.yml` entre la révision déjà vérifiée `c70d1275f1fb08514291feb4c9181a748408b798` et `v8.4.0`.
- Formulaire, Popover, runtime interne des frames, `uix-fonts`, images d'entité dans les aperçus de carte et références aux résultats Broker sont couverts. L'option des frames reste expérimentale et désactivée par défaut.
- La [référence Badge](./forge/sparks/badge), auparavant absente, est ajoutée. Les versions française et allemande couvrent désormais les 64 chemins Markdown canoniques, avec une page de statut supplémentaire. La page Badge est une référence compacte avec les tableaux complets des options et variables CSS ; les autres exemples originaux sont liés.
- Vue d'ensemble, pied de page, lien de publication, métadonnées JSON allemandes et `llms.txt` sont actualisés. Les mentions bêta historiques indiquent les versions d'introduction ; les rapports datés ci-dessous décrivent les vérifications précédentes.
- Ajout de 17 ancres compatibles avec les liens anglais existants : 36 liens internes vers des sections françaises sont rétablis sans modifier leurs titres ni leurs ancres françaises.
- Vérification des sources, de la couverture, de la construction, des liens, des langues et des exemples copiables ; sans nouvelle révision phrase par phrase de toutes les traductions antérieures ni tests d'exécution Home Assistant.

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

## Mise à jour du 30 septembre 2026

Les pages françaises sur les [entités](./using/entities) et les [images](./using/images) ont été comparées à la révision documentaire canonique [`7d7c95a`](https://github.com/Lint-Free-Technology/uix/commit/7d7c95acb449c1222d8a338e3d9423f91ff0f2a2). Les parts CSS pour les marqueurs de carte depuis Home Assistant 2026.10.0, `hui-map-overview` et la restriction aux surcharges propres à une entité ont été ajoutées. La base stable reste UIX `8.3.1` ; le pied de page indique également les changements documentaires vérifiés jusqu’à UIX `8.4.0-beta.3`.

## Mise à jour de Broker du 5 octobre 2026

Les pages [Directives](./broker/directives#regles-de-la-directive) et [Règles](./broker/rules#formulaire-compact-de-donnees-capturees) ont été comparées aux changements de référence [`105b8cd`](https://github.com/Lint-Free-Technology/uix/commit/105b8cd446ea082553be627530efe8a752d57dec) et [`04d8e14`](https://github.com/Lint-Free-Technology/uix/commit/04d8e14b006f24e795997c68191f9fde3652bd22). Les références aux résultats `@<directive-id>`, l’exemple YAML inchangé et la disponibilité à partir de UIX `8.4.0-beta.9` ont été ajoutés. Ces références sont réservées aux règles de directive. Les pages allemandes correspondantes ont également été mises à jour ; la base stable reste UIX `8.3.1`.

## Prochaine étape

La documentation française sera révisée au fil des prochaines modifications de la documentation canonique.

## Vérification du 8 octobre 2026

Les changements de la documentation anglaise à la révision [`c70d1275f1fb`](https://github.com/Lint-Free-Technology/uix/commit/c70d1275f1fb08514291feb4c9181a748408b798), branche `master`, ont été comparés aux versions allemande et française.

- Nouveau [spark Formulaire](./forge/sparks/form) : schéma, Markdown, envoi/effacement, densité, variables CSS et valeurs du formulaire dans les actions.
- Nouvelle [action Popover](./extras/uix-actions#popover) : cartes, icônes d'en-tête, boutons de pied de page, intégration des formulaires et exemples originaux.
- Broker : `block` synchrone, ancres des règles, réutilisation de l'état du panneau, référence `previous` des info-bulles, Promises JavaScript et événements du cycle de vie des styles. Suppression des fonctionnalités futures obsolètes.
- Navigation, aperçus de Forge et FAQ complétés ; six médias originaux nouveaux ou modifiés repris.
- Les changements déjà présents concernant les panneaux intégrés et d'applications ont été comparés à nouveau. Les changements des images d'entité, des marqueurs de carte et des polices des thèmes ont été ajoutés.

Cette vérification porte sur les changements documentaires signalés. La base stable des métadonnées reste `8.3.1` ; elle ne constitue pas une révision complète de toutes les pages pour une publication stable ultérieure. Les exemples YAML/JavaScript et les médias du nouveau formulaire et du popover proviennent sans modification de la source anglaise. La construction et la vérification des liens contrôlent la publication, sans tests d'exécution dans Home Assistant.
