# Rules

## Erstes Beispiel

Lege eine Regel an und öffne den Assistenten. Wähle **Zustand**, deinen Testhelfer und als neuen Wert `on`. Füge unter **DANN** eine Aktion für einen zweiten Helfer hinzu. Exportiere die Regel als HA-YAML und prüfe sie in Home Assistant.

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
