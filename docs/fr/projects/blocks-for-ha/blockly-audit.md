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

## Fonctions d’action et retours conditionnels depuis 0.1.47

Dans **Fonctions**, placer une définition d’action à côté de l’automatisation. Saisir un nom valide sans espaces, ajouter jusqu’à huit paramètres ASCII distincts via l’engrenage et insérer les actions HA dans le corps. Le bloc d’appel apparaît automatiquement ; connecter tous les arguments. Lire les paramètres avec des blocs de variable de **Variables**, par exemple pour un message de journal, une pause ou une affectation.

L’export produit une `sequence` HA native. Chaque appel reçoit ses propres variables internes de paramètre ; les arguments sont évalués lors de l’appel. Les appels imbriqués sont possibles, sans récursion ni corps vide. Les paramètres ne remplacent pas les variables HA de même nom. Les autres affectations restent des affectations HA ordinaires. Les champs de texte Jinja/JSON gardent leur contexte HA normal et ne sont pas réécrits pour les paramètres locaux ; utiliser les blocs de variable. **Stop** arrête toujours toute l’exécution HA.

**Si / renvoyer / sinon** produit une valeur Jinja conditionnelle. Seule la branche sélectionnée est évaluée. Relier ce bloc à la sortie d’une fonction de valeur ou à une autre entrée de valeur. Condition et deux branches sont requises. Ce n’est pas un retour anticipé d’une suite d’actions.

