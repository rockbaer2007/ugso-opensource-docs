---
title: Festtags-Card-Editor
description: Programmation de Noël avec cinq commandes, images de fêtes, décoration GIF et neige.
---

# Festtags-Card-Editor

**Version 0.1.12** · Éditeur DE/EN · Documentation DE/EN/FR.

[Deutsch](/projects/festtags-card-editor/) · [English](/en/projects/festtags-card-editor/)

![Commande de Noël avec un fond personnel, de la neige et deux commandes d’éclairage](/images/festtags-card-editor/weihnachtssteuerung-card.png)

Exemple d’un tableau de bord configuré. Le fond est fourni par l’utilisateur et n’est pas inclus dans l’application. La capture ne montre pas le mouvement des flocons.

## Fonctions

- Choix de la région puis du pays : 47 pays et dates personnalisées, traditions occidentales/juliennes.
- Jusqu'à cinq cibles (`light`, `switch`, `input_boolean`) avec des horaires individuels.
- Chaque jour dans une période ou uniquement lors des fêtes choisies ; calcul annuel de l'Avent et passage à l'année suivante automatiques.
- Période par défaut : premier dimanche de l'Avent jusqu'au 10 janvier inclus. Les pauses sont conservées après redémarrage.
- Capteurs pour les fêtes actuelles/suivantes et la prochaine commutation, avec une carte de tableau de bord.
- Icône d'état réelle facultative : `mdi:lightbulb` allumé, `mdi:lightbulb-outline` éteint.

Les listes nationales proposent des fêtes et coutumes, pas un calendrier légal complet. Premier/deuxième jour de Noël, Saint-Étienne, Sinterklaas, Pakjesavond, Trois Rois et Épiphanie sont des entrées séparées. Certaines correspondent à la même date.

## Installation et mises à jour

1. Créer une sauvegarde complète HA et ajouter/actualiser le [dépôt d'applications UGSo](https://github.com/rockbaer2007/ugso-ha-mqtt-addons).
2. Installer/mettre à jour et démarrer **Festtags-Card-Editor**. Architectures : aarch64 et amd64.
3. **Redémarrer Home Assistant entièrement**, pas seulement l'application, pour charger l'intégration actualisée.
4. Ouvrir l'éditeur. À la première installation, choisir **Set up integration**. Régler pays, cibles et horaires, puis enregistrer.
5. Cliquer sur **Register card resource**, puis recharger complètement le tableau de bord.

```yaml
type: custom:weihnachtssteuerung-card
title: Commande de Noël
```

Les réglages et images existants sont conservés. La programmation fonctionne dans HA Core même si l'application d'édition est arrêtée. Les administrateurs accèdent à l'éditeur par Ingress. La recherche des entités porte sur le nom, l'identifiant, la zone ou l'appareil. L'interface de l'éditeur existe en allemand et en anglais.

## Images et arrière-plans personnels

Aucune illustration n'est fournie. Utiliser ses propres fichiers avec les droits nécessaires.

| Utilisation | Dossier HA | Chemin URL |
| --- | --- | --- |
| Images par pays/fête | `/config/www/weihnachtssteuerung/bilder` | `/local/weihnachtssteuerung/bilder` |
| Arrière-plans et décorations | `/config/www/weihnachtssteuerung/background` | `/local/weihnachtssteuerung/background` |

Téléverser des fichiers PNG, JPG, WebP ou GIF (maximum 5 Mio/16 mégapixels) ; les animations restent intactes. Les SVG déjà présents peuvent être associés, mais pas téléversés. Les noms en double reçoivent un suffixe sans écrasement. **Unassign**/**No file** supprime uniquement l'association.

Les images de fêtes ont une hauteur de 110 px dans la carte, avec proportions conservées ; les aperçus de l'éditeur mesurent 90 × 90 px. Plusieurs images peuvent apparaître ensemble. Arrière-plan et décoration ont des réglages indépendants de transparence, taille et position X/Y. Transparence 0 % = visible, 100 % = invisible ; X/Y 0/0 = en haut à gauche, 100/100 = en bas à droite. L'assombrissement améliore la lisibilité. Textes et boutons restent utilisables au-dessus des effets.

## Chute de neige

- Sélectionner **Snowfall** ou **Image + snowfall**. Une décoration GIF séparée peut être activée en plus.
- 6 à 40 particules ; diamètre circulaire réel de 1 à 20 pixels CSS, par défaut 4 px.
- **Animate snowfall anyway** permet une exception explicite à la réduction des mouvements, uniquement pour cette carte. Désactivée par défaut.
- L'animation continue de se mettre en pause hors écran ou lorsque la page est masquée.
- Enregistrer ; après une mise à jour du fichier de la carte, enregistrer sa ressource et recharger le tableau de bord.

## Test Chrome confirmé le 25 novembre 2026

Sur une installation HA avec la carte **0.1.12**, un GIF chargé et **30 flocons animés simultanément** ont été confirmés. La position des particules a changé entre deux observations ; animation `snow-fall`, état `running`. Aucun réglage n'a été modifié pendant ce test combiné. Ce résultat ne garantit pas les performances de toutes les tablettes.

**Firefox anime, mais pas Chrome :** dans le cas observé, Chrome chargeait encore la ressource **0.1.8**. Un rechargement seul n'a pas remplacé l'ancienne référence. Dans l'éditeur actuel, cliquer sur **Register card resource**, puis recharger complètement le tableau de bord. Si la réduction des mouvements est active, enregistrer également l'exception explicite. La carte visible reprend l'animation lorsque le fichier actuel et l'exception sont effectifs.

## Liens

- [Version et téléchargements ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/festtags-card-editor-v0.1.12)
- [Sources et guide détaillé](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/festtags_card_editor)
- [UGSo HA Apps](/fr/projects-mqtt/)
