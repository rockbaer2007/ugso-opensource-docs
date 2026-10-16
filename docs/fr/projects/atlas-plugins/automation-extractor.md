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
- Version installable actuelle : `0.1.28`
- Interface en allemand, anglais et français ; la langue ATLAS enregistrée est appliquée à l’ouverture du plugin.

Dans l’Administration ATLAS, vous pouvez saisir directement l’URL GitHub. Lors de la vérification, ATLAS la convertit automatiquement en adresse `repository.json` correspondante.

Depuis 0.1.28, l'analyse compte les véritables éléments YAML des déclencheurs,
conditions et actions. Les en-têtes et étapes imbriquées n'ajoutent pas
d'éléments principaux. Les syntaxes moderne et classique sont prises en charge.
Paramètres et automatisations sources restent inchangés ; une sauvegarde
précède toujours l’analyse du fichier système chargé.

- lire `/config/automations.yaml` via le chemin File Studio autorisé ;
- sauvegarder le contenu chargé de `/config/automations.yaml` avant son analyse, dans `/config/atlas_backups/automations/<date-heure>/automations.yaml` ;
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

## Restauration sécurisée du plugin

Dans **Administration → Gestionnaire de plugins → Automation Exporter / Editor →
Restaurer**, choisir une sauvegarde existante. Vérifier version, direction et
compatibilité, puis utiliser l’action qui sauvegarde le plugin actuel et applique
la version choisie. Annuler conserve l’installation. Une modification simultanée
du plugin ou de sa gestion impose un nouvel aperçu.

Cette opération restaure le **paquet du plugin**. Elle ne rétablit pas un ancien
état des automatisations sources, exports, projets, corbeille ou historique. Elle
n’importe rien automatiquement dans Home Assistant et n’écrit pas dans
`automations.yaml`.

::: info Vérification isolée du 16/10/2026
Les vrais paquets **0.1.27 → 0.1.28 → 0.1.27 → 0.1.28** ont été vérifiés avec
ATLAS 0.1.312 : redémarrage, aperçu, annulation et restauration dans l’interface.
Un aperçu périmé est refusé après une modification effective de la gestion.
Dépôts et données de test isolées ont été sauvegardés avant les changements.
YAML source, exports existants, projet, autre plugin, corbeille et historique
restent identiques. Analyse DE/EN/FR, sauvegardes identiques à la source, paires
d’export/import avec/sans ID et ouverture dans File Studio réussissent. La version
HA provient d’un serveur de test local : ni authentification HA réelle, ni mise
à jour GitHub, ni migration de format ne sont qualifiées.
**Pi 5 et Proxmox sont restés inchangés pendant cet essai isolé.**
:::

::: info Vérification native ultérieure sur Pi 5 et Proxmox le 16/10/2026
Après de nouvelles sauvegardes HA locales et des copies supplémentaires sur PC,
les deux hôtes passent **0.1.28 installée → 0.1.27 → 0.1.28 d’origine**. Le vrai
ancien paquet est appliqué via l’aperçu de compatibilité du serveur ; annulation
et restauration de la nouvelle sauvegarde utilisent l’administration. Les hôtes
conservent ATLAS 0.1.312 et HA 2026.10.1.

Les neuf fichiers du plugin d’origine sont restaurés exactement. Automatisations
sources contrôlées, exports et sauvegardes d’automatisations existants, paramètres,
projets serveur, autres plugins, corbeille et historique sont conservés. L’analyse
d’un YAML de test importé est identique avant et après restauration. Aucune
automatisation utilisateur n’est exportée, exécutée ou réécrite dans HA ; aucun
redémarrage HA/App n’est nécessaire. Ce contrôle ne qualifie ni restauration HA
complète, ni migration de format, ni nouvelle publication GitHub.
:::

Après restauration, recharger l’administration et la page du plugin. Pendant
l’essai, l’administration ouverte signalait brièvement des changements non
enregistrés alors que l’état serveur était correctement restauré. Le rechargement
affichait de nouveau l’état partagé. Ne pas adopter un ancien état local pour
cette seule raison.

Langue et apparence sont enregistrées localement. Analyse chargée, sélection,
filtres, dossier d’export saisi et liste des exports appartiennent à la session.
Après rechargement, charger de nouveau la source et choisir le dossier si
nécessaire. Les fichiers déjà exportés restent disponibles dans File Studio.

## Rôle

ATLAS Automation Exporter / Editor complète File Studio : File Studio fournit une interface de fichiers sécurisée, tandis que l’Automation Exporter / Editor analyse et exporte les automatisations.
