---
title: Catalogue des blocs
description: Tous les blocs UGSo avec images françaises et fonctions.
---

# Catalogue des blocs

**0.1.35 · 118 types**. Les images montrent les vrais blocs Blockly en français. Les variantes des menus déroulants ne sont pas des types supplémentaires. Les IDs techniques restent identiques en DE/EN/FR. Les textes et entités d’exemple gardent leurs valeurs d’origine.

Déclencheurs orange, conditions violettes, valeurs vertes, actions bleues avec le thème UGSo Standard. Les autres palettes adaptent les couleurs. [Usage et import](./) · [Paquets personnalisés](./custom-blocks).

## Système

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Journal … message …**<br><code>ugso_log_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_log_action.png" alt="Journal … message …" style="max-width:280px;max-height:180px"> | Écrit dans le journal système HA à l’exécution. La configuration HA peut filtrer info/debug. |
| **Script HA … …**<br><code>ugso_script_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_script_action.png" alt="Script HA … …" style="max-width:280px;max-height:180px"> | Appeler et attendre reprend après la fin du script. Transmettre les paramètres via l’action HA générique. |
| **Actualiser l’entité …**<br><code>ugso_update_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_update_action.png" alt="Actualiser l’entité …" style="max-width:280px;max-height:180px"> | Demande l’actualisation de l’entité dans HA. Prise en charge selon l’intégration ; ne définit pas un état. |
| **Assistant … … …**<br><code>ugso_helper_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_helper_action.png" alt="Assistant … … …" style="max-width:280px;max-height:180px"> | Actions adaptées au type d’assistant. Rechercher une entité ou saisir son ID. |

## Valeurs

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Nombre**<br><code>ugso_number</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_number.png" alt="Nombre" style="max-width:280px;max-height:180px"> | Nombre fixe éditable. Utilisable pour valeurs et seuils de déclencheurs numériques. |
| **Pourcentage**<br><code>ugso_percent</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_percent.png" alt="Pourcentage" style="max-width:280px;max-height:180px"> | Curseur de 0 à 100, valeur numérique en pourcentage. |
| **Texte …**<br><code>ugso_text</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text.png" alt="Texte …" style="max-width:280px;max-height:180px"> | Texte multiligne éditable ; contenu conservé exactement sans traduction automatique. |
| **Couleur …**<br><code>ugso_colour</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_colour.png" alt="Couleur …" style="max-width:280px;max-height:180px"> | Sélectionner une couleur ; conversion en liste de canaux RGB pour HA. |

## Date et heure

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Date du jour … …**<br><code>ugso_date_condition</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_date_condition.png" alt="Date du jour … …" style="max-width:280px;max-height:180px"> | Compare la date du jour, année comprise, dans le fuseau HA. Ne déclenche pas une automatisation. |
| **L’heure actuelle est … …**<br><code>ugso_time_compare</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_time_compare.png" alt="L’heure actuelle est … …" style="max-width:280px;max-height:180px"> | Comparer l’heure locale HA ; intervalle avec début inclus et fin exclue, même à travers minuit. Condition, pas déclencheur. |
| **L’heure actuelle … est … …**<br><code>ugso_time_compare_input</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_time_compare_input.png" alt="L’heure actuelle … est … …" style="max-width:280px;max-height:180px"> | Comparer une heure raccordée. Décocher l’heure actuelle affiche une entrée de date à comparer. |
| **Heure actuelle comme date**<br><code>ugso_time_now</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_time_now.png" alt="Heure actuelle comme date" style="max-width:280px;max-height:180px"> | Date HA avec fuseau horaire, pour les calculs ou le formatage. |
| **Date calculée …**<br><code>ugso_time_boundary</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_time_boundary.png" alt="Date calculée …" style="max-width:280px;max-height:180px"> | Début du jour, du jour suivant, de la semaine (lundi), du mois ou de l’année dans le fuseau HA. |
| **Prochain événement solaire … décalage (minutes) …**<br><code>ugso_time_sun</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_time_sun.png" alt="Prochain événement solaire … décalage (minutes) …" style="max-width:280px;max-height:180px"> | Prochain événement de sun.sun en heure locale HA, éventuellement demain. Une valeur absente provoque une erreur de modèle. |
| **Calculer la date … … … …**<br><code>ugso_time_shift</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_time_shift.png" alt="Calculer la date … … … …" style="max-width:280px;max-height:180px"> | Ajouter ou soustraire une durée à une date ; millisecondes, secondes, minutes, heures ou jours. Nombre fini requis. |
| **Date … au format …**<br><code>ugso_time_format</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_time_format.png" alt="Date … au format …" style="max-width:280px;max-height:180px"> | Texte formaté ou temps Unix pour l’affichage ou les variables. Utiliser la date pour les calculs. |

