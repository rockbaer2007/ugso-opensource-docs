---
title: Interface des paquets de widgets
description: Créer et installer des paquets de widgets locaux pour HA Grafik Visual Studio.
---

# Interface des paquets de widgets {#widget-paket-schnittstelle}

Depuis la version **Studio 0.1.288**, les paquets sont nommés **Industrie**, **Technic**, **Energy**, **Solar**, **Printer** et **Calendar +**, sans le préfixe « UGSo ». Les paquets déjà installés s'affichent désormais avec ces nouveaux noms. Les identifiants techniques des paquets et les définitions des widgets restent inchangés ; les projets existants ainsi que les mises à jour des paquets demeurent compatibles. Les nouveaux téléchargements utilisent également ces noms sans préfixe.

Le paquet externe **Industrie** — incluant des jauges/potentiomètres et leurs paramètres — dispose de sa [propre page dédiée](/fr/projects/grafik-visual-studio/industrial).

## Autres modifications des interfaces {#weitere-schnittstellenanderungen}

À partir de Studio **0.1.266**, l'API 0.2 prend en charge le rendu hôte fixe `calendar-plus` pour [Calendar +](/fr/projects/grafik-visual-studio/calendar-plus). Les calendriers sont détectés automatiquement ; la visibilité et les couleurs sont conservées pour chaque ID d'entité. Cet ensemble dédié dispose de sa propre page dans la barre latérale.

À partir de Studio **0.1.261**, l'API 0.2 prend en charge le rendu hôte fixe `printer-widget` pour l'ensemble autonome [Printer](/fr/projects/grafik-visual-studio/printer). Il lit une entité d'état, des entités optionnelles de type message/performance/page, ainsi qu'un maximum de six entités de niveau actif. Le paquet ne contient pas de scripts exécutables ; l'hôte répartit automatiquement les graphismes des cartouches dans des colonnes de largeur égale.

À partir de Studio **0.1.225**, la couleur définie sous **Paramètres → Général → Éditeur et points d'ancrage → Point de sortie** s'applique également aux sorties des convertisseurs de valeur (*Value Converter*), *LineBox* et *LineBox Math*. Les sorties *Math* connectées conservent cette couleur. Les sorties de signal et les points d'ancrage du boîtier disposent de paramètres de couleur distincts.

À partir de la version **0.1.208**, si la confirmation des risques est omise lors d'un clic sur **Installer**, elle est mise en surbrillance en rouge et l'affichage défile automatiquement pour la rendre visible. Une fois la case cochée, la mise en surbrillance disparaît.

À partir de la version **0.1.207**, l'onglet s'ouvre automatiquement sur le catalogue fraîchement chargé, affichant l'état d'installation actuel. Après une suppression, un paquet publié dans le catalogue redevient disponible à l'installation, même s'il avait été installé localement auparavant. Les nouveaux paquets mis à disposition apparaissent lors de la prochaine ouverture.

Depuis **0.1.205**, les paquets du catalogue et les paquets de widgets installés localement s'affichent sous forme de **deux cartes côte à côte**, chacune dotée d'une icône. Si elle est disponible, l'icône du paquet installé est utilisée ; dans le cas contraire, une icône de widget s'affiche. Les options de mise à jour et de suppression restent disponibles pour les paquets installés.

Depuis la version **0.1.206**, la barre de sélection **Local / Catalogue / GitHub** reste visible en haut lors du défilement. L'ensemble du contenu de l'onglet partage **une zone de défilement unique** ; il n'y a plus de zones de défilement imbriquées pour le catalogue et les paquets installés.

