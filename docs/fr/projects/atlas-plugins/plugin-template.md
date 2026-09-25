---
title: Modèle de plugin ATLAS
description: Créer un plugin ATLAS à partir du modèle GitHub officiel.
---
# Modèle de plugin ATLAS

Le [modèle officiel ATLAS Plugin Template sur GitHub](https://github.com/rockbaer2007/atlas-plugin-template) fournit un dépôt prêt à l'emploi pour un plugin ATLAS. Utilisez **Use this template** sur GitHub pour créer votre propre dépôt.

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
6. Activez GitHub Pages pour la branche `main`. Le catalogue sera alors disponible à l'adresse `https://raw.githubusercontent.com/<owner>/<repo>/main/repository.json`.
7. Ajoutez l'URL du catalogue dans l'Administration ATLAS et installez le plugin pour le tester.

## Contenu du modèle

Le modèle comprend un petit plugin d'exemple, son manifeste, un catalogue, une page d'installation, un générateur de paquet, des validations et un workflow GitHub Actions. Ce workflow lance la génération et les contrôles à chaque push et pull request.

Augmentez la version du plugin pour chaque publication, puis exécutez `npm run build`. Conservez l'identifiant du plugin après sa publication. Vérifiez les autorisations et les capacités déclarées avant la mise en ligne.

## Limites actuelles de l'installation

L'installateur générique de dépôts stocke actuellement les fichiers du paquet localement. Il n'exécute pas automatiquement le code arbitraire téléchargé depuis un dépôt. Le format du paquet stocke les fichiers du plugin sous forme de texte ; les fichiers binaires volumineux doivent être hébergés séparément et référencés par URL.

Consultez [Format du dépôt](./repository-format) pour les détails du catalogue et du paquet. Dépôt du modèle : [rockbaer2007/atlas-plugin-template](https://github.com/rockbaer2007/atlas-plugin-template).