## Conversion

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Convertir en nombre …**<br><code>ugso_convert_number</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_convert_number.png" alt="Convertir en nombre …" style="max-width:280px;max-height:180px"> | HA float() : nombre décimal complet, sans préfixe parseFloat ni valeur de secours implicite. Pour comparaisons, variables et calculs de dates, pas pour un seuil fixe de déclencheur. |
| **Convertir en booléen …**<br><code>ugso_convert_boolean</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_convert_boolean.png" alt="Convertir en booléen …" style="max-width:280px;max-height:180px"> | HA bool() : true/false, on/off, yes/no, 1/0. Une valeur non reconnue provoque une erreur de modèle. |
| **Convertir en texte …**<br><code>ugso_convert_string</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_convert_string.png" alt="Convertir en texte …" style="max-width:280px;max-height:180px"> | Représentation textuelle Jinja, sans sérialisation JSON. Les booléens deviennent True/False. |
| **Type de …**<br><code>ugso_convert_type</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_convert_type.png" alt="Type de …" style="max-width:280px;max-height:180px"> | HA typeof() : noms de types Python, str, int, float, bool, dict, list ou NoneType. HA 2023.4 ou ultérieur. |
| **Convertir en date/heure … entrée …**<br><code>ugso_convert_datetime</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_convert_datetime.png" alt="Convertir en date/heure … entrée …" style="max-width:280px;max-height:180px"> | Préférer un texte ISO avec Z ou décalage de fuseau explicite. Choisir l’unité Unix. Résultat en heure locale HA ; une entrée invalide provoque une erreur de modèle. |
| **Date/heure … vers …**<br><code>ugso_convert_date_format</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_convert_date_format.png" alt="Date/heure … vers …" style="max-width:280px;max-height:180px"> | Le format détermine le raccord : date, nombre à l’exécution ou texte. Format personnalisé Python strftime. |
| **Durée … entrée … vers …**<br><code>ugso_convert_duration</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_convert_duration.png" alt="Durée … entrée … vers …" style="max-width:280px;max-height:180px"> | Durée numérique, en millisecondes par défaut comme dans ioBroker. Fractions de seconde tronquées. Heures/minutes peuvent dépasser 24/60 ; signe conservé. |
| **JSON vers valeur …**<br><code>ugso_convert_from_json</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_convert_from_json.png" alt="JSON vers valeur …" style="max-width:280px;max-height:180px"> | HA from_json : objet, liste ou valeur simple. JSON invalide : erreur, sans objet vide de secours. |
| **Valeur vers JSON … indenter …**<br><code>ugso_convert_to_json</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_convert_to_json.png" alt="Valeur vers JSON … indenter …" style="max-width:280px;max-height:180px"> | HA to_json avec indentation facultative. Convertir les dates en texte ISO ou nombre Unix auparavant. |

## Délais

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Pause … …**<br><code>ugso_pause</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_pause.png" alt="Pause … …" style="max-width:280px;max-height:180px"> | Délai natif HA. L’entrée doit fournir un nombre, vérifié à l’exécution. Les millisecondes ne garantissent pas une précision temps réel. |
| **Attendre que … pendant au plus … … continuer après expiration …**<br><code>ugso_wait</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_wait.png" alt="Attendre que … pendant au plus … … continuer après expiration …" style="max-width:280px;max-height:180px"> | HA wait_template avec expiration. Sans coche : arrêt de cette exécution à l’expiration. Utiliser des conditions liées aux entités ; l’heure seule ne rafraîchit pas continuellement le modèle. |
| **Arrêter cette exécution … comme erreur …**<br><code>ugso_stop</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_stop.png" alt="Arrêter cette exécution … comme erreur …" style="max-width:280px;max-height:180px"> | Arrête l’exécution HA actuelle, y compris les boucles englobantes. Ne supprime pas un temporisateur nommé ioBroker. |

## Objet

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Nouvel objet …**<br><code>ugso_object_new</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_object_new.png" alt="Nouvel objet …" style="max-width:280px;max-height:180px"> | Dictionnaire local à attributs nommés. Ajouter des entrées avec l’engrenage ou +/−. Ce n’est ni une entité HA ni un point de données ioBroker. |
| **Attribut … de l’objet …**<br><code>ugso_object_get</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_object_get.png" alt="Attribut … de l’objet …" style="max-width:280px;max-height:180px"> | Lit une clé du dictionnaire, y compris keys/items. Clé absente : null ; type d’objet invalide : erreur de modèle HA. |
| **L’objet … possède l’attribut …**<br><code>ugso_object_has</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_object_has.png" alt="L’objet … possède l’attribut …" style="max-width:280px;max-height:180px"> | Vérifier la présence d’une clé dans un dictionnaire, y compris une clé dont la valeur est null. |
| **Attributs de l’objet …**<br><code>ugso_object_keys</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_object_keys.png" alt="Attributs de l’objet …" style="max-width:280px;max-height:180px"> | Liste des clés du dictionnaire, pour parcourir les éléments ou produire du JSON. |
| **Définir l’attribut … de la variable … à …**<br><code>ugso_object_set</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_object_set.png" alt="Définir l’attribut … de la variable … à …" style="max-width:280px;max-height:180px"> | Affecte à cette variable HA un nouveau dictionnaire avec la clé modifiée. Initialiser la variable comme objet. Les autres variables et attributs HA restent inchangés. |
| **Supprimer l’attribut … de la variable …**<br><code>ugso_object_remove</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_object_remove.png" alt="Supprimer l’attribut … de la variable …" style="max-width:280px;max-height:180px"> | Affecte un nouveau dictionnaire sans cette clé. Une clé absente laisse le contenu inchangé. La variable doit déjà contenir un objet. |

