---
title: Editor und Tastenkombinationen
---

# Editor und Tastenkombinationen

## Einstieg

Ab **0.1.184** unterscheiden Hintergrundfarben die Widget-Sets in der Palette: **Interaktiv** ist olivgrün, **Spezial** blau und **Datenfluss** violett. **Basis** behält seine bisherige Darstellung. Zusätzliche installierte Sets erhalten jeweils eine eigene Farbe. Die Farben gelten für die Auswahlknöpfe der Palette; die Gestaltung eingefügter Widgets bleibt unabhängig.

![Olivgrüne Einträge des interaktiven Widget-Sets](/images/grafik-visual-studio/palette-set-colors.png)

Ab Studio **0.1.115** öffnet ein Rechtsklick auf ein Widget, eine Gruppenlasche oder die freie Editorfläche ein Kontextmenü: **Auswählen**, **Gruppieren**, **Gruppierung aufheben**, **Gruppe bearbeiten**, **Kopieren**, **Ausschneiden**, **Einfügen** und **Löschen**. **Mehr** enthält Duplizieren, Vorder-/Hintergrund, Sperren/Entsperren, Rückgängig/Wiederholen und Widget-Import/Export. Nicht verfügbare Aktionen sind ausgegraut; Escape schließt das Menü, Pfeil hoch/runter navigiert darin. Auswählen bietet alle Widgets und die Widgets unter dem Mauszeiger.

Gruppen behalten die freien Positionen ihrer Mitglieder und werden beim Ziehen eines Mitglieds oder der Gruppenlasche gemeinsam bewegt. Sie werden im Projekt gespeichert; Kopien und Exporte mehrerer ausgewählter Widgets erhalten beim Einfügen beziehungsweise Import unabhängige Gruppen. **Gruppe bearbeiten** erlaubt einzelne Mitglieder zu bearbeiten; **Gruppenbearbeitung beenden** oder ein Klick auf die Gruppenlasche wechselt zurück zur gemeinsamen Auswahl. Gruppierung aufheben erhält Positionen und Größen. Rückgängig/Wiederholen gilt auch für Gruppierung und Bewegung. Gruppen sind flach; SVG-Verbindungslinien können nicht gruppiert werden, und Gruppen mit gesperrten Mitgliedern lassen sich nicht ziehen. Die Runtime zeigt weder Gruppenrahmen noch das Editormenü. Die Gruppierung erzeugt keine Tab-Inhalte und importiert keine VIS2-Widgets.

Lege im Menü **Projekte** ein Projekt an und wähle über **Seiten** eine Seite. Stelle die Seitengröße ein, öffne **Widgets** und füge ein Element aus der Palette ein. Mit **Widgets suchen** oben in der Palette filterst du die verfügbaren Widgets nach Name oder Typ; passende Gruppen öffnen sich während der Suche, ohne ihre bisherigen Klappzustände zu ändern. Ein Klick auf ein Widget wählt es aus; rechts erscheinen seine Eigenschaften. Über **Runtime** prüfst du die Ansicht. **Speichern** sichert manuell; unter **Einstellungen → Allgemein** lassen sich Auto-Save und dessen Verzögerung ändern. Unter **Widget-Pakete** kannst du ab Version 0.1.80 ein lokales `.wg.zip` installieren. Die erste Schnittstelle 0.1 unterstützt geprüfte Text-Widgets mit Eigenschaften; installierte Pakete erscheinen als eigenes Set in der Palette. Seit 0.1.83 dürfen Widget- und Paketbilder geprüfte SVG- oder PNG-Dateien sein; ohne eigenes Widget-Bild erscheint das integrierte SVG-Textsymbol. Das Entfernen ist gesperrt, wenn ein Paket-Widget in einem Projekt verwendet wird. Ab 0.1.82 installiert der Tab **Tools** lokale `.tp.zip`-Pakete. Das erste deklarative Tool zeigt eine Vorschau und ändert nach Bestätigung die Hintergrundfarbe der aktuellen Seite; **Rückgängig** kann die Änderung zurücknehmen. Auch Tool-Bilder dürfen SVG oder PNG sein; Studio-Buttons verwenden SVG-Symbole. GitHub-Installation und Updates folgen später.

In der Widget-Auswahl der oberen Leiste kannst du mehrere Widgets markieren oder die Auswahl aufheben. Die Aktionsleiste bietet Ausschneiden, Kopieren, Einfügen, Duplizieren, Löschen und bis zu 50 Schritte Rückgängig/Wiederholen. Die zehn Ausrichtungsaktionen arbeiten mit mehreren ausgewählten normalen Widgets; das erste ausgewählte Widget ist die Referenz. Bei **Breite** und **Höhe** öffnet langes Drücken (etwa 0,6 Sekunden) eine Eingabe für den gewünschten Pixelwert.

Die Runtime zentriert eine Seite, wenn sie vollständig ins Browserfenster passt. Bei größeren Seiten beginnt sie links oben; horizontale und vertikale Scrollbalken machen die ganze Seite erreichbar, ohne Widget-Koordinaten zu verändern.

## Widget-Auswahl, Kopieren und Löschen

![Widget-Auswahlliste vor der Editorfläche](/images/grafik-visual-studio/widget-menu.png)

Die angehakten Zeilen wählen dieselben Widgets auf der Arbeitsfläche aus. Die Liste bleibt davor sichtbar; **Kopieren** und **Löschen** betreffen alle angehakten Widgets.

![Mehrere eingefügte Widgets gemeinsam verschoben](/images/grafik-visual-studio/multi-move.png)

