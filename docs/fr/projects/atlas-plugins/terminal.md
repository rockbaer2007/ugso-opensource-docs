---
title: ATLAS Terminal
description: Terminal web ATLAS avec couleurs ANSI, SSH facultatif, thèmes Oh My Posh et police Nerd Font servie par le serveur.
---
# ATLAS Terminal

ATLAS Terminal est un dépôt de plugin indépendant qui fournit un terminal web authentifié. Il propose les couleurs ANSI, une taille de police réglable, des thèmes Oh My Posh sélectionnables et une connexion SSH facultative vers une cible configurée côté serveur.

## Dépôt et installation

- GitHub : [rockbaer2007/atlas-terminal-plugin](https://github.com/rockbaer2007/atlas-terminal-plugin)
- Page d'installation : [Ajouter ATLAS Terminal](https://rockbaer2007.github.io/atlas-terminal-plugin/install.html)
- Manifeste du dépôt : [repository.json](https://raw.githubusercontent.com/rockbaer2007/atlas-terminal-plugin/main/repository.json)
- Version du plugin : `0.1.5`

Dans l'Administration ATLAS, ouvrez **Plugins → Ajouter un dépôt**, choisissez **Plugin** et saisissez l'URL du manifeste. Vérifiez le dépôt, puis installez le paquet du plugin. L'hôte ATLAS doit fournir un backend Terminal compatible.

## Fonctionnalités

- terminal web avec couleurs ANSI
- taille de police réglable localement
- thèmes Oh My Posh sélectionnables pour les sessions Bash locales
- la police Nerd Font Meslo LGM est servie par Home Assistant ; aucune installation locale n'est nécessaire sur les clients
- cible SSH facultative avec hôte, utilisateur, clé et fichier `known_hosts` configurés côté serveur
- vérification de la clé d'hôte maintenue ; le navigateur ne peut pas choisir une cible SSH arbitraire
- interface versionnée séparément dans le dépôt du plugin

## Installer la Nerd Font

Placez `MesloLGMNerdFontMono-Regular.ttf` et `MesloLGMNerdFontMono-Bold.ttf` dans `/config/www/fonts/` ou directement dans `/config/www/`. Home Assistant les sert sous `/local/fonts/` ou `/local/`, et le terminal charge les fichiers de police depuis ces chemins.

## Prérequis et sécurité

Le dépôt contient l'interface du plugin, mais **ce n'est ni un serveur SSH autonome ni un module complémentaire Home Assistant**. L'hôte ATLAS fournit le shell ainsi que les fonctions Supervisor et WebSocket. La déclaration de compatibilité indique ATLAS `>=0.2.0-alpha.79` et Home Assistant `>=2026.8`. Le chargement de la police Meslo depuis Home Assistant nécessite l'App/Add-on `0.1.214` ou une version plus récente.

Le terminal est désactivé par défaut. Activez-le uniquement après avoir configuré sur l'hôte ATLAS un jeton d'accès aléatoire et robuste d'au moins 32 caractères sûrs pour les URL. Le shell local s'exécute avec les droits du processus ATLAS. En mode App/Add-on Home Assistant, les permissions Supervisor peuvent également autoriser des commandes `ha` d'administration. Considérez donc l'accès au terminal comme un accès administratif.

Le jeton reste dans le stockage local du navigateur et est transmis lors de la connexion via le sous-protocole WebSocket, jamais dans une URL. Les scripts du même site peuvent accéder à ce stockage. Utilisez le terminal uniquement dans un profil de navigateur de confiance.

## État et licence

Le plugin est indiqué comme **expérimental**, car il nécessite un backend ATLAS compatible. Il est distribué sous licence [MIT](https://github.com/rockbaer2007/atlas-terminal-plugin/blob/main/LICENSE).
