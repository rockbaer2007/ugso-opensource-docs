# Home Assistant Card Editor

Der Home Assistant Card Editor ist das erste offizielle ATLAS-Referenz-Plugin. Er zeigt, wie Plugin-Lebenszyklus, Discovery, Administration, Hub-Anzeige, Import/Export und Paketbau zusammen funktionieren.

## Aufgabe

Das Plugin stellt einen Editor für Home-Assistant-Cards bereit. Es unterstützt Simple- und Expert-Workflows, Entity-Auswahl, Ressourcenprüfung, YAML/JSON-Import, HACS-nahe Bundle-Exporte und mehrsprachige Card-Pakete.

Im Expert-Workflow bleibt das Hintergrundraster quadratisch. Die Anzahl der Spalten wird oben über einen horizontalen Slider gesteuert, die Anzahl der Zeilen links über einen vertikalen Slider. Die frühere Streckfunktion ist damit als kontrollierte Rastergröße von `12` bis `17` Feldern pro Achse umgesetzt.

## Extension Points

Der Editor nutzt aktuell diese ATLAS-Extension-Points:

- `homeassistant.card-editor`
- `homeassistant.card-target`
- `homeassistant.entity-picker`
- `homeassistant.exporter`
- `atlas.plugin.package-builder`

## Paket

`createHomeAssistantCardEditorPluginInstallPackage()` erzeugt ein erstes Installpaket für das Referenz-Plugin. Es enthält ein Plugin-Manifest, eine README und ein Beispiel für eine Home-Assistant-Card-Konfiguration.

## Beschreibung im Hub

Hub und Administration können lokalisierte Beschreibungen aus dem Plugin-Repository anzeigen. Wenn Deutsch gewählt ist, wird bevorzugt `descriptions.de` verwendet. Englisch bleibt der Fallback.
