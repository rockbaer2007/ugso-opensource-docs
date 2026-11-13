---
title: Logic Studio
description: HA Logic Studio Pro 0.1.67 · Import ioBroker étendu dans Blocks JS
---
# <img class="package-icon" src="/images/logic-studio/icon.svg" width="40" height="40" alt=""> Logic Studio

**0.1.12 – mise à jour publique de test, 8 novembre 2026.** Interface et documentation sont désormais disponibles en **DE/EN/FR**. Logic Studio est une application HA autonome pour les plans à blocs fonctionnels, indépendante de Grafik Visual Studio et Blocks for HA. Le canevas React Flow conserve ses blocs personnalisés, connexions typées, zoom et MiniMap ; bibliothèques et licences sont incluses localement.

::: warning Version de test
Installer d’abord sur un système de test et créer une sauvegarde complète. Les propriétés natives détaillées sont actuellement modifiables en JSON. L’application ne réécrit pas les automatisations/scripts dans HA et ne commande aucun appareil. Vérifier et installer soi-même les sorties générées.
:::

[Version de test GitHub et ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/logic-studio-v0.1.12) · [Sources dans le dépôt commun](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/logic_studio)

## HA Logic Studio Pro 0.1.67

Version de test publique actuelle. Créer une sauvegarde complète et essayer la mise à jour sur un système de test.

Les blocs importés de vérification de l’existence d’un état et d’identifiant d’objet conservent leur identifiant ioBroker. Associez explicitement chaque identifiant à une entité Home Assistant dans le bloc. Blocks JS retrouve les données Blockly intégrées dans un fichier JavaScript même si d’autres commentaires les suivent.

La section **Adaptations du code requises** de l’aperçu explique comment remplacer les blocs non pris en charge, comme `exec`. Après une sauvegarde complète sur `.193`, des fichiers de test XML et JavaScript ont été importés et les nouveaux champs d’association ont été vérifiés dans l’éditeur.

### Reconnexion après un redémarrage de Core

Une sauvegarde complète a été créée sur le système de test `.193` avant l’essai. Après le redémarrage de Home Assistant Core, le moteur d’exécution s’est reconnecté 31 secondes après la coupure. La même exécution du script JavaScript a ensuite reçu le passage de l’entité de test de `off` à `on` et l’événement HA personnalisé `logic_studio_runtime_test` avec ses données de test.

[HA Logic Studio Pro 0.1.67 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.67)

## HA Logic Studio Pro 0.1.66

Activez la sauvegarde des compteurs et des mémoires dans le diagramme fonctionnel, puis enregistrez le projet. Les blocs CTU, CTD, CTUD, RS et SR peuvent retrouver leurs valeurs après le redémarrage de l’application.

Le rapport d’import de Blocks JS répertorie séparément les identifiants ioBroker calculés. Dans le champ d’association JSON du bloc importé, associez chaque identifiant ioBroker possible à une entité Home Assistant.

Sur `.193`, le compteur CTU et la mémoire RS ont conservé les valeurs `1` et `true` après le redémarrage de l’application.

Lors du test en conditions réelles sur `.193`, le script Blocks JS importé a calculé l’identifiant ioBroker `zigbee.0.sensor`. L’association JSON lui a permis de lire l’assistant de test Home Assistant `input_boolean.logic_studio_runtime_test`. Deux lancements avec le bouton de lecture ont inscrit `false` dans le journal lorsque l’assistant était désactivé et `true` lorsqu’il était activé.

[HA Logic Studio Pro 0.1.66 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.66)

## HA Logic Studio Pro 0.1.65

### Démarrage automatique, simulation et import ioBroker

Les projets JavaScript, TypeScript et les diagrammes fonctionnels peuvent être exécutés au démarrage de l’application. Activer **Exécuter au démarrage de l’application** et enregistrer le projet. La simulation propose des points d’arrêt et le pas à pas. L’organisation automatique conserve la position des blocs épinglés. L’aperçu d’import ioBroker de Blocks JS liste les blocs non pris en charge et les identifiants fixes à associer.

