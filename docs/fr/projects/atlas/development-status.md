---
title: État du développement
description: État actuel du développement d'ATLAS.
---
# État du développement

## État actuel

Au **13/10/2026** : framework **0.2.0-alpha.88**, application HA **0.1.287**.
Les quatre étapes de stabilisation sont terminées. La vérification couvre
870 tests des paquets, cinq tests supplémentaires, les contrôles de types et
les builds, ainsi que 15 étapes dans un navigateur isolé en DE/EN/FR. La migration
testée conserve les anciens réglages Admin, dépôts, thème et plugins actifs ;
les secrets passent dans le stockage chiffré.

La dernière modification concerne uniquement les tests et la documentation.
Le fonctionnement, les options HA et les contrats des plugins restent inchangés.
Les mises à jour réelles du Supervisor, le matériel, les navigateurs mobiles et
l'exécution ARM64 n'ont pas été vérifiés.

ATLAS est en cours de développement. L'application Home Assistant comprend
l'Administration, le Hub des plugins et le Card Editor ; File Studio et
Automation Exporter / Editor sont distribués comme plugins indépendants.

La version actuelle de l'application Home Assistant est `0.1.287`.
L'Administration et le Hub des plugins proposent des interfaces en allemand,
anglais et français. Leur préférence de langue enregistrée est partagée entre
les deux interfaces, y compris lorsque leurs ports sont différents. Le
paramètre `language` d'une URL reste prioritaire pour la page ouverte.

## Suite du travail

- Étendre progressivement la traduction aux interfaces de plugins qui déclarent
  leurs propres textes localisés.
- Continuer à intégrer les fonctions Renderer et Theme dans des parcours visibles
  de l'application.
- Stabiliser les API et les contrats avant une version de production.

::: info État évolutif
La feuille de route évolue avec le développement. Consultez les pages ATLAS et
Plugins ATLAS pour connaître les fonctions documentées.
:::
