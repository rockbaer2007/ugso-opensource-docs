---
title: ATLAS Terminal
description: Plugin ATLAS indépendant pour un terminal web authentifié, avec couleurs ANSI et cible SSH facultative.
---
# ATLAS Terminal

ATLAS Terminal est un dépôt de plugin indépendant qui fournit un terminal web authentifié. Il propose les couleurs ANSI, une taille de police réglable et une connexion SSH facultative vers une cible configurée côté serveur. L'invite s'inspire d'Oh My Posh.

## Dépôt et installation

- GitHub : [rockbaer2007/atlas-terminal-plugin](https://github.com/rockbaer2007/atlas-terminal-plugin)
- Page d'installation : [Ajouter ATLAS Terminal](https://rockbaer2007.github.io/atlas-terminal-plugin/install.html)
- Manifeste du dépôt : [repository.json](https://raw.githubusercontent.com/rockbaer2007/atlas-terminal-plugin/main/repository.json)
- Version du plugin : `0.1.1`

Dans l'Administration ATLAS, ouvrez **Plugins → Ajouter un dépôt**, choisissez **Plugin** et saisissez l'URL du manifeste. Vérifiez le dépôt, puis installez le paquet du plugin. L'hôte ATLAS doit fournir un backend Terminal compatible.

## Fonctionnalités

- terminal web avec couleurs ANSI
- taille de police réglable localement
- cible SSH facultative avec hôte, utilisateur, clé et fichier `known_hosts` configurés côté serveur
- vérification de la clé d'hôte maintenue ; le navigateur ne peut pas choisir une cible SSH arbitraire
- interface versionnée séparément dans le dépôt du plugin

## Prérequis et sécurité

Le dépôt contient l'interface du plugin, mais **ce n'est ni un serveur SSH autonome ni un module complémentaire Home Assistant**. L'hôte ATLAS fournit le shell ainsi que les fonctions Supervisor et WebSocket. La déclaration de compatibilité indique ATLAS `>=0.2.0-alpha.76` et Home Assistant `>=2026.8`.

Le terminal est désactivé par défaut. Activez-le uniquement après avoir configuré sur l'hôte ATLAS un jeton d'accès aléatoire et robuste d'au moins 32 caractères sûrs pour les URL. Le shell local s'exécute avec les droits du processus ATLAS. En mode App/Add-on Home Assistant, les permissions Supervisor peuvent également autoriser des commandes `ha` d'administration. Considérez donc l'accès au terminal comme un accès administratif.

Le jeton reste dans le stockage local du navigateur et est transmis lors de la connexion via le sous-protocole WebSocket, jamais dans une URL. Les scripts du même site peuvent accéder à ce stockage. Utilisez le terminal uniquement dans un profil de navigateur de confiance.

## État et licence

Le plugin est indiqué comme **expérimental**, car il nécessite un backend ATLAS compatible. Il est distribué sous licence [MIT](https://github.com/rockbaer2007/atlas-terminal-plugin/blob/main/LICENSE).