## Déclencheurs

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Quand … atteint l’état …**<br><code>ugso_state_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_state_trigger.png" alt="Quand … atteint l’état …" style="max-width:280px;max-height:180px"> | Réagit à un changement d’état. |
| **Quand … franchit … …**<br><code>ugso_numeric_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_numeric_trigger.png" alt="Quand … franchit … …" style="max-width:280px;max-height:180px"> | Démarre au franchissement d’un seuil, pas continuellement tant que la condition reste vraie. |
| **Quand il est …**<br><code>ugso_time_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_time_trigger.png" alt="Quand il est …" style="max-width:280px;max-height:180px"> | Déclencher l’automatisation à une heure fixe au format HH:mm:ss. |
| **Au …**<br><code>ugso_sun_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_sun_trigger.png" alt="Au …" style="max-width:280px;max-height:180px"> | Déclencher au lever ou au coucher du soleil, selon Home Assistant. |
| **Quand Home Assistant démarre**<br><code>ugso_start_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_start_trigger.png" alt="Quand Home Assistant démarre" style="max-width:280px;max-height:180px"> | Déclencher au démarrage de Home Assistant. |

## Conditions

| Bloc | Image | Fonction |
| --- | --- | --- |
| **… est …**<br><code>ugso_state_condition</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_state_condition.png" alt="… est …" style="max-width:280px;max-height:180px"> | Vérifier si l’entité possède l’état indiqué. Les valeurs on/off restent les IDs HA. |
| **… est … …**<br><code>ugso_numeric_condition</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_numeric_condition.png" alt="… est … …" style="max-width:280px;max-height:180px"> | Comparer l’état numérique d’une entité avec une borne fixe, au-dessus ou en dessous. |
| **Groupe de conditions**<br><code>ugso_logic_condition</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_logic_condition.png" alt="Groupe de conditions" style="max-width:280px;max-height:180px"> | Groupe ET, OU ou NON extensible jusqu’à 100 conditions. Engrenage ou +/− pour modifier les entrées. |

## Actions

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Allumer / éteindre / basculer**<br><code>ugso_switch_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_switch_action.png" alt="Allumer / éteindre / basculer" style="max-width:280px;max-height:180px"> | Action du domaine de l’entité choisie. Vérifier sa disponibilité dans HA. |
| **Action HA … cible … données (JSON) …**<br><code>ugso_service_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_service_action.png" alt="Action HA … cible … données (JSON) …" style="max-width:280px;max-height:180px"> | Cible facultative. Données sous forme d’objet JSON ; l’intégration doit être présente dans HA. |
| **Attendre … secondes**<br><code>ugso_delay_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_delay_action.png" alt="Attendre … secondes" style="max-width:280px;max-height:180px"> | Attendre un nombre de secondes via une action delay native HA. |
| **Si … faire …**<br><code>ugso_if_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_if_action.png" alt="Si … faire …" style="max-width:280px;max-height:180px"> | Branche if native HA avec actions, sinon si et sinon. Engrenage et +/− pour étendre les branches. |
| **Lampe … couleur … luminosité … %**<br><code>ugso_colour_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_colour_action.png" alt="Lampe … couleur … luminosité … %" style="max-width:280px;max-height:180px"> | Action light.turn_on avec couleur RGB et brightness_pct. Lampe compatible et luminosité 0–100 requises. |

## Logique

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Comparaison**<br><code>ugso_compare</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_compare.png" alt="Comparaison" style="max-width:280px;max-height:180px"> | Compare deux valeurs HA. Nombres et textes ont des types différents ; convertir explicitement les valeurs de capteurs dans les modèles. |
| **ET / OU compact**<br><code>ugso_binary_logic</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_binary_logic.png" alt="ET / OU compact" style="max-width:280px;max-height:180px"> | Combiner deux booléens avec ET/OU ; groupe natif HA ou expression Jinja selon l’usage. |
| **NON …**<br><code>ugso_not</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_not.png" alt="NON …" style="max-width:280px;max-height:180px"> | Nier une condition : groupe not natif HA ou expression not Jinja lorsqu’utilisé comme valeur. |
| **Vrai / faux**<br><code>ugso_boolean</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_boolean.png" alt="Vrai / faux" style="max-width:280px;max-height:180px"> | Constante vrai/faux, pour conditions et variables. L’export conserve le type booléen YAML. |
| **aucune valeur (null)**<br><code>ugso_null</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_null.png" alt="aucune valeur (null)" style="max-width:280px;max-height:180px"> | YAML null ou Jinja none, ni zéro ni faux. |
| **Si … alors valeur … sinon valeur …**<br><code>ugso_ternary</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ternary.png" alt="Si … alors valeur … sinon valeur …" style="max-width:280px;max-height:180px"> | Renvoie une valeur, pas une suite d’actions. HA évalue l’expression Jinja pour variables, messages de journal ou comparaisons. |
| **Intervalle numérique**<br><code>ugso_logic_range</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_logic_range.png" alt="Intervalle numérique" style="max-width:280px;max-height:180px"> | Tester un nombre entre deux bornes, avec comparaisons strictes ou inclusives indépendantes. |
| **Si … est … utiliser …**<br><code>ugso_logic_default</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_logic_default.png" alt="Si … est … utiliser …" style="max-width:280px;max-height:180px"> | Le mode null conserve 0, false et le texte vide. Le mode vide remplace aussi les valeurs fausses, listes/objets vides inclus. Règles Python/Jinja différentes de JavaScript. |
| **Selon la valeur … …**<br><code>ugso_case</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_case.png" alt="Selon la valeur … …" style="max-width:280px;max-height:180px"> | Exécute uniquement la première branche correspondante, sinon la branche par défaut. HA choose natif, sans passage aux cas suivants de JavaScript. |

