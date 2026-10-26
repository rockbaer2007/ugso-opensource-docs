---
title: Abschnittshintergründe
description: Hintergrundfarbe und Deckkraft von Home-Assistant-Abschnitten mit UIX gestalten.
---
# Abschnittshintergründe stylen

Der Hintergrund eines Abschnitts ist ein Geschwisterelement des Abschnitts und lässt sich deshalb nicht direkt über dessen normale Styles erreichen. Das Original beschreibt zwei Wege: UIX-Variablen für Farbe und Deckkraft oder UIX-Styling direkt in der Hintergrundkonfiguration.

## Option 1: UIX-CSS-Variablen verwenden

Setze `--uix-section-background-color` und `--uix-section-background-opacity` am Abschnitt oder einem Vorfahren. Templates sind möglich. Die Hintergrundkonfiguration muss aktiviert sein; `background: true` ist die von Home Assistant unterstützte Kurzform mit Standardfarbe und Standarddeckkraft.

::: info
`hui-section-background` ist ein Geschwisterelement. `--ha-section-background-color` im normalen Abschnitts-Styling erreicht es deshalb nicht. UIX überträgt bei jeder Aktualisierung `--section-background-color` und `--section-background-opacity` direkt auf dieses Hintergrundelement.
:::

```yaml
type: grid
cards: []
background: true
uix:
  style: |
    :host {
        --uix-section-background-color: {{ 'red' if is_state('input_boolean.test_boolean', 'on') else 'green' }};
        --uix-section-background-opacity: {{ states('input_number.increment_test') | float / 100 }};
    }
```

## Option 2: UIX-Styling in der Hintergrundkonfiguration

`background.uix` gestaltet das Hintergrundelement selbst. Die gesamte Abschnittskonfiguration steht Templates zur Verfügung. Für Farbe und Deckkraft verwende dort `--ha-section-background-color` und `--ha-section-background-opacity`. Direkte CSS-Eigenschaften für Hintergrund und Deckkraft benötigen andernfalls `!important`.

```yaml
type: grid
cards: []
background:
  uix:
    style: |
      :host {
        --ha-section-background-color: yellow;
        border: 2px solid red;
        box-shadow: 10px 5px 5px red;
      }
```
