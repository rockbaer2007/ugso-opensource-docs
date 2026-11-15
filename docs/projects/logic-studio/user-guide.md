# Bedienungsanleitung

Diese Anleitung richtet sich an Einsteiger. Öffne HA Logic Studio Pro in Home Assistant, wähle **Neues Projekt**, dann einen Editor und einen Namen. Für die Beispiele kannst du unter **Einstellungen → Geräte & Dienste → Helfer** einen eigenen Umschalter anlegen. Im Beispiel heißt er `input_boolean.studio_test`. Verwende die tatsächliche Entitäts-ID deines Helfers.

## Welchen Editor brauche ich?

- **Funktionsplan** für Signale, Timer und Zähler auf einer Zeichenfläche.
- **Rules** für Regeln nach dem Muster FALLS → DANN oder SONST.
- **Blocks A** für Home-Assistant-Automationen, die du aus Blöcken zusammensetzt.
- **Blocks JS** für Skripte aus Blöcken und den ioBroker-Import.
- **JavaScript** oder **TypeScript** zum Schreiben eigener Skripte.
- **HA-YAML** zum Bearbeiten, Prüfen und Visualisieren von Automationen und Skripten.

## Bedienung in den Editoren

- **Speichern** übernimmt deine Änderungen. Orange zeigt an, dass etwas geändert wurde. Grau bedeutet, dass nichts zu speichern ist.
- **Abbrechen** verwirft seit dem letzten Speichern vorgenommene Änderungen und lädt den gespeicherten Stand.
- **Testlauf** nutzt bei den Skripteditoren eine Simulation. Im Funktionsplan kannst du Eingänge in der Simulation umschalten.
- **Play** startet in Funktionsplan, Blocks JS, JavaScript und TypeScript den gespeicherten Stand in der Runtime. Dort können freigegebene HA-Aktionen echte Entitäten verändern. **Stopp** beendet den Lauf.
- **Prüfen** zeigt Fehler vor dem Export oder Ausführen. **Exportieren** erzeugt eine Datei, die du bei Bedarf in Home Assistant übernimmst.
- **Expertenmodus** im Projektmenü zeigt zusätzliche Werkzeuge des jeweiligen Editors. **Protokoll** zeigt Ausgaben und Fehler des geöffneten Projekts.

## Editoren

- [Funktionsplan](./user-guide/function-plan)
- [Rules](./user-guide/rules)
- [Blocks A](./user-guide/blocks-a)
- [Blocks JS](./user-guide/blocks-js)
- [JavaScript](./user-guide/javascript)
- [TypeScript](./user-guide/typescript)
- [HA-YAML](./user-guide/ha-yaml)
- [Fehler melden und mitarbeiten](./user-guide/feedback)
