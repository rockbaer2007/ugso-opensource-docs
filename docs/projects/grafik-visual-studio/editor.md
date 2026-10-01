---
title: Editor und Tastenkombinationen
---

# Editor und Tastenkombinationen

## Einstieg

Lege im Menü **Projekte** ein Projekt an und wähle über **Seiten** eine Seite. Stelle die Seitengröße ein, öffne **Widgets** und füge ein Element aus der Palette ein. Mit **Widgets suchen** oben in der Palette filterst du die verfügbaren Widgets nach Name oder Typ; passende Gruppen öffnen sich während der Suche, ohne ihre bisherigen Klappzustände zu ändern. Ein Klick auf ein Widget wählt es aus; rechts erscheinen seine Eigenschaften. Über **Runtime** prüfst du die Ansicht. **Speichern** sichert manuell; unter **Einstellungen → Allgemein** lassen sich Auto-Save und dessen Verzögerung ändern. Die weiteren Tabs **Widget-Pakete** und **Tools** zeigen derzeit noch leere Listen; Paketinstallation folgt später.

In der Widget-Auswahl der oberen Leiste kannst du mehrere Widgets markieren oder die Auswahl aufheben. Die Aktionsleiste bietet Ausschneiden, Kopieren, Einfügen, Duplizieren, Löschen und bis zu 50 Schritte Rückgängig/Wiederholen. Die zehn Ausrichtungsaktionen arbeiten mit mehreren ausgewählten normalen Widgets; das erste ausgewählte Widget ist die Referenz. Bei **Breite** und **Höhe** öffnet langes Drücken (etwa 0,6 Sekunden) eine Eingabe für den gewünschten Pixelwert.

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

Aktiviere **Andockpunkte** in den Eigenschaften eines Ziel-Widgets. Die Punkte an den Seiten können einzeln geschaltet werden; die Gruppen-Checkbox deaktiviert bei Bedarf alle. Die Enden einer SVG-Verbindung lassen sich auf aktive Punkte ziehen. Ein Zwischenpunkt teilt den Pfad in weitere Segmente; nur ein ausdrücklich aktivierter **Sammelpunkt** kann von anderen Linien als Kopplung ausgewählt werden. Eine bloße Kreuzung verbindet Linien nicht. Für die Darstellung stehen unter anderem Linie, Zickzack-/Mehrpunktpfad, Farben, Dicke, Pfeilspitzen, Animation und z-index bereit.

## Sichtbarkeit und Filter

**Generell** und **Sichtbarkeit** sind bei jedem Widget vorhanden und standardmäßig deaktiviert. „Generell“ enthält unter anderem Name, Kommentar, CSS-Klasse, Filterwort und Sperre. Der Editor-Filter kann Widgets anhand des Filterworts ausblenden oder nur passende anzeigen. Die Sichtbarkeit kann in der Runtime einen Home-Assistant-Zustand mit Bedingung und Vergleichswert prüfen; die Gruppenauswertung ist noch offen.
