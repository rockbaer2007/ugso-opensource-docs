---
title: Délais, objets et logique
---

# Délais, objets et logique

Les blocs génèrent des **actions natives HA** et des expressions Jinja. Aucun temporisateur JavaScript n’exécute les actions dans le navigateur. [Tous les blocs avec images](./blocks).

## Délais et boucles

| Fonction | Exécution HA |
| --- | --- |
| Pause | `delay`, durée numérique en ms, secondes, minutes ou heures. Les ms ne garantissent pas un temps réel précis. |
| Attendre une condition | `wait_template`, durée maximale et case continuer après expiration. Sans coche, l’expiration termine cette exécution. |
| Arrêter | `stop`, raison et indicateur d’erreur. Arrête l’exécution complète, boucles englobantes comprises. |
| Répéter N fois | `repeat.count`, entier positif. Indice `repeat.index`, à partir de 1. |
| Tant que | Condition vérifiée avant chaque tour. Peut n’exécuter aucun tour. |
| Jusqu’à | Condition vérifiée après chaque tour. Au moins un tour. |
| Pour chaque élément | `repeat.for_each`, élément `repeat.item`, indice `repeat.index`. Entrée liste obligatoire. |

Ajouter une pause si une boucle risque de tourner continuellement. Une condition d’attente doit dépendre d’entités : l’heure seule ne réévalue pas constamment `wait_template`. Les temporisateurs et intervalles nommés ioBroker ne sont pas équivalents à ces actions ; un arrêt de boucle complète n’est pas un `break` ou `continue` ciblé.

## Objets et listes

Un nouvel objet est un dictionnaire local. L’engrenage ou +/− ajoute jusqu’à 100 clés. On peut lire un attribut, vérifier sa présence et obtenir la liste des clés. Clé absente : `null` ; objet invalide : erreur de modèle HA.

Modifier/supprimer un attribut affecte un **nouveau dictionnaire** à la variable. Initialiser la variable comme objet auparavant. Ces opérations ne modifient ni une autre variable ni les attributs d’une entité HA. Les listes sont aussi des valeurs locales ; les changements produisent de nouvelles listes compatibles avec le bac à sable Jinja immuable.

## Logique et choix

Comparaison, ET/OU, NON, booléens, null et choix de valeur sont disponibles. Les groupes ET/OU/NON peuvent être étendus avec +/− ou l’engrenage. Utilisés comme conditions, ils génèrent les groupes natifs HA ; utilisés comme valeurs, ils génèrent des expressions Jinja.

**Si / sinon si / sinon** crée des branches d’actions. **Selon la valeur** compare des cas, exécute seulement le premier cas correspondant puis utilise la branche par défaut si nécessaire. Il génère `choose`, sans passage automatique aux cas suivants de JavaScript.

**Limiter une valeur entre deux bornes** vérifie un intervalle numérique, avec bornes strictes ou inclusives. **Valeur de secours** distingue null/non défini et vide/faux/0. Le premier mode conserve 0, faux et texte vide ; le second remplace aussi listes et objets vides selon les règles Python/Jinja.

Le choix conditionnel de **valeur** ne contient pas d’actions. Une condition seule ne déclenche aucune automatisation.

[Scripts HA](https://www.home-assistant.io/docs/scripts/) · [Sources ioBroker](https://github.com/ioBroker/ioBroker.javascript) · [Blockly](https://github.com/RaspberryPiFoundation/blockly).
