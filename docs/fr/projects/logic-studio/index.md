---
title: Logic Studio
description: HA Logic Studio Pro 0.1.98 · Conservation des journaux d’exécution
---
# <img class="package-icon" src="/images/logic-studio/icon.svg" width="40" height="40" alt=""> Logic Studio

**0.1.12 – mise à jour publique de test, 8 novembre 2026.** Interface et documentation sont désormais disponibles en **DE/EN/FR**. Logic Studio est une application HA autonome pour les plans à blocs fonctionnels, indépendante de Grafik Visual Studio et Blocks for HA. Le canevas React Flow conserve ses blocs personnalisés, connexions typées, zoom et MiniMap ; bibliothèques et licences sont incluses localement.

::: warning Version de test
Installer d’abord sur un système de test et créer une sauvegarde complète. Les propriétés natives détaillées sont actuellement modifiables en JSON. L’application ne réécrit pas les automatisations/scripts dans HA et ne commande aucun appareil. Vérifier et installer soi-même les sorties générées.
:::

[Version de test GitHub et ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/logic-studio-v0.1.12) · [Sources dans le dépôt commun](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/logic_studio)

## HA Logic Studio Pro

HA Logic Studio Pro est une application Home Assistant autonome dans le dépôt commun UGSo. Elle s’appuie sur Logic Studio et sur l’expérience acquise avec ioBroker.

**Fonctionnalités disponibles**

- **Diagramme fonctionnel :** Relier les blocs, afficher les signaux aux entrées et simuler le diagramme. Sur le serveur HA, l’exécution peut réagir aux changements ou suivre un cycle fixe.
- **Règles et Blocks A :** Créer des automatisations dans un éditeur visuel et les exporter au format YAML de HA.
- **Blocks JS, JavaScript et TypeScript :** Modifier la logique, la tester avec des valeurs simulées et l’exécuter sur le serveur HA.
- **YAML HA :** Modifier, valider et exporter les automatisations et les scripts.
- **Gestion des projets :** Enregistrer les projets et les dossiers sur le serveur pour chaque utilisateur HA.
- **Choix de la langue :** Les éditeurs sont disponibles en allemand, en anglais et en français.

La version **0.1.62** a ajouté les fonctions de règles décrites ci-dessous.

### HA Logic Studio Pro 0.1.121–0.1.140

**0.1.125 · Message ioBroker avec réponse dans Blocks JS**

Blocks JS importe `sendto_custom` avec ses paramètres nommés et sa branche de réponse. À l’importation, il est possible d’associer une action de script HA qui renvoie des données. Lors du test avec Play et un véritable export Blockly d’ioBroker sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc), les paramètres `left: 17` et `right: 25` ont donné **42**. La branche de réponse a lu `result.total` et journalisé **42**.

[HA Logic Studio Pro 0.1.125 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.125)

**0.1.124 · Liaison directe ioBroker dans Blocks JS**

Blocks JS importe le bloc ioBroker `direct` avec des associations distinctes pour la source et la cible ainsi que l’option « uniquement en cas de changement ». Lors du test avec Play et un véritable export Blockly sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc), le passage de la source de **0** à **53** a écrit **53** dans l’assistant cible. La cible a ensuite été réglée sur **7** pour la vérification. Quand seul un attribut de la source a changé et que sa valeur est restée à **53**, la cible est restée à **7**.

[HA Logic Studio Pro 0.1.124 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.124)

**0.1.123 · Import de valeurs asynchrones dans Blocks JS**

Blocks JS importe `get_value_async` avec l’association à une entité HA et la branche de réponse. Le bloc « Valeur lue » renvoie la valeur sélectionnée dans cette branche. Lors du test avec Play et un véritable export Blockly d’ioBroker sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc), le script a lu et journalisé **52**, puis écrit **52** dans un assistant numérique HA associé séparément.

[HA Logic Studio Pro 0.1.123 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.123)

**0.1.122 · Points de données ioBroker associés aux assistants HA**

Blocks JS importe `createState` avec les blocs de lecture et de mise à jour. Dans la boîte de dialogue d’importation, on peut associer un assistant HA existant, en créer un ou reporter l’association.

Lors du test en conditions réelles sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc), Blocks JS a créé un assistant numérique avec la valeur initiale **17**. Le script a lu **17**, écrit **42**, puis relu **42** après son redémarrage. L’export Blockly d’ioBroker a produit le même espace de travail et a servi à vérifier dans Chrome l’association à un assistant existant.

[HA Logic Studio Pro 0.1.122 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.122)

**0.1.121 · Onglets compacts et enregistrement groupé**

Chaque onglet réunit le nom du projet, un carré rouge pour les modifications non enregistrées et le bouton de fermeture. Un trait bleu indique l’onglet actif.

Dans Chrome, **Tout enregistrer** est resté masqué avec un seul onglet modifié. Avec deux onglets modifiés, le bouton est apparu entre **Enregistrer** et **Annuler**. Les deux modifications étaient toujours présentes après le clic et le rechargement. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.121 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.121)

### HA Logic Studio Pro 0.1.101–0.1.120

**0.1.120 · Lecture asynchrone d’objet et enregistrement de tous les onglets**

Blocks JS importe `get_object_async` avec une association explicite à une entité HA. Lors du test avec le bouton Play sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc), la branche de réponse a renvoyé le nom affiché **Logic Studio Runtime Test** via `common.name`.

**Tout enregistrer** apparaît lorsque plusieurs onglets sont ouverts. Ce bouton enregistre ensemble les modifications de tous les projets ouverts. Un carré rouge signale chaque onglet contenant des modifications non enregistrées.

[HA Logic Studio Pro 0.1.120 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.120)

**0.1.119 · Import du sélecteur ioBroker**

Blocks JS importe le sélecteur ioBroker `$()` sous forme de bloc de liste. L’expression d’origine reste visible sur le bloc. Les entités HA associées explicitement lors de l’import sont enregistrées dans une liste fixe. Lors du test avec le bouton Play sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc), la boucle importée a journalisé une fois chacun des deux identifiants `input_boolean.logic_studio_runtime_test` et `input_number.ugso_rules_080_level`.

[HA Logic Studio Pro 0.1.119 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.119)

**0.1.118 · Import des membres d’une catégorie ioBroker**

Blocks JS importe `get_enum_members` avec l’option « états uniquement » activée. Lors de l’import, la catégorie est associée à une zone ou à une étiquette Home Assistant. Lors du test avec le bouton Play sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc), la boucle importée a journalisé une seule fois chacun des deux identifiants de l’étiquette HA. Le journal affichait `input_boolean.logic_studio_runtime_test` et `input_number.ugso_rules_080_level`.

[HA Logic Studio Pro 0.1.118 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.118)

**0.1.117 · Import du déclencheur de catégorie ioBroker**

Lors de l’import de `onEnumMembers`, Blocks JS associe la catégorie à une zone ou à une étiquette Home Assistant et enregistre les entités correspondantes. Sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc), un export Blockly a été associé à une étiquette HA comprenant deux assistants de test. Le script en cours d’exécution a journalisé `input_boolean.logic_studio_runtime_test` avec la valeur `true` et `input_number.ugso_rules_080_level` avec la valeur `42.0`. Le changement d’état de `counter.ugso_rules_080_count`, en dehors de l’étiquette, n’a produit aucune sortie.

[HA Logic Studio Pro 0.1.117 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.117)

**0.1.116 · Import du déclencheur de journal ioBroker**

Blocks JS importe `onLog` et les blocs qui lisent le message et le niveau de journalisation. Un export Blockly ioBroker réel a été importé sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc). Lorsque l’événement `system_log_event` a été déclenché manuellement dans Home Assistant avec le niveau `WARNING`, le script a journalisé le message et `warn`. L’événement de contrôle avec `ERROR` n’a produit aucune sortie. Pour recevoir les événements du journal générés automatiquement, activez `system_log.fire_event` dans Home Assistant et autorisez `system_log_event` dans `runtime_events` dans l’application.