## Boucles

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Répéter … fois faire …**<br><code>ugso_repeat</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_repeat.png" alt="Répéter … fois faire …" style="max-width:280px;max-height:180px"> | HA repeat.count natif. repeat.index commence à 1. Le nombre de répétitions doit être un entier positif. |
| **Répéter … … faire …**<br><code>ugso_repeat_while</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_repeat_while.png" alt="Répéter … … faire …" style="max-width:280px;max-height:180px"> | Tant que vérifie avant chaque tour ; jusqu’à vérifie après et exécute au moins un tour. Ajouter une pause pour éviter une boucle infinie intensive. Aucun intervalle en arrière-plan. |
| **Pour chaque élément de … faire …**<br><code>ugso_foreach</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_foreach.png" alt="Pour chaque élément de … faire …" style="max-width:280px;max-height:180px"> | HA repeat.for_each. Élément : &#123;&#123; repeat.item &#125;&#125;, indice : &#123;&#123; repeat.index &#125;&#125;. L’entrée doit être une liste. |
| **Compter … de … à … par pas de … faire …**<br><code>ugso_for_range</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_for_range.png" alt="Compter … de … à … par pas de … faire …" style="max-width:280px;max-height:180px"> | Bornes entières fixes, fin inclusive si atteinte par les pas. Sens automatique, pas absolu &gt;0, au plus 10000 tours. HA repeat.for_each affecte une variable à chaque tour. |
| **Pour chaque valeur … de la liste … faire …**<br><code>ugso_foreach_variable</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_foreach_variable.png" alt="Pour chaque valeur … de la liste … faire …" style="max-width:280px;max-height:180px"> | HA repeat.for_each affecte repeat.item à la variable avant le corps. Éviter de réutiliser la même variable dans des boucles imbriquées. |

## Mathématiques

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Calcul arithmétique**<br><code>ugso_math_arithmetic</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_math_arithmetic.png" alt="Calcul arithmétique" style="max-width:280px;max-height:180px"> | Addition, soustraction, multiplication, division ou puissance de nombres. Aucune conversion automatique des textes/booléens. |
| **Fonction numérique**<br><code>ugso_math_single</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_math_single.png" alt="Fonction numérique" style="max-width:280px;max-height:180px"> | Racine carrée, valeur absolue, négation, logarithmes et exponentielles. Valeurs invalides : erreur de modèle. |
| **Trigonométrie**<br><code>ugso_math_trig</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_math_trig.png" alt="Trigonométrie" style="max-width:280px;max-height:180px"> | Angles en degrés ; fonctions inverses en degrés. HA utilise des radians en interne. |
| **Constante**<br><code>ugso_math_constant</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_math_constant.png" alt="Constante" style="max-width:280px;max-height:180px"> | Constantes mathématiques finies. L’infini n’est pas proposé comme valeur numérique exportable. |
| **… est …**<br><code>ugso_math_property</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_math_property.png" alt="… est …" style="max-width:280px;max-height:180px"> | Vérifie les propriétés d’un nombre. Diviseur visible uniquement pour la divisibilité ; zéro est invalide. |
| **… … à … décimales**<br><code>ugso_math_round</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_math_round.png" alt="… … à … décimales" style="max-width:280px;max-height:180px"> | Arrondit à 0–10 décimales. HA/Jinja arrondit les égalités vers le pair ; supérieur/inférieur suit ceil/floor. |
| **… de la liste …**<br><code>ugso_math_list</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_math_list.png" alt="… de la liste …" style="max-width:280px;max-height:180px"> | Statistiques d’une liste numérique ; élément aléatoire de tout type. Somme vide : 0 ; autres résultats vides : null. |
| **Reste de … ÷ …**<br><code>ugso_math_modulo</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_math_modulo.png" alt="Reste de … ÷ …" style="max-width:280px;max-height:180px"> | Modulo Jinja. Avec un dividende négatif, le signe suit le diviseur et peut différer de JavaScript. |
| **Limiter … entre … et …**<br><code>ugso_math_clamp</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_math_clamp.png" alt="Limiter … entre … et …" style="max-width:280px;max-height:180px"> | Limite un nombre. Les bornes inversées sont d’abord triées. |
| **Entier aléatoire entre … et …**<br><code>ugso_math_random_int</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_math_random_int.png" alt="Entier aléatoire entre … et …" style="max-width:280px;max-height:180px"> | Bornes entières inclusives, au plus 10000 valeurs possibles. Bornes inversées autorisées. |
| **Nombre aléatoire de 0 à moins de 1**<br><code>ugso_math_random_fraction</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_math_random_fraction.png" alt="Nombre aléatoire de 0 à moins de 1" style="max-width:280px;max-height:180px"> | Pas de 0,00001, nouvelle valeur à chaque évaluation. Aléatoire non cryptographique. |
| **Angle atan2 y … x … en degrés**<br><code>ugso_math_atan2</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_math_atan2.png" alt="Angle atan2 y … x … en degrés" style="max-width:280px;max-height:180px"> | Angle sur quatre quadrants du standard Blockly, en complément des captures ioBroker. |

