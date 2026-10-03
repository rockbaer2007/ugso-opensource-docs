---
title: SVG LineBox Math
---

# SVG LineBox Math

![SVG LineBox Math: Berechnungsdialog mit Anschlüssen A–P, Eingangswerten und Durchschnitt 90](/images/grafik-visual-studio/linebox-math-dialog.png)

Das Bild zeigt den Berechnungsdialog mit **Durchschnitt aller belegten Eingänge**. Eingang **A** enthält bereits die Summe seiner beiden Leitungen (100 + 50 = **150**), Eingang **B** liefert **30**. Daher lautet das Ergebnis **90**. **G** ist als Ausgang eingerichtet und gibt dieses Ergebnis weiter. Die grünen Buchstaben A, B und G kennzeichnen angeschlossene Punkte; die orangefarbenen Buchstaben sind ohne Leitung. Ein unverbundener Eingang mit `—` zählt beim Durchschnitt nicht mit. Bei dieser Berechnungsart ist das Formelfeld deaktiviert, seine bisherige Formel bleibt jedoch erhalten.

Ab Studio 0.1.137 steht **SVG LineBox Math** ebenfalls unter **HA Grafik – Spezial**. Es bleibt als Quadrat im Editor und in der Runtime sichtbar. Seine 16 Anschlüsse heißen im Uhrzeigersinn A–P, beginnend links oben: A–E oben, E–I rechts, I–M unten und M–A links. Jede Seite besitzt drei zusätzliche Punkte zwischen ihren Ecken. Im Editor sind angeschlossene Punkte grün und freie Punkte orange, mit kontrastreichen Buchstaben; in der Runtime verschwinden die Markierungen. Leitungen treten rechtwinklig ein. A/E werden von oben, I/M von unten angefahren; die seitlichen Punkte über ihre jeweilige Seitenkante.

Wähle das Widget und öffne **Berechnung bearbeiten**. Dort stellst du die Quadratgröße (96–2000 px), die Rollen **Aus**, **Eingang** und **Ausgang** für jeden Buchstaben sowie die Berechnung ein. Neue Andockpunkte sind zunächst ausgeschaltet; eine Eingangs- oder Ausgangsrolle im Dialog aktiviert den jeweiligen Punkt. Alle Punkte lassen sich auch im Bereich **Andockpunkte** gemeinsam einschalten.

**Eigene Formel** unterstützt `+`, `-`, `*`, `/`, Klammern, Zahlen mit Dezimalpunkt und die Buchstaben A–P. Multiplikation und Division gehen vor Addition und Subtraktion. Beispiel: `(A + B) / C`. Mehrere Leitungen an einem Eingang werden zunächst mit Vorzeichen summiert: A mit 100 und 50 ergibt 150; B mit 30 ergibt bei `A - B` den Wert 120. **Durchschnitt aller belegten Eingänge** zählt jeden belegten Eingangsanschluss einmal, hier also `(150 + 30) / 2 = 90`; unbelegte Punkte bleiben unberücksichtigt.

Die Vorschau zeigt Eingangswerte und Ergebnis. Ausgänge geben das Ergebnis intern an SVG-Lines, weitere LineBoxes und Widgets mit numerischer Dockpunktübernahme weiter. Eine zusätzliche HA-Entität ist nicht nötig. Fehlende oder ungültige angeschlossene Werte, nicht belegte Formel-Eingänge, Division durch null und Rückkopplungen stoppen die Ausgabe. Das Widget zeigt dann `—` mit Fehlerhinweis; Formeln werden ohne JavaScript-Ausführung ausgewertet. Der Dialog übernimmt Änderungen erst mit **Anwenden** und unterstützt Rückgängig.
