---
title: Custom Panels
description: Custom Panels mit UIX stylen.
---
# Custom Panels stylen

::: info iframe-Custom-Panels ab UIX 8.2.0-beta.1
Direkt geladene Custom Panels kann UIX bereits stylen. Styling für Custom Panels, die als iframe geladen werden, ist experimentell und muss aktiviert werden. Siehe [Extras - Custom Panels als iframe stylen](../extras/style-custom-panels).
:::

UIX stylt Custom Panels, die nicht als iframe geladen werden, direkt. Es kann außerdem Custom Panels stylen, die als iframe geladen werden. Diese Funktion ist aktuell experimentell.

::: info So funktioniert iframe-Styling
1. Custom Panels im iframe werden über einen Patch in `ha-panel-custom` gestylt. Dadurch entsteht eine gepatchte Home-Assistant-Frontend-`customPanelJS`, die im iframe zunächst die normale Home-Assistant-Frontend-`customPanelJS` und danach ein verdichtetes UIX-JavaScript-Modul ausführt.
2. Wenn UIX erkennt, dass kein Theme angewendet wurde, wird UIX Styling mit dem aktuell geladenen Home-Assistant-Frontend-Theme angewendet. Manche Custom Panels wie HACS wenden das Theme selbst an; dann erbt UIX Styling dieses Theme.
3. Home-Assistant-Custom-Panels werden mit einer Konfiguration inklusive `name:` definiert. UIX nutzt diesen Namen für die Theme-Variable, mit der iframe-Custom-Panels gestylt werden.
:::

## Beispiele

### Direkt geladene Custom Panels stylen

Nutze die direkte Custom-Theme-Variable `uix-panel-custom(-yaml)`.

Beispiel für das gezielte Styling des Browser-Mod-Panels:

```yaml
UIX Test:

  uix-theme: UIX Test

  uix-panel-custom-yaml: |
    browser-mod-browser-panel $: |
      browser-mod-browser-settings-card {
        --card-background-color: red;
        --primary-text-color: white;
        --secondary-text-color: whitesmoke;
        --ha-color-form-background: darkorange;
      }
```

Beispiel für das Styling aller direkt geladenen Custom Panels:

```yaml
UIX Test:

  uix-theme: UIX Test

  uix-panel-custom: |
    ha-panel-custom > * {
      --card-background-color: red;
      --primary-text-color: white;
      --secondary-text-color: whitesmoke;
      --ha-color-form-background: darkorange;
    }
```

Das Ergebnis ist beim Browser-Mod-Browser-Panel in beiden Beispielen gleich.

![Browser Mod browser panel styling](https://raw.githubusercontent.com/Lint-Free-Technology/uix/aae59986fc7f0475f27c7662a6a2ee7af310672b/docs/source/assets/page-assets/using/custom-panel-browser-mod.png)

::: info
Die DOM-Struktur von Custom Panels verwendet nicht immer Shadow Roots oder Home-Assistant-Elemente. Prüfe deshalb das Custom Panel mit den Browser-Entwicklertools, um sinnvolle Styling-Ziele zu finden.
:::

### Custom Panels im iframe stylen

Nutze die Theme-Variable `uix-<name>(-yaml)`, wobei `name` der Name des [Home-Assistant-Custom-Panels](https://www.home-assistant.io/integrations/panel_custom/) ist. Wenn du den Namen nicht kennst, kannst du im Browser-Inspector nachsehen, welches erste Element im DOM des iframe liegt. Das Tag dieses Elements ist der Custom-Panel-Name.

Beispiel für [HACS](https://hacs.xyz), das als iframe-Custom-Panel geladen wird:

Für HACS ist der Custom-Panel-Name `hacs-frontend`, also lautet die UIX-Styling-Theme-Variable `uix-hacs-frontend(-yaml)`.

```yaml
UIX Test:

  uix-theme: UIX Test

  uix-hacs-frontend-yaml: |
    hacs-dashboard $ hass-tabs-subpage-data-table $ hass-tabs-subpage $: |
      .toolbar {
        background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
      }
    hacs-repository-dashboard $:
      .: |
        ha-card {
          background-color: orange;
        }
      hass-subpage $: |
        .toolbar {
          background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
        }
      hass-loading-screen $: |
        .toolbar {
          background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
        }
```

![HACS panel styling](https://raw.githubusercontent.com/Lint-Free-Technology/uix/aae59986fc7f0475f27c7662a6a2ee7af310672b/docs/source/assets/page-assets/using/custom-panel-hacs.png)

::: warning Theme-Updates
Theme-Updates für das aktuell ausgewählte Theme werden angewendet, während ein Custom Panel angezeigt wird. Wenn du aber das Theme des Nutzers wechselst, der das Custom Panel gerade sieht, muss das Panel neu geladen werden.
:::
