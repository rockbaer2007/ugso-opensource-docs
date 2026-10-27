---
title: Catalogue des blocs
description: Tous les blocs UGSo avec images françaises et fonctions.
---

# Catalogue des blocs

Depuis **0.1.66**, les valeurs de texte simples sont vides dans toutes les catégories : sujet/message MQTT, contenus d’objets/listes, conversions et valeurs de remplacement sans exemples. Réponses Assist et texte Jinja utilisent aussi des champs sur une ligne. Saisir les valeurs requises avant l’export. Séparateurs, structures JSON valides et réglages numériques, horaires et d’actions conservés. L’ouverture d’un projet conserve ses textes, y compris les sauts de ligne existants. Les éditeurs multilignes de code Jinja et JSON restent disponibles.

## Blocs logiques séparés et engrenages HA depuis 0.1.61

**et** (`ugso_and`) et **ou** (`ugso_or`) sont des blocs extensibles séparés ; **non** a une entrée. Le bloc combiné `ugso_logic_condition` reste pris en charge pour les anciens projets. Ajouter, retirer et ordonner les entrées HA facultatives par engrenage. [Groupes examinés et images](./advanced).

## Horaire et données du déclencheur depuis 0.1.60

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Horaire** · Déclencheurs<br><code>ugso_schedule_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_schedule_trigger.png" alt="Horaire" style="max-width:280px;max-height:180px"> | Champ CRON avec dialogue Assistant/Simple/CRON et secondes. Motifs horaires et heures avec jours HA natifs. [Règles et limites](./time). |
| **↪ Données du déclencheur** · Déclencheurs<br><code>ugso_trigger_value</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_trigger_value.png" alt="Données du déclencheur" style="max-width:280px;max-height:180px"> | État actuel/précédent, ID d’entité, ID/type du déclencheur, message MQTT/JSON et données d’événement. Donnée absente : `none`. |

Les déclencheurs HA avancés sont directement dans **Déclencheurs**. Le déclencheur solaire dispose aussi d’un décalage facultatif en minutes. [Comparaison des déclencheurs ioBroker](./time).

## Libellés, commentaires et MQTT depuis 0.1.59

Les libellés standard et les éditeurs par engrenage suivent maintenant ioBroker/Blockly en DE/EN/FR : **Attributs / Attribut**, **Liste / Élément**, **joindre / Élément** et **selon / dans le cas de / default**. Les noms d’attributs sont modifiables dans l’éditeur ; la branche default peut être ajoutée ou supprimée. Les libellés de texte, listes, mathématiques et logique sont harmonisés. Les entrées HA supplémentaires, les affectations immuables, les formats de date Python et le prochain événement solaire restent explicites.

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Commentaire** · Système<br><code>ugso_comment</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_comment.png" alt="Commentaire" style="max-width:280px;max-height:180px"> | Note jaune, libre ou dans une chaîne d’actions. Le projet JSON conserve texte et position. Les notes actives sont regroupées en lignes `#` avant l’automatisation YAML et redeviennent des blocs libres à l’import, aussi en mode ajout. Les positions originales des commentaires YAML ne sont pas conservées. Aucune action exécutée. |
| **Message MQTT** · Messages<br><code>ugso_mqtt_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_mqtt_action.png" alt="Message MQTT" style="max-width:280px;max-height:180px"> | Sujet (Topic), message, conserver et QoS 0/1/2. Entrées texte ou Jinja ; sortie native `mqtt.publish`. Sans sélection d’instance. L’intégration MQTT de HA doit être configurée ; HA effectue l’envoi. |

Depuis **0.1.58**, les commandes suivent autant que possible ioBroker : extension uniquement par l’engrenage, sans boutons +/−/S supplémentaires. Cela concerne aussi objets, listes, texte, cas et branches parallèles. ET/OU compact est retiré du menu ; les projets existants restent lisibles. Les champs HA, connexions et fonctions YAML sont conservés. L’objectif est une apparence familière d’ioBroker avec une prise en charge complète des automatisations HA.

## Messages depuis 0.1.48

Nouvelle catégorie **Messages**, trois blocs DE/EN/FR. [Configuration, clés et envoi](../callmebot/).

Depuis **0.1.50**, également **Signal · CallMeBot** avec sa propre sélection de profil. [Configurer l’application Signal](../callmebot-signal/).

| Bloc | Image | Fonction |
| --- | --- | --- |
| **WhatsApp · CallMeBot**<br><code>ugso_callmebot_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_callmebot_action.png" alt="CallMeBot" style="max-width:360px;max-height:180px"> | Profil, texte/Jinja et journal. Envoi MQTT via l’application CallMeBot Whatsapp. Clés conservées dans le backend. |
| **Signal · CallMeBot**<br><code>ugso_callmebot_signal_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_callmebot_signal_action.png" alt="CallMeBot" style="max-width:360px;max-height:180px"> | Profil, texte/Jinja et journal. Envoi MQTT via l’application CallMeBot Signal. Clés conservées dans le backend. |
| **Intégration WhatsApp**<br><code>ugso_whatsapp_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_whatsapp_action.png" alt="Intégration WhatsApp" style="max-width:360px;max-height:180px"> | whatsapp.send_message avec number ou target, ou notify.whatsapp. Destinataire sans +, message et compte facultatif. Configurer le jeton une fois dans HA. |

## Fonctions depuis 0.1.47

Le catalogue actuel contient **169 types de blocs**. [Paramètres, export et limites](./blockly-audit).

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Définir une fonction d’action**<br><code>procedures_defnoreturn</code> | <img src="/assets/blocks-for-ha/blocks/fr/procedures_defnoreturn.png" alt="Définir une fonction d’action" style="max-width:280px;max-height:180px"> | Suite d’actions HA réutilisable ; jusqu’à huit paramètres via l’engrenage. Définition à côté de l’automatisation. |
| **Appeler une fonction d’action**<br><code>procedures_callnoreturn</code> | <img src="/assets/blocks-for-ha/blocks/fr/procedures_callnoreturn.png" alt="Appeler une fonction d’action" style="max-width:280px;max-height:180px"> | Appel dynamique avec entrées d’argument. Export en groupe HA avec ses propres variables de paramètre. |
| **Valeur de retour conditionnelle**<br><code>ugso_function_result</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_function_result.png" alt="Si renvoyer sinon" style="max-width:280px;max-height:180px"> | Si / valeur / sinon ; seule la branche choisie est évaluée dans HA. Sans suite d’actions. |

Depuis **0.1.45**, la boîte à outils ne contient plus de doublons : nombre dans **Mathématiques**, texte dans **Texte**, couleur dans **Couleur** et groupe ET/OU/NON dans **Logique**. **Valeurs** contient uniquement le pourcentage. Les 163 types et projets existants restent pris en charge.

**0.1.44 · 163 types**. Tous les types ont été vérifiés pour les champs de sélection HA appropriés. Les images montrent les vrais blocs Blockly en français. Les variantes des menus déroulants ne sont pas des types supplémentaires. Les IDs techniques restent identiques en DE/EN/FR. Les textes et entités d’exemple gardent leurs valeurs d’origine. [Sélection HA](./entities).

Dans Standard/Dark, les déclencheurs sont orange, les conditions et la logique bleues, les valeurs vertes, les actions bleu turquoise et les objets bruns. Les autres palettes adaptent les couleurs. [Usage et import](./) · [Paquets personnalisés](./custom-blocks).

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
| **Pourcentage**<br><code>ugso_percent</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_percent.png" alt="Pourcentage" style="max-width:280px;max-height:180px"> | Curseur de 0 à 100, valeur numérique en pourcentage. |

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
| **Nouvel objet …**<br><code>ugso_object_new</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_object_new.png" alt="Nouvel objet …" style="max-width:280px;max-height:180px"> | Dictionnaire local à attributs nommés. Ajouter des entrées avec l’engrenage. Ce n’est ni une entité HA ni un point de données ioBroker. |
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

## Actions

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Allumer / éteindre / basculer**<br><code>ugso_switch_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_switch_action.png" alt="Allumer / éteindre / basculer" style="max-width:280px;max-height:180px"> | Action du domaine de l’entité choisie. Vérifier sa disponibilité dans HA. |
| **Action HA … cible … données (JSON) …**<br><code>ugso_service_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_service_action.png" alt="Action HA … cible … données (JSON) …" style="max-width:280px;max-height:180px"> | Cible facultative. Données sous forme d’objet JSON ; l’intégration doit être présente dans HA. |
| **Attendre … secondes**<br><code>ugso_delay_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_delay_action.png" alt="Attendre … secondes" style="max-width:280px;max-height:180px"> | Attendre un nombre de secondes via une action delay native HA. |
| **Lampe … couleur … luminosité … %**<br><code>ugso_colour_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_colour_action.png" alt="Lampe … couleur … luminosité … %" style="max-width:280px;max-height:180px"> | Action light.turn_on avec couleur RGB et brightness_pct. Lampe compatible et luminosité 0–100 requises. |

## Logique

Depuis **0.1.57**, les entrées des groupes ET/OU extensibles sont alignées horizontalement, avec « et » ou « ou » entre elles. Le sélecteur contient uniquement « et / ou / non ». Les blocs de l’engrenage portent le même opérateur au lieu de « Condition », également en DE/EN. La logique HA reste inchangée.

Depuis **0.1.56**, le bloc Si extensible est disponible ici. Logique est bleu et Objets brun dans Standard/Dark. [Couleurs et branches](./themes).

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Si … faire …**<br><code>ugso_if_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_if_action.png" alt="Si … faire …" style="max-width:280px;max-height:180px"> | Branche if native HA avec actions, sinon si et sinon. Engrenage pour étendre les branches. |
| **Groupe de conditions**<br><code>ugso_logic_condition</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_logic_condition.png" alt="Groupe de conditions" style="max-width:280px;max-height:180px"> | Groupe ET, OU ou NON extensible jusqu’à 100 conditions. Engrenage pour modifier les entrées. |
| **Comparaison**<br><code>ugso_compare</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_compare.png" alt="Comparaison" style="max-width:280px;max-height:180px"> | Compare deux valeurs HA. Nombres et textes ont des types différents ; convertir explicitement les valeurs de capteurs dans les modèles. |
| **ET / OU compact**<br><code>ugso_binary_logic</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_binary_logic.png" alt="ET / OU compact" style="max-width:280px;max-height:180px"> | Projets existants uniquement ; retiré du menu. Utiliser le groupe ET/OU extensible. |
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
| **Nombre**<br><code>ugso_number</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_number.png" alt="Nombre" style="max-width:280px;max-height:180px"> | Nombre fixe éditable. Utilisable pour valeurs et seuils de déclencheurs numériques. |
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
| **Texte**<br><code>ugso_text</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text.png" alt="Texte" style="max-width:280px;max-height:180px"> | Depuis 0.1.65, champ vide sur une ligne entre guillemets, sans ligne d’aide supplémentaire. Entrée valide. Le texte existant reste intact à l’import de projet/YAML, y compris les sauts de ligne. |
| **Saut de ligne …**<br><code>ugso_text_newline</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_newline.png" alt="Saut de ligne …" style="max-width:280px;max-height:180px"> | Un véritable saut de ligne pour assembler du texte. |
| **Créer du texte avec …**<br><code>ugso_text_join</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_text_join.png" alt="Créer du texte avec …" style="max-width:280px;max-height:180px"> | Assemble 0–100 valeurs en texte. L’engrenage modifie le nombre d’entrées. |
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
| **Liste …**<br><code>ugso_list_new</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_list_new.png" alt="Liste …" style="max-width:280px;max-height:180px"> | Créer une liste de 0–100 valeurs ; l’engrenage modifie le nombre d’entrées. |
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
| **Couleur …**<br><code>ugso_colour</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_colour.png" alt="Couleur …" style="max-width:280px;max-height:180px"> | Sélectionner une couleur ; conversion en liste de canaux RGB pour HA. |
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
| **Jinja – code personnalisé**<br><code>ugso_template</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_template.png" alt="Jinja – code personnalisé" style="max-width:280px;max-height:180px"> | Modèle Jinja comprenant &#123;&#123; ... &#125;&#125; ou &#123;% ... %&#125;. Évalué uniquement dans Home Assistant. |
| **Jinja – condition personnalisée**<br><code>ugso_template_condition</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_template_condition.png" alt="Jinja – condition personnalisée" style="max-width:280px;max-height:180px"> | HA évalue ce modèle Jinja comme condition. Ne déclenche pas une automatisation. |

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

Depuis **0.1.50**, également **Signal · CallMeBot** avec sa propre sélection de profil. [Configurer l’application Signal](../callmebot-signal/).

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

Depuis **0.1.31**, le nouveau bloc prend en charge temperature.changed natif. Cible (JSON) : entity_id texte ou liste. Seuil (JSON) : type any, above, below, between ou outside. any exige seulement type ; above/below exigent value, between/outside value_min et value_max. Nombres : number et unit_of_measurement (°C/°F). Références : entity (sensor, number ou input_number). ID facultatif. Depuis 0.1.39, cibles zone, appareil, étage et étiquette prises en charge. Les topics MQTT, qos/retain/evaluate_payload et contenus JSON/Jinja multilignes restent présents.

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

Depuis **0.1.34**, le menu **Variables** propose **Définir les variables (JSON)**. L’objet JSON contient 1–100 noms de variables avec texte, modèle HA, nombre, booléen ou null. Plusieurs entrées restent une seule action native `variables`, avec leur ordre. Les affectations uniques conservent le bloc existant. Depuis 0.1.39, listes/objets et variables au niveau automation sont pris en charge ; voir [HA avancé et Jinja](./advanced). Modifier noms et modèles directement dans le JSON ; le dialogue de renommage Blockly ne modifie pas ce texte JSON libre. Les noms importés sont également enregistrés dans Blockly.

