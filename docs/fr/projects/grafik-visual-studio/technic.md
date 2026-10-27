---
title: Technic
description: Installez le jeu de widgets externe « Technic » et connectez « Window – Wall » à Home Assistant.
---

# Technic {#technic}

À partir de **Studio 0.1.296**, le thermostat propose en outre une fonction [Climate](/fr/projects/grafik-visual-studio/ha-quellen-climate) (gestion du climat) — désactivée par défaut — incluant : deux consignes, modes de fonctionnement, préréglages, ventilation, oscillation, humidité et marche/arrêt, selon les capacités de l'appareil. Les propriétés du widget et les messages d'exécution sont disponibles en allemand, anglais et français ; les paramètres existants restent valides.

Les paquets et outils complémentaires sont proposés de manière centralisée sur [visualstudio.ugso-software.de](https://visualstudio.ugso-software.de/?lang=de). Ce site open source contient des descriptions et des instructions ; le téléchargement s'effectue via le catalogue de paquets.

**Inspiré des [widgets « Technic » pour ioBroker créés par Sefina-DS](https://github.com/Sefina-DS/ioBroker.vis-2-widgets-technic).** Adaptation spécifique pour Home Assistant.

À partir de **Studio 0.1.203**, vous pouvez installer **Technic 1.6.0**. Ce paquet contient les sept types de widgets : **Window – Wall**, **Switch – Boolean**, **Dimmer – Light**, **Room – Overlay**, **Clock – Date**, **Thermostat – Temperature** et **Status – List**. La version 1.6.0 peut être installée via le gestionnaire de paquets en tant qu'extension des versions précédentes ; les widgets existants sont conservés.

## Status – List {#status-–-list}

![Liste d'états affichant la température et l'état d'une fenêtre ; données de test simulées pour HA](/images/grafik-visual-studio/technic-status-runtime.png)

La liste d'états affiche jusqu'à **dix lignes d'état en lecture seule**. Par défaut, le nombre de lignes est réglé sur **0** ; le widget apparaît alors vide. Taille par défaut : **160 × 120 pixels**. Dans la section **Lignes d'état**, vous pouvez configurer le nombre de lignes, le **décalage de la colonne des valeurs (90 px)** et la **marge gauche du conteneur (8 px)**. Le décalage détermine la largeur de la colonne des libellés ; la colonne des valeurs commence ensuite, avec un espacement de 4 px. L'espacement gauche du conteneur s'ajoute à la marge interne fixe de 8 px.

Selon le nombre défini, les **lignes d'état [1]** à **[10]** s'affichent. Chaque ligne se voit attribuer une étiquette et une entité Home Assistant. Le type **Nombre** prend en charge les unités, les décimales et la couleur des chiffres. Le type **Vrai / Faux** permet de définir des textes et des couleurs pour les états ON/OFF, ainsi que des entités supplémentaires (séparées par des virgules) combinées par des opérateurs **ET** ou **OU**. Les champs d'origine `oid1` à `oid10` correspondent aux champs Studio `rowEntityId1` à `rowEntityId10` ; les champs `oidsExtra1` à `oidsExtra10` correspondent aux champs `extraEntityIds1` à `extraEntityIds10`.

Les valeurs manquantes, inconnues ou indisponibles sont traitées comme `—`. La taille de la police, la police elle-même, le style gras et la couleur de l'étiquette sont définis via **CSS → Police et texte**. Les étiquettes ou valeurs trop longues sont tronquées avec des points de suspension ; le texte complet est alors visible dans une info-bulle (tooltip). Si vous utilisez des unités longues, augmentez la largeur du widget ; l'exemple illustré utilise 240 pixels. Si le nombre de lignes est trop élevé, un défilement (scroll) est activé au sein du widget. Les clics ne modifient pas les états dans Home Assistant et ne masquent pas les étiquettes. Toutes les lignes et tous les espacements sont conservés lors de l'exportation du projet ou du widget.

## Thermostat – Température {#thermostat-–-temperature}

![Contrôleur de température après une modification de la consigne ; l'étiquette reste visible](/images/grafik-visual-studio/technic-temperature-runtime.png)

Le régulateur de température affiche la température de consigne/réelle, l'humidité, l'état du servomoteur et le mode refroidissement. Taille standard : **220 × 220 pixels**, plage **15–28**, pas de **0,5**. Dans la section **Général**, vous pouvez configurer le libellé, l'affichage, la position (haut/bas), la taille de l'icône et la protection en écriture. Dans la section **Régulateur**, vous définissez les limites et le pas ; la section **Couleurs** permet de configurer les états MARCHE, ARRÊT et Refroidissement.

| Champ d'origine | Liaison Studio | Home Assistant |
| --- | --- | --- |
| `oid_temp_soll` | Température de consigne | `climate` (avec consigne unique) ou `input_number` |
| `oid_temp_ist` | Température réelle | Capteur de température ou `climate.current_temperature` |
| `oid_feuchtigkeit` | Humidité | Capteur (en pourcentage) ou `climate.current_humidity` |
| `oid_stellmotor` | Servomoteur | Capteur 0–100 %, état booléen ou `climate.hvac_action` |
| `oid_kuehlmodus` | Mode refroidissement | État booléen ou état de refroidissement d'une entité `climate` |

Les liaisons de lecture laissées vides utilisent les attributs correspondants de l'entité de consigne `climate`. Avec l'`input_number`, des capteurs distincts sont nécessaires. Une activité de chauffage/refroidissement correspond à **100 %**, tandis qu'un état inactif/éteint correspond à **0 %** ; il ne s'agit pas ici de la position mesurée de la vanne. Les valeurs manquantes ou indisponibles sont traitées via l'`—`.

En mode exécution (runtime), vous pouvez manipuler l'**arc à 300°** ou utiliser le curseur via le clavier. L'écriture (`climate.set_temperature` ou `input_number.set_value`) ne s'effectue qu'au moment du relâchement. Le système vérifie au préalable les capacités et limites actuelles de Home Assistant (HA), ainsi que les pas d'incrémentation. Toute incompatibilité de grille, état inconnu, protection en écriture ou mode édition empêche l'opération d'écriture. Le curseur modifie uniquement la valeur de consigne ; le mode de fonctionnement et l'état marche/arrêt ne sont pas affectés. En cas d'erreur liée à Home Assistant, un message s'affiche ; les libellés restent visibles.

![Historique sur sept jours avec températures de consigne et réelle, ainsi qu'un axe séparé pour le servomoteur ; données de test simulées](/images/grafik-visual-studio/technic-temperature-history.png)

La fonction **Historique** affiche les données sur **24 heures** ou **7 jours** en puisant dans l'**enregistreur (Recorder) de Home Assistant**. Les températures de consigne et réelle utilisent l'axe des températures, tandis que le servomoteur utilise l'axe des pourcentages situé à droite. Les trois couleurs sont configurables dans la section **Historique (HA-Recorder)**. Les valeurs inconnues entraînent une interruption de la courbe. L'enregistreur doit capturer les entités sélectionnées et conserver les données pour la période souhaitée. Ici, le paramètre ioBroker `influxInstance` est remplacé par les données issues de l'enregistreur Home Assistant. Toutes les liaisons, options d'affichage et couleurs sont préservées lors de l'exportation du projet ou du widget. Les illustrations sont issues d'un test local utilisant des réponses simulées de Home Assistant.

## Horloge – Date {#clock-–-date}

![Horloge en temps réel avec affichage des secondes et date en allemand](/images/grafik-visual-studio/technic-clock-runtime.png)

L'horloge affiche l'**heure locale et le fuseau horaire du navigateur**. Elle ne nécessite aucune entité HA (Home Assistant). L'affichage se met à jour chaque seconde sans redessiner les autres widgets ; si l'onglet du navigateur a été mis en pause, l'heure actuelle est réactualisée lors de sa réactivation.

Dans la section **Général**, vous pouvez définir la disposition (côte à côte ou l'un en dessous de l'autre), l'alignement (gauche, centre ou droite), l'espacement, un arrière-plan optionnel, le rayon des coins et la marge intérieure. La taille par défaut est de 260 × 90 pixels. Les dates longues ou les polices de grande taille nécessitent davantage d'espace ; le contenu qui dépasse reste accessible via une barre de défilement.

Dans la section **Heure**, vous pouvez configurer l'affichage, le format 12/24 heures, les secondes, la couleur, la taille de la police et le style en gras. Le format 12 heures utilise les mentions AM/PM. Dans la section **Date**, vous pouvez configurer séparément l'affichage, la couleur, la taille de la police et le style en gras.

La langue utilisée pour la date est indépendante de la langue de l'interface Studio : allemand, anglais, français, espagnol, italien ou néerlandais. Différents formats sont disponibles : jour-mois-année, mois-jour-année ou année-mois-jour ; les séparateurs peuvent être des points, des tirets, des barres obliques ou des espaces. Le mois peut être affiché sous forme numérique, abrégée ou complète ; l'année peut être indiquée sur deux ou quatre chiffres, et un zéro peut être ajouté devant le jour si nécessaire. Le jour de la semaine peut être masqué, affiché en format abrégé ou complet. Les noms des mois et des jours sont issus des paramètres linguistiques du navigateur. Toutes ces options sont conservées lors de l'exportation du projet ou du widget.

## Pièce – Superposition (Overlay) {#room-–-overlay}

![Tuile de pièce avec libellé visible et page de destination du studio ouverte](/images/grafik-visual-studio/technic-room-popup.png)

La tuile de pièce affiche un **nom de pièce** personnalisable ainsi que jusqu'à **dix lignes d'état**. Il est possible de configurer la couleur du nom, la taille de la police, le style gras, l'alignement horizontal et vertical, ainsi que les quatre marges internes. Taille par défaut : 160 × 100 pixels.

Dans la section **Lignes d'état**, vous définissez le nombre de lignes, la taille de la police et la couleur du texte. Les lignes peuvent être disposées les unes en dessous des autres ou horizontalement, avec des séparateurs et des espacements. Les groupes correspondants, de **Ligne d'état [1]** à **[10]**, s'affichent en fonction du nombre choisi.

Chaque ligne se voit attribuer un libellé et une entité Home Assistant. Pour le type **Nombre**, il est possible de définir une unité, le nombre de décimales et la couleur du chiffre. Pour le type **Vrai / Faux**, vous pouvez configurer le texte et la couleur pour les états MARCHE/ARRÊT, ainsi qu'ajouter des entités supplémentaires (séparées par des virgules) combinées par des opérateurs **ET** ou **OU**. Les valeurs manquantes, inconnues ou indisponibles s'affichent sous la forme `—` ; elles ne sont pas considérées comme étant à l'état « éteint ». Les données sont traitées en mode lecture seule.

Dans la section **Comportement au clic / Popup**, sélectionnez une **page cible Studio** existante. L'option **Popup** ouvre l'instance d'exécution de cette page dans une fenêtre modale (dialogue), tandis que **Changer de page** permet d'y accéder directement. Une vue ioBroker doit d'abord être reproduite en tant que page Studio. Si aucune cible valide n'est définie, la tuile ne déclenche aucune action ; les auto-références et les inclusions récursives sont interdites. Dans l'éditeur, un clic permet de sélectionner l'élément.

Il est possible de configurer la largeur et la hauteur de la fenêtre contextuelle (popup), sa position X/Y fixe (au lieu d'un centrage automatique), ainsi que l'arrière-plan, la couleur et l'épaisseur de la bordure, et le rayon des coins. Vous pouvez également définir la fermeture au clic en dehors de la fenêtre, l'affichage d'un bouton de fermeture, et une fermeture automatique après un certain nombre de secondes (la valeur `0` désactive cette fonction). La touche **Échap** permet toujours de fermer la fenêtre. La popup reste ouverte lors des mises à jour en temps réel ; son libellé demeure visible. La fenêtre se ferme automatiquement lors d'un changement de page ou de la suppression de la tuile. La taille est limitée aux dimensions de l'écran. Tous les paramètres sont conservés lors de l'exportation du projet ou du widget.

## Installation {#installieren}

Téléchargez le fichier [ugso.technic.wg](https://visualstudio.ugso-software.de/?kind=widget&lang=de). Accédez à **Paramètres → Packs de widgets → Installer un fichier .wg / .wg.zip local** et sélectionnez le fichier. Après un rechargement, l'ensemble apparaît, associé automatiquement à une couleur disponible. Ce composant est indépendant des widgets intégrés, ainsi que des modules liés à la météo et au chauffage.

Le [code source et la procédure de construction reproductible du paquet](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/technic) sont accessibles au public. Le paquet téléchargeable contient les éléments `README.md` et `LICENSE.txt`, incluant le texte intégral de la licence MIT ainsi que la mention d'origine `Copyright (c) 2026 Sefina-DS`.

## Fenêtre – Mur {#window-–-wall}

Dans la section **Général**, vous pouvez configurer le libellé, l'option **Afficher le libellé**, la position (haut/bas), la taille de l'icône (10–100 %), le côté de la poignée (gauche/droite) et la couleur de l'icône. La taille par défaut est de 120 × 160 pixels. L'option **Lecture seule** verrouille l'utilisation.

Sous **Points de données**, vous trouverez trois liaisons HA (Home Assistant) indépendantes :

| Champ d'origine | Champ Studio | Home Assistant |
| --- | --- | --- |
| `oid_kontakt` | Contact d'ouverture : Entité | par ex. `binary_sensor.fenster_garage` ; `on` signifie « ouvert » |
| `oid_rollo` | Volet roulant : Entité « cover » | par ex. `cover.rollo_garage` ; lit `current_position` |
| `oid_modus` | Mode : Entité | par ex. `input_boolean.rollo_manuell` ; désactivé = Automatique, activé = Manuel |

Chaque liaison dispose de sa propre option d'inversion. **Inverser le volet** inverse l'affichage ainsi que la valeur d'écriture (`100 − Position`). En fonctionnement normal, 0 signifie « fermé » et 100 signifie « ouvert ». Une valeur inconnue reste inconnue, même après inversion. Le contact est uniquement lu. Un symbole **A/M** (optionnel) indique le mode ; `?` indique un mode inconnu.

![Composant Technic installé et liaisons HA dans l'éditeur](/images/grafik-visual-studio/technic-window-editor.png)

## Utilisation {#bedienung}

En mode exécution (Runtime), un clic sur la fenêtre ouvre une boîte de dialogue dotée d'un curseur de position, de valeurs rapides (**0 / 25 / 50 / 75 / 100 %**) et d'une option de changement de mode. L'utilisation est également possible via le clavier ; la touche Échap ou le bouton **Fermer** permettent de quitter la boîte de dialogue. L'action liée au volet roulant utilise exclusivement l'entité `cover.set_cover_position`. La commande de position (`supported_features` avec SET_POSITION) est vérifiée avant toute écriture. Le changement de mode ne s'applique qu'aux entités `input_boolean` ou `switch` disponibles. Un capteur reste un simple élément d'affichage.

L'assistant de mode ne représente que l'interrupteur : vous devez configurer l'automatisation réelle des volets roulants dans Home Assistant. Aucune automatisation n'est créée ou désactivée par ce biais. En cas d'échec d'une action, une notification s'affiche et permet de retenter l'opération ; les actions en attente ne sont pas envoyées en double.

![Boîte de dialogue en mode exécution avec position du volet et changement de mode](/images/grafik-visual-studio/technic-window-runtime.png)

## Interrupteur – Booléen {#switch-–-boolean}

L'interrupteur reprend les options de configuration de `tplTechnicSchalterBoolean`. Paramètres par défaut : **Device** (appareil), libellé visible en bas, dimensions 120 × 160 pixels, icône d'alimentation affichée à 80 %, couleur pour l'état ACTIF (`#2dd4b0`) et couleur pour l'état INACTIF (`#5f8f8a`).

Le **point de données (MARCHE/ARRÊT)** permet de lier l'entité Home Assistant. **Type de valeur → Vrai / Faux** : lit les états `on`/`off` et permet de commuter les éléments `switch`, `light` ou `input_boolean` via `turn_on`/`turn_off`. **0 / 1** : lit exclusivement les valeurs 0 et 1 et écrit des valeurs numériques dans un élément auxiliaire `input_number`. Les limites et le pas de cet élément doivent être compatibles avec ces valeurs. Les capteurs conservent leur rôle d'indicateurs ; les états inconnus, manquants ou non disponibles ne peuvent pas être commutés.

**Sélectionner une icône** : propose 16 types de symboles : sélection, PC de bureau, alimentation, lampe de chevet, suspension, suspension ronde, lampe de bureau, spots, ruban LED RGB, lampe de table, lien, ventilateur, clé, smartphone, prise de courant et TV. Il s'agit de dessins géométriques SVG originaux, et non de simples tracés graphiques importés. La couleur (pour les états MARCHE/ARRÊT) et la taille sont réglables. L'option « Sélection » affiche une coche uniquement lorsque l'état est MARCHE.

Un clic sur le symbole déclenche la commutation en mode exécution (runtime) ; l'intitulé reste visible. L'utilisation au clavier est possible via les touches Tab et Entrée/Espace. L'option **Lecture seule** empêche toute modification. Les actions en cours ne sont pas envoyées en double ; en cas d'erreur, un message s'affiche et permet de réessayer. **MARCHE (Aperçu)** ne s'applique que dans l'éditeur, lorsque l'élément n'est pas lié. Tous les paramètres sont conservés dans le projet et lors de l'exportation.

![Commutateur après activation, avec intitulé visible](/images/grafik-visual-studio/technic-switch-runtime.png)

## Variateur – Éclairage {#dimmer-–-light}

Correspond aux options de `tplTechnicReglerLicht` : libellé **Light** (Éclairage), affiché en bas ; taille de l'icône : 80 %, dimensions : 160 × 200 pixels. **Couleur (activé)** correspond à `#2ecfbf`, **Couleur (désactivé)** à `#5f8f8a`, et **Arrière-plan du curseur** à `#0d1820`. La taille, les couleurs et la position du libellé sont configurables ; l'affichage repose sur une implémentation SVG spécifique.

Le champ **On/Off : Entité** accepte `light`, `switch` ou `input_boolean`. Le champ **Luminosité : Entité (0–100)** accepte une entité dimmable (`light`) ou un « helper » (élément auxiliaire) de type numérique (`input_number`). Pour un éclairage HA (Home Assistant) standard, saisissez **la même entité « light » dans les deux champs**. Le système convertit l'attribut HA `brightness` (plage 0–255) en pourcentage. Lorsque l'éclairage est éteint, la valeur affichée est 0 %. L'élément auxiliaire numérique doit être configuré avec : min = 0, max = 100 et pas (step) = 1. Les capteurs peuvent afficher des valeurs, mais ne permettent pas de contrôle.

L'option **Lier On/Off à la luminosité** est activée par défaut : l'état « activé » définit la luminosité à 100 %, l'état « désactivé » à 0 %, et toute modification de la luminosité au-dessus de 0 allume l'éclairage. Les deux entités liées doivent être disponibles et inscriptibles. Si la même entité « light » est utilisée, une seule commande HA est générée. Sans cette liaison, les entités restent indépendantes ; toutefois, une action sur la luminosité via `light.turn_on` entraînera tout de même l'allumage de l'éclairage concerné. 0 % utilisé `light.turn_off`.

Faites glisser l'arc de cercle extérieur ou utilisez le curseur (via le clavier). La valeur s'affiche localement pendant le déplacement et n'est transmise qu'au moment du relâchement. Le bouton central « Power » permet d'allumer ou d'éteindre (ON/OFF). L'étiquette reste visible. L'option **Lecture seule** bloque toute action ; les entités inconnues ou non dimmables ne peuvent pas être manipulées. Les valeurs en temps réel manquantes ne sont pas remplacées par des valeurs de prévisualisation. Les paramètres **ON (Prévisualisation)** et **Luminosité (Prévisualisation)** ne s'appliquent que dans l'éditeur, pour les éléments non liés.

L'hôte vérifie toutes les cibles avant la première opération d'écriture. Dans le cas d'entités distinctes, les appels vers HA (Home Assistant) sont exécutés les uns après les autres ; une erreur côté fournisseur peut entraîner une application partielle de l'action. Le message d'erreur invite à vérifier l'état actuel avant toute nouvelle tentative. Les actions en cours ne sont pas envoyées en double. Le fonctionnement a été validé avec des entités HA simulées ; le matériel réel doit faire l'objet de tests distincts.

![Contrôleur d'éclairage en exécution (runtime) réglé à 50 % avec étiquette visible](/images/grafik-visual-studio/technic-light-runtime.png)

## Prévisualisation et exportation {#vorschau-und-export}

La **Prévisualisation** propose des options pour l'état des fenêtres, la position des volets roulants et le mode manuel. Ces valeurs ne s'appliquent que dans l'éditeur, pour les affichages non liés. En cas de liaison, ce sont les valeurs en temps réel qui sont lues. En mode exécution (runtime), les valeurs non liées ou manquantes restent inconnues ; elles ne sont pas remplacées par des valeurs de prévisualisation. Dans l'éditeur, les clics ne déclenchent aucune action de commutation dans HA.

Toutes les options d'affichage, les trois liaisons d'entités, les inversions, les valeurs de prévisualisation et la protection en écriture sont conservées lors de l'exportation du projet et du widget. Le test a été effectué avec des entités HA simulées ; une commande de volets roulants réelle doit être testée avec votre propre matériel.
