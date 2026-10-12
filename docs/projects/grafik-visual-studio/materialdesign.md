---
title: Material Design
description: Material Design 1.1.0 für Studio 0.1.292 mit DE/EN/FR und kompatiblen Updates.
---

# Material Design

Ab **Studio 0.1.295** füllen die Paket-Icons samt Symbolbereich ihren Rahmen in Seitenleiste und Widget-Auswahl. Die Paketgrafiken und Einstellungen bleiben erhalten; ein Paketupdate ist dafür nicht erforderlich. [Interaktiv-Neuerungen](/projects/grafik-visual-studio/interaktiv).

**Paket 1.1.0 · Studio ab 0.1.292 · 49 Widgets · MIT.** Eigenständige Renderer, angelehnt an [ioBroker VIS2 Material Design von typhosj/Scrounger](https://github.com/typhosj/ioBroker.vis2-materialdesign). Die originalen MDI-Zuordnungen bleiben als lokale SVGs enthalten. Technische Paket-ID: <code>ugso.materialdesign</code>.

[English](/en/projects/grafik-visual-studio/materialdesign) · [Français](/fr/projects/grafik-visual-studio/materialdesign) · [Quellcode](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign)

## Installation und erhaltene Einstellungen

1. Das vorhandene Studio-Projekt als JSON sichern.
2. Studio auf **0.1.292 oder neuer** aktualisieren und neu starten.
3. [Material Design 1.1.0 herunterladen](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign/blob/main/dist/ugso.materialdesign-1.1.0.wg). Unter **Einstellungen → Widget-Pakete → Lokal** installieren oder den direkten GitHub-Dateilink verwenden.
4. Das Paket wird additiv aktualisiert. Danach die Seite neu laden und das bestehende Projekt prüfen.

Die Installation schreibt **keine Projektdatei um**. Vorhandene Felder, Standardwerte, Reihenfolge und technische IDs bleiben geschützt. Neue Felder/Gruppen und Auswahlwerte werden ergänzt. Farben, Texte, Größen, Entitätszuordnungen und deaktivierte Gruppen bleiben gespeichert. Ältere veröffentlichte Paketdateien bleiben verfügbar.

Alte **State-Multi**-Widgets behalten den Wertezyklus. Mehrziel-Schreiben wird ausdrücklich als eigener Modus gewählt. Alte Advanced-Views behalten ihre Wertzuordnung; Seitenname/ID und numerischer Index sind zusätzliche Modi. Neue Widgets enthalten die entsprechenden Originalmodi. Ein Stilwechsel ändert keine Schreibziele.

## Sprachen und Gestaltung

**Material-Sprache** folgt Studio oder wählt **Deutsch, Englisch oder Französisch** für Widget und Material-Eigenschaften. Benutzertexte sowie Seiten- und Entitäts-IDs werden nicht übersetzt. Die Studio-Gesamtoberfläche bleibt DE/EN; Französisch wird hier für Material angeboten.

**Klassisch**, **Material 3** und **Projektstandard** bleiben wählbar. Das Farbschema folgt der Seite oder wird auf Hell/Dunkel festgelegt. Explizite Farben, Schriftgrößen und Abstände haben Vorrang. Die Vorschau enthält unverändert 26 Paletten; ihr klassischer weißer Hintergrund entspricht dem Original.

## Widgets und Originalfunktionen

| Familie | Ergänzungen und Bedienung |
| --- | --- |
| Buttons / Icon Buttons | Zustandstexte/-farben/-symbole, Druckfarbe, Taster, begrenzte Addition, neues Fenster, Navigation und zeitliche Entsperrung |
| State Multi | Bisheriger Zyklus oder mehrere Entitäten mit eigenem Wert und Verzögerung |
| Checkbox / Switch | Eigene Ein-/Aus-Werte oder boolescher Modus, Labelposition und echter Switch mit Spur/Griff |
| Input / Select / Autocomplete | Eingabeformen, Anhänge, Untertext/Zähler, Icons, Hover-/Auswahlfarben, Tastatur und Maske: # = Ziffer, A = Buchstabe, * = Buchstabe/Ziffer |
| Slider / Slider Round | Wirksame Griff-/Spurgröße, Grenzen/Schritt, Skala, Working-Entität, Schreiben während Bedienung oder beim Loslassen, Bogen/Startwinkel |
| Progress | Linear/rund, bestimmt/unbestimmt, Größe/Drehung, Schwellenfarben und Werttext |
| Value / Icon / Version | Zahl/Bool/Text/Datum/Dauer, Faktor/Offset, Bedingungen, Link und Änderungseffekt; statisches oder Zustandsicon; tatsächliche Paketversion |
| HTML Card | Titel/Untertitel, Bild, Kartenlayouts, Farben, Bildaktualisierung und isoliertes HTML |
| List / Icon List / Table / Alerts | Subtexte, Navigation/Links/Bedienung, JSON-Statusleisten, Bildspalten, Spaltenformatierung, feste Kopfzeile, Sortierung und Quittierung |
| Vier Diagramme | Balken, Pie/Donut, JSON und Recorder; bis zu vier Y-Achsen, Stacks, Füllung/Stufenlinien, Tooltips, Wertlabels, Paletten und Legendenposition |
| Calendar | Monat/Woche/Tag/Jahr/Liste, Kalenderwochen, Farben und Zeitraster in DE/EN/FR |
| Top App Bar | Modal/permanent/automatisch öffnender Drawer, Untereinträge und ausgewählter Index; bisherige Seitenlinks bleiben ein eigener Modus |
| Grid/Masonry / Advanced Views | Responsive Spalten, Sichtbarkeit je Ansicht, Wertzuordnung/Name/Index, boolesche Indizes 0/1, Vorladen und Erhalten geladener Ansichten |

**Erweiterte Optionen anzeigen** blendet Details ein, ohne beim Ausblenden Werte zu löschen. Für Ziele, Ansichten, Datenreihen oder Menüpunkte die Anzahl setzen.

## Home Assistant und Daten

Geprüfte HA-Aktionen unterstützen <code>switch/input_boolean</code>, <code>number/input_number</code>, <code>text/input_text</code>, <code>select/input_select</code>, <code>button/input_button</code> mit <code>PRESS</code>, Leuchten-Helligkeit, Lüfter-Prozent und Cover-Position. Zustände, Auswahloptionen und Wertebereiche werden geprüft. Sensoren, Attribute und nicht verfügbare Entitäten bleiben Anzeigen.

Mehrziel-Aktionen laufen nacheinander und stoppen bei Fehler oder Seitenwechsel. Bereits ausgeführte Aktionen werden nicht zurückgerollt. Frei eingebbare HA-Dienste und ausführbare ioBroker-Bindings werden nicht übernommen.

Die Top App Bar im **State-Modus** schreibt den Index in ihre Entität. Eine **Advanced View in Widget 8** mit derselben Entität und **Index-Modus** zeigt die zugehörige lokale Studio-Seite. Ohne Entität kann der vorhandene Studio-Datenfluss verbunden werden; getrennte lokale Vorschauwerte werden nicht automatisch geteilt.

Listen lesen Editorzeilen oder JSON; Tabellen nutzen die konfigurierten Spaltenschlüssel. Optionales HTML in Listentexten wird bereinigt: keine Skripte, Event-Handler oder aktiven Einbettungen. HTML-Karten bleiben in einer Sandbox. Zielseiten können fremde iFrames blockieren.

Diagramme lesen <code>axisLabels/graphs</code>, <code>labels/datasets</code> oder Punktlisten. Recorder ist auf **zehn Entitäten und 1–168 Stunden** begrenzt. Die X-Achse berücksichtigt tatsächliche Zeitabstände. Aggregation: keine, Durchschnitt, Minimum, Maximum, Summe oder letzter Wert; Intervall in Minuten. Fehlende Zustände werden nicht erfunden.

Keine automatische ioBroker-Projektübernahme: HA-Entitäten, Recorder und Studio-Seiten ersetzen Objekt-IDs, History-Adapter und VIS-Views. SVG-Diagramme und Renderer sind eigene Umsetzungen; universelle Pixelgleichheit wird nicht zugesichert.

## Prüfung und Veröffentlichung

Browserprüfungen umfassen alle 49 Einträge in DE/EN/FR, Klassisch/Material 3 und Hell/Dunkel sowie Bedienabläufe. Ein Update mit echten Paketdateien erhält alte Projekte bytegenau. Tatsächliche HA-Gerätefunktionen zusätzlich in der eigenen Installation prüfen.

[Vergleichsprojekt](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign/blob/main/comparison/materialdesign-widgetvergleich.json) · [Ausgangsaudit](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign/blob/main/comparison/AUDIT-2026-10-12.md)

Im [Paketkatalog](https://visualstudio.ugso-software.de/?lang=de) **1.1.0**, Mindest-Studio **0.1.292**, ID <code>ugso.materialdesign</code> und MIT registrieren. GitHub-Veröffentlichung bedeutet keine automatische Katalogfreigabe. Prüfsumme: <code>dist/SHA256SUMS</code>.
