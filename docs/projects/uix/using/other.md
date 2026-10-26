---
title: Weitere Styling-Optionen
description: custom:mod-card als selten benötigten Ausweg für spezielle Karten verwenden.
---
# Weitere Styling-Optionen

Karten ohne `<ha-element>` lassen sich mit der mitgelieferten Karte `custom:mod-card` umschließen. Das ist nur in sehr wenigen Fällen notwendig und kann mehr Probleme verursachen, als es löst. Oft enthält die Karte eine andere Karte; dann sollte das Styling auf diese innere Karte angewendet werden.

::: warning custom:mod-card mit Vorsicht verwenden
Der Wrapper erzeugt ein `<ha-card>` und setzt die eigentliche Karte hinein. Die eingeschlossene Karte wird transparent und ohne Rahmen oder Hintergrund gestaltet.
:::

```yaml
type: custom:mod-card
card:
  type: custom:beloved-custom-card
  ...
uix:
  style: |
    ha-card {
      ...
    }
```

Die Auslassungspunkte im Originalbeispiel sind Platzhalter für deine Kartenkonfiguration und CSS-Regeln; sie bilden keine direkt ausführbare Beispielkonfiguration.
