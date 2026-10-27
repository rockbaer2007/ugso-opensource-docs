<a id="depannage"></a>
<a id="statut"></a>

# Dépannage {#fehlersuche}

## MQTT signale `Not authorized` {#mqtt-meldet-not-authorized}

L'application utilise le service MQTT interne de Home Assistant. Vérifiez :

- que l'application « Mosquitto broker » est installée et démarrée
- que l'intégration MQTT est configurée
- que l'application a été redémarrée une fois Mosquitto disponible

## La FRITZ!Box signale `401 Unauthorized` {#fritz-box-meldet-401-unauthorized}

Vérifiez le nom d'utilisateur, le mot de passe et les autorisations de l'utilisateur FRITZ!Box. L'utilisateur doit disposer des droits d'accès aux données FRITZ!Box requises.

## Certaines valeurs restent à `unknown` {#einzelne-werte-bleiben-unknown}

Toutes les FRITZ!Box ne fournissent pas l'ensemble des données via les mêmes interfaces. L'application tente d'utiliser TR-064, la découverte de services (Service Discovery) ainsi que des mécanismes de repli (fallbacks) via Web/Lua. Si une valeur est manquante, activez `log_value_details` et examinez les lignes de journal correspondantes.

## Port `1012` {#port-1012}

Le port `1012` est réservé au suivi des appels en temps réel. Les débits d'envoi (upload) et de réception (download) ainsi que l'état de la FRITZ!Box ne sont pas transmis via le port `1012`.

## HACS ne trouve pas le projet {#hacs-findet-das-projekt-nicht}

C'est normal. Ce projet est une application « Supervisor » ; il s'installe en tant que dépôt (repository) via la boutique d'applications de Home Assistant, et non via HACS.
