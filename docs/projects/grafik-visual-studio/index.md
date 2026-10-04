---
title: HA Grafik Visual Studio
description: "Das etwas andere Dashboard für Home Assistant: aktueller Entwicklungsstand und Bedienung."
---

# HA Grafik Visual Studio

Neu ab Studio **0.1.210**: Das externe [Material-Design-Set](materialdesign.md) startet mit **Preview Color Schemes**, 26 Farbreihen und Klassisch/Material 3/Projektstandard. Paket 0.1.0 ist für den Registrierungstest im Community-Katalog vorbereitet.

## Paketkatalog und Downloads

Ab Katalog-Webseite **0.1.10** akzeptiert die Widget-Registrierung ausschließlich `.wg`, die Tool-Registrierung ausschließlich `.tp`. Die Dateiauswahl zeigt nur die passende Endung. Der Server prüft die Endung von Upload-Dateinamen und Download-Link-Pfaden sowie weiterhin Paketinhalt und Manifest-Typ. Die Upload-Prüfung gilt auch in der Administration.

Mit Katalog-Webseite **0.1.9** fragt die Registrierung nach neuen Studio-Funktionen (Ja/Nein/Unsicher); bei Ja oder Unsicher ist eine Beschreibung erforderlich und die Mindestversion kann als „Noch unbekannt“ angegeben werden. Bei Nein ist eine konkrete Mindestversion Pflicht. Die Administration legt die Mindestversion bei der Prüfung und nach einer erforderlichen Studio-Anpassung fest; vor der Freigabe muss eine konkrete Version eingetragen sein. Ein optionaler Paket-Upload erkennt die verwendeten Renderer/Aktionen; ohne Datei erfolgt die Analyse in der Administration. Unbekannte Funktionen erhalten „Studio-Anpassung erforderlich“ und bleiben bis zur Umsetzung und erneuten Prüfung außerhalb des öffentlichen Katalogs. Das Webseiten-Update muss vom Betreiber hochgeladen werden.

Ab Studio **0.1.212** kennzeichnet ein rotes `mdi:alert`-Symbol die GitHub-Auswahl und den Installationshinweis bei Widget- und Tool-Paketen. Vor der Installation muss das Installationsrisiko bestätigt werden.

Studio erkennt neue freigegebene Paketversionen beim Öffnen der Paketeinstellungen oder über **Katalog aktualisieren** und bietet **Aktualisieren** an. Dafür müssen die Paket-IDs übereinstimmen; das gilt auch für vorher lokal oder über GitHub installierte Pakete. Updates werden bewusst installiert. Beliebige GitHub-Repositories werden nicht automatisch überwacht.