Ziehe eines der ausgewählten Widgets, um die gesamte Auswahl zu verschieben, auch nach Kopieren und Einfügen. Ausgewählte Verbindungen und Zwischenpunkte bewegen sich mit; gesperrte Widgets verhindern das gemeinsame Verschieben. Rückgängig nimmt den Zug als einen Schritt zurück.

![Löschbestätigung mit fünf Minuten Unterdrückung](/images/grafik-visual-studio/delete-dialog.png)

**Abbrechen** oder Escape beendet das Löschen. Das Häkchen unterdrückt weitere Fragen für fünf Minuten in dieser Editorsitzung. Gelöschte Widgets lassen sich weiterhin mit Rückgängig wiederherstellen.

## Dateien und Bildauswahl

![Dateisuche unterhalb des Studio-Stammordners](/images/grafik-visual-studio/files-search.png)

Der Stammordner ist **/config/www/studio**. Studio legt ihn nach Möglichkeit an; fehlende Schreibrechte werden gemeldet. Auch die Bildauswahl der Widgets verwendet diesen Ordner; öffentliche Pfade beginnen mit **/local/studio/**. Die Suche berücksichtigt alle Unterordner sowie Dateinamen und Pfade ohne Beachtung der Groß-/Kleinschreibung. Ein leeres Suchfeld zeigt wieder den geöffneten Ordner. Bilder einschließlich GIF lassen sich auswählen. Der Wechsel zum übergeordneten Ordner bleibt innerhalb dieses Stammordners.

## Sprache der Oberfläche

Öffne **Einstellungen → Allgemein → Sprache → App-Sprache**, wähle eine Option und klicke auf **Speichern**:

| Auswahl | Anzeige |
| --- | --- |
| **Automatisch (Home Assistant)** | Deutsch, wenn Home Assistant auf Deutsch eingestellt ist; bei jeder anderen Sprache Englisch. Ist die HA-Sprache nicht erreichbar, gilt die Browsersprache mit demselben Deutsch-/Englisch-Rückfall. |
| **Deutsch** | Die Oberfläche bleibt auf Deutsch. |
| **English** | Die Oberfläche bleibt auf Englisch. |

Die Auswahl gilt nur in diesem Browser und bleibt nach einem Neuladen erhalten. Andere Benutzer und Browser behalten ihre eigene Wahl. Die Sprache ändert Oberflächentexte wie Menüs, Dialoge, Widget-Palette und Eigenschaften; selbst vergebene Projekt- und Widget-Namen sowie Widget-Inhalte werden nicht übersetzt.

## Tastatur und Maus

| Aktion | Bedienung |
| --- | --- |
| Rückgängig | `Strg+Z` (macOS: `⌘+Z`) |
| Wiederholen | `Strg+Y` oder `Strg+Umschalt+Z` (macOS: `⌘+Y` oder `⌘+Umschalt+Z`) |
| Widget zur Mehrfachauswahl hinzufügen oder daraus entfernen | `Strg+Umschalt` gedrückt halten und das Widget anklicken |
| Freien Anfangs- oder Endpunkt einer Verbindung verschieben | Punkt mit der Maus ziehen; fokussierten Punkt mit den Pfeiltasten in 1-Pixel-Schritten bewegen |
| Linienpunkt schneller bewegen | Beim Drücken einer Pfeiltaste zusätzlich `Umschalt` halten: 10 Pixel pro Schritt |
| Angedockten Linienpunkt lösen | `Strg` halten und den Punkt ziehen; mit `Strg` plus Pfeiltaste ebenfalls möglich |
| Ganze Verbindungslinie verschieben | Auf die Linie drücken und mit gedrückter Maustaste ziehen; bestehende Andockverbindungen werden dabei gelöst |
| Zwischen- oder Sammelpunkt einfügen | Linie anklicken, „Zwischenpunkt“ oder „Sammelpunkt“ wählen und mit **OK** bestätigen |

Die Kürzel für Rückgängig/Wiederholen gelten, wenn der Fokus nicht in einem Eingabefeld, Textbereich oder Auswahlfeld liegt. Für Ausschneiden, Kopieren und Einfügen stehen Schaltflächen bereit; dafür sind derzeit keine globalen `Strg+X/C/V`-Kürzel eingerichtet.

## Verbindungslinien und Andockpunkte

Aktiviere **Andockpunkte** in den Eigenschaften eines Ziel-Widgets. Bei neuen Widgets sind alle Punkte aus. **Alle Punkte** schaltet die zwölf Positionen gemeinsam; einzelne Punkte können danach angepasst werden. Die Gruppen-Checkbox aktiviert oder deaktiviert den gesamten Bereich. Die Enden einer SVG-Verbindung lassen sich auf aktive Punkte ziehen. Ein Zwischenpunkt teilt den Pfad in weitere Segmente; nur ein ausdrücklich aktivierter **Sammelpunkt** kann von anderen Linien als Kopplung ausgewählt werden. Eine bloße Kreuzung verbindet Linien nicht. Für die Darstellung stehen unter anderem Linie, Zickzack-/Mehrpunktpfad, Farben, Dicke, Pfeilspitzen, Animation und z-index bereit.

## Sichtbarkeit und Filter

**Generell** und **Sichtbarkeit** sind bei jedem Widget vorhanden und standardmäßig deaktiviert. „Generell“ enthält unter anderem Name, Kommentar, CSS-Klasse, Filterwort und Sperre. Der Editor-Filter kann Widgets anhand des Filterworts ausblenden oder nur passende anzeigen. Die Sichtbarkeit kann in der Runtime einen Home-Assistant-Zustand mit Bedingung und Vergleichswert prüfen; die Gruppenauswertung ist noch offen.
