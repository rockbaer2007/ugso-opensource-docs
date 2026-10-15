---
title: Versions et compatibilité
description: Numérotation, migrations de données et mises à jour sûres pour ATLAS et ses plugins.
---
# Versions et compatibilité

Ces règles de publication s'appliquent à partir du 15 octobre 2026. Elles ne modifient ni les installations existantes ni les formats de données. Le contrôle automatique bloquant de compatibilité n'est pas encore implémenté.

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

Les champs de dépôt `compatibility.atlas`, `host` et `homeAssistant` décrivent la compatibilité annoncée. `atlas` désigne l'App/runtime. Ces valeurs sont affichées mais ne bloquent pas l'installation. Une information absente signifie **non vérifié**. Les plugins existants restent utilisables.

La recherche de mises à jour compare numériquement les textes des versions ; ce n'est pas un résolveur SemVer complet. Séparément, les dépendances des modules du noyau acceptent les triplets numériques exacts, `^` et `*`, mais pas les plages générales ni les préversions. Pour une version majeure zéro, le contrôle caret actuel conserve la même version MINOR ; `^0.0.3` accepte aussi `0.0.4`. Préférer des versions exactes pour ces modules.

L'identifiant et la version du paquet sont comparés au manifeste avant remplacement. Les capacités déclarées ne sont ni des autorisations automatiques ni un bac à sable. Un futur contrôle doit aussi s'effectuer côté serveur avant remplacement et prendre en compte les paquets existants sans nouvelles métadonnées.

## Préserver et restaurer les données

1. Avant une mise à jour, sauvegarder HA et les données ATLAS, ou l'installation autonome avec ses données et son identité. Exporter aussi les paramètres Admin locaux, projets et métadonnées partagées des plugins. Les données propres aux plugins et collections du navigateur demandent des sauvegardes distinctes.
2. Conserver l'adresse du runtime, les chemins persistants et l'identité. Les paramètres chiffrés ne deviennent pas automatiquement transférables vers une autre installation. Une sauvegarde du code ne remplace pas celle des données.
3. Mettre à jour un composant à la fois ; redémarrer HA après les mises à jour de l'intégration comme indiqué. Vérifier ensuite paramètres, projets et plugins actifs.
4. Restaurer ensemble le code **et** les données correspondantes. Un ancien programme ne doit pas écraser un format plus récent inconnu.

Les futures migrations exigent un aperçu sans écriture, la sauvegarde de l'original, la transformation et validation d'une copie, une application explicite, le contrôle des conflits et un remplacement atomique. Ne jamais remplacer un format inconnu ou corrompu par des données vides. Répétitions et échecs doivent préserver les données. Ce sont des exigences, pas une migration universelle déjà disponible.

L'installateur restaure l'ancien dossier si son remplacement échoue ; après succès, il ne le conserve pas comme archive de retour arrière. Les sauvegardes partagées des plugins contiennent les métadonnées, pas tous leurs fichiers et données.

## Périmètre vérifié

Les mises à jour de commit HACS et redémarrages HA ont réussi sur Pi 5 et Proxmox en préservant paramètres, projets et plugins. L'intégration est restée en 0.1.301 avec un code inchangé. Une vraie migration de version/schéma et d'autres versions HA restent à vérifier. Les nouvelles migrations nécessitent des tests des formats anciens, actuels et inconnus, des échecs, conflits et restaurations.

La [politique technique du dépôt source](https://github.com/rockbaer2007/atlas/blob/main/docs/project/specifications/VERSION_COMPATIBILITY_POLICY.md) précise les règles et leurs limites.
