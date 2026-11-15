# Funktionsplan

## Erstes Beispiel

Erstelle einen Funktionsplan. Ziehe einen digitalen Eingang und einen Ausgang auf die Fläche. Verbinde den Ausgangspin des Eingangs mit dem Eingangspin des Ausgangs. Starte die Simulation und schalte den Eingang um. Der Ausgang folgt dem Signal.

In der Zeichenfläche siehst du die verbundenen Bausteine und die Miniübersicht unten rechts.

![Funktionsplan mit verbundenen Bausteinen und Miniübersicht](/images/logic-studio/0.1.8-react-flow-193.jpg)

## Funktionen

### Zeichenfläche

Bausteine ziehen, verschieben und verbinden. Mit Zoom und Einpassen behältst du den Überblick.

### Parameter

Wähle den Baustein und stelle etwa die Zeit eines Timers oder den Sollwert eines Zählers ein.

### HA-Ein- und Ausgänge

Ordne eine Entität für das Eingangssignal und bei Bedarf eine freigegebene HA-Aktion für den Ausgang zu.

### Simulation

Schalte Eingangswerte um und verfolge die Signale an den Anschlüssen.

### Haltepunkt und Einzelschritt

Halte die Simulation an und gehe einen Zyklus weiter, um die Werte zu prüfen.

### Anordnen und Anheften

Ordne den Plan automatisch an. Angeheftete Bausteine behalten dabei ihre Position.

### Play und Live-Diagnose

Starte den gespeicherten Plan. Die Diagnose zeigt Werte und Fehler des laufenden Plans.

### Zähler und Merker speichern

Aktiviere die Option, wenn diese Werte einen App-Neustart überstehen sollen. Eine Änderung am Plan kann den Speicher zurücksetzen.

## Wenn etwas nicht klappt

Wenn die Verbindung nicht angenommen wird, vergleiche die Typen beider Anschlüsse. Ein Zahlenausgang passt nicht an jeden Eingang.
