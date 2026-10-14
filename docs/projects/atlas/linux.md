---
title: Linux und systemd
description: ATLAS unter Linux installieren, aktualisieren und sichern.
---

# Linux und systemd

Der Linux-Installer ab ATLAS **0.1.298** verwendet denselben kombinierten
App-Server wie Docker und die HA-App. Administration und Card Editor laufen
zusammen; externe Plugins bleiben separat installierbar. Die native
ATLAS-HA/HACS-Frontend-Integration ist eine weitere A7-Aufgabe.

## Voraussetzungen

- Linux mit laufendem systemd, Node.js ab Version 22 und Root-Zugriff für den Installer.
- Ein auf Linux gebautes Paket für die CPU-Architektur, libc und Node-ABI des Zielsystems.
- Drei freie Ports: 4176 für die App, 4175 und 4174 für interne Oberflächen.
- Genügend Platz für mindestens zwei Laufzeitversionen und die Datensicherungen.

AMD64 und ARM64 werden beim Paketbau unterstützt. Der Paketbau verwendet
Debian Bookworm/glibc; ein Alpine/musl-Paket ist dafür nicht austauschbar.
Andere Distributionen und native ARM64-Linux-Installationen benötigen eigene
Qualifikation. Die HA-ARM64-Tests ersetzen diese Prüfung nicht.

Der Installer verwendet den Systembenutzer `atlas`. Existiert dieser schon
mit einem anderen Home-Verzeichnis oder einer anderen Hauptgruppe, bricht er
ab. Er übernimmt keine fremde ATLAS-Installation automatisch.

## Paket vorbereiten

Auf einem Linux-Buildsystem mit den vorhandenen Build-Abhängigkeiten:

```sh
corepack enable
pnpm install --frozen-lockfile
pnpm build
pnpm test:linux
pnpm linux:prepare
```

Das Ergebnis liegt unter `output/linux-runtime`. Das Verzeichnis enthält
die gebaute Anwendung, Abhängigkeiten, das Referenzplugin und
`atlas-linux-runtime.json`. Ein bestehendes Ausgabeverzeichnis wird nicht überschrieben.

Alternativ außerhalb des Ziel-LXC mit Docker bauen:

```sh
docker build -f packaging/linux/Dockerfile --target export --output type=local,dest=output/linux-export .
```

Der Export enthält ein Laufzeitarchiv, Manifest, Prüfsummen und die Node-Datei
mit Lizenz aus dem offiziellen Node-Image. Prüfen Sie die Herkunft und
SHA-256-Werte vor Verwendung. Verwenden Sie eine passende Node-Installation;
ersetzen Sie eine vorhandene Node-Version nicht ungeprüft. Beim Transfer oder
Entpacken bleiben die relativen Symlinks in `node_modules` erhalten.

## Installation

Mit einem geprüften, entpackten Paket und einer passenden Node-Version:

```sh
sudo node /pfad/linux-runtime/scripts/atlas-linux-installer.mjs install --source /pfad/linux-runtime
sudo systemctl status atlas
curl --fail http://127.0.0.1:4176/health
```

Der Installer prüft Paket, Architektur und native Module, erstellt eine
Sicherung, installiert eine eigene Laufzeitversion und startet den Dienst.
Die Bereitschaftsprüfung verlangt beide Oberflächen, die erwartete
App-Version und den Linux-Verteilungstyp. Belegte Ports anderer Dienste
werden nicht durch Abschalten dieser Dienste freigemacht.

## Dauerhafte Daten

| Pfad | Inhalt |
| --- | --- |
| `/opt/atlas/releases/` | Getrennte Laufzeitversionen. |
| `/opt/atlas/current` | Aktuelle Laufzeit als symbolischer Link. |
| `/opt/atlas/installation.json` | Installationsstand und vorherige Laufzeit. |
| `/var/lib/atlas/` | Dauerhafte Daten, Plugins, Identität, Dateihistorie und Papierkorb. |
| `/etc/atlas/atlas.env` | Geschützte Konfiguration; wird bei Updates erhalten. |
| `/etc/systemd/system/atlas.service` | Verwalteter Dienst. |
| `/etc/systemd/system/atlas.service.d/` | Eigene systemd-Ergänzungen. |
| `/var/backups/atlas/` | Zeitgestempelte Sicherungen. |