[HA Logic Studio Pro 0.1.116 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.116)

**0.1.115 · Indication sur le déclencheur de modification de fichier ioBroker**

Sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc), l’import d’un export Blockly ioBroker réel contenant `onFile` a conservé le motif `ugso-115-*.txt` et le bloc de nom de fichier `onFile_data` dans le rappel. L’indication figurait dans le récapitulatif de l’import et directement sur le bloc. Elle explique comment une automatisation Home Assistant avec Folder Watcher lit le nom via `trigger.to_state.attributes.file`.

[HA Logic Studio Pro 0.1.115 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.115)

**0.1.114 · Indication sur l’ancien bloc GET ioBroker**

Sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc), l’import d’un export Blockly ioBroker réel contenant `request` a conservé l’URL GET et la branche de réponse avec `result`. L’indication figurait dans le récapitulatif de l’import et directement sur le bloc. Elle explique comment passer à « HTTP GET · HA REST » et associer `result`, `response.statusCode` et `error` aux blocs de réponse. Le test a vérifié l’import et l’indication.

[HA Logic Studio Pro 0.1.114 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.114)

**0.1.113 · Indication sur le bloc ioBroker « Lire un fichier »**

Sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc), l’action native `file.read_file` de Home Assistant a renvoyé `data.probe = 42` pour le fichier JSON de test. L’import de l’export Blockly ioBroker réel dans Blocks JS a conservé le nom du fichier et le bloc `file_data` imbriqué dans le rappel. L’indication figurait dans le récapitulatif de l’import et directement sur le bloc. Elle explique comment traiter le contenu dans un script Home Assistant avec `response_variable` et `.data`.

[HA Logic Studio Pro 0.1.113 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.113)

**0.1.112 · Indication sur le bloc ioBroker « Écrire un fichier »**

Sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc), Blocks JS a importé un export Blockly ioBroker réel contenant `file_write`. Le bloc de remplacement a conservé les entrées de l’objet de stockage, du nom de fichier et du contenu. L’indication figurait dans le récapitulatif de l’import et directement sur le bloc. Elle explique comment `notify.send_message` ajoute du texte à un fichier configuré et quand un service dédié est nécessaire pour reproduire le comportement d’écriture d’origine.

[HA Logic Studio Pro 0.1.112 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.112)

**0.1.111 · Indication sur le bloc de fichier ioBroker**

Sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc), l’import d’un export Blockly ioBroker réel a conservé le nom de fichier `ugso-111-probe.txt`. L’indication figurait dans le récapitulatif de l’import et directement sur le bloc. Elle précise que `downloader.download_file` lance une requête GET distincte. Pour enregistrer la réponse déjà reçue et réutiliser le chemin du fichier, il faut configurer un service dédié. Après la reconstruction locale, l’en-tête du Studio dans Chrome affichait `0.1.111`.

[HA Logic Studio Pro 0.1.111 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.111)

**0.1.110 · Indication pour le type de réponse HTTP arraybuffer**

Blocks JS conserve l’export Blockly ioBroker avec `arraybuffer` sous forme de bloc de remplacement identifié. Lors du test de contrôle avec Play, en mode texte, Home Assistant a renvoyé les quatre octets `00 41 C3 A9` sous forme de **trois caractères**. `byteLength` valait `null`. Pour `00 41 FF 80`, Home Assistant a signalé une erreur de décodage et Blocks JS n’a reçu aucun octet. L’indication sur le bloc explique qu’un point de terminaison peut renvoyer les données binaires en **Base64 dans du JSON**. Il faut adapter le traitement de la réponse. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

Lors du test suivant avec Play sur le système de test PC (64), une fonction JavaScript dans Blocks JS a décodé le champ Base64 de la réponse JSON et obtenu les octets `00 41 FF 80`. Le journal d’exécution a affiché la suite d’octets et la longueur `4`.

[HA Logic Studio Pro 0.1.110 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.110)

**0.1.109 · Gestion des réponses JSON invalides**

Lors du test avec Play, les deux réponses JSON invalides ont atteint la branche d’erreur. Quand Home Assistant n’a pas pu décoder la réponse JSON, la branche a reçu un message explicite et le statut HTTP était `null`. Quand Blocks JS a lui-même analysé le texte invalide, il a signalé « Réponse JSON invalide. » et conservé **HTTP 200**. Dans la même exécution, la requête valide suivante a renvoyé **`42`** et le script a continué. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.109 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.109)

**0.1.108 · Type de réponse HTTP JSON dans les imports ioBroker**

Blocks JS importe le type de réponse `json` et permet d’accéder directement aux champs de la réponse. Lors du test avec Play, l’export Blockly ioBroker d’origine avec conversion JSON en objet et la variante XML adaptée avec `TYPE=json` et accès direct ont tous deux renvoyé **`42`** pour **`result.value`**. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.108 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.108)

**0.1.107 · URL HTTP calculées dans les imports ioBroker**

Blocks JS conserve l’expression d’URL ioBroker. La commande REST HA autorisée définit l’hôte et le préfixe fixe de l’URL. Blocks JS transmet la partie variable dans `url_suffix`. Lors du test GET avec Play, le point de terminaison a reçu **`garten & 42`** comme valeur unique du paramètre de requête et a renvoyé **HTTP 200**. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

Lors du **test POST avec Play** réalisé ensuite à partir d’un export Blockly ioBroker, le point de terminaison a reçu dans la même requête la valeur calculée `garten & 42` et le corps JSON `{"probe":42}`. Il a renvoyé **HTTP 200**. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.107 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.107)

**0.1.106 · En-têtes de requête dans les imports POST ioBroker**

Blocks JS conserve les valeurs Content-Type personnalisées des blocs POST ioBroker. Le bloc affiche la valeur importée pour configurer la commande REST de HA. Lors du test réel avec Play, le point de terminaison a confirmé **`Content-Type: application/vnd.ugso+json`** et **`Accept: application/json`**. La requête POST a renvoyé HTTP 200 et transmis la valeur JSON `42`. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.106 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.106)

**0.1.105 · Gestion des erreurs HTTP dans Blocks JS**

Blocks JS importe le bloc d’erreur ioBroker pour les requêtes HTTP. Lors de deux essais réels avec Play, le script importé a d’abord journalisé **HTTP 404**. Au second appel, une **erreur de connexion** a atteint la branche d’erreur sans statut HTTP. Le moteur d’exécution est resté actif dans les deux cas. Lors d’un autre essai réel avec Play, un point de terminaison lent a provoqué un **dépassement du délai HTTP**. La branche d’erreur s’est exécutée sans statut HTTP (`null`), puis le script a continué à tourner. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.105 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.105)

**0.1.104 · En-têtes de réponse HTTP dans Blocks JS**

Blocks JS importe les en-têtes de réponse d’ioBroker. Leurs noms sont convertis en minuscules pour permettre la lecture d’une clé comme `content-type`. Lors du test réel avec Play, la requête GET a renvoyé **`Content-Type: application/json`**. Le script importé a lu cet en-tête et inscrit `application/json` dans le journal. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.104 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.104)

**0.1.103 · Import HTTP POST dans Blocks JS**

Blocks JS importe HTTP POST depuis ioBroker avec le corps JSON, la vérification du statut et le traitement de la réponse. Lors du test réel avec Play, le point de terminaison temporaire a reçu `{"probe":42}` et renvoyé le **statut 200**. Le script importé a lu le champ JSON `value` et inscrit **42** dans le journal. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.103 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.103)

**0.1.102 · Import HTTP GET dans Blocks JS**

