---
title: Modèle de plugin ATLAS
description: Créer un plugin ATLAS à partir du modèle GitHub officiel.
---
# Modèle de plugin ATLAS

Le [modèle officiel ATLAS Plugin Template sur GitHub](https://github.com/rockbaer2007/atlas-plugin-template) fournit un dépôt prêt à l'emploi pour un plugin ATLAS. Utilisez **Use this template** sur GitHub pour créer votre propre dépôt.

## Générateur de plugins dans l'Administration

L’Administration ATLAS propose un générateur pour identifiant, nom, description, version, chemin d’entrée et capacités. Choisir une icône MDI du catalogue local ou un PNG personnel jusqu’à 512 KiB ; le paquet inclut image et mentions de licence nécessaires. Couleurs et transparence du PNG sont conservées. Il génère une base HTML/CSS/JavaScript modifiable, un paquet, `repository.json` et un `README.md` localisé, également téléchargeable séparément. Vérifier contenus et chemins avant publication. Aucun dépôt GitHub ni publication automatique n’est créé. Les paquets importés pris en charge sont installés sur le serveur App après contrôle de compatibilité et servis sous `/plugin-assets/<slug>/`. Leur interface s’exécute à l’ouverture dans le navigateur ; les hooks Runtime ne sont pas enregistrés automatiquement. Garder `entry` et chemins du paquet cohérents.

Les plugins qui proposent leur propre choix de langue reprennent la préférence ATLAS enregistrée à leur ouverture. Le paramètre `language` de l'URL du plugin est prioritaire. Si un plugin ne prend pas en charge la langue choisie, il utilise sa langue de repli configurée.

## Démarrage rapide

1. Ouvrez le dépôt du modèle, puis choisissez **Use this template** → **Create a new repository**.
2. Clonez votre nouveau dépôt et modifiez `plugins/atlas-plugin/atlas-plugin.json`. Définissez un identifiant unique, un nom, une version, une description et uniquement les capacités réellement nécessaires.
3. Remplacez l'application d'exemple dans `plugins/atlas-plugin/`, puis remplacez `icon.svg`, `logo.svg` et `preview.svg` par les ressources de votre plugin.
4. Générez et validez le paquet localement :

   ```sh
   npm run build
   npm run check
   ```

5. Adaptez `repository.json` et `install.html` à votre dépôt. Le générateur reprend l'identifiant, le nom, la version, les descriptions et les chemins des ressources du manifeste afin de synchroniser le catalogue.
6. Après le push, le catalogue est accessible à `https://raw.githubusercontent.com/<owner>/<repo>/main/repository.json` sans GitHub Pages. Activer Pages séparément pour publier `install.html` si souhaité.
7. Ajoutez l'URL du catalogue dans l'Administration ATLAS et installez le plugin pour le tester.

## Contenu du modèle

Le modèle comprend un petit plugin d'exemple, son manifeste, un catalogue, une page d'installation, un générateur de paquet, des validations et un workflow GitHub Actions. Ce workflow lance la génération et les contrôles à chaque push et pull request.

Augmentez la version du plugin pour chaque publication, puis exécutez `npm run build`. Conservez l'identifiant du plugin après sa publication. Vérifiez les autorisations et les capacités déclarées avant la mise en ligne.

## Limites actuelles de l'installation

Le serveur App installe les paquets validés, depuis un dépôt ou un import, dans le stockage persistant et sert les fichiers web sous `/plugin-assets/<slug>/`. Leur JavaScript s’exécute dans le navigateur à l’ouverture ; les modules Node ou hooks Runtime ne sont pas enregistrés automatiquement. Ce n’est pas une sandbox : vérifier paquet et code avant ouverture. Les fichiers contiennent du texte ou des ressources Base64 explicitement marquées ; maximum 300 fichiers et 20 MB par paquet. Héberger séparément les gros fichiers binaires.

Consultez [Format du dépôt](./repository-format) pour les détails du catalogue et du paquet. Dépôt du modèle : [rockbaer2007/atlas-plugin-template](https://github.com/rockbaer2007/atlas-plugin-template).
