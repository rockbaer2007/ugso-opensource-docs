---
title: SVG LineBox – Linienwerte sammeln und weitergeben
---

# SVG LineBox

Die **SVG LineBox** unter **HA Grafik – Spezial** sammelt Zahlenwerte verbundener SVG-Lines, bildet eine vorzeichenbehaftete Summe und kann sie an Ausgangslinien sowie optional an einen Home-Assistant-Zahlenhelfer weitergeben. Im Editor ist der Kasten sichtbar. In der Runtime verschwindet er; aktive Leitungen treffen sich optisch in seiner Mitte.

## Im Editor einrichten

1. Füge eine **SVG LineBox** und die benötigten **SVG-Lines** ein.
2. Aktiviere bei der LineBox **Andockpunkte** und nur die benötigten Positionen. Anfangs sind alle zwölf aus. **Alle Punkte** schaltet sie gemeinsam ein oder aus; jede Position kann auch einzeln gewählt werden.
3. Unter **Anschlüsse** erscheint für jeden aktiven Punkt die Rolle **Eingang**, **Nullstellung** oder **Ausgang**. **Nullstellung** ist der Standard und nimmt nicht an der Berechnung teil. Für deaktivierte Punkte gibt es keine Rollenwahl.
4. Verbinde die Eingangsleitungen mit Eingängen und eine weitere SVG-Line mit einem Ausgang. Ab Studio 0.1.126 kann eine Leitung den Wert eines am anderen Ende verbundenen numerischen Widgets übernehmen, etwa Number. Alternativ wählst du unter **Animation → Richtungsquelle** eine **Zahlen-Entität**; diese eigene Linienquelle hat Vorrang.
5. Aktiviere am Ausgang **Berechneten Wert weitergeben** und an der Ausgangslinie **Animation aktivieren**. Erst dann steuert die Summe deren Richtung und Geschwindigkeit.

Die Andockpunkte haben dieselben zwölf Positionen wie bei anderen Widgets: links/rechts je oben, Mitte, unten; oben/unten je bei 1/4, Mitte und 3/4. Du kannst mehrere Linien an einem Punkt anschließen. **Eingang** und **Ausgang** bestimmen die Funktion, nicht allein die optische Richtung der Linie.

<video controls playsinline preload="metadata" style="width: 100%; max-width: 960px" aria-label="SVG LineBox im Editor bearbeiten">
  <source src="/videos/grafik-visual-studio/linebox_edit.mp4" type="video/mp4">
  <a href="/videos/grafik-visual-studio/linebox_edit.mp4">Editor-Video öffnen</a>
</video>

[Editor-Video direkt öffnen](/videos/grafik-visual-studio/linebox_edit.mp4)

## Wie die Summe entsteht

Die LineBox berücksichtigt sichtbare SVG-Lines an **Eingängen** mit einem gültigen Zahlenwert. Eine explizite Zahlen-Entität der Linie hat Vorrang; ohne sie wird der Wert vom verbundenen numerischen Widget oder einem freigegebenen LineBox-Ausgang übernommen. Bei Number wird der Multiplikator berücksichtigt, ohne die Anzeige zu runden. Die Animation einer manuellen Eingangsleitung bleibt unabhängig von der Wertübernahme. Für eigene Linienwerte gilt: Endet die Leitung an der LineBox, geht ihr Wert mit seinem Vorzeichen in die Summe ein; beginnt sie dort, zählt er mit umgekehrtem Vorzeichen. Automatisch übernommene Widget-Werte werden entsprechend der Leitungsorientierung umgerechnet. Jede Leitung wird höchstens einmal gezählt. Fehlende oder ungültige Zustände werden ausgelassen; ohne gültigen Eingang gibt es keinen berechneten Wert. Null ist gültig. Interne Rückkopplungsschleifen werden abgebrochen.

**Beispiel ohne zusätzliche Helfer:** Number mit 125 und Number mit 79 über zwei Leitungen an Eingänge anschließen: Die LineBox zeigt **204**. Verbinde den freigegebenen Ausgang mit einem weiteren Number, Red Number, Gauge oder Bar. Dort unter **Wertquelle → Wert vom Dockpunkt** den **Eingangs-Dockpunkt** wählen und unter **Andockpunkte** aktivieren. Die Anzeige übernimmt den Wert direkt; mehrere gültige Linien an diesem Punkt werden vorzeichenbehaftet summiert. Ohne gültigen Wert erscheint `--`. Die übrigen Quellen sind **Home-Assistant-Entität / Vorschau** (bisheriges Verhalten) und **Vorschauwert** (ignoriert eine eingetragene Entität).

