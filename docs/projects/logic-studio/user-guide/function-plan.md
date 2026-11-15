# Funktionsplan

## Ein Signal im Funktionsplan umkehren

### 1. Plan öffnen und Bausteine hinzufügen

Öffne **Funktionsplan** im Projektbaum. Suche links nacheinander `STATE_IN`, `NOT` und `STATE_OUT`. Klicke jeweils auf den Baustein, um ihn einzufügen. Ziehe die Bausteine an ihrer Kopfzeile in dieser Reihenfolge von links nach rechts.

### 2. Eingang konfigurieren

Öffne über das Zahnrad die Eigenschaften von `STATE_IN`. Trage die Entitäts-ID deines Sensors oder Testhelfers ein. Im Bild ist das `binary_sensor.bewegung`. Stelle **Signaltyp** auf `BOOL` und **Demo-Eingang (nur Simulation)** auf `TRUE`.

### 3. Ausgang konfigurieren

Öffne die Eigenschaften von `STATE_OUT`. Trage eine passende Ziel-ID ein. Im Bild ist es `light.flur`. Lass den **Ausgangsmodus** auf `BOOL`. Ein BOOL-Signal hat genau zwei Werte, `TRUE` und `FALSE`.

### 4. Anschlüsse verbinden

Ziehe vom runden Ausgangspunkt **Q** von `STATE_IN` zum Eingangspunkt **IN** von `NOT`. Ziehe dann von **OUT** an `NOT` zu **IN** an `STATE_OUT`. Oberhalb der Zeichenfläche sollten drei Bausteine und zwei Verbindungen stehen.

### 5. Simulation ausführen

Klicke oben auf **Simulation** (Kolbensymbol). Am Eingang siehst du `Demo: true`. `NOT` kehrt den Wert um. Bei `STATE_OUT` steht deshalb `Demo: false`. Die Simulation verwendet Demowerte und schaltet die Leuchte nicht.

### 6. Gegenprobe machen

Setze den Demo-Eingang auf `FALSE` und klicke erneut auf **Simulation**. Jetzt ist der Ausgang `true`. Mit **Simulation zurücksetzen** startest du den Simulationszustand neu. Wenn du den Plan behalten möchtest, speichere das Projekt.

[![Funktionsplan mit STATE_IN, NOT und STATE_OUT. Die Simulation zeigt true am Eingang und false am Ausgang.](/images/logic-studio/user-guide/function-plan-walkthrough-de.jpg)](/images/logic-studio/user-guide/function-plan-walkthrough-de.jpg)

Wenn eine Verbindung abgelehnt wird, prüfe die Signaltypen. Falls die Simulation eine fehlende Entitäts-ID meldet, überprüfe die Eigenschaften von Eingang und Ausgang. Nutze für dieses Beispiel das Simulationssymbol. **Play** in der Projektleiste startet die Runtime.

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