## Texte

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Saut de ligne …**<br><code>ugso_text_newline</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_newline.png" alt="Saut de ligne …" style="max-width:280px;max-height:180px"> | Un véritable saut de ligne pour assembler du texte. |
| **Créer du texte avec …**<br><code>ugso_text_join</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_join.png" alt="Créer du texte avec …" style="max-width:280px;max-height:180px"> | Assemble 0–100 valeurs en texte. Engrenage et +/− modifient le nombre d’entrées. |
| **Ajouter le texte … à la variable …**<br><code>ugso_text_append</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_append.png" alt="Ajouter le texte … à la variable …" style="max-width:280px;max-height:180px"> | Affecte un nouveau texte à une variable textuelle déjà initialisée. N’écrit pas dans une entité HA. |
| **Longueur du texte …**<br><code>ugso_text_length</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_length.png" alt="Longueur du texte …" style="max-width:280px;max-height:180px"> | Nombre de points de code Unicode, pas d’unités UTF-16 JavaScript. |
| **Le texte … est vide**<br><code>ugso_text_empty</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_empty.png" alt="Le texte … est vide" style="max-width:280px;max-height:180px"> | Vérifie si la longueur du texte est zéro. |
| **Le texte … contient …**<br><code>ugso_text_contains</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_contains.png" alt="Le texte … contient …" style="max-width:280px;max-height:180px"> | Recherche un sous-texte en respectant la casse. |
| **Dans le texte … trouver la … occurrence de …**<br><code>ugso_text_index</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_index.png" alt="Dans le texte … trouver la … occurrence de …" style="max-width:280px;max-height:180px"> | Position à partir de 1 en points de code Unicode ; résultat absent : 0. |
| **Dans le texte … prendre le caractère … à …**<br><code>ugso_text_char</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_char.png" alt="Dans le texte … prendre le caractère … à …" style="max-width:280px;max-height:180px"> | Position à partir de 1 depuis début/fin, premier/dernier/aléatoire. Hors limites : texte vide. |
| **Sous-texte de … de … à … inclus**<br><code>ugso_text_slice</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_slice.png" alt="Sous-texte de … de … à … inclus" style="max-width:280px;max-height:180px"> | Bornes inclusives à partir de 1 depuis le début. Bornes invalides/inversées : texte vide. |
| **Texte … en …**<br><code>ugso_text_case</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_case.png" alt="Texte … en …" style="max-width:280px;max-height:180px"> | Convertit le texte Unicode en majuscules, minuscules ou casse de titre. |
| **Retirer les espaces … du texte …**<br><code>ugso_text_trim</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_trim.png" alt="Retirer les espaces … du texte …" style="max-width:280px;max-height:180px"> | Retire les espaces extérieurs, tabulations et sauts de ligne compris. |
| **Compter … dans le texte …**<br><code>ugso_text_count</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_count.png" alt="Compter … dans le texte …" style="max-width:280px;max-height:180px"> | Compte les occurrences sans chevauchement ; recherche vide : 0. |
| **Remplacer … par … dans le texte …**<br><code>ugso_text_replace</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_replace.png" alt="Remplacer … par … dans le texte …" style="max-width:280px;max-height:180px"> | Remplace toutes les occurrences littérales, sans regex. Recherche vide : texte inchangé. |
| **Inverser le texte …**<br><code>ugso_text_reverse</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_reverse.png" alt="Inverser le texte …" style="max-width:280px;max-height:180px"> | Opération standard Blockly supplémentaire. Inverse les points de code Unicode, pas les graphèmes composés. |