Beispiel: Zwei Eingangsleitungen enden an der LineBox mit `1000` und `-300`. Die Summe ist `700`. Bei einer dritten Leitung, die an einem **Ausgang** beginnt und dort **Berechneten Wert weitergeben** aktiviert hat, bedeutet `700` Fluss vom Anfang zum Ende. Endet die Ausgangsleitung an der Box, wird das Vorzeichen für ihre Orientierung umgekehrt. Ihre Farben, Pfeilspitzen und Linienart bleiben ihre eigenen. Ist ihre Animation ausgeschaltet, bleibt sie auch bei einem übergebenen Wert stehen; `0` oder kein gültiger Eingang stoppt sie ebenfalls. Mit **SVG LineBox-Teiler (bei Übergabe)** an der Ausgangslinie ergibt `700 ÷ 100 = 7` Zyklen/s. Die allgemeine Grenze der Zahlenanimation liegt bei 0,05–20 Zyklen/s.

Bei **Nullstellung** nimmt ein Punkt weder an Summe noch Ausgabe teil. Schalte **Berechneten Wert weitergeben** an einem Ausgang aus, wenn die angeschlossene SVG-Line wieder allein durch ihre eigenen Animationseinstellungen gesteuert werden soll. Eine bloße Linienkreuzung koppelt nichts.

## Verbindungspunkt und Runtime

Aktive Leitungen werden in der Runtime zur Mitte der unsichtbaren Box geführt. Die Gruppe **Verbindungspunkt** steuert die Darstellung:

| Eigenschaft | Wirkung |
| --- | --- |
| **Kreis anzeigen** | Blendet den Kreis über den Leitungsenden ein oder aus. Standard: ein. Er erscheint bei mindestens zwei sichtbaren angeschlossenen Leitungen. |
| **Durchmesser (px)** | Gewünschter Kreisdurchmesser von 4–100 px; bei dicken Leitungen wächst er bei Bedarf, damit die Enden verdeckt bleiben. |
| **Füllfarbe**, **Randfarbe**, **Randbreite (px)** | Farben und Randstärke des Kreises; die Randbreite lässt sich von 0–20 px einstellen. |
| **Ausgabewert anzeigen** | **Aus** (Standard), **Über dem Kreis** oder **Unter dem Kreis**. Zeigt die signierte Eingangssumme; ohne gültigen Eingang erscheint ein Gedankenstrich. Die Anzeige kann auch bei ausgeblendetem Kreis genutzt werden. |

Der angezeigte Wert aktualisiert sich in der Runtime auch während einer Sliderbewegung. Der Kreis liegt optisch über den verbundenen Leitungen und verdeckt ihre kantigen Enden.

<video controls playsinline preload="metadata" style="width: 100%; max-width: 960px" aria-label="SVG LineBox in der Runtime">
  <source src="/videos/grafik-visual-studio/linebox_runtime.mp4" type="video/mp4">
  <a href="/videos/grafik-visual-studio/linebox_runtime.mp4">Runtime-Video öffnen</a>
</video>

[Runtime-Video direkt öffnen](/videos/grafik-visual-studio/linebox_runtime.mp4)

## Optionaler Home-Assistant-Zahlenhelfer

Die Übergabe an Ausgangslinien funktioniert intern und benötigt keinen Helfer. Wenn du die Summe auch in Home Assistant weiterverarbeiten möchtest, aktiviere unter **Zahlenhelfer-Ausgabe** **Zusätzlich an Zahlenhelfer schreiben** und wähle einen vorhandenen `input_number.*`-Helfer. In der Runtime schreibt die App nur bei geändertem Wert; kurze Änderungen werden zusammengefasst. Der erlaubte Wertebereich des Helfers muss die mögliche Summe umfassen. Ist derselbe Helfer zugleich Zahlenquelle einer Eingangsleitung dieser LineBox, wird die Ausgabe zur Vermeidung einer direkten Rückkopplung verweigert. Ohne gültigen Eingang erfolgt kein Schreibvorgang.

Die erste Version liest Zahlen-Entitäten über die Eingangsleitungen. Eine eigene Entitätssteuerung pro Anschluss ist noch nicht vorhanden. Der frühere Palettenname **Linebox** bleibt als Suchbegriff erhalten; gespeicherte Projekte behalten den technischen Typ `linebox` und bestehende eigene Widget-Namen.

Weitere Einstellungen zu Verlauf, Farben, Pfeilen und Animation findest du bei [SVG-Line](./svg-line).
