---
title: Format du dépôt
description: Format des dépôts ATLAS, modèle de plugin et génération des paquets installables.
---
# Format du dépôt

ATLAS utilise son propre format pour les dépôts de plugins installables. Il est distinct des dépôts d'extensions Home Assistant et s'identifie avec des métadonnées ATLAS.

## Références

- Dépôt de démonstration : [atlas-plugin-repository-demo](https://github.com/rockbaer2007/atlas-plugin-repository-demo)
- Fichier catalogue : [repository.json](https://raw.githubusercontent.com/rockbaer2007/atlas-plugin-repository-demo/main/repository.json)
- Modèle GitHub officiel : [atlas-plugin-template](https://github.com/rockbaer2007/atlas-plugin-template)

Le modèle inclut un plugin fonctionnel, son manifeste, un catalogue, des visuels,
un générateur de paquet et des contrôles de validation. Après modification du
manifeste, `npm run build` régénère le paquet installable et synchronise le
catalogue ; `npm run check` vérifie leur cohérence. GitHub Actions exécute ces
contrôles à chaque modification.

L'installateur générique actuel stocke les fichiers du paquet localement. Il
n'exécute pas le code arbitraire téléchargé depuis un dépôt de plugins.

Les chemins relatifs du catalogue sont résolus par rapport à `repository.json`.
Le champ `package` désigne le paquet installable ; `manifest` reste disponible
pour l'aperçu, le diagnostic et la vérification manuelle.
