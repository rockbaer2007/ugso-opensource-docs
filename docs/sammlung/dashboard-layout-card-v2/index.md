---
title: Dashboard Layout Card V2
description: Dashboard Layout Card V2 für Home Assistant mit Seitenmenü, Submenüs, Sections V2, Kiosk-Optionen, Backup-Export und mehrsprachigem Editor.
---
# Dashboard Layout Card V2

Die **Dashboard Layout Card V2** ist ein parallel installierbarer Fork der bekannten Lovelace `layout-card`. Sie überschreibt die originale Card nicht und bringt eigene `*-v2` Layouttypen, ein seitliches Dashboard-Menü, Submenüs, Kiosk-Optionen und einen erweiterten Editor für Home-Assistant-Dashboards mit.

| Feld | Wert |
| --- | --- |
| Repository | [rockbaer2007/lovelace-layout-card-v2](https://github.com/rockbaer2007/lovelace-layout-card-v2) |
| Status | experimentell, nutzbar |
| Installation | HACS als benutzerdefiniertes Frontend-Repository |
| Kategorie | HA Dashboard -> Dashboard-Erweiterungen |

## Überblick

Die Card ist weniger eine einzelne Lovelace-Karte als eine Dashboard-/Ansichts-Erweiterung. Ziel ist ein flexibles Home-Assistant-Dashboard mit seitlichem Menü, Unterseiten und einer kompakten Darstellung für Tablets oder Kiosk-Displays.

Wichtige Funktionen:

- eigene V2-Layouttypen: `sections-layout-v2`, `masonry-layout-v2`, `horizontal-layout-v2`, `vertical-layout-v2`, `grid-layout-v2`
- seitliches Menü links oder rechts
- optionaler Icon-only-Modus für Mobile, Tablet und Kiosk
- Submenü-Spalte pro Hauptmenüpunkt
- Home-Eintrag und Unterseiten/Subviews
- neue Unterseiten standardmäßig als Sections V2
- Theme-Übernahme von der Hauptansicht
- digitale oder analoge Uhr, Datum und Wochentag
- Benachrichtigungs-Popup und Statuswerte
- globale Styles, individuelle Button-Farben und Farbfavoriten
- Opacity-Regler für Menü-, Card-, Benachrichtigungs-, Status- und Trennerrahmen
- YAML-Backup-Export im Editor
- optionale Sprachumschaltung per YAML für Screenshots
- optionales Ausblenden von Home-Assistant-Header und Sidebar

![Dashboard Layout Card V2 Ansicht](/images/dashboard-layout-card-v2/view.png)

Die V2-Layouts erscheinen in der normalen Home-Assistant-Auswahl für Ansichts-Layouts zusätzlich zu den Standardlayouts.

![Dashboard Layout Card V2 Ansichtsauswahl](/images/dashboard-layout-card-v2/view-layout-selection.png)

Sections-V2-Ansichten verhalten sich im Bearbeitungsmodus nah an der nativen Home-Assistant-Abschnittsansicht. Abschnitte können über den Drei-Striche-Griff verschoben werden; die neue Reihenfolge wird direkt in der Ansicht gespeichert.

<video controls src="/images/dashboard-layout-card-v2/demo.mp4" style="width: 100%; border-radius: 8px;"></video>

## Installation über HACS

Repository als benutzerdefiniertes Frontend-Repository hinzufügen:

```text
https://github.com/rockbaer2007/lovelace-layout-card-v2
```

Danach sollte Home Assistant diese Ressource laden:

```text
/hacsfiles/lovelace-layout-card-v2/dashboard-layout-card-v2.js
```

Wenn nach einem Update noch eine alte Version angezeigt wird:

- HACS-Repositories aktualisieren
- Browser-Cache leeren
- Dashboard hart neu laden

## Benötigte Helper

Es müssen nur die Helper angelegt werden, deren Funktion im Menü genutzt wird. Die Helper werden in Home Assistant unter **Einstellungen > Geräte & Dienste > Helfer** erstellt.

| Entity | Helper-Typ | Zweck | Pflicht? |
| --- | --- | --- | --- |
| `input_text.dashboard_notification` | Text | Optionaler Benachrichtigungstext im Dashboard. Leer, `unknown` und `unavailable` blenden die Meldung aus. | Nur wenn `menu.notify.enabled` genutzt wird. |
| `input_boolean.dashboard_holiday` | Umschalter | Optionales Tages-Symbol für Feiertage. | Nur wenn das Tages-Symbol auf Feiertage reagieren soll. |
| `input_boolean.dashboard_birthday` | Umschalter | Optionales Tages-Symbol für Geburtstage. | Nur wenn das Tages-Symbol auf Geburtstage reagieren soll. |
| `input_boolean.dashboard_christmas` | Umschalter | Optionales Tages-Symbol für Advent/Weihnachten. | Nur wenn das Tages-Symbol auf Advent/Weihnachten reagieren soll. |

Statuswerte benötigen keine speziellen Helper. Dort können beliebige lesbare Home-Assistant-Entitäten verwendet werden, zum Beispiel Sensoren, Binary-Sensoren oder Template-Sensoren.

![Dashboard Layout Card V2 Helper-Hinweis](/images/dashboard-layout-card-v2/notify-helper-missing.png)

## Benachrichtigung und Statuswerte

Die optionale Benachrichtigungsbox wird oberhalb der Statuswerte im seitlichen Menü angezeigt. Empfohlen ist ein Text-Helfer wie `input_text.dashboard_notification`. Solange die Entity fehlt, leer ist, `unknown` oder `unavailable` meldet, bleibt die Box ausgeblendet. Ist der Helper noch nicht vorhanden, zeigt der Editor eine kurze Anleitung zum Erstellen des Text-Helfers.

Sobald der Helper Text enthält, erscheint die Meldung im Menü, zum Beispiel für Störungen, Wartungshinweise oder kurze Dashboard-Hinweise. Darunter können bis zu vier Statuswerte angezeigt werden. Numerische Werte werden kompakt mit maximal einer Nachkommastelle formatiert.

Im Icon-only-Modus werden Uhr, Datum und Statuswerte ausgeblendet; Benachrichtigungen bleiben über einen kompakten Hinweisbutton als Popup erreichbar.

![Dashboard Layout Card V2 Benachrichtigung und Statuswerte](/images/dashboard-layout-card-v2/notify-and-status.png)

## Menü, Submenüs und Farben

Bis einschließlich 600 Pixel Bildschirmbreite zeigen die Menütasten automatisch nur Icons. Zusätzlich kann der Icon-only-Modus manuell aktiviert werden, zum Beispiel für Kiosk-Tablets oder Wanddisplays.

Für Menüeinträge können Submenüs angelegt werden. Das Submenü steht als eigene Icon-Spalte neben dem Hauptmenü und zeigt immer nur die Unterseiten des aktuell gewählten Hauptmenüpunktes. Der erste Submenübutton kann als Startseite des Hauptmenüpunktes dienen oder deaktiviert werden, damit direkt zur ersten Unterseite gewechselt wird. Die Subbuttons übernehmen zunächst den Stil des Hauptbuttons; der Submenü-Hintergrund ist separat einstellbar.

Hauptmenü-, Submenü- und Home-Einträge können optional eigene Farben erhalten. Unterstützt werden Icon-Farbe, aktive Icon-Farbe, Icon-Hintergrund, aktiver Icon-Hintergrund, Button-Farbe und aktive Button-Farbe je Eintrag. Leere Felder verwenden weiterhin den globalen Menü-Stil.

Die zugehörigen YAML-Felder sind `icon_color`, `icon_active_color`, `icon_background_color`, `icon_background_active_color`, `tab_color` und `active_tab_color`. Ein Reset-Button setzt bei Bedarf nur diese Farben des jeweiligen Eintrags auf globale Werte zurück; Seite, Pfad, Icon, Submenü und globale Farben bleiben erhalten.

Menü-, Card-, Benachrichtigungs- und Statusrahmen besitzen eigene Opacity-Regler. Auch Trenner können mit eigener Opacity für Farbe und 3D-Effekt eingestellt werden. Dadurch lassen sich sichtbare Rahmen, transparente Glasoptik und zurückhaltende Kiosk-Layouts genauer abstimmen.

## Editor-Tabs

Das Editorfenster öffnet standardmäßig breiter mit 80 Prozent der Ansichtsbreite und kann per Doppelklick auf den oberen Rand auf 95 Prozent erweitert werden.

| Tab | Optionen |
| --- | --- |
| Menü | Menüposition (`left`, `none`, `right`), Menütitel und globaler Icon-only-Modus für Kiosk-/Tablet-Layouts. |
| Hauptseite | Hauptseite anzeigen oder ausblenden, Titel, Pfad, Icon, eigene Home-Farben für Icon und Button, maximale Sections-V2-Spalten, dichte Abschnittsplatzierung, zusätzlicher Platz oben und Theme-Übernahme von der Hauptansicht. |
| Anzeige | Uhrmodus (`none`, `digital`, `analog`), Stundenmarkierungen, Minutenmarkierungen und Sekundenzeiger der Analoguhr, Datum anzeigen, Wochentag (`none`, `short`, `long`), Wochenendfarbe, Uhr-/Ringfarbe, Analogfarben für Teilungen und Zeiger, Holiday-/Birthday-/Christmas-Helper sowie Größe des Tages-Symbols. |
| Seiten | Hauptmenü-Seiten, Abstände und Trenner; Titel, Pfad, Icon, Layouttyp, maximale Spalten, eigene Farben je Eintrag, Zurücksetzen auf globale Farben, Verhalten des ersten Submenübuttons, Trennerfarbe, Trenner-3D-Farbe, Trenner-Opacity und Trennerhöhe. |
| Submenü | Unterseiten der ausgewählten Hauptseite mit Titel, Pfad, Icon, Layouttyp, maximalen Spalten, eigenen Farben je Eintrag und Zurücksetzen auf globale Farben. Der Tab erscheint, wenn der ausgewählte Haupteintrag Unterseiten besitzt. |
| Meldungen | Optionales Benachrichtigungs-Popup über Text-Helfer, Rahmenfarbe und Opacity der Benachrichtigung, optionale Statuswerte mit bis zu vier Entity-Zeilen, Labels, Einheiten, Status-Rahmenfarbe und Status-Rahmen-Opacity. |
| Styles Global | Uhrgröße, Datumgröße, Umbruchgröße für langen Wochentag, Tab-/Text-/Hoverfarben, Menürahmenfarbe und Opacity, Tab-3D-Farbe, Card-/Inhaltsrahmenfarbe und Opacity, Card-3D-Farbe, gemeinsamer 3D-Versatz, Icon-Farbe, aktive Icon-Farbe, Icon-Feld-Farbe, aktive Icon-Feld-Farbe, Icon-Form, Icon-Größe, Menü-Hintergrundmodus (`none`, `color`, `image`), Menü-Hintergrundfarbe und Opacity, Menü-Hintergrundbild, Submenü-Hintergrundfarbe und Submenü-Hintergrund-Opacity. |
| Farben | Bis zu 20 wiederverwendbare Farbfavoriten. Der Button **Farben speichern** speichert nur diese Favoriten. |
| Backup | YAML-Export des aktuellen Dashboard-Editorstands auf den eigenen PC. |
| Erweitert | Home-Assistant-Chrome-Einstellungen, Admin-Bedienelemente optional dauerhaft sichtbar, Liste sichtbarer Benutzer und JSON-Spezialoptionen für Seitendaten. |

## YAML-Backup

Im Tab **Backup** kann der aktuelle Dashboard-Stand als YAML-Datei auf den eigenen PC exportiert werden. Der Export verändert Home Assistant nicht und eignet sich als Sicherung vor größeren Tests oder Designänderungen. Der Tab ist außerdem vorbereitet, damit später ein YAML-Import ergänzt werden kann.

## YAML-Sprachumschaltung für Screenshots

Für Dokumentations-Screenshots oder Sprachtests kann die angezeigte Sprache direkt im YAML erzwungen werden. Diese Option ist absichtlich nicht im Editor sichtbar.

```yaml
debug:
  language: de # de, en oder fr
```

Ohne `debug.language` nutzt die Card automatisch die Home-Assistant- oder Browser-Sprache und fällt auf Englisch zurück. Wenn der View-Editor geöffnet wird und der Eintrag fehlt, schreibt er einen leeren Platzhalter, der direkt im YAML gefüllt werden kann.

## Hintergrundbilder

Für Menü-Hintergründe funktionieren Hochformat-Bilder besonders gut. Ein praktisches Seitenverhältnis ist ungefähr `1:2,5` Breite:Höhe. Andere Formate sind möglich, werden durch `cover` aber je nach sichtbarer Menüfläche zugeschnitten.

Die Bilder müssen in Home Assistant unter `www` liegen, zum Beispiel:

```text
/config/www/image/back2.jpg
```

Im Editor wird dann verwendet:

```text
/local/image/back2.jpg
```

Bitte nur eigene Bilder oder Bilder mit passender freier/Open-Source-Lizenz verwenden.

## Beispiel

```yaml
views:
  - type: custom:sections-layout-v2
    path: home
    title: Home
    icon: mdi:home
    debug:
      language:
    layout:
      dashboard_layout_v2:
        inherit_theme: true
        menu:
          position: left
          title: House
          show_home: true
          icon_only: false
          home:
            title: Home
            path: home
            icon: mdi:home
          clock: analog
          analog_hour_marks: false
          analog_seconds: false
          date: true
          weekday: long
          style:
            icon_color: "#fbff00"
            icon_background_color: "#ffffff"
            icon_shape: circle
            icon_size: 28px
            active_tab_color: "#333aff"
            inactive_tab_color: "#191c3e"
            tab_border_color: "#fdf9d3"
            card_border_color: "transparent"
            background_mode: image
            background_image: /local/image/back2.jpg
        pages:
          - title: Basement
            path: basement
            icon: mdi:home-floor-negative-1
            layout_type: custom:sections-layout-v2
            max_columns: 3
          - type: divider
            color: "#ffffff"
            divider_opacity: 100
          - title: Garden
            path: garden
            icon: mdi:flower
            layout_type: custom:sections-layout-v2
            max_columns: 4
    sections:
      - type: grid
        cards: []
```
