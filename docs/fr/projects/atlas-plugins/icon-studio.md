---
title: ATLAS Icon Studio
description: Gérer, importer, supprimer et enregistrer des jeux d’icônes Home Assistant avec ATLAS Icon Studio.
---
# ATLAS Icon Studio

ATLAS Icon Studio est un plugin installé séparément pour créer et gérer des jeux d’icônes Home Assistant avec le préfixe `atlas:`. La version 0.1.15 prend en charge les grandes collections sans limite fixe du nombre d’icônes ; la liste affiche 24 éléments à la fois.

## Gestion des icônes

Sélectionnez une icône dans la collection et utilisez **Supprimer l’icône**. Icon Studio sélectionne ensuite automatiquement la prochaine icône supprimable. Vous pouvez ainsi en supprimer plusieurs à la suite sans devoir en sélectionner une après chaque suppression. L’icône de référence `atlas:home` est protégée et ne peut pas être supprimée. La collection conserve toujours au moins une icône.

La recherche, la navigation au clavier et l’export portent sur toute la collection, même si seule une petite partie est affichée. Les collections peuvent être sauvegardées et restaurées au format JSON ; les conflits de noms peuvent être remplacés, ignorés ou renommés automatiquement.

## Home Assistant

Les jeux d’icônes peuvent être exportés localement sous `atlas-iconset.js` ou lus directement depuis `/config/www/atlas-iconset.js` avec File Studio. Lors de l’enregistrement, vous pouvez remplacer le fichier existant ; File Studio crée d’abord une sauvegarde. Icon Studio peut aussi créer un nouveau fichier numéroté et afficher son chemin de ressource `/local/...` à enregistrer dans Home Assistant. L’accès direct nécessite que `/config/www` soit autorisé dans File Studio.

Consultez le [README du plugin](https://github.com/rockbaer2007/atlas-icon-studio-plugin#readme) pour les détails d’installation, de formats et de chemins.
