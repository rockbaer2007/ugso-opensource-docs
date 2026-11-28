---
title: 3D Printer Card
description: Kompakte Home-Assistant-Card für Klipper und Moonraker mit Profilen, Kamera und Temperaturgraphen.
---

# 3D Printer Card

[English](/en/projects/3d-printer-card/) · [Français](/fr/projects/3d-printer-card/)

**Version 0.1.7. Funktioniert nur mit Klipper und Moonraker.** Die [Moonraker-Integration](https://github.com/marcolivierarsenault/moonraker-home-assistant) muss installiert und für jeden Drucker eingerichtet sein. Die Card verwendet deren HA-Entitäten ohne eigene Anmeldung oder zusätzliche Druckerverbindung.

## Installation

[![Im Marketplace öffnen](/images/3d-printer-card/marketplace.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=rockbaer2007&repository=3d-printer-card&category=plugin)

1. Einstellungen sichern. Die [Moonraker-Integration im Marketplace](https://my.home-assistant.io/redirect/hacs_repository/?owner=marcolivierarsenault&repository=moonraker-home-assistant&category=integration) installieren und konfigurieren.
2. `https://github.com/rockbaer2007/3d-printer-card` im Marketplace als benutzerdefiniertes **Dashboard**-Repository hinzufügen und herunterladen. Noch nicht im allgemeinen Marketplace-Katalog gelistet.
3. Ressource `/hacsfiles/3d-printer-card/3d-printer-card.js` als **JavaScript-Modul** prüfen und Browser neu laden. Eine bisherige lokale Ressource ersetzen; nicht beide gleichzeitig laden.
4. Im Dashboard **3D Printer Card** hinzufügen. Der technische Typ bleibt `custom:moonraker-display-card`.

Manuell: JS-Datei aus dem Release nach `/config/www/3d-printer-card/` kopieren und `/local/3d-printer-card/3d-printer-card.js?v=0.1.7` als JavaScript-Modul registrieren. Kein HA-Neustart nötig. Alle Entitäten der Beispielvorlage durch die eigenen ersetzen.

## Anzeige und Profile

- Status, Dateiname, Fortschritt, Druckdauer, Restzeit, geschätzte Gesamtdauer, Fertigstellung und Schichten; außerdem Geschwindigkeit, Lüfter und Meldungen.
- Düse und Bett jeweils Ist/Soll in einem Graphen; Board- und Padtemperatur jeweils Ist im zweiten Graphen. Verläufe benötigen die entsprechenden Entitäten im HA-Recorder.
- Livekamera rechts mit ungefähr einem Drittel der Breite und optionaler Modellvorschau. Auf schmalen Displays untereinander.
- Kompakte Wertefelder, flache Graphen, Standardbreite 24 Spalten, automatische Höhe. Eine HA-Abschnittsansicht verwenden; Panelansichten erzwingen volle Breite.
- Bis zu 20 Druckerprofile mit eigenen Entitäten und Kameras.

Im visuellen Editor **Profil hinzufügen** oder **Profil bearbeiten** öffnen. Über **Drucker erkennen** den `current_print_state`-Sensor wählen; das Entitätspräfix wird erkannt. Kameras und abweichende Zuordnungen über die native HA-Entitätensuche auswählen. **Profil übernehmen**, danach im äußeren Editor **Speichern**. Der Editor ist derzeit Deutsch; Doku DE/EN/FR. Bestehende Profile bleiben kompatibel.

## Bilder aus der Praxis

Die folgenden Screenshots zeigen die Card und den deutschsprachigen Editor. Ein Klick öffnet das jeweilige Bild in voller Größe.

### Übersicht mit Kamera und Temperaturgraphen

[![3D Printer Card für den Ender3 V2: Status, Fortschritt, Zeitangaben, Kamera rechts sowie Temperaturgraphen für Düse, Bett und System](/images/3d-printer-card/card-overview.png)](/images/3d-printer-card/card-overview.png)

### Karteneditor mit Profilwahl und Vorschau

[![Visueller Karteneditor mit Druckerprofil-Auswahl, Profil hinzufügen und Profil bearbeiten sowie der Vorschau rechts](/images/3d-printer-card/card-editor.jpeg)](/images/3d-printer-card/card-editor.jpeg)

### Druckerprofil hinzufügen

[![Dialog zum Hinzufügen eines Druckerprofils mit Profilname, Druckstatus-Entität, erkanntem Präfix, Kamera und Modellvorschaubild](/images/3d-printer-card/profile-add.png)](/images/3d-printer-card/profile-add.png)

### Druckerprofil bearbeiten

[![Bearbeitung des Ender3-V2-Profils mit HA-Entitätenauswahl, Kamera, Modellvorschau und aufklappbaren Zuordnungen für Status, Temperaturen und Druckzeiten](/images/3d-printer-card/profile-edit.png)](/images/3d-printer-card/profile-edit.png)

## Druckabbruch und Prüfung

Einzige Aktion: **Druck abbrechen**, über den vorhandenen HA-Button bei aktivem/pausiertem Druck und betriebsbereitem Drucker. Bestätigung und erneute Zustandsprüfung sind erforderlich. Profilwechsel senden keine Druckerbefehle. Kein Filamentverbrauch und keine Gesamtstatistik.

Mit echten Entitäten unter HA 2026.11.3 geprüft: Anzeige, Kamera, Graphen und Profilbearbeitung bei erhaltenen Einstellungen. Zusätzlich 16 automatisierte Tests und Browserprüfungen mit 390, 800 und 1500 Pixeln ohne Überläufe oder ungewollte Dienstaufrufe. Kein echter laufender Druck wurde im Test abgebrochen.

## Downloads

Kopierfertige Forenbeiträge: [Deutsch](https://github.com/rockbaer2007/3d-printer-card/blob/main/forum/forenbeitrag-de.md) · [English](https://github.com/rockbaer2007/3d-printer-card/blob/main/forum/forum-post-en.md).

- [GitHub und vollständige Anleitung](https://github.com/rockbaer2007/3d-printer-card)
- [Release 0.1.7 mit ZIP und JavaScript](https://github.com/rockbaer2007/3d-printer-card/releases/tag/v0.1.7)
- [Changelog](https://github.com/rockbaer2007/3d-printer-card/blob/main/CHANGELOG.md)

MIT-Lizenz. Eigenständiges Frontend-Projekt, getrennt von der Moonraker-Integration.
