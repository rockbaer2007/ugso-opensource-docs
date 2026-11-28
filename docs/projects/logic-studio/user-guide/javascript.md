# JavaScript

Seit **0.1.136** liefern die schreibenden HA-APIs Promises. Für eine feste Reihenfolge beispielsweise `await ha.setSensorState("sensor.example", 1.5);` verwenden und danach mit `ha.readState("sensor.example")` lesen. Die Sensor-API wartet auf die bestätigte HA-Antwort und stellt den bestätigten Wert im lesbaren Snapshot bereit. `await ha.callAction(...)` wartet auf die Annahme des Auftrags, nicht auf eine physische Gerätebewegung. Timer und explizite Callback-Blöcke bleiben separate Fortsetzungen. 99 lokale Tests erfolgreich; kein HA-Livetest für diese Version.

## Erstes Beispiel

In diesem Beispiel schreibt eine einzelne Zeile eine Meldung ins Protokoll.

1. Wähle **Neues Projekt → JavaScript** und ersetze den Beispielcode durch `ha.log('Studio-Test');`.
2. Klicke rechts oben auf **Testlauf starten**. Du kannst den Code dabei vor dem Speichern ausprobieren.
3. Scrolle zum **Protokoll**. Unter `message` steht `Studio-Test`. Klicke auf **Speichern**, wenn du den Entwurf behalten möchtest.

[![JavaScript-Testlauf mit Studio-Test im Protokoll](/images/logic-studio/user-guide/javascript-de.png)](/images/logic-studio/user-guide/javascript-de.png)

## Funktionen

### Code vervollständigen

Beginne einen API-Namen zu tippen. Die Vorschläge zeigen Namen und beim Aufruf die erwarteten Parameter.

### Testwerte und Testlauf

Probiere dein Skript mit simulierten Zuständen. Protokollausgaben und Fehler helfen dir beim Prüfen.

### Fehlerzeile

Klicke auf die gemeldete Zeile oder gehe zu ihrer Nummer. Prüfe den angegebenen Ausdruck im ursprünglichen Code.

### Globale Funktionen

Exportiere eine Funktion aus einem globalen Skript. Wähle das Skript im Projekt aus, das die Funktion nutzen soll.

### Runtime und Autostart

Speichere und starte per Play. Aktiviere Autostart pro Projekt, falls es nach einem App-Neustart wieder laufen soll.

### Runtime-Protokoll

Lies Ausgaben und Fehler auch nach einem App-Neustart. Die App begrenzt die Aufbewahrung nach Alter und Größe.

## Wenn etwas nicht klappt

Wenn eine HA-Aktion abgelehnt wird, kontrolliere die freigegebenen Entitäten und Aktionen in den App-Optionen.
