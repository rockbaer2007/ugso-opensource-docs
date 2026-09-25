---
title: App- und Ingress-Panels stylen
description: Home-Assistant-App- und Ingress-Panels mit UIX stylen.
---
# App- und Ingress-Panels stylen

Home Assistant zeigt einzelne Apps und Ingress-Seiten in einem `<ha-panel-app>`-Element an. Mit dem Theme-Schlüssel `uix-app` oder `uix-app-yaml` kannst du den offenen Shadow Root dieses Panels stylen.

Das ist nicht die Liste der installierten Apps unter `/config/apps/installed`. Diese gehört zum Konfigurationspanel und verwendet `uix-config`.

## Beispiel

Dieses Beispiel stylt den Header des Home-Assistant-Panels, legt eine nicht interaktive CRT-Überlagerung über das Ingress-iframe und stylt außerdem das Zigbee2MQTT-Dokument innerhalb dieses iframes.

Aktiviere die experimentelle Option [Frame-Panels stylen](../extras/style-frame-panels), bevor du den Abschnitt `uix-zigbee2mqtt` verwendest.

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

![Beispiel für App-Panel-Styling](/projects/uix/app-panel-example.png)

## Geltungsbereich

::: info
Das Styling gleichursprünglicher App-Frames ist ab UIX 3.4.0-beta.1 verfügbar.
:::

`uix-app` stylt weiterhin die Oberfläche des Home-Assistant-Panels und kann dessen iframe überlagern. Zusätzlich installiert UIX seine interne Frame-Laufzeit in gleichursprünglichen App-Frames. Das Styling der Frame-Inhalte erfordert die experimentelle Option [Frame-Panels stylen](../extras/style-frame-panels); das Styling des Host-Elements nicht.

Für Frame-Inhalte verwendest du `uix-<app-slug>` oder die Variante mit `-yaml`. UIX prüft zuerst den vollständigen Home-Assistant-App-Slug und danach einen vom Repository unabhängigen Slug, bei dem `core_`, `local_` oder ein achtstelliger Repository-Hash entfernt wurde. `uix-a0d7b954_nodered` hat beispielsweise Vorrang vor `uix-nodered`.

::: tip
Den App-Slug für `uix-<app-slug>` findest du am einfachsten in der Browser-Entwicklerkonsole. Die von `uixFrame.js` ausgegebene UIX-Ladeinformation sieht beispielsweise so aus:

<span style="background:#CE3226;color:white;padding:2px 5px;font-weight:bold;border-radius:5px;">💡 UIX 8.4.0 IS INSTALLED 💡 for 45df7312_zigbee2mqtt</span>

Der letzte Teil der Meldung ist der App-Slug, hier also `45df7312_zigbee2mqtt`.
:::

Die Frame-Laufzeit ist eine interne API, die auch von Custom-Panel-Frames verwendet wird. Die Begriffe für Nutzer bleiben getrennt: `uix-app` bezeichnet immer den Container `<ha-panel-app>`, `uix-panel-custom` immer den Container `<ha-panel-custom>`.

## Styling

Einige App-Panels wie das KNX-Frontend verwenden `ha-card` zur Darstellung von Informationen. Damit dein `uix-card`- oder `uix-card-yaml`-Theme dort greift, aktiviere die experimentelle Option [Always patch ha-card](../extras/always-patch-ha-card).
