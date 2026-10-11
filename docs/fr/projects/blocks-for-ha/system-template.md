---
title: Valeurs système et constructeur de templates
description: Valeurs d’entités partagées, commandes d’applications et d’automatisations, templates lisibles.
---

# Valeurs système et constructeur de templates

Depuis **0.1.62**, entièrement traduit en DE/EN/FR. Les blocs Système fournissent aussi les valeurs des Templates. Réutiliser les blocs texte, mathématiques et variables existants.

Depuis **0.1.63**, Template possède des entrées de valeurs directes sur des lignes verticales, comme Écrire un fichier dans ioBroker. Tous les blocs Template sont sans engrenage ; les entrées correspondent à leur type.

## Templates par usage depuis 0.1.64

Ces blocs sont dans **Templates**, sans engrenage. **Composer du texte** produit du texte pour les messages. **Heure dans la plage** et **Vérifier la variation** renvoient un booléen et se branchent directement sur « Seulement si », « si », « et » ou « ou ». **Choisir une valeur – si/sinon** propose des types de résultat avec les entrées adaptées.

### Heure dans la plage

Saisir début et fin en `HH:MM` ou `HH:MM:SS`. L’heure locale actuelle de HA est vérifiée : **début inclus**, **fin exclue**. Avec 10:00 et 13:00, cela correspond à `'10:00:00' <= now().strftime('%H:%M:%S') < '13:00:00'`. De 22:00 à 06:00 fonctionne en passant minuit. Des bornes égales donnent faux. C’est une condition, pas un déclencheur horaire.

![Heure dans la plage](/assets/blocks-for-ha/blocks/fr/ugso_template_time_window.png)

### Vérifier la variation

**Hausse supérieure à 10**, **baisse supérieure à 20** vérifie `nouvelle valeur - ancienne valeur > 10` ou `< -20`. Saisir la baisse comme une amplitude positive. Exactement +10 ou −20 ne satisfait pas la condition.

Laisser Ancienne valeur et Nouvelle valeur vides utilise `trigger.from_state.state` et `trigger.to_state.state`, pour les déclencheurs d’état. Un déclencheur ou ancien état absent donne faux, comme un ancien état `unknown`, `unavailable` ou `none`. On peut aussi brancher des variables enregistrées ou des valeurs d’entités Système. Les deux valeurs utilisent `float(0)`, comme l’exemple : le texte non numérique vaut 0. Une nouvelle valeur absente vaut aussi 0. Vérifier séparément la nouvelle valeur si ce comportement ne convient pas.

![Vérifier la variation](/assets/blocks-for-ha/blocks/fr/ugso_template_change.png)

### Code Jinja personnalisé

**Jinja – code personnalisé** accepte un template complet pour une entrée de valeur ; **Jinja – condition personnalisée** accepte un template booléen complet. Les instructions multilignes `{% if %}`, `{% set %}` et `{% else %}` sont conservées. Seule une expression unique <code v-pre>{{ ... }}</code> peut constituer une partie de Composer du texte ; brancher les templates avec instructions directement sur leur destination.

![Code personnalisé](/assets/blocks-for-ha/blocks/fr/ugso_template.png)
![Condition personnalisée](/assets/blocks-for-ha/blocks/fr/ugso_template_condition.png)

Les entrées de code libre équivalentes ont été retirées de **Jinja (expérimental)** et figurent une seule fois dans **Templates**. La catégorie expérimentale garde le constructeur Jinja décomposable. Ses parties modifient des expressions Jinja et ne sont pas des actions HA supplémentaires. Les anciens blocs de projet et le code original importé restent lisibles.

**Contrôler l’application** et **Contrôler l’automatisation** sont dans **Système**. Depuis 0.1.64, ils ont deux lignes comme Contrôler l’instance dans ioBroker : sélection en haut, Action en dessous. Les applications HA et entités d’automatisation remplacent les instances ioBroker.

## Système

Les changements dans l’engrenage modifient immédiatement le bloc principal : ajouter affiche une ligne, retirer la masque et adapte la taille, même avec le dialogue ouvert.

| Bloc | Utilisation |
| --- | --- |
| ID de l’entité | Choisir une entité et brancher son ID sur un autre bloc. |
| Valeur de l’entité | Sélection HA fixe : état, nom, unité, attribut, dernière modification ou actualisation. |
| Valeur de l’ID d’entité | Brancher un ID provenant d’un bloc ID d’entité, texte ou variable. |
| Lire une fois dans une variable | Enregistrer un instantané puis exécuter les actions contenues. Ce n’est pas un déclencheur. La variable reste disponible pour les étapes HA suivantes. |
| Contrôler l’application | Démarrer, arrêter ou redémarrer. Choisir une application installée via Supervisor ou saisir son identifiant. |
| Contrôler l’automatisation | Activer, désactiver, basculer ou exécuter maintenant. |

