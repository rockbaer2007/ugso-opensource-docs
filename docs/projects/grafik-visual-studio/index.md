---
title: HA Grafik Visual Studio
description: "Das etwas andere Dashboard für Home Assistant: aktueller Entwicklungsstand und Bedienung."
---

# HA Grafik Visual Studio

**Das etwas andere Dashboard für Home Assistant.** Grafik Visual Studio ist eine experimentelle Home-Assistant-App mit freier Editorfläche und getrennter Runtime. Das Projekt befindet sich in einer frühen Entwicklungsphase; Format und Bedienung können sich ändern. Es ist derzeit nicht für produktive Dashboards gedacht.

[Editor und Tastenkombinationen](./editor) · [Alle 48 Widgets](./widgets) · [SVG-Line](./svg-line) · [SVG LineBox mit Videos](./svg-linebox) · [SVG LineBox Math](./svg-linebox-math) · [Widget-Paket-Schnittstelle](./widget-pakete) · [Tool-Paket-Schnittstelle](./tool-pakete) · [Packer für Pakete](./packer) · [Quellcode und Home-Assistant-App](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio)

![Editor von HA Grafik Visual Studio mit Widget-Palette und SVG-Verbindungslinien](/images/grafik-visual-studio/editor-zeichnung.png)

*Editoransicht mit gezeichneten Verbindungslinien. [Bild in voller Auflösung öffnen](/images/grafik-visual-studio/editor-zeichnung.png).*

## Was derzeit möglich ist

- Im Dateien-Fenster sucht das Suchfeld in allen Unterordnern von `/config/www/studio`, unabhängig vom geöffneten Ordner. Die Suche ignoriert Groß-/Kleinschreibung und berücksichtigt Dateinamen sowie Pfade. Treffer zeigen eine Bildvorschau und den relativen Pfad; Dateitypfilter und Bildübernahme bleiben nutzbar. Ein leeres Suchfeld zeigt wieder den geöffneten Ordner.
- Mehrfach ausgewählte Widgets lassen sich durch Ziehen eines ausgewählten Widgets gemeinsam verschieben, auch nach Kopieren und Einfügen. Ausgewählte SVG-Linien und Zwischenpunkte wandern mit; bestehende Andockverbindungen bleiben erhalten. Gesperrte Widgets verhindern das gemeinsame Verschieben. Ein Zug lässt sich als Ganzes rückgängig machen.
- Die Widget-Auswahlliste bleibt vor allen Widgets sichtbar. Über „Kopieren“ und „Löschen“ direkt in der Liste lassen sich die angehakten Widgets gemeinsam bearbeiten; beim Löschen gilt der Bestätigungsdialog.
- Beim Löschen von Widgets erscheint ein Bestätigungsdialog mit den ausgewählten Widget-IDs. „Abbrechen“ oder Escape bricht ab; „Frage für die nächsten 5 Minuten unterdrücken“ überspringt weitere Löschfragen für fünf Minuten im geöffneten Editor. Löschen lässt sich weiterhin rückgängig machen.
- Die Widget-Auswahl übernimmt einzelne Häkchen und die Auswahl aller Widgets sofort in die Editorfläche. Signalbilder, Extrasteuerung und Andockpunkte sind bei neuen Widgets standardmäßig deaktiviert und lassen sich bei Bedarf aktivieren.
- Die Bildauswahl der Widgets verwendet ebenfalls `/config/www/studio`; übernommene und kopierte Bildpfade beginnen mit `/local/studio/`.
- Mehrere Projekte und benannte Seiten mit eigenen Abmessungen, Hintergrund und Widgets verwalten. Die Runtime zeigt sichtbare Seiten separat an.
- Widgets auf einer scrollbar erreichbaren Fläche platzieren, verschieben, skalieren, benennen und per z-index anordnen. Mehrfachauswahl, Ausrichtung, Größenabgleich, Kopieren, Einfügen sowie Rückgängig/Wiederholen sind im Editor vorhanden.
- Widgets aus den Gruppen „HA Grafik – Basis“, „HA Grafik – Interaktiv“ und „HA Grafik – Spezial“ verwenden. Dazu gehören unter anderem Text, HTML, Bild, Zahl, Schalter, Slider, Tabelle, SVG-Line und SVG LineBox. Die Widget-Palette zeigt je nach Typ eine Vorschau oder ein Symbol.
- Eigenschaften für Layout, CSS, „Generell“, Sichtbarkeit und Andockpunkte bearbeiten. Der Editor-Widget-Filter verwendet das Feld „Filterwort“ aus „Generell“.
- Mit dem Spezial-Widget Verbindungslinien mit Zwischen- und explizit aktivierten Sammelpunkten, Farben, Pfeilspitzen und Animationen zeichnen. Kreuzende Linien koppeln sich nicht von selbst.
- Dateien aus Home Assistants `/config/www/studio`-Ordner auswählen und unterstützte Dateien hochladen. Der Dateienbrowser legt diesen Stammordner beim Öffnen automatisch an. Falls Schreibrechte fehlen, erscheint ein Hinweis zum manuellen Erstellen. Der Entitätenbrowser kann Entitäten und aktuelle Zustände suchen und Entity-IDs in Widget-Felder übernehmen.
- Änderungen automatisch nach einer einstellbaren Wartezeit speichern (standardmäßig fünf Sekunden) oder manuell speichern. Widgets lassen sich als JSON exportieren und importieren.
- Die Oberfläche übernimmt die Home-Assistant-Sprache: Deutsch bei deutscher HA-Sprache, sonst Englisch. Unter **Einstellungen → Sprache** kann jeder Browser **Automatisch**, **Deutsch** oder **English** wählen. Projekt- und Widget-Inhalte bleiben dabei unverändert.

## Grenzen des aktuellen Stands

In der Runtime lesen Sensor, String, Red Number, Bar, Gauge und Bool HTML eine gebundene Home-Assistant-Entität alle fünf Sekunden; auch Sichtbarkeitsregeln verwenden diese Zustände. Ein Switch-Widget kann `switch`, `light` und `input_boolean` über HA-Dienste schalten und zeigt anschließend den bestätigten HA-Zustand. Die übrigen Daten- und Steuer-Widgets verwenden noch lokale Testwerte. Die Auswahl einer Entity-ID bedeutet dort noch keine Live-Anbindung. „Nur für Gruppen“ in der Sichtbarkeit und das Verhalten von `multi-views` sind noch nicht vollständig umgesetzt. Der Editor-Filter wirkt nur auf die Editoransicht.

Die App hat einen normalen Home-Assistant-Ingress-Eintrag. Getrennte Seitenleisteneinträge für Editor und Runtime erfordern zusätzlich die experimentelle Integration aus `custom_components/ha_grafik_visual_studio`; sie setzt Home Assistant OS oder Supervised mit Supervisor voraus. Die [Repository-README](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/README.md) enthält die Installationsschritte.

Die Bedienung ist von VIS2 inspiriert. Grafik Visual Studio ist eine eigenständige Implementierung; VIS2-Code und VIS2-Widgets werden nicht mitgeliefert.
