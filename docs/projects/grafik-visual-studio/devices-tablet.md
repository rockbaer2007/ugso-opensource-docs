---
title: Geräte und Tablet
description: Geräte-Kacheln, Grundriss-Marker, Tablet-Rückkehr und Paketfähigkeiten ab Studio 0.1.297.
---

# Geräte und Tablet

Ab **Studio 0.1.297** enthält die Palette das integrierte Set **Geräte**. Keine zusätzliche Paketinstallation erforderlich. [GitHub-Update](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/grafik-visual-studio-v0.1.297).

## Geräte hinzufügen

Das Set aufklappen, ein Widget auf die Editorfläche ziehen und in den Eigenschaften die HA-Entität auswählen. **Schalter, Dimmer, farbiges Licht, Thermostat und Messwert** stehen jeweils als **Kachel** und **Grundriss-Marker mit Popup** bereit: insgesamt zehn Einträge. Position und Größe sind frei einstellbar; dies ist kein automatisches responsives Raster. Die fünf Standard-CSS-Gruppen stehen zur Verfügung, neue optionale Gruppen bleiben deaktiviert. Widget-Sprache: DE/EN/FR, allgemeine Studio-Oberfläche: DE/EN.

![Geräte-Kacheln und Grundriss-Marker, lokale Demo](/images/grafik-visual-studio/devices-desktop-297.jpg)

| Widget | Quelle und Bedienung |
| --- | --- |
| Schalter | `switch`, `light` oder `input_boolean`; ein/aus |
| Dimmer | `light`; Helligkeit nur bei passender HA-Fähigkeit |
| Farbiges Licht | `light`; ein/aus, Helligkeit und RGB je nach unterstütztem Farbmodus |
| Thermostat | `climate`; einzelner Temperatursollwert innerhalb nativer Grenzen/Schrittweite |
| Messwert | Zustand und Einheit; ausschließlich lesend |

Die Runtime bietet nur von der Entität unterstützte Bedienelemente an. **Nur lesen** sperrt Schreibaktionen. Im Editor werden keine Geräte geschaltet; nicht verfügbare Entitäten sind deaktiviert. Die Serverprüfung bleibt aktiv. Eine angenommene Anfrage ist noch keine physische Gerätebestätigung. Für erweiterte Climate-Funktionen wie Temperaturbereiche weiterhin [Technic/Climate](./ha-quellen-climate) verwenden.

## Tablet-Rückkehr und Startseite

Unter **Einstellungen → Allgemein** aktualisiert **Zustände bei Tablet-Rückkehr aktualisieren** die HA-Werte beim Wiederanzeigen, bei Seitenwiederherstellung und nach erneuter Netzwerkverbindung. Die gesamte Seite wird dafür nicht neu geladen. Browser/Tablet dürfen ihre Timer im Hintergrund aussetzen; beim Zurückkehren wird dies berücksichtigt.

**Startseite nach Inaktivität** und **Inaktivitäts-Startseite** bestimmen Zeit und sichtbare Zielseite im aktuellen Projekt. **0 Sekunden = aus** und bleibt die Voreinstellung. Offene Dialoge, laufende Schreibaktionen und aktive Bearbeitung verschieben die automatische Navigation. Keine Kiosk- oder Zugriffsrechte werden verändert.

![Geräteansicht bei 1280 × 800, lokale Demo](/images/grafik-visual-studio/devices-tablet-297.jpg)

![Licht-Popup auf dem Tablet, lokale Demo](/images/grafik-visual-studio/devices-tablet-popup-297.jpg)

## Live-Werte in Überschriften

Rahmen- und Geräteüberschriften können optional einen HA-Zustand oder ein Attribut mit Nachkommastellen und Einheit anzeigen. Entität und gegebenenfalls Attribut in der entsprechenden Eigenschaftsgruppe wählen. Bestehende Überschriften bleiben erhalten; HA-Werte werden als Text eingefügt.

## Renderer und Paketfähigkeiten

Geräte, Wetter, Heizräume, Fensterübersicht, Vermieterbenachrichtigung, Technic-Statusliste und Material-Farbschemata laden ihre Renderer bei Bedarf. Gemeinsame Editor-Module bleiben normal geladen. Gleichzeitige Anforderungen verwenden denselben Ladevorgang.

Installierte Paketmanifeste werden alle **30 Sekunden** und bei Rückkehr geprüft. Änderungen aktualisieren die Palette ohne Neustart. Dies installiert keine angebotenen Katalog-Updates automatisch. Fehlerhafte Ersetzungen behalten den bisherigen Katalog; entfernte Definitionen bleiben für bereits offene Projekte im Speicher, aber stehen nicht mehr für neue Widgets in der Palette. Projekte werden nicht automatisch migriert. Siehe [Paketinstallation](./widget-pakete).

`optionalCapabilities` im Manifest ist ein freiwilliger Hinweis: `entity-state`, `history`, `light-color`, `climate`. Die Paketliste zeigt unterstützt/nicht unterstützt. Unbekannte Fähigkeiten erteilen keine Berechtigungen. Alte Manifeste bleiben gültig; tatsächliche Steuerung hängt weiterhin von HA und den jeweiligen Entitätsfähigkeiten ab.

![Paketimport mit zwei Widgets und Fähigkeitsanzeige auf .177](/images/grafik-visual-studio/package-import-297.jpg)

## Prüfung und Grenzen

Am **8. November 2026** auf **.177 / HA 2026.11.0 / Raspberry Pi 5 ARM64** und **.193 / HA 2026.10.4 / Proxmox amd64** geprüft: Projekt speichern/erneut laden, tatsächliches Schalten eines temporären HA-Helfers mit Rückmeldung sowie Inaktivitäts-Rückkehr. Auf .177 zusätzlich Marker-Dialog und manueller lokaler Paketimport 1.1.0 mit zwei Widgets und Fähigkeitsanzeige. Testpaket und Testhelfer danach entfernt; Inaktivität wieder auf 0 Sekunden. Studio bleibt auf beiden Systemen installiert, bestehende Projekte/Einstellungen erhalten.

Helligkeit, RGB und Thermostat wurden mit lokalen simulierten Entitäten geprüft. Die neuen Ansichten wurden im Desktop-Browser bei 1440 × 1000 und mit Tablet-Ansicht 1280 × 800 kontrolliert. Das bestätigt keinen Test auf echter Tablet-Hardware oder mit jedem Lampen-/Heizungstyp. 394 JavaScript- und 109 Python-Prüfungen bestanden; ergänzend 7 gezielte JavaScript- und 17 Paket-Python-Prüfungen. [Technischer Prüfbericht](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/devices-tablet-0.1.297.md).

Eigenständige HA-Umsetzung ohne übernommenen VIS-2-Code oder -Grafiken. Web Components und ein responsiver Rastercontainer bleiben getrennte Folgevorhaben.
