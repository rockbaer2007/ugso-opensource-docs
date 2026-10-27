---
title: Météo et chauffage
description: Installer et configurer le paquet optionnel de widgets graphiques.
---

# Météo et chauffage {#wetter-und-heizung}

Les paquets et outils complémentaires sont proposés de manière centralisée sur [visualstudio.ugso-software.de](https://visualstudio.ugso-software.de/?lang=de). Ce site open source contient des descriptions et des instructions ; le téléchargement s'effectue via le catalogue de paquets.

**Inspiré par les widgets « Météo et chauffage » pour ioBroker, créés par [rg-engineering](https://github.com/rg-engineering/ioBroker.vis-2-widgets-weather-and-heating).** Les widgets Studio constituent une implémentation spécifique pour Home Assistant.

À partir de **Studio 0.1.194**, vous pouvez installer le paquet **« Météo et chauffage » 1.7.0**. Il comprend : un **graphique général**, un **graphique en barres sur deux semaines**, un **widget météo**, une **vue d'ensemble des pièces chauffées**, un **widget météo METEORED**, un **suivi de l'état des fenêtres**, une fonction pour **informer le propriétaire** et les **paramètres généraux de chauffage**. La référence fonctionnelle est [ioBroker.vis-2-widgets-weather-and-heating](https://github.com/rg-engineering/ioBroker.vis-2-widgets-weather-and-heating) ; toutefois, Studio utilise ses propres modes de représentation. D'autres widgets liés à la météo et au chauffage, ainsi que des intégrations spécifiques aux adaptateurs ioBroker, ne sont pas encore inclus.

## Installation {#installieren}

Téléchargez [ugso.weather-heating.wg](https://visualstudio.ugso-software.de/?kind=widget&lang=de). Accédez à **Paramètres → Packs de widgets → Installer un fichier .wg / .wg.zip local** et sélectionnez le fichier. Après un rechargement, un nouvel ensemble apparaît, doté d'une couleur attribuée automatiquement. L'attribution de cette couleur est conservée dans le navigateur, même en cas de suppression et de réinstallation. Les 74 widgets intégrés restent disponibles.

## Configurer le diagramme {#diagramm-konfigurieren}

Vous pouvez mettre à jour un pack installé (de 1.0.0 à 1.6.0) vers la version 1.7.0 en utilisant la même procédure d'importation. Les widgets existants et les valeurs de projet sont conservés. Les mises à jour ne peuvent qu'ajouter de nouveaux widgets ; toute modification des définitions existantes ou toute tentative de retour à une version antérieure (downgrade) sera rejetée.

## Paramètres généraux de chauffage {#allgemeine-heizparameter}

Le widget affiche huit lignes : **Période de chauffage active**, **Jour férié aujourd'hui**, **Présent**, **Fête en cours**, **Invités présents**, **Vacances à domicile**, **Vacances (absent)** et **Mode cheminée**. Dans la section **Entités des paramètres de chauffage**, vous pouvez associer une entité HA spécifique à chaque ligne. L'entité « pièce » (choisie en option) s'affiche sous forme de texte au-dessus des commutateurs ; elle n'est pas modifiée. L'instance `heatingcontrol.0` initiale n'est pas requise.

En mode exécution (runtime), les entités `input_boolean.*` et `switch.*` disponibles peuvent être commutées (activées/désactivées) via l'état `on`/`off`. Chaque action n'agit que sur l'entité cliquée. Les capteurs, comme `binary_sensor.*`, servent uniquement d'affichage. Pendant l'exécution d'une commande, l'entité concernée est verrouillée ; les erreurs sont signalées via l'état de commutation existant dans Studio. L'option **Général → Lecture seule** bloque toutes les actions de commutation. L'option **Sans carte** supprime l'arrière-plan de carte externe.

Les lignes non liées sont désactivées en mode exécution et marquées comme **Non lié**. Si des valeurs liées sont manquantes ou indisponibles, l'état affiché est **Inconnu**, accompagné d'un commutateur hachuré. Aucune valeur de prévisualisation n'est utilisée comme valeur en temps réel. Les cases à cocher situées sous **Prévisualisation** ne s'appliquent qu'à l'éditeur pour les éléments non liés ; aucune commande de commutation n'y est envoyée non plus.

L'ensemble des neuf liaisons d'entités, valeurs de prévisualisation, paramètres de lecture seule et options d'affichage sont conservés dans le projet ainsi que lors de l'exportation du widget. Le widget regroupe vos entités HA (Home Assistant) existantes ; il ne calcule pas les durées de chauffage, les jours fériés ou la présence, et ne contient pas de système de régulation de chauffage propre.

![Paramètres généraux de chauffage et leurs liaisons d'entités](/images/grafik-visual-studio/weather-heating-params.png)

## Informer mon propriétaire {#meinen-vermieter-informieren}

Le widget propose les champs **Priorité** (Information, Important, Urgent), **Message** et **Envoyer**. Dans l'éditeur, il s'agit d'une prévisualisation. Lors de l'exécution, les données ne sont transmises à Home Assistant que lorsqu'une action d'envoi est explicitement déclenchée. Les messages vides ainsi que les clics répétés survenant pendant une transmission en cours sont ignorés. En cas d'erreur, le message est conservé pour une nouvelle tentative ; si Home Assistant (HA) l'accepte, il est supprimé. L'acceptation par HA ne confirme pas la bonne réception effective du message.

Sous la rubrique **Général**, vous trouverez les options suivantes : **Sans carte**, **Type de message**, **Action de notification HA**, **Entité de notification** et **Objet / En-tête du message**. Exemple : utilisez l'action `notify.send_message` avec votre entité spécifique `notify.vermieter`. Vous pouvez également utiliser une action nommée préalablement configurée, telle que `notify.vermieter_email` ; dans ce cas, le champ « Entité » reste vide. L'identifiant générique `notify.notify` n'est pas accepté. Les destinataires, les identifiants d'accès et les fournisseurs de services doivent être configurés dans Home Assistant, et non dans le widget. Consultez la section [Notifications HA](https://www.home-assistant.io/integrations/notify/).

Les types de messages — e-mail, WhatsApp, Signal, Pushbullet et Jira — correspondent au canal configuré. Ce choix n'installe aucun fournisseur de service et ne modifie pas automatiquement la destination dans Home Assistant. L'instance ioBroker d'origine, `email.0`, est remplacée par votre action Home Assistant. Dans la version initiale, seul l'envoi par e-mail est implémenté ; toutefois, l'interface Studio utilise la même configuration HA pour tous les canaux paramétrés.

Le titre et la priorité sont insérés sous forme de texte avant le message, par exemple `Meinen Vermieter informieren` et `[urgent]`. La priorité ne correspond pas à un niveau de distribution ou d'alerte spécifique à un fournisseur. Limites : 10.000 caractères pour le message, 200 caractères pour le titre. Les brouillons sont conservés lors des mises à jour d'état HA (Home Assistant), mais uniquement dans le formulaire actuel : un changement de page ou un rechargement les supprime. Les exportations de projets ou de widgets incluent la configuration, mais pas les messages saisis.

![Formulaire de message et configuration de la cible HA dans l'éditeur](/images/grafik-visual-studio/weather-heating-landlord.png)

## Aperçu de l'état des fenêtres {#fensterstatus-ubersicht}

Dans la section **Liste des fenêtres**, vous sélectionnez une entité HA et, éventuellement, un attribut contenant une liste JSON. Le point de données d'origine se nomme `WindowStatesHtmlTableVis2`, mais il contient du JSON. En l'absence de liaison avec une entité, le widget utilise l'aperçu modifiable :

```json
[
  {"room":"Wohnzimmer","sinceText":"seit","changed":"03.10.2026 12:30","isOpen":true},
  {"room":"Küche","sinceText":"seit","changed":"03.10.2026 11:00","isOpen":false}
]
```

`isOpen` accepte les valeurs booléennes, 1/0, ainsi que les textes `true`/`false`, `on`/`off` et `open`/`closed`. Si l'état est absent, le widget reconnaît les anciens noms d'icônes `fts_window_1w_open.svg` et `fts_window_1w.svg`, sans pour autant charger de fichiers image. Sinon, la mention **Inconnu** s'affiche. Les textes relatifs aux pièces et aux modifications sont affichés sous forme de texte brut, et non en HTML. Limites : 200.000 caractères JSON, 500 pièces et 512 caractères par champ de texte.

**Pièces ouvertes : Entité** et un attribut optionnel fournissent un nombre entier non négatif. Sont comptées les pièces dont les fenêtres sont ouvertes. Sans cette liaison, le nombre est déduit uniquement à partir d'une liste non vide contenant des états entièrement connus. En l'absence de données liées, aucune prévisualisation n'est utilisée ; un nombre inconnu est explicitement affiché.

Sous **Couleurs**, on trouve le titre, la ligne d'état, le nom de la pièce (ouvert/fermé), l'heure de la dernière modification (ouvert/fermé) et l'arrière-plan de la pièce. Par défaut, l'état « ouvert » utilise le rouge, l'état « fermé » le vert, et l'heure de modification associée le bleu. L'affectation suit les noms des champs ; l'inversion présente dans l'original n'est pas reprise. Une couleur d'arrière-plan spécifique est utilisée, indépendante de la valeur de thème ioBroker `background.paper`. L'option **Général → Sans carte** supprime l'arrière-plan extérieur de la carte. Les paramètres sont conservés dans le projet ainsi que lors de l'exportation du widget.

Votre entité HA doit déjà fournir la liste JSON ; le widget n'agrège pas les capteurs de fenêtre individuels et ne modifie pas les états dans HA. Aucun adaptateur `heatingcontrol` n'est requis.

![Aperçu de l'état des fenêtres avec les pièces ouvertes et fermées](/images/grafik-visual-studio/weather-heating-windows.png)

Sous **Général**, vous trouverez le titre, le nombre de séries (1–10), la légende et l'option d'affichage sans carte. La première série peut utiliser l'entité générale. Chaque groupe **Données [N]** propose sa propre entité, un attribut optionnel, un JSON de prévisualisation, des clés X/Y, un nom, une unité, une couleur, un type (ligne/barre), un axe des valeurs (gauche/droite) et un calcul de différence. Avec une liaison à une entité, le graphique lit exclusivement son état ou son attribut. En l'absence de données en temps réel, aucun JSON de prévisualisation n'est utilisé. Aucune écriture d'états dans HA (Home Assistant) n'est effectuée.

Exemple de JSON de prévisualisation ou d'attribut HA :

```json
[
  {"x":"2026-10-03T08:00:00","value":12},
  {"x":"2026-10-03T09:00:00","value":18},
  {"x":"2026-10-03T10:00:00","value":15}
]
```

Les clés par défaut sont `x` et `value` ; il est également possible d'utiliser des clés personnalisées ainsi que des paires `[x,y]`. Le champ **Temps** attend des dates au format ISO ou des millisecondes Unix. Le champ **Catégorie** permet d'afficher du texte, par exemple des années. Les points temporels sont triés avant le calcul des différences. Les valeurs manquantes interrompent la ligne et la séquence des différences ; la première différence n'a pas de prédécesseur. Les axes gauche et droit sont mis à l'échelle indépendamment.

L'**axe X** utilise la clé standard `ddd HH:mm` pour les étiquettes. Jetons (tokens) pris en charge : `YYYY`, `MM`, `DD`, `ddd`, `HH`, `mm`, `ss`. Les couleurs sont définies sous **WIDGET → CSS Graphique**. Jusqu'à 20.000 lignes de saisie sont acceptées ; Les séries volumineuses sont limitées à un maximum de 500 points par série. Le widget ne récupère pas l'historique HA (Home Assistant) : l'entité sélectionnée doit déjà fournir le tableau de données.

![Ensemble installé avec aperçu du graphique](/images/grafik-visual-studio/weather-heating-chart.png)

## Graphique en barres sur deux semaines {#balkendiagramm-fur-zwei-wochen}

Les groupes **Semaine actuelle** et **Semaine précédente** contiennent chacun sept entités HA (du lundi au dimanche), ainsi que des valeurs de prévisualisation modifiables. Le widget compare les paires de jours côte à côte. Il ne calcule pas lui-même l'historique hebdomadaire et ne décale pas les valeurs lors du passage à la semaine suivante : vos capteurs doivent fournir la valeur correspondant à chaque jour.

L'option **Afficher les valeurs hebdomadaires** fonctionne de la même manière que l'option originale « Visible » : si elle est désactivée, le widget affiche uniquement les valeurs de prévisualisation ; si elle est activée, il lit exclusivement les 14 entités journalières. Les valeurs « live » non liées, indisponibles ou non numériques ne génèrent pas de barres. Zéro est une valeur valide. La visibilité globale du widget se gère toujours via le paramètre **Visibilité**.

Dans la section **Général**, vous pouvez configurer le titre et sa couleur, la couleur du texte de la légende, l'unité, les couleurs des semaines, la couleur des étiquettes des axes, le positionnement de l'axe Y (gauche/droite), le nombre de décimales (0 à 5), la légende et l'option **Sans carte**. L'**axe X** dispose de sa propre couleur. Les unités et les valeurs formatées apparaissent dans la légende et dans les infobulles des barres ; les jours de la semaine s'affichent dans la langue de l'application. Les couleurs sont appliquées selon vos réglages.

![Graphique en barres sur deux semaines dans l'ensemble installé](/images/grafik-visual-studio/weather-heating-two-weeks.png)

## Widget météo {#wetter-widget}

La **Source de données** propose `home-assistant`, `json` et `individual`. La **Structure des données** permet de sélectionner cinq valeurs journalières (`daily`) ou jusqu'à 24 valeurs horaires (`hourly`). Ces sources remplacent la sélection de l'instance ioBroker et de l'OID par des liaisons (bindings) vers HA (Home Assistant).

Avec `home-assistant`, vous sélectionnez une entité `weather.*`. Le serveur Studio récupère les prévisions via [weather.get_forecasts](https://www.home-assistant.io/integrations/weather/). Les réponses valides sont mises en cache pendant cinq minutes ; en cas d'erreur, une nouvelle tentative est effectuée après un délai minimal d'une minute. L'intégration météo utilisée doit prendre en charge le type de prévision choisi. Les unités de température et de précipitations sont extraites des attributs correspondants. Une véritable récupération des données depuis HA nécessite une connexion active à l'add-on ou au Supervisor.

Avec `json`, le widget lit l'**attribut de prévision (JSON)** sélectionné ; s'il est vide, l'état de l'entité est utilisé. Un tableau (array) est attendu, par exemple :

```json
[{"datetime":"2026-10-03T12:00:00Z","temperature":18,"templow":10,"precipitation":0,"cloud_coverage":25,"precipitation_probability":40}]
```

Avec `individual`, vous associez les **dates [1–5]** ou les **horaires [1–24]**, ainsi que les valeurs correspondantes pour la température, les précipitations, la couverture nuageuse et la probabilité, à des capteurs individuels. Les données temporelles doivent être au format ISO ou exprimées en millisecondes Unix. Les vues journalières n'utilisent que les cinq premières liaisons de chaque groupe de valeurs. Les moments non valides sont omis ; les valeurs manquantes interrompent les lignes. La valeur zéro est considérée comme valide. En l'absence d'entité météo ou JSON liée, les deux premières sources affichent des données de prévisualisation modifiables. Les données en temps réel manquantes ne sont jamais remplacées par des valeurs de prévisualisation.

Les paramètres **Température**, **Pluie**, **Nuages** et **Probabilité de pluie** peuvent être activés individuellement. Chaque groupe dispose de ses propres couleurs et d'un axe des valeurs (gauche ou droite) ; les précipitations sont représentées sous forme de barres. L'option **Afficher dans le second graphique** crée une zone graphique distincte. Si des unités différentes sont présentes sur un même axe, elles sont automatiquement séparées. L'option **Soleil ou nuages** affiche la couverture nuageuse (ou son complément) en pourcentage ; elle n'indique pas la durée d'ensoleillement. Les valeurs manquantes fournies par la source ne sont pas estimées à partir de l'état du temps. Il est possible de configurer le nom, l'entité de localisation (optionnelle), la légende, les couleurs, le format de date sur l'axe X, la taille, ainsi que l'option **Sans carte**.

![Widget météo affichant la température et les précipitations](/images/grafik-visual-studio/weather-heating-weather.png)

## Aperçu des chaufferies {#ubersicht-uber-heizraume}

À partir de **0.1.190**, ce widget affiche un tableau de pièces au format HTML, généré à partir du point de données source `RoomStatesHtmlTable`. Dans la section **Tableau de pièces**, vous sélectionnez une entité HA (Home Assistant) et, éventuellement, un **attribut de tableau**. Si aucun attribut n'est spécifié, c'est l'état (state) de l'entité qui est utilisé. En cas de liaison, le widget exploite exclusivement cette valeur en temps réel ; si la valeur est absente ou indisponible, le message **Aucun tableau de pièces disponible** s'affiche. En l'absence de liaison avec une entité, le champ **Aperçu du tableau de pièces (HTML)** peut être modifié, y compris via l'éditeur HTML.

Ce widget ne génère pas de données relatives aux pièces ni de profils de chauffage, et ne pilote aucun thermostat. Aucune instance ioBroker (telle que `heatingcontrol.0`) n'est requise ; la source HA sélectionnée doit déjà fournir le tableau sous forme de chaîne HTML. Il est recommandé de placer les contenus HTML volumineux dans un attribut plutôt que dans l'état (state).

Les options **Général → Sans carte**, **Couleurs → Couleur des en-têtes**, ainsi que les paramètres de taille et les réglages CSS communs sont disponibles. La structure des tableaux, la mise en forme du texte, les fusions de cellules (cell spans) ainsi que les couleurs et espacements définis sont conservés. Les scripts, gestionnaires d'événements, formulaires, contenus intégrés (embeds) et ressources externes sont supprimés. La saisie est limitée à 200.000 caractères, et l'affichage est restreint à 5.000 nœuds avec un maximum de 40 niveaux d'imbrication. Les tableaux volumineux peuvent faire l'objet d'un défilement (scroll) à l'intérieur du widget. Tous les paramètres sont préservés lors de l'exportation du widget ou du projet.

![Aperçu de la chaufferie avec tableau de prévisualisation](/images/grafik-visual-studio/weather-heating-rooms.png)

## Widget météo METEORED {#meteored-wetter-widget}

À partir de **0.1.191**, vous trouverez dans la section **Général** les options **Sans carte**, **ID du widget Meteored** et **Activer le rechargement**. Créez votre widget sur [Meteored / daswetter.com](https://www.daswetter.com/widget/) et saisissez uniquement son identifiant (ID) ; n'entrez ni code HTML complet, ni URL. Sont autorisés : 1 à 128 caractères (lettres, chiffres, traits de soulignement ou traits d'union). N'oubliez pas d'autoriser, sur le site du fournisseur, le nom de domaine depuis lequel vous accédez réellement à l'interface d'exécution (runtime).

L'interface d'exécution charge le chargeur officiel `https://api.meteored.com/widget/loader/ID` dans un cadre (frame) séparé. Un accès à Internet ainsi qu'une configuration valide auprès du fournisseur sont requis. L'option **Activer le rechargement** est activée par défaut et déclenche un rechargement une fois par heure. Si vous la désactivez, le minuteur s'arrête ; toute modification ou suppression de l'identifiant entraîne la suppression de l'ancien minuteur. Le simple rafraîchissement de l'interface d'exécution ne relance pas le cadre ni son minuteur. Dans l'éditeur, un aperçu de la configuration s'affiche ; si l'identifiant est vide ou invalide, aucun contenu n'est chargé.

Le frame utilise `sandbox="allow-scripts"` ; la page de chargement (*loader*) reçoit le même environnement isolé (*sandbox*) via son en-tête HTTP. Ainsi, le code Meteored s'exécute sans accès au DOM du Studio. Le widget ne nécessite aucune entité HA et reprend le lieu, la langue et la mise en forme définis dans votre configuration Meteored. Ces trois options, ainsi que la taille et le CSS, sont conservées lors de l'exportation. Une vérification complète de l'affichage du fournisseur nécessite votre véritable identifiant de widget et un domaine autorisé.

![Configuration METEORED dans l'éditeur](/images/grafik-visual-studio/weather-heating-meteored.png)

La construction reproductible du paquet et le manifeste vérifié sont disponibles dans le [code source](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/weather-heating). Le [contrat de paquet](/fr/projects/grafik-visual-studio/widget-packages) décrit l'interface 0.2.
