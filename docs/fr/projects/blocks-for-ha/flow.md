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

Un nouvel objet est un dictionnaire local. L’engrenage ajoute jusqu’à 100 clés. On peut lire un attribut, vérifier sa présence et obtenir la liste des clés. Clé absente : `null` ; objet invalide : erreur de modèle HA.

Modifier/supprimer un attribut affecte un **nouveau dictionnaire** à la variable. Initialiser la variable comme objet auparavant. Ces opérations ne modifient ni une autre variable ni les attributs d’une entité HA. Les listes sont aussi des valeurs locales ; les changements produisent de nouvelles listes compatibles avec le bac à sable Jinja immuable.

## Logique et choix

Comparaison, ET/OU, NON, booléens, null et choix de valeur sont disponibles. Les groupes ET/OU/NON peuvent être étendus avec l’engrenage. Utilisés comme conditions, ils génèrent les groupes natifs HA ; utilisés comme valeurs, ils génèrent des expressions Jinja.

**Si / sinon si / sinon** crée des branches d’actions. **Selon la valeur** compare des cas, exécute seulement le premier cas correspondant puis utilise la branche par défaut si nécessaire. Il génère `choose`, sans passage automatique aux cas suivants de JavaScript.

**Limiter une valeur entre deux bornes** vérifie un intervalle numérique, avec bornes strictes ou inclusives. **Valeur de secours** distingue null/non défini et vide/faux/0. Le premier mode conserve 0, faux et texte vide ; le second remplace aussi listes et objets vides selon les règles Python/Jinja.

Le choix conditionnel de **valeur** ne contient pas d’actions. Une condition seule ne déclenche aucune automatisation.

