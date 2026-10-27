<a id="statut"></a>

# Installation {#installation}

Vous pouvez ouvrir le dépôt directement dans Home Assistant en utilisant ce bouton :

[![Ouvrir Heizöl to MQTT dans Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Frockbaer2007%2Fheizoel-to-mqtt)

## Ajouter le dépôt d'applications {#app-repository-hinzufugen}

1. Ouvrez Home Assistant.
2. Allez dans **Paramètres > Modules complémentaires > Boutique des modules complémentaires** (App Store).
3. Dans le menu (les trois points), sélectionnez **Dépôts**.
4. Ajoutez ce dépôt :

```text
https://github.com/rockbaer2007/heizoel-to-mqtt
```

5. Installer **Heizöl to MQTT**.
6. Configurer le code postal, les quantités et les sources.
7. Lancer l'application.

## MQTT {#mqtt}

L'application utilise le service MQTT interne de Home Assistant si le broker Mosquitto est disponible en tant qu'application.
