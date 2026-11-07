---
title: Client MQTT
description: Transmettre en temps réel des valeurs sélectionnées de Home Assistant via MQTT et les piloter de manière ciblée.
---

# Client MQTT 0.1.30 {#mqtt-client-0-1-16}

Transmettre les états et attributs HA sélectionnés vers un broker MQTT externe. La version 0.1.30 donne la priorité aux retours de commande et ajoute un contrôle des états HA. Installez la mise à jour de l’application HA ; le script 0.1.27 peut rester.

[Release 0.1.30](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.30)

## Important : activer explicitement les mesures supplémentaires {#enable-device-readings}

::: warning Important : activer explicitement les mesures supplémentaires
**Une étiquette seule n’active pas les mesures supplémentaires.** Dans **Transmission et TLS**, cochez **« Inclure automatiquement les mesures et valeurs de batterie du même appareil »** (interface allemande : **„Zugehörige Mess- und Batteriewerte desselben Geräts automatisch einbeziehen“**), puis cliquez sur **« Enregistrer et connecter »**. Sans cette case, l’énergie, la tension, le courant et la puissance ne sont pas automatiquement ajoutés à l’interrupteur étiqueté. Les valeurs sélectionnées manuellement restent indépendantes de cette option.
:::

Seuls les capteurs compatibles, activés dans HA et associés au même appareil HA sont inclus, s’ils existent. Aucune mesure absente de l’appareil n’est créée. **« Vérifier les mesures associées »** indique la détection et les motifs d’exclusion. Les états de commande sont prioritaires ; les mesures peuvent suivre avec un délai.

## Pour VIS 2 en particulier : le script JavaScript ioBroker {#javascript-vis2-helper}

::: tip Pour VIS 2 en particulier : le script JavaScript ioBroker
Le **JavaScript fourni s’exécute dans l’adaptateur JavaScript ioBroker, pas dans Home Assistant**. Il crée des points virtuels sous `0_userdata.0.ugso_mqtt` : **un point par valeur pour l’affichage et la commande**, même si MQTT utilise des topics `state` et `set` séparés. Les interrupteurs et valeurs de lampe compatibles disposent du canal de commande approprié ; les mesures restent en lecture seule. Les métadonnées HA adaptées déterminent les types, unités et rôles non ambigus. Une commande n’est confirmée qu’après un véritable retour HA.

**Vérifiez d’abord l’aperçu, puis choisissez `mode: 'apply'`.** L’aperçu crée uniquement les dossiers de base/points de sauvegarde manquants du script ; les points VIS-2 virtuels sont créés en mode application. **setObject** doit être autorisé dans les réglages de l’adaptateur pour leur création. Les valeurs existantes et rôles définis manuellement restent protégés. L’application HA est en **0.1.30**, le script actuel reste en **0.1.27** : cette différence est volontaire. Le transfert MQTT seul fonctionne aussi sans le script.
:::

## Nouveauté 0.1.30 : identifiants repliables

La section **Identifiants** dispose désormais d’un bouton pour la déplier ou la replier, également utilisable au clavier. Si le broker est configuré, l’adresse IP, le port, le nom d’utilisateur et le mot de passe restent repliés après chargement et enregistrement. Si des champs obligatoires manquent, la section s’ouvre pour les corriger. **Transmission et TLS**, **Enregistrer et connecter** et **Valeurs actuellement transmises** restent visibles. Les réglages et identifiants ne sont pas modifiés. La priorité de la version 0.1.29 et le script 0.1.27 sont conservés. L’utilisateur a confirmé le bon fonctionnement du retour de commande avec un délai d’environ une demi-seconde. La lampe Zigbee a également été testée avec succès : le retour d’état fonctionne et la luminosité suit HA à 100 %.

## Nouveauté 0.1.29 : états de commande avant mesures

