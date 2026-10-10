---
title: Blocs et modèles personnalisés
---

# Blocs et modèles personnalisés

Le bouton **Block-/Template-Editor** ouvre un éditeur occupant environ **95 % de la largeur et de la hauteur** de l’écran. Il crée plusieurs blocs dans un paquet, avec aperçu Blockly et sorties HA/Jinja. Les définitions sont déclaratives ; aucun générateur JavaScript importé n’est exécuté.

## Créer un paquet

1. Renseigner ID, version, nom, auteur, licence et description du paquet.
2. Ajouter les blocs puis choisir valeur, condition, action ou déclencheur.
3. Déclarer les champs : texte, nombre, case à cocher ou entité, et les entrées de valeurs typées.
4. Renseigner le modèle de sortie : expression Jinja pour une valeur/condition, structure YAML native pour une action/déclencheur.
5. Vérifier l’aperçu et les diagnostics ; appliquer le paquet.

Les blocs appliqués apparaissent dans **Personnalisés**, avant la recherche. Les IDs techniques sont placés dans un espace de noms propre au paquet. Les noms de champs, variables et IDs ne sont pas traduits. Les libellés des paquets restent dans la langue de leur auteur.

## Copier, télécharger et importer

**JSON prüfen** vérifie le JSON collé. **ZIP einlesen** lit l’archive du même format. Après vérification, **Übernehmen** installe le paquet localement. JSON et ZIP contiennent la même définition ; ils ne doivent pas contenir du code exécutable arbitraire.

Les projets de format 3 incluent les définitions des paquets utilisés pour permettre la restauration sur un autre navigateur. Les paquets installés sont également conservés localement. Les collisions de types et imports invalides sont refusés ; le contrôle préalable évite une installation partielle.

Pour publier, fournir nom, description, auteur, licence, version et image, avec du JSON copiable et des téléchargements JSON/ZIP. Aucune publication automatique depuis l’éditeur. [Catalogue des paquets](./catalog/).

## Limites

Le JSON de définition produit par le [Blockly Developer Tools](https://docs.blockly.com/guides/create-custom-blocks/blockly-developer-tools/) décrit la forme d’un bloc, mais ne suffit pas à produire une automatisation HA. Il faut un modèle de sortie et un schéma de paquet vérifiable. Les générateurs Python, PHP, JavaScript, Lua et Dart du Block Factory ne sont pas les générateurs HA/Jinja de ce projet.

Les menus déroulants personnalisés, champs variable/image, conteneurs d’instructions, mutateurs et entrées dynamiques supplémentaires restent des pistes d’évolution. Les références à des blocs inconnus et les sorties non représentables sont refusées.

Le [paquet capteur et lampe](./catalog/sensor-light) illustre une valeur de capteur, une condition de seuil et une action de luminosité. Tester les résultats et remplacer les entités avant utilisation dans HA.
