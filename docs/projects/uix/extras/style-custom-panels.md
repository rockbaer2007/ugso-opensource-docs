---
title: Style custom panels loaded as iframe
description: Experimentelle Option für Styling von iframe-Custom-Panels.
---
# Custom Panels im iframe stylen

::: info Verfügbar ab UIX 8.2.0-beta.1
Diese Option ist experimentell.
:::

Standardmäßig stylt UIX keine Custom Panels, die als iframe geladen werden. Mit dieser experimentellen Einstellung kann Styling für solche Custom Panels aktiviert werden. Weitere Informationen und Beispiele stehen unter [Custom Panels stylen](../using/custom-panels).

## Einstellung über die Integrations-UI

Die Option ist standardmäßig **nicht gesetzt**.

1. In Home Assistant zu **Settings -> Devices & Services -> UI eXtension -> Configure** gehen.
2. **Experimental settings** im Menü wählen.
3. **Style custom panels loaded as iFrame** aktivieren.
4. Speichern.

Die Einstellung ist sofort für alle verbundenen Browser-Sessions verfügbar. Ein Neuladen der Seite kann nötig sein, wenn gerade ein Custom Panel angezeigt wird.

## Verhalten bei aktivierter Option

- Custom Panels werden über einen Patch in `ha-panel-custom` gestylt. Dadurch entsteht eine gepatchte Home-Assistant-Frontend-`customPanelJS`, die im iframe zuerst die normale Home-Assistant-Frontend-`customPanelJS` und danach ein verdichtetes UIX-JavaScript-Modul ausführt.
- UIX Styling wird auf das Haupt-Element des Custom Panels angewendet.
- Wenn UIX erkennt, dass kein Theme angewendet wurde, nutzt UIX Styling das aktuell geladene Home-Assistant-Frontend-Theme. Manche Custom Panels wie HACS wenden das Theme selbst an; in diesem Fall erbt UIX Styling dieses Theme.