Sur `.193`, le projet de test JavaScript enregistré a démarré automatiquement après le redémarrage de l’application. Un point d’arrêt, un pas de simulation et l’aperçu d’import ioBroker avec un identifiant fixe ont également été vérifiés.

[HA Logic Studio Pro 0.1.65 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.65)

## HA Logic Studio Pro 0.1.62


HA Logic Studio Pro est une application Home Assistant autonome dans le dépôt commun UGSo. Elle s’appuie sur Logic Studio et sur l’expérience acquise avec ioBroker.

**Fonctionnalités disponibles**

- **Diagramme fonctionnel :** Relier les blocs, afficher les signaux aux entrées et simuler le diagramme. Sur le serveur HA, l’exécution peut réagir aux changements ou suivre un cycle fixe.
- **Règles et Blocks A :** Créer des automatisations dans un éditeur visuel et les exporter au format YAML de HA.
- **Blocks JS, JavaScript et TypeScript :** Modifier la logique, la tester avec des valeurs simulées et l’exécuter sur le serveur HA.
- **YAML HA :** Modifier, valider et exporter les automatisations et les scripts.
- **Gestion des projets :** Enregistrer les projets et les dossiers sur le serveur pour chaque utilisateur HA.
- **Choix de la langue :** Les éditeurs sont disponibles en allemand, en anglais et en français.

La version **0.1.62** a ajouté les fonctions de règles décrites ci-dessous.

### Règles enrichies et test en conditions réelles sur .193

Les déclencheurs d’état prennent en charge les valeurs de départ et d’arrivée, un attribut et une durée minimale. Les conditions vérifient les états, les attributs et les seuils numériques. Les branches ALORS et SINON proposent un sélecteur d’actions HA avec des paramètres JSON et des étapes de temporisation distinctes.

L’éditeur et le sélecteur d’actions ont été testés localement dans le navigateur. Après une sauvegarde complète, le YAML généré a été exécuté directement dans Home Assistant sur `.193`. Une impulsion brève n’a rien déclenché. Un état maintenu trois secondes a exécuté ALORS. Un changement du nom d’affichage a exécuté SINON. Les deux traces ont confirmé le délai de deux secondes et la valeur de texte attendue. L’automatisation et les deux auxiliaires de test ont été supprimés.

Les nouveaux blocs s’exportent en YAML HA. Rules → JS indique si un bloc empêche la conversion.

[HA Logic Studio Pro 0.1.62 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.62)

### Export YAML et test en conditions réelles sur .193

L’export des règles conserve les états tels que `on` et `off` sous forme de texte, sans les convertir en booléens YAML. L’automatisation corrigée a été exécutée directement dans Home Assistant sur `.193` avec des entrées de test.

| Déclencheur | Condition | Résultat de la trace HA |
| --- | --- | --- |
| Changement d’état | OU satisfaite | Deux actions ALORS |
| Changement d’état | ET non satisfaite | Deux actions SINON |
| Événement HA | Condition NON vraie | Deux actions ALORS |
| Heure 20:26 | Condition NON fausse | Deux actions SINON |

Une sauvegarde complète a été créée avant le test. L’automatisation et les trois entrées de test ont ensuite été supprimées.

[HA Logic Studio Pro 0.1.61 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.61)

### Règles : palette compacte et déclencheurs multiples

L’éditeur affiche une liste compacte avec des icônes à gauche. Une règle peut combiner des changements d’état, une heure quotidienne et des événements Home Assistant. Les conditions acceptent ET, OU et NON. Les branches ALORS et SINON exécutent plusieurs actions dans l’ordre affiché.

Sur le système `.193`, une règle existante a été testée avec trois déclencheurs, deux conditions et deux actions par branche. L’aperçu YAML présentait la structure attendue. Lors du test dans Studio, les trois déclencheurs simulés ont lancé les deux actions ALORS lorsque la condition OU était satisfaite. Lorsque la condition ET ne l’était pas, les deux actions SINON se sont exécutées dans l’ordre configuré. Aucun appareil réel n’a été commandé.

[HA Logic Studio Pro 0.1.60 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.60)

![Éditeur de règles sur .193 avec la palette compacte et les deux branches](/images/logic-studio/0.1.60-rules-test-193.png)