## Listes

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Liste …**<br><code>ugso_list_new</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_list_new.png" alt="Liste …" style="max-width:280px;max-height:180px"> | Créer une liste de 0–100 valeurs ; l’engrenage ou +/− modifie le nombre d’entrées. |
| **Longueur de la liste …**<br><code>ugso_list_length</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_list_length.png" alt="Longueur de la liste …" style="max-width:280px;max-height:180px"> | Nombre d’éléments, utilisable comme nombre à l’exécution. L’entrée doit être une liste. |
| **La liste … est vide**<br><code>ugso_list_empty</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_list_empty.png" alt="La liste … est vide" style="max-width:280px;max-height:180px"> | Vérifie la longueur d’une liste, pas une valeur fausse générale de JavaScript. |
| **Liste avec … copies de …**<br><code>ugso_list_repeat</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_list_repeat.png" alt="Liste avec … copies de …" style="max-width:280px;max-height:180px"> | Nouvelle liste avec 0–10000 répétitions d’une valeur. |
| **Dans la liste … trouver la … occurrence de …**<br><code>ugso_list_index</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_list_index.png" alt="Dans la liste … trouver la … occurrence de …" style="max-width:280px;max-height:180px"> | Position à partir de 1, absent : 0. Égalité HA/Python, pas égalité de référence JavaScript. |
| **Dans la liste … prendre l’élément … à …**<br><code>ugso_list_get</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_list_get.png" alt="Dans la liste … prendre l’élément … à …" style="max-width:280px;max-height:180px"> | Position à partir de 1 depuis début/fin, premier/dernier/aléatoire. Hors limites ou liste vide : null. |
| **Dans la variable … … à … la valeur …**<br><code>ugso_list_set</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_list_set.png" alt="Dans la variable … … à … la valeur …" style="max-width:280px;max-height:180px"> | Affecte une nouvelle liste avec valeur remplacée/insérée. Indice à partir de 1 ; insertion autorisée à longueur+1. Indice invalide : liste inchangée. |
| **Retirer la position … de la variable liste …**<br><code>ugso_list_remove</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_list_remove.png" alt="Retirer la position … de la variable liste …" style="max-width:280px;max-height:180px"> | Affecte une nouvelle liste sans cet élément. Indice à partir de 1 ; indice invalide : liste inchangée. |
| **Sous-liste de … de … à … inclus**<br><code>ugso_list_slice</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_list_slice.png" alt="Sous-liste de … de … à … inclus" style="max-width:280px;max-height:180px"> | Copie une plage inclusive à partir de 1 depuis le début. Bornes invalides/inversées : liste vide. |
| **… valeur … séparateur …**<br><code>ugso_list_split</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_list_split.png" alt="… valeur … séparateur …" style="max-width:280px;max-height:180px"> | Découpe le texte selon un séparateur littéral ou assemble une liste. Séparateur vide : caractères Unicode. |
| **Trier la liste … … …**<br><code>ugso_list_sort</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_list_sort.png" alt="Trier la liste … … …" style="max-width:280px;max-height:180px"> | Nouvelle liste triée ; original inchangé. Mode numérique : nombres requis ; mode texte : éléments convertis en texte. |
| **Inverser la liste …**<br><code>ugso_list_reverse</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_list_reverse.png" alt="Inverser la liste …" style="max-width:280px;max-height:180px"> | Nouvelle liste dans l’ordre inverse ; original inchangé. |

## Couleur

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Couleur aléatoire**<br><code>ugso_colour_random</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_colour_random.png" alt="Couleur aléatoire" style="max-width:280px;max-height:180px"> | Nouvelle liste RGB de trois canaux aléatoires de 0 à 255 à chaque évaluation. |
| **Couleur rouge … % vert … % bleu … %**<br><code>ugso_colour_rgb</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_colour_rgb.png" alt="Couleur rouge … % vert … % bleu … %" style="max-width:280px;max-height:180px"> | Pourcentages RGB limités à 0–100, convertis en 0–255 et arrondis à la moitié supérieure. |
| **Mélanger la couleur … avec … part de la couleur 2 …**<br><code>ugso_colour_blend</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_colour_blend.png" alt="Mélanger la couleur … avec … part de la couleur 2 …" style="max-width:280px;max-height:180px"> | Mélange RGB linéaire. Part 0 = première couleur, 1 = seconde. Sans correction gamma ; résultat : liste RGB. |

## Variables

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Augmenter … de …**<br><code>ugso_variable_change</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_variable_change.png" alt="Augmenter … de …" style="max-width:280px;max-height:180px"> | Ajoute à une variable numérique déjà initialisée. Pas négatif : diminution. Valeurs non définies, textes, booléens et null ne sont pas automatiquement convertis. |
| **Définir … à …**<br><code>ugso_variable_set</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_variable_set.png" alt="Définir … à …" style="max-width:280px;max-height:180px"> | Définit ou modifie une variable HA pour cette exécution. Affecter avant de lire. |
| **Variable …**<br><code>ugso_variable_get</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_variable_get.png" alt="Variable …" style="max-width:280px;max-height:180px"> | Produit &#123;&#123; nom_variable &#125;&#125; pour un modèle HA. Ce n’est pas un assistant enregistré durablement. |

## Modèles

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Modèle …**<br><code>ugso_template</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_template.png" alt="Modèle …" style="max-width:280px;max-height:180px"> | Modèle Jinja comprenant &#123;&#123; ... &#125;&#125; ou &#123;% ... %&#125;. Évalué uniquement dans Home Assistant. |
| **Le modèle est vrai …**<br><code>ugso_template_condition</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_template_condition.png" alt="Le modèle est vrai …" style="max-width:280px;max-height:180px"> | HA évalue ce modèle Jinja comme condition. Ne déclenche pas une automatisation. |

## Autres blocs

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Automatisation … Quand … Seulement si … Alors …**<br><code>ugso_automation</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_automation.png" alt="Automatisation … Quand … Seulement si … Alors …" style="max-width:280px;max-height:180px"> | Automatisation native Home Assistant. Nom et mode au-dessus de l’espace de travail. |