Editorprojekte und Teile der Administration liegen im Browser. Exportieren
Sie diese zusätzlich in den jeweiligen Oberflächen. Eine Dateisicherung auf
dem Server erfasst keinen Browser-Speicher. Behalten Sie bei Updates dieselbe
Browseradresse, dieselbe Datenablage und dieselbe Installationsidentität bei,
damit lokal gebundene verschlüsselte Zugangsdaten gültig bleiben.
Docker-/HA-Daten werden nicht stillschweigend in eine neue Installation migriert.

## Update und Rückwechsel

```sh
sudo node /pfad/neues-paket/scripts/atlas-linux-installer.mjs update --source /pfad/neues-paket
sudo node /opt/atlas/current/scripts/atlas-linux-installer.mjs rollback
```

Vor dem Update wird der ATLAS-Dienst gestoppt und dessen Datenstand gesichert.
Umgebungsdatei, bestehende Plugins und systemd-Ergänzungen werden erhalten.
Der Wechsel der Laufzeit erfolgt über den aktuellen Link. Scheitert die neue
Laufzeit, wird die vorherige wiederhergestellt. Zuvor gestoppte Installationen
bleiben nach der Prüfung gestoppt; die bisherige Boot-Aktivierung wird nicht geändert.

Der Rückwechsel betrifft den Programmstand. Er stellt nicht automatisch alte
Benutzerdaten wieder her. Bei künftigen Datenmigrationen muss deren Rückwärts-
kompatibilität separat geprüft werden. Alte Releases und Backups werden nicht
automatisch gelöscht. Ändern Sie den verwalteten Dienst nicht direkt;
`systemctl edit atlas` erstellt lokale Ergänzungen.

## Sicherung und Wiederherstellung

```sh
sudo node /opt/atlas/current/scripts/atlas-linux-installer.mjs backup
sudo node /opt/atlas/current/scripts/atlas-linux-installer.mjs status
```

Die Sicherung erfolgt bei gestopptem Dienst und umfasst Daten, Konfiguration,
Dienstdatei, Ergänzungen und Installationsmanifest. Danach startet ein zuvor
aktiver Dienst wieder. Das Backup ist nur für Root zugänglich und kann
Zugangsdaten enthalten. Externe Datenpfade, SSH-Schlüssel außerhalb der
ATLAS-Datenablage und Browserprojekte müssen zusätzlich gesichert werden.

Für eine manuelle Wiederherstellung stoppen Sie ATLAS, sichern den aktuellen
Stand erneut und stellen die ausgewählte Daten-/Konfigurationssicherung am
ursprünglichen Ort mit passenden Besitzrechten wieder her. Bewahren Sie die
Installationsidentität. Stellen Sie den dazu passenden Programmstand bereit
und prüfen Sie danach `/health`. Eine Sicherung auf einer anderen Installation
entsperrt keine dort gebundenen Secrets. Ein VM-/LXC-Snapshot vor der
Erstinstallation bietet zusätzlich die Wiederherstellung des vollständigen Hosts.

## Netzwerk und Plugins

Standardmäßig sind alle Oberflächen nur über Loopback erreichbar, Terminal
ist deaktiviert. Der Installer öffnet keine Firewall. Für einen bewussten
LAN-Betrieb kann der Administrator `ATLAS_APP_HOST` ändern und den Zugriff
gezielt begrenzen; interne Ports bleiben lokal. Die Administration ist eine
Verwaltungsoberfläche und gehört nicht ungeschützt ins Internet.

Bei File Studio müssen Linux-Dateirechte und die genehmigten Pfade
zusammenpassen. Home-Assistant-Dateien auf einem anderen Host werden dadurch
nicht automatisch eingebunden. SSH und Oh My Posh für das externe Terminal
sind zusätzliche, optionale Voraussetzungen und nicht im Linux-Paket enthalten.

## Testumfang

Installer-Regressionsprüfungen verwenden ausschließlich temporäre Testdaten.
Sie prüfen Datenerhalt, Backup, fehlgeschlagenes Update, Rückwechsel,
Dienstzustand, überschreibungsfreie Installation und Pfad-/ABI-Prüfungen.
Ein erfolgreicher Container-Test mit simuliertem Dienst ersetzt keinen
nativen systemd-Test. Native Ergebnisse und noch offene Plattformen stehen im
[Entwicklungsstand](/projects/atlas/entwicklungsstand).