### Créer une règle avec l’assistant

Choisissez **Règles → Assistant**. Le dialogue suit quatre étapes : **Déclencheur → Conditions → Actions → Récapitulatif**. Une règle peut réagir à un changement d’état, à une heure quotidienne dans le fuseau horaire de HA ou à un événement Home Assistant. Les conditions et la branche SINON sont facultatives. Le récapitulatif affiche l’aperçu YAML. **Appliquer** transfère le brouillon dans l’éditeur ; **Enregistrer** le conserve. Les règles existantes restent modifiables et peuvent être ouvertes en JavaScript ou en YAML HA.

[HA Logic Studio Pro 0.1.59 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.59)

Le 12 novembre 2026, les trois déclencheurs ont été testés directement dans Home Assistant sur le système de test `.193`. Le passage de l’état désactivé à l’état activé, le déclenchement quotidien à 19 h 38 (heure locale de HA) et l’événement `rules_live_0159_event` ont chacun activé la sortie de test. Une sauvegarde complète a été créée avant le test. Les trois automatisations et les deux assistants de test ont ensuite été supprimés.

![Home Assistant affiche la dernière exécution des trois automatisations de test et la sortie de test activée](/images/logic-studio/0.1.59-rules-live-test-193.png)

### Nouveautés depuis la version 0.1.12

- **Arborescence et éditeurs.** Les projets et dossiers sont enregistrés sur le serveur pour chaque utilisateur HA. Les projets locaux peuvent être migrés au premier démarrage depuis le navigateur d’origine. JavaScript et TypeScript disposent de la coloration syntaxique, de numéros de ligne et de barres d’outils dédiées. Les icônes et couleurs correspondent entre le sélecteur, l’arborescence et les filtres. Blocks A et Blocks JS ont des filtres distincts. La largeur automatique du volet reste réglable par la poignée.
- **Blocks A et Blocks JS.** Blocks A utilise le catalogue intégré de Blocks for HA. Blocks JS dispose de sa propre palette JavaScript. Blocks A exporte des automatisations HA en YAML. Blocks JS génère le JavaScript pour la simulation et le moteur. Les blocs ioBroker inconnus sont conservés sous forme de blocs de remplacement et bloquent la génération du code jusqu’à leur remplacement. Associer les identifiants d’objets ioBroker aux entités HA correspondantes.
- **Diagramme fonctionnel.** La barre supérieure comporte les icônes de simulation, d’avancement d’une seconde et de réinitialisation. Le format de sortie et l’aperçu sont à droite. Les connexions peuvent être déplacées vers une autre entrée et les valeurs des signaux s’affichent à l’entrée cible.
- **Moteur serveur.** Le bouton de lecture lance JavaScript, TypeScript transpilé ou Blocks JS sur le serveur HA. L’arrêt et le redémarrage sont disponibles dans l’éditeur. L’état et le journal restent accessibles depuis un autre navigateur. Le **test** séparé utilise des états et événements simulés. Les scripts et automatisations YAML sont exécutés par Home Assistant après import.

### Configurer le moteur en direct

Dans **Paramètres → Applications → HA Logic Studio Pro → Configuration**, ajouter les entrées nécessaires, enregistrer puis redémarrer l’application. Les listes sont vides par défaut. Exemple avec une entrée booléenne dédiée au test :

```yaml
runtime_read_entities: []
runtime_write_entities:
  - input_boolean.logic_studio_runtime_test
runtime_events:
  - logic_studio_runtime_test
```

L’autorisation d’écriture inclut la lecture. `ha.readState` et `ha.readAttribute` renvoient les dernières valeurs confirmées par HA. `ha.onState`, `ha.onAttribute` et `ha.onEvent` réagissent aux changements et événements autorisés. `ha.callAction` permet la commutation, la modification des entrées numériques, textuelles ou de sélection et l’appui sur des boutons pour une cible autorisée. `ha.schedule` accepte des motifs horaires et des heures fixes, avec des jours de la semaine facultatifs, dans le fuseau horaire de HA.