Blocks JS importe HTTP GET depuis ioBroker avec la vérification du statut et le traitement du JSON. Pour exécuter le bloc, associez-lui une commande REST Home Assistant autorisée. Lors du test réel, la requête HTTP a renvoyé le **statut 200**. Le script importé a lu le champ JSON `value` et inscrit **42** dans le journal. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.102 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.102)

**0.1.101 · Indication sur le bloc exec importé**

Dans l’export de test ioBroker, le bloc `exec` reçoit la comparaison « heure actuelle avant 12:00 ». Le test a confirmé que l’indication apparaît dans le récapitulatif d’import et directement sur le bloc de substitution Blockly. La comparaison est conservée. Le commentaire explique comment la brancher sur « si » et placer l’action HA souhaitée dans « faire ». [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.101 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.101)

### HA Logic Studio Pro 0.1.81–0.1.100

**0.1.100 · Condition de modèle dans Rules**

Le mode expert permet d’ajouter une condition Jinja. Rules l’exporte comme condition de modèle native de Home Assistant. Lors du test, ALORS a activé l’assistant de test et SINON l’a désactivé. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.100 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.100)

**0.1.99 · Validation de la structure des branches HA YAML imbriquées**

L’éditeur HA YAML signale les erreurs de structure dans les branches `choose` imbriquées à la ligne concernée. Sur le système de test, l’éditeur a signalé la **ligne 10**. Les 159 octets de l’export du blueprint étaient identiques, y compris les paramètres et le champ supplémentaire. Les essais JavaScript et TypeScript ont tous deux indiqué la **ligne 2**. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.99 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.99)

**0.1.98 · Conservation des journaux d’exécution**

Les journaux d’exécution sont conservés jusqu’à **30 jours** par projet, dans la limite de **64 Kio** et de **100 entrées**. Le nettoyage s’applique aussi aux projets arrêtés. Le test en conditions réelles a supprimé une entrée vieille de 31 jours et réduit un fichier de **84 240 à 65 430 octets**. La nouvelle entrée d’exécution était toujours consultable dans le projet de test arrêté après le redémarrage de l’application. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.98 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.98)

**0.1.97 · Échange Blocks JS et mémoire du diagramme fonctionnel**

Dans Blocks JS, la vue des identifiants d’entité affiche aussi l’identifiant ioBroker d’origine du bloc importé sélectionné. Les indications d’import ont été vérifiées avec les exports d’origine `test33.xml` et `test33.js`. Le bloc de mise à jour sélectionné et sa valeur connectée ont été importés dans un brouillon séparé à partir d’un texte JSON et d’un fichier.

Dans le diagramme fonctionnel, le plan enregistré a conservé la valeur `1` du compteur et la valeur `true` du bistable après le redémarrage de l’application et la relance du plan. Les tests automatisés du moteur d’exécution vérifient le redémarrage avec une entrée déjà active et l’abandon des anciennes valeurs après une modification des connexions. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.97 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.97)

**0.1.96 · Groupes de conditions et catalogues de cibles Blocks A**

**Règles.** Les groupes ET, OU et NON imbriqués peuvent être combinés avec des identifiants de déclencheur. Lors du test en conditions réelles dans HA, `first` a exécuté la branche ALORS. Une condition interne a bloqué `second`, ce qui a exécuté SINON. La trace a confirmé l’attente d’un état, le paramètre de script `42`, la notification et l’événement final. La zone et l’étiquette ont sélectionné la même entité de test. Pour actualiser la liste des entités après une modification des affectations, il suffit de sélectionner à nouveau la zone ou l’étiquette.

**Blocks A.** La zone, l’étiquette, l’appareil de bouclage et l’étage de test étaient tous disponibles dans le sélecteur de cibles. Le brouillon YAML HA contenait les identifiants correspondants sous `area_id`, `label_id`, `device_id` et `floor_id`. Les objets de test ont ensuite été supprimés. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.96 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.96)

**0.1.95 · Condition « Déclenché par » dans Règles**

Chaque déclencheur peut avoir un **identifiant facultatif**. La condition **Déclenché par** utilise l’un de ces identifiants et s’exporte sous la forme `condition: trigger` dans le YAML HA. Lors du test en conditions réelles, l’événement HA associé à l’identifiant `first` a exécuté la branche **ALORS**. L’événement associé à `second` a exécuté la branche **SINON**. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.95 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.95)

**0.1.94 · Associer le YAML HA à une automatisation ou à un script**

Le bouton **Associer une entrée HA** permet de lier un projet YAML à une automatisation ou à un script existant. Après enregistrement, l’éditeur affiche son statut et l’heure du dernier déclenchement si elle est disponible. Sur le système de test PC (64), l’automatisation de test a été désactivée, réactivée puis déclenchée avec vérification des conditions. Le script de test a été démarré puis arrêté. Les liens ont été conservés après rechargement. Le bouton **Annuler** a restauré le lien enregistré. [Système de test PC (64)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.94 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.94)

**0.1.93 · Réexport YAML avec des instances de plans directeurs**

Le réexport YAML conserve le contenu d’origine, y compris les champs supplémentaires, les commentaires, les balises YAML, le chemin du plan directeur et ses entrées. Sur le système de test PC (64), le fichier de test du couloir avec des champs imbriqués supplémentaires et une instance de plan directeur ont été importés puis réexportés. La comparaison SHA-256 a confirmé que les deux exports étaient identiques octet pour octet aux fichiers importés. Chrome a conservé le suffixe `.crdownload` pour les deux fichiers pendant le test.

[HA Logic Studio Pro 0.1.93 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.93)

**0.1.92 · Insérer des entités et des actions au curseur YAML**

Utilisez **Insérer une entité** ou **Insérer une action HA** pour insérer l’identifiant choisi à la position du curseur. Si du texte est sélectionné, l’identifiant le remplace. Lors du test de l’automatisation du couloir sur le système de test PC (64), `sun.sun` et `homeassistant.turn_off` ont été insérés exactement aux emplacements du curseur prévus. Les trois branches `choose` sont restées visibles.

[HA Logic Studio Pro 0.1.92 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.92)

**0.1.91 · Vérification du catalogue Home Assistant dans l’éditeur YAML**

L’éditeur YAML signale dans le code les entités inconnues, les champs cibles invalides et les champs d’action absents du catalogue Home Assistant. La vérification du catalogue ignore les modèles dynamiques. Lors du test de l’automatisation du couloir sur le système de test PC (64), l’éditeur a signalé une entité inconnue à la **ligne 28** et un champ `light.turn_on` invalide à la **ligne 45**. Les deux marqueurs ont disparu après correction. Les trois branches `choose` sont restées visibles.

[HA Logic Studio Pro 0.1.91 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.91)

**0.1.90 · Coloration syntaxique et erreurs dans YAML HA**

L’éditeur YAML HA affiche la coloration syntaxique et les numéros de ligne. Les erreurs sont signalées dans le code et dans la marge. Lors du test de l’automatisation du couloir sur le système de test PC (64), l’éditeur a signalé une clé `mode` dupliquée volontairement à la **ligne 79**. Après correction, le marqueur a disparu et les trois branches `choose` sont restées visibles.

[HA Logic Studio Pro 0.1.90 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.90)

**0.1.89 · Import JSON dans YAML HA**

Utilisez **Importer du JSON** pour sélectionner un fichier ou coller son contenu. La configuration validée s’ouvre comme brouillon YAML. Sélectionnez **Enregistrer** pour la conserver.

Sur le système de test PC (64), les fichiers `Flur.automation.json` de Logic Studio Pro et `flur test.flode.json` de FLODE ont été importés via le sélecteur de fichiers. Les deux imports ont produit un YAML équivalent et conservé les trois branches `choose` pour basculer, allumer et éteindre.

