---
title: Datenfluss – Werte, Konvertierung und Berechnung
---

# HA Grafik – Datenfluss

Ab **0.1.286** gilt die Runtime-Ausblendung bei explizitem **Z-Index −100 oder kleiner für alle Widgets**, nicht nur Linien. Ein ausgeblendetes Number-Widget kann weiterhin Werte an Math übergeben; eine ausgeblendete MathBox rechnet weiterhin. Die Regel deaktiviert keine Wertequelle. Im Editor bleibt alles bearbeitbar.

Bis Studio **0.1.285** ergänzt: SVG-Line und Wert-Verbindung unterstützen **Linie → Vertikale Startposition**. Rechtwinklige vertikale Linien laufen erst senkrecht, dann auf Zielhöhe nach links oder rechts. Punktgriffe starten nach 6 px Bewegung und verschieben keine Mehrfachauswahl. Angedockte Linien als Ganzes mit **Alt** ziehen. Eine normale SVG-Line mit **Z-Index −100 oder kleiner** bleibt ebenfalls in der Runtime unsichtbar, ohne ihre Werte zu verlieren. Sie kann **Number → Math** verbinden; Anleitung und Nullwert-Beispiel unter [LineBox Math](./svg-linebox-math).

Ab Studio **0.1.141** enthält die eigene Palette **HA Grafik – Datenfluss** drei Widgets. Alle Berechnungen und Konvertierungen laufen im Browser des jeweiligen Display-Computers. Home Assistant liefert die Entitätswerte; zusätzliche HA-Entitäten sind für die interne Verarbeitung nicht nötig. Die Visualisierung muss dafür geöffnet sein.

| Widget | Im Editor | In der Runtime |
| --- | --- | --- |
| **Wert-Verbindung** | Einfache SVG-Linie ohne Animation, mit Richtung vom Start zum Ziel | Unsichtbar; Werte werden weitergegeben |
| **Wert-Konverter** | Widget und eigener Dialog mit Radiobuttons, Eingangs-/Ausgangstyp und Vorschau | Immer unsichtbar; Konvertierung bleibt aktiv |
| **Wert-Berechnung** | Gleicher Editor wie [SVG LineBox Math](./svg-linebox-math), mit vier Rechnungen und Anschlüssen A–P | Standardmäßig unsichtbar; alle Rechnungen und Ausgänge bleiben aktiv |

Wert-Verbindung und Wert-Berechnung verwenden intern die bestehenden SVG-Line- und SVG-LineBox-Math-Typen. Dadurch bleiben Andocken, Verschieben, Kopieren, Projektimport/-export und die gemeinsame Rechenlogik erhalten. Bei SVG LineBox Math lässt sich **In Runtime ausblenden** ebenfalls einschalten. Bei Wert-Berechnung kannst du diese Option wieder ausschalten, wenn du das Rechenwidget sehen möchtest.

## Eine Quelle verbinden

![Einzelner Ausgangspunkt mit Positionsauswahl](/images/grafik-visual-studio/output-point.png)

Seit 0.1.154 bleibt CSS Allgemein auch bei diesen Widgets verpflichtend aktiv; die übrigen CSS-Bereiche sind optional.


Ab **0.1.143** sind bei neuen Datenfluss-Widgets die optionalen CSS-Bereiche standardmäßig deaktiviert, bei Wert-Berechnung zusätzlich **Darstellung**. Berechnung und Konvertierung bleiben aktiv. Die Bereiche lassen sich bei Bedarf einschalten; deaktivierte CSS-Felder werden nicht exportiert. Neue Wert-Verbindungen haben an beiden Enden keine Pfeilspitzen. Bereits gespeicherte Widgets behalten ihre Einstellungen.

1. Schalte bei einem Widget mit Entitäts- oder Vorschauwert unter **Datenfluss** **Ausgangspunkt aktivieren** ein. Wähle mit den Radiobuttons **Oben**, **Unten**, **Rechts** oder **Links** die Mitte der entsprechenden Seite; standardmäßig rechts. Dieser einzelne Ausgang funktioniert unabhängig vom Bereich **Andockpunkte** und ist abschaltbar. Unter **Einstellungen → Ausgangspunkt** stellst du seine eigene Farbe ein. Der Punkt ist nur im Editor sichtbar; die Wertweitergabe bleibt in der Runtime aktiv. Widgets ohne verfügbaren Wert, etwa reine Rahmen, liefern keinen Wert. Bestehende Andockpunkt-Konfigurationen bleiben erhalten; LineBox, LineBox Math und Konverter verwenden weiterhin ihre eigenen Anschlüsse.
2. Füge eine **Wert-Verbindung** ein: Start an den Ausgang der Quelle, Ziel an den Eingang des Konverters oder Empfängers. Der Wertfluss folgt immer dieser Richtung, auch ohne sichtbare Pfeilspitzen; Linienanimation ist ausgeschaltet.
3. Öffne am Konverter **Konvertierung bearbeiten**, wähle Ein- und Ausgang und aktiviere **Gewählte Ein-/Ausgangs-Dockpunkte aktivieren**. Neue Dockpunkte bleiben bis zur ausdrücklichen Aktivierung aus.
4. Wähle die Konvertierung und prüfe die Vorschau. Bei **Number** und **String** im Basic-Set aktiviere unter **Datenfluss** **Eingangspunkt aktivieren**. Bei anderen normalen Empfängern aktiviere **Wert vom Datenfluss übernehmen** und deren Eingangs-Dockpunkt. Number kann alternativ seine bestehende numerische Dockpunktübernahme verwenden; dort werden mehrere Zahlenwerte weiterhin summiert.

