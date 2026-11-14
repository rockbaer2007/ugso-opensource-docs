---
title: Palette, utilisés récemment et exécution
description: Miniatures, widgets récents enregistrés et démarrage/arrêt dans Studio 0.1.299.
---

# Palette, utilisés récemment et exécution

**Studio 0.1.299** inclut la nouvelle palette et l’exécution intégrée précédemment testée localement dans 0.1.298. [Mise à jour GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/grafik-visual-studio-v0.1.299).

## Miniatures et descriptions

La palette présente trois tuiles identiques par ligne : miniature en haut, nom en dessous. Les instruments utilisent leur propre rendu avec des valeurs de démonstration ; appareils et horloges utilisent des miniatures statiques originales. Les images des paquets sont conservées. Survol ou focus clavier : aperçu agrandi et courte description. Les groupes UGSo et SVG-Line/LineBox/Math affichent uniquement leur nom. Les aperçus ne commandent aucun appareil.

## Utilisés récemment

Le groupe **Utilisés récemment**, repliable indépendamment, apparaît directement sous la recherche. Il conserve jusqu’à **douze types de widgets distincts**, le dernier inséré en premier. Réinsérer le même type le replace en tête sans doublon. Tuiles, miniatures et descriptions correspondent à la palette normale.

Un clic insère un nouveau widget avec les valeurs par défaut du type, **pas une copie du dernier widget modifié**. Importer, coller depuis le presse-papiers ou simplement sélectionner un widget ne modifie pas la liste. La recherche filtre également les entrées récentes. Les types de paquets désinstallés ne sont pas proposés ; ils peuvent réapparaître après réinstallation.

Liste et état replié persistent après rechargement ou mise à jour dans le **même profil de navigateur et à la même adresse web**. Ils ne sont ni synchronisés entre appareils ni exportés avec les projets. Effacer les données du navigateur les réinitialise. Si le stockage est bloqué, la liste reste utilisable pendant la session. Les autres réglages et fichiers de projet restent inchangés.

![Widgets récemment utilisés sur le système de test ARM (Pi 5)](/images/grafik-visual-studio/recent-177-299.jpg)

## Exécution au-dessus de la surface

**▶** près des onglets sauvegarde le projet courant puis démarre une exécution isolée au-dessus de la surface. **■** l’arrête. Palette, propriétés et outils d’édition, raccourcis compris, sont grisés et verrouillés. Navigation entre pages et fenêtre séparée restent accessibles. Un échec de sauvegarde empêche le démarrage.

L’arrêt restitue la page initiale de l’éditeur avec sélection, historique et défilement. La navigation de l’aperçu ne change pas la page de l’éditeur. Les widgets à onglets propres conservent leur contexte initial. Les anciens liens de mode Éditeur/Exécution sont retirés du menu ; **Nouvel onglet** ouvre toujours l’exécution indépendante. Les widgets d’exécution peuvent commander les appareils HA comme auparavant.

![Exécution intégrée avec outils d’édition grisés](/images/grafik-visual-studio/inline-runtime-298.jpg)

## Conservation et vérification

Projets, types de widgets, CSS et couleurs existants conservés. Les nouvelles préférences utilisent une clé de stockage distincte. Aucun code ni illustration VIS-2 n’a été copié pour ces fonctions.

Le 8 novembre 2026, la version 0.1.299 a été vérifiée sur le [système de test ARM (Pi 5)](/fr/collection/test-systems#testsystem-arm) (HA 2026.11.0/ARM64) et [système de test PC (64)](/fr/collection/test-systems#testsystem-pc) (HA 2026.10.4/amd64) : miniatures récentes, ordre sans doublons, insertion, repli et conservation après rechargement, ainsi que verrouillage pendant la runtime intégrée. Les insertions de test ont été annulées ; les 13 et 11 widgets existants ont été conservés. Palette et démarrage/arrêt ont également été vérifiés avec sauvegarde, navigation et retour à l’éditeur. Les 23 tests JavaScript et 17 tests Python ont réussi. Détails : [sources et rapports](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/docs).
