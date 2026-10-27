<a id="entites"></a>
<a id="statut"></a>

# Entités {#entitaten}

Les entités sont créées via la découverte MQTT (MQTT Discovery).

## Répondeur {#anrufbeantworter}

Pour chaque répondeur détecté, des entités (allant de `AB0` à `AB4`) sont créées :

- Nouveaux messages
- Anciens messages
- État
- Interrupteur Marche/Arrêt

Le nom du répondeur (tel qu'il apparaît dans la FRITZ!Box) est conservé en tant qu'attribut, mais n'est pas utilisé dans les noms des entités.

## Wi-Fi {#wlan}

Selon le modèle de FRITZ!Box, les éléments suivants sont créés :

- Wi-Fi 2,4 GHz Marche/Arrêt
- Wi-Fi 2,4 GHz État
- Wi-Fi 5 GHz Marche/Arrêt
- Wi-Fi 5 GHz État
- Wi-Fi Invité Marche/Arrêt
- Wi-Fi Invité État

Les capteurs d'état Wi-Fi affichent `Ein` ou `Aus` ; l'état brut fourni par la FRITZ!Box est conservé sous forme d'attribut.

## WAN et état de la FRITZ!Box {#wan-und-box-status}

- Connexion (téléchargement)
- Connexion (envoi)
- Débit de téléchargement
- Débit d'envoi
- État de la liaison WAN
- Rôle de la FRITZ!Box dans le réseau Mesh
- Connexion PPP de la FRITZ!Box
- Adresse IPv4 externe (PPP)
- Adresse IPv6 externe
- État DECT
- DNS over TLS

`WAN Link Status` indique également `Ein` ou `Aus`.

Les valeurs facultatives non fournies par la FRITZ!Box sont masquées ou publiées sous la forme `unknown`.

## Listes d'appels et moniteur d'appels en direct {#anruflisten-und-live-anrufmonitor}

Listes d'appels configurables :

- tous les appels
- appels entrants
- appels sortants
- appels manqués
- appels rejetés
- appels bloqués

Le moniteur d'appels en temps réel fournit des événements tels que `RING`, `CALL`, `CONNECT` et `DISCONNECT`.

## Répertoires téléphoniques {#telefonbucher}

Les répertoires téléphoniques sont affichés avec les noms détectés de la FRITZ!Box. Les listes de blocage Tellows peuvent être masquées via des filtres de nom ou renommées de manière explicite via `phonebook_names`.

## DECT {#dect}

Les informations suivantes sont publiées (en option) pour chaque combiné DECT détecté :

- numéro interne
- identifiant de l'appareil

`NoRingTime` n'est volontairement plus publié.
