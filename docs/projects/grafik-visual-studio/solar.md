---
title: UGSo Solar – Wechselrichter und stapelbare Akkus
description: Neutrale SVG-Module mit bündigen Gehäusekoppelpunkten, Textanzeigen und frei zugeordneten Datenflussanschlüssen.
---

# UGSo Solar

**UGSo Solar 0.1.0** benötigt **Studio 0.1.276 oder neuer**. Das eigenständige Widgetset enthält drei markenunabhängige Module mit transparenten SVG-Grafiken. Importiere die [Paketdatei ugso.solar.wg](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/refs/heads/master/ha_grafik_visual_studio/packages/solar/ugso.solar.wg) über die Paketeinstellungen.

| Widget | Standardgröße | Gehäusekoppelpunkte | Linienpunkte |
| --- | --- | --- | --- |
| Stapel-Kopfteil | 256 × 64 px | Unten mittig | Links, rechts, oben |
| Batteriemodul | 256 × 169 px | Oben und unten mittig | Links, rechts |
| Wechselrichter Solo | 144 × 103,3 px | Keine | Alle vier Seiten |

Die Kopfteilgrafik sitzt mittig auf der unteren Widgetkante. Die Batterie schließt mit der Grafik oben und unten bündig ab. Batterie und Solo behalten beim Vergrößern oder Verkleinern ihre Proportionen. Das sichtbare Solo-Gehäuse ist etwa ein Drittel schmaler als das Kopfteil.

## Einen Stapel zusammensetzen

Füge **ein Kopfteil** und je nach Anlage **1–6 Instanzen desselben Batterie-Widgets** hinzu. Jede Batterie hat eigene Einstellungen und Entitäten. Die mittigen Gehäusekoppelpunkte sind standardmäßig aktiviert, mit Abstand **0 px**. Ziehe eine Batterie mit ihrem oberen Punkt an den unteren Punkt des Kopfteils oder einer anderen Batterie. Die Teile rasten bündig und mittig ein.

Unter **Gehäuse-Snappunkte** lassen sich Snapping, einzelne Punkte, Abstand und dauerhafte Editoranzeige einstellen. Gehäusekoppelpunkte dienen nur der Platzierung; sie übertragen keine Werte. Die Punkte sind in der Runtime unsichtbar.

## Werte als Text auf dem Gehäuse

Für **Leistung**, **Temperatur** und **Ladezustand (SoC)** gibt es jeweils eine Home-Assistant-Entitätsauswahl und einen Vorschauwert. Die Einheiten sind **W**, **°C** und **%**. Leistung aus einer kW-Entität wird in W umgerechnet. Ein Vorschauwert gilt nur, solange keine Entität eingetragen ist. Fehlende oder unbekannte Zustände erscheinen als **—**.

**Wert anzeigen** schaltet ausschließlich die jeweilige Textanzeige ab. Die Entität wird weiterhin aktualisiert, und Ausgänge liefern weiterhin ihren Wert. Bei der Batterie beginnen die aktiven Anzeigen direkt unter der Trennlinie nach dem ersten Drittel und stehen automatisch untereinander, ohne Leerzeilen für ausgeblendete Werte. Es gibt keine Rahmen oder Anzeigekästchen. Die Reihenfolge ist Leistung, Temperatur, SoC. Schriftfarbe und maximale Schriftgröße sind einstellbar; bei wenig Platz wird die Schrift verkleinert.

Standardmäßig zeigt die Batterie alle drei Werte, das Kopfteil keine Werte und Solo nur die Leistung. Die drei Anzeigen lassen sich bei jedem Modul separat aktivieren.

Unter **Leistungsrichtung** kannst du ein Richtungssymbol zuschalten. Lege fest, ob positive Leistung **Energie hinein** oder **Energie heraus** bedeutet, und wähle die beiden Symbole über freie Texteingaben. Bei Leistung 0 oder einem unbekannten Wert wird kein Richtungssymbol gezeigt. Das Vorzeichen des Zahlenwerts bleibt erhalten.

## Ein- und Ausgänge für SVG-Linien

Unter **Linienanschlüsse** hat jede verfügbare Seite zwei Einstellungen:

- **Rolle:** Aus, Eingang oder Ausgang. Standardmäßig sind die Linienpunkte aus.
- **Wert:** Leistung, Temperatur oder Ladezustand (SoC).

Ein **Ausgang** gibt den ausgewählten Wert mit Einheit weiter, zum Beispiel an Number oder an eine SVG-Linie. Ein **Eingang** übernimmt diesen Wert aus genau einer angeschlossenen Quelle und ersetzt für diesen Kanal die Entität. Verwende höchstens einen Eingang pro Wert. Ein anderer Ausgang kann den übernommenen Wert weiterreichen; Rückkopplungen werden abgefangen. Es werden keine Home-Assistant-Entitäten beschrieben.

Die Linienpunkte sind unabhängig von den Gehäusekoppelpunkten. Aktive Ausgänge nutzen die Ausgangspunktfarbe aus den Studio-Einstellungen. In der Runtime verschwinden die Punkte; normale SVG-Linien bleiben sichtbar, Wert-Verbindungen bleiben unsichtbar.

Alle Standard-CSS-Gruppen sind verfügbar; die optionalen Bereiche sind zunächst ausgeschaltet. Eigene Innenabstände und Rahmen können die bündige Darstellung verändern.

Die SVGs sind eigene UGSo-Grafiken ohne Herstellerlogo. [Quellcode, Bauanleitung und MIT-Lizenz](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/solar).
