---
title: HA Dashboard
description: Dashboard-Themes, Layoutideen und visuelle Erweiterungen für Home Assistant.
---
# HA Dashboard

Dieser Bereich sammelt Themen rund um Home-Assistant-Dashboards, die keine einzelne Card und keine Integration sind.

## Dashboard-Erweiterungen

| Projekt | Status | Hinweis |
| --- | --- | --- |
| [Dashboard Layout Card V2](https://github.com/rockbaer2007/lovelace-layout-card-v2) | experimentell | Fork der Lovelace layout-card mit eigenen V2-Layouttypen, seitlichem Tab-Menü, optionalem Icon-only-Modus, Submenü-Spalte, Unterseiten, neuen Unterseiten standardmäßig als Sections V2, Home-Eintrag, Theme-Übernahme von der Hauptansicht, Uhr/Datum, optionalen Stunden-/Minutenmarkierungen der Analoguhr, Farben, Rahmen-Opacity, 3D-Rahmen, Trennern mit automatischer Farbübernahme vom vorherigen Trenner, Benachrichtigungs-Popup im Icon-only-Modus, Statuswerten und optionalem Ausblenden von Home-Assistant-Header/Sidebar. |

![Dashboard Layout Card V2 Ansicht](/images/dashboard-layout-card-v2/view.png)

Die V2-Layouts erscheinen in der normalen Home-Assistant-Auswahl für Ansichts-Layouts zusätzlich zu den Standardlayouts.

![Dashboard Layout Card V2 Ansichtsauswahl](/images/dashboard-layout-card-v2/view-layout-selection.png)

Sections-V2-Ansichten verhalten sich im Bearbeitungsmodus nah an der nativen Home-Assistant-Abschnittsansicht. Abschnitte können über den Drei-Striche-Griff verschoben werden; die neue Reihenfolge wird direkt in der Ansicht gespeichert.

<video controls src="/images/dashboard-layout-card-v2/demo.mp4" style="width: 100%; border-radius: 8px;"></video>

Hinweis: Für Menü-Hintergründe funktionieren Hochformat-Bilder besonders gut. Ein praktisches Seitenverhältnis ist ungefähr `1:2,5` Breite:Höhe. Andere Formate sind möglich, werden durch `cover` aber je nach sichtbarer Menüfläche zugeschnitten. Bitte nur eigene Bilder oder Bilder mit passender freier/Open-Source-Lizenz verwenden.

### Benachrichtigung und Statuswerte

Die optionale Benachrichtigungsbox wird oberhalb der Statuswerte im seitlichen Menü angezeigt. Empfohlen ist ein Text-Helfer wie `input_text.dashboard_notification`. Solange die Entity fehlt, leer ist, `unknown` oder `unavailable` meldet, bleibt die Box ausgeblendet. Ist der Helper noch nicht vorhanden, zeigt der Editor eine kurze Anleitung zum Erstellen des Text-Helfers.

![Dashboard Layout Card V2 Helper-Hinweis](/images/dashboard-layout-card-v2/notify-helper-missing.png)

Sobald der Helper Text enthält, erscheint die Meldung im Menü, zum Beispiel für Störungen, Wartungshinweise oder kurze Dashboard-Hinweise. Darunter können bis zu vier Statuswerte angezeigt werden. Numerische Werte werden kompakt mit maximal einer Nachkommastelle formatiert.

![Dashboard Layout Card V2 Benachrichtigung und Statuswerte](/images/dashboard-layout-card-v2/notify-and-status.png)

Bis einschließlich 600 Pixel Bildschirmbreite zeigen die Menütasten nur Icons. Zusätzlich kann der Icon-only-Modus manuell aktiviert werden, zum Beispiel für Kiosk-Tablets oder Wanddisplays. In diesem Modus werden Uhr, Datum und Statuswerte ausgeblendet; Benachrichtigungen bleiben über einen kompakten Hinweisbutton als Popup erreichbar.

Für Menüeinträge können Submenüs angelegt werden. Das Submenü steht als eigene Icon-Spalte neben dem Hauptmenü und zeigt immer nur die Unterseiten des aktuell gewählten Hauptmenüpunktes. Der erste Submenübutton kann als Startseite des Hauptmenüpunktes dienen oder deaktiviert werden, damit direkt zur ersten Unterseite gewechselt wird. Die Subbuttons übernehmen zunächst den Stil des Hauptbuttons; der Submenü-Hintergrund ist separat einstellbar.

Hauptmenü-, Submenü- und Home-Einträge können optional eigene Farben erhalten. Unterstützt werden Icon-Farbe, aktive Icon-Farbe, Icon-Hintergrund, aktiver Icon-Hintergrund, Button-Farbe und aktive Button-Farbe je Eintrag. Leere Felder verwenden weiterhin den globalen Menü-Stil.

Die zugehörigen YAML-Felder sind `icon_color`, `icon_active_color`, `icon_background_color`, `icon_background_active_color`, `tab_color` und `active_tab_color`. Ein Reset-Button setzt bei Bedarf nur diese Farben des jeweiligen Eintrags auf globale Werte zurück; Seite, Pfad, Icon, Submenü und globale Farben bleiben erhalten.

Menü- und Card-Rahmen besitzen eigene Opacity-Regler. Auch Trenner können mit eigener Opacity für Farbe und 3D-Effekt eingestellt werden. Dadurch lassen sich sichtbare Rahmen, transparente Glasoptik und zurückhaltende Kiosk-Layouts genauer abstimmen.

Der globale Style-Tab heißt **Styles Global**. Dort lassen sich zusätzlich die aktive Icon-Feld-Farbe sowie die Opacity der globalen Menü-Hintergrundfarbe und des separaten Submenü-Hintergrunds einstellen. Der separate Tab **Farben** speichert bis zu 20 Farbfavoriten, die anschließend in allen Farbfeldern ausgewählt werden können; der Button **Farben speichern** schreibt nur diese Favoriten, ohne andere offene Editoränderungen zu übernehmen.

Im Tab **Backup** kann der aktuelle Dashboard-Stand als YAML-Datei auf den eigenen PC exportiert werden. Der Export verändert Home Assistant nicht und eignet sich als Sicherung vor größeren Tests oder Designänderungen. Der Tab ist außerdem vorbereitet, damit später ein YAML-Import ergänzt werden kann.

## Themes

| Projekt | Status | Hinweis |
| --- | --- | --- |
| [Frosted Glass Theme](./frosted-glass-theme/) | geprüft | Modernes Home-Assistant-Theme mit Glasoptik, HACS-Installation, card-mod- oder UIX-Voraussetzung und Lite-Versionen. |
| [NeoMorphix UIX](./neomorphix-uix/) | geprüft | Neumorphes Home-Assistant-Theme mit Light-, Dark-, Claude- und Inset-Varianten; UIX-Varianten sind als PR vorgeschlagen. |

## Abgrenzung

- Einzelne Lovelace-/HACS-Karten stehen unter [HA Cards](./ha-cards).
- Integrationen stehen unter [HA Integrationen](./ha-integrationen).
- Allgemeine externe Beispiele stehen unter [Weitere interessante Beispiele](./weitere-beispiele).
