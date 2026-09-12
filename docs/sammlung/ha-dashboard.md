---
title: HA Dashboard
description: Dashboard-Themes, Layoutideen und visuelle Erweiterungen für Home Assistant.
---
# HA Dashboard

Dieser Bereich sammelt Themen rund um Home-Assistant-Dashboards, die keine einzelne Card und keine Integration sind.

## Dashboard-Erweiterungen

| Projekt | Status | Hinweis |
| --- | --- | --- |
| [Dashboard Layout Card V2](https://github.com/rockbaer2007/lovelace-layout-card-v2) | experimentell | Fork der Lovelace layout-card mit eigenen V2-Layouttypen, seitlichem Tab-Menü, Unterseiten, neuen Unterseiten standardmäßig als Sections V2, Home-Eintrag, Theme-Übernahme von der Hauptansicht, Uhr/Datum, optionalen Stunden-/Minutenmarkierungen der Analoguhr, Farben, 3D-Rahmen, Trennern mit automatischer Farbübernahme vom vorherigen Trenner, Benachrichtigungsbox, Statuswerten und optionalem Ausblenden von Home-Assistant-Header/Sidebar. |

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

## Themes

| Projekt | Status | Hinweis |
| --- | --- | --- |
| [Frosted Glass Theme](./frosted-glass-theme/) | geprüft | Modernes Home-Assistant-Theme mit Glasoptik, HACS-Installation, card-mod- oder UIX-Voraussetzung und Lite-Versionen. |
| [NeoMorphix UIX](./neomorphix-uix/) | geprüft | Neumorphes Home-Assistant-Theme mit Light-, Dark-, Claude- und Inset-Varianten; UIX-Varianten sind als PR vorgeschlagen. |

## Abgrenzung

- Einzelne Lovelace-/HACS-Karten stehen unter [HA Cards](./ha-cards).
- Integrationen stehen unter [HA Integrationen](./ha-integrationen).
- Allgemeine externe Beispiele stehen unter [Weitere interessante Beispiele](./weitere-beispiele).
