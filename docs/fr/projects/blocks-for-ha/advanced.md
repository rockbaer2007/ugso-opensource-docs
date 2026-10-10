---
title: Automatisations HA avancées et Jinja
description: Déclencheurs, conditions, cibles, groupes d’actions et reconnaissance Jinja expérimentale.
---

# Automatisations HA avancées et Jinja

Depuis **0.1.43**, les blocs HA avancés proposent des champs nommés au lieu d’un grand objet JSON. Toujours 163 types ; **HA avancé** et **Jinja (expérimental)** complètent les blocs simples. L’import vérifie la structure ; vérifier ensuite intégrations, IDs d’appareils, modèles et exécution dans Home Assistant.

Les 15 déclencheurs classiques avancés, conditions et étapes générales, cibles/options d’intégration, calendriers, seuils de température, motifs horaires, variables et options d’attente/étape utilisent des champs structurés. **numeric_state** propose entité, seuil supérieur, seuil inférieur, attribut, modèle, durée et ID. Les champs facultatifs vides sont omis ; les deux seuils sont indépendants. Les entités acceptent recherche HA, IDs manuels, listes JSON et modèles. Après changement du type d’un bloc général, ajouter si nécessaire les autres champs dans ses options.

Saisir listes et objets en JSON ; `null` est une valeur nulle explicite, `"null"` du texte. États et payloads restent du texte. Les valeurs inchangées conservent leurs types et le texte Jinja exact. **Options supplémentaires (JSON)** conserve les propriétés complémentaires. Données complexes et branches imbriquées restent des champs JSON séparés ; elles ne sont pas automatiquement décomposées en branches connectées. Les anciens projets JSON chargent automatiquement les nouveaux champs ; import/export YAML et projets restent compatibles.

![Déclencheur numeric-state avec champs séparés](/assets/blocks-for-ha/blocks/fr/ugso_ha_numeric_state_trigger.png)

