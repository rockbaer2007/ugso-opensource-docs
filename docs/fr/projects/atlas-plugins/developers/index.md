---
title: Développement de plugins
description: Guide technique pour les développeurs de plugins ATLAS.
---
# Développement de plugins

Cette rubrique présente le parcours de création d'un plugin ATLAS autonome, du projet de départ au manifeste, au Runtime et à la publication. Les contrats évoluent encore ; vérifiez le modèle et le format de dépôt actuels avant toute publication.

## Parcours recommandé

1. Créez un dépôt à partir du [modèle officiel de plugin](../plugin-template).
2. Choisissez un identifiant unique et stable, puis renseignez le nom, la version, la description, les ressources et les capacités nécessaires dans le manifeste.
3. Développez d'abord l'interface du plugin de manière indépendante. Le modèle actuel contient une petite page d'exemple en HTML/CSS/JavaScript.
4. Générez le paquet et le catalogue avec `npm run build`, puis vérifiez-les avec `npm run check`.
5. Testez le catalogue via le dépôt de démonstration ATLAS ou l'Administration. Augmentez la version du plugin pour chaque modification publiée.

## Guides

- [Versions et compatibilité](./compatibility) : règles de publication, limites vérifiées, sauvegardes et migrations.
- [Manifeste et capacités](./manifest) : métadonnées, identifiants, versions, ressources et déclarations.
- [Runtime et cycle de vie](./runtime) : contrat Runtime et activation, désactivation et nettoyage.
- [Construire, valider et publier](./publishing) : générateur de paquet, catalogue, GitHub Actions et liste de contrôle.
- [Modèle de plugin](../plugin-template) : guide pas à pas du dépôt de démarrage GitHub.
- [Format du dépôt](../repository-format) : champs du catalogue et format du paquet installable.

## Limites de sécurité

Déclarez uniquement les capacités réellement utilisées par votre plugin. Une déclaration décrit son objectif ; ce n'est ni une sandbox ni un accès automatique à Home Assistant ou aux composants internes d'Atlas. Ne demandez pas d'identifiants dans les fichiers du plugin et ne publiez jamais de jeton ni de clé API.

Le serveur App installe les paquets validés, depuis un dépôt ou un import, dans le stockage persistant et sert les fichiers web sous `/plugin-assets/<slug>/`. Leur JavaScript s’exécute dans le navigateur à l’ouverture ; les modules Node ou hooks Runtime ne sont pas enregistrés automatiquement. Ce n’est pas une sandbox : vérifier paquet et code avant ouverture.
