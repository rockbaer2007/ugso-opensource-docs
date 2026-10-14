# Home Assistant Card Editor

Der Home Assistant Card Editor ist das erste offizielle ATLAS-Referenz-Plugin. Er zeigt, wie Plugin-Lebenszyklus, Discovery, Administration, Hub-Anzeige, Import/Export und Paketbau zusammen funktionieren.

## Aufgabe

Produktentscheidung vom 13.10.2026: Der Editor bleibt ausschließlich Expert.
Simple-Modus und Umschalter werden nicht wieder eingeführt. Unterstützte ältere
Projektimporte bleiben kompatibel.

Ab HA-App **0.1.292** entfällt auch die Startmodus-Auswahl in der
HA-App-Konfiguration und in Administration. Alte gespeicherte Simple-Werte
werden als Expert übernommen; Zugangsdaten und andere Einstellungen bleiben erhalten.

Das Plugin stellt einen Editor für Home-Assistant-Cards bereit. Es unterstützt den Expert-Workflow, Entity-Auswahl, Ressourcenprüfung, YAML/JSON-Import, HACS-nahe Bundle-Exporte und mehrsprachige Card-Pakete. Der frühere sichtbare Simple-Modus wurde entfernt; der Editor startet direkt im Expert-Workflow.

Im Expert-Workflow bleibt das Hintergrundraster quadratisch. Die Anzahl der Spalten wird oben über einen horizontalen Slider gesteuert, die Anzahl der Zeilen links über einen vertikalen Slider. Ein eigener Zoom-Slider verändert nur die Zellgröße und skaliert Breite und Höhe gemeinsam. Die frühere Streckfunktion ist damit in Feldanzahl und Zoom getrennt.

## Card-Liste auf Tablets

Ab HA-App **0.1.290** stehen bei einer Editorbreite von 521 bis 1180 Pixeln
zwei Cards nebeneinander in einem scrollbaren Fenster. Die Höhe passt sich an
die erste Card-Zeile an und bleibt auf kleinen Bildschirmhöhen begrenzt.
Weitere Cards sind durch Scrollen erreichbar. Die Aktionsbuttons über der Liste
stehen ebenfalls in zwei gleich breiten Spalten. Auf schmalen Smartphones bleibt
eine Spalte; die Desktop-Seitenleiste bleibt unverändert. Entscheidend ist die
Breite des eingebetteten Editors, nicht der Gerätename. Bestehende Projekte,
Favoriten und Einstellungen bleiben erhalten.

## Mobile Raster- und Titelbedienung

Ab HA-App **0.1.291** ist „Raster & Zoom“ bei Editorbreiten bis 1180 Pixeln
standardmäßig eingeklappt. Ein Antippen öffnet die X-, Y- und Zoom-Slider;
Ein- und Ausklappen verändert keine Werte oder Cards. Beim Wechsel auf eine
Desktopbreite werden die Slider wieder direkt angezeigt.

Auf Tablets stehen Titelfeld, „Titel übernehmen“ und „Entitätsname nutzen“ in
einer Reihe. Auf schmalen Smartphones steht das Titelfeld über den beiden
gleich breiten Buttons. Diese Anordnung gilt in DE/EN/FR.

## Live-Verbindung bei großen Entitätskatalogen

Ab HA-App **0.1.293** verarbeitet ATLAS Entitätsabfragen und Live-Ereignisse
in der Reihenfolge ihres Empfangs. Eine noch laufende Abfrage kann dadurch
ein danach empfangenes Ereignis nicht mehr mit alten Snapshot-Werten überholen.
Nach einem Verbindungsabbruch werden wartende Nachrichten der alten Verbindung
ignoriert; schlägt der neue Socket fehl, wird dessen Fehlerstatus angezeigt.
Gespeicherte Cards, Positionen und Zugangsdaten werden dabei nicht verändert.

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

Hub und Administration können lokalisierte Beschreibungen aus dem Plugin-Repository anzeigen. Die gewählte Sprache bevorzugt `descriptions.de`, `descriptions.en` oder
`descriptions.fr`, sofern vorhanden. Englisch bleibt der Fallback.
