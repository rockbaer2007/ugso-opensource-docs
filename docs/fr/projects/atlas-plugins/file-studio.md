---
title: ATLAS File Studio
description: Page française préparée pour ATLAS File Studio dans la documentation UGSo Open Source.
---
# ATLAS File Studio

ATLAS File Studio est un plugin indépendant pour parcourir et modifier les fichiers Home Assistant dans les chemins autorisés. Il comprend un éditeur, la validation YAML, l’aperçu d’images et d’archives, ainsi que des fonctions de transfert et de sauvegarde.

## Dépôt et installation

- GitHub : [rockbaer2007/atlas-file-studio-plugin](https://github.com/rockbaer2007/atlas-file-studio-plugin)
- Page d’installation : [Ajouter ATLAS File Studio](https://rockbaer2007.github.io/atlas-file-studio-plugin/install.html)
- Fichier du dépôt : [repository.json](https://raw.githubusercontent.com/rockbaer2007/atlas-file-studio-plugin/main/repository.json)

## Langue française

Le sélecteur DE/EN/FR permet de choisir le français. Cette version traduit l’en-tête, les principaux contrôles de la barre d’outils et les messages de limite d’envoi. Les dialogues et messages des workflows de fichiers restent à traduire.

## Archives

File Studio permet de prévisualiser les archives ZIP, TAR, TAR.GZ et TGZ, puis d'en extraire un fichier sélectionné sans décompresser l'ensemble de l'archive. L'extraction complète TAR vérifie les chemins et limite la taille de chaque fichier à 64 Mio ainsi que la taille totale à 512 Mio. Les liens symboliques et les types d'entrée non pris en charge sont ignorés. RAR et RAR5 restent une option ultérieure, sous réserve de trouver un outil librement utilisable.

Les fichiers de 64 Mio maximum peuvent être téléversés directement vers un dossier autorisé. Le transfert utilise les données binaires et contourne ainsi la limite de taille des requêtes JSON.

Les fichiers téléversés sont enregistrés dans le dossier actuellement sélectionné.
Après le téléversement, l'arborescence est actualisée sans ouvrir automatiquement le fichier.

Au-delà de cette limite, aucun téléversement n'est lancé. File Studio invite à utiliser l'[extension Samba de Home Assistant](https://github.com/home-assistant/addons/tree/master/samba) pour les fichiers volumineux.

## Statut

- Le chemin de langue existe.
- La navigation et le build peuvent résoudre cette page.
- La traduction détaillée pourra être affinée lors d'une passe de documentation ultérieure.

## Indication des accès

L'espace File Studio affiche les autorisations de fichiers actives dans un encadré compact, avec une typographie normale et légèrement plus petite. Chaque chemin autorisé possède une couleur distincte, ce qui facilite la lecture de chemins tels que `/config/www`, `/addons` et `/parent-of-config`.
