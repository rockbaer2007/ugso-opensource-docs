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

1. Augmentez la valeur `version` du manifeste à chaque publication fonctionnelle ou visible.
2. Exécutez `npm run build` et `npm run check`.
3. Vérifiez que le manifeste, le catalogue et le paquet généré indiquent le même identifiant et la même version.
4. Contrôlez les fichiers, les chemins des ressources, les requêtes externes et les capacités déclarées.
5. Activez GitHub Pages pour `main` si le catalogue doit être accessible via Pages. Le fichier brut sera disponible à l'adresse `https://raw.githubusercontent.com/<owner>/<repo>/main/repository.json`.
6. Ajoutez l'URL du catalogue dans l'Administration ATLAS et testez l'aperçu et l'installation du paquet.

Conservez l'identifiant du plugin après sa première publication. Le format de paquet étant textuel, hébergez séparément les gros fichiers binaires et référencez-les par URL.

## État de l'installation

L'installateur générique de dépôts ATLAS stocke actuellement les paquets téléchargés localement. Il n'exécute pas automatiquement le code arbitraire inclus. Une génération réussie confirme donc la structure du paquet, pas une installation exécutable ni un audit de sécurité du code.
