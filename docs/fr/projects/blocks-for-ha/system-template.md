---
title: Valeurs système et constructeur de templates
description: Valeurs d’entités partagées, commandes d’applications et d’automatisations, templates lisibles.
---

# Valeurs système et constructeur de templates

Depuis **0.1.62**, entièrement traduit en DE/EN/FR. Les blocs Système fournissent aussi les valeurs des Templates. Réutiliser les blocs texte, mathématiques et variables existants.

Depuis **0.1.63**, Template possède des entrées de valeurs directes sur des lignes verticales, comme Écrire un fichier dans ioBroker. Tous les blocs Template sont sans engrenage ; les entrées correspondent à leur type.

## Système

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

1. Brancher **Templates → Template** sur une entrée de valeur, par exemple « Message ».
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
| si / alors / sinon | Brancher une condition booléenne sur « si » et les valeurs sur « alors » et « sinon ». Brancher un autre Template pour plusieurs parties dans une branche. Une branche vide produit un texte vide. |

Brancher le formatage directement autour de la valeur concernée. Texte, nombres, valeurs d’entités, nouvelles lignes et valeurs conditionnelles utilisent des connexions de valeurs ; « si » accepte uniquement les blocs booléens. Les chaînes d’actions ne se branchent pas sur ces entrées. Les caractères Jinja d’un texte normal restent littéraux. Les anciennes chaînes Afficher sont converties automatiquement lors du chargement dans l’éditeur, en conservant branches et parties désactivées. Les anciens types restent lisibles pour la compatibilité mais ne figurent plus dans le menu.

**Clic droit → Aperçu du template / Jinja** affiche le code produit et demande à HA le rendu des valeurs actuelles. Cet instantané n’exécute aucune action et nécessite une connexion HA accessible. Sans connexion, l’aperçu est explicitement indisponible. Les identifiants d’accès restent sur le serveur. Le JSON du projet conserve les blocs, connexions et options d’engrenage. Le YAML contient du Jinja natif ; son import peut produire un bloc template libre. HA peut interpréter les nombres ou listes purs d’un résultat comme des valeurs natives.

Références : [actions d’automatisation HA](https://www.home-assistant.io/docs/automation/automation_integration_actions/), [Supervisor](https://www.home-assistant.io/integrations/hassio/), [Jinja dans HA](https://www.home-assistant.io/docs/templating/).