Après le redémarrage de l’application, les scripts doivent être relancés. En cas de perte de connexion ou de refus d’une action, le moteur arrête le script et journalise l’erreur. Les déclencheurs astronomiques et la reconnexion automatique restent à ajouter.

**Vérifié sur .193 avec HA 2026.11.1.** Le moteur a lu l’état et un attribut de l’entrée de test, l’a activée par un horaire et l’a désactivée à la réception d’un événement HA réel. Les deux changements d’état ont été signalés. Un horaire Blocks JS importé s’est exécuté toutes les deux secondes. Les tests précédents ont vérifié le démarrage, l’arrêt, le redémarrage et la poursuite de l’exécution après avoir quitté Studio, avec JavaScript et TypeScript.

### Commander des scripts et des automatisations

Dans **Blocks JS → Système**, choisissez une entité Home Assistant avec **Choisir un script ou une automatisation**, puis reliez le bloc à **Commander**. Vous pouvez démarrer ou arrêter les scripts, ainsi qu’activer, désactiver ou déclencher une fois les automatisations. L’option **Vérifier les conditions** est activée par défaut lors du déclenchement. Décochez-la pour ignorer les conditions. Pour l’exécution réelle, autorisez l’entité cible dans `runtime_write_entities`.

[HA Logic Studio Pro 0.1.58 · GitHub et ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.58)

### Fonctions et import ioBroker

**Blocks JS → Fonctions** propose deux blocs de fonction JavaScript, avec ou sans valeur de retour. Utilisez l’engrenage pour définir les paramètres et **…** pour modifier le code. Après l’ajout d’une définition, son bloc d’appel apparaît dans la palette.

L’import ioBroker conserve les définitions, les appels, les paramètres et le code JavaScript. Adaptez les appels propres à ioBroker au moteur HA et associez explicitement les identifiants d’objet importés aux entités HA.

### Interroger l’historique

Utilisez **Blocks JS → Sendto → Interroger l’historique** pour lire les états enregistrés par HA Recorder. Sans période indiquée, la requête utilise la journée en cours dans le fuseau horaire de HA. Le bloc de résultat renvoie des valeurs horodatées. L’import ioBroker conserve la période, l’agrégation, le pas et le nombre de résultats.

[HA Logic Studio Pro 0.1.57 · GitHub et ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.57)

### 0.1.29 · Enregistrement manuel et éditeurs de blocs

Dans tous les éditeurs, **Enregistrer** applique les modifications. **Annuler** restaure la dernière version enregistrée ou abandonne un nouveau projet. Les modifications non enregistrées désactivent **Démarrer** et **Redémarrer**. Il reste possible d’arrêter un script en cours. Blocks A ouvre le sélecteur d’entités directement depuis le champ du bloc. Blocks JS propose une palette inspirée d’ioBroker avec des entités, des actions et des déclencheurs HA, sans Jinja.

[Version de test et ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.29)

### 0.1.28 · Traductions des éditeurs

La version **0.1.28** complète les traductions des éditeurs de règles, Blocks A, Blocks JS, JavaScript, TypeScript et YAML HA. Le choix de langue s’applique aussi au diagramme fonctionnel. [Version de test et ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.28)

Les tests sur .193 ont vérifié dans les trois langues les barres d’outils du diagramme fonctionnel, des règles, de Blocks A, de Blocks JS, de JavaScript, de TypeScript, des automatisations HA et des scripts HA. La boîte de dialogue des exemples de code a aussi été vérifiée en français.

Pour installer la version Pro, sélectionner **HA Logic Studio Pro** dans le dépôt commun UGSo de la boutique d’applications. Pour une installation GitHub existante, rechercher les mises à jour puis sélectionner **HA Logic Studio Pro → Mettre à jour**. Utiliser **DE**, **EN** ou **FR** en haut du volet des projets pour changer la langue des éditeurs.

### 0.1.26 · FBD Runtime

Le bouton **Lecture** lance le diagramme fonctionnel sur le serveur HA. Le mode **Automatique** réagit aux changements des états et attributs autorisés ; le **Cycle fixe** évalue le plan toutes les 100 à 60 000 ms. La simulation et l’export YAML restent séparés. **Enregistrer** valide le brouillon ; **Annuler** rétablit le dernier état enregistré. La barre d’outils est disponible en DE/EN/FR.

