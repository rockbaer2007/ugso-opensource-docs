---
title: Mathématiques, textes, listes et boucles
---

# Mathématiques, textes, listes et boucles

Les fonctions correspondent aux capacités utiles de Blockly et ioBroker, adaptées à **HA/Jinja**. Les données ne sont pas exécutées comme code JavaScript. [Catalogue illustré de chaque type](./blocks).

## Mathématiques

Addition, soustraction, multiplication, division, puissance, racine carrée, valeur absolue, négation, logarithmes et exponentielles sont disponibles. Pas de conversion automatique des textes ou booléens. Les erreurs mathématiques restent des erreurs de modèle.

Les fonctions trigonométriques utilisent des **degrés** ; leurs inverses et `atan2` retournent des degrés. Constantes : π, e, nombre d’or, √2 et √½. Les propriétés testent pair, impair, entier, positif, négatif ou divisible par un diviseur non nul.

L’arrondi propose ordinaire, supérieur et inférieur à **0–10 décimales**. L’arrondi Jinja ordinaire suit la règle d’égalité vers le pair. Le modulo des nombres négatifs suit le signe du diviseur, pouvant différer de JavaScript. La limitation trie d’abord les bornes inversées.

Une liste numérique peut fournir somme, minimum, maximum, moyenne ou médiane ; l’élément aléatoire accepte tout type. Somme vide : 0 ; autres résultats vides : null. Entier aléatoire : bornes inclusives et au plus 10000 possibilités. Fraction aléatoire : 0 inclus à 1 exclu, pas de 0,00001, nouvelle valeur à chaque évaluation. Aucun usage cryptographique.

## Textes

Texte simple ou multiligne, saut LF/CRLF/CR, assemblage extensible, ajout à une variable initialisée, longueur, vide, recherche, caractère, sous-texte, casse, suppression des espaces, comptage, remplacement et inversion.

- Positions à partir de **1** ; recherche absente : **0**.
- Longueur et découpage suivent les **points de code Unicode**, pas les unités UTF-16 ou graphèmes composés.
- Recherche, comptage et remplacement sont littéraux et sensibles à la casse, sans regex. Comptage sans chevauchement.
- Recherche vide : comptage 0, remplacement inchangé.
- Sous-texte : bornes inclusives. Bornes invalides/inversées : texte vide.
- Suppression d’espaces : début, fin ou deux côtés, tabulations et sauts de ligne inclus.

## Listes

Liste vide/extensible, répétition d’un élément, longueur, vide, recherche de première/dernière occurrence, accès depuis le début/la fin ou aléatoire, remplacement/insertion/suppression, sous-liste, découpage/assemblage de texte, tri et inversion.

Toutes les positions commencent à **1**. Accès hors limites ou liste vide : null. Une modification affecte une nouvelle liste à la variable ; l’original n’est pas muté. Indice invalide : liste inchangée. Insertion autorisée jusqu’à longueur+1. Sous-liste inclusive ; bornes invalides/inversées : liste vide.

Séparateur vide lors du découpage : caractères Unicode. Tri numérique : nombres requis. Tri textuel : conversion en texte, avec ou sans distinction de casse. L’égalité est celle de HA/Python, pas l’identité de référence JavaScript.

## Boucles avec variables

Le compteur utilise des bornes entières fixes, fin incluse lorsqu’elle est atteinte par le pas. Le sens est automatique ; pas absolu >0, au plus **10000 tours**. Il génère `repeat.for_each` et affecte la variable avant chaque corps.

Pour chaque valeur d’une liste, une variable nommée reçoit `repeat.item` avant le corps. Éviter la réutilisation de cette variable dans une boucle imbriquée. Les blocs de rupture et continuation ciblées de Blockly nécessitent une autre représentation que `stop` HA ; ils ne sont pas proposés comme équivalents directs.

[Sources Blockly](https://github.com/RaspberryPiFoundation/blockly/tree/develop/blocks) · [Référence ioBroker](https://github.com/ioBroker/ioBroker.javascript) · [Modèles HA](https://www.home-assistant.io/docs/configuration/templating/).
