<a id="configuration"></a>
<a id="statut"></a>

# Configuration {#konfiguration}

Exemple :

```yaml
ip: 192.168.178.1
port: 49000
user: homeassistant
password: secret
call_lists: all,incoming,outgoing,missed,rejected,blocked
phonebooks: all
phonebook_names: 3:tellows Sperrliste 7,4:tellows Sperrliste 8-9
phonebook_name_excludes: ""
poll_interval: 120
call_list_poll_interval: 600
tam_poll_interval: 600
dect_poll_interval: 600
phonebook_poll_interval: 3600
call_monitor_enabled: true
call_monitor_port: 1012
max_calls: 20
max_live_events: 20
include_dect_lines: false
max_dect_lines: 6
dns_over_tls_enabled: true
log_value_details: true
```

## Options importantes {#wichtige-optionen}

`ip` correspond à l'adresse fixe de la FRITZ!Box. Cette option est préférable à `fritz.box` si plusieurs FRITZ!Box sont présentes sur le réseau.

`port` correspond au port TR-064. La valeur par défaut est `49000`.

`call_monitor_port` correspond au port du moniteur d'appels en temps réel. La valeur par défaut est `1012`.

Les requêtes adressées à la FRITZ!Box sont réparties en groupes afin de réduire la charge sur la box :

- `poll_interval` : Wi-Fi, WAN et état général de la box ; intervalle par défaut : `120` secondes
- `call_list_poll_interval` : Journaux d'appels ; intervalle par défaut : `600` secondes
- `tam_poll_interval` : Répondeur ; intervalle par défaut : `600` secondes
- `dect_poll_interval` : État DECT et lignes DECT optionnelles ; intervalle par défaut : `600` secondes
- `phonebook_poll_interval` : Répertoires téléphoniques ; intervalle par défaut : `3600` secondes

Le moniteur d'appels en temps réel reste quant à lui actif en permanence et signale les événements directement via le port `1012`.

Si la connexion WAN/DSL est détectée comme étant hors ligne, l'application suspend les requêtes concernant les journaux d'appels,
le répondeur, le système DECT et les répertoires. Seules les requêtes relatives au Wi-Fi, au WAN
et à l'état général de la connexion restent actives, permettant ainsi à l'application de détecter le rétablissement de la
connexion. Dès que la connexion WAN/DSL est de nouveau en ligne, les groupes précédemment suspendus
font l'objet d'une mise à jour immédiate.
Les capteurs de diagnostic `Abfrage Modus` et `Abfrage Hinweis` indiquent alors si
toutes les requêtes sont en cours (`full`) ou si certaines requêtes détaillées sont suspendues
pendant que la FRITZ!Box rétablit la connexion (`limited`).

## État de la requête dans Home Assistant {#abfragestatus-in-home-assistant}

L'application expose deux capteurs de diagnostic destinés aux tableaux de bord et aux automatisations :

- `Abfrage Modus` : état technique pour les automatisations
- `Abfrage Hinweis` : texte informatif lisible pour les cartes de tableau de bord

Sujets (topics) MQTT :

- `fritzbox/polling/mode`
- `fritzbox/polling/message`
- `fritzbox/polling/attributes`

Valeurs possibles pour `Abfrage Modus` :

- `full` : WAN/DSL en ligne, toutes les requêtes de groupe s'effectuent normalement
- `limited` : WAN/DSL hors ligne, les requêtes détaillées sont suspendues
- `unknown` : l'état de la connexion est en cours de détermination

Exemple d'automatisation dans Home Assistant :

```yaml
alias: FRITZBox Detailabfragen pausiert
trigger:
  - platform: state
    entity_id: sensor.abfrage_modus
    to: "limited"
action:
  - service: persistent_notification.create
    data:
      title: "FRITZ!Box baut Verbindung auf"
      message: "Detailabfragen sind pausiert. Sobald WAN/DSL wieder online ist, werden alle Gruppen nachgezogen."
```

Adaptez `entity_id` au nom réel de l'entité dans votre installation Home Assistant.

`phonebooks` contrôle les répertoires affichés au démarrage. Après la première analyse réussie, l'affichage peut être modifié via l'entité de sélection (select) dans Home Assistant.

`phonebook_names` remplace les noms de répertoires génériques.

`include_dect_lines` active les capteurs optionnels pour les combinés DECT.

`log_value_details` écrit les valeurs brutes et les valeurs normalisées dans le journal de l'application. Pour une utilisation normale, cette fonction peut être désactivée une fois le dépannage terminé.

## MQTT {#mqtt}

Si le service MQTT de Home Assistant est disponible, l'application récupère automatiquement les informations relatives au broker, au port et aux identifiants d'accès internes.