## Fonctions Blockly originales

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Définir une fonction de valeur**<br><code>procedures_defreturn</code> | <img src="/assets/blocks-for-ha/blocks/fr/procedures_defreturn.png" alt="Définir une fonction de valeur" style="max-width:280px;max-height:180px"> | Éditeur Blockly original ; jusqu’à 8 paramètres ASCII via l’engrenage. Retour requis, sans actions ni récursion. Développement en Jinja à l’export. |
| **Appeler une fonction de valeur**<br><code>procedures_callreturn</code> | <img src="/assets/blocks-for-ha/blocks/fr/procedures_callreturn.png" alt="Appeler une fonction de valeur" style="max-width:280px;max-height:180px"> | Appel disponible dynamiquement dans Fonctions. Les entrées suivent les paramètres ; définition unique et tous les arguments requis. |
| **Lire une variable ou un paramètre**<br><code>variables_get</code> | <img src="/assets/blocks-for-ha/blocks/fr/variables_get.png" alt="Lire une variable ou un paramètre" style="max-width:280px;max-height:180px"> | Accès original Blockly, notamment dans les fonctions. Lit le paramètre local si présent, sinon une variable HA. |

## Plugins originaux

Ces plugins fournissent des champs ou commandes, sans être des types de blocs supplémentaires. Licence Apache-2.0, paquets intégrés localement.

| Plugin | Usage | Source originale |
| --- | --- | --- |
| toolbox-search | Rechercher les blocs disponibles ; catégorie en fin de menu. | [Dépôt original](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/toolbox-search) |
| field-slider | Champ curseur numérique. | [Dépôt original](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-slider) |
| field-date | Sélecteur de date. | [Dépôt original](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-date) |
| field-colour | Sélecteur de couleur. | [Dépôt original](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-colour) |
| field-multilineinput | Texte et modèles multilignes. | [Dépôt original](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-multilineinput) |
| field-dependent-dropdown | Choix d’action adapté au domaine de l’assistant. | [Dépôt original](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-dependent-dropdown) |
| theme-dark | Palette sombre. | [Dépôt original](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-dark) |
| theme-modern | Palette Modern. | [Dépôt original](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-modern) |
| theme-tritanopia | Palette adaptée à la tritanopie. | [Dépôt original](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-tritanopia) |
| zoom-to-fit | Ajuster les blocs à la vue. | [Dépôt original](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/zoom-to-fit) |
| workspace-search | Chercher les blocs déjà placés, Ctrl/Cmd+F. | [Dépôt original](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/workspace-search) |


## IDs des déclencheurs et cibles multiples

Depuis **0.1.28** : **États en liste JSON**, par exemple `["1_single","1_double"]` ; IDs facultatifs dans tous les déclencheurs standard ; **Déclenché par ID** comme condition native (ID individuel ou liste JSON). Les actions HA génériques acceptent **Cibles en liste JSON**, des métadonnées facultatives et conservent explicitement les données vides. Les automatisations à quatre boutons et quatre branches `choose` sont entièrement importables.

La sortie **Automatisation individuelle · Éditeur HA** omet l’`id` principal. Les IDs des déclencheurs restent présents. Les projets et la sortie **liste automations.yaml** conservent l’ID existant de l’automatisation.

| Block | Image | Description |
| --- | --- | --- |
| **Déclenché par ID**<br><code>ugso_trigger_condition</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_trigger_condition.png" alt="Déclenché par ID" style="max-width:280px;max-height:180px"> | `condition: trigger` · `id` |

