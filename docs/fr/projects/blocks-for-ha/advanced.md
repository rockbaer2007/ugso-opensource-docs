---
title: Automatisations HA avancées et Jinja
description: Déclencheurs, conditions, cibles, groupes d’actions et reconnaissance Jinja expérimentale.
---

# Automatisations HA avancées et Jinja

Depuis **0.1.39**, 148 types de blocs sont disponibles. **HA avancé** et **Jinja (expérimental)** complètent les blocs simples. Les étapes simples importées gardent leurs formes. Les champs supplémentaires apparaissent en JSON modifiable dans les blocs avancés. L’import vérifie la structure prise en charge ; vérifier ensuite intégrations, IDs d’appareils, modèles et exécution dans Home Assistant.

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

Les variables acceptent également listes et objets imbriqués. Les options communes `alias`, `enabled` et `continue_on_error`, les variables de réponse et les métadonnées sont conservées dans les champs JSON. `enabled` accepte un booléen ou modèle HA ; `continue_on_error` un booléen.

Sous **Projekt & Beschreibung → Options HA**, modifier `variables`, `trigger_variables`, `initial_state`, `trace.stored_traces` et `max_exceeded`. **Appliquer** accepte uniquement des options valides. Les options omises sont supprimées ; `{}` supprime toutes les options gérées par ce champ. Nom et mode restent séparés. Sans `alias`, le nom de fichier devient `automation.yaml`. Les commandes générales de l’application restent actuellement allemandes.

## Attente et groupes d’actions

- **Attendre un déclencheur** relie une chaîne de déclencheurs ; `timeout` / `continue_on_timeout` se règlent dans les options.
- **Groupe d’actions** produit une `sequence` native avec étapes connectables.
- **Parallèle** lance des branches natives. **+ / −** permet 1–100 branches. Supprimer une branche occupée laisse ses blocs déconnectés ; les reconnecter ou supprimer.
- **Continuer seulement si** produit une condition comme étape d’action. Événement, réponse Assist et scène ont leurs blocs.
- Les répétitions acceptent aussi des listes/objets littéraux pour `for_each` ; les délais acceptent unités combinées et fractions. Les formes complexes ou mixtes restent des étapes JSON.

Ces blocs exportent les séquences natives HA. L’exécution se fait dans HA, sans moteur de script local.

## Jinja (expérimental)

**Jinja einlesen** au-dessus de l’espace ouvre un dialogue. Coller le modèle, vérifier l’aperçu, choisir éventuellement **Als Bedingung**, puis **Block erstellen**. Le nouveau bloc apparaît à côté de l’automatisation et doit être connecté. On peut aussi déplacer les blocs valeur/condition depuis la catégorie. Les valeurs et conditions de modèle importées utilisent également Jinja lorsqu’aucune forme simple plus spécifique ne correspond.

![Bloc valeur Jinja expérimental](/assets/blocks-for-ha/blocks/fr/ugso_jinja_value.png)

L’analyse reconnaît états et attributs d’entités, date/heure, variables, filtres, `if/else` et `for`. Le bloc affiche entités et filtres reconnus. Commentaires, chaînes littérales et sections `raw` sont ignorés lors de la recherche de références. L’aperçu signale les structures de contrôle incomplètes.

::: warning Limites de reconnaissance
Analyse prudente de motifs : ce n’est ni un analyseur Jinja complet, ni une décomposition automatique en sous-blocs exécutables, ni une garantie syntaxique. Fonctions inconnues et modèles complexes conservent leur texte original modifiable. Aucun texte n’est réécrit ou exécuté localement. Tester dans HA. Une expression composée accepte uniquement une expression Jinja unique ; un modèle `if/for` complet appartient au bloc valeur autonome.
:::

Les projets Blockly conservent aussi formes et positions. YAML → Blockly → export conserve les valeurs prises en charge, y compris les champs facultatifs absents. Limites : 100 entrées/branches, 10 niveaux d’imbrication et tailles de données/modèles limitées. Les options spécifiques aux appareils ne sont pas exhaustives ; un champ refusé n’est jamais supprimé silencieusement.

## Sources originales et licences

Implémentation originale UGSo selon les spécifications publiques, sans copier le moteur ioBroker. Licences Blockly/plugins sous **Über & Lizenzen** ; application Apache-2.0.

- [Déclencheurs HA](https://www.home-assistant.io/docs/automation/trigger/), [conditions](https://www.home-assistant.io/docs/scripts/conditions/), [séquences](https://www.home-assistant.io/docs/scripts/) et [YAML](https://www.home-assistant.io/docs/automation/yaml/).
- [Puissance](https://www.home-assistant.io/triggers/power.changed/), [mouvement](https://www.home-assistant.io/triggers/motion.detected/), [minuteur terminé](https://www.home-assistant.io/triggers/timer.finished/).
- [Modèles Jinja](https://jinja.palletsprojects.com/en/stable/templates/) et [modèles HA](https://www.home-assistant.io/docs/configuration/templating/).
- [Blocs personnalisés Blockly](https://docs.blockly.com/guides/create-custom-blocks/overview/) et [code UGSo](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/blocks_for_ha).