**Mettez l’application HA MQTT-Client à jour vers 0.1.29 ; le script ioBroker 0.1.27 reste inchangé.** Les états de commande/contact et les retours des commandes sont prioritaires sur les mesures et ne subissent pas la pause de publication configurée. Une transmission déjà engagée se termine normalement ; entre les messages, les lots de mesures/attributs cèdent la priorité aux états urgents ou commandes. À partir de 32 événements en attente, des lots limités de capteurs regroupent les valeurs intermédiaires pour conserver le dernier état de chaque source. Les changements de commande ordinaires restent conservés. Un contrôle périodique lit les états HA réels même avec la connexion en direct active, selon le `poll_interval` existant (5 secondes par défaut). Les valeurs inchangées ne sont pas republiées. **Übertragung und TLS** et la pause de publication des mesures/attributs sont directement visibles ; les identifiants de connexion restent repliables séparément. La ligne d’état distingue la file (**Wartend**), les événements regroupés (**Zusammengefasst**), la dernière réception HA (**HA-Eingang**) et le compteur cumulatif (**Gesendet**). Les réglages et valeurs existants sont conservés. Pour vérifier, laissez le contrôle à 5 secondes et actionnez un relais non critique dans HA. Seul un retour HA réel entraîne `ack: true` ; la transmission au broker ne suffit pas. Vérifié localement ; la latence réelle chez l’utilisateur reste à confirmer.

Les interrupteurs sont reconnus par le domaine `switch.*`, sans classe d’appareil ni unité obligatoire. Les lampes utilisent `light.*`. La sélection automatique des mesures, lorsqu’elle est activée, reste limitée au même appareil HA. Les capteurs utilisent d’abord `device_class` ; si elle manque, les unités non ambiguës de `unit_of_measurement`, telles que W/kW/MW, V/mV/kV, A/mA et Wh/kWh/MWh, sont utilisées. Les classes existantes ne sont jamais remplacées ; des noms similaires ou un pourcentage ambigu ne suffisent pas. **Vérifier les mesures associées** (interface allemande : **Zugehörige Messwerte prüfen**) affiche un rapport en lecture seule des capteurs détectés et des motifs d’exclusion : association d’appareil absente, entité désactivée ou classe/unité inadaptée. Les mesures peuvent attendre derrière les états de commande. Les réglages, identifiants et valeurs existantes sont conservés.

## Nouveauté 0.1.28 : retours HA sans surcharge d’événements étrangers

Cette correction concerne **l’application MQTT-Client dans Home Assistant** : mettez-la à jour vers 0.1.28 et redémarrez l’application. Le script ioBroker 0.1.27 peut rester inchangé ; son seul remplacement ne corrige pas la réception des événements HA. Avec la sélection par étiquette, seuls les événements des entités sélectionnées et de leurs mesures du même appareil activées sont mis en file. Les événements du reste de HA ne peuvent plus remplir cette file. Après modification des étiquettes ou des affectations d’appareils, le client récupère des états HA récents. Les états en attente avec un ancien `last_updated` sont ignorés après resynchronisation ; les changements normalement ordonnés restent conservés. Le compteur de surcharge est cumulatif depuis le démarrage et signale toujours les débordements réels des événements sélectionnés. Le délai de publication configuré, les identifiants de connexion et les sélections sont conservés ; une première synchronisation importante peut encore durer. Après celle-ci, actionnez un relais non critique dans HA et vérifiez que MQTT et le point virtuel ioBroker suivent rapidement. La confirmation sur le système réel de l’utilisateur reste à faire.

## Nouveauté 0.1.27 : commandes sans retain

Les commandes utilisent désormais l’API `sendMessage2Client` de l’adaptateur MQTT ioBroker avec **`retain: false`**. En mode serveur, une écriture normale dans un point MQTT `set` peut parvenir au client avec le drapeau RETAIN. Le client HA continue de refuser ces commandes afin de ne pas exécuter d’anciennes demandes à la reconnexion. Les réglages globaux du broker et les valeurs des points MQTT sont conservés. Le script vérifie le topic de commande par rapport au topic d’état via `native.topic`, sans déduire les chemins des identifiants d’objets. Dans VIS 2, commandez toujours le point virtuel sous `0_userdata.0.ugso_mqtt` avec `ack: false` et `mode: 'apply'`. La ligne `Command handed to MQTT adapter (retain=false)` confirme uniquement la transmission à l’adaptateur ; un nouvel état HA doit confirmer l’exécution. La valeur brute du point MQTT `set` ne change pas nécessairement. Aucun nouvel essai automatique ; les erreurs ou l’absence de retour HA restent non confirmées. Remplacez le fichier complet du script en conservant vos réglages.