Ein Konverter und die allgemeine Datenflussübernahme erlauben **genau eine Quelle je Eingang**. Mehrere ausgehende Verbindungen dürfen dasselbe Ergebnis an unterschiedliche Empfänger verteilen. Der Konverter summiert keine Texte oder Schaltzustände. LineBox Math behält seine eigene Summierung numerischer Mehrfachbelegungen.

### Eingangspunkt bei Number und String

Ab Studio **0.1.274** bieten beide Basic-Widgets unter **Datenfluss** einen eigenen Eingangspunkt. Wie beim Ausgang wählst du **Oben**, **Unten**, **Rechts** oder **Links**; standardmäßig liegt der Eingang links. Der Eingang funktioniert unabhängig vom Bereich **Andockpunkte**. Mit seiner Aktivierung übernimmt das Widget den Wert der angeschlossenen Quelle im Editor und in der Runtime. Beim Wechsel der Seite wandern bestehende Eingangsverbindungen mit. Ein zusätzlich aktivierter Ausgang kann den übernommenen Wert weitergeben.

Nach dem Abschalten der Datenflussübernahme zeigt das Widget wieder seinen Entitäts- oder Vorschauwert. Die Datenflusspunkte sind nur im Editor sichtbar.

## Konverterdialog

![Konverterdialog mit Radiobuttons und Vorschau für Temperaturtext zu Zahl](/images/grafik-visual-studio/dataflow-converter-dialog.png)

| Konvertierung | Einstellungen und Ergebnis |
| --- | --- |
| Zahl → Text | 0–10 Nachkommastellen, Dezimalpunkt oder -komma, optionale Einheit |
| Text → Zahl | Dezimalpunkt/-komma und angehängte Einheit erkennen; Ausgabe als Zahl |
| Schaltzustand → Zahl | Ein → 1, Aus → 0; optional invertieren |
| Zahl → Schaltzustand | Ein bei Wert ≥ Schwellwert, ansonsten Aus; optional invertieren |
| Schaltzustand → Text | Eigene Texte für Ein und Aus; optional invertieren |
| Schaltzustand normalisieren | `on/off`, `true/false` oder `1/0` einlesen; Ausgabe als echte Booleans, Zahlen oder `on/off`-Text |
| Zahl skalieren | `Wert * Faktor + Offset`, optional Zieleinheit; z. B. °C → °F mit Faktor 1,8 und Offset 32 |

Groß-/Kleinschreibung und äußere Leerzeichen werden bei Schaltzuständen toleriert. Unbekannte Zustände werden gemeldet. Nur die zum gewählten Modus passenden Einstellungen werden angezeigt. Änderungen werden erst mit **Anwenden** übernommen und unterstützen Rückgängig.

## Einheiten und Fehler

`23,5 °C` wird in Zahlenwert **23,5** und Einheit **°C** getrennt. Bei einem reinen Wert wird die HA-Einheit aus `unit_of_measurement` beziehungsweise die Widget-Einheit übernommen. Fehlt beides, kannst du eine Fallback-Einheit eintragen. Eine bereits im Text vorhandene Einheit hat Vorrang und wird bei Textausgabe nicht doppelt angehängt. **Einheit im Text mit ausgeben** ist optional. Einheitenerkennung allein führt keine Umrechnung durch; dafür wählst du ausdrücklich **Zahl skalieren** mit passendem Faktor, Offset und Ziel.

Leere Werte, `unknown`, `unavailable`, ungültige Zahlen, unbekannte Schaltzustände, inaktive Eingänge, Mehrfachquellen und Rückkopplungen erzeugen einen Fehler. Standardmäßig wird dann kein Wert ausgegeben. **Ersatzwert bei Fehler aktivieren** ist zunächst aus und gibt bei Aktivierung den eingetragenen Ersatztext aus; das ist keine automatische Zahl- oder Boolean-Konvertierung.

Beispiel: Temperaturanzeige `23,5 °C` → Konverter **Text → Zahl** → Wert-Berechnung `A * 2` → Number **47,0**. In der Runtime sind nur Temperaturanzeige und Number sichtbar. Ergebnisse werden intern weitergegeben und nicht automatisch in Home Assistant gespeichert. Ein einfacher Schwellwert hat derzeit keine Hysterese; er wechselt direkt an der Grenze.
