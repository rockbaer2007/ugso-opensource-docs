<a id="statut"></a>

# Installation {#installation}

## Exigences {#voraussetzungen}

- Home Assistant avec Supervisor/App Store.
- Un broker MQTT, par exemple l'application Mosquitto Broker.
- L'intégration MQTT activée dans Home Assistant.
- Un utilisateur FRITZ!Box disposant des droits appropriés pour la téléphonie, l'état du réseau et les données de la maison intelligente (Smart Home) / du système.
- Le protocole TR-064 activé sur la FRITZ!Box.

## Ajouter le dépôt d'applications {#app-repository-hinzufugen}

Vous pouvez ouvrir le dépôt directement dans Home Assistant en utilisant ce bouton :

[![Ouvrir FRITZ!Box to MQTT dans Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Frockbaer2007%2Fugso-ha-mqtt-addons)

1. Ouvrez Home Assistant.
2. Allez dans **Paramètres > Modules complémentaires > Boutique des modules complémentaires** (App Store).
3. Dans le menu (les trois points), sélectionnez **Dépôts**.
4. Ajoutez ce dépôt :

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

5. Installez **FRITZ!Box to MQTT**.
6. Remplissez la configuration.
7. Démarrez l'application.

## Développement local {#lokale-entwicklung}

Si vous souhaitez tester la version actuelle en local dans Home Assistant, copiez le
dossier de l'add-on depuis le dépôt central vers le dossier Home-Assistant-`addons` :

```text
C:\Users\rockb\source\repos\ugso-ha-mqtt-addons\fritzbox_tr064_tam
```

Destination dans Home Assistant :

```text
/addons/fritzbox_tr064_tam
```

Ensuite, rechargez les dépôts dans la boutique d'add-ons de Home Assistant,
mettez à jour ou installez l'add-on, puis redémarrez.

## HACS {#hacs}

HACS n'est pas la méthode d'installation appropriée pour ce projet. L'application fonctionne en tant que service « Supervisor » basé sur Docker et s'installe via le magasin d'applications de Home Assistant.
