# Blocks A

## Erstes Beispiel

Die Beispielautomation schaltet das Flurlicht ein, sobald der Bewegungssensor `on` meldet.

1. Wähle **Neues Projekt → Blocks A** und gib dem Projekt einen Namen. Auf der Fläche steht der Block **Automation**.
2. Öffne **Auslöser** und ziehe den Zustandsblock in **Wenn**. Im Bild steht `binary_sensor.flur_bewegung` mit dem Zielzustand `on`. Wähle auf deinem System deinen Testhelfer oder Sensor.
3. Öffne **Aktionen** und ziehe den Schaltblock in **Dann**. Im Bild steht `light.flur` auf **einschalten**. Für deinen ersten Versuch kannst du einen zweiten Testhelfer als Ziel verwenden. **Nur wenn** bleibt in diesem Beispiel leer.
4. Klicke auf das Fähnchen **Blöcke prüfen**. Wenn die Prüfung erfolgreich ist, wähle **Als HA-YAML öffnen**. Kontrolliere im Entwurf `triggers` und `actions`, bevor du exportierst.

[![Blocks A mit Zustandsauslöser in Wenn und Schaltaktion in Dann](/images/logic-studio/user-guide/blocks-a-de.png)](/images/logic-studio/user-guide/blocks-a-de.png)

## Funktionen

### Blockpalette und Anschlüsse

Wähle einen Block aus und setze ihn an die passende Stelle. Die Form zeigt, ob er einen Wert liefert oder eine Aktion ausführt.

### Auslöser und Bedingungen

Der Auslöser startet die Automation. Eine Bedingung prüft zum Beispiel, ob der zweite Helfer bereits aus ist.

### Aktionen und Reihenfolge

Stecke Aktionen untereinander. Home Assistant führt sie in der exportierten Reihenfolge aus.

### HA-Auswahl

Wähle eine Entität, Aktion oder ein Geräte-, Bereichs-, Label- oder Etagentarget. Im YAML erkennst du das Ziel am passenden ID-Feld.

### HA-YAML-Entwurf

Öffne die erzeugte Automation als YAML-Entwurf. Der Entwurf zeigt den Namen des Quellprojekts.

### Export

Prüfe das YAML und übernimm es in Home Assistant. Dort kannst du einen echten Auslöser und den Automations-Trace prüfen.

## Wenn etwas nicht klappt

Wenn die Zielauswahl leer ist, kontrolliere, ob es auf dem verbundenen HA-System einen passenden Eintrag gibt.
