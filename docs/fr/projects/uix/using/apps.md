---
title: Styliser les panneaux d'applications et d'Ingress
description: Styliser avec UIX les panneaux d'applications et d'Ingress de Home Assistant.
---
# Styliser les panneaux d'applications et d'Ingress

Home Assistant affiche chaque page d'application ou d'Ingress dans un élément `<ha-panel-app>`. Utilisez la clé de thème `uix-app` ou `uix-app-yaml` pour styliser la racine Shadow DOM ouverte de ce panneau.

Il ne s'agit pas de la liste des applications installées à l'adresse `/config/apps/installed`. Celle-ci appartient au panneau de configuration et utilise `uix-config`.

## Exemple

Cet exemple stylise l'en-tête du panneau Home Assistant et place une superposition CRT non interactive au-dessus de l'iframe Ingress. Il applique également un style au document Zigbee2MQTT dans cette iframe.

Activez l'option expérimentale [Styliser les panneaux intégrés dans un frame](../extras/style-frame-panels) avant d'utiliser le bloc `uix-zigbee2mqtt`.

```yaml
My theme:
  uix-theme: My theme

  uix-app: |
    :host {
      position: relative;
    }

    .header {
      background: #041b0b !important;
      color: #7cff88 !important;
    }

    :host::after {
      content: "";
      position: absolute;
      inset: 0;
      z-index: 1;
      pointer-events: none;
      background: repeating-linear-gradient(
        to bottom,
        rgb(124 255 136 / 8%) 0,
        rgb(124 255 136 / 8%) 1px,
        transparent 1px,
        transparent 3px
      );
    }

  # This is inside the Zigbee2MQTT iframe, not ha-panel-app.
  uix-zigbee2mqtt: |
    :root {
      --color-base-100: #041b0b;
      --color-base-content: #7cff88;
      --bg-color: #041b0b;
    }
```

![Exemple de style d'un panneau d'application](/projects/uix/app-panel-example.png)

## Portée

::: info
Le style des frames d'applications de même origine est disponible à partir de UIX 3.4.0-beta.1.
:::

`uix-app` continue de styliser l'habillage du panneau Home Assistant et peut superposer son iframe. UIX installe également son moteur interne dans les frames d'applications de même origine. Le style du contenu de la frame nécessite l'option expérimentale [Styliser les panneaux intégrés dans un frame](../extras/style-frame-panels) ; le style de l'élément hôte n'en dépend pas.

Pour le contenu de la frame, utilisez `uix-<add-on-slug>` ou sa variante `-yaml`. UIX vérifie d'abord le slug complet du module complémentaire Home Assistant, puis un slug indépendant du dépôt après suppression de `core_`, `local_` ou d'un hash de dépôt de huit caractères. Par exemple, `uix-a0d7b954_nodered` est prioritaire sur `uix-nodered`.

Le moteur des frames est une API interne partagée avec les frames de panneaux personnalisés. Les notions visibles restent distinctes : `uix-app` désigne toujours le conteneur `<ha-panel-app>`, tandis que `uix-panel-custom` désigne toujours le conteneur `<ha-panel-custom>`.
