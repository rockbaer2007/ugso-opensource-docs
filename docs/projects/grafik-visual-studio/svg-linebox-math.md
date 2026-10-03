---
title: SVG LineBox Math
---

# SVG LineBox Math

Ab Studio **0.1.138** enthält der vergrößerte Dialog **vier getrennte Rechnungen**. Jede hat eine eigene Aktivierung, Formel beziehungsweise Durchschnittsberechnung, Ausgangsliste und Ergebnisvorschau. Rechnung 1 übernimmt bei älteren Projekten die bisherige Berechnung und ihre Ausgänge; Rechnungen 2–4 sowie alle internen Eingangsübergaben sind zunächst aus.

## Vier Rechnungen und Ausgangszuordnung

![Erweiterter SVG-LineBox-Math-Dialog mit separaten Rechnungen und interner Übergabe an Eingang C](/images/grafik-visual-studio/linebox-math-four-dialog.png)

Der aktuelle Screenshot zeigt die getrennten Rechnungen und die aktivierte interne Übergabe an C. So kann Rechnung 2 das Ergebnis von Rechnung 1 direkt weiterverarbeiten.

## Berechnung auf dem Display-Computer

Die Berechnungen laufen im Browser des jeweiligen Display-Computers. Home Assistant liefert die Entitätswerte; SVG LineBox Math berechnet daraus die Ergebnisse und gibt sie innerhalb der Visualisierung an andere Widgets weiter. Auch verkettete Rechnungen mit mehreren Ein- und Ausgängen benötigen dafür weder zusätzliche HA-Entitäten noch HA-Automationen.

Damit übernimmt der Display-Computer die Rechenarbeit und die Darstellung. Jedes geöffnete Display berechnet seine eigene Visualisierung. Home Assistant bleibt für die Verbindung und den Austausch der Entitätswerte zuständig; diese Kommunikation verursacht weiterhin Last. Die lokalen Math-Ergebnisse werden durch die interne Dockpunktübergabe nicht automatisch in Home Assistant gespeichert.

Berechnungen stehen nur zur Verfügung, solange die Visualisierung geöffnet ist und ihr Browser ausgeführt wird. Für Abläufe, die auch bei ausgeschaltetem Display zuverlässig weiterlaufen sollen, bleibt eine serverseitige Berechnung oder HA-Automation erforderlich.

## Ausgänge konfigurieren

Stelle zuerst oben die Rollen der Anschlüsse ein. Trage dann je aktivierter Rechnung unter **Ausgänge (z. B. E,F;H)** die gewünschten Buchstaben ein. Komma, Semikolon und Leerzeichen sind als Trennzeichen erlaubt; Kleinbuchstaben werden ebenfalls erkannt. `E,F;H` ordnet dasselbe Ergebnis den drei Ausgängen E, F und H zu. Jeder dieser Punkte muss ein aktiver **Ausgang** sein. Ist ein Buchstabe als Eingang eingerichtet, erscheint ein Hinweis; eine widersprüchliche Zuordnung lässt sich nicht übernehmen. Ein Ausgang darf nur einer Rechnung zugeordnet sein. Ein Ausgang ohne Zuordnung liefert keinen Wert.

## Ergebnisse intern weiterverarbeiten

Jede Rechnung hat die zunächst ausgeschaltete Option **Ergebnis intern an Eingang übergeben**. Erst nach dem Einschalten kannst du unter **Interner Eingang** einen einzelnen aktiven Eingangs-Buchstaben wählen. Andere Rechnungen dürfen diesen Buchstaben anschließend in ihren Formeln verwenden. Die interne Übergabe ersetzt an diesem Punkt die externen Leitungswerte; nach dem Ausschalten gelten wieder die angeschlossenen Leitungen. Pro Eingang ist nur ein internes Ergebnis erlaubt. Die Reihenfolge der Rechnungsnummern spielt für die Auflösung von Abhängigkeiten keine Rolle.

Beispiel mit A = 150 und B = 30:

| Rechnung | Formel | Ausgänge | Interne Übergabe | Ergebnis |
| --- | --- | --- | --- | --- |
| 1 | `A + B` | `E,F;H` | eingeschaltet → Eingang C | 180 |
| 2 | `C * 2` | `G` | aus | 360 |
| 3 | `A - B` | `I` | aus | 120 |
| 4 | deaktiviert | — | aus | — |