[Home Assistant: Trigger IDs](https://www.home-assistant.io/docs/automation/trigger/#trigger-id) · [Trigger condition](https://www.home-assistant.io/docs/scripts/conditions/#trigger-condition)

## Pompes de piscine, événements et heures multiples

Depuis **0.1.30** : activer **Heures en liste JSON** pour plusieurs heures fixes, par exemple `["10:00:00","13:00:00","19:00:00"]`. **Tout changement** omet `to` ; **Entités en liste JSON** surveille plusieurs entités. Sans `to`, HA réagit aussi aux changements d’attributs. Les événements acceptent par exemple `timer.finished` avec un filtre de données JSON facultatif. Les conditions horaires natives conservent `before`/`after` : heures fixes, après inclusif et avant exclusif, même à travers minuit. Des bornes identiques couvrent toute la journée. Assistants horaires, modèles horaires et filtres de jours restent hors de l’import pris en charge. L’automatisation complète conserve le modèle multiligne du minuteur et les branches `choose` imbriquées.

| Block | Image | Description |
| --- | --- | --- |
| **Déclencheur événement**<br><code>ugso_event_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_event_trigger.png" alt="Déclencheur événement" style="max-width:280px;max-height:180px"> | `trigger: event` · `event_type` · `event_data` |
| **Condition horaire HA native**<br><code>ugso_native_time_condition</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_native_time_condition.png" alt="Condition horaire HA native" style="max-width:280px;max-height:180px"> | `condition: time` · `before` · `after` |

[Home Assistant: triggers](https://www.home-assistant.io/docs/automation/trigger/) · [Time condition](https://www.home-assistant.io/docs/scripts/conditions/#time-condition)

## Température modifiée

Depuis **0.1.31**, le nouveau bloc prend en charge temperature.changed natif. Cible (JSON) : entity_id texte ou liste. Seuil (JSON) : type any, above, below, between ou outside. any exige seulement type ; above/below exigent value, between/outside value_min et value_max. Nombres : number et unit_of_measurement (°C/°F). Références : entity (sensor, number ou input_number). ID facultatif. Autres cibles (zone/appareil/étiquette) non prises en charge. Les topics MQTT, qos/retain/evaluate_payload et contenus JSON/Jinja multilignes restent présents.

| Block | Image | Description |
| --- | --- | --- |
| **Température modifiée**<br><code>ugso_temperature_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_temperature_trigger.png" alt="Température modifiée" style="max-width:280px;max-height:180px"> | temperature.changed |

[Home Assistant: temperature.changed](https://www.home-assistant.io/triggers/temperature.changed/)

## Calendriers et variables de réponse

**0.1.32:** `calendar.event_started` / `calendar.event_ended`. Cible : objet JSON avec `entity_id` en texte ou liste. Options facultatives : `offset` avec jours, heures, minutes et secondes combinés ou `HH:MM:SS` ; `offset_type` vaut `before` ou `after`. Décalage nul, options absentes et ID de déclencheur facultatif sont conservés.

Le champ **Variable de réponse (facultative)** du bloc **Action HA** génère `response_variable`, par exemple `termine` pour `calendar.get_events`. Vide, il omet ce champ du YAML. L’automation complète de jours fériés/vacances conserve les deux calendriers, le démarrage HA, les variables zeitpunkt/termin_aktiv, les modèles Jinja multilignes, choose/default et le mode queued. Home Assistant traite les calendriers et les modèles.

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Début/fin d’un événement calendrier**<br><code>ugso_calendar_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_calendar_trigger.png" alt="Début/fin d’un événement calendrier" style="max-width:280px;max-height:180px"> | calendar.event_started / calendar.event_ended |

[Home Assistant: calendar.event_started](https://www.home-assistant.io/triggers/calendar.event_started/) · [calendar.event_ended](https://www.home-assistant.io/triggers/calendar.event_ended/) · [calendar.get_events](https://www.home-assistant.io/actions/calendar.get_events/)

## Déclencheurs numériques avec durée de maintien

Depuis **0.1.33**, le déclencheur numérique accepte plusieurs entités : activer **Entités en liste JSON** et saisir par exemple `["sensor.temp_1","sensor.temp_2"]`. Sans cette case, l’entité unique reste active. **Durée de maintien (JSON)** avec **activée** génère le champ facultatif `for` : par exemple `{"hours":0,"minutes":1,"seconds":0}`, `60` ou `"00:01:00"`. Les unités days/hours/minutes/seconds/milliseconds combinées, les zéros et les modèles de sortie HA sont conservés. Décocher omet `for`. Toujours exactement un seuil numérique fixe (above ou below) ; les IDs et branches choose sont conservés.

Home Assistant déclenche après le franchissement du seuil lorsque la valeur reste de ce côté du seuil pendant toute la durée. Un redémarrage HA ou le rechargement des automations réinitialise le maintien en cours. [Home Assistant: numeric_state](https://www.home-assistant.io/triggers/numeric_state/).

## Plusieurs variables dans une action

Depuis **0.1.34**, le menu **Variables** propose **Définir les variables (JSON)**. L’objet JSON contient 1–100 noms de variables avec texte, modèle HA, nombre, booléen ou null. Plusieurs entrées restent une seule action native `variables`, avec leur ordre. Les affectations uniques conservent le bloc existant. Les valeurs liste/objet et les variables au niveau automation restent non prises en charge. Modifier noms et modèles directement dans le JSON ; le dialogue de renommage Blockly ne modifie pas ce texte JSON libre. Les noms importés sont également enregistrés dans Blockly.

L’exemple de minuterie conserve h/m, les deux entités surveillées, la condition et le mode restart. Les conditions absentes deviennent une liste vide.

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Définir les variables (JSON)**<br><code>ugso_variables_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_variables_action.png" alt="Définir les variables (JSON)" style="max-width:280px;max-height:180px"> | Variables HA natives dans un objet JSON. |

[Home Assistant: variables](https://www.home-assistant.io/docs/scripts/#variables)

## Délai en texte ou modèle

Depuis **0.1.35**, Blocks importe les textes natifs `delay` dans le nouveau bloc sous **Délais**. Exemples : `00:00:02`, `01:30` (une heure et 30 minutes), `00:00:00.250` ou un modèle de sortie HA. La durée reste un texte dans le YAML et le projet sauvegardé. L’exécution HA attend avant de poursuivre les actions suivantes. Les blocs existants en secondes et unités restent disponibles. Cette extension concerne `delay`, pas le délai maximal du bloc attendre-jusqu’à.

L’exemple de réinitialisation désactive d’abord timer_reset, attend deux secondes puis désactive les deux cibles. L’ID input_boolean.timer_runing est conservé exactement comme fourni.

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Attendre durée en texte / modèle**<br><code>ugso_delay_text</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_delay_text.png" alt="Attendre durée en texte / modèle" style="max-width:280px;max-height:180px"> | Texte de durée delay natif / modèle HA. |

[Home Assistant: delay](https://www.home-assistant.io/docs/scripts/#wait-for-time-to-pass-delay)
