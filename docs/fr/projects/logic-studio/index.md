---
title: Logic Studio
description: Première version publique de test de l’éditeur graphique de blocs fonctionnels pour Home Assistant.
---
# <img class="package-icon" src="/images/logic-studio/icon.svg" width="40" height="40" alt=""> Logic Studio

**0.1.6 – première version publique de test, 8 novembre 2026.** Logic Studio est une application HA autonome pour les plans à blocs fonctionnels, indépendante de Grafik Visual Studio et Blocks for HA. L’éditeur est actuellement en **allemand** ; ce guide existe en **DE/EN/FR**.

::: warning Version de test
Installer d’abord sur un système de test et créer une sauvegarde complète. Les propriétés natives détaillées sont actuellement modifiables en JSON. L’application ne réécrit pas les automatisations/scripts dans HA et ne commande aucun appareil. Vérifier et installer soi-même les sorties générées.
:::

[Version de test GitHub et ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/logic-studio-v0.1.6) · [Sources dans le dépôt commun](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/logic_studio)

## Installation de test depuis GitHub

[![Ajouter le dépôt à Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Frockbaer2007%2Fugso-ha-mqtt-addons)

1. Dans **Paramètres → Applications → Boutique d’applications → Dépôts**, ajouter l’adresse ci-dessous. Si « UGSo HA Apps » est déjà configuré, rechercher les mises à jour.
2. Sélectionner et installer **UGSo Logic Studio**. Activer le mode avancé du profil HA si les applications expérimentales sont masquées.
3. Démarrer puis ouvrir l’interface. Compatible **HA OS/Supervised**, **amd64 et aarch64**. La première construction du conteneur peut prendre plusieurs minutes. Ce n’est pas un paquet frontend HACS/Marketplace.

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

**Conserver une installation locale existante :** les applications GitHub et locale ont des identifiants de dépôt et des données séparés. Exporter l’ancien plan en JSON avec **Projekt**, puis utiliser **Öffnen** dans l’application GitHub. Aucune migration ou désinstallation automatique. Chaque application conserve projet et réglages de palette sous `/data`.

## Deux types de plans

| Plan | Usage et sortie |
| --- | --- |
| Flux de valeurs | Entrées/sorties typées, logique, calcul, sélection, mémoires, fronts, temporisateurs et compteurs. 33 types implémentés ; les autres références sont marquées comme modèles. Export YAML d’automatisation HA, YAML de script HA ou fonction JavaScript avec interface hôte. |
| Flux HA natif | Importer automatisations, scripts et blueprints en blocs imbriqués. 53 types HA supplémentaires : déclencheurs, conditions, branches, boucles, attentes, variables et entrées de blueprint. Export uniquement en YAML HA natif. |

La simulation des flux de valeurs utilise des valeurs de démonstration/instantanées. Les blocs persistants nécessitent les helpers texte HA documentés ou un hôte mémoire JavaScript. Les flux HA natifs ne sont ni exécutés dans l’éditeur ni traduits automatiquement en JavaScript. La sortie JavaScript n’est pas un script ioBroker.

## Importation et modification

Ouvrir **HA importieren**, choisir automatisations/scripts/blueprints, puis **Aus HA einlesen**, un fichier YAML/JSON ou du texte. Sélectionner une entrée, vérifier l’aperçu et choisir **Import übernehmen**. Sauvegarder d’abord le projet existant en JSON ; des sauvegardes du projet et des sources sont aussi créées.

Le dossier de configuration HA est monté **en lecture seule**. L’application lit `automations.yaml`, `scripts.yaml` et les fichiers blueprint. Avant analyse, les sources sont copiées sous `/data/ha-source-backups/<horodatage>/` avec leurs noms d’origine. `secrets.yaml` n’est pas ouvert ; `!secret` et `!include` ne sont pas résolus. Importer manuellement les fichiers référencés par les inclusions.

Les liens orange **FLOW** représentent l’ordre et les branches : sortie de branche → **DO**, puis **NEXT → DO**. Les liens jaunes **VALUE/REF** montrent les paramètres de blueprint et leur utilisation `!input`. Configuration HA et chemins de branche sont modifiables en JSON. Les clés de paramètres/champs doivent être uniques. Les sections inconnues restent **YAML_ORIGINAL** ; des liens manquants peuvent bloquer l’export.

![Aperçu d’importation des blueprints HA existants](/images/logic-studio/blueprint-import.png)

Le **menu ⋮** de chaque bloc propose **Eigenschaften** (propriétés), **Duplizieren** (dupliquer) et **Löschen** (supprimer). La duplication copie les propriétés sans liens. La suppression retire les liens associés ; Annuler les restaure. Recherche, favoris et blocs récents facilitent la sélection.

![Menu à trois points d’un bloc](/images/logic-studio/block-menu.png)

## Validation et limites

La base fonctionnelle **0.1.5** a été testée sur **.193 / HA Core 2026.10.4** : import d’un blueprint réel, exemples d’automatisation/script/blueprint, exports YAML identiques sur le fond et actions du menu. **0.1.6** est sa première distribution publique. 22 tests Node et huit tests Python vérifient export, persistance, branches et import sûr ; les contrôles GitHub construisent aussi le conteneur.

L’éditeur ne valide pas toute la sémantique HA : vérifier cibles, templates et sélecteurs dans HA. Commentaires, ancres YAML et mise en forme ne sont pas reconstruits. Limites : **1 Mo, 200 blocs, 500 liens**, imbrication limitée et jusqu’à 250 fichiers blueprint dans les dossiers habituels. Régulateurs, calendrier et sous-plans personnalisés restent partiellement des modèles.

Pour un test local, extraire tout le ZIP, installer Python 3.10+ et les dépendances `requirements.txt`, puis lancer **Start-Demo.cmd** sous Windows. `http://127.0.0.1:4180/` affiche des entités de démonstration sans connexion HA. Le ZIP contient aussi `addon/logic_studio/` pour une installation locale.

[Signaler les problèmes sur GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/issues) avec versions, architecture et petit exemple anonymisé. Ne pas publier identifiants, automatisations personnelles ou sauvegardes complètes. Guides et rapport de test sont inclus. Licence MIT ; attribution des métadonnées de blocs dans `THIRD-PARTY.txt`.
