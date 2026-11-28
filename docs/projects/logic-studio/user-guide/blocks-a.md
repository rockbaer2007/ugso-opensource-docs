# Blocks A

## Sensorzustand setzen {#sensorzustand-setzen}

### Dezimalzahl direkt eingeben {#sensor-dezimalzahl}

Seit **0.1.134**: Wähle unter **System → Sensorzustand setzen · Dezimalzahl** einen Sensor und gib den Wert direkt ein. Vorgabe `0.5`, etwa `33.25` mit Punkt als Dezimaltrennzeichen. Es erfolgt keine Ganzzahlrundung; Speichern und Neuladen erhalten den Wert. Der bisherige Baustein mit Werteingang bleibt verfügbar. WRITE-Freigabe und Sensorattribute werden wie beim bisherigen Baustein behandelt. Blocks A benötigt die laufende Studio-App.

**Geprüft:** 72 lokale Tests sowie nach Sicherung auf HA 2026.11.3 die Werte `0.5` und `33.25`: Blocks JS per Play, Blocks A über die generierten und geprüften Ereignisdaten. Beide Zahlenfelder nach Neuladen bestätigt, Einstellungen und Attribute erhalten.

Ab **0.1.133** steht unter **System** der Baustein **Sensorzustand setzen** bereit:

1. Wähle einen vorhandenen `sensor.*` über die HA-typische Entitätenauswahl.
2. Verbinde den Werteingang mit einer Zahl, einem Text oder einer Berechnung (höchstens 255 Zeichen als Zustand).
3. Gib den Sensor in der App-Konfiguration unter **WRITE – einzelne Ziele** (`runtime_write_entities`) frei. Vorhandene Einträge erhalten. READ allein genügt nicht.
4. Wähle **Blöcke prüfen → Als HA-YAML öffnen**. Installiere die geprüfte Automation anschließend selbst in Home Assistant.

Beispiel der erzeugten Aktion:

```yaml
actions:
  - event: logic_studio_set_sensor_state
    event_data:
      entity_id: sensor.example
      state: 43
```

Die laufende Studio-App empfängt das Ereignis und prüft WRITE. Ohne laufende App erfolgt keine Verarbeitung. Für diesen internen Eingang ist keine allgemeine EVENT-Freigabe nötig. Fehler stehen im App-Protokoll; ein erfolgreich ausgelöstes Ereignis bestätigt noch keinen erfolgreichen Schreibzugriff.

Der Baustein erhält Einheit, Geräteklasse und andere Attribute. Er verhält sich wie **Entwicklerwerkzeuge → Zustände**, schaltet kein Gerät und legt keinen dauerhaften Sensor an. Die zuständige Integration kann den Wert später ersetzen. Die YAML-Vorschau führt keinen Schreibzugriff aus.

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