[HA Logic Studio Pro 0.1.89 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.89)

**0.1.88 · Aperçu graphique du YAML HA**

La carte « Choisir » est centrée entre les branches et affiche en permanence les libellés des connecteurs. Sur le système de test PC (64), l’automatisation du couloir affichait **Option 1**, **Option 2**, **Option 3** et **Par défaut**. Les sept connexions étaient visibles, les cartes ne se chevauchaient pas et le texte YAML est resté identique après le changement de vue.

[HA Logic Studio Pro 0.1.88 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.88)

**0.1.87 · React Flow**

L’aperçu graphique du YAML HA utilise React Flow avec une grille de points fine, des cartes compactes, une minicarte, le zoom, le déplacement et le cadrage global. Chaque carte `choose` présente une sortie nommée par option et une sortie par défaut. Le graphe est en lecture seule. Les modifications se font dans l’éditeur YAML.

Les trois sorties de l’automatisation du couloir ont été vérifiées sur le système de test PC (64). Les cartes sont restées distinctes malgré les identifiants d’entité longs, et le texte YAML était identique après le retour dans l’éditeur.

[HA Logic Studio Pro 0.1.87 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.87)

**0.1.86 · Aperçu graphique du YAML HA**

L’aperçu graphique affiche les déclencheurs, les conditions et les actions sous forme de cartes. Pour une action `choose`, il présente chaque branche avec ses conditions et ses actions.

Sur le système de test PC (64 bits), l’automatisation du couloir affichait les quatre déclencheurs et les trois branches `choose`. Les deux fichiers YAML téléchargés étaient identiques octet pour octet. La comparaison avec la configuration saisie a confirmé la conservation de tous les champs, dont les identifiants des déclencheurs, l’identifiant de l’appareil et les options d’événement, les entités cibles, les décalages solaires et `mode: restart`. [Système de test PC (64 bits)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.86 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.86)

**0.1.85 · Plages horaires et jours de la semaine dans les règles**

**Plage horaire et jours de la semaine** permet de combiner une heure de début, une heure de fin et les jours souhaités. Il est aussi possible de choisir uniquement les jours. L’export utilise la condition native `condition: time` de Home Assistant.

Lors du test en conditions réelles, l’automatisation s’est exécutée uniquement quand l’heure et le jour correspondaient. Hors de la plage horaire ou lorsque le jour ne correspondait pas, les assistants de test sont restés désactivés. [Système de test PC (64 bits)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.85 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.85)

**0.1.84 · Déclencheur au démarrage de Home Assistant**

La palette et l’assistant de règles proposent **Démarrage de Home Assistant**. L’export YAML utilise `trigger: homeassistant` avec `event: start`.

Lors du test en conditions réelles, l’automatisation a activé l’assistant de test après le redémarrage de Home Assistant Core. [Système de test PC (64 bits)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.84 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.84)

**0.1.83 · Déclencheurs MQTT dans les règles**

L’assistant de règles propose **Message MQTT** avec un topic obligatoire et un filtre de contenu facultatif. Sans filtre, tout message publié sur ce topic déclenche l’automatisation.

Lors du test en conditions réelles, l’automatisation s’est exécutée une seule fois, lorsque le topic et le contenu correspondaient. Un autre topic et un contenu différent n’ont déclenché aucune exécution. La trace Home Assistant a confirmé l’action sur le compteur. [Système de test PC (64 bits)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.83 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.83)

**0.1.82**

L’assistant de règles propose le déclencheur **Heure depuis un assistant**. Sélectionnez un assistant Home Assistant de type `input_datetime` qui inclut une heure. L’export YAML utilise `trigger: time` et indique l’identifiant de l’entité sous `at`. Home Assistant prend en compte les modifications de l’heure dans cet assistant.

