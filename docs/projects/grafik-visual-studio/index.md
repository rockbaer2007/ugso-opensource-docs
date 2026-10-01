---
title: HA Grafik Visual Studio
description: "Das etwas andere Dashboard für Home Assistant: aktueller Entwicklungsstand und Bedienung."
---

# HA Grafik Visual Studio

**Das etwas andere Dashboard für Home Assistant.** Grafik Visual Studio ist eine experimentelle Home-Assistant-App mit freier Editorfläche und getrennter Runtime. Das Projekt befindet sich in einer frühen Entwicklungsphase; Format und Bedienung können sich ändern. Es ist derzeit nicht für produktive Dashboards gedacht.

[Editor und Tastenkombinationen](./editor) · [Alle 45 Widgets](./widgets) · [Zeichnen: SVG-Verbindungslinie](./zeichnen) · [Widget-Paket-Schnittstelle](./widget-pakete) · [Tool-Paket-Schnittstelle](./tool-pakete) · [Packer für Pakete](./packer) · [Quellcode und Home-Assistant-App](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio)

![Editor von HA Grafik Visual Studio mit Widget-Palette und SVG-Verbindungslinien](/images/grafik-visual-studio/editor-zeichnung.png)

*Editoransicht mit gezeichneten Verbindungslinien. [Bild in voller Auflösung öffnen](/images/grafik-visual-studio/editor-zeichnung.png).*

## Was derzeit möglich ist

- Mehrere Projekte und benannte Seiten mit eigenen Abmessungen, Hintergrund und Widgets verwalten. Die Runtime zeigt sichtbare Seiten separat an.
- Widgets auf einer scrollbar erreichbaren Fläche platzieren, verschieben, skalieren, benennen und per z-index anordnen. Mehrfachauswahl, Ausrichtung, Größenabgleich, Kopieren, Einfügen sowie Rückgängig/Wiederholen sind im Editor vorhanden.
- Widgets aus den Gruppen „HA Grafik – Basis“, „HA Grafik – Interaktiv“ und „HA Grafik – Spezial“ verwenden. Dazu gehören unter anderem Text, HTML, Bild, Zahl, Schalter, Slider, Tabelle und die SVG-Verbindungslinie. Die Widget-Palette zeigt je nach Typ eine Vorschau oder ein Symbol.
- Eigenschaften für Layout, CSS, „Generell“, Sichtbarkeit und Andockpunkte bearbeiten. Der Editor-Widget-Filter verwendet das Feld „Filterwort“ aus „Generell“.
- Mit dem Spezial-Widget Verbindungslinien mit Zwischen- und explizit aktivierten Sammelpunkten, Farben, Pfeilspitzen und Animationen zeichnen. Kreuzende Linien koppeln sich nicht von selbst.
- Dateien aus Home Assistants `www`-Ordner auswählen und unterstützte Dateien hochladen. Der Entitätenbrowser kann Entitäten und aktuelle Zustände suchen und Entity-IDs in Widget-Felder übernehmen.
- Änderungen automatisch nach einer einstellbaren Wartezeit speichern (standardmäßig fünf Sekunden) oder manuell speichern. Widgets lassen sich als JSON exportieren und importieren.
- Die Oberfläche übernimmt die Home-Assistant-Sprache: Deutsch bei deutscher HA-Sprache, sonst Englisch. Unter **Einstellungen → Sprache** kann jeder Browser **Automatisch**, **Deutsch** oder **English** wählen. Projekt- und Widget-Inhalte bleiben dabei unverändert.

## Grenzen des aktuellen Stands

In der Runtime lesen Sensor, String, Red Number, Bar, Gauge und Bool HTML eine gebundene Home-Assistant-Entität alle fünf Sekunden; auch Sichtbarkeitsregeln verwenden diese Zustände. Ein Switch-Widget kann `switch`, `light` und `input_boolean` über HA-Dienste schalten und zeigt anschließend den bestätigten HA-Zustand. Die übrigen Daten- und Steuer-Widgets verwenden noch lokale Testwerte. Die Auswahl einer Entity-ID bedeutet dort noch keine Live-Anbindung. „Nur für Gruppen“ in der Sichtbarkeit und das Verhalten von `multi-views` sind noch nicht vollständig umgesetzt. Der Editor-Filter wirkt nur auf die Editoransicht.

Die App hat einen normalen Home-Assistant-Ingress-Eintrag. Getrennte Seitenleisteneinträge für Editor und Runtime erfordern zusätzlich die experimentelle Integration aus `custom_components/ha_grafik_visual_studio`; sie setzt Home Assistant OS oder Supervised mit Supervisor voraus. Die [Repository-README](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/README.md) enthält die Installationsschritte.

Die Bedienung ist von VIS2 inspiriert. Grafik Visual Studio ist eine eigenständige Implementierung; VIS2-Code und VIS2-Widgets werden nicht mitgeliefert.
