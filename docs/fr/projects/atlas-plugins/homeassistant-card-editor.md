---
title: Home Assistant Card Editor
description: "Plugin de référence ATLAS : workflow Expert, commandes mobiles, connexion et points d’extension."
---

# Home Assistant Card Editor

Le Home Assistant Card Editor est le premier plugin officiel de référence ATLAS.
Il illustre le cycle de vie, la découverte, l’Administration, le Hub,
l’import/export et la création de packages. Son
[guide utilisateur](/fr/projects/atlas/card-editor) détaille les cartes et les styles.

## Objectif

Au 16/10/2026 : plugin de référence **0.2.0-alpha.108** dans l’App **0.1.312**.
Il est mis à jour avec ATLAS, pas comme un plugin externe à remplacer.
Voir le [guide de l’éditeur](../atlas/card-editor) et les
[projets App/Runtime](../atlas/frontend) pour projets partagés et parcours HACS.

Décision du 13/10/2026 : l’éditeur conserve uniquement le workflow Expert.
Le mode Simple et son sélecteur ne seront pas réintroduits. Les imports de
projets anciens pris en charge restent compatibles.

Depuis l’application HA **0.1.292**, le choix du mode de démarrage disparaît
aussi de la configuration HA et de l’Administration. Les anciennes valeurs
Simple sont traitées comme Expert ; identifiants et autres paramètres sont conservés.

Le plugin propose la sélection d’entités, les vérifications de ressources,
l’import YAML/JSON, les bundles destinés à HACS et les packages multilingues.
Les cellules de la grille restent carrées. Le curseur horizontal règle les
colonnes et le curseur vertical les lignes ; Zoom modifie la taille des cellules
et leurs deux dimensions ensemble.

## Liste des cartes sur tablette

Depuis l’application HA **0.1.290**, une largeur d’éditeur de 521 à 1180 pixels
affiche deux cartes côte à côte dans une fenêtre défilante. Sa hauteur suit
la première rangée et reste limitée sur les écrans peu hauts. Le défilement
donne accès aux autres cartes. Les boutons au-dessus de la liste utilisent
aussi deux colonnes de même largeur. Les téléphones étroits conservent une
colonne ; la barre latérale de bureau reste inchangée. La largeur de l’éditeur
intégré détermine la présentation, pas le nom de l’appareil.
Les projets, favoris et paramètres existants sont conservés.

## Commandes mobiles de grille et de titre

Depuis l’application HA **0.1.291**, Grille et zoom est replié par défaut jusqu’à
une largeur d’éditeur de 1180 pixels. Touchez le titre pour afficher X, Y et Zoom ;
ouvrir ou fermer le groupe ne modifie aucune valeur ou carte. À la largeur
de bureau, les curseurs s’affichent directement.

Sur tablette, le champ de titre et les deux boutons d’application du titre
et du nom d’entité partagent une rangée. Sur téléphone étroit, le champ se
trouve au-dessus des deux boutons de même largeur. Cela s’applique en DE/EN/FR.

## Connexion avec de grands catalogues d’entités

Depuis l’application HA **0.1.293**, ATLAS traite les instantanés d’entités
et événements en direct dans leur ordre d’arrivée. Un instantané en cours
ne peut plus terminer après un événement reçu ensuite et remplacer sa valeur
par une ancienne. Les messages d’une connexion fermée sont ignorés ; l’échec
d’un nouveau socket affiche son propre état. Les cartes, positions et
identifiants enregistrés restent inchangés.

## Points d’extension

Le plugin utilise :

- `homeassistant.card-editor`
- `homeassistant.card-target`
- `homeassistant.entity-picker`
- `homeassistant.exporter`
- `atlas.plugin.package-builder`

## Package

`createHomeAssistantCardEditorPluginInstallPackage()` crée le package
d’installation avec son manifeste, un README et un exemple de configuration HA.

## Description dans le Hub

Le Hub et l’Administration utilisent les descriptions localisées du dépôt.
La langue sélectionnée donne la priorité à `descriptions.de`,
`descriptions.en` ou `descriptions.fr` lorsqu’elles sont disponibles ;
l’anglais reste la langue de repli.