Widget-Pakete, Tool-Pakete und Zusatztools findest du zentral im [UGSo-Paketkatalog auf visualstudio.ugso-software.de](https://visualstudio.ugso-software.de/?lang=de). Dazu gehören Technic, Wetter/Heizung, der Colorpicker sowie **Widget Test** und **Tools Test** für die Prüfung der Paketinstallation. Der **Packer für Windows und Linux** steht dort unter **Zusatztools** bereit. Beschreibung und Anleitung bleiben auf dieser Open-Source-Seite; Paketdateien werden über die Katalog-Subdomain angeboten.

**Das etwas andere Dashboard für Home Assistant.** Grafik Visual Studio ist eine experimentelle Home-Assistant-App mit freier Editorfläche und getrennter Runtime. Das Projekt befindet sich in einer frühen Entwicklungsphase; Format und Bedienung können sich ändern. Es ist derzeit nicht für produktive Dashboards gedacht.

[Editor und Tastenkombinationen](./editor) · [Alle 74 Widgets](./widgets) · [SVG-Line](./svg-line) · [SVG LineBox mit Videos](./svg-linebox) · [SVG LineBox Math](./svg-linebox-math) · [Widget-Paket-Schnittstelle](./widget-pakete) · [Tool-Paket-Schnittstelle](./tool-pakete) · [Packer für Pakete](./packer) · [Quellcode und Home-Assistant-App](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio)

![Editor von HA Grafik Visual Studio mit Widget-Palette und SVG-Verbindungslinien](/images/grafik-visual-studio/editor-zeichnung.png)

*Editoransicht mit gezeichneten Verbindungslinien. [Bild in voller Auflösung öffnen](/images/grafik-visual-studio/editor-zeichnung.png).*

## Was derzeit möglich ist

- Im Dateien-Fenster sucht das Suchfeld in allen Unterordnern von `/config/www/studio`, unabhängig vom geöffneten Ordner. Die Suche ignoriert Groß-/Kleinschreibung und berücksichtigt Dateinamen sowie Pfade. Treffer zeigen eine Bildvorschau und den relativen Pfad; Dateitypfilter und Bildübernahme bleiben nutzbar. Ein leeres Suchfeld zeigt wieder den geöffneten Ordner.
- Mehrfach ausgewählte Widgets lassen sich durch Ziehen eines ausgewählten Widgets gemeinsam verschieben, auch nach Kopieren und Einfügen. Ausgewählte SVG-Linien und Zwischenpunkte wandern mit; bestehende Andockverbindungen bleiben erhalten. Gesperrte Widgets verhindern das gemeinsame Verschieben. Ein Zug lässt sich als Ganzes rückgängig machen.
- Die Widget-Auswahlliste bleibt vor allen Widgets sichtbar. Ab **0.1.209** werden die angehakten Widgets über **Kopieren** und **Löschen** in der Werkzeugleiste bearbeitet; die doppelten Buttons unten in der Liste entfallen. Beim Löschen gilt der Bestätigungsdialog.
- Beim Löschen von Widgets erscheint ein Bestätigungsdialog mit den ausgewählten Widget-IDs. „Abbrechen“ oder Escape bricht ab; „Frage für die nächsten 5 Minuten unterdrücken“ überspringt weitere Löschfragen für fünf Minuten im geöffneten Editor. Löschen lässt sich weiterhin rückgängig machen.
- Die Widget-Auswahl übernimmt einzelne Häkchen und die Auswahl aller Widgets sofort in die Editorfläche. Signalbilder, Extrasteuerung und Andockpunkte sind bei neuen Widgets standardmäßig deaktiviert und lassen sich bei Bedarf aktivieren.
- Die Bildauswahl der Widgets verwendet ebenfalls `/config/www/studio`; übernommene und kopierte Bildpfade beginnen mit `/local/studio/`.
- Mehrere Projekte und benannte Seiten mit eigenen Abmessungen, Hintergrund und Widgets verwalten. Die Runtime zeigt sichtbare Seiten separat an.
- Widgets auf einer scrollbar erreichbaren Fläche platzieren, verschieben, skalieren, benennen und per z-index anordnen. Mehrfachauswahl, Ausrichtung, Größenabgleich, Kopieren, Einfügen sowie Rückgängig/Wiederholen sind im Editor vorhanden.
- 74 Widgets aus „HA Grafik – Basis“, „HA Grafik – Interaktiv“, „HA Grafik – Spezial“, „HA Grafik – Datenfluss“ und „HA Grafik – Gauges“ verwenden. Dazu gehören HTML, Bilder, Zahlen, Bedienelemente, Tabellen, Kalender, Dashboard-Einbettung, SVG-Linien, Berechnungen, Konverter und zehn Messinstrumente. Die Palette zeigt je nach Typ eine Vorschau oder ein Symbol.
- Eigenschaften für Layout, CSS, „Generell“, Sichtbarkeit und Andockpunkte bearbeiten. Der Editor-Widget-Filter verwendet das Feld „Filterwort“ aus „Generell“.
- Mit dem Spezial-Widget Verbindungslinien mit Zwischen- und explizit aktivierten Sammelpunkten, Farben, Pfeilspitzen und Animationen zeichnen. Kreuzende Linien koppeln sich nicht von selbst.
- Dateien aus Home Assistants `/config/www/studio`-Ordner auswählen und unterstützte Dateien hochladen. Der Dateienbrowser legt diesen Stammordner beim Öffnen automatisch an. Falls Schreibrechte fehlen, erscheint ein Hinweis zum manuellen Erstellen. Der Entitätenbrowser kann Entitäten und aktuelle Zustände suchen und Entity-IDs in Widget-Felder übernehmen.
- Änderungen automatisch nach einer einstellbaren Wartezeit speichern (standardmäßig fünf Sekunden) oder manuell speichern. Widgets lassen sich als JSON exportieren und importieren.
- Die Oberfläche übernimmt die Home-Assistant-Sprache: Deutsch bei deutscher HA-Sprache, sonst Englisch. Unter **Einstellungen → Sprache** kann jeder Browser **Automatisch**, **Deutsch** oder **English** wählen. Projekt- und Widget-Inhalte bleiben dabei unverändert.

## Ergänzungen bis 0.1.158

Die [Widget-Übersicht](./widgets) erklärt jetzt die VIS2-inspirierten Wertelisten, Bool HTML/Checkbox/Select, Table, HTML State, Bar, HTML/Navigation, Filter, String und Input val mit Bildern. CSS Allgemein bleibt bei jedem Widget aktiv. Umsteigerhinweise lassen sich unter Einstellungen → Allgemein abschalten.

**Dashboard in widget** unter Spezial bettet ein HA-Dashboard bis 800 × 640 Pixel ein. **View in widget** bleibt für Studio-Seiten zuständig. Unter [Datenfluss](./datenfluss) stehen Wert-Verbindung, Wert-Konverter und Wert-Berechnung bereit; [LineBox Math](./svg-linebox-math) bietet vier Rechnungen und eine einstellbare Darstellung.

## Vorgemerkt: Kalender-JSON-Integration

Geplant ist eine eigene Home-Assistant-Integration, die HA-Kalender für Kalender-Widgets und andere Verbraucher als JSON-Terminlisten bereitstellt. Die Terminanzahl soll der Sensorzustand sein; die vollständige Liste liegt im Attribut `events`. Zeitraum und Aktualisierung sollen einstellbar sein. Die direkte `calendar.*`-Anbindung des Terminkalenders ist bereits vorhanden; die wiederverwendbare Integration ist noch nicht implementiert.

## Grenzen des aktuellen Stands

In der Runtime lesen Sensor, String, Red Number, Bar, Gauge und Bool HTML eine gebundene Home-Assistant-Entität alle fünf Sekunden; auch Sichtbarkeitsregeln verwenden diese Zustände. Ein Switch-Widget kann `switch`, `light` und `input_boolean` über HA-Dienste schalten und zeigt anschließend den bestätigten HA-Zustand. Die übrigen Daten- und Steuer-Widgets verwenden noch lokale Testwerte. Die Auswahl einer Entity-ID bedeutet dort noch keine Live-Anbindung. „Nur für Gruppen“ in der Sichtbarkeit und das Verhalten von `multi-views` sind noch nicht vollständig umgesetzt. Der Editor-Filter wirkt nur auf die Editoransicht.

Die App hat einen normalen Home-Assistant-Ingress-Eintrag. Getrennte Seitenleisteneinträge für Editor und Runtime erfordern zusätzlich die experimentelle Integration aus `custom_components/ha_grafik_visual_studio`; sie setzt Home Assistant OS oder Supervised mit Supervisor voraus. Die [Repository-README](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/README.md) enthält die Installationsschritte.

Die Bedienung ist von VIS2 inspiriert. Grafik Visual Studio ist eine eigenständige Implementierung; VIS2-Code und VIS2-Widgets werden nicht mitgeliefert.
