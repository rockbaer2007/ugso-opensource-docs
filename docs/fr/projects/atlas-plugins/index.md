---
title: Plugins ATLAS
description: Documentation des extensions installables pour ATLAS.
---
# Plugins ATLAS

Cette rubrique présente les extensions installables d'ATLAS : format des dépôts, publication, mises à jour et pages consacrées à chaque plugin.

::: warning État du développement
Les interfaces de plugins sont encore en cours d'élaboration. La documentation décrit l'état actuel d'ATLAS et sera complétée à mesure que les contrats se stabiliseront.
:::

## Pour commencer

- [Format du dépôt](./repository-format) : structure de `repository.json`, champs obligatoires, identifiant ATLAS et exemple.
- [Modèle de plugin](./plugin-template) : utiliser le modèle, personnaliser un plugin, créer son paquet et le publier.
- [Plugins vérifiés](./verified-plugins) : liste des plugins vérifiés et des nouvelles propositions qui restent à examiner.
- [Home Assistant Card Editor](./homeassistant-card-editor) : premier plugin de référence officiel d'ATLAS.
- [ATLAS File Studio](./file-studio) : plugin indépendant pour les chemins Home Assistant autorisés.
- [ATLAS Terminal](./terminal) : terminal web authentifié avec couleurs ANSI, SSH facultatif, thèmes Oh My Posh et police Nerd Font servie par le serveur.
- [ATLAS Automation Exporter / Editor](./automation-extractor) : analyse, sauvegarde de sécurité et export d'automatisations Home Assistant.
- [Dépôt de démonstration](./demo-repository) : dépôt public de test pour l'Administration, le Hub et le parcours d'installation.

## Objectif

Les plugins ATLAS étendent la plateforme sans modifier directement ses paquets centraux. Ils peuvent fournir des outils liés à Home Assistant, des éditeurs de cartes, des outils de diagnostic, des moteurs de rendu, des thèmes, des fournisseurs ou, à terme, des extensions communautaires.

## Cycle de vie

Un plugin doit pouvoir être installé, vérifié, activé, mis à jour et supprimé de manière traçable :

1. Lire le manifeste.
2. Vérifier les dépendances.
3. Enregistrer le plugin.
4. Fournir des services, commandes ou interfaces.
5. Activer le plugin.
6. Signaler les diagnostics et l'état.
7. Désactiver le plugin ou le supprimer proprement.

## Référence technique actuelle

L'adaptateur Runtime constitue le point d'entrée actuel. `createRuntimeModuleFromPlugin()` convertit un `RuntimePlugin` en module Runtime ATLAS. `RuntimePluginCatalog` permet la découverte ; l'Administration affiche les plugins, compare leurs versions et prépare les installations locales.

Le Hub suit une règle de démarrage simple : sans plugin installé, il renvoie vers l'Administration ; avec un seul plugin actif, il ouvre directement celui-ci ; avec deux plugins actifs ou plus, il affiche la page de sélection. Les plugins planifiés ou désactivés peuvent être affichés, mais ne démarrent pas automatiquement.

Le Hub peut aussi préparer des entrées de barre latérale Home Assistant. La fenêtre affiche dynamiquement le nom, l'URL, la version, l'état et l'icône proposée, puis copie l'URL seule ou un bloc `panel_iframe` prêt à utiliser dans `configuration.yaml`. Les listes de capacités et les URL restent repliées par défaut afin de garder le Hub compact.

En mode App/Add-on, Card Editor, Administration et les ressources locales des plugins sont servies par les routes de l'application ATLAS. Les chemins de base Home Assistant Ingress sont ainsi conservés dans le Hub et les liens de barre latérale.

Les nouveaux plugins locaux reçoivent une URL de lancement automatique si leur dossier contient `index.html` et que le manifeste ne définit pas `entry`. ATLAS publie alors `/plugin-assets/<dossier-du-plugin>/index.html`.

## Règles de publication

Un plugin publiable doit avoir un nom clair, une version explicite, des dépendances documentées, des données de démonstration ou de repli sûres, des artefacts de build traçables et des indications pour ATLAS, Home Assistant ou HACS.

## Automation Exporter / Editor

ATLAS Automation Exporter / Editor ajoute des outils pour détecter les automatisations, afficher leurs dépendances, créer une sauvegarde de sécurité lors de la lecture et exporter une version d'archive qui conserve l'`id`, ainsi qu'une version d'import nettoyée sans `id` pour l'éditeur YAML de Home Assistant.