Lors du test en conditions réelles sur le système de test PC (64 bits), l’heure de l’assistant a été modifiée de 17:27:27 à 17:27:56. L’automatisation ne s’est pas déclenchée à l’heure initiale. La trace Home Assistant confirme son exécution à **17:27:56**. [système de test PC (64 bits)](/fr/collection/test-systems#testsystem-pc)

[HA Logic Studio Pro 0.1.82 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.82)

**0.1.81**

L’assistant de règles propose le lever et le coucher du soleil comme déclencheurs. Le décalage facultatif se saisit en minutes. Une valeur négative déclenche la règle avant l’événement solaire et une valeur positive la déclenche après.

L’export YAML a été vérifié et validé dans la version installée sur le [système de test PC (64 bits)](/fr/collection/test-systems#testsystem-pc). Pour 30 minutes avant le lever du soleil, il a généré `event: sunrise` et `offset: -1800`. Pour 15 minutes après le coucher du soleil, il a généré `event: sunset` et `offset: 900`. Les décalages du YAML sont exprimés en secondes.

[HA Logic Studio Pro 0.1.81 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.81)

### HA Logic Studio Pro 0.1.61–0.1.80

::: details Historique des versions

**0.1.80**

L’assistant de règles propose le déclencheur **Seuil numérique** avec une limite inférieure, une limite supérieure ou les deux pour définir un intervalle. L’attribut et la durée minimale sont facultatifs. L’export YAML utilise le déclencheur natif `numeric_state` de Home Assistant.

Sur le [système de test PC (64 bits)](/fr/collection/test-systems#testsystem-pc), l’éditeur installé a généré `above: 50` pour le seuil « Au-dessus de 50 ». Lors du test du YAML exporté dans Home Assistant, l’automatisation s’est déclenchée une fois à 51. Le compteur est resté à 1 à 65 puis à 49. Il est passé à 2 lors du nouveau franchissement du seuil à 52.

[HA Logic Studio Pro 0.1.80 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.80)

**0.1.79**

L’aperçu de l’import dans Blocks JS indique, pour chaque bloc, l’entité Home Assistant à associer ou la modification de code encore nécessaire. Les identifiants ioBroker fixes peuvent être associés à des entités HA directement dans l’aperçu.

Sur le [système de test PC (64 bits)](/fr/collection/test-systems#testsystem-pc), l’export original `test33.xml` a permis d’associer le déclencheur d’état à un capteur et le bloc d’écriture à un assistant numérique. Le test a simulé l’écriture des valeurs `21` et `20`.

[HA Logic Studio Pro 0.1.79 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.79)

**0.1.78**

Dans **Scripts globaux**, les projets JavaScript et TypeScript peuvent sélectionner des scripts enregistrés dans le dossier du même nom. La boîte de dialogue indique comment appeler les fonctions nommées déclarées avec `export function`, par exemple `shared.script_43.twice(21)`.

Sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc), un projet JavaScript et un projet TypeScript du dossier des scripts généraux ont appelé la même fonction TypeScript globale. Les deux projets ont obtenu `42` en mode test et dans le moteur d’exécution. TypeScript a signalé un argument de type incorrect à la ligne 2. La sélection a été conservée après rechargement.

[HA Logic Studio Pro 0.1.78 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.78)

**0.1.77**

**Vérifier les types** contrôle le code TypeScript et les types de l’API de script. L’éditeur signale les lignes en erreur. Un clic sur le numéro dans le journal revient à la ligne du code source. Le test et le moteur vérifient les types avant d’exécuter le script.

Sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc), deux erreurs de type provoquées volontairement ont été signalées aux lignes 2 et 3. Après correction, le test a réussi. Au lancement du script erroné, le moteur a signalé la ligne 2.

[HA Logic Studio Pro 0.1.77 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.77)

**0.1.76**

Dans les éditeurs JavaScript et TypeScript, la saisie de `ha.` suggère les méthodes de l’API de script. La liste affiche les paramètres et les types de retour. L’éditeur met en évidence le paramètre en cours de saisie.

Le test dans Chrome sur le [système de test PC (64)](/fr/collection/test-systems#testsystem-pc) a vérifié la sélection au clavier dans les deux éditeurs et les signatures de `ha.readState`, `ha.callAction` et `ha.pause`.

[HA Logic Studio Pro 0.1.76 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.76)

**0.1.75**

Lorsque l’erreur peut être localisée, le journal affiche la ligne d’origine du code JavaScript ou TypeScript, en mode test comme en exécution. Un clic sur le numéro de ligne ouvre la ligne concernée dans l’éditeur.

Sur le **système de test PC (64)**, les deux modes ont signalé les erreurs provoquées à la **ligne 3 en JavaScript** et à la **ligne 5 en TypeScript**. Le numéro de ligne TypeScript était correct même après la suppression d’une déclaration de type lors de la transpilation.

[HA Logic Studio Pro 0.1.75 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.75)

**0.1.74**

Logic Studio Pro conserve les 100 dernières entrées du journal d’exécution par utilisateur et par projet. Sur le système de test PC (64), une entrée restait consultable avec le même horodatage après le redémarrage de l’application. Le script était arrêté et l’entrée ne figurait pas dans le journal d’un autre projet.

[HA Logic Studio Pro 0.1.74 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.74)

**0.1.73**

Lors du test sur le système de test PC (64) avec la version 0.1.72, le deuxième déclenchement a commencé avant la fin du premier. Les deux se sont terminés. Une erreur volontaire a arrêté le script concerné. L’autre script a ensuite traité un troisième déclenchement avec succès.

Après la mise à jour locale vers la version 0.1.73 sur le système de test PC (64), la page de l’application dans Home Assistant n’affichait plus « Expérimental » et l’en-tête de Studio n’affichait plus « Test interne ». Les trois projets de test ont été supprimés.

[HA Logic Studio Pro 0.1.73 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.73)

**0.1.72**

Blocks JS importe les messages ioBroker entre scripts avec réponse et adresse cible calculée. L’aperçu indique, pour chaque bloc concerné, l’adresse de réception et le traitement de la réponse à vérifier.

Sur le système de test PC (64), un script Blocks JS en cours d’exécution a construit l’adresse cible à partir de deux fragments de texte. Le second script a journalisé la réception et le bloc de réponse de l’expéditeur s’est exécuté. Les deux projets de test ont ensuite été supprimés et l’autorisation temporaire de `logic_studio_script_message` a été retirée.

[HA Logic Studio Pro 0.1.72 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.72)

**0.1.71**

Le bouton Mode expert dans le menu des projets enregistre le choix pour chaque utilisateur de Home Assistant. Il affiche les outils avancés, dont le code source et l’API de script en JavaScript, l’import et le code généré dans Blocks JS, ainsi que les réglages de diagnostic et d’exécution dans le diagramme fonctionnel. Enregistrer, Annuler, Tester et Lancer restent directement accessibles dans les éditeurs qui les proposent.

Après une sauvegarde complète sur le système de test PC (64), les trois éditeurs ont été vérifiés. Le choix a été conservé après rechargement. Le réglage initial a ensuite été rétabli et vérifié après un nouveau rechargement.

[HA Logic Studio Pro 0.1.71 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.71)

**0.1.70**

L’icône en forme de crayon dans l’arborescence permet de renommer un dossier personnalisé. Après une sauvegarde complète sur le système de test PC (64), la comparaison des exports avant le renommage et après le rechargement a confirmé que l’identifiant du dossier, l’affectation des deux projets et leur ordre étaient conservés. Le nom d’origine a ensuite été rétabli et vérifié après un nouveau rechargement.

[HA Logic Studio Pro 0.1.70 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.70)

**0.1.69**

L’assistant de règles prend en compte le changement de langue dans l’éditeur ouvert. Après une sauvegarde complète sur le système de test PC (64), le test dans Chrome au format tablette (820 × 1180 px) a confirmé que le titre, les étapes et les déclencheurs suivaient le changement **DE → EN → FR → DE**. L’interface de Studio et le gestionnaire d’applications de Home Assistant affichaient tous deux **0.1.69**. Le serveur lit désormais la version affichée dans les métadonnées du paquet.

[HA Logic Studio Pro 0.1.69 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.69)

**0.1.68**

L’export YAML télécharge le fichier directement depuis l’éditeur. Deux exports sur le système de test PC (64) ont produit deux fichiers YAML complets, identiques octet pour octet. Chrome a bloqué le deuxième téléchargement en le signalant comme non sécurisé. Après confirmation manuelle avec **Conserver**, le deuxième fichier était lui aussi complet dans le dossier des téléchargements.

[HA Logic Studio Pro 0.1.68 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.68)

**0.1.67**

Version de test publique actuelle. Créer une sauvegarde complète et essayer la mise à jour sur un système de test.

Les blocs importés de vérification de l’existence d’un état et d’identifiant d’objet conservent leur identifiant ioBroker. Associez explicitement chaque identifiant à une entité Home Assistant dans le bloc. Blocks JS retrouve les données Blockly intégrées dans un fichier JavaScript même si d’autres commentaires les suivent.

La section **Adaptations du code requises** de l’aperçu explique comment remplacer les blocs non pris en charge, comme `exec`. Après une sauvegarde complète sur le système de test PC (64), des fichiers de test XML et JavaScript ont été importés et les nouveaux champs d’association ont été vérifiés dans l’éditeur.

**Reconnexion après un redémarrage de Core**

Une sauvegarde complète a été créée sur le système de test PC (64) avant l’essai. Après le redémarrage de Home Assistant Core, le moteur d’exécution s’est reconnecté 31 secondes après la coupure. La même exécution du script JavaScript a ensuite reçu le passage de l’entité de test de `off` à `on` et l’événement HA personnalisé `logic_studio_runtime_test` avec ses données de test.

**Dossier et ordre des scripts après rechargement**

Après une sauvegarde complète sur le système de test PC (64), deux scripts de test ont été déplacés par glisser-déposer dans un autre dossier. Après l’enregistrement de l’ordre et le rechargement de Logic Studio Pro, les deux scripts étaient toujours dans le dossier de destination, dans l’ordre enregistré.

[HA Logic Studio Pro 0.1.67 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.67)

**0.1.66**

Activez la sauvegarde des compteurs et des mémoires dans le diagramme fonctionnel, puis enregistrez le projet. Les blocs CTU, CTD, CTUD, RS et SR peuvent retrouver leurs valeurs après le redémarrage de l’application.

Le rapport d’import de Blocks JS répertorie séparément les identifiants ioBroker calculés. Dans le champ d’association JSON du bloc importé, associez chaque identifiant ioBroker possible à une entité Home Assistant.

Sur le système de test PC (64), le compteur CTU et la mémoire RS ont conservé les valeurs `1` et `true` après le redémarrage de l’application.

Lors du test en conditions réelles sur le système de test PC (64), le script Blocks JS importé a calculé l’identifiant ioBroker `zigbee.0.sensor`. L’association JSON lui a permis de lire l’assistant de test Home Assistant `input_boolean.logic_studio_runtime_test`. Deux lancements avec le bouton de lecture ont inscrit `false` dans le journal lorsque l’assistant était désactivé et `true` lorsqu’il était activé.

[HA Logic Studio Pro 0.1.66 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.66)

**0.1.65**

**Démarrage automatique, simulation et import ioBroker**

Les projets JavaScript, TypeScript et les diagrammes fonctionnels peuvent être exécutés au démarrage de l’application. Activer **Exécuter au démarrage de l’application** et enregistrer le projet. La simulation propose des points d’arrêt et le pas à pas. L’organisation automatique conserve la position des blocs épinglés. L’aperçu d’import ioBroker de Blocks JS liste les blocs non pris en charge et les identifiants fixes à associer.

Sur le système de test PC (64), le projet de test JavaScript enregistré a démarré automatiquement après le redémarrage de l’application. Un point d’arrêt, un pas de simulation et l’aperçu d’import ioBroker avec un identifiant fixe ont également été vérifiés.

[HA Logic Studio Pro 0.1.65 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.65)

**Règles enrichies et test en conditions réelles sur le système de test PC (64)**

Les déclencheurs d’état prennent en charge les valeurs de départ et d’arrivée, un attribut et une durée minimale. Les conditions vérifient les états, les attributs et les seuils numériques. Les branches ALORS et SINON proposent un sélecteur d’actions HA avec des paramètres JSON et des étapes de temporisation distinctes.

L’éditeur et le sélecteur d’actions ont été testés localement dans le navigateur. Après une sauvegarde complète, le YAML généré a été exécuté directement dans Home Assistant sur le système de test PC (64). Une impulsion brève n’a rien déclenché. Un état maintenu trois secondes a exécuté ALORS. Un changement du nom d’affichage a exécuté SINON. Les deux traces ont confirmé le délai de deux secondes et la valeur de texte attendue. L’automatisation et les deux auxiliaires de test ont été supprimés.

Les nouveaux blocs s’exportent en YAML HA. Rules → JS indique si un bloc empêche la conversion.

[HA Logic Studio Pro 0.1.62 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.62)

**Export YAML et test en conditions réelles sur le système de test PC (64)**

L’export des règles conserve les états tels que `on` et `off` sous forme de texte, sans les convertir en booléens YAML. L’automatisation corrigée a été exécutée directement dans Home Assistant sur le système de test PC (64) avec des entrées de test.

| Déclencheur | Condition | Résultat de la trace HA |
| --- | --- | --- |
| Changement d’état | OU satisfaite | Deux actions ALORS |
| Changement d’état | ET non satisfaite | Deux actions SINON |
| Événement HA | Condition NON vraie | Deux actions ALORS |
| Heure 20:26 | Condition NON fausse | Deux actions SINON |

Une sauvegarde complète a été créée avant le test. L’automatisation et les trois entrées de test ont ensuite été supprimées.

[HA Logic Studio Pro 0.1.61 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.61)

:::

### HA Logic Studio Pro 0.1.41–0.1.60

::: details Historique des versions

**Règles : palette compacte et déclencheurs multiples**

L’éditeur affiche une liste compacte avec des icônes à gauche. Une règle peut combiner des changements d’état, une heure quotidienne et des événements Home Assistant. Les conditions acceptent ET, OU et NON. Les branches ALORS et SINON exécutent plusieurs actions dans l’ordre affiché.

Sur le système de test PC (64), une règle existante a été testée avec trois déclencheurs, deux conditions et deux actions par branche. L’aperçu YAML présentait la structure attendue. Lors du test dans Studio, les trois déclencheurs simulés ont lancé les deux actions ALORS lorsque la condition OU était satisfaite. Lorsque la condition ET ne l’était pas, les deux actions SINON se sont exécutées dans l’ordre configuré. Aucun appareil réel n’a été commandé.

[HA Logic Studio Pro 0.1.60 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.60)

![Éditeur de règles sur le système de test PC (64) avec la palette compacte et les deux branches](/images/logic-studio/0.1.60-rules-test-193.png)

**Créer une règle avec l’assistant**

Choisissez **Règles → Assistant**. Le dialogue suit quatre étapes : **Déclencheur → Conditions → Actions → Récapitulatif**. Une règle peut réagir à un changement d’état, à une heure quotidienne dans le fuseau horaire de HA ou à un événement Home Assistant. Les conditions et la branche SINON sont facultatives. Le récapitulatif affiche l’aperçu YAML. **Appliquer** transfère le brouillon dans l’éditeur ; **Enregistrer** le conserve. Les règles existantes restent modifiables et peuvent être ouvertes en JavaScript ou en YAML HA.

[HA Logic Studio Pro 0.1.59 · GitHub / ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.59)

Le 12 novembre 2026, les trois déclencheurs ont été testés directement dans Home Assistant sur le système de test PC (64). Le passage de l’état désactivé à l’état activé, le déclenchement quotidien à 19 h 38 (heure locale de HA) et l’événement `rules_live_0159_event` ont chacun activé la sortie de test. Une sauvegarde complète a été créée avant le test. Les trois automatisations et les deux assistants de test ont ensuite été supprimés.

![Home Assistant affiche la dernière exécution des trois automatisations de test et la sortie de test activée](/images/logic-studio/0.1.59-rules-live-test-193.png)

**Nouveautés depuis la version 0.1.12**

- **Arborescence et éditeurs.** Les projets et dossiers sont enregistrés sur le serveur pour chaque utilisateur HA. Les projets locaux peuvent être migrés au premier démarrage depuis le navigateur d’origine. JavaScript et TypeScript disposent de la coloration syntaxique, de numéros de ligne et de barres d’outils dédiées. Les icônes et couleurs correspondent entre le sélecteur, l’arborescence et les filtres. Blocks A et Blocks JS ont des filtres distincts. La largeur automatique du volet reste réglable par la poignée.
- **Blocks A et Blocks JS.** Blocks A utilise le catalogue intégré de Blocks for HA. Blocks JS dispose de sa propre palette JavaScript. Blocks A exporte des automatisations HA en YAML. Blocks JS génère le JavaScript pour la simulation et le moteur. Les blocs ioBroker inconnus sont conservés sous forme de blocs de remplacement et bloquent la génération du code jusqu’à leur remplacement. Associer les identifiants d’objets ioBroker aux entités HA correspondantes.
- **Diagramme fonctionnel.** La barre supérieure comporte les icônes de simulation, d’avancement d’une seconde et de réinitialisation. Le format de sortie et l’aperçu sont à droite. Les connexions peuvent être déplacées vers une autre entrée et les valeurs des signaux s’affichent à l’entrée cible.
- **Moteur serveur.** Le bouton de lecture lance JavaScript, TypeScript transpilé ou Blocks JS sur le serveur HA. L’arrêt et le redémarrage sont disponibles dans l’éditeur. L’état et le journal restent accessibles depuis un autre navigateur. Le **test** séparé utilise des états et événements simulés. Les scripts et automatisations YAML sont exécutés par Home Assistant après import.

**Configurer le moteur en direct**

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

**Vérifié sur le système de test PC (64) avec HA 2026.11.1.** Le moteur a lu l’état et un attribut de l’entrée de test, l’a activée par un horaire et l’a désactivée à la réception d’un événement HA réel. Les deux changements d’état ont été signalés. Un horaire Blocks JS importé s’est exécuté toutes les deux secondes. Les tests précédents ont vérifié le démarrage, l’arrêt, le redémarrage et la poursuite de l’exécution après avoir quitté Studio, avec JavaScript et TypeScript.

**Commander des scripts et des automatisations**

Dans **Blocks JS → Système**, choisissez une entité Home Assistant avec **Choisir un script ou une automatisation**, puis reliez le bloc à **Commander**. Vous pouvez démarrer ou arrêter les scripts, ainsi qu’activer, désactiver ou déclencher une fois les automatisations. L’option **Vérifier les conditions** est activée par défaut lors du déclenchement. Décochez-la pour ignorer les conditions. Pour l’exécution réelle, autorisez l’entité cible dans `runtime_write_entities`.

[HA Logic Studio Pro 0.1.58 · GitHub et ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.58)

**Fonctions et import ioBroker**

**Blocks JS → Fonctions** propose deux blocs de fonction JavaScript, avec ou sans valeur de retour. Utilisez l’engrenage pour définir les paramètres et **…** pour modifier le code. Après l’ajout d’une définition, son bloc d’appel apparaît dans la palette.

L’import ioBroker conserve les définitions, les appels, les paramètres et le code JavaScript. Adaptez les appels propres à ioBroker au moteur HA et associez explicitement les identifiants d’objet importés aux entités HA.

**Interroger l’historique**

Utilisez **Blocks JS → Sendto → Interroger l’historique** pour lire les états enregistrés par HA Recorder. Sans période indiquée, la requête utilise la journée en cours dans le fuseau horaire de HA. Le bloc de résultat renvoie des valeurs horodatées. L’import ioBroker conserve la période, l’agrégation, le pas et le nombre de résultats.

[HA Logic Studio Pro 0.1.57 · GitHub et ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.57)

:::

### HA Logic Studio Pro 0.1.21–0.1.40

::: details Historique des versions

**0.1.29 · Enregistrement manuel et éditeurs de blocs**

Dans tous les éditeurs, **Enregistrer** applique les modifications. **Annuler** restaure la dernière version enregistrée ou abandonne un nouveau projet. Les modifications non enregistrées désactivent **Démarrer** et **Redémarrer**. Il reste possible d’arrêter un script en cours. Blocks A ouvre le sélecteur d’entités directement depuis le champ du bloc. Blocks JS propose une palette inspirée d’ioBroker avec des entités, des actions et des déclencheurs HA, sans Jinja.

[Version de test et ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.29)

**0.1.28 · Traductions des éditeurs**

La version **0.1.28** complète les traductions des éditeurs de règles, Blocks A, Blocks JS, JavaScript, TypeScript et YAML HA. Le choix de langue s’applique aussi au diagramme fonctionnel. [Version de test et ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.28)

Les tests sur le système de test PC (64) ont vérifié dans les trois langues les barres d’outils du diagramme fonctionnel, des règles, de Blocks A, de Blocks JS, de JavaScript, de TypeScript, des automatisations HA et des scripts HA. La boîte de dialogue des exemples de code a aussi été vérifiée en français.

Pour installer la version Pro, sélectionner **HA Logic Studio Pro** dans le dépôt commun UGSo de la boutique d’applications. Pour une installation GitHub existante, rechercher les mises à jour puis sélectionner **HA Logic Studio Pro → Mettre à jour**. Utiliser **DE**, **EN** ou **FR** en haut du volet des projets pour changer la langue des éditeurs.

**0.1.26 · FBD Runtime**

Le bouton **Lecture** lance le diagramme fonctionnel sur le serveur HA. Le mode **Automatique** réagit aux changements des états et attributs autorisés ; le **Cycle fixe** évalue le plan toutes les 100 à 60 000 ms. La simulation et l’export YAML restent séparés. **Enregistrer** valide le brouillon ; **Annuler** rétablit le dernier état enregistré. La barre d’outils est disponible en DE/EN/FR.

Sur le système de test PC (64), le démarrage automatique a activé l’entité de test et le cycle de 200 ms l’a désactivée. L’arrêt et l’annulation d’une modification non enregistrée ont aussi été vérifiés. Les deux modes ont également été testés localement avec des changements d’entrée.

[Mise à jour de test GitHub et ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/ha-logic-studio-pro-v0.1.26) · [Application dans le dépôt commun](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_logic_studio_pro)

:::

### HA Logic Studio Pro 0.1.1–0.1.20

::: details Historique des versions

Les premières versions publiques de test ont introduit l’application autonome avec les plans fonctionnels, l’import Home Assistant et React Flow.

[HA Logic Studio Pro · GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases?q=ha-logic-studio-pro+0.1.&expanded=true)

:::

## Installation de test depuis GitHub

[![Ajouter le dépôt à Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Frockbaer2007%2Fugso-ha-mqtt-addons)

1. Dans **Paramètres → Applications → Boutique d’applications → Dépôts**, ajouter l’adresse ci-dessous. Si « UGSo HA Apps » est déjà configuré, rechercher les mises à jour.
2. Sélectionner et installer **UGSo Logic Studio**. Activer le mode avancé du profil HA si les applications expérimentales sont masquées.
3. Démarrer puis ouvrir l’interface. Compatible **HA OS/Supervised**, **amd64 et aarch64**. La première construction du conteneur peut prendre plusieurs minutes. Ce n’est pas un paquet frontend HACS/Marketplace.

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

**Conserver une installation locale existante :** les applications GitHub et locale ont des identifiants de dépôt et des données séparés. Exporter l’ancien plan en JSON avec **Projekt**, puis utiliser **Öffnen** dans l’application GitHub. Aucune migration ou désinstallation automatique. Chaque application conserve projet et réglages de palette sous `/data`.

**Mettre à jour une application GitHub existante :** sauvegarder d’abord, rechercher les mises à jour dans le gestionnaire d’applications puis choisir **UGSo Logic Studio → Mettre à jour**. Conserver l’installation : `/data`, les identifiants d’entités et les plans existants sont préservés. Ne pas désinstaller ni changer d’identifiant d’application. Sur le système de test PC (64), le plan original, les favoris, les blocs récents et les catégories repliées ont été conservés après la mise à jour.

## Langue, barre d’outils et documentation

Choisir **Langue → Deutsch / English / Français** dans l’en-tête. Menus, descriptions des blocs, sélecteur d’entités et dialogues d’import/export changent sans rechargement. Le choix est enregistré avec les préférences du navigateur/de l’application. **Noms personnels, identifiants d’entités, valeurs, noms des bornes et code YAML/JavaScript généré ne sont pas traduits.**

**Documentation**, à droite, présente les raccourcis implémentés et, pour le bloc sélectionné, sa description et ses entrées/sorties. **Ctrl+Z / Ctrl+Y** : annuler/rétablir ; **Suppr** : supprimer la sélection ; **Échap** : annuler une connexion/fermer un menu. Tab et Entrée/Espace permettent de choisir et connecter les bornes. Les commandes du débogueur de l’éditeur de référence ioBroker ne sont pas présentées comme disponibles.

La barre regroupe **Annuler/rétablir → Projet → Simulation → Sortie**. Les trois boutons de simulation ont les mêmes dimensions et des bordures distinctes. Le menu Projet propose aussi **Nouveau projet** et **Charger l’exemple**. Le sélecteur d’entités s’ouvre via l’icône **à côté de l’identifiant d’entité HA** dans les propriétés STATE_IN/STATE_OUT ; l’ancien bouton supérieur est retiré.

![Documentation allemande sur le système de test PC (64) avec le plan original conservé](/images/logic-studio/0.1.12-193-de-documentation.png)

![Documentation anglaise du même plan sur le système de test PC (64)](/images/logic-studio/0.1.12-193-en-documentation.png)

![Documentation française du même plan sur le système de test PC (64)](/images/logic-studio/0.1.12-193-fr-documentation.png)

## Deux types de plans

| Plan | Usage et sortie |
| --- | --- |
| Flux de valeurs | Entrées/sorties typées, logique, calcul, sélection, mémoires, fronts, temporisateurs et compteurs. 33 types implémentés ; les autres références sont marquées comme modèles. Export YAML d’automatisation HA, YAML de script HA ou fonction JavaScript avec interface hôte. |
| Flux HA natif | Importer automatisations, scripts et blueprints en blocs imbriqués. 53 types HA supplémentaires : déclencheurs, conditions, branches, boucles, attentes, variables et entrées de blueprint. Export uniquement en YAML HA natif. |

La simulation des flux de valeurs utilise des valeurs de démonstration/instantanées. Les blocs persistants nécessitent les helpers texte HA documentés ou un hôte mémoire JavaScript. Les flux HA natifs ne sont ni exécutés dans l’éditeur ni traduits automatiquement en JavaScript. La sortie JavaScript n’est pas un script ioBroker.

## Connexions à la souris et mini-vue

Maintenir le bouton de la souris sur une borne colorée, faire glisser vers une borne opposée compatible puis relâcher. Le curseur devient une croix et un aperçu du lien suit la souris. Les cibles compatibles sont marquées en vert ; les entrées incompatibles ou occupées en rouge. Le glissement d’une entrée vers une sortie fonctionne aussi. **Échap** ou relâcher sur une zone vide annule ; **Annuler** retire un lien nouvellement créé.

**BOOL se connecte uniquement à BOOL.** Les types identiques sont compatibles ; la conversion élargissante `INT → REAL` est aussi autorisée. Les bornes explicitement `ANY` sont universelles. Nombres et textes ne sont pas convertis implicitement en BOOL. Une entrée accepte un seul lien ; types incompatibles, bornes de même direction, liens vers le même bloc et cycles sont refusés avec une explication. Au clavier, sélectionner la sortie avec Tab/Entrée, puis l’entrée et Entrée.

![Bornes BOOL compatibles reliées à la souris sur le système de test PC (64)](/images/logic-studio/0.1.7-bool-verbunden.png)

![Connexion STRING vers BOOL refusée avec une erreur de type explicite](/images/logic-studio/0.1.7-typ-abgewiesen.png)

En bas à droite, la **MiniMap** affiche les positions colorées des blocs et la zone visible. Faire glisser dans la MiniMap pour naviguer et utiliser la molette pour zoomer. Faire glisser le canevas vide déplace la vue ; **+/−** règlent le zoom et **Alles anzeigen** cadre tous les blocs. Déplacer un bloc par son en-tête. L’attribution **React Flow** reste visible en bas à droite. Depuis 0.1.8, la bibliothèque fonctionne réellement dans l’éditeur ; la logique métier, la validation des types et les exportateurs restent propres à Logic Studio.

![Canevas React Flow avec plan original conservé et MiniMap sur le système de test PC (64)](/images/logic-studio/0.1.8-react-flow-193.jpg)

![Test local React Flow avec blocs typés](/images/logic-studio/0.1.8-react-flow-local.jpg)

Les images suivantes documentent aussi les tests précédents de 0.1.7.

![Mini-vue avec positions des blocs et cadre visible sur le système de test PC (64)](/images/logic-studio/0.1.7-miniuebersicht.png)

## Importation et modification

Ouvrir **HA importieren**, choisir automatisations/scripts/blueprints, puis **Aus HA einlesen**, un fichier YAML/JSON ou du texte. Sélectionner une entrée, vérifier l’aperçu et choisir **Import übernehmen**. Sauvegarder d’abord le projet existant en JSON ; des sauvegardes du projet et des sources sont aussi créées.

Le dossier de configuration HA est monté **en lecture seule**. L’application lit `automations.yaml`, `scripts.yaml` et les fichiers blueprint. Avant analyse, les sources sont copiées sous `/data/ha-source-backups/<horodatage>/` avec leurs noms d’origine. `secrets.yaml` n’est pas ouvert ; `!secret` et `!include` ne sont pas résolus. Importer manuellement les fichiers référencés par les inclusions.

Les liens orange **FLOW** représentent l’ordre et les branches : sortie de branche → **DO**, puis **NEXT → DO**. Les liens jaunes **VALUE/REF** montrent les paramètres de blueprint et leur utilisation `!input`. Configuration HA et chemins de branche sont modifiables en JSON. Les clés de paramètres/champs doivent être uniques. Les sections inconnues restent **YAML_ORIGINAL** ; des liens manquants peuvent bloquer l’export.

![Aperçu d’importation des blueprints HA existants](/images/logic-studio/blueprint-import.png)

Le **menu ⋮** de chaque bloc propose **Eigenschaften** (propriétés), **Duplizieren** (dupliquer) et **Löschen** (supprimer). La duplication copie les propriétés sans liens. La suppression retire les liens associés ; Annuler les restaure. Recherche, favoris et blocs récents facilitent la sélection.

![Menu à trois points d’un bloc](/images/logic-studio/block-menu.png)

## Validation et limites

**0.1.12 sur le système de test PC (64) / HA Core 2026.10.4 :** Application locale mise à jour depuis 0.1.8 après sauvegarde complète. DE/EN/FR, documentation et sélection d’entités HA réelles validés. Le français reste mémorisé après rechargement du navigateur, redémarrage de l’application et nouveau chargement du projet enregistré ; l’allemand a ensuite été rétabli. Le JSON ne diffère **que par la version** : cinq blocs, trois liens, noms, valeurs et positions sont identiques. Le YAML généré est identique en EN et FR. Aucun appareil commandé. **31 tests Node et neuf tests Python** réussis. Les anciens rapports ci-dessous sont conservés comme historique.

![Retour à l’allemand après redémarrage réussi sur le système de test PC (64)](/images/logic-studio/0.1.12-193-neustart-de.png)

**0.1.8 sur le système de test PC (64) / HA Core 2026.10.4 :** Application locale existante mise à jour après sauvegarde complète. Connexions BOOL à la souris, refus STRING→BOOL, entrées occupées, déplacement/annulation, duplication, zoom et MiniMap validés. Le sélecteur lit les entités HA ; un script imbriqué avec If/Then/Else, Delay et Stop a été importé puis exporté sans modification de structure. Le plan original a été restauré et comparé après rechargement : **identifiants, positions, paramètres et trois liens inchangés**, ainsi que favoris, blocs récents et catégories repliées. Aucun appareil commandé. Construction Docker et test HTTP du conteneur réussis, ainsi que **29 tests Node et huit tests Python**. Images de l’interface allemande. Le changement clair/sombre n’a pas été retesté manuellement à cette étape.

La base fonctionnelle **0.1.5** a été testée sur **système de test PC (64) / HA Core 2026.10.4** : import d’un blueprint réel, exemples d’automatisation/script/blueprint, exports YAML identiques sur le fond et actions du menu. **0.1.6** est sa première distribution publique. 22 tests Node et huit tests Python vérifient export, persistance, branches et import sûr ; les contrôles GitHub construisent aussi le conteneur.

**0.1.7 sur le système de test PC (64) / HA Core 2026.10.4 :** tests réels à la souris réussis pour BOOL → BOOL et le sens inverse. STRING → BOOL et une entrée occupée ont été refusés. Mini-vue, navigation par clic et touche Début vérifiées. Le plan original a été rétabli et comparé à sa sauvegarde : **cinq blocs, trois liens et tous les réglages de palette conservés**, y compris après la mise à jour locale vers 0.1.7. Sauvegardes HA complète et projet/réglages séparées créées au préalable ; aucun appareil commandé. **26 tests Node et huit tests Python** réussissent actuellement. Les captures montrent l’interface allemande.

L’éditeur ne valide pas toute la sémantique HA : vérifier cibles, templates et sélecteurs dans HA. Commentaires, ancres YAML et mise en forme ne sont pas reconstruits. Limites : **1 Mo, 200 blocs, 500 liens**, imbrication limitée et jusqu’à 250 fichiers blueprint dans les dossiers habituels. Régulateurs, calendrier et sous-plans personnalisés restent partiellement des modèles.

Pour un test local, extraire tout le ZIP, installer Python 3.10+ et les dépendances `requirements.txt`, puis lancer **Start-Demo.cmd** sous Windows. `http://127.0.0.1:4180/` affiche des entités de démonstration sans connexion HA. Le ZIP contient aussi `addon/logic_studio/` pour une installation locale.

[Signaler les problèmes sur GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/issues) avec versions, architecture et petit exemple anonymisé. Ne pas publier identifiants, automatisations personnelles ou sauvegardes complètes. Guides et rapport de test sont inclus. Licence MIT ; attribution des métadonnées de blocs dans `THIRD-PARTY.txt`.