Eine Rechnung darf ihr Ergebnis nicht an einen Eingang zurückführen, von dem sie selbst abhängt. Direkte und indirekte Rückkopplungen sowie doppelte Zuordnungen werden gemeldet und vor dem Übernehmen zurückgewiesen. Bei **Durchschnitt aller belegten Eingänge** zählen auch aktiv zugewiesene interne Eingänge mit; eine Übergabe dieser Durchschnittsrechnung an ihren eigenen Eingangsbereich wäre daher eine Rückkopplung.

Ein Rechenfehler wie Division durch null stoppt die betreffende Rechnung und ihre abhängigen Rechnungen. Unabhängige Rechnungen arbeiten weiter. Fehlende Werte sind nur dann relevant, wenn die Rechnung diesen Eingang verwendet; eine Durchschnittsrechnung benötigt gültige Werte an allen belegten Eingängen. Der Dialog zeigt Hinweise pro Rechnung. Bei kleinen Bildschirmen wird der Inhalt scrollbar und die Rechnungsbereiche stehen untereinander.

## Grundlagen und Beispiel einer Einzelrechnung

Das folgende Bild zeigt den ursprünglichen Dialog aus Studio 0.1.137. Die Berechnung funktioniert weiterhin als Rechnung 1 im erweiterten Dialog.

![SVG LineBox Math: Berechnungsdialog mit Anschlüssen A–P, Eingangswerten und Durchschnitt 90](/images/grafik-visual-studio/linebox-math-dialog.png)

Das Bild zeigt den Berechnungsdialog mit **Durchschnitt aller belegten Eingänge**. Eingang **A** enthält bereits die Summe seiner beiden Leitungen (100 + 50 = **150**), Eingang **B** liefert **30**. Daher lautet das Ergebnis **90**. **G** ist als Ausgang eingerichtet und gibt dieses Ergebnis weiter. Die grünen Buchstaben A, B und G kennzeichnen angeschlossene Punkte; die orangefarbenen Buchstaben sind ohne Leitung. Ein unverbundener Eingang mit `—` zählt beim Durchschnitt nicht mit. Bei dieser Berechnungsart ist das Formelfeld deaktiviert, seine bisherige Formel bleibt jedoch erhalten.

Ab Studio 0.1.137 steht **SVG LineBox Math** ebenfalls unter **HA Grafik – Spezial**. Es bleibt als Quadrat im Editor und in der Runtime sichtbar. Seine 16 Anschlüsse heißen im Uhrzeigersinn A–P, beginnend links oben: A–E oben, E–I rechts, I–M unten und M–A links. Jede Seite besitzt drei zusätzliche Punkte zwischen ihren Ecken. Im Editor sind angeschlossene Punkte grün und freie Punkte orange, mit kontrastreichen Buchstaben; in der Runtime verschwinden die Markierungen. Leitungen treten rechtwinklig ein. A/E werden von oben, I/M von unten angefahren; die seitlichen Punkte über ihre jeweilige Seitenkante.

Wähle das Widget und öffne **Berechnung bearbeiten**. Dort stellst du die Quadratgröße (96–2000 px), die Rollen **Aus**, **Eingang** und **Ausgang** für jeden Buchstaben sowie die Berechnung ein. Neue Andockpunkte sind zunächst ausgeschaltet; eine Eingangs- oder Ausgangsrolle im Dialog aktiviert den jeweiligen Punkt. Alle Punkte lassen sich auch im Bereich **Andockpunkte** gemeinsam einschalten.

**Eigene Formel** unterstützt `+`, `-`, `*`, `/`, Klammern, Zahlen mit Dezimalpunkt und die Buchstaben A–P. Multiplikation und Division gehen vor Addition und Subtraktion. Beispiel: `(A + B) / C`. Mehrere Leitungen an einem Eingang werden zunächst mit Vorzeichen summiert: A mit 100 und 50 ergibt 150; B mit 30 ergibt bei `A - B` den Wert 120. **Durchschnitt aller belegten Eingänge** zählt jeden belegten Eingangsanschluss einmal, hier also `(150 + 30) / 2 = 90`; unbelegte Punkte bleiben unberücksichtigt.

Die Vorschau zeigt Eingangswerte und Ergebnis. Ausgänge geben das Ergebnis intern an SVG-Lines, weitere LineBoxes und Widgets mit numerischer Dockpunktübernahme weiter. Eine zusätzliche HA-Entität ist nicht nötig. Fehlende oder ungültige angeschlossene Werte, nicht belegte Formel-Eingänge, Division durch null und Rückkopplungen stoppen die Ausgabe. Das Widget zeigt dann `—` mit Fehlerhinweis; Formeln werden ohne JavaScript-Ausführung ausgewertet. Der Dialog übernimmt Änderungen erst mit **Anwenden** und unterstützt Rückgängig.
