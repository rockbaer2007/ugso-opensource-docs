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

1. **A1 – Installation HA réelle :** vérifier la mise à jour Supervisor, Ingress, les entités et les plugins installés en conservant les réglages et projets.
2. **A2 – ARM64 et mobile :** vérifier Raspberry Pi, les dispositions, dialogues et imports/exports sur mobile.
3. **A3 – Simple/Expert :** clarifier le sélecteur prévu avec le démarrage Expert actuel, sans perdre les projets.
4. **A5 – Production :** vérifier et améliorer Renderer, Theme et les API des plugins avec des projets réels plus grands, les mises à jour et reconnexions.
5. **A6 – Documentation française :** compléter les pages FR et aligner la structure et le contenu DE/EN/FR.
6. **A7 – Déploiement :** préparer l'installateur Linux/systemd et l'intégration native ATLAS HA/HACS avec le même runtime.

**A4 – Le nettoyage de la feuille de route est terminé.** Les fonctions achevées
restent dans l'historique et ne sont plus des tâches ouvertes. Les plugins
indépendants conservent leurs propres listes de travaux.
La liste de référence se trouve dans la [feuille de route ATLAS](https://github.com/rockbaer2007/atlas/blob/main/ROADMAP.md).

::: info État évolutif
La feuille de route évolue avec le développement. Consultez les pages ATLAS et
Plugins ATLAS pour connaître les fonctions documentées.
:::
