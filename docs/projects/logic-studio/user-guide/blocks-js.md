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

## Einen Import Schritt für Schritt prüfen

1. Öffne das Projektmenü und schalte den **Expertenmodus** ein. Öffne im Editor **Expertenwerkzeuge → ioBroker-Export einfügen**.
2. Füge das Blockly-XML oder einen ioBroker-JavaScript-Export mit eingebetteten Blockly-Daten ein. Klicke **Import prüfen**. Die Liste zeigt, welche Blöcke übernommen wurden und wo eine Zuordnung fehlt.
3. Klicke **Als Projekt öffnen** und ergänze die Hinweise direkt an den betroffenen Blöcken. Bei einem importierten POST trägst du beispielsweise den HA-REST-Befehl ein, der die Header und den Zeitrahmen definiert.
4. Speichere den Entwurf und starte zuerst den **Testlauf**. Für die echte Ausführung wähle danach **Play**. Öffne das **Protokoll**, kontrolliere die Ausgabe und beende den Lauf mit **Stopp**.

## Wenn etwas nicht klappt

Wenn der Import einen Platzhalter zeigt, lies den Blockhinweis und ersetze oder ergänze den Block vor dem Start.
