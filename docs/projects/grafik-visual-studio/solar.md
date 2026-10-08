---
title: UGSo Solar – Wechselrichter und stapelbare Akkus
description: Neutrale SVG-Module mit bündigen Gehäusekoppelpunkten, Textanzeigen und frei zugeordneten Datenflussanschlüssen.
---

# UGSo Solar

**UGSo Solar 0.1.2** benötigt **Studio 0.1.279 oder neuer**. Das eigenständige Widgetset enthält vier markenunabhängige Module mit transparenten SVG-Grafiken. Aktualisiere zuerst Studio und importiere danach die [Paketdatei ugso.solar.wg](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/refs/heads/master/ha_grafik_visual_studio/packages/solar/ugso.solar.wg) über die Paketeinstellungen.

| Widget | Standardgröße | Gehäusekoppelpunkte | Linienpunkte |
| --- | --- | --- | --- |
| Stapel-Kopfteil | 256 × 64 px | Unten mittig | Links/rechts sowie je zwei Solarpanel-Eingänge an beiden Gehäuseseiten |
| Batteriemodul | 256 × 169 px | Oben und unten mittig | Links, rechts |
| Wechselrichter Solo | 144 × 103,3 px | Keine | Alle vier Seiten |
| Solarpanel mit Standfuß | 320 × 288 px | Keine | Ein Ausgang: Standrohr oder Widgetkante links/rechts |

Die Kopfteilgrafik sitzt mittig auf der unteren Widgetkante. Die Batterie schließt mit der Grafik oben und unten bündig ab. Batterie und Solo behalten beim Vergrößern oder Verkleinern ihre Proportionen. Das sichtbare Solo-Gehäuse ist etwa ein Drittel schmaler als das Kopfteil.

## Solarpanel mit Standrohr und Fuß

Unter **Solar-Modul → Ausrichtung** wählst du **Wie Vorlage** oder **Gespiegelt**. Die SVG-Grafik wird horizontal gespiegelt; Schrift und Wertanzeige bleiben lesbar. Beim Skalieren bleiben die Proportionen erhalten.

Wähle unter **Leistung → Eingangsentität (Leistung)** eine Home-Assistant-Entität. Werte in kW werden in W umgerechnet. **Wert anzeigen** blendet nur den rahmenlosen Text aus; der Ausgang liefert weiter Daten. Ohne Entität gilt der Vorschauwert, bei unbekannter Entität erscheint ein Strich.

Unter **Linienanschluss → Position des Ausgangspunkts** stehen drei Positionen zur Wahl: **Am Standrohr über dem Fuß**, **Widgetkante links** und **Widgetkante rechts**. Die Kantenpositionen liegen auf gleicher Höhe wie der Punkt am Rohr. Es bleibt genau ein Ausgang; bereits angeschlossene SVG-Linien folgen beim Umstellen automatisch. **Ausgangspunkt aktiv** schaltet ihn ab oder an. In der Runtime ist der Punkt unsichtbar, die SVG-Linie bleibt sichtbar. Das Solarpanel hat keine Gehäusekoppelpunkte.

## Einen Stapel zusammensetzen

Füge **ein Kopfteil** und je nach Anlage **1–6 Instanzen desselben Batterie-Widgets** hinzu. Jede Batterie hat eigene Einstellungen und Entitäten. Die mittigen Gehäusekoppelpunkte sind standardmäßig aktiviert, mit Abstand **0 px**. Ziehe eine Batterie mit ihrem oberen Punkt an den unteren Punkt des Kopfteils oder einer anderen Batterie. Die Teile rasten bündig und mittig ein.

Unter **Gehäuse-Snappunkte** lassen sich Snapping, einzelne Punkte, Abstand und dauerhafte Editoranzeige einstellen. Gehäusekoppelpunkte dienen nur der Platzierung; sie übertragen keine Werte. Die Punkte sind in der Runtime unsichtbar.

## Werte als Text auf dem Gehäuse

Für **Leistung**, **Temperatur** und **Ladezustand (SoC)** gibt es jeweils eine Home-Assistant-Entitätsauswahl und einen Vorschauwert. Die Einheiten sind **W**, **°C** und **%**. Leistung aus einer kW-Entität wird in W umgerechnet. Ein Vorschauwert gilt nur, solange keine Entität eingetragen ist. Fehlende oder unbekannte Zustände erscheinen als **—**.

