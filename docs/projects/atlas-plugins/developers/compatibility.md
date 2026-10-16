---
title: Versionen und Kompatibilität
description: Versionsregeln, Datenmigrationen und sichere Updates für ATLAS und Plugins.
---
# Versionen und Kompatibilität

Diese Veröffentlichungsregeln gelten seit dem 15. Oktober 2026. App 0.1.302 ergänzt die automatische Prüfung vor Plugin-Installationen und Updates; 0.1.303 erkennt zusätzlich die verbundene HA-Version. Bestehende Installationen und Datenformate werden nicht migriert.

## Welche Version zählt?

| Version | Bedeutung |
| --- | --- |
| ATLAS App/Runtime | Version des ausgelieferten Docker-, App/Add-on- oder Linux-Pakets. |
| HA-Integration | Version von `atlas_frontend`; ein HACS-Commit wird zusätzlich erfasst. |
| Framework | Eigene Version je `@atlas/*`-Paket; kein Ersatz für die App-Version. |
| Plugin | Eigene Version bei stabiler Plugin-ID; Manifest, Katalog und Paket müssen übereinstimmen. |
| Datenformat | Art und Formatversion gespeicherter Daten; eine Revision zählt Änderungen für die Konfliktprüfung. |

Der Card Editor wird mit ATLAS ausgeliefert. Externe Plugins werden unabhängig aktualisiert. Gleiche Versionsnummern verschiedener Komponenten beweisen keine Kompatibilität.

## Veröffentlichungsregeln

Verwende `MAJOR.MINOR.PATCH`: PATCH für kompatible Fehlerkorrekturen, MINOR für kompatible Funktionen, ab einer stabilen 1.x-Schnittstelle MAJOR für Vertragsbrüche. Vor 1.0 erfordert ein Vertragsbruch eine neue MINOR-Version und Migrationshinweise. Künftige inkompatible Änderungen dürfen deshalb nicht als weiterer 0.1.x-Patch erscheinen. Bestehende Versionen werden nicht umbenannt.

Alpha-Versionen sind ausdrücklich Teststände. Geänderte veröffentlichte Pakete erhalten eine neue Version; reine Dokumentationsänderungen brauchen keine Laufzeitversion. Halte Quell-Commit und geprüfte Kombinationen in den Release-Notizen fest.

## Was prüft ATLAS heute?

Repository-Angaben `compatibility.atlas`, `host` und `homeAssistant` beschreiben beanspruchte Kompatibilität. `atlas` bezieht sich auf die App/Runtime. Seit 0.1.302 prüft der Server die Angaben aus Katalog, Paket und enthaltenem Manifest vor dem Ersetzen gemeinsam. SemVer-Bereiche wie `>=0.1.302 <0.2.0` werden ausgewertet. Ein bekannter Widerspruch oder eine ungültige Voraussetzung blockiert das Paket; die installierte Version bleibt erhalten. Fehlende Angaben bedeuten **ungeprüft** und erfordern eine ausdrückliche Bestätigung. Bestehende Plugins werden nicht deaktiviert.

`host` akzeptiert einen Namen oder eine Liste von Alternativen. `administration-local` bleibt der historische Name für den gemeinsamen Node-Installer; `docker`, `linux` und `homeassistant` passen zum konfigurierten Bereitstellungsziel. Die Bestätigung kann bekannte Inkompatibilität nicht übergehen. Die Vorschau schreibt keine Dateien; beim tatsächlichen Installieren prüft der Server erneut. Auch lokale Paketimporte werden geprüft.

Seit 0.1.303 fragt die Administration die HA-Version über die authentifizierte `/api/config`-Antwort der konfigurierten Verbindung ab. Token und sonstige HA-Konfiguration bleiben im Backend. Bei HA-Anforderungen wird vor Vorschau und Installation neu abgefragt; eine Version aus dem Browser wird nicht übernommen. Fehlende Zugangsdaten, Zeitüberschreitungen, Weiterleitungen, verweigerter Zugriff oder ungültige Antworten bleiben **unbekannt** und erfordern eine ausdrückliche Prüfung. Ein alter erfolgreicher Wert wird nicht weiterverwendet. Beta-, RC- und Entwicklungsversionen bleiben Vorabversionen. Unbekannte Metadatenfelder benötigen weiterhin eine Prüfung. Der lesende Endpunkt `/api/homeassistant/version` liefert nur bereinigte Versionsmetadaten oder einen festen Fehlergrund; er verändert keine Einstellungen oder Projekte.

Die Update-Anzeige vergleicht Versionstexte numerisch; sie ist kein vollständiger SemVer-Prüfer. Kernel-Modulabhängigkeiten unterstützen separat exakte Zahlentripel, `^` und `*`, aber keine allgemeinen Bereiche oder Vorabversionen. Der aktuelle Caret-Abgleich hält bei Version 0 die MINOR-Version gleich; `^0.0.3` akzeptiert dabei auch `0.0.4`. Nutze für solche Module exakte Versionen.

