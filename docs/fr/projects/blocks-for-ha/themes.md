---
title: Thèmes et zoom
---

# Thèmes et zoom

Depuis **0.1.27**, les blocs UGSo Standard/Dark utilisent des libellés blancs. Les fonds bleus et bruns intermédiaires sont légèrement assombris pour un contraste d’au moins **4,5:1**. Les couleurs claires originales de Modern/Tritanopia utilisent une écriture sombre suffisamment contrastée. Les champs éditables restent distincts et lisibles. Les images DE/EN/FR du catalogue ont été régénérées avec cette correction.

Le thème de l’application et la palette Blockly sont **indépendants**. La langue des blocs est également un réglage distinct. Ni thèmes ni zoom ni langue ne modifient le YAML.

## Palette Blockly

| Choix | Apparence | Source originale |
| --- | --- | --- |
| UGSo Standard | Couleurs des groupes UGSo, menu sombre et panneau de blocs clair | Adaptation UGSo de Blockly Classic |
| Dark | Espace de travail et panneau sombres, fond du menu distinct | [theme-dark](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-dark) |
| Modern | Palette Modern originale avec bordures marquées et groupes UGSo | [theme-modern](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-modern) |
| Tritanopia | Palette des groupes standard adaptée, complétée pour les groupes HA | [theme-tritanopia](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-tritanopia) |

Tritanopia vise les personnes présentant cette déficience de vision des couleurs. Les blocs clairs ont des libellés sombres, les blocs sombres des libellés clairs. Les champs éditables restent visuellement distincts. Les noms des catégories apportent un repère supplémentaire. Cela ne constitue pas une certification complète d’accessibilité.

![Palette Dark, blocs français](/assets/blocks-for-ha/themes/fr/dark.png)

![Palette Tritanopia, blocs français](/assets/blocks-for-ha/themes/fr/tritanopia.png)

Le choix est sauvegardé localement. Une préférence inconnue revient au standard ; si le stockage est bloqué, le changement reste possible pour la page actuelle.

## Zoom

Depuis **0.1.40**, tous les thèmes utilisent une **police de 16 px**. Le menu de blocs reste à **100 %** : ajustement, molette et zoom modifient uniquement l’espace de travail. Zoom initial 100 %, ajustement 85–120 %, zoom manuel 50–240 %. Les grandes automatisations restent défilables ; l’ajustement ne descend pas sous 85 % afin de préserver la lisibilité. Vérifié en Full HD, 2560 px et HiDPI.

## Apparence de l’application

**Darstellung** propose **Hell**, **Dunkel** et **System** pour l’en-tête, les panneaux, formulaires, YAML, dialogues et éditeurs. System suit immédiatement la préférence de couleur du navigateur/système ; un choix manuel la remplace. Préférence locale, indépendante de la palette Blockly. Le badge Built with Blockly utilise automatiquement la variante adaptée.

Blockly et les plugins de thèmes/zoom sont épinglés à 13.3.0 et intégrés localement sous Apache-2.0. [Catalogue et liens des plugins](./blocks).
