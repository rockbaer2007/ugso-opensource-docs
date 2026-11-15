# Blocks JS

## Erstes Beispiel

Ziehe einen Block für die Protokollausgabe in den Arbeitsbereich. Verbinde seinen Werteingang mit **Zustand von Entität** und wähle deinen Testhelfer. Starte den Testlauf und suche den Wert im Protokoll.

## Funktionen

### System, Aktionen und Sendto

Lies Entitäten, schalte freigegebene Ziele, sende Nachrichten oder nutze eine Verlaufsabfrage. Dynamische Anschlüsse nehmen zum Beispiel eine Entitäts-ID aus einer Schleife an.

### Trigger, Datum und Timeouts

Starte Aktionen bei Zustandsänderung, Astrozeit oder Zeitplan. Nutze einfache oder benannte CRON-Pläne, Verzögerungen und Intervalle. Benannte Läufe lassen sich stoppen.

### Werte bearbeiten

Konvertierung, Objekt, Logik, Mathematik, Text, Listen und Farbe liefern Werte, die du in andere Blöcke stecken kannst. Schleifen wiederholen Abläufe.

### Variablen und Funktionen

Speichere Zwischenwerte in Variablen. Funktionen bündeln Schritte, können Werte zurückgeben und lassen sich erneut aufrufen.

### ioBroker-Import

Öffne im Expertenmodus **ioBroker-Export einfügen**, füge den Export ein und prüfe die Übersicht. Wähle HA-Entitäten ausdrücklich zu und beachte Hinweise direkt am Block.

### HTTP in importierten Blöcken

Ordne einen freigegebenen HA-REST-Befehl zu. URL, Timeout und zusätzliche Request-Header werden in HA konfiguriert. Der importierte Content-Type steht als Vorgabe im POST-Block.

### Testlauf und Play

Der Testlauf simuliert. Speichere vor Play und schau im Protokoll nach, ob die echte HA-Aktion ausgeführt wurde.

## Wenn etwas nicht klappt

Wenn der Import einen Platzhalter zeigt, lies den Blockhinweis und ersetze oder ergänze den Block vor dem Start.
