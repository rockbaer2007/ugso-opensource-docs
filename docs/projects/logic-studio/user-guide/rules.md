# Rules

## Regel für ein Flurlicht erstellen

### 1. Projekt anlegen

Wähle **Neues Projekt → Regeln** und gib einen Namen ein, etwa **Flurlicht bei Bewegung**. Öffne **Assistent**. Der Dialog führt dich durch **Löst aus**, **Bedingungen**, **Aktionen** und **Übersicht**.

### 2. Auslöser festlegen

Wähle **Zustand**. Trage bei **Entität** deinen Bewegungssensor oder ersten Testhelfer ein. Im Bild ist es `binary_sensor.bewegung`. Trage bei **Nach** `on` ein. Lass **Von**, Attribut und Mindestdauer leer. Klicke auf **Weiter**.

[![Zustandsauslöser im ersten Schritt des Rules-Assistenten](/images/logic-studio/user-guide/rules-trigger-de.jpg)](/images/logic-studio/user-guide/rules-trigger-de.jpg)

### 3. Bedingungen überspringen

Klicke im Schritt **Bedingungen** auf **Weiter**. Für dieses Beispiel reicht der Zustandswechsel als Auslöser. Eine zusätzliche Bedingung wäre etwa, dass es nach 18 Uhr ist.

### 4. Aktion hinzufügen

Wähle bei **DANN** **+ Hinzufügen**. Lass als Schritttyp **HA-Aktion** stehen. Wähle `light.turn_on` und als **Ziel-Entität** deine Testleuchte. In der Demo ist es `light.flur`. Für einen zweiten Umschalter als Ziel verwende `input_boolean.turn_on`. Lass **SONST** leer und klicke auf **Weiter**.

### 5. Übersicht und YAML prüfen

Unter `triggers` steht die gewählte Entität mit `to: "on"`. Unter `actions` stehen die Aktion und ihr Ziel. Klicke auf **Übernehmen**. Im Editor kannst du die Regel speichern, mit **Als HA-YAML öffnen** den Entwurf ansehen und dort die Datei exportieren.

### 6. In Home Assistant ausprobieren

Übernimm die geprüfte Automation in Home Assistant. Setze den Auslöser zunächst auf `off` und dann auf `on`. Kontrolliere, ob das richtige Ziel eingeschaltet wurde. Im **Trace** der Automation siehst du, welcher Auslöser und welche Aktion ausgeführt wurden.

[![Rules mit Zustandsauslöser im Abschnitt FALLS und Lichtaktion im Abschnitt DANN](/images/logic-studio/user-guide/rules-walkthrough-de.jpg)](/images/logic-studio/user-guide/rules-walkthrough-de.jpg)

## Funktionen

### Assistent und Palette

Der Assistent führt durch Auslöser, Bedingungen und Aktionen. In der Palette kannst du suchen und Bausteine zum passenden Abschnitt ziehen.

### Auslöser

Ein Auslöser startet die Regel. Wähle Zustand mit Von/Nach, Attribut und Mindestdauer, Zahlenschwelle, Uhrzeit, Helferuhrzeit, Sonne mit Versatz, MQTT, HA-Ereignis oder HA-Start. Bereich und Label fassen ausgewählte Entitäten zusammen.

### Bedingungen

Prüfe Zustand, Zahlenwert, Attribut, Uhrzeit oder Wochentag. UND verlangt alle Prüfungen, ODER mindestens eine, NICHT kehrt die Prüfung um.

### Ausgelöst durch

Gib Auslösern IDs wie `first` und `second`. Prüfe die ID unter UND. Damit entscheidet dieselbe Regel je nach Auslöser zwischen DANN und SONST.

### Template

Im Expertenmodus kannst du eine native HA-Template-Bedingung eingeben. Ihr Ergebnis entscheidet, ob die Bedingung erfüllt ist.

### Aktionen und Zweige

Füge mehrere Aktionen in der gewünschten Reihenfolge ein. Wähle Ziel und Parameter oder nutze Verzögerung, Warten auf Zustand, Skriptaufruf oder Benachrichtigung.

### YAML und Rules-JSON

YAML ist für Home Assistant. Rules-JSON als Text oder Datei kannst du wieder im Rules-Editor öffnen.

## Wenn etwas nicht klappt

Wenn ein Schwellenwert-Auslöser nur einmal feuert, bringe den Wert erst wieder aus dem Schwellenbereich und anschließend erneut hinein.
