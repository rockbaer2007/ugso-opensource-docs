---
title: ATLAS File Studio
description: Page française préparée pour ATLAS File Studio dans la documentation UGSo Open Source.
---
# ATLAS File Studio

Cette page française a été ajoutée afin que la documentation Open Source dispose d'un chemin de langue complet. La traduction détaillée sera encore enrichie.

La page anglaise correspondante est actuellement la référence de structure : [`en/projects/atlas-plugins/file-studio.md`](/en/projects/atlas-plugins/file-studio).

## Archives

File Studio permet de prévisualiser les archives ZIP, TAR, TAR.GZ et TGZ, puis d'en extraire un fichier sélectionné sans décompresser l'ensemble de l'archive. L'extraction complète TAR vérifie les chemins et limite la taille de chaque fichier à 64 Mio ainsi que la taille totale à 512 Mio. Les liens symboliques et les types d'entrée non pris en charge sont ignorés. RAR et RAR5 restent une option ultérieure, sous réserve de trouver un outil librement utilisable.

Les fichiers de 64 Mio maximum peuvent être téléversés directement vers un dossier autorisé. Le transfert utilise les données binaires et contourne ainsi la limite de taille des requêtes JSON.

## Statut

- Le chemin de langue existe.
- La navigation et le build peuvent résoudre cette page.
- La traduction détaillée pourra être affinée lors d'une passe de documentation ultérieure.

## Indication des accès

L'espace File Studio affiche les autorisations de fichiers actives dans un encadré compact, avec une typographie normale et légèrement plus petite. Chaque chemin autorisé possède une couleur distincte, ce qui facilite la lecture de chemins tels que `/config/www`, `/addons` et `/parent-of-config`.