Sur .193, le démarrage automatique a activé l’entité de test et le cycle de 200 ms l’a désactivée. L’arrêt et l’annulation d’une modification non enregistrée ont aussi été vérifiés. Les deux modes ont également été testés localement avec des changements d’entrée.

[Mise à jour de test GitHub et ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.26) · [Application dans le dépôt commun](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_logic_studio_pro)

## Installation de test depuis GitHub

[![Ajouter le dépôt à Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Frockbaer2007%2Fugso-ha-mqtt-addons)

1. Dans **Paramètres → Applications → Boutique d’applications → Dépôts**, ajouter l’adresse ci-dessous. Si « UGSo HA Apps » est déjà configuré, rechercher les mises à jour.
2. Sélectionner et installer **UGSo Logic Studio**. Activer le mode avancé du profil HA si les applications expérimentales sont masquées.
3. Démarrer puis ouvrir l’interface. Compatible **HA OS/Supervised**, **amd64 et aarch64**. La première construction du conteneur peut prendre plusieurs minutes. Ce n’est pas un paquet frontend HACS/Marketplace.

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

**Conserver une installation locale existante :** les applications GitHub et locale ont des identifiants de dépôt et des données séparés. Exporter l’ancien plan en JSON avec **Projekt**, puis utiliser **Öffnen** dans l’application GitHub. Aucune migration ou désinstallation automatique. Chaque application conserve projet et réglages de palette sous `/data`.

**Mettre à jour une application GitHub existante :** sauvegarder d’abord, rechercher les mises à jour dans le gestionnaire d’applications puis choisir **UGSo Logic Studio → Mettre à jour**. Conserver l’installation : `/data`, les identifiants d’entités et les plans existants sont préservés. Ne pas désinstaller ni changer d’identifiant d’application. Sur .193, le plan original, les favoris, les blocs récents et les catégories repliées ont été conservés après la mise à jour.

## Langue, barre d’outils et documentation

Choisir **Langue → Deutsch / English / Français** dans l’en-tête. Menus, descriptions des blocs, sélecteur d’entités et dialogues d’import/export changent sans rechargement. Le choix est enregistré avec les préférences du navigateur/de l’application. **Noms personnels, identifiants d’entités, valeurs, noms des bornes et code YAML/JavaScript généré ne sont pas traduits.**

**Documentation**, à droite, présente les raccourcis implémentés et, pour le bloc sélectionné, sa description et ses entrées/sorties. **Ctrl+Z / Ctrl+Y** : annuler/rétablir ; **Suppr** : supprimer la sélection ; **Échap** : annuler une connexion/fermer un menu. Tab et Entrée/Espace permettent de choisir et connecter les bornes. Les commandes du débogueur de l’éditeur de référence ioBroker ne sont pas présentées comme disponibles.

La barre regroupe **Annuler/rétablir → Projet → Simulation → Sortie**. Les trois boutons de simulation ont les mêmes dimensions et des bordures distinctes. Le menu Projet propose aussi **Nouveau projet** et **Charger l’exemple**. Le sélecteur d’entités s’ouvre via l’icône **à côté de l’identifiant d’entité HA** dans les propriétés STATE_IN/STATE_OUT ; l’ancien bouton supérieur est retiré.

![Documentation allemande sur .193 avec le plan original conservé](/images/logic-studio/0.1.12-193-de-documentation.png)

![Documentation anglaise du même plan sur .193](/images/logic-studio/0.1.12-193-en-documentation.png)

![Documentation française du même plan sur .193](/images/logic-studio/0.1.12-193-fr-documentation.png)

## Deux types de plans

| Plan | Usage et sortie |
| --- | --- |
| Flux de valeurs | Entrées/sorties typées, logique, calcul, sélection, mémoires, fronts, temporisateurs et compteurs. 33 types implémentés ; les autres références sont marquées comme modèles. Export YAML d’automatisation HA, YAML de script HA ou fonction JavaScript avec interface hôte. |
| Flux HA natif | Importer automatisations, scripts et blueprints en blocs imbriqués. 53 types HA supplémentaires : déclencheurs, conditions, branches, boucles, attentes, variables et entrées de blueprint. Export uniquement en YAML HA natif. |

La simulation des flux de valeurs utilise des valeurs de démonstration/instantanées. Les blocs persistants nécessitent les helpers texte HA documentés ou un hôte mémoire JavaScript. Les flux HA natifs ne sont ni exécutés dans l’éditeur ni traduits automatiquement en JavaScript. La sortie JavaScript n’est pas un script ioBroker.

## Connexions à la souris et mini-vue

Maintenir le bouton de la souris sur une borne colorée, faire glisser vers une borne opposée compatible puis relâcher. Le curseur devient une croix et un aperçu du lien suit la souris. Les cibles compatibles sont marquées en vert ; les entrées incompatibles ou occupées en rouge. Le glissement d’une entrée vers une sortie fonctionne aussi. **Échap** ou relâcher sur une zone vide annule ; **Annuler** retire un lien nouvellement créé.

**BOOL se connecte uniquement à BOOL.** Les types identiques sont compatibles ; la conversion élargissante `INT → REAL` est aussi autorisée. Les bornes explicitement `ANY` sont universelles. Nombres et textes ne sont pas convertis implicitement en BOOL. Une entrée accepte un seul lien ; types incompatibles, bornes de même direction, liens vers le même bloc et cycles sont refusés avec une explication. Au clavier, sélectionner la sortie avec Tab/Entrée, puis l’entrée et Entrée.

![Bornes BOOL compatibles reliées à la souris sur .193](/images/logic-studio/0.1.7-bool-verbunden.png)

![Connexion STRING vers BOOL refusée avec une erreur de type explicite](/images/logic-studio/0.1.7-typ-abgewiesen.png)

En bas à droite, la **MiniMap** affiche les positions colorées des blocs et la zone visible. Faire glisser dans la MiniMap pour naviguer et utiliser la molette pour zoomer. Faire glisser le canevas vide déplace la vue ; **+/−** règlent le zoom et **Alles anzeigen** cadre tous les blocs. Déplacer un bloc par son en-tête. L’attribution **React Flow** reste visible en bas à droite. Depuis 0.1.8, la bibliothèque fonctionne réellement dans l’éditeur ; la logique métier, la validation des types et les exportateurs restent propres à Logic Studio.

![Canevas React Flow avec plan original conservé et MiniMap sur .193](/images/logic-studio/0.1.8-react-flow-193.jpg)

![Test local React Flow avec blocs typés](/images/logic-studio/0.1.8-react-flow-local.jpg)

Les images suivantes documentent aussi les tests précédents de 0.1.7.

![Mini-vue avec positions des blocs et cadre visible sur .193](/images/logic-studio/0.1.7-miniuebersicht.png)

## Importation et modification

Ouvrir **HA importieren**, choisir automatisations/scripts/blueprints, puis **Aus HA einlesen**, un fichier YAML/JSON ou du texte. Sélectionner une entrée, vérifier l’aperçu et choisir **Import übernehmen**. Sauvegarder d’abord le projet existant en JSON ; des sauvegardes du projet et des sources sont aussi créées.

Le dossier de configuration HA est monté **en lecture seule**. L’application lit `automations.yaml`, `scripts.yaml` et les fichiers blueprint. Avant analyse, les sources sont copiées sous `/data/ha-source-backups/<horodatage>/` avec leurs noms d’origine. `secrets.yaml` n’est pas ouvert ; `!secret` et `!include` ne sont pas résolus. Importer manuellement les fichiers référencés par les inclusions.

Les liens orange **FLOW** représentent l’ordre et les branches : sortie de branche → **DO**, puis **NEXT → DO**. Les liens jaunes **VALUE/REF** montrent les paramètres de blueprint et leur utilisation `!input`. Configuration HA et chemins de branche sont modifiables en JSON. Les clés de paramètres/champs doivent être uniques. Les sections inconnues restent **YAML_ORIGINAL** ; des liens manquants peuvent bloquer l’export.

![Aperçu d’importation des blueprints HA existants](/images/logic-studio/blueprint-import.png)

Le **menu ⋮** de chaque bloc propose **Eigenschaften** (propriétés), **Duplizieren** (dupliquer) et **Löschen** (supprimer). La duplication copie les propriétés sans liens. La suppression retire les liens associés ; Annuler les restaure. Recherche, favoris et blocs récents facilitent la sélection.

![Menu à trois points d’un bloc](/images/logic-studio/block-menu.png)

## Validation et limites

**0.1.12 sur .193 / HA Core 2026.10.4 :** Application locale mise à jour depuis 0.1.8 après sauvegarde complète. DE/EN/FR, documentation et sélection d’entités HA réelles validés. Le français reste mémorisé après rechargement du navigateur, redémarrage de l’application et nouveau chargement du projet enregistré ; l’allemand a ensuite été rétabli. Le JSON ne diffère **que par la version** : cinq blocs, trois liens, noms, valeurs et positions sont identiques. Le YAML généré est identique en EN et FR. Aucun appareil commandé. **31 tests Node et neuf tests Python** réussis. Les anciens rapports ci-dessous sont conservés comme historique.

![Retour à l’allemand après redémarrage réussi sur .193](/images/logic-studio/0.1.12-193-neustart-de.png)

**0.1.8 sur .193 / HA Core 2026.10.4 :** Application locale existante mise à jour après sauvegarde complète. Connexions BOOL à la souris, refus STRING→BOOL, entrées occupées, déplacement/annulation, duplication, zoom et MiniMap validés. Le sélecteur lit les entités HA ; un script imbriqué avec If/Then/Else, Delay et Stop a été importé puis exporté sans modification de structure. Le plan original a été restauré et comparé après rechargement : **identifiants, positions, paramètres et trois liens inchangés**, ainsi que favoris, blocs récents et catégories repliées. Aucun appareil commandé. Construction Docker et test HTTP du conteneur réussis, ainsi que **29 tests Node et huit tests Python**. Images de l’interface allemande. Le changement clair/sombre n’a pas été retesté manuellement à cette étape.

La base fonctionnelle **0.1.5** a été testée sur **.193 / HA Core 2026.10.4** : import d’un blueprint réel, exemples d’automatisation/script/blueprint, exports YAML identiques sur le fond et actions du menu. **0.1.6** est sa première distribution publique. 22 tests Node et huit tests Python vérifient export, persistance, branches et import sûr ; les contrôles GitHub construisent aussi le conteneur.

**0.1.7 sur .193 / HA Core 2026.10.4 :** tests réels à la souris réussis pour BOOL → BOOL et le sens inverse. STRING → BOOL et une entrée occupée ont été refusés. Mini-vue, navigation par clic et touche Début vérifiées. Le plan original a été rétabli et comparé à sa sauvegarde : **cinq blocs, trois liens et tous les réglages de palette conservés**, y compris après la mise à jour locale vers 0.1.7. Sauvegardes HA complète et projet/réglages séparées créées au préalable ; aucun appareil commandé. **26 tests Node et huit tests Python** réussissent actuellement. Les captures montrent l’interface allemande.

L’éditeur ne valide pas toute la sémantique HA : vérifier cibles, templates et sélecteurs dans HA. Commentaires, ancres YAML et mise en forme ne sont pas reconstruits. Limites : **1 Mo, 200 blocs, 500 liens**, imbrication limitée et jusqu’à 250 fichiers blueprint dans les dossiers habituels. Régulateurs, calendrier et sous-plans personnalisés restent partiellement des modèles.

Pour un test local, extraire tout le ZIP, installer Python 3.10+ et les dépendances `requirements.txt`, puis lancer **Start-Demo.cmd** sous Windows. `http://127.0.0.1:4180/` affiche des entités de démonstration sans connexion HA. Le ZIP contient aussi `addon/logic_studio/` pour une installation locale.

[Signaler les problèmes sur GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/issues) avec versions, architecture et petit exemple anonymisé. Ne pas publier identifiants, automatisations personnelles ou sauvegardes complètes. Guides et rapport de test sont inclus. Licence MIT ; attribution des métadonnées de blocs dans `THIRD-PARTY.txt`.
