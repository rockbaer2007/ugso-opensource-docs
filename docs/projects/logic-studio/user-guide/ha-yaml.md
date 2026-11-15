# HA-YAML

## Erstes Beispiel

Die Vorlage zeigt eine Automation, die bei Bewegung das Flurlicht einschaltet.

1. Wähle **Neues Projekt → HA-YAML**, stelle **HA-Automation** ein, öffne die Vorlage und gib dem Entwurf einen Namen.
2. Wähle **YAML**. Unter `triggers` steht der Zustandsauslöser. Unter `actions` steht `light.turn_on` mit dem Ziel `light.flur`. Ersetze für eine eigene Automation die Entitäts-IDs durch deine tatsächlichen Ziele.
3. Klicke auf **Prüfen**. Falls eine Zeile markiert wird, öffne den Hinweis und korrigiere die markierte Stelle.
4. Wechsle zu **Grafisch**. Die Verbindung führt vom Bewegungsauslöser zur Lichtaktion. Über **Exportieren** kannst du das YAML als Datei speichern.

[![HA-YAML-Quelltext mit Auslöser, Aktion und Ziel](/images/logic-studio/user-guide/ha-yaml-source-de.png)](/images/logic-studio/user-guide/ha-yaml-source-de.png)

[![Grafische Vorschau mit verbundenem Bewegungsauslöser und Lichtaktion](/images/logic-studio/user-guide/ha-yaml-graph-de.png)](/images/logic-studio/user-guide/ha-yaml-graph-de.png)

## Funktionen

### YAML-Eingabe und Import

Öffne eine YAML-Datei oder füge YAML ein. Der JSON-Import unterstützt HA-Automationsdaten und kompatible FLODE-Exporte.

### Syntax und Struktur

Farben helfen beim Lesen. Prüfen markiert Syntaxfehler, unbekannte Entitäten, ungültige Aktionsfelder und Fehler in verschachtelten `choose`-Zweigen an der Zeile.

### Entitäten und Aktionen einfügen

Setze den Cursor an die gewünschte Stelle. Wähle eine Entität oder HA-Aktion, um ihren Bezeichner dort einzufügen.

### Grafisch

Verschiebe und zoome den Ablauf. **Alles einpassen** zeigt den ganzen Plan. Beschriftete `choose`-Ausgänge zeigen, welcher Zweig zu welcher Aktion führt.

### YAML- und JSON-Export

Nutze YAML für HA. Verwende die JSON-Ansicht für den JSON-Export. Ein unveränderter YAML-Entwurf kann inklusive unbekannter Felder und Blueprint-Feldern zurückexportiert werden.

### HA-Verknüpfung

Wähle optional eine vorhandene Automation oder ein Skript. Du kannst den Status prüfen und die angebotenen Steueraktionen nutzen.

## Wenn etwas nicht klappt

Wenn eine Zeile rot markiert ist, prüfe Einrückung und Feldnamen. Die grafische Ansicht dient zur Vorschau. Änderungen nimmst du im YAML vor.
