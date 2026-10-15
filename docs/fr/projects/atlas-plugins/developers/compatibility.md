---
title: Versions et compatibilité
description: Numérotation, migrations de données et mises à jour sûres pour ATLAS et ses plugins.
---
# Versions et compatibilité

Ces règles de publication s'appliquent à partir du 15 octobre 2026. L'App 0.1.302 ajoute un contrôle automatique avant installation et mise à jour des plugins ; 0.1.303 détecte aussi la version HA connectée. Les installations et formats existants ne sont pas migrés.

## Quelle version utiliser ?

| Version | Signification |
| --- | --- |
| App/runtime ATLAS | Version du paquet Docker, App/Add-on ou Linux distribué. |
| Intégration HA | Version de `atlas_frontend` ; noter séparément le commit HACS. |
| Framework | Version indépendante pour chaque paquet `@atlas/*`, distincte de celle de l'App. |
| Plugin | Version indépendante et identifiant stable ; manifeste, catalogue et paquet doivent correspondre. |
| Format des données | Type et version du format enregistré ; une révision compte les changements pour détecter les conflits. |

Le Card Editor est livré avec ATLAS. Les plugins externes sont mis à jour indépendamment. Des numéros identiques entre composants ne prouvent pas leur compatibilité.

## Règles de publication

Utiliser `MAJOR.MINOR.PATCH` : PATCH pour les corrections compatibles, MINOR pour les fonctions compatibles et MAJOR pour les ruptures après stabilisation d'une interface 1.x. Avant 1.0, une rupture exige une nouvelle version MINOR et des instructions de migration. Une future rupture ne doit donc pas être publiée comme un autre correctif 0.1.x. Les anciennes versions ne sont pas renommées.

Les versions alpha désignent explicitement des versions de test. Un paquet publié dont le contenu change doit recevoir une nouvelle version ; une modification documentaire seule n'exige pas de nouvelle version du runtime. Indiquer le commit source et les combinaisons testées dans les notes de publication.

## Que vérifie ATLAS aujourd'hui ?

Les champs de dépôt `compatibility.atlas`, `host` et `homeAssistant` décrivent la compatibilité annoncée. `atlas` désigne l'App/runtime. Depuis 0.1.302, le serveur contrôle ensemble les déclarations du catalogue, du paquet et du manifeste inclus avant remplacement. Les plages SemVer comme `>=0.1.302 <0.2.0` sont évaluées. Une incompatibilité connue ou une condition invalide bloque le paquet et conserve la version installée. Une information absente signifie **non vérifié** et exige une confirmation explicite. Les plugins installés ne sont pas désactivés.

`host` accepte un nom ou une liste d'alternatives. `administration-local` conserve son sens historique d'installateur Node commun ; `docker`, `linux` et `homeassistant` correspondent à la cible configurée. La confirmation ne contourne pas une incompatibilité connue. L'aperçu n'écrit aucun fichier ; le serveur vérifie à nouveau lors de l'installation. Les imports locaux sont aussi contrôlés.

Depuis 0.1.303, l'Administration détecte la version HA via la réponse authentifiée `/api/config` de la connexion configurée. Les jetons et toute autre configuration HA restent sur le serveur. Une condition HA déclenche une nouvelle requête avant l'aperçu et l'installation ; les versions fournies par le navigateur sont ignorées. Des identifiants absents, délais dépassés, redirections, accès refusés ou réponses invalides restent **inconnus** et exigent une vérification explicite. Une ancienne valeur valide n'est jamais réutilisée. Les versions bêta, RC et de développement restent des préversions. Les champs inconnus exigent toujours une vérification. L'endpoint en lecture seule `/api/homeassistant/version` retourne uniquement les métadonnées de version filtrées ou une raison fixe d'échec ; il ne modifie ni paramètres ni projets.

La recherche de mises à jour compare numériquement les textes des versions ; ce n'est pas un résolveur SemVer complet. Séparément, les dépendances des modules du noyau acceptent les triplets numériques exacts, `^` et `*`, mais pas les plages générales ni les préversions. Pour une version majeure zéro, le contrôle caret actuel conserve la même version MINOR ; `^0.0.3` accepte aussi `0.0.4`. Préférer des versions exactes pour ces modules.

L'identifiant et la version du paquet sont comparés au manifeste avant remplacement ; les mises à jour par dépôt doivent aussi correspondre à la version du catalogue. Les capacités déclarées ne sont ni des autorisations automatiques ni un bac à sable. Des versions compatibles ne remplacent ni les tests fonctionnels ni l'évaluation de confiance d'un plugin.

## Préserver et restaurer les données

1. Avant une mise à jour, sauvegarder HA et les données ATLAS, ou l'installation autonome avec ses données et son identité. Exporter aussi les paramètres Admin locaux, projets et métadonnées partagées des plugins. Les données propres aux plugins et collections du navigateur demandent des sauvegardes distinctes.
2. Conserver l'adresse du runtime, les chemins persistants et l'identité. Les paramètres chiffrés ne deviennent pas automatiquement transférables vers une autre installation. Une sauvegarde du code ne remplace pas celle des données.
3. Mettre à jour un composant à la fois ; redémarrer HA après les mises à jour de l'intégration comme indiqué. Vérifier ensuite paramètres, projets et plugins actifs.
4. Restaurer ensemble le code **et** les données correspondantes. Un ancien programme ne doit pas écraser un format plus récent inconnu.

Les futures migrations exigent un aperçu sans écriture, la sauvegarde de l'original, la transformation et validation d'une copie, une application explicite, le contrôle des conflits et un remplacement atomique. Ne jamais remplacer un format inconnu ou corrompu par des données vides. Répétitions et échecs doivent préserver les données. Ce sont des exigences, pas une migration universelle déjà disponible.

Depuis ATLAS 0.1.304, chaque remplacement conserve une sauvegarde vérifiée du paquet sous `<ATLAS_PLUGIN_DATA_ROOT>/.recovery`, dans le volume persistant existant et exclue des fichiers publics des plugins. Dans le gestionnaire, Importer un paquet remplace un plugin existant seulement après un aperçu et Sauvegarder et appliquer. Restaurer propose les versions sauvegardées. Le sens du changement de version et les capacités sont visibles ; une compatibilité inconnue exige une confirmation, une incompatibilité connue bloque l’application. Les aperçus périmés sont refusés. Fichiers et métadonnées partagées sont repris ensemble, en conservant activation et dépôts. Une restauration sauvegarde aussi la version actuellement installée.

Cette fonction restaure le code du plugin. Identifiants, projets, collections du navigateur et formats de données des plugins ne sont ni réinitialisés ni migrés. Des sauvegardes complètes et des données correspondantes restent nécessaires. Limites par plugin : 300 fichiers/20 MB par sauvegarde, 256 MiB et 200 sauvegardes au total. Aucune suppression automatique ; un stockage plein ou illisible bloque le remplacement. Le Card Editor intégré reste mis à jour avec ATLAS. La vérification native de cette interface sur Pi et Proxmox reste à effectuer.

## Périmètre vérifié

Les mises à jour de commit HACS et redémarrages HA ont réussi sur Pi 5 et Proxmox en préservant paramètres, projets et plugins. L'intégration est restée en 0.1.301 avec un code inchangé. Une vraie migration de version/schéma et d'autres versions HA restent à vérifier. Les nouvelles migrations nécessitent des tests des formats anciens, actuels et inconnus, des échecs, conflits et restaurations.

La [politique technique du dépôt source](https://github.com/rockbaer2007/atlas/blob/main/docs/project/specifications/VERSION_COMPATIBILITY_POLICY.md) précise les règles et leurs limites.
