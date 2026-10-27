<a id="statut"></a>

# Installation {#installation}

::: warning Archives : développement arrêté
Ce guide concerne l'ancienne version du paquet. « Parcel Tracker » étant une solution beaucoup plus aboutie, nous avons décidé de stopper le développement de « Parcel to MQTT ». Consultez [Parcel Tracker par SoerenKaiser99](https://github.com/SoerenKaiser99/parcel_tracker) pour découvrir cette alternative et savoir comment l'installer.
:::

L'ancienne version du paquet se trouve dans le [dossier `parcel_to_mqtt` du dépôt d'add-ons partagé](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/parcel_to_mqtt). Dans Home Assistant, saisissez l'URL du dépôt indiquée ci-dessous (sans inclure `/tree/master/parcel_to_mqtt`).

[![Ouvrir Parcel to MQTT dans Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Frockbaer2007%2Fugso-ha-mqtt-addons)

1. Ouvrez Home Assistant.
2. Allez dans **Paramètres > Modules complémentaires > Boutique des modules complémentaires**.
3. Ouvrez la section **Dépôts** via le menu (les trois points).
4. Ajoutez ce dépôt :

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

5. Installez **Parcel to MQTT**.
6. Saisissez vos numéros de suivi DHL.
7. Lancez l'application.

La découverte MQTT (MQTT Discovery) doit être activée dans Home Assistant. Un broker MQTT est requis.
