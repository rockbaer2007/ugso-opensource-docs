---
title: Versionen und Kompatibilität
description: Versionsregeln, Datenmigrationen und sichere Updates für ATLAS und Plugins.
---
# Versionen und Kompatibilität

Diese Veröffentlichungsregeln gelten seit dem 15. Oktober 2026. Sie ändern keine vorhandenen Installationen oder Datenformate. Eine automatische Kompatibilitätssperre ist noch nicht implementiert.

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

Repository-Angaben `compatibility.atlas`, `host` und `homeAssistant` beschreiben beanspruchte Kompatibilität. `atlas` bezieht sich auf die App/Runtime. Diese Angaben werden angezeigt, aber noch nicht als Installationssperre durchgesetzt. Fehlende Angaben bedeuten **ungeprüft**. Bestehende Plugins bleiben verwendbar.

Die Update-Anzeige vergleicht Versionstexte numerisch; sie ist kein vollständiger SemVer-Prüfer. Kernel-Modulabhängigkeiten unterstützen separat exakte Zahlentripel, `^` und `*`, aber keine allgemeinen Bereiche oder Vorabversionen. Der aktuelle Caret-Abgleich hält bei Version 0 die MINOR-Version gleich; `^0.0.3` akzeptiert dabei auch `0.0.4`. Nutze für solche Module exakte Versionen.

Paket- und Manifest-ID sowie Version werden vor dem Ersetzen geprüft. Deklarierte Fähigkeiten sind keine automatischen Berechtigungen und keine Sandbox. Eine spätere Kompatibilitätsprüfung muss auch serverseitig vor dem Ersetzen greifen und bestehende Pakete ohne neue Metadaten berücksichtigen.

## Daten erhalten und wiederherstellen

1. Sichere vor Updates HA und ATLAS-Daten beziehungsweise die eigenständige Installation mit Daten und Installationsidentität. Exportiere lokale Admin-Einstellungen, Editor-Projekte und gemeinsame Plugin-Metadaten zusätzlich. Externe Plugin-Daten und browserlokale Sammlungen brauchen eigene Sicherungen.
2. Behalte Laufzeitadresse, persistente Datenpfade und Identität bei. Verschlüsselte Einstellungen sind dadurch nicht automatisch auf andere Installationen übertragbar. Eine Quellcode-Sicherung ersetzt kein Datenbackup.
3. Aktualisiere eine Komponente nach der anderen; starte HA nach Integrationsupdates wie beschrieben neu. Prüfe anschließend Einstellungen, Projekte und aktive Plugins.
4. Stelle bei Bedarf passenden Programmstand **und** den dazugehörigen Datenstand wieder her. Ein älteres Programm darf neuere unbekannte Formate nicht überschreiben.

Für künftige Datenmigrationen gelten: Vorschau ohne Schreibzugriff, Original sichern, Kopie umwandeln und validieren, ausdrücklich übernehmen, Konflikte prüfen und atomar ersetzen. Unbekannte oder beschädigte Formate dürfen nicht durch leere Daten ersetzt werden. Wiederholungen und Fehler müssen ohne Datenverlust behandelt werden. Diese Regeln sind Anforderungen, keine Behauptung einer bereits vorhandenen universellen Migration.

Der Paketinstaller stellt bei einem fehlgeschlagenen Verzeichnistausch den vorherigen Stand wieder her; nach Erfolg behält er ihn nicht als Rückkehrarchiv. Die gemeinsame Plugin-Sicherung enthält Metadaten, nicht alle Paketdateien und Plugin-Daten.

## Geprüfter Umfang

HACS-Commit-Update und HA-Neustart sind auf Pi 5 und Proxmox mit erhaltenen Einstellungen, Projekten und Plugins geprüft. Dabei blieb die Integration bei 0.1.301 und unverändertem Integrationscode. Ein echter Versions-/Schemawechsel und weitere HA-Versionen bleiben zu prüfen. Neue Migrationen brauchen Tests mit alten, aktuellen und unbekannten Formaten, Fehlerfällen, Konflikten und Wiederherstellung.

Die technische [Versionsrichtlinie im Quellrepository](https://github.com/rockbaer2007/atlas/blob/main/docs/project/specifications/VERSION_COMPATIBILITY_POLICY.md) beschreibt die Regeln und Grenzen genauer.