[Scripts HA](https://www.home-assistant.io/docs/scripts/) · [Sources ioBroker](https://github.com/ioBroker/ioBroker.javascript) · [Blockly](https://github.com/RaspberryPiFoundation/blockly).

Depuis **0.1.39** : unités de durée combinées, listes for_each littérales, options HA, attente de déclencheur, timer.finished, branches parallèles et groupes d’actions. [Guide HA avancé et Jinja](./advanced).

:::: details Référence détaillée issue de la documentation allemande

## Temporisations, objets, logique et boucles {#timeouts-objekt-logik-und-schleifen}

Cette page décrit les 18 ajouts apportés par 0.1.13 (qui comptait alors 68 types de blocs). On en dénombre actuellement **105**, incluant des blocs supplémentaires dédiés aux mathématiques, au texte, aux listes et aux boucles, issus de 0.1.14 [voir ici](/fr/projects/blocks-for-ha/collections).

Depuis **0.1.13** , 18 nouveaux blocs viennent enrichir l'éditeur, portant le total à **68 types de blocs**. [Images et fonctionnalités de tous les blocs](/fr/projects/blocks-for-ha/blocks#ablaufe-objekte-und-listen-seit-0-1-13). Ils sont basés sur les blocs réels de type [Timeout](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_timeout.ts), [Objet](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_object.ts), [Logique](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_logic.ts) et [Switch](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_switch.ts) de l'adaptateur JavaScript d'ioBroker. Le tableau suivant explique les similitudes et les limites ; le code JavaScript d'ioBroker n'est pas importé.

### Timeouts (Temporisations) {#timeouts}

| ioBroker | Blocs UGSo pour HA | Différence |
| --- | --- | --- |
| Pause, unité ms/sec/min | **Pause** (ms/secondes/minutes/heures) avec valeur dynamique | Utilise la fonction native `delay` de HA. L'exécution en cours est mise en attente ; le navigateur n'est pas bloqué. |
| Exécuter un timeout dans…, durée fixe/variable | **Pause**, suivie d'actions | HA exécute les étapes suivantes les unes après les autres. Il n'y a pas de callback indépendant ni de gestionnaire (handle) de timeout nommé. |
| Arrêter le timeout | **Arrêter le script HA** (pour un script lancé séparément) ; **Arrêter cette exécution** (pour l'exécution en cours) | L'arrêt met fin à toute l'exécution en cours. Il n'est pas possible de supprimer sélectivement un timeout spécifique (comme dans ioBroker). |
| Temporisation avec gestionnaire (handle) | Aucun bloc de gestionnaire | Utilisez les scripts HA ou les « helpers » (assistants) de type minuteur via le système/les actions. Un « helper » de type minuteur ne déclenche pas de callback intégré. |
| Exécuter un intervalle toutes les… | **Répéter tant que/jusqu'à** avec une **Pause** dans le corps de la boucle | Répétition séquentielle : la durée de l'action augmentée de la pause détermine l'intervalle. Pas de `setInterval` ni de cycles (ticks) parallèles se chevauchant. |
| Arrêt de l'exécution cyclique | Modifier la condition de boucle ou arrêter un script HA distinct. | **Arrêter cette exécution** interrompt également les boucles englobantes ; cela ne correspond pas à un simple `break` local. |
| Intervalle en tant que « handle » | Pas de bloc de gestion (handle block). | Les scripts lancés séparément peuvent être arrêtés via `script.turn_off`. |
| Fonctionnalités supplémentaires dans UGSo | **Attendre jusqu'à**, répétition limitée, « Pour chaque entrée ». | Contrôle natif de HA, incluant des options de dépassement de délai (timeout) et la possibilité de considérer l'interruption de l'exécution comme une erreur. |

**Attendre jusqu'à** (*Warte bis*) utilise `wait_template` de HA avec un délai d'attente (timeout) obligatoire. Si l'option « continuer en cas de dépassement de délai » n'est pas activée, l'exécution s'arrête dès l'expiration du délai. Si elle est activée, les actions suivantes sont exécutées même si la condition n'est pas remplie. Conditions basées sur des entités : les modèles (templates) temporels purs (utilisant `now()`) ne sont pas réévalués en continu durant l'attente (`wait_template`). HA fournit ensuite `wait.completed`, utilisable dans le bloc de modèle. [Attentes et répétitions dans HA](https://www.home-assistant.io/docs/scripts/).

**Tant que** effectue la vérification avant chaque itération ; **jusqu'à** effectue la vérification après et exécute le corps de la boucle au moins une fois. Une pause dans le corps de la boucle évite une boucle infinie trop serrée. Les durées en millisecondes constituent des délais minimaux et non une garantie de temps réel. Un redémarrage de HA interrompt les délais/attentes en cours ; pour une planification persistante, utilisez des stratégies distinctes basées sur des minuteurs ou des déclencheurs. [Assistant de minuterie](https://www.home-assistant.io/integrations/timer/).

Durée constante : 0 à 86 400 secondes, avec unité explicite. Nombre de répétitions constant : 1 à 10 000 itérations complètes. Les variables et modèles (templates) intégrés doivent fournir des valeurs numériques valides lors de l'exécution ; la validation et la gestion des erreurs éventuelles sont effectuées par HA. Les limites indiquées pour les constantes sont des contraintes de l'éditeur et ne constituent pas des limites garanties lors de l'exécution des modèles.

### Objet {#objekt}

| ioBroker | Bloc UGSo | Comportement |
| --- | --- | --- |
| Nouvel objet avec icône d'engrenage | **Nouvel objet** avec icône d'engrenage | 0 à 100 attributs, clés uniques nommées librement, valeurs quelconques (y compris des objets ou listes imbriqués). |
| Définir l'attribut de l'objet sur une valeur | **Définir l'attribut dans la variable sur** | Assigne une nouvelle valeur à un attribut au sein d'une variable objet préalablement définie. Les autres copies de la variable restent inchangées. |
| Supprimer l'attribut | **Supprimer l'attribut de la variable** | Crée un nouveau dictionnaire dépourvu de la clé spécifiée ; si la clé est absente, le contenu reste inchangé. |
| L'objet possède l'attribut | **L'objet possède l'attribut** | Test booléen vérifiant la présence d'une clé spécifique dans le dictionnaire. |
| Attributs de l'objet | **Attributs de l'objet** | Liste des clés utilisables avec la boucle « pour chaque entrée ». |
| Lecture d'attribut (équivalent à « System » dans ioBroker) | **Attribut d'objet** | Accès par clé plutôt que par notation pointée (moins sûre) ; si la clé est absente, le résultat est `null`. Des noms tels que `keys` ou `items` sont également pris en charge. |

Ces objets correspondent à des valeurs locales au sein d'une exécution d'automatisation. Ils ne créent pas d'entités, ne modifient pas les attributs d'entités HA et ne correspondent pas aux définitions de points de données ioBroker. Le « setter » (assignateur) utilise un sélecteur de variable afin de garantir une cible unique pour la nouvelle assignation. La variable doit être préalablement définie sur **Nouvel objet**, une valeur de modèle de dictionnaire (dictionary template) ou **JSON vers objet**. L'utilisation d'un autre type provoquera une erreur de modèle (template) dans HA.

Le [bac à sable (sandbox) Jinja immuable](https://jinja.palletsprojects.com/en/stable/sandbox/) ne permet pas de modification directe via `update` ou `pop`. Par conséquent, UGSo crée des copies des dictionnaires et procède à une nouvelle assignation. Aucune mutation d'objet JavaScript ni accès direct au système HA n'est effectué.

### Logique et Blockly original {#logik-und-original-blockly}

Les définitions logiques Blockly originales (https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/logic.ts) incluent les structures « si / sinon si / sinon », des variantes fixes « si / sinon », des comparaisons, les opérateurs ET/OU/NON, les booléens, la valeur nulle (`null`) et la sélection conditionnelle de valeurs. Ces fonctionnalités de base sont déjà présentes dans UGSo : **« Si »** (dans la section Actions), les valeurs (dans la section **Logique**), ainsi que les groupes extensibles ET/OU/NON (dans les sections Conditions et Logique). Les formes de sélection et de connexion proviennent de la bibliothèque Blockly originale ; le code HA-YAML/Jinja est généré par UGSo.

| Extension ioBroker | UGSo | Sémantique |
| --- | --- | --- |
| ET/OU avec icône d'engrenage | Groupe extensible existant (également disponible sous « Logique ») | 1 à 100 entrées booléennes ; engrenage pour réorganiser les éléments. |
| « le cas est » / « dans le cas de » / « faire » | **« Le cas est »** | 1 à 100 cas (avec engrenage), bloc « sinon » optionnel. La première correspondance est retenue ; pas de comportement de type « fall-through » (exécution en cascade) comme en JavaScript. |
| min ≤ valeur ≤ max | **Comparaison de plage** | Chaque borne peut être définie indépendamment comme stricte ou inclusive. Aucune conversion automatique de texte en nombre ; utiliser l'option **« En nombre »** pour les valeurs issues de capteurs ou de modèles (templates). |
| « si vide… alors… » | **Valeur de remplacement** (avec choix du mode) | La valeur par défaut (`null` / non définie) est remplacée par 0, « faux » ou une chaîne vide. Les options « vide/faux/0 » s'appliquent également aux listes et dictionnaires vides. |

Pour la valeur de remplacement, ioBroker utilise l'opérateur OU de JavaScript : dans ce contexte, les tableaux ou objets vides sont évalués comme « vrais ». À l'inverse, Jinja/Python les considère comme « faux ». Le mode « null » supplémentaire évite que des nombres ou des valeurs booléennes valides ne soient remplacés par inadvertance. Les états de capteur non disponibles, tels que « unknown » (inconnu) ou « unavailable » (indisponible), sont considérés comme du texte ; il ne s'agit pas de valeurs « null » et ils ne sont donc pas remplacés automatiquement.

Les comparaisons de cas utilisent les règles d'égalité de HA/Jinja ; les valeurs booléennes et les nombres peuvent se comporter différemment par rapport à l'instruction « switch » en JavaScript. L'expression de test est évaluée pour chaque branche HA examinée. Si tous les cas doivent comparer un même instantané (« snapshot »), il est conseillé de stocker au préalable la valeur changeante dans une variable, puis d'utiliser cette variable comme valeur de comparaison.

### Boucles et listes {#schleifen-und-listen}

Les blocs **Répéter un nombre de fois**, **tant que/jusqu'à** et **Pour chaque élément** ont été repris depuis les blocs de boucle originaux de [Blockly](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/loops.ts). Les blocs **Créer une liste**, **Longueur de la liste** et **La liste est vide** s'inspirent des blocs de liste [originaux](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/lists.ts). Ces fonctionnalités sont également présentes dans d'autres catégories ioBroker, en dehors des trois menus affichés ici ; elles ne sont donc pas présentées comme une lacune spécifique à ioBroker.

La création de listes prend en charge de 0 à 100 entrées (au choix), configurables via l'icône en forme de roue dentée ou les boutons +/-. Chaque entrée attend une liste ; la valeur actuelle et l'index (commençant à 1) sont accessibles dans le bloc modèle (template) sous les variables `repeat.item` et `repeat.index` de Home Assistant. Les vérifications de longueur ou de vacuité s'appliquent à de véritables listes, et non à du texte ou des dictionnaires. Jinja peut générer des erreurs d'exécution si le type fourni en entrée est différent.

```yaml
actions:
  - variables:
      daten: '{{ {"attribute1": "alt"} }}'
  - variables:
      daten: '{{ dict((daten if daten is mapping else none), **{"attribute1": "neu"}) }}'
  - repeat:
      count: 3
      sequence:
        - delay:
            milliseconds: 1000
        - action: system_log.write
          data:
            message: '{{ repeat.index }}'
            level: info
```

### Enregistrement et fonctionnalités disponibles {#speicherung-und-offene-funktionen}

Le fichier JSON du projet conserve la forme des blocs, leur ordre et les noms des attributs. Le format YAML permet de charger directement les pauses, les attentes (*waits*), les arrêts et les répétitions sous forme de blocs dédiés. Les structures de sélection (choix/cas) sont chargées en tant que blocs `choose` existants ; les valeurs complexes (objets, listes, logique) sont chargées sous forme de modèles (*templates*) génériques. Le comportement YAML est préservé, bien que la forme originale ne puisse pas être reconstruite de manière univoque. Depuis 0.1.39, les mappages de durée combinés, les véritables boucles `for_each` et certains champs d'options supplémentaires de Home Assistant sont conservés tels quels. [Séquences avancées et Jinja](/fr/projects/blocks-for-ha/advanced).

Les déclencheurs périodiques, l'événement `timer.finished` et les branches parallèles sont désormais pris en charge. Les minuteurs nommés sont gérés via les actions natives `timer` de Home Assistant ; la sémantique locale de type `break`/`continue` reste prévue pour une implémentation ultérieure. Les boucles de comptage à nombre fixe d'itérations et le traitement des listes ont été ajoutés depuis [0.1.14](/fr/projects/blocks-for-ha/collections). L'option **Arrêter cette exécution** n'est explicitement pas traduite par une instruction `break` ou `continue`. Les blocs spécifiques aux états ou aux attributs d'entités demeurent des tâches distinctes. L'ensemble de base original de Blockly n'inclut pas, par défaut, le moteur de temporisation (*timeout*) d'ioBroker ni les blocs d'objets ioBroker correspondants ; il s'agit d'extensions propres à l'adaptateur.

Vérifié : cycles complets (modèle/YAML/projet), détection des erreurs de saisie, bac à sable Jinja immuable avec valeurs d'exécution, ainsi que navigation via le navigateur, fonction de mutation et annulation (Undo). Un test sur une instance HA réelle reste à effectuer.

::::
