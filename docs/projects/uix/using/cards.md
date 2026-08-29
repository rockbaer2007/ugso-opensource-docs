---
title: Karten
description: Karten mit UIX stylen.
---
# Karten stylen

Karten werden gestylt, indem der Kartenkonfiguration ein `uix`-Block hinzugefügt wird:

```yaml
uix:
  style: <styles>
```

In der einfachsten Form ist `<styles>` ein CSS-String, der je nach Kartentyp in das passende Element injiziert wird. Wo UIX genau angewendet wird, hängt davon ab, ob die Karte von Home Assistant über `<hui-card>` gerendert wird oder ob eine Custom Card selbst ein `<ha-card>` enthält.

::: info
UI eXtension funktioniert mit Karten, die in einem `<hui-card>` enthalten sind, oder mit Karten, die ein `<ha-card>` enthalten. Das umfasst fast alle Standardkarten von Home Assistant und viele Custom Cards.
:::

Bei Karten innerhalb eines `<hui-card>` wird das Styling in einen Shadow Root injiziert. Das unterste Element ist dann `:host`; in vielen Standardkarten ist das erste Element im Shadow Root zusätzlich `<ha-card>`.

Bei vielen Custom Cards, die nicht den modernen `<hui-root>`-Container verwenden, aber ein `<ha-card>` enthalten, wird das Styling direkt in `ha-card` injiziert. Weitere Details stehen unter [Konzepte - Anwendung](../concepts/application).

::: tip CSS-Variablen
Home-Assistant-Themes nutzen intensiv CSS-Variablen. Diese können in UIX gesetzt und gelesen werden. CSS-Variablen beginnen mit zwei Bindestrichen:

```yaml
type: tile
entity: light.bed_light
vertical: false
features_position: bottom
uix:
  style: |
    ha-card {
      --ha-card-background: teal;
      --ha-tile-info-primary-color: var(--yellow-color);
      --ha-tile-info-secondary-color: var(--white-color);
    }
```

![Styling with CSS variables](https://raw.githubusercontent.com/Lint-Free-Technology/uix/9a0fa57d4afd262a5eaec4f1bfb7c154667bb2c9/docs/source/assets/page-assets/using/basic-first-uix.png)
:::

## Lokales Theme für ein gestyltes Element

Optional kann für genau dieses UIX-Element ein lokales Home-Assistant-Theme gesetzt werden. Das Theme kann wiederum [UIX Themes](./themes) enthalten.

```yaml
uix:
  theme: my-awesome-theme
  style: |
    ha-card {
      color: var(--primary-color);
    }
```

`uix.theme` überschreibt das geerbte oder aktuelle Theme für diesen UIX-Knoten und seine UIX-Kindpfade, solange ein Kind kein eigenes `theme` setzt. Ein vollständiges Beispiel steht unter [UIX Themes - Override mit `uix.theme`](./themes#lokales-theme-override-mit-uixtheme).

## Eigene CSS-Variablen

UIX-Themes können eigene CSS-Variablen bereitstellen. Sinnvoll ist das hoch in der Frontend-Hierarchie, zum Beispiel über `uix-drawer`, `uix-view` oder `uix-root`:

```yaml
uix-drawer: |
  :host {
    &#123;% set isDark = is_state('sun.sun','below_horizon') %&#125;
    --darkslateblue-if-dark: &#123;&#123; 'darkslateblue' if isDark else 'red' &#125;&#125;;
    --slategrey-if-dark: &#123;&#123; 'slategrey' if isDark else 'green' &#125;&#125;;
    --yellow-if-not-dark: &#123;&#123; 'yellow' if not isDark else 'pink' &#125;&#125;;
    --orange-if-not-dark: &#123;&#123; 'orange' if not isDark else 'purple' &#125;&#125;;
  }
```

Weiter unten in der Frontend-Hierarchie können diese Variablen verwendet werden, etwa in `uix-card`, `uix-dialog` oder direkt in einem Karten-`uix`:

```yaml
type: entities
entities:
  - entity: sun.sun
    uix:
      style: |
        hui-generic-entity-row {
          background: var(--darkslateblue-if-dark);
          color: var(--slategrey-if-dark);
          --state-icon-color: var(--slategrey-if-dark);
        }
  - entity: sun.sun
    uix:
      style: |
        hui-generic-entity-row {
          background: var(--yellow-if-not-dark);
          color: var(--orange-if-not-dark);
          --state-icon-color: var(--orange-if-not-dark);
        }
  - entity: sun.sun
```

![Custom CSS variables](https://raw.githubusercontent.com/Lint-Free-Technology/uix/9a0fa57d4afd262a5eaec4f1bfb7c154667bb2c9/docs/source/assets/page-assets/using/custom-css-variables.png)