## Nouveauté 0.1.26 : création automatique de la base

Les dossiers de base du script (`virtualRoot`, `aliasRoot`) et les deux points de sauvegarde (`virtualBackupId`, `backupId`) absents sont désormais créés automatiquement au démarrage dans **tous les modes**, y compris `preview` et `restore`. Les dossiers, sauvegardes, valeurs et rôles manuels existants ne sont pas écrasés. Les nouveaux journaux contiennent des structures vides valides. Autorisez `setObject` dans l’instance JavaScript même pour l’aperçu. Les autorisations manquantes et les chemins incompatibles sont signalés comme erreurs. L’aperçu ne crée aucun point VIS 2 commandable et ne modifie ni les rôles MQTT ni les valeurs des appareils ; utilisez `mode: 'apply'` après vérification pour ces opérations. Le traitement événementiel de la version 0.1.25 est conservé.

## Points VIS 2 automatiques depuis 0.1.24

Le script ioBroker combiné crée des points virtuels réunissant retour d’état et
canal de commande. Il prend en charge les interrupteurs, valeurs Light et autres
canaux numériques/listes/texte autorisés ; dates et mesures restent en lecture
seule. Les valeurs MQTT d’origine, paramètres et alias existants sont conservés.
Aperçu, sauvegarde automatique, contrôle des types/limites et protection contre les
boucles sont inclus. Les avertissements pour les points optionnels absents sont
corrigés. Préparé pour les API de l’adaptateur JavaScript **10.4.10** ; pas encore
de nouvel essai dans une installation réelle.

