---
title: Bibliothèque d’icônes ATLAS
description: Rechercher des jeux d’icônes Home Assistant, les parcourir et copier leurs noms.
---
# Bibliothèque d’icônes ATLAS

La Bibliothèque d’icônes ATLAS est un plugin autonome qui permet de rechercher et de parcourir des jeux d’icônes. Les icônes sont affichées dans une grille de 20 colonnes au maximum ; pour les grands jeux, l’interface ne rend que la partie visible. Cliquez sur une icône pour copier son nom complet, par exemple `mdi:home` ou `atlas:home`.

## Charger des jeux d’icônes

Le paquet du plugin inclut le catalogue MDI. Les collections Icon Studio peuvent être importées depuis l’ordinateur sous forme de fichiers JavaScript ou chargées depuis `/config/www/` avec File Studio. Le scanner parcourt également les sous-dossiers, notamment `/config/www/community/` (accessible dans Home Assistant sous `/local/community/`). Il recherche les jeux d’icônes JavaScript compatibles lorsque le nom du fichier ou d’un dossier contient « icon », puis regroupe ceux qui utilisent le même préfixe. Les collections importées sont enregistrées localement dans le navigateur.

Certains anciens jeux d’icônes Home Assistant exposent leurs noms via `window.customIcons` et peuvent être affichés ainsi. La nouvelle interface `window.customIconsets` ne fournit pas de mécanisme général pour lister tous les noms d’un jeu quelconque. Ces jeux ne peuvent être affichés que s’ils fournissent également une liste de noms lisible.

File Studio doit autoriser l’accès à `/config/www/`. Le plugin n’a pas besoin d’un jeton Home Assistant pour cet accès.

## Installation et code source

Ajoutez ce dépôt externe dans le gestionnaire de plugins ATLAS :

```text
https://raw.githubusercontent.com/rockbaer2007/atlas-icon-library-plugin/main/repository.json
```

ATLAS 0.1.248 ou une version ultérieure est requis, car cette version corrige l’installation des paquets externes.

Consultez le [dépôt GitHub](https://github.com/rockbaer2007/atlas-icon-library-plugin) pour le code source et les instructions de développement.
