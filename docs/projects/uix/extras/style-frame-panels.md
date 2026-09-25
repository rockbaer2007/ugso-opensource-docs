---
title: Frame-Panels stylen (experimentell)
description: UIX-Styling innerhalb unterstützter App- und Custom-Panel-Frames aktivieren.
---
# Frame-Panels stylen (experimentell)

Standardmäßig fügt UIX keine Styles in Frame-Inhalte ein. Aktiviere diese experimentelle Einstellung, damit die interne UIX-Laufzeit in unterstützten gleichursprünglichen App- und Custom-Panel-Frames ausgeführt wird. Das Styling des Host-Elements mit `uix-app` und `uix-panel-custom` ist von dieser Option nicht betroffen.

::: warning Kompatibilität mit Frameworks
Die Frame-Laufzeit wurde ausführlich mit dem Lit-basierten Frontend von Home Assistant getestet. Apps und Custom Panels, die in iframes mit anderen Frameworks laufen, können ein anderes Lebenszyklus- oder Shadow-DOM-Verhalten haben. Panels mit einem üblichen Light-DOM-Root und ohne Shadow-DOM-Grenzen funktionieren in der Regel gut. Panels, die ihr DOM reaktiv verwalten oder komplexes Shadow DOM verwenden, müssen für die jeweilige App geprüft werden. Untersuche den Frame, teste jeden Selektor und melde Kompatibilitätsprobleme.

Bei Frames ohne Lit verwendet UIX ein Fallback-Stylesheet, statt einen `uix-node` in das App-DOM einzufügen. Dieses Fallback unterstützt direktes CSS einschließlich Templates, aber keine UIX-YAML-Selektorpfade. Verwende im direkten Style-Block normale CSS-Selektoren.
:::

## Einstellung über die Integrationsoberfläche

Die Option ist standardmäßig **nicht gesetzt**. So aktivierst du sie:

1. Öffne in Home Assistant **Einstellungen → Geräte & Dienste → UI eXtension → Konfigurieren**.
2. Wähle im Menü **Experimentelle Einstellungen**.
3. Aktiviere **Frame-Panels stylen**.
4. Speichere die Einstellung.

Die Einstellung gilt sofort für alle verbundenen Browsersitzungen. Damit sie auf ein gerade angezeigtes Frame-Panel angewendet wird, kann ein Neuladen der Seite erforderlich sein.

## Verhalten bei aktivierter Option

Wenn die Option aktiviert ist:

- Installiert UIX seine interne, vom Paneltyp unabhängige Laufzeit in unterstützten gleichursprünglichen App- und Custom-Panel-Frames.
- Bei Custom-Panel-Frames verwendet UIX den Namen des Panels als Theme-Ziel. Bei App-Frames wird zuerst der vollständige Add-on-Slug und danach der vom Repository unabhängige Slug geprüft.
- UIX fügt einen Styling-Knoten nur ein, wenn das aktive Theme ein passendes Ziel `uix-<target>` definiert. Frames ohne passenden Abschnitt `uix-<target>` bleiben unverändert.
- Wenn UIX erkennt, dass kein Theme angewendet wurde, wird UIX Styling mit dem aktuell geladenen Home-Assistant-Frontend-Theme ausgeführt. Einige Custom Panels wie HACS wenden das Theme selbst an; in diesem Fall übernimmt UIX Styling dieses Theme.

::: tip
Das Ziel für `uix-<target>` findest du am einfachsten in der Browser-Entwicklerkonsole. Die von `uixFrame.js` ausgegebene UIX-Ladeinformation sieht beispielsweise so aus:

<span style="background:#CE3226;color:white;padding:2px 5px;font-weight:bold;border-radius:5px;">💡 UIX 8.4.0 IS INSTALLED 💡 for hacs-frontend</span>

Der letzte Teil der Meldung ist das Ziel, hier also `hacs-frontend`.
:::
