---
title: Abschnittshintergründe
description: Section-Hintergründe in Home Assistant mit UIX stylen.
---
# Abschnittshintergründe stylen

UIX kann Hintergründe für Dashboard-Abschnitte setzen. Das ist besonders für Section-Views nützlich, bei denen Home Assistant einzelne Bereiche als eigene Container rendert.

## Option 1: UIX-CSS-Variablen verwenden

UIX stellt Variablen bereit, die direkt in einem Theme gesetzt werden können. Sie werden auf den Section-Hintergrund angewendet und können Farben, Gradients oder Bilder enthalten.

::: info
Diese Methode eignet sich gut, wenn derselbe Stil für viele Abschnitte gelten soll oder wenn ein Theme zentral gesteuert wird.
:::

::: details Beispiel

```yaml
my-theme:
  uix-theme: my-theme
  uix-grid-section: |
    :host {
      --uix-section-background: linear-gradient(135deg, #1b263b, #415a77);
    }
```

:::

## Option 2: UIX-Styling direkt an der Section-Konfiguration

Wenn nur ein einzelner Abschnitt angepasst werden soll, kann UIX direkt in der Section-Konfiguration genutzt werden.

::: details Beispiel

```yaml
type: section
title: Klima
uix:
  style: |
    :host {
      background: rgba(0, 0, 0, 0.18);
      border-radius: 16px;
      padding: 8px;
    }
cards:
  - type: tile
    entity: climate.living_room
```

:::

Nutze direkte Section-Styles sparsam, wenn dieselbe Gestaltung mehrfach gebraucht wird. Für wiederkehrende Gestaltung ist ein Theme leichter zu warten.
