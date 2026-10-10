---
title: Comparaison Blockly, couleurs et fonctions
---

# Comparaison Blockly, couleurs et fonctions

Les exemples ioBroker servent de référence d’usage ; les blocs produisent des structures **HA/YAML et Jinja**. Le JavaScript ioBroker n’est pas transféré comme moteur d’exécution.

## Couverture et adaptations

| Groupe | Adaptation |
| --- | --- |
| Logique | Comparaisons, ET/OU/NON, booléens, null, choix de valeur, branches, cas, intervalle et valeur de secours. |
| Boucles | Répétition, tant que/jusqu’à, pour chaque élément, compteur et boucle avec variable nommée. |
| Mathématiques | Calculs, propriétés, constantes, trigonométrie et atan2, arrondis, statistiques, modulo, limitation, aléatoire. |
| Textes | Multiligne, sauts de ligne, assemblage, recherche, extraction, casse, suppression d’espaces, comptage, remplacement et inversion. |
| Listes | Création, répétition, lecture, copie, modification immuable, découpage/assemblage, tri et inversion. |
| Couleurs | Sélecteur, RGB en pourcentages, aléatoire, mélange et action de lampe. |
| Variables et fonctions | Variables HA pendant l’exécution ; fonctions de valeur Blockly développées en Jinja. |
| HA | Déclencheurs, entités, scripts, assistants, journal, mises à jour, actions génériques et modèles. |

Opérations ajoutées au-delà des captures ioBroker : notamment atan2, inversion du texte, attente avec expiration et fonctions de valeur avec paramètres. Le catalogue recense les **111 types** ; les variantes de menus déroulants ne sont pas des types supplémentaires.

Des adaptations ne sont pas disponibles comme équivalents directs : `break`/`continue` ciblés, fonctions contenant des actions ou récursion, invites navigateur à l’exécution HA, intervalles ioBroker nommés, JSONata sans moteur HA. Un `stop` termine tout le scénario et ne doit pas être décrit comme une simple rupture de boucle.

## Couleurs

RGB : pourcentages limités à 0–100, convertis en canaux 0–255. Rouge 100, vert 50, bleu 0 donne `[255,128,0]`. Mélange : part 0 pour la première couleur et 1 pour la seconde ; rouge/bleu à 0,5 donne `[128,0,128]`. Mélange linéaire sans correction gamma.

La couleur aléatoire crée trois canaux à chaque évaluation. L’action de lampe produit `light.turn_on` avec la couleur et une luminosité en pourcentage. La lampe doit prendre en charge ces options.

## Fonctions

L’éditeur natif Blockly définit une fonction avec valeur de retour. L’engrenage modifie jusqu’à **8 paramètres**. Les noms doivent être des identifiants ASCII valides et distincts. Les appels apparaissent dynamiquement dans Fonctions et leurs entrées suivent les paramètres.

À l’export, l’expression de retour est développée en Jinja, avec liaison locale des paramètres. Pas d’action ni récursion. Définition manquante/ambiguë, retour absent, argument absent ou excès de paramètres empêchent l’export. Un accès à une variable dans une fonction lit le paramètre local s’il existe, sinon la variable HA.

## Sources originales

[Blockly](https://github.com/RaspberryPiFoundation/blockly) · [Blocs standard](https://github.com/RaspberryPiFoundation/blockly/tree/develop/blocks) · [Blockly samples et plugins](https://github.com/raspberrypifoundation/blockly-samples) · [ioBroker JavaScript](https://github.com/ioBroker/ioBroker.javascript) · [Modèles HA](https://www.home-assistant.io/docs/configuration/templating/).

Les extensions d’origine sont liées individuellement dans le [catalogue](./blocks). Les notices de licence restent incluses dans l’application.