Spécification originale : [Déclencheurs HA](https://www.home-assistant.io/docs/automation/trigger/), [Conditions HA](https://www.home-assistant.io/docs/scripts/conditions/), [Étapes HA](https://www.home-assistant.io/docs/scripts/).

## Déclencheurs et conditions

| Domaine | Ajouts pris en charge |
| --- | --- |
| État | Plusieurs entités ; `from`, `to`, `not_from`, `not_to`, listes et `null` ; attributs et `for`. |
| Nombres | Deux bornes, entités auxiliaires comme bornes, attributs, `value_template`, durée et plusieurs entités. |
| Heure | Heures et listes, auxiliaires/capteurs horaires, source avec décalage, jours et motifs horaires. |
| Soleil et HA | Lever/coucher avec décalage ; démarrage et arrêt de HA. |
| Autres déclencheurs | MQTT, modèle, webhook, zone, appareil, tag, conversation, géolocalisation, événement et calendrier classique. |
| Intégrations | `calendar.event_started/ended`, `temperature.changed`, `power.changed`, `motion.detected`, `timer.finished`. Cibles appareil, zone, étage et étiquette également possibles. |
| Conditions | Heure/jour, état avec listes/attribut/durée/`match`, bornes numériques, soleil, zone, appareil, ID du déclencheur, modèle et ET/OU/NON imbriqués. La forme abrégée d’un modèle est conservée. |

Le bloc d’intégration propose un menu puissance, mouvement et minuteur. Saisir cible et options séparément. Changer d’intégration remplace uniquement les exemples inchangés ; les valeurs personnalisées restent. Les déclencheurs JSON avancés acceptent `alias`, `enabled`, `id` et les variables du déclencheur. Types inconnus et champs non pris en charge sont refusés avec un message.

## Cibles, variables et options

**Action HA avec type de cible** propose `entity_id`, `device_id`, `area_id`, `floor_id` et `label_id`. Saisir un ID, une liste JSON ou un modèle HA. **Étape HA avancée** accepte plusieurs types de cibles simultanément. Les données d’action peuvent être un objet ou un modèle HA complet ; l’import conserve les deux formes.

Les variables acceptent listes et objets imbriqués. Chaque variable existante dispose d’un champ ; ajouter de nouveaux noms dans les options supplémentaires. Les options `alias`, `enabled`, `continue_on_error`, variables de réponse et métadonnées disposent de champs séparés. `enabled` accepte un booléen ou modèle HA ; `continue_on_error` un booléen.

Sous **Projekt & Beschreibung → Options HA**, modifier `variables`, `trigger_variables`, `initial_state`, `trace.stored_traces` et `max_exceeded`. **Appliquer** accepte uniquement des options valides. Les options omises sont supprimées ; `{}` supprime toutes les options gérées par ce champ. Nom et mode restent séparés. Sans `alias`, le nom de fichier devient `automation.yaml`. Les commandes générales de l’application restent actuellement allemandes.

## Attente et groupes d’actions

- **Attendre un déclencheur** relie une chaîne de déclencheurs ; `timeout` / `continue_on_timeout` se règlent dans les options.
- **Groupe d’actions** produit une `sequence` native avec étapes connectables.
- **Parallèle** lance des branches natives. **+ / −** permet 1–100 branches. Supprimer une branche occupée laisse ses blocs déconnectés ; les reconnecter ou supprimer.
- **Continuer seulement si** produit une condition comme étape d’action. Événement, réponse Assist et scène ont leurs blocs.
- Les répétitions acceptent aussi des listes/objets littéraux pour `for_each` ; les délais acceptent unités combinées et fractions. Les formes complexes ou mixtes restent des étapes JSON.

Ces blocs exportent les séquences natives HA. L’exécution se fait dans HA, sans moteur de script local.

## Jinja (expérimental)

Depuis **0.1.41**, **Jinja einlesen** peut décomposer les modèles en blocs imbriqués modifiables. Coller le modèle, vérifier l’aperçu, laisser **Décomposer en blocs modifiables** activé et choisir éventuellement **Als Bedingung**. **Block erstellen** place la structure connectée à côté de l’automatisation. Relier le bloc valeur extérieur à une affectation de variable ou une entrée de valeur ; relier le bloc condition à une entrée booléenne. Désactiver la décomposition crée un bloc de texte original.

![Bloc valeur Jinja composé](/assets/blocks-for-ha/blocks/fr/ugso_jinja_composed_value.png)

Exemple : <code v-pre>Eau: {{ states('sensor.water') | float(0) | round(1) }} °C</code> devient des parties de texte et une sortie contenant une fonction d’entité, `float` et `round`. Le champ d’entité ouvre la recherche existante. Modifier séparément entité, filtres, arguments et précision. L’import YAML décompose les valeurs correspondantes, par exemple dans une affectation unique de variable, et les conditions de modèle. Les formes existantes plus spécifiques sont conservées. Les modèles dans le JSON de données/options restent dans le champ JSON.

![Structure modifiable de l’exemple](/assets/blocks-for-ha/jinja/fr.png)

| Parties prises en charge | Représentation |
| --- | --- |
| `states`, `state_attr`, `is_state`, `is_state_attr` avec ID d’entité fixe | Fonction d’entité avec recherche et entrées d’arguments |
| `now()`, noms simples de variables, nombres, chaînes entre guillemets, booléens et `none` | Blocs d’expression ; noms de variables Jinja dans des champs texte |
| `float`, `int`, `round`, `default`, `abs`, `lower`, `upper`, `trim`, `length`, `string`, `list`, `join`, `replace` | Filtres imbriqués avec 0–3 arguments positionnels |
| `+`, `-`, `*`, `/`, `//`, `%`, `~`, comparaisons, `and`, `or`, `not` | Calculs/comparaisons avec parenthèses explicites |
| `valeur if condition else autre_valeur` | Sélection conditionnelle de valeur |
| Texte, <code v-pre>{{ ... }}</code>, simples `{% if ... %}...{% else %}...{% endif %}` | Blocs texte, sortie, liaison et si/sinon |
| `{% for item in items %}...{% else %}...{% endfor %}` | Boucle simple sur une expression, cas vide facultatif et parties imbriquées |

**Conserver l’original :** Les structures inchangées gardent le texte exact, espaces compris, après rechargement et annulation/rétablissement. Les modifications génèrent du Jinja reformatté ; restaurer les champs à la même structure rétablit l’original. Les projets Blockly sauvegardent structure et original. YAML sauvegarde le texte, analysé à nouveau lors de l’import.

::: warning Limites de décomposition
Analyseur original d’un sous-ensemble limité de Jinja. Dès qu’une partie n’est pas prise en charge, le **modèle entier** reste un bloc original modifiable. Exemples : `set`, `namespace`, accès aux objets/listes, littéraux liste/objet, tests `is defined`, comparaisons en chaîne, `elif`, arguments nommés, fonctions/filtres inconnus, commentaires et marqueurs de contrôle des espaces. Pas de décomposition partielle, de garantie syntaxique ni d’exécution locale. Le bloc valeur extérieur accepte des modèles entiers ; seul un affichage Jinja unique s’intègre dans un autre calcul. Entrées manquantes ou littéraux invalides empêchent l’export. Limites : 10000 caractères, 100 parties et imbrication bornée. Les noms de variables Jinja ne sont pas renommés automatiquement avec les autres variables Blockly. Home Assistant évalue le modèle ; y tester.
:::

Les projets Blockly conservent aussi formes et positions. YAML → Blockly → export conserve les valeurs prises en charge, y compris les champs facultatifs absents. Limites : 100 entrées/branches, 10 niveaux d’imbrication et tailles de données/modèles limitées. Les options spécifiques aux appareils ne sont pas exhaustives ; un champ refusé n’est jamais supprimé silencieusement.

## Sources originales et licences

Implémentation originale UGSo selon les spécifications publiques, sans copier le moteur ioBroker. Licences Blockly/plugins sous **Über & Lizenzen** ; application Apache-2.0.

- [Déclencheurs HA](https://www.home-assistant.io/docs/automation/trigger/), [conditions](https://www.home-assistant.io/docs/scripts/conditions/), [séquences](https://www.home-assistant.io/docs/scripts/) et [YAML](https://www.home-assistant.io/docs/automation/yaml/).
- [Puissance](https://www.home-assistant.io/triggers/power.changed/), [mouvement](https://www.home-assistant.io/triggers/motion.detected/), [minuteur terminé](https://www.home-assistant.io/triggers/timer.finished/).
- [Modèles Jinja](https://jinja.palletsprojects.com/en/stable/templates/) et [modèles HA](https://www.home-assistant.io/docs/configuration/templating/).
- [Blocs personnalisés Blockly](https://docs.blockly.com/guides/create-custom-blocks/overview/) et [code UGSo](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/blocks_for_ha).