Les projets JSON conservent définitions, paramètres, appels et disposition. Le YAML contient les étapes ou expressions développées ; sa réimportation reconstruit ces étapes, sans recréer les définitions de fonction. [Images des blocs](./blocks#fonctions-depuis-0-1-47).

## Fonctions de valeur

L’éditeur natif Blockly définit une fonction avec valeur de retour. L’engrenage modifie jusqu’à **8 paramètres**. Les noms doivent être des identifiants ASCII valides et distincts. Les appels apparaissent dynamiquement dans Fonctions et leurs entrées suivent les paramètres.

À l’export, l’expression de retour est développée en Jinja, avec liaison locale des paramètres. Pas d’action ni récursion. Définition manquante/ambiguë, retour absent, argument absent ou excès de paramètres empêchent l’export. Un accès à une variable dans une fonction lit le paramètre local s’il existe, sinon la variable HA.

## Sources originales

[Blockly](https://github.com/RaspberryPiFoundation/blockly) · [Blocs standard](https://github.com/RaspberryPiFoundation/blockly/tree/develop/blocks) · [Blockly samples et plugins](https://github.com/raspberrypifoundation/blockly-samples) · [ioBroker JavaScript](https://github.com/ioBroker/ioBroker.javascript) · [Modèles HA](https://www.home-assistant.io/docs/configuration/templating/).

Les extensions d’origine sont liées individuellement dans le [catalogue](./blocks). Les notices de licence restent incluses dans l’application.

:::: details Référence détaillée issue de la documentation allemande

## Alignement Blockly, couleurs et fonctions {#blockly-abgleich-farben-und-funktionen}

### Fonctions d'action et retours conditionnels depuis 0.1.47 {#aktionsfunktionen-und-bedingte-ruckgaben-seit-0-1-47}

Dans la section **Fonctions**, il est possible de définir une fonction d'action indépendamment de l'automatisation. Saisissez un nom valide (sans espaces), ajoutez jusqu'à huit paramètres ASCII distincts via l'icône en forme de roue dentée, et insérez des actions Home Assistant (HA) dans le corps de la fonction. L'appel correspondant apparaît automatiquement dans la même catégorie ; tous les arguments doivent être connectés. Utilisez des blocs issus de la catégorie **Variables** pour lire les paramètres (par exemple, pour un message de journal, une pause ou l'affectation d'une valeur à une variable).

L'exportation génère une structure native HA `sequence`. Chaque appel dispose de ses propres liaisons de paramètres internes ; les arguments sont évalués au moment de l'appel. Les appels imbriqués sont autorisés, contrairement à la récursivité ou aux corps de fonction vides. Les variables HA portant le même nom ne sont pas écrasées par la liaison des paramètres. Les autres affectations de variables au sein du corps de la fonction correspondent à des affectations HA classiques. Les champs de texte libre (Jinja/JSON) restent dans le contexte HA standard et ne sont pas convertis pour utiliser les paramètres locaux ; utilisez plutôt les blocs de variables prévus à cet effet. La commande **Stop** interrompt toujours l'exécution complète du processus HA.

Le bloc de valeur **Si / renvoyer / sinon** fournit la valeur appropriée sous forme d'expression Jinja. Seule la branche sélectionnée est évaluée ; elle peut être connectée à l'entrée de retour d'une fonction de valeur ou à d'autres entrées de valeur. Les deux branches de valeur ainsi que la condition sont obligatoires. Il ne s'agit pas d'un élément `return` prématuré issu d'une séquence d'actions.

Les projets au format JSON conservent les définitions, les paramètres, les appels et la disposition. Le format YAML contient des étapes ou des expressions résolues ; une réimportation depuis le YAML reconstruit ces étapes, mais pas les définitions de fonctions originales. [Illustrations des blocs](/fr/projects/blocks-for-ha/blocks#funktionen-seit-0-1-47). Les tableaux suivants documentent également une comparaison historique de 0.1.15.

État de **0.1.15** au 10 octobre 2026 : **111 types de blocs pris en charge**. Trois calculs de couleur et trois types Blockly originaux destinés aux fonctions de valeur/paramètres ont été ajoutés. Une définition de fonction est autorisée aux côtés de l'automatisation ; en revanche, la présence d'autres blocs non connectés empêche toujours l'exportation.

### Sources et méthodologie {#quellen-und-vorgehen}

La comparaison a porté sur les blocs standard installés dans notre environnement, issus de **Blockly 13.3.0**, sur la [bibliothèque de blocs Blockly](https://github.com/raspberrypifoundation/blockly/tree/4195d60c610bec4b4b186aa22d58cb16beb42dfa/blocks) originale, ainsi que sur la [boîte à outils standard d'ioBroker](https://github.com/ioBroker/ioBroker.javascript/blob/a87561ce0fd9a4ac05631fb35892fb8cb67613d2/src-editor/index.html) et son [pont Blockly](https://github.com/ioBroker/ioBroker.javascript/blob/a87561ce0fd9a4ac05631fb35892fb8cb67613d2/src-editor/src/Components/blockly-plugins/bridge.ts). Les liens renvoient aux commits examinés.

**Le fait qu'un élément soit enregistré, proposé dans le menu ou exportable via notre système sont des choses différentes.** ioBroker charge la bibliothèque standard dans son intégralité. Un bloc qui y est enregistré ne doit pas nécessairement apparaître dans la boîte à outils (toolbox) standard. Par ailleurs, les images ne reflètent pas forcément la boîte à outils actuelle. L'inversion de texte est désormais incluse dans le menu ioBroker ; `atan2` y est absent, mais il est bien enregistré grâce à l'importation de la bibliothèque. Cela ne prouve en rien qu'ioBroker serait incapable d'exécuter `atan2`.

### Toutes les catégories standard {#alle-standardkategorien}

| Catégorie / types originaux | Menu standard ioBroker | UGSo / HA et variantes ouvertes |
| --- | --- | --- |
| Logique : `controls_if`, `controls_ifelse`, `logic_compare`, `logic_operation`, `logic_negate`, `logic_boolean`, `logic_null`, `logic_ternary` | Inclus ; blocs supplémentaires personnalisés pour ET/OU, conditions (cas), plages et valeurs de remplacement | Comparaison, regroupements, structures « si / sinon si / sinon », sélection de valeurs, plages et sélection de cas sont implémentés. Les variantes de forme sont regroupées au sein de blocs dédiés. |
| Boucles : `controls_repeat`, `controls_repeat_ext`, `controls_whileUntil`, `controls_for`, `controls_forEach` | Incluses, principalement la variante basée sur une valeur pour le nombre de répétitions | Implémentations pour : nombre de répétitions, « tant que », « jusqu'à », « pour chaque », ainsi que des limites de comptage entières fixes. Limites de comptage dynamiques ou interrompues ouvertes. |
| Contrôle de boucle : `controls_flow_statements` | break / continue | Instruction break/continue locale ouverte. La fonction « Arrêter l'exécution » met fin à l'ensemble de l'exécution HA et ne constitue pas une alternative équivalente. |
| Mathématiques : `math_number`, `math_arithmetic`, `math_single`, `math_trig`, `math_constant`, `math_number_property`, `math_round`, `math_on_list`, `math_modulo`, `math_constrain`, `math_random_int`, `math_random_float`, `math_change` | Inclus ; décimales fixes supplémentaires | Blocs dédiés au calcul, aux statistiques, à l'arrondi, aux nombres aléatoires et à la modification de variables. À venir : nombres premiers, écart-type, mode (avec gestion de toutes les égalités) et infini. Aucune garantie d'une identité parfaite entre toutes les variantes proposées dans les menus déroulants. |
| Mathématiques : `math_atan2` | Non proposé, bibliothèque enregistrée | Gestion des angles sur quatre quadrants déjà implémentée. |
| Texte : `text`, `text_join`, `text_append`, `text_length`, `text_isEmpty`, `text_indexOf`, `text_charAt`, `text_getSubstring`, `text_changeCase`, `text_trim`, `text_count`, `text_replace`, `text_reverse` | Inclus ; inclut également le texte multiligne, les sauts de ligne, la fonction « contient » et le formatage numérique | Implémenté, y compris l'inversion de texte. La gestion des sous-chaînes est actuellement limitée à un début fixe ; d'autres variantes de positionnement ainsi que le formatage numérique propre à ioBroker restent à venir. |
| Texte : `text_print`, `text_prompt`, `text_prompt_ext` | Non proposé | Sortie via l'action « HA-Log ». Une invite (prompt) du navigateur ne constituerait pas une saisie HA ultérieure ; elle n'est donc pas implémentée en tant que telle. |
| Listes : `lists_create_empty`, `lists_create_with`, `lists_repeat`, `lists_length`, `lists_isEmpty`, `lists_indexOf`, `lists_getIndex`, `lists_setIndex`, `lists_getSublist`, `lists_split`, `lists_sort`, `lists_reverse` | Inclus ; liste vide disponible comme variante | Implémentation réalisée pour : création de liste (0 à 100 éléments), répétition, recherche/lecture/définition/suppression/insertion, sous-liste, division/fusion, tri/inversion. Opérations combinées (lecture et suppression) incluses ; d'autres fonctionnalités (positions finales/aléatoires) restent à prévoir. |
| Variables : `variables_get`, `variables_set`, variantes de type dynamique `variables_get_dynamic`, `variables_set_dynamic` | Catégorie dynamique VARIABLE ; pas de catégorie VARIABLE_DYNAMIC | Implémentation réalisée pour : création, lecture, définition et incrémentation. La sélection de type (via une fenêtre modale dédiée) reste prévue pour une implémentation ultérieure. Un « getter » original est également disponible pour les paramètres de fonction. |
| Fonctions : `procedures_defreturn`, `procedures_callreturn`, `procedures_defnoreturn`, `procedures_callnoreturn`, `procedures_ifreturn` | Catégorie dynamique PROCEDURE | Nouveauté : définition de valeur originale / appel avec paramètres et valeur de retour. Les actions sans valeur de retour sont gérées via l'appel de script HA existant ; pas de fonctions d'action locales ni d'instruction `return` anticipée. |
| Couleur : picker/random/rgb/blend (sélecteur/aléatoire/RVB/mélange) à partir de `field-colour` | Les quatre sont inclus | Désormais, le sélecteur de couleur ainsi que les options aléatoire, RVB et mélange se trouvent dans une catégorie dédiée ; utilisation de générateurs HA spécifiques au lieu de JavaScript. |

Les blocs auxiliaires internes de type « mutator » ne constituent pas des blocs utilisateur autonomes. Les anciennes formes d'alias sont prises en compte via leur fonction correspondante. Dans ioBroker, les catégories supplémentaires — Système, Actions, Sendto, Date/Heure, Conversion, Déclencheurs (Trigger), Temporisations (Timeouts) et Objet — constituent des extensions du moteur de script. Nos équivalents, déjà documentés, se trouvent sous les rubriques [Date/Heure](/fr/projects/blocks-for-ha/time), [Conversion](/fr/projects/blocks-for-ha/conversion), [Temporisations/Objet/Logique](/fr/projects/blocks-for-ha/flow) et [Collections](/fr/projects/blocks-for-ha/collections). Les adaptateurs externes et les plugins tiers installés ultérieurement ne font pas partie de ce comparatif standard. Les fonctions « Sendto/JSONata » ainsi que les minuteurs JavaScript nommés ne sont pas considérés comme des fonctions natives de HA.

### Utilisation des couleurs {#farben-verwenden}

La section **Couleur** propose un sélecteur de couleurs, une option de couleur aléatoire, des pourcentages RVB (RGB) et un mélange de couleurs. Les valeurs en pourcentage sont limitées à la plage 0–100, et le facteur de mélange à la plage 0–1. Les canaux sont convertis sur une échelle de 0 à 255, les valeurs positives fractionnaires étant arrondies à l'entier supérieur. Un mélange de 0 donne la première couleur, un mélange de 1 donne la seconde ; un mélange à 0,5 entre le rouge et le bleu donne `[128, 0, 128]`. Aucune correction gamma n'est appliquée.

Contrairement aux blocs de couleur JavaScript originaux, nos valeurs calculées fournissent des **listes RVB pour HA** (et non des codes hexadécimaux). Connectez le bloc à l'entrée **Lumière → Couleur** ou à une assignation de variable. Un sélecteur de couleur fixe exporte toujours une liste RVB native, tandis que les calculs génèrent un modèle (template) au format `data.rgb_color`. Une variable RGB enregistrée peut également être connectée. Trois canaux numériques, chacun compris entre 0 et 255, sont requis ; veillez à convertir au préalable toute valeur exprimée en format hexadécimal. Des valeurs non valides entraîneront une erreur dans le modèle (template).

Le mélangeur évalue chaque bloc de couleur qui y est directement connecté. Il est conseillé de stocker les entrées numériques ou les modèles (templates) variables — en particulier le facteur de mélange — dans une variable avant de les utiliser ; en effet, les vérifications de type générées automatiquement ou l'utilisation répétée de paramètres de fonction peuvent entraîner plusieurs évaluations des expressions. Le hasard généré n'est pas de nature cryptographique. Les générateurs utilisent les fonctions auxiliaires documentées de HA : [zip](https://www.home-assistant.io/template-functions/zip/), [multiply](https://www.home-assistant.io/template-functions/multiply/) et [add](https://www.home-assistant.io/template-functions/add/). Cette référence de fonctions s'applique à la version actuelle de HA ; veuillez vérifier la disponibilité sur les installations plus anciennes.

### Utilisation des fonctions de valeur {#wertfunktionen-verwenden}

1. Ouvrez la section **Fonctions** et faites glisser un bloc de définition sur l'espace de travail.
2. Nommez-le, par exemple, `doppelt` ; ajoutez un paramètre `x` en cliquant sur l'icône en forme d'engrenage.
3. Connectez l'expression **Variable x × Nombre 2** comme valeur de retour. Les paramètres sont récupérés via des blocs de type « getter » de variable.
4. Rouvrez la catégorie : l'appel `doppelt`, doté de l'entrée `x`, est désormais disponible dynamiquement. Connectez-y le nombre 21 et assignez cet appel, par exemple, à une variable.

Lors de l'exportation, l'expression Jinja correspondante est générée avec l'argument 21 ; il ne s'agit pas d'une fonction JavaScript ou Python. Jusqu'à huit paramètres distincts sont autorisés ; leurs noms doivent être composés de lettres ASCII, de chiffres et de traits de soulignement, et commencer par une lettre ou un trait de soulignement. Les appels imbriqués sont possibles, dans la limite de la profondeur d'expression autorisée. La récursivité, l'absence d'arguments ou de valeurs de retour, les doublons dans les noms, ainsi que la présence d'un corps d'action, empêchent l'exportation. Au sein d'une fonction de valeur, les paramètres ont priorité sur les variables d'automatisation portant le même nom. En dehors, ce sont les variables HA standard et leurs règles de portée qui s'appliquent. Lors de l'exécution, le typage des valeurs de retour ne dépend pas uniquement de la couleur du connecteur Blockly ; dans les conditions, le résultat doit être de type booléen.

Les projets JSON incluent des définitions, des paramètres et des appels. Le format YAML enregistre la signification développée et la rouvre ultérieurement sous forme de modèle (template) ; aucune définition de fonction n'est reconstruite à partir de celle-ci. L'importation via les outils de développement (Developer Tools) — prévue pour des paquets de blocs ou de modèles personnalisés — demeure une tâche distincte dans la feuille de route.

Points vérifiés : cycle complet projet/YAML, limites de couleurs, évaluation Jinja via un environnement isolé (sandbox) immuable incluant des « assistants » (helpers) HA simulés, mutateur de fonction d'origine, menu dynamique et rechargement du navigateur. L'exécution dans une véritable installation Home Assistant reste encore à tester.

[Visuels des blocs et descriptions détaillées](/fr/projects/blocks-for-ha/blocks) · [Couleurs d'origine](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-colour) · [Blocs Blockly personnalisés](https://developers.google.com/blockly/guides/create-custom-blocks/overview)

::::