[Configuration et correspondances](./iobroker-roles.md#vis2) ·
[Version 0.1.24](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.24)

## Attribution des rôles ioBroker depuis 0.1.23

Un JavaScript optionnel attribue aux dates, horodatages et mesures non ambiguës
des rôles ioBroker adaptés. Il comprend un aperçu, une sauvegarde préalable et une
restauration contrôlée. Les valeurs existantes, identifiants de connexion et rôles
spécifiques manuels sont conservés. Les mesures MQTT accessibles en écriture utilisent
des alias en lecture seule. Les types, unités et classes incompatibles sont ignorés.

[Installation et correspondances complètes HA → ioBroker](./iobroker-roles.md) ·
[Version 0.1.23](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.23)

## Nouveautés de la version 0.1.22

La sélection par étiquette comprend désormais l’état, les métadonnées standard
disponibles et les canaux de commande des entités pilotables prises en charge.
Les interrupteurs reçoivent automatiquement `<base>/set` pour `ON`/`OFF` ;
les nombres, listes de choix et boutons utilisent leurs commandes prises en charge.
Aucune commande n’est envoyée lors de la configuration. Les commandes persistantes,
vides ou invalides sont rejetées.

Les lampes ne reçoivent que les canaux correspondant aux fonctions déclarées par HA :

| Canal sous `<base>` | Valeur et canal de commande |
| --- | --- |
| `brightness/state`, `brightness/set` | Luminosité de 0 à 100 % |
| `rgb_color/state`, `rgb_color/set` | JSON `[255,128,0]`, composantes de 0 à 255 |
| `effect/state`, `effect/set` | Nom figurant dans la liste d’effets déclarée |
| `color_temp_kelvin/state`, `color_temp_kelvin/set` | Kelvin entiers dans les limites déclarées |

`<base>` est le topic existant sans `/state`. Les listes d’effets, modes de couleur
et limites Kelvin sont des attributs en lecture seule. Les attributs HA sélectionnés
manuellement conservent leur chemin et leur unité : `attribute/brightness` reste
compris entre 0 et 255.

Dans **Übertragung und TLS** (Transmission et TLS), activez **Zugehörige Mess- und
Batteriewerte desselben Geräts automatisch einbeziehen** pour inclure les mesures
associées. `label_device_readings` vaut `false` par défaut. Les mesures prises
en charge sont l’énergie, la tension, le courant, la puissance, la température,
l’humidité, la batterie et un éventuel capteur de batterie faible. Seule l’identité
de l’appareil HA est utilisée, jamais la similitude des noms. Aucun seuil n’est
inventé. Ces capteurs supplémentaires n’ont pas de canal de commande.

Les métadonnées automatiques comprennent les noms, classes d’appareil, unités et
classes d’état disponibles, ainsi que les choix et limites nécessaires. Les autres
attributs restent sélectionnables manuellement. `device_class` est transmis comme
métadonnée ; cela ne modifie pas automatiquement un rôle ioBroker tel que `date`.

La fenêtre des transmissions affiche aussi les attributs automatiques, valeurs
Light et canaux de commande actifs avec leur origine. Le retrait d’une étiquette
révoque les valeurs et commandes automatiques au prochain contrôle ; les commandes
en attente sont revérifiées avant exécution. Les sélections manuelles et identifiants
sont conservés. Les anciennes valeurs persistantes ne sont supprimées qu’avec le
nettoyage confirmé des topics.

Vérification locale avec HA et broker simulés ; aucun nouvel essai sur appareil HA.
[Version 0.1.22](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.22)

## Transmissions actuelles

Depuis **0.1.21**, seuls les identifiants de connexion se replient automatiquement.
**Übertragung und TLS** (Transmission et TLS) reste accessible séparément.
Les boutons **Enregistrer et connecter** et **Transmissions actuelles**, de même
taille, restent visibles sur une même ligne.

Le second bouton ouvre une liste avec recherche et défilement de tous les états et
attributs actuellement sélectionnés, y compris les états sélectionnés par une
étiquette HA. Les états en double sont regroupés. L’origine est indiquée par un
badge avec texte : **Étiquette** en bleu, **Manuel** en vert, **Les deux** en violet.
Depuis 0.1.22, les attributs standard automatiques et les valeurs Light sont également affichés.

Chaque entrée affiche le nom, l’identifiant de l’entité, l’attribut éventuel, la
valeur actuelle et le topic MQTT. Le dernier accusé de réception du broker comprend
la date et la valeur envoyée ; les valeurs non confirmées sont signalées et les
erreurs apparaissent séparément en rouge. L’accusé confirme l’acceptation par le
broker, pas le traitement par ioBroker ou un appareil cible. La fenêtre ouverte
s’actualise toutes les trois secondes ainsi qu’avec **Actualiser**.
L’aperçu concerne la connexion en cours et se réinitialise à son redémarrage.
Les paramètres et identifiants de connexion ne sont ni modifiés ni affichés dans
cette liste. Vérifications locales : sélections manuelles et par étiquette,
attributs, erreurs de confirmation et présentation mobile.
[Version 0.1.21](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.21)

**0.1.20 :** Les paramètres de connexion sont repliables sous **Zugangsdaten**
(Identifiants de connexion). La section reste ouverte pour la première
configuration. Avec une adresse de broker enregistrée, elle se replie après le
chargement et l’enregistrement réussi. Cliquez sur le titre pour la rouvrir.
Les messages d’enregistrement et d’erreur restent visibles ; les paramètres et
les identifiants de connexion sont conservés.
[Version 0.1.20](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.20)

La version **0.1.19** sépare également les lignes dans la liste des transmissions :
le nom apparaît au-dessus du résumé de l’état, des attributs sélectionnés et de la
commande de retour. **Modifier** reste à droite. Cette vue a aussi été vérifiée
localement sur des largeurs de 1300 et 390 pixels.
[Version 0.1.19](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.19)

Depuis la version **0.1.18**, chaque ligne de la fenêtre d’un appareil distingue
le **nom** sur la première ligne, l’**identifiant de l’entité** sur la deuxième,
puis le **type cible et le nombre d’attributs** sur la troisième. Les noms et
identifiants longs passent à la ligne ; l’état actuel reste à droite. Cette
présentation est conservée après une modification de la sélection. Elle a été
vérifiée localement sur des largeurs de 1300 et 390 pixels. La mise à jour conserve
les paramètres, les identifiants de connexion et les transmissions sélectionnées.
[Version 0.1.18](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.18)

Le client MQTT transmet des appareils, des états et des attributs sélectionnés depuis Home Assistant vers un broker MQTT externe, comme par exemple l'adaptateur MQTT d'ioBroker. Au lieu de répliquer toutes les entités HA, vous sélectionnez vous-même les valeurs dont vous avez besoin. Le broker HA existant demeure en place. L'application lit les données directement depuis HA ; il ne s'agit pas d'un pont entre brokers (bridge).

[Code source et référence de configuration](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/mqtt_client) · [Documentation en anglais](/en/projects/mqtt-client/)

## Configuration et sélection {#einrichtung-und-auswahl}

1. Ajoutez `https://github.com/rockbaer2007/ugso-ha-mqtt-addons` depuis l'App Store de Home Assistant. 2. Installer et lancer le **client MQTT** ; les architectures amd64 et aarch64 sont prises en charge.
3. Ouvrir l'interface web et enregistrer l'hôte, le port, l'utilisateur et le mot de passe du broker externe. En l'absence de TLS, le port par défaut est 1883.
4. Sélectionner un appareil sur la gauche. Dans la fenêtre qui s'affiche, ses entités sont regroupées par catégories : commandes, capteurs, configuration et diagnostic. La fonction de recherche permet également de trouver des entités au sein d'un appareil.
5. Sélectionner les valeurs et attributs souhaités. La case à cocher située à droite d'une ligne de valeur permet de transférer l'état ainsi que tous les attributs associés ; la sélection de l'appareil permet quant à elle d'inclure toutes les valeurs de celui-ci.

Les modifications sont appliquées immédiatement. Aucun jeton d'accès (access token) HA supplémentaire n'est requis : l'application utilise l'accès « Supervisor » pour interagir avec l'API HA Core. En cas d'utilisation de plusieurs instances, veillez à employer des identifiants client (client IDs) et des préfixes de sujet (topic prefixes) distincts.

## Transmettre les états avec une étiquette Home Assistant {#weiterleitung-per-label}

![Dialogue Home Assistant de création d’une étiquette](/images/projects/mqtt-client/ha-label-erstellen.png)

*Exemple dans Home Assistant : l’étiquette s’appelle « zu mqtt client ». Saisissez dans le client MQTT l’identifiant de l’étiquette que vous avez créée.*

1. **Créez l’étiquette :** Dans Home Assistant, ouvrez **Paramètres → Zones, étiquettes et zones géographiques → Étiquettes**. Créez **zu mqtt client**, comme sur la capture.
2. **Relevez l’identifiant :** Ouvrez **Paramètres → Outils → Modèle** (**Outils de développement → Modèle** dans les anciennes versions). Collez le modèle ci-dessous et copiez le résultat, par exemple `zu_mqtt_client`.
3. **Saisissez l’identifiant dans le client MQTT :** Ouvrez **MQTT-Client** dans la barre latérale de Home Assistant. Dépliez **Übertragung und TLS** (Transmission et TLS). Collez le résultat dans **HA-Label-ID für Zustandsweiterleitung**, juste sous **Topic-Präfix**, puis cliquez sur **Speichern und verbinden** (Enregistrer et connecter).
4. **Attribuez l’étiquette :** Ouvrez **Paramètres → Appareils et services → Entités**, sélectionnez l’entité et ouvrez ses paramètres avec la roue dentée. Choisissez **Ajouter une étiquette → zu mqtt client**, puis cliquez sur **Mettre à jour**.

```jinja
{{ label_id("zu mqtt client") }}
```

[Home Assistant · label_id](https://www.home-assistant.io/template-functions/label_id/)

Le client vérifie les associations selon l’intervalle d’interrogation configuré. L’étiquette transmet l’état et les métadonnées standard et active les commandes prises en charge. Les autres attributs restent sélectionnables manuellement. Le retrait de l’étiquette arrête la transmission et les commandes automatiques. Les entités sélectionnées manuellement restent actives. Le nettoyage des topics persistants permet de supprimer la dernière valeur MQTT mémorisée si nécessaire.

Essai effectué sur Home Assistant `.177` avec un broker MQTT séparé. Après l’ajout de l’étiquette, le broker a reçu `off` et `on`. Après son retrait, le changement d’état suivant n’a plus été envoyé. [Release 0.1.17](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/mqtt-client-v0.1.17)

## Transmission en temps réel et état {#live-ubertragung-und-status}

Après le chargement initial de l'état complet, l'application traite les changements d'état de HA en temps réel via WebSocket. Si la connexion à HA est rétablie, l'état initial est rechargé ; si la connexion MQTT est rétablie, toutes les valeurs sélectionnées sont retransmises.

En cas de défaillance de la connexion en temps réel, le mécanisme d'interrogation (polling) précédent prend le relais — configuré par défaut sur un intervalle de cinq secondes, mais ajustable via `poll_interval` (de 1 à 300 secondes). Les changements survenus pendant une interruption ou entre deux intervalles d'interrogation ne peuvent pas être reconstitués a posteriori. Une saturation de la file d'attente des événements est signalée et déclenche une resynchronisation.

L'état permet de distinguer la connexion MQTT de l'accessibilité de HA ; il affiche le mode actif (temps réel/interrogation), l'heure de la dernière synchronisation, la date de la dernière publication, le nombre total de publications, ainsi que tout type d'erreur ayant été résolu. Les identifiants d'accès et le contenu des messages (payloads) ne sont pas affichés.

| Sujet MQTT | Contenu |
| --- | --- |
| `<topic_prefix>/<device>/<value>/state` | État sous forme textuelle |
| `<topic_prefix>/<device>/<value>/attribute/<attribute>` | Attribut sélectionné |
| `<topic_prefix>/<device>/<value>/set` | Canal de retour pour les commandes de contrôle prises en charge |
| `<topic_prefix>/availability` | `online` en cas de synchronisation HA réussie ; sinon `offline` |

Le préfixe par défaut est `ha_external`. Les états et les attributs sont publiés avec un niveau de QoS 1 et le drapeau « retain » (conservation) ; aucune configuration de découverte MQTT (MQTT discovery) n'est générée. Lors de la connexion initiale, les états et les attributs sont envoyés avant les canaux de retour d'information `/set`, avec un intervalle par défaut de 50 ms entre chaque publication. Les messages `unknown` et `unavailable` sont transmis tels quels ; les entités inexistantes renvoient `unavailable`.

## Commandes de contrôle vers HA {#steuerbefehle-zuruck-an-ha}

Les canaux de retour d'information sont automatiquement activés pour les entités contrôlables sélectionnées. Les capteurs restent en mode « sortie uniquement ». Envoyez les commandes vers le sujet (`topic`) `/set` correspondant, **sans utiliser l'indicateur « retain »**.

| Entité | Données (Payload) |
| --- | --- |
| Entité commutable | `ON` ou `OFF` |
| `number`, `input_number` | Valeur numérique |
| `select`, `input_select` | Nom d'une option disponible |
| `text`, `input_text` | Texte |
| `button`, `input_button` | `PRESS` |
| `cover` | `OPEN`, `CLOSE`, `STOP` ou `{"position":45}` |
| `light` | `{"brightness_pct":75}` |
| `fan` | `{"percentage":50}` |

Les commandes JSON n'autorisent que le champ spécifié, accompagné d'une valeur numérique comprise entre 0 et 100. L'appareil HA (Home Assistant) doit prendre en charge cette fonctionnalité. Les anciens identifiants d'entité (Entity IDs), tels que `ha_external/switch.plug/set`, restent valides. Les messages avec l'indicateur « retain » (persistant), les commandes obsolètes et les contenus non valides sont ignorés ; l'exécution d'actions HA arbitraires n'est pas prévue.

## Suppression des « topics » persistants (retain topics) obsolètes {#veraltete-retain-topics-entfernen}

La fonction **Vérifier les « topics » persistants obsolètes** affiche les « topics » enregistrés qui ne sont plus utilisés en raison de modifications apportées à la sélection, aux préfixes ou aux noms des appareils. Sélectionnez les « topics » concernés et confirmez leur suppression ; un maximum de 100 éléments peut être traité par opération.

L'application supprime uniquement les publications qu'elle a elle-même effectuées et confirmées avec succès sur le broker actuellement configuré. Les « topics » actifs ainsi que ceux créés par d'autres sources restent intacts. L'inventaire est conservé de manière permanente sous `/data/mqtt-topics.json`. En cas d'échec de la suppression, l'élément est conservé pour une nouvelle tentative ultérieure. Il n'existe **pas de nettoyage automatique**. Les anciens « topics » non répertoriés, créés avant cette mise à jour, doivent être supprimés directement sur le broker.

## Sauvegarde et restauration des paramètres {#einstellungen-sichern-und-wiederherstellen}

La fonction **Sauvegarder les paramètres** permet de télécharger un fichier JSON contenant les paramètres du broker, l'identifiant client (Client ID), le préfixe des « topics », la sélection, l'intervalle d'interrogation, l'espacement des publications et l'autorité de certification (CA) personnalisée. La fonction **Ouvrir une sauvegarde** vérifie le contenu du fichier et demande une confirmation avant de procéder au remplacement des paramètres actuels.

Le fichier ne contient **ni mot de passe MQTT, ni certificat client, ni clé privée, ni jeton (token) HA**. Il n'est pas chiffré. Si vous utilisez le même broker, les identifiants et le certificat/la clé client stockés localement sont conservés. Si vous changez de broker, ces informations doivent être saisies à nouveau. Les messages « retained » (conservés) ne sont pas inclus ; cette procédure ne remplace pas une sauvegarde complète de l'application HA.

## TLS avec certificats personnalisés {#tls-mit-eigenen-zertifikaten}

Dans la section **Transmission et TLS**, vous pouvez charger des fichiers PEM (contenant une autorité de certification, un certificat client et une clé privée) ou coller leur contenu textuel. Le certificat et la clé doivent être fournis ensemble. Le port TLS dépend du broker utilisé ; il s'agit souvent du port 8883.

Le certificat du serveur et le nom d'hôte sont systématiquement vérifiés, soit via les autorités de confiance du système, soit via une autorité de certification (CA) personnalisée. Si les champs de données sensibles sont laissés vides, les valeurs précédemment enregistrées sont conservées. Pour les supprimer, cochez l'option spécifique **Supprimer les certificats et clés TLS enregistrés** et enregistrez vos modifications. Toute configuration TLS invalide sera rejetée lors de la tentative de modification des paramètres.

## Mise à jour et compatibilité {#update-und-kompatibilitat}

Les paramètres existants issus de 0.1.15 restent valides : les identifiants du broker, la sélection des appareils/attributs, l'ID client, le préfixe des sujets (topics), l'intervalle d'interrogation et l'intervalle de publication ne sont pas modifiés au démarrage. La configuration TLS est conservée ; les nouveaux champs relatifs aux certificats sont vides par défaut. Les données conservées (« retained data ») ne sont pas supprimées lors de la mise à jour.

La version 0.1.16 a été validée via des tests backend, un broker MQTT, un point de terminaison WebSocket, TLS avec certificat client, une interface web et un déploiement Docker. L'installation effective dans Home Assistant (HA) ainsi que les fonctionnalités prises en charge doivent être vérifiées dans votre propre environnement.
