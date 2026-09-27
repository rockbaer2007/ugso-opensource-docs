---
title: ATLAS Automation Exporter / Editor
description: Analyser et exporter les automatisations Home Assistant avec ATLAS.
---
# ATLAS Automation Exporter / Editor

ATLAS Automation Exporter / Editor est un plugin autonome d’ATLAS. Il reprend l’idée de l’ancien outil Windows de séparation de `automations.yaml` et l’intègre directement à l’architecture des plugins ATLAS.

## Objectif

Le plugin analyse les automatisations Home Assistant, exporte les éléments sélectionnés et prépare leur modification dans File Studio.

## Dépôt

- GitHub : `https://github.com/rockbaer2007/atlas-automation-exporter-editor-plugin`
- Page d’installation : `https://rockbaer2007.github.io/atlas-automation-exporter-editor-plugin/install.html`
- Fichier du dépôt : `https://raw.githubusercontent.com/rockbaer2007/atlas-automation-exporter-editor-plugin/main/repository.json`
- Version installable actuelle : `0.1.25`
- Interface en allemand, anglais et français ; la langue ATLAS enregistrée est appliquée à l’ouverture du plugin.

Dans l’Administration ATLAS, vous pouvez saisir directement l’URL GitHub. Lors de la vérification, ATLAS la convertit automatiquement en adresse `repository.json` correspondante.

- lire `/config/automations.yaml` via le chemin File Studio autorisé ;
- créer une sauvegarde avant de lire le véritable `/config/automations.yaml`, dans `/config/atlas_backups/automations/<date-heure>/automations.yaml` ;
- analyser les fichiers `.yaml` et `.yml` importés ;
- afficher l’ID, l’alias, la description, les déclencheurs, les conditions et les actions ;
- détecter les appels de service au format classique `service:` et au format moderne `action: domain.service` ;
- conserver une automatisation contenant un fragment de déclencheur ou d’action à la racine comme une seule entrée afin d’éviter de faux conflits ;
- conserver les déclencheurs horaires au format `HH:MM:SS` entre guillemets et convertir les valeurs numériques en secondes, par exemple `25200` en `'07:00:00'` ;
- signaler les ID ou alias absents ou en double, les déclencheurs ou actions manquants et les automatisations désactivées ;
- marquer les ID et alias en double comme conflits dans la liste ;
- filtrer les automatisations qui comportent des avertissements ;
- afficher le YAML détaillé avec une coloration similaire à File Studio ;
- limiter la liste à environ 15 lignes visibles et la faire défiler indépendamment ;
- afficher les entités, scripts, scènes, assistants et cibles de notification associés ;
- regrouper et filtrer les automatisations par domaine, zone ou appareil ;
- choisir le dossier d’exportation et enregistrer la sélection dans un dossier horodaté ;
- créer deux fichiers portant le même nom : une version d’exportation avec `id` et une version d’importation nettoyée sans `id` pour l’éditeur YAML Home Assistant ;
- consulter les automatisations exportées et préparer leur modification dans File Studio.

## Sécurité

Le plugin n’écrit pas dans les fichiers système de Home Assistant. Il lit les fichiers YAML système ou importés, crée une sauvegarde avant d’ouvrir le véritable `automations.yaml`, analyse les automatisations et exporte des fichiers YAML séparés. La restauration manuelle et la modification ultérieure se font dans File Studio et avec les outils YAML de Home Assistant.

## Rôle

ATLAS Automation Exporter / Editor complète File Studio : File Studio fournit une interface de fichiers sécurisée, tandis que l’Automation Exporter / Editor analyse et exporte les automatisations.