Paket- und Manifest-ID sowie Version werden vor dem Ersetzen geprüft; beim Repository-Update muss auch die Katalogversion stimmen. Deklarierte Fähigkeiten sind keine automatischen Berechtigungen und keine Sandbox. Eine passende Versionsangabe ersetzt keinen Funktionstest oder eine Vertrauensprüfung des Plugins.

## Daten erhalten und wiederherstellen

1. Sichere vor Updates HA und ATLAS-Daten beziehungsweise die eigenständige Installation mit Daten und Installationsidentität. Exportiere lokale Admin-Einstellungen, Editor-Projekte und gemeinsame Plugin-Metadaten zusätzlich. Externe Plugin-Daten und browserlokale Sammlungen brauchen eigene Sicherungen.
2. Behalte Laufzeitadresse, persistente Datenpfade und Identität bei. Verschlüsselte Einstellungen sind dadurch nicht automatisch auf andere Installationen übertragbar. Eine Quellcode-Sicherung ersetzt kein Datenbackup.
3. Aktualisiere eine Komponente nach der anderen; starte HA nach Integrationsupdates wie beschrieben neu. Prüfe anschließend Einstellungen, Projekte und aktive Plugins.
4. Stelle bei Bedarf passenden Programmstand **und** den dazugehörigen Datenstand wieder her. Ein älteres Programm darf neuere unbekannte Formate nicht überschreiben.

Für künftige Datenmigrationen gelten: Vorschau ohne Schreibzugriff, Original sichern, Kopie umwandeln und validieren, ausdrücklich übernehmen, Konflikte prüfen und atomar ersetzen. Unbekannte oder beschädigte Formate dürfen nicht durch leere Daten ersetzt werden. Wiederholungen und Fehler müssen ohne Datenverlust behandelt werden. Diese Regeln sind Anforderungen, keine Behauptung einer bereits vorhandenen universellen Migration.

Ab ATLAS 0.1.304 bleibt vor jedem Ersetzen eine geprüfte Paket-Rücksicherung unter `<ATLAS_PLUGIN_DATA_ROOT>/.recovery` im vorhandenen persistenten Datenpfad erhalten. Dieser Bereich ist nicht als öffentliche Plugin-Datei erreichbar. Im Plugin-Manager ersetzt „Paket importieren“ ein vorhandenes Plugin erst nach Vorschau und „Sichern und übernehmen“. „Wiederherstellen“ zeigt gespeicherte Versionen zur Auswahl. Versionsrichtung und Fähigkeiten sind sichtbar; ungeklärte Kompatibilität braucht eine bewusste Bestätigung, bekannte Inkompatibilität sperrt die Übernahme. Veraltete Vorschauen werden abgewiesen. Dateien und gemeinsamer Plugin-Eintrag werden zusammen übernommen; Aktivierung und Repositories bleiben erhalten. Auch vor einer Wiederherstellung wird die gerade installierte Version gesichert.

Diese Funktion stellt Plugin-Code wieder her. Zugangsdaten, Editor-Projekte, Browser-Sammlungen und Plugin-Datenformate werden nicht zurückgesetzt oder migriert. Vollständige Backups und passende Datenstände bleiben erforderlich. Grenzen je Plugin: 300 Dateien/20 MB pro Sicherung, insgesamt 256 MiB und 200 Sicherungen. Es gibt keine automatische Bereinigung; bei vollen oder unlesbaren Sicherungen wird das Ersetzen gesperrt. Der integrierte Card Editor wird weiterhin nur mit ATLAS aktualisiert. Die nativen Oberflächenprüfungen sind im folgenden Prüfumfang dokumentiert.

## Geprüfter Umfang

Der echte HACS-Integrationswechsel 0.1.301 → 0.1.306 und HA-Neustarts sind auf Pi 5 und Proxmox mit erhaltenen Einstellungen, Projekten und Plugins geprüft. Isoliert bestehen auch Rückkehr und erneutes Update. Das Konfigurationsformat bleibt 1.1; ein unbekanntes Format 1.2 wird ohne Umschreiben abgewiesen. Die Integration ist gegen HA 2026.10.1 sowie zusätzlich isoliert gegen 2026.9.4 geprüft. Weitere Versionen und echte Umwandlungen zwischen unterschiedlichen Datenformaten bleiben offen. Neue Migrationen brauchen Tests mit alten, aktuellen und unbekannten Formaten, Fehlerfällen, Konflikten und Wiederherstellung.

Die Paket-Wiederherstellung in der Oberfläche ist zuerst isoliert und danach auf Pi 5 und Proxmox für Icon Bibliothek, File Studio und Terminal geprüft. Originaldateien, Projekte, andere Plugins und geprüfte Einstellungen bleiben erhalten. Das ist keine generische Rückmigration beliebiger Plugin-Daten. Die getrennte vollständige HAOS-Wiederherstellung mit Papierkorb/Historie und geänderter IP ist im [File-Studio-Leitfaden](../file-studio) dokumentiert.

Die technische [Versionsrichtlinie im Quellrepository](https://github.com/rockbaer2007/atlas/blob/main/docs/project/specifications/VERSION_COMPATIBILITY_POLICY.md) beschreibt die Regeln und Grenzen genauer.
