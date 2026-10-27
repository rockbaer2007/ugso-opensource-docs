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

:::: details Référence détaillée issue de la documentation allemande

## Mathématiques, texte, listes et boucles {#mathematik-text-listen-und-schleifen}

**Depuis 0.1.14 :** 37 types de blocs supplémentaires, pour un total de **105**. [Tous les blocs sont illustrés par des captures d'écran réelles de l'éditeur](/fr/projects/blocks-for-ha/blocks). Les deux images de texte issues du modèle appartiennent à la même catégorie et ne sont comptabilisées qu'une seule fois. Le système génère ses propres sorties HA-YAML/Jinja ; le code JavaScript propre à ioBroker n'est pas exécuté.

### Comparaison avec les versions originales {#abgleich-mit-den-originalen}

Références : ensemble original des blocs Blockly pour les [boucles](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/loops.ts), les [mathématiques](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/math.ts), le [texte](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/text.ts) et les [listes](https://github.com/RaspberryPiFoundation/blockly/blob/main/packages/blockly/blocks/lists.ts). Les ajouts spécifiques à ioBroker concernant les [décimales](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_number.ts) et le [texte](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_text.ts) ont également été examinés. La sortie finale repose sur les [fonctions de modèle (template) de HA](https://www.home-assistant.io/template-functions/) et les [actions de script de HA](https://www.home-assistant.io/docs/scripts/).

| Domaine / Original | Implémentation UGSo | Différences / variantes en suspens |
| --- | --- | --- |
| Répéter tant que / jusqu'à | Blocs natifs HA existants | « Tant que » vérifie avant, « jusqu'à » vérifie après. |
| Compter de/à/pas | Nouveau bloc de boucle de comptage | Bornes entières fixes, valeur de pas, fin incluse (sur la grille), incrémentation/décrémentation automatique, max. 10 000 valeurs. Les bornes dynamiques ou non entières ne sont pas prises en charge. |
| Pour chaque valeur d'une liste | Avec variable nommée supplémentaire | Avant chaque exécution du corps de la boucle, la variable est définie à partir de `repeat.item`. |
| break / continue | En suspens | L'instruction « Stop » de HA interrompt l'ensemble de l'exécution. Une implémentation locale correcte nécessiterait un modèle de flux de contrôle supplémentaire ainsi que des tests sur les boucles imbriquées. |
| Incrémenter un nombre ou une variable | Déjà disponible | Les variables doivent être initialisées au préalable ; l'incrémentation nécessite un nombre. |
| Arithmétique, fonctions simples, trigonométrie, constantes | Nouvelle catégorie « Mathématiques » | Racine, valeur absolue, négation, ln/log10, puissances ; angles en degrés. L'infini n'est pas pris en charge. |
| Propriétés des nombres | Pair, impair, entier, positif, négatif, divisible | La vérification des nombres premiers reste à implémenter. |
| Arrondi / décimales (ioBroker) | Bloc unique, arrondi standard/supérieur/inférieur, 0 à 10 décimales | Utilisation de l'arrondi HA/Jinja plutôt que `Math.round` de JavaScript. |
| Opérations mathématiques sur des listes | Somme, min/max, moyenne, médiane, élément aléatoire | Le mode statistique (Blockly) — sous forme de liste de toutes les valeurs les plus fréquentes — ainsi que l'écart-type restent à implémenter ; la fonction `statistical_mode` de HA ne correspond pas exactement à cette fonctionnalité. |
| Modulo, limitation (clamp), aléatoire | Nouveaux blocs de valeur | Pour le modulo avec des nombres négatifs, le comportement de Jinja est appliqué. La génération de nombres entiers aléatoires inclut les bornes ; elle offre un maximum de 10 000 possibilités. Les nombres décimaux aléatoires utilisent un pas de 0,00001. |
| atan2 | Également repris du Blockly original | Non visible dans les illustrations mathématiques fournies ; ceci n'est pas considéré comme une lacune d'ioBroker. |
| Texte sur une ou plusieurs lignes | Bloc de texte existant | Champ multiligne original. |
| Saut de ligne, concaténation, ajout | Nouveaux blocs de texte | LF/CRLF/CR ; concaténation via l'icône « engrenage » (+/-) ; l'ajout affecte une nouvelle variable texte. |
| Longueur/vide/contient/rechercher/caractère/sous-chaîne | Nouveaux blocs de texte | Indexation à partir de 1 ; résultat 0 si l'élément est introuvable. Les plages incluent le début et la fin ; la sous-chaîne peut être définie sans borne de fin. |
| Majuscules/minuscules/casse titre, trim, compter, remplacer, inverser | Nouveaux blocs de texte | Utilisation de littéraux (et non d'expressions régulières) ; règles Unicode/Python. L'inversion de texte fait également partie du périmètre Blockly original. |
| print / prompt | Action de journalisation (log) disponible ; prompt non implémenté | Une boîte de dialogue dans le navigateur ne constituerait pas une saisie adaptée à l'automatisation HA (Home Assistant) exécutée ultérieurement. |
| Liste vide / Liste avec éléments | Bloc de liste existant (0 à 100 entrées) | L'icône « engrenage » (+/-) permet de modifier les entrées. |
| Répétition de liste, longueur/vide, index, lecture, sous-liste | Blocs de liste existants et nouveaux | Lecture depuis le début/la fin, premier/dernier élément, ou élément aléatoire. La sous-liste inclut la borne de fin. |
| Modifier / insérer / supprimer dans une liste | Nouveaux blocs d'action | Crée une nouvelle liste dans la variable sélectionnée ; n'affecte pas les autres variables. « Lire et supprimer » en tant que bloc combiné ; la modification depuis la fin et la suppression aléatoire restent à prévoir. |
| Scinder/fusionner, trier, inverser | Nouveaux blocs de liste | Numérique / Texte / Texte (insensible à la casse) ; la liste originale est préservée. |

### Utilisation et valeurs d'exécution {#bedienung-und-laufzeitwerte}

Le menu, le panneau contextuel (flyout) clair et les blocs colorés restent bien distincts ; la fonction **Rechercher** se situe tout à la fin. Les éléments mathématiques sont bleu-violet, le texte est vert foncé, les listes sont violettes et les boucles sont vertes. Des valeurs peuvent être insérées dans des variables, des comparaisons, des modèles (templates) et des pauses d'exécution. Les seuils numériques fixes servant de déclencheurs n'acceptent toujours que des blocs numériques, et non des modèles calculés.

Le bloc de concaténation de texte dispose de 0 à 100 entrées. La création de variables s'effectue toujours dans la catégorie « Variables » ; les opérations de modification de texte ou de liste utilisent ces variables. Avant toute opération d'ajout ou de modification, la variable doit être du type approprié. Si nécessaire, une chaîne de caractères représentant un état (lue depuis HA) doit être explicitement convertie en nombre à l'aide du bloc de conversion. L'utilisation de types invalides ou d'index comportant des décimales entraîne une erreur de modèle (template) plutôt qu'une conversion silencieuse.

L'index **1** désigne le premier élément. En comptant depuis la fin, l'index 1 désigne le dernier élément. Lors d'une lecture, un index situé hors limites renvoie un texte vide ou une valeur nulle ; dans le cas d'une modification de liste, celle-ci reste inchangée. Une insertion à la position « longueur + 1 » équivaut à un ajout à la fin. Pour les sous-ensembles (plages), si la valeur de début est supérieure à celle de fin, ou si la valeur de début est inférieure à 1, le résultat est une valeur vide. Une limite de fin dépassant la longueur totale est tronquée.

Exemple : compter avec `i` de 1 à 5 par pas de 2, et enregistrer dans le corps de la boucle une valeur de modèle (template) via `i` :

```yaml
actions:
  - repeat:
      for_each: '{{ range(1, 6, 2) | list }}'
      sequence:
        - variables:
            i: '{{ repeat.item }}'
        - action: system_log.write
          data:
            level: info
            message: '{{ i }}'
```

Cela donne : 1, 3, 5. Dans le cas de boucles imbriquées, il est conseillé d'utiliser des noms de variables différents ; `repeat.item` fait toujours référence à l'itération la plus interne. Stocker au préalable dans une variable les expressions aléatoires ou dépendantes du temps qui sont appelées à plusieurs reprises, si la même valeur est requise à différents endroits : les modèles (templates) imbriqués peuvent en effet évaluer les entrées à plusieurs reprises.

### Différences par rapport à JavaScript et stockage {#unterschiede-zu-javascript-und-speicherung}

- Avec 0 décimale, 2,5 devient 2 et 3,5 devient 4 ; la fonction `Math.round` de JavaScript se comporte différemment. L'arrondi à l'entier supérieur ou inférieur utilise respectivement `ceil` et `floor`.
- Modulo négatif : −9 modulo 2 donne 1. Les angles sont convertis entre les degrés et les radians (dans le contexte HA).
- Les opérations sur les chaînes de caractères utilisent des points de code Unicode. En JavaScript, un émoji peut être représenté par deux unités UTF-16 ; les caractères combinés (graphèmes) correspondent toujours à plusieurs points de code. La mise en majuscules (titre) et le rognage (*trim*) suivent le comportement de Python/Jinja.
- Une chaîne de recherche vide est explicitement traitée comme 0 (pour le comptage) ou comme une chaîne inchangée (pour le remplacement). Les correspondances ne se chevauchent pas. La recherche est littérale et sensible à la casse.
- Liste vide : la somme est 0 ; les autres agrégats mathématiques renvoient `null`, tout comme l'extraction d'un élément aléatoire. L'agrégation ou le tri numérique nécessitent des nombres réels ; les booléens ou les chaînes de caractères ne sont pas acceptés. L'égalité en Python — qui peut considérer `1` et `vrai` comme équivalents — diffère de l'égalité par référence utilisée en JavaScript.
- Les modifications apportées aux listes créent des copies via des découpages (*slices*) et l'assignation à de nouvelles variables HA. Aucune mutation de type `list.append` ou `list.pop` n'est possible dans l'environnement HA (sandbox) immuable.

Le fichier JSON du projet conserve les formes des blocs, les champs, les menus déroulants, l'ordre des éléments et les entrées liées. L'importation YAML préserve la sémantique : les expressions complexes sont traitées comme des modèles (*templates*) génériques, et les boucles de comptage sont converties en boucles natives de type « pour chaque élément » (*for-each*) avec assignation de variable. Le YAML ne contient pas suffisamment d'informations pour permettre une reconstruction univoque des formes Blockly originales.

Vérifié : les 37 nouveaux types de blocs ont été testés via JSON/YAML, en incluant les cas limites ; utilisation d'un environnement « bac à sable » (sandbox) Jinja immuable avec les fonctions mathématiques d'assistance de Home Assistant (HA) ; intégration des catégories et du bouton « texte plus » dans le navigateur ; génération de l'application et de la documentation ; prévisualisation Docker. L'exécution au sein d'une instance Home Assistant réelle reste à effectuer.

::::
