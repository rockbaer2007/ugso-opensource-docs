---
title: SVG-Line – Verbindungslinien zeichnen und animieren
---

# SVG-Line

**SVG-Line** findest du unter **HA Grafik – Spezial**. Das Widget verbindet andere Widgets optisch, führt Linien über Ecken und kann einen Wertefluss animieren. Eine Linie kann an Widget-Andockpunkten, an einem ausdrücklich aktivierten Sammelpunkt einer anderen SVG-Line oder an freien Koordinaten beginnen und enden. Sie ist selbst keine Home-Assistant-Entität; eine optionale Entität steuert ihre Animation.

## Verbindung und Andockpunkte

1. Füge SVG-Line ein. Wähle sie im Editor aus; Anfang und Ende erscheinen als ziehbare Kreise.
2. Aktiviere beim Zielwidget **Andockpunkte** und die gewünschten Positionen. Die zwölf Punkte sind bei neuen Widgets zunächst aus: links/rechts jeweils oben, Mitte und unten; oben/unten jeweils bei 1/4, Mitte und 3/4. **Alle Punkte** schaltet sie gemeinsam um. Mehrere Linien dürfen denselben Punkt belegen.
3. Ziehe einen Linienendpunkt auf einen aktiven Andockpunkt. Alternativ stelle unter **Start** und **Ziel** jeweils Widget und Andockpunkt ein. **Oder aktiver Sammelpunkt** wählt einen Sammelpunkt einer anderen SVG-Line; **Freies X/Y** positioniert ein ungebundenes Ende.

| Bearbeitung | Wirkung |
| --- | --- |
| Freien Endpunkt ziehen | Ändert Anfang oder Ende der Linie. Mit den Pfeiltasten verschiebst du einen fokussierten Punkt um 1 Pixel, mit `Umschalt` um 10 Pixel. |
| Angedockten Endpunkt mit `Strg` ziehen | Löst die Verbindung und verschiebt den Punkt. `Strg` plus Pfeiltaste funktioniert ebenfalls. |
| Zwischenpunkt ziehen | Ändert den Verlauf des manuellen Mehrpunktpfads. |
| Linie mit gedrückter Maustaste ziehen | Verschiebt die ganze Linie und löst dabei bisherige Start-/Ziel-Andockungen. |
| Linie ohne Ziehen anklicken | Öffnet die Wahl **Zwischenpunkt** oder **Sammelpunkt**; nach **OK** wird der Punkt eingefügt. |

## Pfad und Sammelpunkte

Unter **Pfad und Sammelpunkte** gibt es vier **Pfadarten**: **Gerade**, **Automatisch rechtwinklig**, **Kurve** und **Manueller Zickzack-/Mehrpunktpfad**. Der **Eckenradius** rundet Ecken im passenden Verlauf ab. Über **Zwischenpunkte und Sammelpunkte** kannst du Punkte benennen, setzen und bearbeiten. Ein per Klick eingefügter Punkt wechselt die Linie in den manuellen Mehrpunktmodus.

Ein **Zwischenpunkt** knickt nur den Pfad. Ein **Sammelpunkt** ist ein möglicher Anschluss für weitere SVG-Lines, wenn er aktiviert ist. Ziehe deren freien Endpunkt auf den sichtbaren Sammelpunkt oder wähle ihn in den Eigenschaften. Mehrere Linien können denselben Sammelpunkt nutzen. Eine bloße Kreuzung oder Berührung koppelt keine Linien. Ein deaktivierter Sammelpunkt nimmt keine neue Verbindung an.

## Linie und Pfeilspitzen

| Gruppe | Einstellmöglichkeiten |
| --- | --- |
| **Linie** | **Grundfarbe**, **Animationsfarbe**, **Dicke** (1–40 px), **Deckkraft**, **Linienart** (durchgezogen, gestrichelt, gepunktet), **Strichlänge**, **Abstand** zwischen Strichen/Punkten und **Linienenden** (rund, stumpf, quadratisch). |
| **Pfeilspitzen** | **Am Anfang** und **Am Ende** unabhängig: keine, gefüllter Pfeil, offener Pfeil oder Kreis. **Größe** und **Farbe** gelten für die Marker. Bei umgekehrter Flussrichtung wechseln die angezeigten Marker ihre Seite. |

## Animation und Richtungsquelle

Aktiviere **Animation aktivieren** und wähle als **Animationsart** Zweifarbenfluss, laufende Striche, Puls oder Lichtpunkt. Unter **Richtungsquelle** ist immer genau eine Variante aktiv:

| Quelle | Richtung und Geschwindigkeit |
| --- | --- |
| **Manuell** | **Richtung** Anfang → Ende oder Ende → Anfang sowie **Dauer** von 0,2–20 Sekunden je Zyklus. Bei Verbindung mit einem Sammelpunkt richtet sich der manuelle Fluss auf diesen Punkt aus. |
| **Zahlen-Entität** | Positive Werte laufen vom Anfang zum Ende, negative umgekehrt; `0` stoppt den Fluss. Betrag ÷ **Teiler** (Standard `1`) ergibt Zyklen pro Sekunde, begrenzt auf 0,05–20. Beispiel: `1000 W ÷ 100 = 10` Zyklen/s. |
| **Bool-Entität** | `on`/`true`/`1` läuft vorwärts, `off`/`false`/`0` rückwärts. **Bool-Richtung umkehren** tauscht die Zuordnung. Die eingestellte **Dauer** bestimmt den Takt. |

Fehlende oder ungültige Entitätszustände halten die Animation an. Die ausgewählte Entität wird im Editor und in der Runtime aktualisiert. Die **SVG LineBox** kann an einem als Ausgang eingerichteten Andockpunkt Vorzeichen und Betrag ihres berechneten Wertes an die Linie übergeben. Diese Übergabe hat Vorrang vor der gewählten Richtungsquelle. Die Ausgangslinie braucht weiterhin **Animation aktivieren**; bei `0` oder ohne gültigen Eingang steht sie still. **SVG LineBox-Teiler (bei Übergabe)** bestimmt dann ihren Takt, während ihre eigenen Farben und Linienart erhalten bleiben. [SVG LineBox ausführlich erklärt](./svg-linebox).

## Hauptlinie, Kreuzungen und Ebenen

Mit **Hauptlinie / Flussgruppe** ordnest du eine Linie einer anderen zu. **Animationstakt der Hauptlinie übernehmen (eigene Farben behalten)** übernimmt Takt und Animationsart, während die Nebenlinie bei laufendem Fluss ihre eigene Farbe behält. **Synchronisierung** bietet **Gleicher Takt** und **Am Sammelpunkt synchron ankommen**. Bei direkter Kopplung an einen Sammelpunkt einer nicht animierten Hauptlinie stoppt die Nebenlinie ebenfalls und zeigt deren Grundfarbe einschließlich der Pfeilspitzen. Nach dem Lösen gelten wieder die gespeicherten eigenen Einstellungen.

Unter **Kreuzung und z-index** stehen **Überlagerung**, **Lücke** und **Brücke / Bogen** sowie **Automatisch**, **Darüber**, **Darunter** oder **Manuell** für die Stapelung zur Verfügung. Ein höherer z-index liegt sichtbar vor einem niedrigeren. **Klicks durchlassen** beeinflusst die Interaktion in der Runtime. Kreuzungsdarstellung und z-index verbinden Linien nicht; dazu brauchst du einen Sammelpunkt oder die [SVG LineBox](./svg-linebox).

SVG-Line ist noch experimentell; insbesondere Kreuzungseffekte und synchronisierte Animation können sich je nach Pfad und Browser unterscheiden.