![Valeur d’entité](/assets/blocks-for-ha/blocks/fr/ugso_entity_value.png)
![Valeur dynamique](/assets/blocks-for-ha/blocks/fr/ugso_entity_value_dynamic.png)
![Instantané](/assets/blocks-for-ha/blocks/fr/ugso_entity_snapshot.png)
![Commande d’automatisation](/assets/blocks-for-ha/blocks/fr/ugso_automation_control.png)
![Commande d’application](/assets/blocks-for-ha/blocks/fr/ugso_app_control.png)

Choisir **Attribut** et saisir son nom ; la ligne correspondante apparaît automatiquement. Les états sont souvent du texte. Utiliser **Conversion → en nombre** avant les calculs si nécessaire. Les attributs et horodatages absents donnent `none` ; un état absent donne `unknown` selon HA. **Valeur de remplacement** permet de traiter ces cas.

L’engrenage de **Contrôler l’automatisation** ajoute **Brancher l’ID d’entité**, **Vérifier les conditions** et **Arrêter les actions en cours**. L’ID branché remplace la sélection fixe. Les conditions concernent « exécuter maintenant », l’arrêt concerne « désactiver ». Sans option explicite, HA applique ses valeurs par défaut : exécuter ignore les conditions, désactiver arrête les actions en cours. Activer permet d’écouter les déclencheurs sans exécuter immédiatement les actions.

**Contrôler l’application** nécessite Supervisor et les droits administrateur. L’application reçoit un accès en lecture à Supervisor pour la sélection ; démarrage/arrêt/redémarrage se produisent uniquement lors de l’exécution de l’automatisation exportée dans HA. Sans Supervisor, l’identifiant reste modifiable mais l’action est indisponible. Export : `hassio.app_start`, `hassio.app_stop`, `hassio.app_restart` avec `data.app`.

## Construire un Template

1. Brancher **Templates → Composer du texte** sur une entrée texte, par exemple « Message ».
2. Brancher un **Texte** normal directement sur **Partie 1**.
3. Brancher une **Valeur d’entité de Système** ou un **Format du nombre** directement sur **Partie 2**.
4. Remplir la dernière entrée ajoute automatiquement une autre entrée. L’ordre de haut en bas détermine la sortie. Les entrées vides sont ignorées et conservent leur position pour annuler/rétablir.

Exemple : texte `Température : ` → valeur de `sensor.temperature` via **Format du nombre**, avec le nombre mathématique `1` pour les décimales → texte ` °C`. Résultat possible : `Température : 21.6 °C`.

![Template](/assets/blocks-for-ha/blocks/fr/ugso_template_builder.png)
![Nouvelle ligne comme valeur](/assets/blocks-for-ha/blocks/fr/ugso_template_linebreak.png)
![Format du nombre](/assets/blocks-for-ha/blocks/fr/ugso_number_format.png)
![Sortie conditionnelle](/assets/blocks-for-ha/blocks/fr/ugso_template_conditional.png)

| Complément | Signification |
| --- | --- |
| Format du nombre | 0–10 décimales avec un point décimal. Utiliser un nombre mathématique pour leur quantité. Brancher le remplacement directement sur son entrée facultative ; sinon texte vide pour les nombres invalides. |
| Valeur sinon | Remplacement pour `unknown`, `unavailable`, `none` et texte vide. Conserve `0` et `false`. |
| Nouvelle ligne | Commencer une nouvelle ligne à cet endroit. |
| Choisir une valeur – si/sinon | Choisir le type : Valeur, Texte, Nombre ou Booléen. Brancher un booléen sur « si » et des valeurs adaptées sur « alors » et « sinon ». Utiliser Composer du texte pour plusieurs parties. Une branche vide produit du texte vide pour Valeur/Texte ; Nombre/Booléen exigent les deux branches. |

Brancher le formatage directement autour de la valeur concernée. Texte, nombres, valeurs d’entités, nouvelles lignes et valeurs conditionnelles utilisent des connexions de valeurs ; « si » accepte uniquement les blocs booléens. Les chaînes d’actions ne se branchent pas sur ces entrées. Les caractères Jinja d’un texte normal restent littéraux. Les anciennes chaînes Afficher sont converties automatiquement lors du chargement dans l’éditeur, en conservant branches et parties désactivées. Les anciens types restent lisibles pour la compatibilité mais ne figurent plus dans le menu.

**Clic droit → Aperçu du template / Jinja** affiche le code produit et demande à HA le rendu des valeurs actuelles. Cet instantané n’exécute aucune action et nécessite une connexion HA accessible. Sans connexion, l’aperçu est explicitement indisponible. Les identifiants d’accès restent sur le serveur. Le JSON du projet conserve les blocs, connexions et options d’engrenage. Le YAML contient du Jinja natif ; son import peut produire un bloc template libre. HA peut interpréter les nombres ou listes purs d’un résultat comme des valeurs natives.

Références : [actions d’automatisation HA](https://www.home-assistant.io/docs/automation/automation_integration_actions/), [Supervisor](https://www.home-assistant.io/integrations/hassio/), [Jinja dans HA](https://www.home-assistant.io/docs/templating/).