À partir de la version Studio **0.1.204**, la section **Paramètres → Packs de widgets** propose les sources suivantes : **Local / Catalogue / GitHub**. Le [catalogue UGSo](https://visualstudio.ugso-software.de/?kind=widget&lang=de) affiche la description, la licence, la version de Studio requise ainsi que la version installée. Les packs de test sont signalés par une mention orange. GitHub prend en charge les liens directs et publics vers les fichiers `.wg` (y compris les liens de type « blob », « raw » ou « release ») ; un lien vers la page d'accueil d'un dépôt ne suffit pas. Avant toute installation, l'utilisateur doit confirmer explicitement qu'il accepte les risques éventuels. Les téléchargements depuis le catalogue sont vérifiés via une empreinte SHA-256, ainsi que par l'identifiant et la version du pack sélectionné ; la procédure habituelle de vérification des packs s'applique ensuite. La fenêtre des paramètres reste ouverte après l'installation, tandis que la palette et la liste des packs sont mises à jour. Les outils complémentaires autonomes, tels que le « Packer », sont téléchargés via le lien du catalogue.

À partir de la version Studio 0.1.203, l'API 0.2 prend en charge `technic-status-list` : elle permet d'afficher jusqu'à dix lignes de données HA (Home Assistant) en lecture seule, en utilisant les liaisons (« bindings ») ainsi que les options numériques et logiques (ET/OU) de `technic-room`. Les paramètres `valueOffset` et `containerPaddingLeft` permettent de contrôler les colonnes et l'espacement interne. La police est héritée du CSS ; si le contenu dépasse, les lignes deviennent défilantes. Le pack demeure déclaratif. Voir [Technic](/fr/projects/grafik-visual-studio/technic#status-list).

À partir de la version Studio 0.1.202, l'API 0.2 prend en charge `technic-temperature` avec cinq liaisons HA, des limites pour les curseurs, un pas d'incrémentation et des couleurs. L'hôte fixe vérifie les capacités actuelles et les grilles de valeurs avant l'application de `climate.set_temperature` ou `input_number.set_value`. La fonction « Historique » lit les données du « HA-Recorder » pour un maximum de trois entités, sur une période de 24 heures ou de sept jours, et fournit au plus 720 points par série. Les paquets ne contiennent, par ailleurs, aucun script exécutable ni jeton (token) HA. Voir [Technic](/fr/projects/grafik-visual-studio/technic#thermostat-temperature).

À partir de la version Studio 0.1.201, l'API 0.2 prend en charge `technic-clock` pour l'affichage de l'heure du navigateur ainsi que des dates configurables séparément. L'hôte met uniquement à jour le texte via un « ticker » (défilement) commun. Les noms des dates utilisent `Intl`, et le séparateur d'espace est enregistré sous `separator=space`. Aucune liaison d'entité ni fichier de paquet exécutable n'est requis.

À partir de la version Studio 0.1.200, l'API 0.2 prend en charge le moteur de rendu hôte `technic-room` : lecture d'un maximum de dix lignes d'état HA, formatage des nombres, entrées booléennes de type ET/OU, et une fonction locale `targetPage`. Les fenêtres contextuelles (« popups ») de pièce restent ouvertes lors des mises à jour en temps réel ; elles se ferment en cas de changement de page ou de suppression. L'environnement d'exécution (« runtime ») limite la taille des boîtes de dialogue et empêche les imbrications récursives. Le paquet ne contient aucun script exécutable.

À partir de la version Studio 0.1.187, l'**interface 0.2** enrichit les widgets textuels (issus de 0.1) en y ajoutant des diagrammes déclaratifs. Le kit téléchargeable [Météo et Chauffage](/fr/projects/grafik-visual-studio/weather-heating) exploite cette extension. Les kits externes se voient attribuer automatiquement une couleur de palette encore inutilisée, distincte des teintes déjà existantes. Cette attribution est conservée dans le navigateur, même après un rechargement, une suppression ou une réinstallation ; les kits de base et les kits intégrés, quant à eux, conservent leurs couleurs.

## Interface 0.1 : Texte {#schnittstelle-0-1-text}

Depuis la version Studio 0.1.89, il est possible d'installer des paquets au format ZIP portant l'extension `.wg`. Les fichiers utilisant l'ancienne extension `.wg.zip` restent compatibles ; l'extension et le manifeste doivent toutefois correspondre au type de paquet de widgets.

Vous pouvez installer un fichier local de type `.wg` ou `.wg.zip` via le menu **Paramètres → Paquets de widgets → Local**. L'interface 0.1 prend en charge des widgets textuels déclaratifs et vérifiés. À partir de la version Studio 0.1.204, ces widgets apparaissent directement sous forme de kit dédié dans la palette de widgets et sont opérationnels aussi bien dans l'éditeur qu'en phase d'exécution (runtime). L'installation n'entraîne l'exécution d'aucun code contenu dans le paquet.

## Construction du paquet {#paket-aufbauen}

Le fichier ZIP contient, à sa racine, un fichier encodé en UTF-8 nommé `manifest.json`, ainsi que — le cas échéant — des images au format SVG ou PNG (référencées dans le fichier principal) situées sous `icons/`. À partir du Studio 0.1.197, les fichiers `LICENSE.txt` et `README.md` sont également autorisés ; ils doivent être au format texte UTF-8 et ne pas dépasser 50 Ko chacun. Ces documents ne sont ni exécutés ni affichés en tant que HTML dans le Studio. Aucun autre type de fichier n'est admis. L'identifiant de paquet (package ID) utilise une notation par points, par exemple `beispiel.widgets` ; les types de widgets appartiennent à leur propre espace de noms, comme `beispiel.widgets/label`. La version du paquet suit le format `x.y.z`. Un paquet contient entre 1 et 30 widgets ; chacun apparaît comme une entrée distincte dans l'ensemble de paquets de la palette.

À partir du Studio 0.1.197, 0.2 prend en charge `render: {"kind":"technic-window","valueKey":"heading"}`. L'hôte fixe lit `contactEntityId`, `coverEntityId` (`current_position`, `supported_features`) ainsi que `modeEntityId` ; `invertContact`, `invertCover` et `invertMode` inversent les valeurs. L'écriture au moment de l'exécution (runtime) est limitée au contrôle de position d'une entité `cover` disponible et à un mode `input_boolean`/`switch`. Voir [Technic](/fr/projects/grafik-visual-studio/technic).

À partir du Studio 0.1.198, 0.2 complète `render: {"kind":"technic-switch","valueKey":"heading"}`. `entityId` est évalué par rapport à `valueType` (type booléen ou numérique) ; l'écriture au moment de l'exécution est limitée aux entités de type `switch`, `light`, `input_boolean` ou `input_number` (avec des valeurs 0/1). `readOnly` bloque l'utilisation. `iconKey`, `iconScale`, `colorAN`/`colorAUS` ainsi que les options de désignation contrôlent l'affichage fixe.

Dans le Studio, 0.1.199 est complété par 0.2 et `render: {"kind":"technic-light","valueKey":"heading"}`. `powerEntityId` et `brightnessEntityId` sont lus séparément ; la luminosité est extraite de `light.brightness` ou d'une entité de type « helper » numérique. `linkPowerDimmer` associe l'état (marche/arrêt) et la valeur en pourcentage. L'hôte fixe vérifie toutes les cibles pour `/api/light-dimmer` ; les liaisons identiques vers des entités de type « light » sont regroupées en un seul appel. Les cibles distinctes sont traitées comme des actions HA (Home Assistant) séquentielles.

```json
{
  "format": "ha-grafik-widget-package",
  "apiVersion": "0.1",
  "id": "beispiel.widgets",
  "name": "Beispiel Widgets",
  "version": "1.0.0",
  "license": "MIT",
  "widgets": [{
    "type": "beispiel.widgets/label",
    "label": "Label",
    "defaults": { "text": "Hallo" },
    "propertyGroups": [{
      "label": "Inhalt",
      "fields": [{ "key": "text", "label": "Text", "type": "text" }]
    }],
    "render": { "kind": "text", "valueKey": "text" }
  }]
}
```

`valueKey` désigne un champ de texte ou numérique modifiable. Les éléments `text`, `number`, `checkbox`, `color`, `range` et `select` sont prévus pour les propriétés. Chaque propriété doit disposer d'une valeur par défaut appropriée dans `defaults`. Les sections communes **Général** et **Visibilité** sont ajoutées automatiquement par le Studio. Un paquet ou un widget peut également spécifier `"icon": "icons/name.svg"` ou `.png` ; le fichier image correspondant doit alors être inclus dans le fichier ZIP. En l'absence d'image personnalisée pour le widget, le symbole textuel SVG intégré s'affiche.

Le fichier ZIP ne doit pas dépasser 2 Mo, le manifeste 200 Ko, et chaque image 50 Ko. Les images PNG sont limitées à 1024 × 1024 pixels ; les fichiers SVG sont contrôlés pour s'assurer qu'ils ne contiennent que des formes et des attributs passifs. Les images associées aux paquets et aux widgets peuvent être au format SVG ou PNG, tandis que les boutons d'action du Studio conservent leurs symboles SVG.

## Interface 0.2 : Graphique {#schnittstelle-0-2-diagramm}

Le manifeste utilise `apiVersion: "0.2"` et `render: {"kind":"chart","valueKey":"headline"}`. `headline` est un champ texte déclaré avec une valeur par défaut. L'instance enregistre la version de définition 0.2. Le manifeste et les icônes demeurent les seuls fichiers de paquet autorisés ; le Studio effectue le rendu graphique à l'aide de son propre moteur SVG.

Les clés de graphique fixes et les limites sont définies dans le [contrat de graphique](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/widget-rules.md#widget-paket-schnittstelle-02). Il est possible de configurer jusqu'à dix séries JSON, des lignes ou des barres, des axes gauche/droite, des axes temporels ou catégoriels, ainsi que des liaisons en lecture seule vers des états ou attributs HA (Home Assistant). Les formateurs exécutables et les actions d'écriture ne sont pas pris en charge. Les paquets texte existants basés sur 0.1 restent utilisables.

## Installation et gestion {#installieren-und-verwalten}

À partir du Studio 0.1.194, 0.2 prend en charge `render: {"kind":"heating-params","valueKey":"chosenRoomEntityId"}`. L'hôte lit huit liaisons indépendantes (`*EntityId`) correspondant aux paramètres suivants : période de chauffe, jours fériés, présence, mode « fête », invités, vacances (à domicile ou absent) et mode « cheminée ». `chosenRoomEntityId` constitue un affichage textuel optionnel. Les valeurs booléennes `*Preview` non liées ne sont prises en compte que dans l'éditeur. En phase d'exécution, les commutations sont limitées aux entités `input_boolean`/`switch` disponibles ; `readOnly` permet de verrouiller toutes les lignes. Voir [Météo et chauffage](/fr/projects/grafik-visual-studio/weather-heating).

À partir de Studio 0.1.193, 0.2 prend en charge `render: {"kind":"landlord-notification","valueKey":"messageSubject"}`. L'hôte fixe propose un formulaire de message pour l'exécution (runtime). `notificationService` désigne une action `notify.*` spécifique ; `notify.send_message` nécessite `notifyEntityId`. `messageType` décrit le canal configuré, et `messageSubject` le titre textuel. L'envoi ne s'effectue qu'après validation (commande d'envoi), jamais depuis l'éditeur. La priorité est transmise sous forme de texte ; les brouillons ne sont pas inclus dans le format du projet. Voir [Météo et chauffage](/fr/projects/grafik-visual-studio/weather-heating).

À partir de Studio 0.1.192, 0.2 prend également en charge `render: {"kind":"window-overview","valueKey":"windowPreview"}`. L'hôte lit une liste de pièces au format JSON via `entityId` et, éventuellement, `tableAttribute`. `openCountEntityId` et, éventuellement, `openCountAttribute` fournissent un décompte distinct des pièces ouvertes. En l'absence de liaison à une liste, la valeur de prévisualisation est utilisée ; en l'absence de liaison à un décompte, seule une liste entièrement connue et non vide est prise en compte. Les valeurs inconnues restent inconnues. Voir [Météo et chauffage](/fr/projects/grafik-visual-studio/weather-heating).

À partir de Studio 0.1.191, 0.2 prend en outre en charge `render: {"kind":"meteored","valueKey":"meteoredWidgetId"}`. Ce mode hôte fixe charge, lors de l'exécution, le chargeur officiel de Meteored dans un cadre (frame) isolé ; `enableReload` gère le rechargement horaire. Les paquets ne contiennent toujours ni scripts ni URL de chargement personnalisées. L'éditeur affiche un aperçu de la configuration. L'identifiant du fournisseur et l'autorisation de domaine doivent être configurés par l'utilisateur.

À partir de la version Studio 0.1.190, l'interface 0.2 propose également `render: {"kind":"room-table","valueKey":"tablePreview"}`. L'hôte lit `entityId` et, éventuellement, `tableAttribute`, ou utilise la valeur de prévisualisation déclarée si aucune liaison n'est établie. Il reproduit des éléments de tableau HTML passifs ainsi que certains formats ; les contenus exécutables et les ressources externes sont supprimés. Ce nouveau mode nécessite au minimum la version Studio 0.1.190. Le module optionnel [Météo et chauffage](/fr/projects/grafik-visual-studio/weather-heating) sert de référence.

1. Créez un fichier ZIP nommé `mein-paket.wg` contenant les fichiers indiqués. Le format `mein-paket.wg.zip` reste également pris en charge.
2. Accédez à **Paramètres → Packs de widgets** et sélectionnez le fichier ZIP local.
3. Vérifiez les informations affichées : identifiant du pack, version, version de l'API, nombre de widgets et licence. Rechargez l'application via la fonction **Recharger** pour que l'ensemble apparaisse dans la palette.

À partir de la version Studio 0.1.188, l'importation locale permet d'installer une version de paquet supérieure, à condition que l'identité du paquet et toutes les définitions de widgets existantes restent strictement inchangées. Il est possible d'ajouter de nouveaux widgets, y compris au sein de paquets déjà utilisés. Les projets existants ne sont pas modifiés. Toute modification des définitions existantes, toute installation d'une version identique ou toute rétrogradation (downgrade) sera rejetée. La **suppression** reste bloquée tant qu'un type de widget issu du paquet est utilisé dans un projet. L'installation depuis GitHub et les mises à jour automatiques ne sont pas encore disponibles. Les scripts personnalisés, les liaisons avec les états de Home Assistant et les actions d'écriture ne font pas partie de l'interface 0.1.

Les fonctionnalités de base des widgets existants doivent être préservées lors des futures extensions. L'ensemble des règles ainsi que les fonctionnalités prévues sont détaillés dans les [règles relatives aux widgets dans le code source](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/widget-rules.md).
