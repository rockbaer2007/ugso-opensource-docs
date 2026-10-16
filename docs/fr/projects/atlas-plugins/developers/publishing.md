---
title: Construire, valider et publier
description: Préparer et valider les paquets de plugins et catalogues ATLAS.
---
# Construire, valider et publier

Le [modèle de plugin](../plugin-template) automatise les étapes répétitives du dépôt GitHub d'un plugin.

## Générer le paquet et le catalogue

```sh
npm run build
npm run check
```

La génération crée un paquet installable à partir du manifeste et synchronise l'entrée correspondante dans `repository.json`. Les contrôles vérifient notamment les identifiants, le chemin du paquet et les métadonnées du paquet généré. GitHub Actions lance ces commandes à chaque push et pull request.

## Étapes de publication

Respecter les [règles de version et de compatibilité](./compatibility), notamment les sauvegardes, limites de migration et procédures de restauration.

1. Augmentez la valeur `version` du manifeste à chaque publication fonctionnelle ou visible.
2. Exécutez `npm run build` et `npm run check`.
3. Vérifiez que le manifeste, le catalogue et le paquet généré indiquent le même identifiant et la même version.
4. Contrôlez les fichiers, les chemins des ressources, les requêtes externes et les capacités déclarées.
5. Publier le catalogue par push vers `main` : `https://raw.githubusercontent.com/<owner>/<repo>/main/repository.json`. GitHub Pages n’est pas nécessaire pour ce fichier brut ; l’activer éventuellement pour `install.html`.
6. Ajoutez l'URL du catalogue dans l'Administration ATLAS et testez l'aperçu et l'installation du paquet.

Conservez l'identifiant du plugin après sa première publication. Le format de paquet étant textuel, hébergez séparément les gros fichiers binaires et référencez-les par URL.

## État de l'installation

Le serveur App installe les paquets validés, depuis un dépôt ou un import, dans le stockage persistant et sert les fichiers web sous `/plugin-assets/<slug>/`. Leur JavaScript s’exécute dans le navigateur à l’ouverture ; les modules Node ou hooks Runtime ne sont pas enregistrés automatiquement. Ce n’est pas une sandbox : vérifier paquet et code avant ouverture. La génération seule ne remplace pas les contrôles d’exécution et de sécurité.
