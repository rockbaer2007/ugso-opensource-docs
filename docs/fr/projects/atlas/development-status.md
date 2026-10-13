---
title: État du développement
description: État actuel du développement d'ATLAS.
---
# État du développement

## État actuel

Au **13/10/2026** : framework **0.2.0-alpha.88**, application HA **0.1.289**.
Les quatre étapes de stabilisation sont terminées. La vérification couvre
870 tests des paquets, cinq tests supplémentaires, les contrôles de types et
les builds, ainsi que 15 étapes dans un navigateur isolé en DE/EN/FR. La migration
testée conserve les anciens réglages Admin, dépôts, thème et plugins actifs ;
les secrets passent dans le stockage chiffré.

A1 est vérifié sur l'installation HA réelle : mise à jour Supervisor de 0.1.287
à 0.1.288, redémarrage séparé et Ingress pour les six plugins installés.
Les réglages Admin, plugins actifs et la configuration complète de l'éditeur
restent identiques avant et après la mise à jour et le redémarrage, sauf les
horodatages d'export. Une sauvegarde HA locale chiffrée a été créée auparavant.
0.1.288 corrige la version affichée dans l'Administration ; les options HA et
contrats des plugins restent inchangés. L'éditeur se reconnecte et charge les
entités et ressources Lovelace réelles. Le canevas Expert existant était vide ;
les projets plus grands restent A5. Le matériel, les navigateurs mobiles, ARM64
et tous les formats de projets propres aux plugins ne sont pas vérifiés.

A2 est vérifié en émulation : images HA amd64 et ARM64 et contexte Chromium
mobile tactile à 360×800, 390×844, 844×390 et 768×1024 en DE/EN/FR. 0.1.289
corrige les débordements de l'Administration et de l'éditeur et adapte les
dialogues de rapport, import YAML et export aux écrans étroits. Les réglages,
projets de test remplis et données des plugins sont conservés après changement
de langue, import JSON/HACS et redémarrage. ARM64 est émulé sur x86 ; Raspberry
Pi natif, Android/iOS, glisser/redimensionner au toucher, clavier virtuel et
dialogues natifs de fichiers/téléchargements restent à vérifier. Ces tests
isolés ne modifient pas l'installation HA réelle.

ATLAS est en cours de développement. L'application Home Assistant comprend
l'Administration, le Hub des plugins et le Card Editor ; File Studio et
Automation Exporter / Editor sont distribués comme plugins indépendants.

La version actuelle de l'application Home Assistant est `0.1.289`.
L'Administration et le Hub des plugins proposent des interfaces en allemand,
anglais et français. Leur préférence de langue enregistrée est partagée entre
les deux interfaces, y compris lorsque leurs ports sont différents. Le
paramètre `language` d'une URL reste prioritaire pour la page ouverte.

## Suite du travail

1. **A2 – Appareils ARM64/mobiles réels :** après l'émulation, vérifier Raspberry Pi, Android/iOS, gestes tactiles, clavier, dialogues natifs de fichiers/téléchargements et Ingress.
2. **A3 – Simple/Expert :** clarifier le sélecteur prévu avec le démarrage Expert actuel, sans perdre les projets.
3. **A5 – Production :** vérifier et améliorer Renderer, Theme et les API des plugins avec des projets réels plus grands, les mises à jour et reconnexions.
4. **A6 – Documentation française :** compléter les pages FR et aligner la structure et le contenu DE/EN/FR.
5. **A7 – Déploiement :** préparer l'installateur Linux/systemd et l'intégration native ATLAS HA/HACS avec le même runtime.

**A1 – Installation HA réelle et A4 – Nettoyage de la feuille de route sont terminés.** Les fonctions achevées
restent dans l'historique et ne sont plus des tâches ouvertes. Les plugins
indépendants conservent leurs propres listes de travaux.
La liste de référence se trouve dans la [feuille de route ATLAS](https://github.com/rockbaer2007/atlas/blob/main/ROADMAP.md).

::: info État évolutif
La feuille de route évolue avec le développement. Consultez les pages ATLAS et
Plugins ATLAS pour connaître les fonctions documentées.
:::