**Wert anzeigen** schaltet ausschließlich die jeweilige Textanzeige ab. Die Entität wird weiterhin aktualisiert, und Ausgänge liefern weiterhin ihren Wert. Bei der Batterie beginnen die aktiven Anzeigen direkt unter der Trennlinie nach dem ersten Drittel und stehen automatisch untereinander, ohne Leerzeilen für ausgeblendete Werte. Es gibt keine Rahmen oder Anzeigekästchen. Die Reihenfolge ist Leistung, Temperatur, SoC. Schriftfarbe und maximale Schriftgröße sind einstellbar; bei wenig Platz wird die Schrift verkleinert.

Standardmäßig zeigt die Batterie alle drei Werte und Solo nur die Leistung. Das Kopfteil zeigt keine Werte und bietet keine Gruppen für Leistung, Temperatur, SoC oder Leistungsrichtung. Beim Solo-Wechselrichter bleiben diese Einstellungen erhalten.

Bei der Batterie lässt sich unter **Leistung**, **Temperatur** und **Ladezustand (SoC)** jeweils die **Schriftfarbe des Werts** getrennt einstellen. Ohne eigene Farbe gilt die allgemeine Schriftfarbe. Die Farbe bleibt auch beim Aus- und Wiedereinblenden der Anzeige erhalten.

Unter **Leistungsrichtung** kannst du ein Richtungssymbol zuschalten. Lege fest, ob positive Leistung **Energie hinein** oder **Energie heraus** bedeutet, und wähle die beiden Symbole über freie Texteingaben. Bei Leistung 0 oder einem unbekannten Wert wird kein Richtungssymbol gezeigt. Das Vorzeichen des Zahlenwerts bleibt erhalten.

## Ein- und Ausgänge für SVG-Linien

Bei der Batterie gibt es links und rechts zusätzlich eine **Position**: **Widgetkante Mitte** oder **Gehäusekante an unterer Naht**. Beide Seiten lassen sich unabhängig umstellen. Vorhandene Verbindungen folgen automatisch; Ein-/Ausgangsrolle und Wertzuordnung bleiben erhalten. Die mittigen Gehäusekoppelpunkte oben/unten für das Stapeln ändern sich dadurch nicht.

Das Kopfteil besitzt vier optische Solarpanel-Anschlussbuchsen: links oben/unten und rechts oben/unten. Diese vier Eingänge sind standardmäßig aktiv und unter **Linienanschlüsse** einzeln abschaltbar. Sie folgen der unten bündigen Grafik auch bei anderer Widgethöhe. Verbinde die SVG-Linie eines Solarpanels mit einer solchen Buchse. Die Eingänge sind getrennte Linienziele; Werte werden nicht automatisch summiert. Der frühere obere Linienanschluss entfällt; die bisherigen linken/rechten Linienpunkte bleiben verfügbar.

Unter **Linienanschlüsse** hat jede verfügbare Seite zwei Einstellungen:

- **Rolle:** Aus, Eingang oder Ausgang. Standardmäßig sind die Linienpunkte aus.
- **Wert:** Leistung, Temperatur oder Ladezustand (SoC).

Ein **Ausgang** gibt den ausgewählten Wert mit Einheit weiter, zum Beispiel an Number oder an eine SVG-Linie. Ein **Eingang** übernimmt diesen Wert aus genau einer angeschlossenen Quelle und ersetzt für diesen Kanal die Entität. Verwende höchstens einen Eingang pro Wert. Ein anderer Ausgang kann den übernommenen Wert weiterreichen; Rückkopplungen werden abgefangen. Es werden keine Home-Assistant-Entitäten beschrieben.

Die Linienpunkte sind unabhängig von den Gehäusekoppelpunkten. Aktive Ausgänge nutzen die Ausgangspunktfarbe aus den Studio-Einstellungen. In der Runtime verschwinden die Punkte; normale SVG-Linien bleiben sichtbar, Wert-Verbindungen bleiben unsichtbar.

Alle Standard-CSS-Gruppen sind verfügbar; die optionalen Bereiche sind zunächst ausgeschaltet. Eigene Innenabstände und Rahmen können die bündige Darstellung verändern.

Die SVGs sind eigene UGSo-Grafiken ohne Herstellerlogo. [Quellcode, Bauanleitung und MIT-Lizenz](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/solar).
