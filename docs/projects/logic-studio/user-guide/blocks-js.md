# Blocks JS

## Erstes Beispiel

Der Testlauf liest einen simulierten Entitätszustand und schreibt ihn ins Protokoll.

1. Wähle **Neues Projekt → Blocks JS**. Öffne **System** und ziehe **debug output** in den Arbeitsbereich.
2. Ziehe **Zustand von Entität** aus derselben Kategorie in den freien Werteanschluss von **debug output**. Wähle deine Testentität. Im Bild ist es `binary_sensor.bewegung`.
3. Wähle **Testlauf starten**. Unter **Protokoll** stehen der gelesene Zustand und die Ausgabemeldung. In der Demo steht dort `on`. Der Testlauf sendet hier keinen Schaltbefehl.

[![Blocks JS mit verbundenem Entitätsblock und Zustand on im Protokoll](/images/logic-studio/user-guide/blocks-js-de.png)](/images/logic-studio/user-guide/blocks-js-de.png)

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

### Berechnete ioBroker-ID auf Existenz prüfen

Wenn dein ioBroker-Skript eine ID aus mehreren Textteilen zusammensetzt, kannst du sie mit dem importierten Block `state_exists_var` prüfen.

1. Öffne die Importprüfung und trage im Feld **ID-Zuordnung (JSON)** die fertig zusammengesetzte ioBroker-ID und die dazugehörige HA-Entitäts-ID ein, zum Beispiel `{"0_userdata.0.garten.pumpe":"switch.gartenpumpe"}`. Das Feld findest du auch am importierten Block.
2. Gib die zugeordnete Entität in den App-Einstellungen unter `runtime_read_entities` frei, sofern sie noch keine Schreibfreigabe hat.
3. Speichere das Projekt und starte **Play**. Eine vorhandene HA-Entität ergibt `true`, eine zugeordnete, aber fehlende Entität `false`. Fehlt für die berechnete ID ein Eintrag, stoppt der Lauf und nennt die ID im Protokoll. Ergänze den Eintrag am Block und starte erneut.

### Einen ioBroker-Datenpunkt als HA-Helfer übernehmen

Wenn dein Blockly-Export den Block **Datenpunkt erzeugen** (`createState`) enthält, kannst du den Wert in einem Home-Assistant-Helfer speichern. Der Helfer erscheint in Home Assistant unter **Einstellungen → Geräte & Dienste → Helfer**.

1. Öffne **Expertenwerkzeuge → ioBroker-Export einfügen** und klicke nach dem Einfügen auf **Import prüfen**.
2. Wähle für die ioBroker-ID eine der drei Möglichkeiten:
   - **Helfer zuordnen** verwendet einen vorhandenen Helfer. Sein aktueller Wert bleibt erhalten.
   - **Helfer anlegen** schlägt aus dem Datentyp einen Schalter, Zahlen- oder Texthelfer vor. Prüfe und bestätige den Namen. Das Anlegen erfordert ein HA-Administratorkonto. Ein unterstützter fester Startwert wird einmalig gesetzt. Bei einem berechneten Startwert kannst du einen Helfer in HA vorbereiten und zuordnen.
   - **Später zuordnen** lässt die Zuordnung offen. Öffne das Projekt und wähle vor dem Start im importierten Block eine passende HA-Entität aus.
3. Prüfe, ob die Blöcke zum Erzeugen, Lesen und Aktualisieren derselben ioBroker-ID auf dieselbe HA-Entität zeigen. Wähle **Als Projekt öffnen** und speichere das Projekt.
4. Gib den Helfer in den App-Optionen unter `runtime_read_entities` und für das Aktualisieren zusätzlich unter `runtime_write_entities` frei. Starte das gespeicherte Skript mit **Play**. Das Skript greift auf den aktuellen Wert des Helfers zu, auch wenn du ihn in Home Assistant änderst.

Im Beispiel wird ein Zahlenhelfer mit **17** angelegt. Im Protokoll steht beim ersten Start **17** und das Skript schreibt **42**. Nach einem Skriptneustart steht im Protokoll **42**. So kannst du prüfen, ob der Startwert nur bei der Anlage gesetzt wurde. [Blockly-Beispiel](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/ha-logic-studio-pro-v0.1.122/ha_logic_studio_pro/tests/fixtures/iobroker-create-state.xml)

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