L’exemple de minuterie conserve h/m, les deux entités surveillées, la condition et le mode restart. Les conditions absentes deviennent une liste vide.

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Définir les variables (JSON)**<br><code>ugso_variables_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_variables_action.png" alt="Définir les variables (JSON)" style="max-width:280px;max-height:180px"> | Variables avec champs individuels ; listes et objets en JSON, nouveaux noms dans les options supplémentaires. |

[Home Assistant: variables](https://www.home-assistant.io/docs/scripts/#variables)

## Délai en texte ou modèle

Depuis **0.1.35**, Blocks importe les textes natifs `delay` dans le nouveau bloc sous **Délais**. Exemples : `00:00:02`, `01:30` (une heure et 30 minutes), `00:00:00.250` ou un modèle de sortie HA. La durée reste un texte dans le YAML et le projet sauvegardé. L’exécution HA attend avant de poursuivre les actions suivantes. Les blocs existants en secondes et unités restent disponibles. Cette extension concerne `delay`, pas le délai maximal du bloc attendre-jusqu’à.

L’exemple de réinitialisation désactive d’abord timer_reset, attend deux secondes puis désactive les deux cibles. L’ID input_boolean.timer_runing est conservé exactement comme fourni.

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Attendre durée en texte / modèle**<br><code>ugso_delay_text</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_delay_text.png" alt="Attendre durée en texte / modèle" style="max-width:280px;max-height:180px"> | Texte de durée delay natif / modèle HA. |

[Home Assistant: delay](https://www.home-assistant.io/docs/scripts/#wait-for-time-to-pass-delay)

## Noms d’action HA dynamiques

Depuis **0.1.36**, le premier champ du bloc **Action HA** accepte un nom d’action fixe ou un modèle Jinja. Il est éditable sur plusieurs lignes. Exemples : `input_boolean.turn_on`, `input_boolean.turn_` suivi d’une expression Jinja ou un modèle if/else complet. Cible, données, métadonnées et variable de réponse conservent leurs champs existants. Modèles et sauts de ligne sont conservés à l’import, dans le projet et à l’export YAML.

L’exemple Shelly conserve le préfixe `input_boolean.turn_` avec la lecture de l’état et les branches choose imbriquées. Home Assistant évalue le nom à l’exécution ; il doit alors produire un service disponible. Blocks vérifie les noms fixes et délimiteurs de modèle, pas la syntaxe Jinja ni le résultat à l’exécution. Les cibles restent des IDs fixes ; les modèles pour un objet data complet ne font pas partie de cette extension.

[Home Assistant: choosing the action with a template](https://www.home-assistant.io/docs/scripts/perform-actions/#choosing-the-action-with-a-template)


## Déclencheur de motif horaire

Depuis **0.1.37**, **Déclencheurs** propose un bloc natif `time_pattern`. Le champ JSON accepte par exemple `{"seconds":"/30"}` pour les secondes 0 et 30 de chaque minute. Clés facultatives : `hours`, `minutes`, `seconds` ; au moins une est requise. Valeurs fixes : heures 0–23, minutes/secondes 0–59, nombres ou textes sans zéro initial. `*` correspond à toute valeur, `/n` aux valeurs divisibles par n (n > 0 dans la plage du champ). Les unités omises et les types nombre/texte restent inchangés ; Home Assistant applique ses valeurs par défaut lors de l’exécution. Un ID de déclencheur facultatif est disponible.

L’automatisation LCD avec quatre actions `input_text.set_value` et `mode: restart` conserve ses modèles Jinja, formatage, découpage, remplissage et sauts de ligne après import, rechargement et export. Home Assistant exécute les modèles et le planning.

| Block | Type |
| --- | --- |
| ![Motif horaire (JSON)](/assets/blocks-for-ha/blocks/fr/ugso_time_pattern_trigger.png) | `ugso_time_pattern_trigger` |

[Home Assistant: time_pattern](https://www.home-assistant.io/triggers/time_pattern/).


## Entités cibles dynamiques

Depuis **0.1.39**, **Cible** dans le bloc générique **Action HA** accepte un ID fixe ou un modèle HA, par exemple <code v-pre>{{ ziel_tv }}</code>. Le dialogue de sélection propose un champ multiligne. La liste JSON des cibles peut mélanger IDs fixes et modèles. Jinja est conservé et évalué par Home Assistant lors de l’exécution. Les cibles dynamiques importées utilisent le bloc générique, car les blocs spécialisés ne peuvent pas déterminer leur domaine de façon fiable.

L’automatisation TV de la chambre avec variable multiligne du mode été, horaires 21:30 et 00:30 et deux branches choose est vérifiée. Modèles de cible, texte de variable et conditions horaires restent inchangés après import, rechargement et export. Les champs d’entité des déclencheurs et conditions exigent toujours des IDs fixes.

[Home Assistant: templates in action targets](https://www.home-assistant.io/docs/scripts/perform-actions/#setting-targets-and-options-with-a-template).


## HA avancé et Jinja depuis 0.1.39

[Anleitung / Guide](./advanced).

| Bloc | Image | Fonction |
| --- | --- | --- |
| **HA state**<br><code>ugso_ha_state_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_state_trigger.png" alt="HA state" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **HA numeric_state**<br><code>ugso_ha_numeric_state_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_numeric_state_trigger.png" alt="HA numeric_state" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **HA time**<br><code>ugso_ha_time_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_time_trigger.png" alt="HA time" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **HA sun**<br><code>ugso_ha_sun_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_sun_trigger.png" alt="HA sun" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **HA homeassistant**<br><code>ugso_ha_homeassistant_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_homeassistant_trigger.png" alt="HA homeassistant" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **HA mqtt**<br><code>ugso_ha_mqtt_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_mqtt_trigger.png" alt="HA mqtt" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **HA template**<br><code>ugso_ha_template_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_template_trigger.png" alt="HA template" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **HA webhook**<br><code>ugso_ha_webhook_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_webhook_trigger.png" alt="HA webhook" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **HA zone**<br><code>ugso_ha_zone_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_zone_trigger.png" alt="HA zone" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **HA device**<br><code>ugso_ha_device_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_device_trigger.png" alt="HA device" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **HA tag**<br><code>ugso_ha_tag_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_tag_trigger.png" alt="HA tag" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **HA conversation**<br><code>ugso_ha_conversation_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_conversation_trigger.png" alt="HA conversation" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **HA geo_location**<br><code>ugso_ha_geo_location_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_geo_location_trigger.png" alt="HA geo_location" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **HA calendar**<br><code>ugso_ha_calendar_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_calendar_trigger.png" alt="HA calendar" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **HA event**<br><code>ugso_ha_event_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_event_trigger.png" alt="HA event" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **Déclencheur HA (avancé)**<br><code>ugso_ha_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_trigger.png" alt="Déclencheur HA (avancé)" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **Condition HA (avancée)**<br><code>ugso_ha_condition</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_condition.png" alt="Condition HA (avancée)" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **Étape HA (avancée)**<br><code>ugso_ha_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_ha_action.png" alt="Étape HA (avancée)" style="max-width:280px;max-height:180px"> | Champs HA nommés et options JSON supplémentaires. Structure vérifiée ; vérifier intégration et exécution dans HA. |
| **Action HA type de cible cible données options d’étape**<br><code>ugso_target_action</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_target_action.png" alt="Action HA type de cible cible données options d’étape" style="max-width:280px;max-height:180px"> | Champs HA avancés ou Jinja original. Structure prise en charge vérifiée ; vérifier intégration et exécution dans HA. |
| **Intégration HA cible options activées**<br><code>ugso_integration_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_integration_trigger.png" alt="Intégration HA cible options activées" style="max-width:280px;max-height:180px"> | Champs HA avancés ou Jinja original. Structure prise en charge vérifiée ; vérifier intégration et exécution dans HA. |
| **Groupe d’actions**<br><code>ugso_sequence</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_sequence.png" alt="Groupe d’actions" style="max-width:280px;max-height:180px"> | Champs HA avancés ou Jinja original. Structure prise en charge vérifiée ; vérifier intégration et exécution dans HA. |
| **Parallèle branche 1 branche 2**<br><code>ugso_parallel</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_parallel.png" alt="Parallèle branche 1 branche 2" style="max-width:280px;max-height:180px"> | Champs HA avancés ou Jinja original. Structure prise en charge vérifiée ; vérifier intégration et exécution dans HA. |
| **Attendre un déclencheur options**<br><code>ugso_wait_trigger</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_wait_trigger.png" alt="Attendre un déclencheur options" style="max-width:280px;max-height:180px"> | Champs HA avancés ou Jinja original. Structure prise en charge vérifiée ; vérifier intégration et exécution dans HA. |
| **Continuer seulement si**<br><code>ugso_condition_step</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_condition_step.png" alt="Continuer seulement si" style="max-width:280px;max-height:180px"> | Champs HA avancés ou Jinja original. Structure prise en charge vérifiée ; vérifier intégration et exécution dans HA. |
| **Émettre un événement données**<br><code>ugso_fire_event</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_fire_event.png" alt="Émettre un événement données" style="max-width:280px;max-height:180px"> | Champs HA avancés ou Jinja original. Structure prise en charge vérifiée ; vérifier intégration et exécution dans HA. |
| **Réponse Assist**<br><code>ugso_assist_response</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_assist_response.png" alt="Réponse Assist" style="max-width:280px;max-height:180px"> | Champs HA avancés ou Jinja original. Structure prise en charge vérifiée ; vérifier intégration et exécution dans HA. |
| **Activer la scène**<br><code>ugso_scene</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_scene.png" alt="Activer la scène" style="max-width:280px;max-height:180px"> | Champs HA avancés ou Jinja original. Structure prise en charge vérifiée ; vérifier intégration et exécution dans HA. |
| **Jinja (expérimental)**<br><code>ugso_jinja_value</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_value.png" alt="Jinja (expérimental)" style="max-width:280px;max-height:180px"> | Champs HA avancés ou Jinja original. Structure prise en charge vérifiée ; vérifier intégration et exécution dans HA. |
| **Condition Jinja (expérimentale)**<br><code>ugso_jinja_condition</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_condition.png" alt="Condition Jinja (expérimentale)" style="max-width:280px;max-height:180px"> | Champs HA avancés ou Jinja original. Structure prise en charge vérifiée ; vérifier intégration et exécution dans HA. |

## Structures Jinja (expérimental)

Depuis **0.1.64**, les blocs de code libre figurent uniquement dans **Templates** sous **Jinja – code personnalisé** et **Jinja – condition personnalisée**. Les anciens types `ugso_jinja_value` et `ugso_jinja_condition` restent lisibles pour les projets et imports ; les images suivantes documentent ces anciens types. [Templates par usage](./system-template).

15 nouveaux types depuis 0.1.41. Les blocs valeur/condition extérieurs relient les parties imbriquées à HA. Expressions Jinja et parties du modèle ont des connexions typées distinctes. [Import, édition et limites](./advanced#jinja-experimental).

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Jinja composé**<br><code>ugso_jinja_composed_value</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_composed_value.png" alt="Jinja composé" style="max-width:280px;max-height:180px"> | Bloc valeur extérieur : modèle complet, original conservé jusqu’à modification. |
| **Condition Jinja composée**<br><code>ugso_jinja_composed_condition</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_composed_condition.png" alt="Condition Jinja composée" style="max-width:280px;max-height:180px"> | Bloc booléen extérieur pour une condition de modèle HA. |
| **Entité fonction**<br><code>ugso_jinja_entity</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_entity.png" alt="Entité fonction" style="max-width:280px;max-height:180px"> | Rechercher une entité et choisir states/state_attr/is_state/is_state_attr ; relier les arguments. |
| **Filtre arguments valeur**<br><code>ugso_jinja_filter</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_filter.png" alt="Filtre arguments valeur" style="max-width:280px;max-height:180px"> | Choisir un filtre ; relier 0–3 arguments positionnels et une expression Jinja. |
| **Littéral (Jinja)**<br><code>ugso_jinja_literal</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_literal.png" alt="Littéral (Jinja)" style="max-width:280px;max-height:180px"> | Nombre, chaîne entre guillemets, true/false ou none en syntaxe Jinja. |
| **Variable Jinja**<br><code>ugso_jinja_variable</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_variable.png" alt="Variable Jinja" style="max-width:280px;max-height:180px"> | Nom simple de variable Jinja en texte ; sans renommage automatique Blockly. |
| **Maintenant (Jinja)**<br><code>ugso_jinja_now</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_now.png" alt="Maintenant (Jinja)" style="max-width:280px;max-height:180px"> | Générer now() ; Home Assistant fournit l’heure lors de l’évaluation. |
| **Expression**<br><code>ugso_jinja_binary</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_binary.png" alt="Expression" style="max-width:280px;max-height:180px"> | Calculer, comparer ou combiner deux expressions Jinja avec and/or. |
| **Expression**<br><code>ugso_jinja_unary</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_unary.png" alt="Expression" style="max-width:280px;max-height:180px"> | Appliquer not, un signe négatif ou positif à une expression Jinja. |
| **Valeur si sinon**<br><code>ugso_jinja_select</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_select.png" alt="Valeur si sinon" style="max-width:280px;max-height:180px"> | Choisir une valeur : yes if test else no. Trois entrées obligatoires. |
| **Afficher**<br><code>ugso_jinja_output</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_output.png" alt="Afficher" style="max-width:280px;max-height:180px"> | Afficher une expression comme <code v-pre>{{ ... }}</code> dans un modèle. |
| **Texte Jinja**<br><code>ugso_jinja_text</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_text.png" alt="Texte Jinja" style="max-width:280px;max-height:180px"> | Texte littéral, espaces compris ; ne pas insérer de délimiteurs Jinja. |
| **Parties du modèle puis**<br><code>ugso_jinja_join</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_join.png" alt="Parties du modèle puis" style="max-width:280px;max-height:180px"> | Relier deux parties de modèle dans l’ordre affiché. |
| **Si texte sinon**<br><code>ugso_jinja_if</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_if.png" alt="Si texte sinon" style="max-width:280px;max-height:180px"> | if/else avec condition et parties texte/sortie imbriquées. |
| **Pour dans texte si vide**<br><code>ugso_jinja_for</code> | <img src="/assets/blocks-for-ha/blocks/fr/ugso_jinja_for.png" alt="Pour dans texte si vide" style="max-width:280px;max-height:180px"> | Boucle for simple : variable, expression, contenu et cas vide facultatif. |

:::: details Référence détaillée issue de la documentation allemande

## Liste des blocs {#liste-der-blocks}

Depuis la version **0.1.66**, les champs de texte simples sont vides par défaut : les rubriques « Topic MQTT et message », « Contenu d'objet/liste », « Transformations » et « Valeurs de remplacement » ne contiennent plus de texte d'exemple. Les champs « Réponse Assist » et « Texte Jinja » utilisent également des zones de texte sur une seule ligne. Vous devez saisir les contenus nécessaires vous-même avant l'exportation. Les délimiteurs, les structures JSON de base valides, ainsi que les paramètres relatifs aux nombres, au temps et aux actions sont conservés. Les textes enregistrés ne sont pas effacés à l'ouverture ; les sauts de ligne existants sont également préservés. Les éditeurs multilignes pour le code Jinja et le JSON restent disponibles.

### Blocs logiques individuels et paramètres HA (via l'icône engrenage) depuis 0.1.61 {#einzelne-logikblocke-und-ha-zahnrader-seit-0-1-61}

Les blocs **ET** (`ugso_and`) et **OU** (`ugso_or`) sont désormais des blocs extensibles ; le bloc **NON** conserve une entrée unique. Le bloc combiné `ugso_logic_condition` n'est pris en charge que pour les anciens projets. Les entrées HA optionnelles peuvent être ajoutées, supprimées ou réorganisées individuellement via l'icône engrenage. [Comparatif complet des groupes de blocs vérifiés et de leurs visuels](/fr/projects/blocks-for-ha/advanced).

### Calendrier et données de déclenchement depuis 0.1.60 {#zeitplan-und-ausloserdaten-seit-0-1-60}

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Planification** · Déclencheur<br><code>ugso_schedule_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_schedule_trigger.png" alt="Zeitplan" style="max-width:280px;max-height:180px"> | Champ CRON avec assistant/mode simple/dialogue CRON et gestion des secondes. Modèles temporels natifs HA et heures spécifiques avec jours de la semaine. [Règles et limites prises en charge](/fr/projects/blocks-for-ha/time). |
| **↪ Données du déclencheur** · Déclencheur<br><code>ugso_trigger_value</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_trigger_value.png" alt="Auslöserdaten" style="max-width:280px;max-height:180px"> | Valeur/ancienne valeur, ID d'entité, ID/type de déclencheur, message MQTT/JSON et données d'événement. Données manquantes : `none`. |

Les déclencheurs natifs HA avancés sont classés directement sous **Déclencheurs**. Le déclencheur solaire dispose en outre d'un décalage optionnel en minutes. [Comparaison avec les déclencheurs ioBroker](/fr/projects/blocks-for-ha/time).

### Libellés, commentaires et MQTT depuis 0.1.59 {#beschriftungen-kommentar-und-mqtt-seit-0-1-59}

Les libellés standard et les fenêtres contextuelles (popups) accessibles via l'icône en forme d'engrenage suivent désormais la convention ioBroker/Blockly en DE/EN/FR : **Attributs / Attribut**, **Liste / Élément**, **connecter / Élément** et **le cas est / dans le cas de / default**. Les noms d'attributs sont modifiables dans la fenêtre contextuelle ; la branche « default » peut être ajoutée ou supprimée. Les libellés relatifs au texte, aux listes, aux mathématiques et à la logique ont été harmonisés. Les entrées HA (Home Assistant) supplémentaires, les affectations de variables immuables, les formats de date Python et la prochaine heure solaire restent clairement identifiables.

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Commentaire** · Système<br><code>ugso_comment</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_comment.png" alt="Kommentar" style="max-width:280px;max-height:180px"> | Note jaune, placée librement ou au sein d'une chaîne d'actions. Le JSON du projet conserve le texte et la position. Les commentaires actifs sont regroupés dans le YAML sous forme de lignes `#` avant l'automatisation ; lors de l'importation, ils sont réintégrés en tant que blocs de commentaires libres (y compris lors d'un ajout). Les positions initiales des commentaires dans le YAML ne sont pas conservées. Aucune action. |
| **Message MQTT** · Messages<br><code>ugso_mqtt_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_mqtt_action.png" alt="MQTT-Nachricht" style="max-width:280px;max-height:180px"> | Sujet (Topic), message, indicateur « Retain » et QoS 0/1/2. Entrées de type texte ou Jinja ; sortie native `mqtt.publish`. Pas de sélection d'instance. L'intégration MQTT de HA doit être configurée ; c'est HA qui effectue l'envoi. |

Depuis la version **0.1.58**, l'interface utilisateur s'inspire étroitement de celle d'ioBroker : les extensions s'effectuent exclusivement via l'icône en forme de roue dentée, sans boutons « + », « - » ou « S » supplémentaires. Cela s'applique également aux objets, aux listes, au texte, aux sélections conditionnelles et aux blocs parallèles. Le bloc compact ET/OU a été retiré du menu ; les projets existants restent lisibles. Les champs HA, les connexions et les fonctions YAML sont conservés. L'objectif est de conserver l'apparence familière d'ioBroker tout en offrant une prise en charge complète des automatisations HA.

### Messages depuis 0.1.48 {#nachrichten-seit-0-1-48}

Nouvelle catégorie **Messages**, incluant trois blocs (disponibles en DE/EN/FR). [Configuration, gestion des clés et envoi](/fr/projects/callmebot/).

Depuis **0.1.50**, ajout de **Signal · CallMeBot** avec sélection de profil dédiée. [Configurer l'application Signal](/fr/projects/callmebot-signal/).

| Bloc | Image | Fonction |
| --- | --- | --- |
| **WhatsApp · CallMeBot**<br><code>ugso_callmebot_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_callmebot_action.png" alt="CallMeBot" style="max-width:360px;max-height:180px"> | Profil du destinataire, texte/Jinja et niveau de journalisation. Envoi MQTT via l'application WhatsApp CallMeBot. Les clés restent dans le backend. |
| **Signal · CallMeBot**<br><code>ugso_callmebot_signal_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_callmebot_signal_action.png" alt="CallMeBot" style="max-width:360px;max-height:180px"> | Profil du destinataire, texte/Jinja et niveau de journalisation. Envoi MQTT via l'application Signal CallMeBot. Les clés restent dans le backend. |
| **Intégration WhatsApp**<br><code>ugso_whatsapp_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_whatsapp_action.png" alt="WhatsApp-Integration" style="max-width:360px;max-height:180px"> | `whatsapp.send_message` avec `number` ou `target`, ainsi que `notify.whatsapp`. Destinataire (sans le signe +), message, compte optionnel. Le jeton (token) doit être configuré une seule fois dans l'intégration HA. |

### Fonctionnalités depuis 0.1.47 {#funktionen-seit-0-1-47}

Le catalogue actuel comprend **169 types de blocs**. [Paramètres, exportation et limites](/fr/projects/blocks-for-ha/blockly-audit).

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Définir une fonction d'action**<br><code>procedures_defnoreturn</code> | <img src="/assets/blocks-for-ha/blocks/de/procedures_defnoreturn.png" alt="Aktionsfunktion definieren" style="max-width:280px;max-height:180px"> | Séquence HA réutilisable ; jusqu'à huit paramètres configurables via l'icône en forme d'engrenage. Définition située en dehors de l'automatisation. |
| **Appeler une fonction d'action**<br><code>procedures_callnoreturn</code> | <img src="/assets/blocks-for-ha/blocks/de/procedures_callnoreturn.png" alt="Aktionsfunktion aufrufen" style="max-width:280px;max-height:180px"> | Appel dynamique avec passage d'arguments. Exportable en tant que groupe de séquences HA avec ses propres liaisons de paramètres. |
| **Valeur de retour conditionnelle**<br><code>ugso_function_result</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_function_result.png" alt="Falls gib zurück sonst" style="max-width:280px;max-height:180px"> | Si / Valeur / Sinon ; seule la valeur sélectionnée est évaluée dans HA. Aucune séquence d'actions n'est exécutée. |

Depuis **0.1.45**, la boîte à outils ne contient plus d'entrées en double : les nombres se trouvent sous **Mathématiques**, le texte sous **Texte**, les couleurs sous **Couleur**, et les opérateurs ET/OU/NON (extensibles) sous **Logique**. La catégorie **Valeurs** ne contient désormais que les pourcentages. Les 163 types de blocs et les projets existants restent inchangés.

Depuis 0.1.17, les champs d'entités ouvrent une fenêtre de recherche. [Charger, sélectionner et saisir manuellement des entités](/fr/projects/blocks-for-ha/entities).

État au **0.1.44** : 163 types de blocs. Tous les types de blocs ont été vérifiés par rapport aux champs de sélection HA correspondants. Les images présentent les blocs UGSo tels qu'ils apparaissent réellement dans l'éditeur. Les variantes de menus déroulants ne sont pas comptabilisées comme des types de blocs supplémentaires. Guides : [Sélection d'entités](/fr/projects/blocks-for-ha/entities), [Date et heure](/fr/projects/blocks-for-ha/time), [Conversion](/fr/projects/blocks-for-ha/conversion).

Dans les thèmes Standard/Sombre, les déclencheurs sont orange, les conditions et la logique sont bleues, les valeurs sont vertes, les actions sont bleu turquoise et les objets sont marron. Les points de connexion latéraux sont typés ; les déclencheurs et les actions forment des chaînes verticales distinctes. Les identifiants d'entités peuvent être recherchés ou saisis manuellement.

### Couleurs et fonctions de valeur depuis 0.1.15 {#farben-und-wertfunktionen-seit-0-1-15}

[Utilisation, sortie HA et comparaison complète des sources](/fr/projects/blocks-for-ha/blockly-audit).

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Couleur aléatoire**<br><code>ugso_colour_random</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_colour_random.png" alt="Zufällige Farbe" style="max-width:280px;max-height:180px"> | Trois canaux RGB aléatoires (0–255). Générés à chaque évaluation ; non cryptographique. |
| **Couleur depuis RGB**<br><code>ugso_colour_rgb</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_colour_rgb.png" alt="Farbe aus RGB" style="max-width:280px;max-height:180px"> | Limite les pourcentages à la plage 0–100 et les convertit en canaux RGB. 100/50/0 donne [255,128,0]. |
| **Mélanger les couleurs**<br><code>ugso_colour_blend</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_colour_blend.png" alt="Farben mischen" style="max-width:280px;max-height:180px"> | Mélange RGB linéaire. Proportion de la couleur 2 comprise entre 0 et 1. Rouge/Bleu à 0,5 donne [128,0,128], sans correction gamma. |
| **Définir une fonction avec retour**<br><code>procedures_defreturn</code> | <img src="/assets/blocks-for-ha/blocks/de/procedures_defreturn.png" alt="Wertfunktion definieren" style="max-width:280px;max-height:180px"> | Éditeur Blockly original ; icône d'engrenage pour ajouter jusqu'à huit paramètres ; valeur de retour requise. Aucune action. Expansion Jinja lors de l'exportation. |
| **Appel de fonction (avec valeur de retour)**<br><code>procedures_callreturn</code> | <img src="/assets/blocks-for-ha/blocks/de/procedures_callreturn.png" alt="Wertfunktion aufrufen" style="max-width:280px;max-height:180px"> | Apparaît dynamiquement au sein des fonctions. Les entrées d'arguments suivent les paramètres. Le résultat est renvoyé sous forme de valeur ou de condition booléenne ; aucune récursion autorisée. |
| **Accesseur de paramètre (original)**<br><code>variables_get</code> | <img src="/assets/blocks-for-ha/blocks/de/variables_get.png" alt="Originaler Parameter-Getter" style="max-width:280px;max-height:180px"> | Accesseur Blockly original, accessible par exemple depuis le menu contextuel de la définition. Lit le paramètre dans le corps de la fonction ; sinon, lit une variable HA. L'accesseur spécifique reste utilisable. |

### Mathématiques, texte, listes et boucles de comptage depuis 0.1.14 {#mathematik-text-listen-und-zahlschleifen-seit-0-1-14}

[Blockly original / ioBroker / HA : correspondance, exemples et limites](/fr/projects/blocks-for-ha/collections).

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Arithmétique**<br><code>ugso_math_arithmetic</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_arithmetic.png" alt="Arithmetik" style="max-width:280px;max-height:180px"> | Effectue des calculs numériques : addition, soustraction, multiplication, division ou puissance. Aucune conversion automatique vers le texte ou le type booléen. |
| **Calcul sur un nombre unique**<br><code>ugso_math_single</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_single.png" alt="Einzelne Zahl berechnen" style="max-width:280px;max-height:180px"> | Racine carrée, valeur absolue, négation, logarithmes et fonctions exponentielles. Les valeurs non valides génèrent une erreur de modèle. |
| **Trigonométrie**<br><code>ugso_math_trig</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_trig.png" alt="Trigonometrie" style="max-width:280px;max-height:180px"> | Fonctions trigonométriques en degrés ; les fonctions inverses renvoient des degrés. HA utilise en interne les radians. |
| **Constantes**<br><code>ugso_math_constant</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_constant.png" alt="Konstanten" style="max-width:280px;max-height:180px"> | Constantes mathématiques finies. L'infini n'est pas proposé en tant que valeur numérique exportable. |
| **Propriétés des nombres**<br><code>ugso_math_property</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_property.png" alt="Zahleneigenschaften" style="max-width:280px;max-height:180px"> | Vérification des propriétés des nombres. Le diviseur n'apparaît que dans le cas d'une divisibilité ; un diviseur nul est invalide. |
| **Arrondis**<br><code>ugso_math_round</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_round.png" alt="Runden" style="max-width:280px;max-height:180px"> | Arrondit à 0–10 décimales près. HA/Jinja arrondit les valeurs se terminant par 0,5 vers le nombre pair ; les arrondis par excès ou par défaut suivent les fonctions `ceil` et `floor`. |
| **Opérations mathématiques sur une liste**<br><code>ugso_math_list</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_list.png" alt="Mathematik über Liste" style="max-width:280px;max-height:180px"> | Statistiques sur une liste de nombres ; l'option « élément aléatoire » accepte n'importe quel élément de la liste. Une somme vide vaut 0 ; les autres résultats vides valent `null`. |
| **Modulo**<br><code>ugso_math_modulo</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_modulo.png" alt="Modulo" style="max-width:280px;max-height:180px"> | Modulo selon Jinja. Si le dividende est négatif, le signe du résultat suit celui du diviseur, ce qui peut différer du comportement en JavaScript. |
| **Bornage**<br><code>ugso_math_clamp</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_clamp.png" alt="Begrenzen" style="max-width:280px;max-height:180px"> | Restreint une valeur numérique à un intervalle donné. Si les bornes sont inversées, elles sont triées au préalable. |
| **Nombre entier aléatoire**<br><code>ugso_math_random_int</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_random_int.png" alt="Ganzzahlige Zufallszahl" style="max-width:280px;max-height:180px"> | Inclut les deux bornes entières. Au maximum 10 000 valeurs possibles ; les bornes peuvent être inversées. |
| **Fraction aléatoire**<br><code>ugso_math_random_fraction</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_random_fraction.png" alt="Zufallsbruch" style="max-width:280px;max-height:180px"> | Valeur aléatoire par pas de 0,00001. Il ne s'agit pas d'un hasard cryptographique ; la valeur est recalculée à chaque évaluation. |
| **Angle atan2**<br><code>ugso_math_atan2</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_math_atan2.png" alt="Winkel atan2" style="max-width:280px;max-height:180px"> | Fonction d'angle à quatre quadrants issue du standard Blockly, en complément des illustrations présentées. |
| **Saut de ligne**<br><code>ugso_text_newline</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_newline.png" alt="Zeilenumbruch" style="max-width:280px;max-height:180px"> | Génère un véritable saut de ligne pour la concaténation de texte. |
| **Concaténer du texte**<br><code>ugso_text_join</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_join.png" alt="Text verknüpfen" style="max-width:280px;max-height:180px"> | Concatène de 0 à 100 valeurs sous forme de texte. L'icône en forme de roue dentée permet de modifier le nombre d'entrées. |
| **Ajouter au texte**<br><code>ugso_text_append</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_append.png" alt="Text anhängen" style="max-width:280px;max-height:180px"> | Ajoute un nouveau texte à une variable textuelle préalablement initialisée. Aucune écriture d'une entité HA. |
| **Longueur du texte**<br><code>ugso_text_length</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_length.png" alt="Textlänge" style="max-width:280px;max-height:180px"> | Nombre de points de code Unicode, et non d'unités de code UTF-16 JavaScript. |
| **Le texte est vide**<br><code>ugso_text_empty</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_empty.png" alt="Text ist leer" style="max-width:280px;max-height:180px"> | Vérifie si la longueur d'un texte est égale à 0. |
| **Le texte contient**<br><code>ugso_text_contains</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_contains.png" alt="Text enthält" style="max-width:280px;max-height:180px"> | Vérifie la présence d'une sous-chaîne, en tenant compte de la casse. |
| **Rechercher dans le texte**<br><code>ugso_text_index</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_index.png" alt="Text suchen" style="max-width:280px;max-height:180px"> | Position (indexée à partir de 1) ; renvoie 0 si non trouvé. Basé sur les points de code Unicode. |
| **Lire un caractère**<br><code>ugso_text_char</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_char.png" alt="Zeichen lesen" style="max-width:280px;max-height:180px"> | Récupère un caractère (indexé à partir de 1) depuis le début ou la fin, ou choisit le premier, le dernier ou un caractère aléatoire. Renvoie un texte vide si l'index est hors limites. |
| **Extrait de texte**<br><code>ugso_text_slice</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_slice.png" alt="Teiltext" style="max-width:280px;max-height:180px"> | Bornes inclusives, indexées à partir de 1. Des bornes invalides ou inversées renvoient un texte vide. |
| **Casse (majuscules/minuscules/titre)**<br><code>ugso_text_case</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_case.png" alt="Groß-/Klein-/Titelbuchstaben" style="max-width:280px;max-height:180px"> | Convertit le texte Unicode en majuscules, minuscules ou format « titre ». |
| **Supprimer les espaces**<br><code>ugso_text_trim</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_trim.png" alt="Leerraum entfernen" style="max-width:280px;max-height:180px"> | Supprime les espaces aux extrémités, y compris les tabulations et les sauts de ligne. |
| **Compter le texte**<br><code>ugso_text_count</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_count.png" alt="Text zählen" style="max-width:280px;max-height:180px"> | Compte les occurrences non chevauchantes ; un texte de recherche vide renvoie 0. |
| **Remplacer le texte**<br><code>ugso_text_replace</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_replace.png" alt="Text ersetzen" style="max-width:280px;max-height:180px"> | Remplace toutes les occurrences littérales (sans expression régulière). Un texte de recherche vide laisse le texte inchangé. |
| **Inverser le texte**<br><code>ugso_text_reverse</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text_reverse.png" alt="Text umkehren" style="max-width:280px;max-height:180px"> | Bloc Blockly standard supplémentaire. Inverse les points de code Unicode, et non les graphèmes composés. |
| **Répéter un élément de liste**<br><code>ugso_list_repeat</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_repeat.png" alt="Listenelement wiederholen" style="max-width:280px;max-height:180px"> | Nouvelle liste contenant une valeur répétée entre 0 et 10 000 fois. |
| **Rechercher un élément de liste**<br><code>ugso_list_index</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_index.png" alt="Listenelement suchen" style="max-width:280px;max-height:180px"> | Position indexée à partir de 1 ; renvoie 0 si l'élément est introuvable. Utilise l'égalité de type HA/Python plutôt que l'égalité par référence de JavaScript. |
| **Lire un élément de liste**<br><code>ugso_list_get</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_get.png" alt="Listenelement lesen" style="max-width:280px;max-height:180px"> | Lit un élément (indexé à partir de 1 depuis le début ou la fin, premier/dernier, ou aléatoire). Renvoie « null » si l'index est hors limites ou si la liste est vide. |
| **Définir/insérer un élément de liste**<br><code>ugso_list_set</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_set.png" alt="Listenelement setzen/einfügen" style="max-width:280px;max-height:180px"> | Crée une nouvelle liste avec une valeur remplacée ou insérée. Indexation à partir de 1 ; l'insertion est autorisée jusqu'à la position « longueur + 1 ». Un index invalide laisse la liste inchangée. |
| **Supprimer un élément de la liste**<br><code>ugso_list_remove</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_remove.png" alt="Listenelement entfernen" style="max-width:280px;max-height:180px"> | Renvoie une nouvelle liste sans cet élément. Index à partir de 1 ; un index invalide laisse la liste inchangée. |
| **Sous-liste**<br><code>ugso_list_slice</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_slice.png" alt="Teilliste" style="max-width:280px;max-height:180px"> | Copie d'une plage, bornes incluses, indexée à partir de 1. Des bornes inversées ou invalides produisent une liste vide. |
| **Diviser/Joindre une liste ou un texte**<br><code>ugso_list_split</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_split.png" alt="Liste/Text teilen/verbinden" style="max-width:280px;max-height:180px"> | Divise un texte selon un séparateur littéral, ou joint les éléments d'une liste. Un séparateur vide entraîne une division en caractères Unicode. |
| **Trier une liste**<br><code>ugso_list_sort</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_sort.png" alt="Liste sortieren" style="max-width:280px;max-height:180px"> | Nouvelle liste triée ; la liste originale reste inchangée. Le mode numérique exige des nombres, tandis que le mode texte convertit les éléments en texte. |
| **Inverser la liste**<br><code>ugso_list_reverse</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_reverse.png" alt="Liste umkehren" style="max-width:280px;max-height:180px"> | Nouvelle liste dans l'ordre inverse ; la liste originale est préservée. |
| **Boucle de comptage**<br><code>ugso_for_range</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_for_range.png" alt="Zählschleife" style="max-width:280px;max-height:180px"> | Bornes entières fixes ; la borne de fin est incluse si elle correspond au pas. Sens croissant ou décroissant déterminé automatiquement ; pas > 0 ; maximum 10 000 itérations. Correspond à `repeat.for_each` dans HA, avec une variable définie pour chaque itération. |
| **Pour chaque valeur avec variable**<br><code>ugso_foreach_variable</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_foreach_variable.png" alt="Für jeden Wert mit Variable" style="max-width:280px;max-height:180px"> | Correspond à `repeat.for_each` dans HA avec une variable nommée, définie à partir de `repeat.item` avant l'exécution du corps de la boucle. Éviter de réutiliser la même variable dans des boucles imbriquées. |

### Séquences, objets et listes depuis 0.1.13 {#ablaufe-objekte-und-listen-seit-0-1-13}

[ioBroker / Blockly original / HA natif : Comparaison et limites](/fr/projects/blocks-for-ha/flow).

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Pause**<br><code>ugso_pause</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_pause.png" alt="Pause" style="max-width:280px;max-height:180px"> | Durée exprimée en ms, secondes, minutes ou heures ; valeur constante ou calculée. Attente HA native. |
| **Attendre jusqu'à**<br><code>ugso_wait</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_wait.png" alt="Warte bis" style="max-width:280px;max-height:180px"> | Condition booléenne avec délai d'attente (timeout) et point d'ancrage pour la poursuite ; sans ce point d'ancrage, l'exécution s'arrête en cas de dépassement du délai. |
| **Arrêter cette exécution**<br><code>ugso_stop</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_stop.png" alt="Diesen Lauf stoppen" style="max-width:280px;max-height:180px"> | Motif et point d'ancrage d'erreur optionnel. Met fin à l'exécution complète, y compris au sein des boucles. |
| **Répéter un nombre de fois**<br><code>ugso_repeat</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_repeat.png" alt="Wiederhole Anzahl" style="max-width:280px;max-height:180px"> | Corps d'action pour `HA-repeat.count` ; `repeat.index` correspond à l'index (commençant à 1). |
| **Répéter tant que / jusqu'à**<br><code>ugso_repeat_while</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_repeat_while.png" alt="Wiederhole solange/bis" style="max-width:280px;max-height:180px"> | Entrée booléenne et corps d'action. « Tant que » vérifie la condition avant, « jusqu'à » après. Utiliser une pause dans le corps. |
| **Pour chaque élément**<br><code>ugso_foreach</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_foreach.png" alt="Für jeden Eintrag" style="max-width:280px;max-height:180px"> | Parcourt une liste ; valeur actuelle accessible via le modèle `repeat.item`, index via `repeat.index`. |
| **Nouvel objet**<br><code>ugso_object_new</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_object_new.png" alt="Neues Objekt" style="max-width:280px;max-height:180px"> | 0 à 100 attributs nommés (via l'icône engrenage/+−). Valeur de type dictionnaire ; ce n'est pas une entité HA. |
| **Attribut de l'objet**<br><code>ugso_object_get</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_object_get.png" alt="Attribut von Objekt" style="max-width:280px;max-height:180px"> | Lecture d'une clé ; renvoie « null » si la clé est absente. Nécessite un dictionnaire. |
| **L'objet possède l'attribut**<br><code>ugso_object_has</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_object_has.png" alt="Objekt hat Attribut" style="max-width:280px;max-height:180px"> | Test booléen sur la présence d'une clé dans un dictionnaire. |
| **Attributs de l'objet**<br><code>ugso_object_keys</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_object_keys.png" alt="Attribute des Objekts" style="max-width:280px;max-height:180px"> | Liste des clés (utilisable avec les blocs de type liste ou « pour chaque élément »). |
| **Définir un attribut dans une variable**<br><code>ugso_object_set</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_object_set.png" alt="Setze Attribut in Variable" style="max-width:280px;max-height:180px"> | Sélection de la variable et connexion de la valeur ; assigne une copie du dictionnaire avec une clé modifiée. L'élément doit être défini au préalable en tant qu'objet. |
| **Supprimer un attribut d'une variable**<br><code>ugso_object_remove</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_object_remove.png" alt="Entferne Attribut aus Variable" style="max-width:280px;max-height:180px"> | Nouvelle assignation sans la clé spécifiée. Aucune modification (mutation) d'autres variables ou attributs d'entité. |
| **Comparaison de plage**<br><code>ugso_logic_range</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_logic_range.png" alt="Bereichsvergleich" style="max-width:280px;max-height:180px"> | Utilisation indépendante de &lt; ou ≤ pour les bornes inférieure et supérieure ; accepte des nombres fixes ou des valeurs numériques dynamiques. |
| **Valeur de remplacement**<br><code>ugso_logic_default</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_logic_default.png" alt="Ersatzwert" style="max-width:280px;max-height:180px"> | Déclenchement si la valeur est nulle/non définie, vide, fausse ou égale à 0 ; le mode « null » considère les valeurs 0 et « faux » comme valides. |
| **Le cas est**<br><code>ugso_case</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_case.png" alt="Der Fall ist" style="max-width:280px;max-height:180px"> | 1 à 100 valeurs de cas (configurables via l'icône d'engrenage ou les boutons +/-) associées à des blocs d'action. Exécution lors de la première correspondance ; un bloc par défaut optionnel est disponible. |
| **Créer une liste**<br><code>ugso_list_new</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_new.png" alt="Liste erstellen" style="max-width:280px;max-height:180px"> | 0 à 100 éléments au choix, ajoutables via l'icône engrenage/+− ; prend en charge les valeurs imbriquées. |
| **Longueur de la liste**<br><code>ugso_list_length</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_length.png" alt="Listenlänge" style="max-width:280px;max-height:180px"> | Longueur d'une liste sous forme de valeur numérique (calculée à l'exécution). Les chaînes de caractères et les dictionnaires ne sont pas considérés comme des listes. |
| **La liste est vide**<br><code>ugso_list_empty</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_list_empty.png" alt="Liste ist leer" style="max-width:280px;max-height:180px"> | Vérification booléenne : la liste ne contient aucun élément. |

### Conversion depuis 0.1.12 {#konvertierung-seit-0-1-12}

[Guide, comparaison avec ioBroker et JSONata préconfiguré](/fr/projects/blocks-for-ha/conversion).

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Vers nombre**<br><code>ugso_convert_number</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_number.png" alt="Nach Zahl" style="max-width:280px;max-height:180px"> | HA float sans valeur de remplacement ; nombre complet avec point décimal. Valeur numérique utilisable pour les variables, les comparaisons et les calculs temporels. |
| **Vers valeur logique**<br><code>ugso_convert_boolean</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_boolean.png" alt="Nach Logikwert" style="max-width:280px;max-height:180px"> | HA bool ; valeurs booléennes ou textuelles reconnues. Sortie booléenne pour les conditions et la logique. |
| **Vers chaîne**<br><code>ugso_convert_string</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_string.png" alt="Nach String" style="max-width:280px;max-height:180px"> | Représentation textuelle Jinja d'une valeur ; aucune sérialisation JSON. |
| **Type de**<br><code>ugso_convert_type</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_type.png" alt="Typ von" style="max-width:280px;max-height:180px"> | HA typeof renvoie le nom du type Python, par ex. str, float, bool, dict. À partir de HA 2023.4. |
| **Vers date/heure**<br><code>ugso_convert_datetime</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_datetime.png" alt="Nach Datum/Zeit" style="max-width:280px;max-height:180px"> | Texte au format ISO ou secondes/millisecondes Unix convertis en heure locale HA. Sortie de type temporel (datetime). |
| **Date/Heure vers …**<br><code>ugso_convert_date_format</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_date_format.png" alt="Datum/Zeit nach …" style="max-width:280px;max-height:180px"> | Valeur de date, format, nombre Unix ou composante de date. La sélection modifie le type de sortie ; l'option « format personnalisé » affiche un champ texte. |
| **Formater une durée**<br><code>ugso_convert_duration</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_duration.png" alt="Zeitdifferenz formatieren" style="max-width:280px;max-height:180px"> | Durée en millisecondes ou en secondes convertie au format hh:mm:ss, hh:mm ou mm:ss. Le signe ainsi que les valeurs élevées d'heures ou de minutes sont conservés. |
| **JSON vers valeur**<br><code>ugso_convert_from_json</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_from_json.png" alt="JSON nach Wert" style="max-width:280px;max-height:180px"> | Convertit un texte JSON en objet, liste ou valeur unique. Un JSON invalide génère une erreur HA. |
| **Valeur vers JSON**<br><code>ugso_convert_to_json</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_convert_to_json.png" alt="Wert nach JSON" style="max-width:280px;max-height:180px"> | Sérialisation JSON avec une case à cocher pour l'indentation. Formater les valeurs de date au préalable. |

### Date et heure depuis 0.1.11 {#datum-und-zeit-seit-0-1-11}

Les blocs temporels violets utilisent un connecteur spécifique typé pour les valeurs de date. [Utilisation, cas limites et comparaison](/fr/projects/blocks-for-ha/time).

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Comparaison horaire**<br><code>ugso_time_compare</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_compare.png" alt="Uhrzeitvergleich" style="max-width:280px;max-height:180px"> | Heure fixe HH:mm/HH:mm:ss ; inférieur, supérieur, égal ou plage horaire. La borne de fin n'apparaît que pour les conditions « entre » ou « pas entre ». |
| **Comparaison horaire avec entrées**<br><code>ugso_time_compare_input</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_compare_input.png" alt="Uhrzeitvergleich mit Eingängen" style="max-width:280px;max-height:180px"> | Limites horaires définies via des blocs de texte. Si l'option est décochée, une entrée dédiée à la valeur de date/heure apparaît. Les plages horaires peuvent s'étendre au-delà de minuit. |
| **Heure actuelle (valeur de date/heure)**<br><code>ugso_time_now</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_now.png" alt="Aktuelle Zeit als Datumswert" style="max-width:280px;max-height:180px"> | Heure locale de Home Assistant (avec date et fuseau horaire) ; sortie de type « Time » utilisable pour des calculs ou du formatage. |
| **Heure calculée**<br><code>ugso_time_boundary</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_boundary.png" alt="Berechnete Zeit" style="max-width:280px;max-height:180px"> | Début de la journée, du jour suivant, de la semaine (lundi), du mois ou de l'année, selon l'heure locale de Home Assistant. |
| **Événement solaire**<br><code>ugso_time_sun</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_sun.png" alt="Nächste Sonnenzeit" style="max-width:280px;max-height:180px"> | Lever, coucher, crépuscule, zénith ou minuit solaire (basé sur `sun.sun`). Décalage en minutes ; peut être demain. |
| **Calculer le temps**<br><code>ugso_time_shift</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_shift.png" alt="Zeit berechnen" style="max-width:280px;max-height:180px"> | Valeur de date décalée d'un nombre en millisecondes, secondes, minutes, heures ou jours. |
| **Formater le temps**<br><code>ugso_time_format</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_format.png" alt="Zeit formatieren" style="max-width:280px;max-height:180px"> | Valeur de date formatée en heure, date, date/heure, format ISO avec fuseau horaire ou secondes Unix. |

### Autres blocs {#weitere-blocks}

| Bloc | Image dans l'éditeur | Description de la fonction |
| --- | --- | --- |
| **Automatisation**<br><code>ugso_automation</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_automation.png" alt="Automation" style="max-width:280px;max-height:180px"> | Cadre contenant des déclencheurs, une condition facultative et une chaîne d'actions. Le nom, l'ID, la description et le mode se trouvent en dehors du bloc. |
| **État atteint**<br><code>ugso_state_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_state_trigger.png" alt="Zustand erreicht" style="max-width:280px;max-height:180px"> | Se déclenche lorsque l'entité atteint l'état spécifié. Génère `trigger: state` avec `to`. |
| **Valeur numérique au-dessus/en dessous d'un seuil**<br><code>ugso_numeric_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_numeric_trigger.png" alt="Zahl über/unter Grenze" style="max-width:280px;max-height:180px"> | Se déclenche lors du franchissement d'une limite, et non en continu. Limite définie par une valeur numérique ; `trigger: numeric_state`. |
| **Heure**<br><code>ugso_time_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_time_trigger.png" alt="Uhrzeit" style="max-width:280px;max-height:180px"> | Déclencheur horaire quotidien, au format HH:MM ou HH:MM:SS ; `trigger: time`. |
| **Lever/Coucher du soleil**<br><code>ugso_sun_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_sun_trigger.png" alt="Sonnenaufgang/-untergang" style="max-width:280px;max-height:180px"> | Menu déroulant pour choisir entre le lever ou le coucher du soleil ; `trigger: sun`. |
| **Démarrage de HA**<br><code>ugso_start_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_start_trigger.png" alt="HA startet" style="max-width:280px;max-height:180px"> | Se déclenche au démarrage de Home Assistant ; `trigger: homeassistant`. |
| **L'état est**<br><code>ugso_state_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_state_condition.png" alt="Zustand ist" style="max-width:280px;max-height:180px"> | Condition booléenne : l'entité présente l'état spécifié ; `condition: state`. |
| **Comparaison numérique**<br><code>ugso_numeric_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_numeric_condition.png" alt="Zahlenvergleich" style="max-width:280px;max-height:180px"> | Condition booléenne basée sur un seuil (au-dessus/en dessous) ; `condition: numeric_state`. |
| **ET / OU / NON**<br><code>ugso_logic_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_logic_condition.png" alt="UND / ODER / NICHT" style="max-width:280px;max-height:180px"> | Combine 1 à 100 conditions. L'icône en forme d'engrenage permet d'ajouter, de supprimer et de réorganiser les entrées. `and`, `or`, `not`. |
| **Date du jour**<br><code>ugso_date_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_date_condition.png" alt="Datum heute" style="max-width:280px;max-height:180px"> | Sélection de date (est / à partir de / jusqu'à), année incluse. Le modèle HA compare la date actuelle selon le fuseau horaire de HA. Ne constitue pas un déclencheur en soi. |
| **Nombre**<br><code>ugso_number</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_number.png" alt="Zahl" style="max-width:280px;max-height:180px"> | Bloc de valeur numérique sans limite. Utilisable dans les seuils et les durées d'attente ; les règles de validation propres à ces éléments restent applicables. |
| **Pourcentage**<br><code>ugso_percent</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_percent.png" alt="Prozent" style="max-width:280px;max-height:180px"> | Curseur et saisie précise pour des valeurs entières de 0 à 100. Sortie numérique, par exemple pour un état de charge ou une luminosité. |
| **Texte**<br><code>ugso_text</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_text.png" alt="Text" style="max-width:280px;max-height:180px"> | Depuis 0.1.65, champ de saisie vide sur une seule ligne entre guillemets, sans ligne d’indication supplémentaire. Entrée valide la saisie. Les textes déjà enregistrés sont conservés lors de l’importation d’un projet ou de YAML, y compris les sauts de ligne. |
| **Couleur**<br><code>ugso_colour</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_colour.png" alt="Farbe" style="max-width:280px;max-height:180px"> | Sélecteur de couleur (format hexadécimal) ; disponible sous forme de liste RGB pour l'éclairage, les variables ou les calculs de couleurs. Sortie de type couleur/valeur ; ne peut pas être connectée à des entrées numériques fixes. |
| **Activer / Désactiver / Basculer**<br><code>ugso_switch_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_switch_action.png" alt="Ein / Aus / Umschalten" style="max-width:280px;max-height:180px"> | Action liée au domaine de l'entité : `turn_on`, `turn_off` ou `toggle`. L'entité doit prendre en charge l'action choisie. |
| **Action HA générique**<br><code>ugso_service_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_service_action.png" alt="Generische HA-Aktion" style="max-width:280px;max-height:180px"> | Nom de l'action, entité cible (facultatif) et données sous forme d'objet JSON. À utiliser pour les paramètres qui ne sont pas encore pris en charge par les blocs de fonctions prédéfinis. |
| **Attendre (secondes)**<br><code>ugso_delay_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_delay_action.png" alt="Warte Sekunden" style="max-width:280px;max-height:180px"> | Pause de 0 à 86 400 secondes entières. Entrée numérique avec valeur par défaut (shadow). |
| **Sortie de journal (Log)**<br><code>ugso_log_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_log_action.png" alt="Log-Ausgabe" style="max-width:280px;max-height:180px"> | Message texte et menu déroulant pour le niveau de gravité ; `system_log.write`. Les niveaux « Info » et « Debug » peuvent être filtrés dans HA. |
| **Contrôler un script HA**<br><code>ugso_script_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_script_action.png" alt="HA-Script steuern" style="max-width:280px;max-height:180px"> | Lancer sans attendre, arrêter, ou appeler directement en attendant la fin. `script.turn_on`, `script.turn_off` ou `script.name`. |
| **Mettre à jour une entité**<br><code>ugso_update_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_update_action.png" alt="Entität aktualisieren" style="max-width:280px;max-height:180px"> | `homeassistant.update_entity` demande une mise à jour. Ne modifie pas l'état ; la prise en charge dépend de l'intégration. |
| **Commander les assistants**<br><code>ugso_helper_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_helper_action.png" alt="Helfer steuern" style="max-width:280px;max-height:180px"> | Le type sélectionné (interrupteur/compteur/minuteur) détermine les actions disponibles. L’identifiant d’entité doit correspondre au type. Le minuteur utilise la durée existante ; les paramètres passent par l’action générique. |
| **Lumière avec couleur**<br><code>ugso_colour_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_colour_action.png" alt="Licht mit Farbe" style="max-width:280px;max-height:180px"> | Entité lumineuse, entrée Colour et luminosité de 0 à 100. Génère `light.turn_on` avec `rgb_color` et `brightness_pct`. L’appareil doit prendre en charge la couleur. |

Le bouton moins ou la désactivation de Sinon détache les blocs connectés sans les supprimer. Reconnectez-les ou retirez-les avant l’export YAML. Annuler rétablit les connecteurs et les connexions. Les valeurs fantômes réapparaissent lorsqu’un bloc de valeur qui les remplaçait est retiré.

### Blocs de variables et de modèles depuis 0.1.8 {#variablen-und-template-blocks-seit-0-1-8}

| Bloc | Image dans l'éditeur | Description de la fonction |
| --- | --- | --- |
| **Définir une variable**<br><code>ugso_variable_set</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_variable_set.png" alt="Variable setzen" style="max-width:280px;max-height:180px"> | Bloc d'action : définit la variable sélectionnée sur un nombre, un texte/modèle, un booléen ou null. Crée une action native HA `variables`. À placer avant toute opération de lecture ultérieure. |
| **Lire une variable**<br><code>ugso_variable_get</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_variable_get.png" alt="Variable lesen" style="max-width:280px;max-height:180px"> | Connecteur de chaîne latéral ; génère <code v-pre>{{ name }}</code> pour les messages de journalisation et les affectations de variables supplémentaires. Le menu déroulant permet de renommer ou de supprimer. |
| **Jinja – code personnalisé**<br><code>ugso_template</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_template.png" alt="Jinja – eigener Code" style="max-width:280px;max-height:180px"> | Modèle Jinja multiligne avec connecteur de chaîne pour les messages de journalisation ou les affectations de variables. HA évalue le modèle lors de son exécution ; le bloc lui-même ne l'exécute pas. |
| **Jinja – condition personnalisée**<br><code>ugso_template_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_template_condition.png" alt="Jinja – eigene Bedingung" style="max-width:280px;max-height:180px"> | Connecteur booléen pour les structures « seulement si », « si » et les groupes logiques. Génère `condition: template` avec `value_template`. Le résultat doit être évalué comme « vrai » (true) dans HA ; ne constitue pas un déclencheur en soi. |

### Utilisation des variables et des modèles (templates) {#variablen-und-templates-verwenden}

#### Incrémentation et décrémentation depuis 0.1.10 {#erhohen-und-verringern-seit-0-1-10}

| Bloc | Image dans l'éditeur | Description de la fonction |
| --- | --- | --- |
| **Incrémenter la variable de…**<br><code>ugso_variable_change</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_variable_change.png" alt="Erhöhe Variable um" style="max-width:280px;max-height:180px"> | Menu déroulant pour sélectionner la variable, champ de saisie numérique avec un pas par défaut de `1`. Ajoute la valeur du pas à la variable numérique préalablement définie. Des pas négatifs permettent de décrémenter la valeur ; `0` des pas décimaux sont également possibles. Utilise l'assignation de variables native de HA via Jinja. |

Dans le menu **Variables**, les options **Définir**, **Incrémenter** et **Lire la variable** apparaissent pour chaque variable créée. Exemple dans une séquence d'actions : **Définir test à 10 → Incrémenter test de 1 → Journaliser un message d'information avec la variable test**. Le message utilise alors la valeur `11`. Avec l'étape `-2`, la valeur `10` deviendrait `8`.

Avant toute incrémentation, la variable doit être définie en tant que nombre. Les variables inexistantes, le texte (y compris `"10"`), les valeurs booléennes ou `null` ne sont pas convertis automatiquement et ne sont pas initialisés avec `0` ; l'évaluation Jinja dans HA échouera alors. La simple création d'une variable ne lui attribue aucune valeur. Le format JSON intègre le bloc d'incrémentation ; notre format de sortie YAML spécifique est reconnu comme un bloc d'incrémentation lors de l'importation. Les autres modèles de calcul restent des blocs de type « template ». La discussion prévue concernant les variables typées reste en suspens.

Dans le menu **Variables → Créer une variable…**, créez par exemple `leistung`. Les noms peuvent contenir des lettres, des chiffres et `_`, mais ne doivent pas commencer par un chiffre. Placez le bloc « Définir » dans la section **Alors** et associez-y un nombre ou un modèle (template). Ensuite, insérez le bloc « Lire » dans une action de journalisation (log). La création seule n'attribue pas encore de valeur. Les variables sont valables pour la durée de l'exécution de l'automatisation HA ; elles ne remplacent pas les « assistants » (helpers) stockés de manière permanente.

Exemple : **Définir leistung (puissance) via un modèle (template)** avec <code v-pre>{{ states('sensor.leistung') | float(0) }}</code>, suivi d'un **message de journal (Log Info) : Variable de puissance**. HA lit le capteur au moment de l'affectation et utilise cette valeur à l'étape suivante. Une condition de type « template » peut, par exemple, vérifier <code v-pre>{{ states('sensor.leistung') | float(0) > 100 }}</code>.

Le renommage met à jour les blocs de variables associés. Les noms présents dans des textes Jinja saisis manuellement doivent être modifiés manuellement. Les variables d'action ne sont disponibles qu'après leur affectation ; elles ne sont donc pas accessibles dans les conditions d'automatisation situées en amont. La vérification des blocs porte sur la structure et le YAML, mais ne concerne ni la syntaxe Jinja ni l'existence des entités HA. L'importation prend en charge, pour chaque valeur de variable, les types suivants : texte/template, nombre, booléen ou « null ». Depuis 0.1.34, il est possible d'inclure plusieurs entrées au sein d'un bloc JSON commun. L'utilisation de listes ou d'objets comme valeurs, ainsi que la définition de variables au niveau de l'automatisation, restent proscrites. [Variables natives HA et validité](https://www.home-assistant.io/docs/scripts/#define-variables).

### Blocs logiques depuis 0.1.9 {#logik-blocks-seit-0-1-9}

Depuis **0.1.57**, les entrées des groupes ET/OU extensibles sont disposées côte à côte, avec les opérateurs « et » ou « ou » insérés entre elles. Le menu de sélection ne propose que les options « et / ou / non ». Dans la fenêtre contextuelle (accessible via l'icône en forme de roue dentée), les blocs constitutifs affichent l'opérateur correspondant au lieu du terme générique « Condition » (y compris en anglais et en français). La logique de liaison propre à HA demeure inchangée.

Le bloc conditionnel (« Si ») extensible est également disponible ici (voir **0.1.56**). Les éléments de logique sont affichés en bleu (standard/foncé), et les objets en marron. [Couleurs et extensibilité](/fr/projects/blocks-for-ha/themes).

| Bloc | Visuel dans l'éditeur | Description fonctionnelle |
| --- | --- | --- |
| **Si / sinon si / sinon**<br><code>ugso_if_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_if_action.png" alt="Falls / sonst falls / sonst" style="max-width:280px;max-height:180px"> | L'icône en forme de roue dentée permet d'ajouter, de supprimer ou de réorganiser les branches « sinon si », ainsi que d'ajouter une branche « sinon ». `if` ou `choose` : la première branche dont la condition est remplie est exécutée. |
| **Comparaison**<br><code>ugso_compare</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_compare.png" alt="Vergleich" style="max-width:280px;max-height:180px"> | Compare deux valeurs à l'aide des opérateurs =, ≠, &lt;, ≤, &gt; ou ≥. Permet de connecter des nombres, du texte, des variables ou des expressions de modèle (template) individuelles. Renvoie une valeur booléenne ; le résultat peut être utilisé comme condition dans un modèle HA (Home Assistant) ou comme valeur de variable. |
| **ET / OU (format compact)**<br><code>ugso_binary_logic</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_binary_logic.png" alt="UND ODER kompakt" style="max-width:280px;max-height:180px"> | Réservé aux projets existants ; ce bloc a été retiré du sélecteur. Utilisez plutôt le groupe extensible ET/OU. |
| **NON**<br><code>ugso_not</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_not.png" alt="NICHT" style="max-width:280px;max-height:180px"> | Nie une condition booléenne. Utilise un groupe de conditions natif HA (`not`) comme condition, et une valeur Jinja (`not`) comme variable. |
| **vrai / faux**<br><code>ugso_boolean</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_boolean.png" alt="wahr falsch" style="max-width:280px;max-height:180px"> | Constante booléenne avec menu déroulant. Pour les conditions et les variables ; l'affectation génère de véritables valeurs booléennes YAML. |
| **null**<br><code>ugso_null</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_null.png" alt="null" style="max-width:280px;max-height:180px"> | Aucune valeur. Les variables reçoivent la valeur YAML `null`, et les expressions Jinja la valeur `none`. Ni `0` ni `falsch` ; ne constitue pas un bloc de condition booléenne. |
| **Si → alors valeur → sinon valeur**<br><code>ugso_ternary</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ternary.png" alt="Bedingte Wertauswahl" style="max-width:280px;max-height:180px"> | Sélectionne l'une des deux valeurs en fonction d'une condition booléenne. Pour les variables, les messages de journalisation et les comparaisons ; génère une expression Jinja et ne contient pas de chaîne d'actions. |

**Exemple :** Dans la chaîne d'actions, définissez d'abord `leistung`. Ensuite, utilisez **Définir le message sur « Si »**, avec le test **Comparaison : variable puissance > nombre 100**, la valeur « alors » définie sur le texte **Puissance élevée**, et la valeur « sinon » définie sur le texte **Puissance faible**. Enfin, utilisez **Journaliser info : message (variable « message »)**. HA effectue l'évaluation lors de l'exécution.

Les comparaisons n'effectuent pas de conversion automatique de type : le nombre `20` diffère du texte `"20"`. Si nécessaire, convertissez les états des capteurs dans le modèle (template) à l'aide de `float` ou `int`. Dans un champ d'expression, une seule sortie Jinja est autorisée, par exemple : <code v-pre>{{ states('sensor.leistung') | float(0) }}</code>. Les instructions multilignes et le texte mixte restent utilisables dans un bloc de valeur de modèle (template) dédié. Les sélections de valeurs dynamiques ne sont pas conçues pour servir de limites numériques fixes ou de durées d'attente.

Les projets JSON préservent les formes des blocs et leurs connexions. Le format YAML conserve la sémantique native : lors de la réouverture, les comparaisons et les sélections de valeurs apparaissent sous forme de blocs modèles (templates), tandis que les opérateurs ET/OU/NON sont représentés par des groupes de conditions. [Conditions logiques HA](https://www.home-assistant.io/docs/scripts/conditions/#logical-conditions).

### Plugins originaux et intégration {#originalplugins-und-einbindung}

Les six plugins d’origine précédents sont fixés à **13.2.0** ; les quatre plugins de thèmes/zoom et la recherche dans l’espace de travail sont fixés à **13.3.0**. Ils sont fournis localement avec Blockly **13.3.0**. Licence : Apache-2.0. Les liens suivants mènent directement aux dépôts d’origine. Nos blocs HA, adaptateurs YAML et composants configurables par engrenage sont du code UGSo original.

| Plugin original | Utilisation / État |
| --- | --- |
| [workspace-search](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/workspace-search) | Permet de localiser les blocs déjà placés dans l'espace de travail ; distinct de la recherche dans la boîte à outils (toolbox). Disponible depuis 0.1.21. |
| [toolbox-search](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/toolbox-search) | Recherche de blocs située en bas du menu ; les résultats conservent leurs menus déroulants et leurs blocs par défaut (shadow blocks). |
| [field-multilineinput](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-multilineinput) | Intégré au bloc texte ; les sauts de ligne sont préservés dans le projet et dans le format YAML. |
| [field-slider](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-slider) | Intégré au bloc pourcentage ; plage de 0 à 100 avec saisie numérique précise. |
| [field-colour](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-colour) | Dans le bloc de couleur ; le code hexadécimal est converti en format RVB pour l'action d'éclairage. Aléatoire/RVB/Mélange disponibles depuis 0.1.15 via des générateurs HA dédiés. |
| [theme-dark](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-dark) | Espace de travail sombre et sélection de blocs ; fait partie de la sélection de thèmes enregistrée. |
| [theme-modern](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-modern) | Palette originale avec des bordures plus marquées ; blocs personnalisés via les styles de thème. |
| [theme-tritanopia](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-tritanopia) | Palette originale pour les groupes standard, couleurs étendues UGSo adaptées et contrastes de texte adaptatifs. |
| [zoom-to-fit](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/zoom-to-fit) | Bouton « Ajuster à l'écran » ajouté à côté des commandes de zoom ; accessible également au clavier. |
| [field-date](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-date) | Dans la comparaison de dates ; une sous-classe UGSo sécurise l'appel différé du calendrier. |
| [field-dependent-dropdown](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-dependent-dropdown) | Dans le bloc « assistant » (helper) ; le type d'assistant détermine les actions. Pas de sélection HA en temps réel. |
| [block-plus-minus](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/block-plus-minus) | Principe d'interaction implémenté dans des blocs HA personnalisés ; le plugin original n'est pas installé. L'icône en forme de roue dentée reste disponible. |
| [block-dynamic-connection](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/block-dynamic-connection) | Pas encore intégré. Des connecteurs à extension automatique, des liaisons textuelles et des listes sont prévus. |

La sélection de la couleur utilise en outre la dépendance indirecte [field-grid-dropdown](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/field-grid-dropdown). La sortie HA est générée par nos soins ; les générateurs JavaScript fournis ne sont pas utilisés.

[Vers la vue d'ensemble](/fr/projects/blocks-for-ha/)

Des blocs personnalisés, introduits depuis 0.1.18, viennent compléter les 163 types natifs. [Éditeur](/fr/projects/blocks-for-ha/custom-blocks) et [catalogue de paquets](/fr/projects/blocks-for-ha/catalog/).

### Identifiants de déclenchement (Trigger IDs) et cibles multiples {#trigger-ids-und-mehrere-ziele}

À partir de **0.1.28** : les listes d'états sont désormais prises en charge via des **états définis sous forme de liste JSON** (par ex. `["1_single","1_double"]`) ; des identifiants de déclenchement (« trigger IDs ») facultatifs sont disponibles pour tous les déclencheurs standard ; le critère **« Déclenché par ID »** (« Triggered by ID ») constitue désormais une condition de déclenchement native (prenant en charge un identifiant unique ou une liste JSON). Les actions générales dans Home Assistant (HA) acceptent désormais des **cibles définies sous forme de liste JSON**, permettent l'ajout de métadonnées facultatives et acceptent explicitement des objets de données vides. Les interrupteurs à quatre boutons, dotés de quatre branches `choose`, peuvent désormais être importés intégralement.

**Automatisation individuelle · Éditeur HA** : la génération d'un élément `id` au niveau racine n'est plus effectuée. Les identifiants de déclenchement (« trigger IDs ») sont préservés. Le projet ainsi que la **liste dans `automations.yaml`** conservent tout identifiant d'automatisation existant.

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Déclenché par ID** (« Triggered by ID ») <br> <code> ugso_trigger_condition </code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_trigger_condition.png" alt="Ausgelöst durch ID" style="max-width:280px;max-height:180px"> | `condition: trigger` · `id` |

[Home Assistant : Identifiants de déclenchement (« Trigger IDs »)](https://www.home-assistant.io/docs/automation/trigger/#trigger-id) · [Condition de déclenchement](https://www.home-assistant.io/docs/scripts/conditions/#trigger-condition)

### Pompes de piscine, événements et paramètres temporels multiples {#poolpumpen-ereignisse-und-mehrere-uhrzeiten}

À partir de **0.1.30** : un déclencheur temporel peut désormais accepter plusieurs heures fixes via des **heures définies sous forme de liste JSON** (par ex. `["10:00:00","13:00:00","19:00:00"]`). L'option **« Tout changement »** (« Any change ») au sein d'un déclencheur basé sur l'état omet le paramètre `to` ; l'utilisation d'**entités définies sous forme de liste JSON** permet de surveiller plusieurs entités simultanément. Sans `to`, Home Assistant (HA) réagira également aux changements d'attributs. Le déclencheur d'événement (« event trigger ») prend en charge, par exemple, `timer.finished` ainsi qu'un filtre de données JSON facultatif. La condition temporelle native (« time condition ») conserve `before`/`after` tels quels ; elle gère des plages horaires fixes — incluant l'heure de début et excluant l'heure de fin — même lorsqu'elles s'étendent au-delà de minuit. Des heures de début et de fin identiques correspondent à une durée couvrant « toute la journée ». Les outils d'assistance temporelle (« time helpers »), les modèles temporels (« time templates ») et les filtres par jour de la semaine ne sont actuellement pas pris en charge pour l'importation. L'automatisation complète de la pompe de piscine — incluant son modèle de minuterie (« timer template ») multiligne et l'élément imbriqué `choose` — est préservée.

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Déclencheur d'événement** <br> <code> `ugso_event_trigger` </code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_event_trigger.png" alt="Ereignis-Auslöser" style="max-width:280px;max-height:180px"> | `trigger: event` · `event_type` · `event_data` |
| **Condition temporelle native HA** <br> <code> `ugso_native_time_condition` </code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_native_time_condition.png" alt="Native HA-Zeitbedingung" style="max-width:280px;max-height:180px"> | `condition: time` · `before` · `after` |

[Home Assistant : déclencheurs](https://www.home-assistant.io/docs/automation/trigger/) · [Condition temporelle](https://www.home-assistant.io/docs/scripts/conditions/#time-condition)

### Température modifiée {#temperatur-geandert}

Depuis **0.1.31**, le nouveau bloc prend en charge le déclencheur natif `temperature.changed`. Cible (JSON) : `entity_id` sous forme de texte ou de liste. Seuil (JSON) : type `any`, `above`, `below`, `between` ou `outside`. `any` ne nécessite que le type ; `above`/`below` requièrent une valeur (`value`), tandis que `between`/`outside` nécessitent `value_min` et `value_max`. Nombres : valeur numérique accompagnée de son unité de mesure (`unit_of_measurement`, ex. °C/°F). Références : entité (`sensor`, `number` ou `input_number`). Un identifiant de déclencheur (*Trigger ID*) est disponible en option. Depuis 0.1.39, il est également possible d'importer la zone, l'appareil, l'étage et le libellé (*label*). Les sujets MQTT (*topics*), les paramètres `qos`/`retain`/`evaluate_payload` ainsi que les charges utiles (*payloads*) JSON/Jinja multilignes sont conservés.

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Température modifiée**<br><code>ugso_temperature_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_temperature_trigger.png" alt="Temperatur geändert" style="max-width:280px;max-height:180px"> | `temperature.changed` |

[Home Assistant : `temperature.changed`](https://www.home-assistant.io/triggers/temperature.changed/)

### Calendrier et variables de réponse {#kalender-und-antwortvariablen}

**0.1.32 :** `calendar.event_started` / `calendar.event_ended`. Cible : objet JSON avec `entity_id` sous forme de texte ou de liste. Les options sont facultatives : `offset` (jours, heures, minutes et secondes, combinables) ou `HH:MM:SS` ; `offset_type` correspond à `before` ou `after`. Le décalage nul, les options omises et l'ID de déclencheur optionnel sont conservés.

Le champ **Variable de réponse (optionnel)** dans le bloc **Action HA** génère `response_variable` ; par exemple, `termine` pour `calendar.get_events`. Si le champ est laissé vide, il est omis dans le code YAML. L'automatisation complète pour les jours fériés/vacances intègre les deux calendriers, le démarrage de Home Assistant, les variables `zeitpunkt`/`termin_aktiv`, des modèles Jinja multilignes, les structures `choose`/`default` ainsi que le mode `queued`. Home Assistant traite les calendriers et les modèles.

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Événement de calendrier commence/se termine**<br><code>ugso_calendar_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_calendar_trigger.png" alt="Kalendertermin beginnt/endet" style="max-width:280px;max-height:180px"> | calendar.event_started / calendar.event_ended |

[Home Assistant : calendar.event_started](https://www.home-assistant.io/triggers/calendar.event_started/) · [calendar.event_ended](https://www.home-assistant.io/triggers/calendar.event_ended/) · [calendar.get_events](https://www.home-assistant.io/actions/calendar.get_events/)

### Déclencheurs numériques avec durée de maintien {#numerische-ausloser-mit-haltezeit}

Depuis **0.1.33**, le déclencheur **Valeur au-dessus/en dessous d'un seuil** prend en charge plusieurs entités : activez l'option **Entités sous forme de liste JSON** et saisissez, par exemple, `["sensor.temp_1","sensor.temp_2"]`. Si cette option n'est pas cochée, l'entité unique reste active. L'utilisation de **Haltezeit (JSON)** génère l'élément optionnel `for` : par exemple `{"hours":0,"minutes":1,"seconds":0}`, `60` ou `"00:01:00"`. Les combinaisons de jours/heures/minutes/secondes/millisecondes, les entrées nulles ainsi que les modèles de sortie HA sont conservés. Si la case est décochée, `for` est omis. Par ailleurs, une seule limite numérique fixe (above ou below) est autorisée ; l'identifiant de déclencheur (trigger ID) et les branches « choose » sont préservés.

Home Assistant déclenche une action après le franchissement d'un seuil, à condition que la valeur demeure de ce côté du seuil pendant toute la durée définie (temps de maintien). Le redémarrage de Home Assistant ou le rechargement des automatisations réinitialise le décompte de ce temps de maintien. [Home Assistant : numeric_state](https://www.home-assistant.io/triggers/numeric_state/).

### Variables multiples dans une seule action {#mehrere-variablen-in-einer-aktion}

Depuis la version **0.1.34**, un bloc unifié **Définir des variables (JSON)** est disponible dans le menu **Variables**. L'objet JSON peut contenir entre 1 et 100 noms de variables, avec des valeurs pouvant être du texte, des modèles (templates) Home Assistant, des nombres, des booléens ou `null`. Les entrées multiples sont traitées comme une action native unique (`variables`), en préservant l'ordre défini. Les affectations individuelles peuvent toujours être effectuées via le bloc « Définir une variable » existant. Depuis la version 0.1.39, la prise en charge des listes/objets et des variables au niveau de l'automatisation a également été ajoutée ; voir [Extensions HA et Jinja](/fr/projects/blocks-for-ha/advanced). Les noms et les modèles (templates) contenus dans le JSON doivent être modifiés directement ; leur renommage via la boîte de dialogue Blockly ne mettra pas à jour le texte JSON brut. Lors de l'importation, ces noms sont également enregistrés dans Blockly.

L'exemple de temporisateur inclut les heures/minutes (h/m), les entités surveillées, la condition et le mode `restart`. Si des conditions sont absentes, elles sont ajoutées sous forme de liste vide.

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Définir des variables (JSON)**<br><code>ugso_variables_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_variables_action.png" alt="Variablen setzen (JSON)" style="max-width:280px;max-height:180px"> | Variables avec champs de valeur individuels ; listes et objets au format JSON ; nouveaux noms via des options supplémentaires. |

[Home Assistant : variables](https://www.home-assistant.io/docs/scripts/#variables)

### Durée d'attente sous forme de chaîne de caractères temporelle ou de modèle (template) {#wartezeit-als-zeittext-oder-template}

À partir de la version **0.1.35**, les blocs intègrent nativement des chaînes de caractères temporelles (format `delay`) dans le nouveau bloc, sous la section **Timeouts** (délais d'attente). Exemples : `00:00:02`, `01:30` (une heure et 30 minutes), `00:00:00.250`, ou encore un modèle (template) de sortie Home Assistant. La chaîne temporelle est conservée sous forme de texte dans le code YAML et dans le projet enregistré. Une durée d'attente prolonge l'exécution en cours dans Home Assistant ; les actions suivantes sont déclenchées après cette période. Les blocs existants, basés sur les secondes ou d'autres unités, restent disponibles. Cette amélioration concerne `delay`, mais ne s'applique pas au délai d'attente du bloc « attendre jusqu'à » (« wait until »).

L'exemple de réinitialisation de temporisateur (« timer-reset ») commence par désactiver `timer_reset`, attend deux secondes, puis désactive les deux entités cibles. L'identifiant d'entité `input_boolean.timer_running` est conservé tel quel, conformément à la configuration d'origine.

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Attente (Chaîne temporelle / Modèle)** <br> <code> `ugso_delay_text` </code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_delay_text.png" alt="Warte Zeittext / Template" style="max-width:280px;max-height:180px"> | Chaîne temporelle native / Modèle (template) Home Assistant. |

[Home Assistant : délai (delay)](https://www.home-assistant.io/docs/scripts/#wait-for-time-to-pass-delay)

### Noms d'actions Home Assistant dynamiques {#dynamische-ha-aktionsnamen}

À partir de la version **0.1.36**, le premier champ du bloc **Action HA** accepte soit un nom d'action statique, soit un modèle (template) Jinja. Ce champ prend en charge la saisie sur plusieurs lignes. Il est ainsi possible d'utiliser, par exemple, `input_boolean.turn_on`, `input_boolean.turn_` accompagné d'une expression Jinja, ou encore une structure complète de type `if/else`. Les paramètres « cible » (target), « données » (data), « métadonnées » (metadata) et la variable de réponse restent dans leurs champs dédiés respectifs. Le modèle — incluant ses sauts de ligne — est préservé lors de l'importation, de l'enregistrement du projet et de l'exportation au format YAML.

Dans l'exemple lié à Shelly, l'action composée `input_boolean.turn_` (associée à une requête d'état) est conservée, tout comme les éventuelles branches `choose` imbriquées. Home Assistant n'évalue le nom de l'action qu'au moment de son exécution ; celui-ci doit correspondre à un nom de service valide. Le système vérifie la validité des noms d'actions statiques et la présence des délimiteurs de modèles, mais il ne contrôle ni la syntaxe Jinja ni les résultats obtenus lors de l'exécution. Les entités cibles doivent impérativement être des identifiants fixes ; l'utilisation de modèles pour définir des objets de données complets n'est pas prise en charge par cette amélioration.

[Home Assistant : sélection d'une action via un modèle (template)](https://www.home-assistant.io/docs/scripts/perform-actions/#choosing-the-action-with-a-template)


### Déclencheur basé sur un motif temporel (Time Pattern Trigger) {#zeitmuster-ausloser}

Dans la section **Déclencheurs** (Triggers), un bloc natif `time_pattern` est désormais disponible à partir de la version **0.1.37**. Le champ JSON peut, par exemple, contenir `{"seconds":"/30"}` pour déclencher une action aux secondes 0 et 30 de chaque minute. Les champs `hours`, `minutes` et `seconds` sont facultatifs ; toutefois, au moins l'un d'entre eux doit être renseigné. Les valeurs acceptées sont fixes : heures de 0 à 23, minutes/secondes de 0 à 59, exprimées sous forme numérique ou textuelle (sans zéro non significatif en début de nombre). `*` correspond à n'importe quelle valeur, tandis que `/n` correspond aux valeurs divisibles par *n* (où *n* > 0, dans la plage autorisée). Les unités et types de données (nombre/texte) manquants restent inchangés ; Home Assistant applique ses valeurs par défaut lors de l'exécution. Un identifiant de déclencheur (trigger ID) facultatif peut également être spécifié.

L'automatisation LCD, qui comprend quatre actions `input_text.set_value` et une action `mode: restart`, a été entièrement vérifiée : la syntaxe Jinja, le formatage, la troncature du texte, le remplissage (padding) et les sauts de ligne sont tous préservés. Home Assistant gère l'exécution des modèles (templates) et la planification.

| Bloc | Type |
| --- | --- |
| ![Modèle temporel (JSON)](/assets/blocks-for-ha/blocks/de/ugso_time_pattern_trigger.png) | `ugso_time_pattern_trigger` |

[Home Assistant : time_pattern](https://www.home-assistant.io/triggers/time_pattern/).


### Entités cibles dynamiques {#dynamische-zielentitaten}

À partir de **0.1.39**, le champ **Cible** (Target) dans l'**action HA** générique accepte soit un identifiant d'entité fixe, soit un modèle (template) HA — par exemple, <code v-pre>{{ ziel_tv }}</code>. La fenêtre de sélection des entités propose un champ de saisie multiligne à cet effet. La liste des cibles au format JSON peut également contenir un mélange d'identifiants fixes et de modèles. La syntaxe Jinja demeure intacte et est évaluée exclusivement par Home Assistant. Les cibles dynamiques sont représentées au sein de l'action HA générique lors de l'importation ; des blocs de commutation spécialisés ne seraient pas en mesure de déterminer le domaine de manière fiable.

L'automatisation de la télévision dans la chambre, incluant une variable multiligne pour le mode été, des créneaux horaires à 21h30 et 00h30, ainsi que deux branches de type « choose », a été vérifiée. Les modèles de destination, le contenu des variables et les conditions temporelles sont conservés lors de l'importation, du rechargement du projet et de l'exportation. Les champs de déclenchement et de condition liés aux identifiants d'entités (entity IDs) exigent toujours des identifiants fixes.

[Home Assistant : modèles (templates) dans les cibles d'action](https://www.home-assistant.io/docs/scripts/perform-actions/#setting-targets-and-options-with-a-template).


### Extensions HA et Jinja depuis 0.1.39 {#ha-erweitert-und-jinja-seit-0-1-39}

[Instructions / Guide](/fr/projects/blocks-for-ha/advanced).

| Bloc | Image | Fonction |
| --- | --- | --- |
| **HA state**<br><code>ugso_ha_state_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_state_trigger.png" alt="HA state" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est vérifiée ; il convient de contrôler l'intégration et l'exécution dans HA. |
| **HA numeric_state**<br><code>ugso_ha_numeric_state_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_numeric_state_trigger.png" alt="HA numeric_state" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est vérifiée ; il convient de contrôler l'intégration et l'exécution dans HA. |
| **HA time**<br><code>ugso_ha_time_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_time_trigger.png" alt="HA time" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est en cours de vérification ; vérifier l'intégration et l'exécution dans HA. |
| **HA sun**<br><code>ugso_ha_sun_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_sun_trigger.png" alt="HA sun" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est en cours de vérification ; vérifier l'intégration et l'exécution dans HA. |
| **HA homeassistant**<br><code>ugso_ha_homeassistant_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_homeassistant_trigger.png" alt="HA homeassistant" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est en cours de vérification ; vérifier l'intégration et l'exécution dans HA. |
| **HA mqtt**<br><code>ugso_ha_mqtt_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_mqtt_trigger.png" alt="HA mqtt" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est en cours de vérification ; vérifier l'intégration et l'exécution dans HA. |
| **HA template**<br><code>ugso_ha_template_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_template_trigger.png" alt="HA template" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est en cours de vérification ; vérifier l'intégration et l'exécution dans HA. |
| **HA webhook**<br><code>ugso_ha_webhook_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_webhook_trigger.png" alt="HA webhook" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est vérifiée ; veuillez contrôler l'intégration et l'exécution dans HA. |
| **HA zone**<br><code>ugso_ha_zone_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_zone_trigger.png" alt="HA zone" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est vérifiée ; veuillez contrôler l'intégration et l'exécution dans HA. |
| **HA device**<br><code>ugso_ha_device_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_device_trigger.png" alt="HA device" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est vérifiée ; tester l'intégration et l'exécution dans HA. |
| **HA tag**<br><code>ugso_ha_tag_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_tag_trigger.png" alt="HA tag" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est vérifiée ; tester l'intégration et l'exécution dans HA. |
| **HA conversation**<br><code>ugso_ha_conversation_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_conversation_trigger.png" alt="HA conversation" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est vérifiée ; tester l'intégration et l'exécution dans HA. |
| **HA geo_location**<br><code>ugso_ha_geo_location_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_geo_location_trigger.png" alt="HA geo_location" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est vérifiée ; tester l'intégration et l'exécution dans HA. |
| **HA calendar**<br><code>ugso_ha_calendar_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_calendar_trigger.png" alt="HA calendar" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est vérifiée ; tester l'intégration et l'exécution dans HA. |
| **Événement HA**<br><code>ugso_ha_event_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_event_trigger.png" alt="HA event" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est vérifiée ; tester l'intégration et l'exécution dans HA. |
| **Déclencheur HA (avancé)**<br><code>ugso_ha_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_trigger.png" alt="HA-Auslöser (erweitert)" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est vérifiée ; tester l'intégration et l'exécution dans HA. |
| **Condition HA (avancée)**<br><code>ugso_ha_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_condition.png" alt="HA-Bedingung (erweitert)" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est vérifiée ; tester l'intégration et l'exécution dans HA. |
| **Étape HA (avancée)**<br><code>ugso_ha_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_ha_action.png" alt="HA-Schritt (erweitert)" style="max-width:280px;max-height:180px"> | Entrées HA étiquetées et options JSON supplémentaires. La structure prise en charge est vérifiée ; tester l'intégration et l'exécution dans HA. |
| **Action HA – Type de cible – Cible – Options d'étape**<br><code>ugso_target_action</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_target_action.png" alt="HA-Aktion Zielart Ziel Daten Schrittoptionen" style="max-width:280px;max-height:180px"> | Champs HA avancés ou Jinja natif. La structure prise en charge est vérifiée ; veuillez contrôler l'intégration et l'exécution dans HA. |
| **Utiliser les options de cible de l'intégration HA**<br><code>ugso_integration_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_integration_trigger.png" alt="HA-Integration Ziel Optionen verwenden" style="max-width:280px;max-height:180px"> | Champs HA avancés ou Jinja natif. La structure prise en charge est vérifiée ; veuillez contrôler l'intégration et l'exécution dans HA. |
| **Groupe d'actions**<br><code>ugso_sequence</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_sequence.png" alt="Aktionsgruppe" style="max-width:280px;max-height:180px"> | Champs HA étendus ou Jinja original. La structure prise en charge est vérifiée ; tester l'intégration et l'exécution dans HA. |
| **Parallèle (Branche 1, Branche 2)**<br><code>ugso_parallel</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_parallel.png" alt="Parallel Zweig 1 Zweig 2" style="max-width:280px;max-height:180px"> | Champs HA étendus ou Jinja original. La structure prise en charge est vérifiée ; tester l'intégration et l'exécution dans HA. |
| **Options « Attendre un déclencheur »**<br><code>ugso_wait_trigger</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_wait_trigger.png" alt="Warte auf Auslöser Optionen" style="max-width:280px;max-height:180px"> | Champs HA étendus ou Jinja original. La structure prise en charge est vérifiée ; tester l'intégration et l'exécution dans HA. |
| **Continuer uniquement si**<br><code>ugso_condition_step</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_condition_step.png" alt="Nur weiter wenn" style="max-width:280px;max-height:180px"> | Champs HA étendus ou Jinja original. La structure prise en charge est vérifiée ; tester l'intégration et l'exécution dans HA. |
| **Données de déclenchement d'événement**<br><code>ugso_fire_event</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_fire_event.png" alt="Ereignis auslösen Daten" style="max-width:280px;max-height:180px"> | Champs HA étendus ou Jinja original. La structure prise en charge est vérifiée ; veuillez contrôler l'intégration et l'exécution dans HA. |
| **Réponse de l'assistant**<br><code>ugso_assist_response</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_assist_response.png" alt="Assist antwortet" style="max-width:280px;max-height:180px"> | Champs HA étendus ou Jinja original. La structure prise en charge est vérifiée ; veuillez contrôler l'intégration et l'exécution dans HA. |
| **Activer une scène**<br><code>ugso_scene</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_scene.png" alt="Szene aktivieren" style="max-width:280px;max-height:180px"> | Champs HA étendus ou Jinja original. La structure prise en charge est vérifiée ; veuillez contrôler l'intégration et l'exécution dans HA. |
| **Jinja (expérimental)**<br><code>ugso_jinja_value</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_value.png" alt="Jinja (experimentell)" style="max-width:280px;max-height:180px"> | Champs HA étendus ou Jinja original. La structure prise en charge est vérifiée ; veuillez contrôler l'intégration et l'exécution dans HA. |
| **Condition Jinja (expérimental)**<br><code>ugso_jinja_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_condition.png" alt="Jinja-Bedingung (experimentell)" style="max-width:280px;max-height:180px"> | Champs HA étendus ou Jinja original. La structure prise en charge est vérifiée ; veuillez contrôler l'intégration et l'exécution dans HA. |

### Structures Jinja (expérimental) {#jinja-strukturen-experimentell}

Depuis **0.1.64**, les blocs de code libre sont disponibles uniquement sous **Modèles** (*Templates*) sous les intitulés **Jinja – code personnalisé** et **Jinja – condition personnalisée**. Les anciens types `ugso_jinja_value` et `ugso_jinja_condition` restent lisibles pour les projets enregistrés et lors des importations ; les illustrations suivantes documentent ces anciens types. [Modèles spécifiques à un usage](/fr/projects/blocks-for-ha/system-template).

15 nouveaux types depuis 0.1.41. Les blocs externes de valeur/condition relient les éléments imbriqués à HA. Les expressions Jinja et les composants de modèles disposent de leurs propres connecteurs typés. [Lecture, édition et limites](/fr/projects/blocks-for-ha/advanced#jinja-experimentell).

| Bloc | Image | Fonction |
| --- | --- | --- |
| **Valeur Jinja composée**<br><code>ugso_jinja_composed_value</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_composed_value.png" alt="Jinja zusammengesetzt" style="max-width:280px;max-height:180px"> | Bloc de valeur externe : modèle (template) cohérent ; l'original est conservé jusqu'à sa modification. |
| **Condition Jinja composée**<br><code>ugso_jinja_composed_condition</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_composed_condition.png" alt="Jinja-Bedingung zusammengesetzt" style="max-width:280px;max-height:180px"> | Bloc booléen externe pour une condition de modèle (template) HA. |
| **Fonction d'entité**<br><code>ugso_jinja_entity</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_entity.png" alt="Entität Funktion" style="max-width:280px;max-height:180px"> | Rechercher une entité et sélectionner `states`, `state_attr`, `is_state` ou `is_state_attr` ; ajouter des arguments supplémentaires. |
| **Arguments et valeur de filtre**<br><code>ugso_jinja_filter</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_filter.png" alt="Filter Argumente Wert" style="max-width:280px;max-height:180px"> | Sélectionner un filtre ; ajouter 0 à 3 arguments positionnels ainsi qu'une expression Jinja. |
| **Littéral (Jinja)**<br><code>ugso_jinja_literal</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_literal.png" alt="Literal (Jinja)" style="max-width:280px;max-height:180px"> | Nombre, chaîne de caractères entre guillemets, `true`/`false` ou `none` selon la syntaxe Jinja. |
| **Variable Jinja**<br><code>ugso_jinja_variable</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_variable.png" alt="Jinja-Variable" style="max-width:280px;max-height:180px"> | Nom de variable Jinja simple sous forme de texte ; aucun renommage automatique par Blockly. |
| **Maintenant (Jinja)**<br><code>ugso_jinja_now</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_now.png" alt="Jetzt (Jinja)" style="max-width:280px;max-height:180px"> | Génère `now()` ; Home Assistant fournit l'instant précis lors de l'évaluation. |
| **Expression**<br><code>ugso_jinja_binary</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_binary.png" alt="Ausdruck" style="max-width:280px;max-height:180px"> | Calcule, compare ou combine deux expressions Jinja à l'aide des opérateurs `and` ou `or`. |
| **Expression**<br><code>ugso_jinja_unary</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_unary.png" alt="Ausdruck" style="max-width:280px;max-height:180px"> | Applique `not`, ou un signe négatif ou positif à une expression Jinja. |
| **Valeur conditionnelle**<br><code>ugso_jinja_select</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_select.png" alt="Wert wenn sonst" style="max-width:280px;max-height:180px"> | Sélectionne une valeur : « yes » si le test est vrai, sinon « no ». Les trois entrées d'expression sont requises. |
| **Sortie**<br><code>ugso_jinja_output</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_output.png" alt="Ausgeben" style="max-width:280px;max-height:180px"> | Afficher une expression sous la forme <code v-pre>{{ ... }}</code> au sein d'un modèle (template). |
| **Texte Jinja**<br><code>ugso_jinja_text</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_text.png" alt="Jinja-Text" style="max-width:280px;max-height:180px"> | Texte littéral, espaces compris ; ne pas insérer de caractères de contrôle Jinja ici. |
| **Assemblage de modèles**<br><code>ugso_jinja_join</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_join.png" alt="Template-Teile danach" style="max-width:280px;max-height:180px"> | Combiner deux parties de modèle dans l'ordre indiqué. |
| **Si/Sinon (texte)**<br><code>ugso_jinja_if</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_if.png" alt="Wenn Text sonst" style="max-width:280px;max-height:180px"> | Structure if/else avec condition et blocs de texte/sortie imbriqués. |
| **Boucle « pour » (texte) avec cas vide**<br><code>ugso_jinja_for</code> | <img src="/assets/blocks-for-ha/blocks/de/ugso_jinja_for.png" alt="Für in Text wenn leer" style="max-width:280px;max-height:180px"> | Boucle « for » simple : variable, expression, contenu du modèle et cas optionnel si vide. |

::::
