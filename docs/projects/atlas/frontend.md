# ATLAS im Home-Assistant-Frontend

Ab **0.1.299** enthält ATLAS die optionale Integration **ATLAS Runtime**.
Sie registriert einen eigenen Seitenleisteneintrag für HA-Administratoren.
Darin öffnen sich Plugin Hub, Expert Card Editor und Administration der
vorhandenen ATLAS-Laufzeit. Die Oberfläche folgt der HA-Sprache DE/EN/FR
und der hellen oder dunklen Darstellung.

## Voraussetzungen und Datenerhalt

Stand 16.10.2026: **App 0.1.312**, **Integration 0.1.306**. Die Versionsnummern
sind unabhängig. Die unten genannten Einführungs- und Prüfversionen sind keine
Aufforderung, eine vorhandene neuere App zurückzusetzen. Vollständiger HAOS-Restore
und ein bewusster Adresswechsel sind im [Sicherungsleitfaden](../atlas-plugins/file-studio)
beschrieben; browserlokale Daten brauchen weiterhin einen eigenen Export.

ATLAS muss bereits als App/Add-on, Docker-Container oder
[Linux/systemd-Dienst](/projects/atlas/linux) laufen. HACS installiert die
HA-Integration; der Node-Server und externe Plugins bleiben in ihrer Laufzeit.
Der bestehende Add-on-Ingress-Eintrag wird nicht ersetzt.

Sichere HA vor der Installation. Exportiere bestehende ATLAS-Projekte und
Administrationseinstellungen zusätzlich in ATLAS. Behalte die bisherige
Browseradresse der Laufzeit bei: Browserprojekte, Cookies und verschlüsselte
Einstellungen sind an Adresse beziehungsweise Installationsidentität gebunden.
Ein Wechsel von Hostname, Schema oder Port ist keine automatische Datenmigration.

Browser können den Speicher einer extern eingebetteten Laufzeit zusätzlich
von ihrem separat geöffneten Speicher trennen. Falls vorhandene Projekte oder
verschlüsselte Einstellungen im Panel fehlen, öffne die bisherige Adresse
über **Separat öffnen** und exportiere sie dort; die Integration verschiebt
oder löscht diese Daten nicht. [Hintergrund zur Speichertrennung](https://privacysandbox.google.com/cookies/storage-partitioning).

## Installation über HACS

1. Öffne HACS und seine benutzerdefinierten Repositories.
2. Füge `https://github.com/rockbaer2007/atlas` mit Typ **Integration** hinzu.
3. Lade **ATLAS Runtime** herunter und starte Home Assistant neu.
4. Öffne **Einstellungen → Geräte & Dienste → Integration hinzufügen → ATLAS Runtime**.
5. Trage die im Browser erreichbare Basisadresse der bisherigen Laufzeit ein,
   zum Beispiel `http://atlas-server:4176/` oder `https://atlas.example.org/atlas/`.

Keine HA-Tokens oder Provider-Schlüssel werden in dieser Integration abgefragt.
Die HA-Verbindung bleibt in der ATLAS-Administration. Der Panelcode überträgt
keine HA-Authentifizierung oder Entitätsdaten an das eingebettete Fenster.
Normale HA-Zustandsupdates laden dieses Fenster nicht erneut.

Dies ist ein benutzerdefiniertes HACS-Repository; eine Aufnahme in den
allgemeinen HACS-Katalog wird nicht behauptet. Der Repositorytyp ist
**Integration**, nicht Dashboard. Exportierte HACS-Kartenpakete sind ein
separater Workflow.

### HACS meldet „Unknown error“

Prüfe den zugehörigen Eintrag unter **Einstellungen → System → Protokolle**.
Beim ersten Proxmox-Download wurde in `hacs_repository_download` der Fehler
`AttributeError: 'NoneType' object has no attribute 'data'` beobachtet:
HACS fand seinen Repository-Eintrag nicht, noch bevor der Paketdownload begann.
Lade die HACS-Seite neu, öffne **ATLAS Runtime** erneut und wiederhole den
Download. Im geprüften Fall erschien danach **Ausstehender Neustart**.
Diese Meldung bestätigt den Download; die Einrichtung nach dem HA-Neustart
ist ein weiterer Schritt. Andere „Unknown error“-Ursachen benötigen den
jeweiligen Protokolleintrag.

## Gemeinsame Plugin-Verwaltung ab 0.1.300

App/Ingress und Runtime können die Repository-Liste, importierte Plugin-Metadaten
und Aktivierungszustände im selben ATLAS-Server speichern. Aktualisiere zuerst
die **ATLAS-App/Laufzeit** auf 0.1.300; allein ein HACS-Update genügt dafür nicht.

1. Öffne den bisherigen **ATLAS-App-Zugang**, in dem alle Plugins vorhanden sind.
2. Öffne Administration → Plugin-Manager → **Gemeinsame Plugin-Verwaltung**.
3. Wähle **Lokalen Stand übernehmen** und prüfe Repository-, Plugin- und
   Aktivierungszahlen sowie angezeigte Konflikte.
4. Standardmäßig bleiben bei Konflikten die Serverwerte erhalten. Wähle den
   lokalen Stand nur, wenn dessen Werte bewusst übernommen werden sollen.
5. Klicke **Gesichert übernehmen**. Ein Download sichert die Plugin-Metadaten;
   der Server sichert zusätzlich den bisherigen Stand und die Übernahmedaten,
   bevor er atomar speichert.
6. Öffne die Runtime erneut oder nutze **Serverstand laden**. Weitere Änderungen
   werden gemeinsam gespeichert; offene Administrationen prüfen den Stand alle
   15 Sekunden. Gleichzeitige Änderungen mit veraltetem Stand werden abgewiesen.

Eine leere Übernahme entfernt keine vorhandenen Servereinträge. Bis zur ersten
bestätigten Übernahme bleibt die bisherige lokale Verwaltung gültig. Die alten
Browserdaten werden durch die Übernahme nicht gelöscht. Nicht gespeicherte
Änderungen erhalten eine eigene lokale Wiederherstellungskopie und können erneut
zur Übernahme geprüft werden. **Sicherung prüfen** liest einen Metadatenexport
oder eine Server-Sicherung mit Vorschau; die Übernahme führt Einträge zusammen.

Der Serverstand liegt unter `ATLAS_PLUGIN_DATA_ROOT/.management/state.json`,
die Sicherungen unter `.management/backups/`. Beim App/Add-on und in Docker
liegt dies im dauerhaften Plugin-Datenverzeichnis. Sichere dieses Verzeichnis
mit der Laufzeit. Es werden keine Pakete automatisch installiert oder entfernt.
HA-Tokens, Provider-Schlüssel, Dateiberechtigungen, Editor-Projekte und eigene
Einstellungen externer Plugins bleiben außerhalb dieser Übernahme.

## Gemeinsame Editor-Projekte ab 0.1.301

Aktualisiere die ATLAS-App/Laufzeit auf **0.1.301**. Öffne zuerst den bisherigen
App-Editor mit deinem vorhandenen Projekt. Unter **Gemeinsame Editor-Projekte**
wähle **Neues Serverprojekt → Prüfen und speichern**. Prüfe Name und Feldanzahl,
dann **Gesichert übernehmen**. Zum Übernehmen eines weiteren lokalen Projekts
wähle erneut **Neues Serverprojekt**; gleiche Namen sind erlaubt und ersetzen
keine anderen Projekte automatisch.

In der Runtime: **Projektliste laden**, Projekt auswählen, **Öffnen prüfen**,
Vorschau prüfen und **Gesichert übernehmen**. Gespeichert werden Expert-Felder
mit ihren Card-Konfigurationen, Projektname, Scriptname, Fläche und Rastergröße.
Änderungen werden ausdrücklich über **Prüfen und speichern** gespeichert.
Gleichzeitige Änderungen desselben Projekts werden per Versionsprüfung erkannt.
Die Arbeitsfläche wird nicht automatisch aus einem anderen Browser ersetzt.

Vor dem Öffnen oder Speichern wird die aktuelle Arbeitsfläche serverseitig unter
`ATLAS_PLUGIN_DATA_ROOT/.projects/workspaces/` und als Download gesichert.
Vorherige Serverstände liegen unter `.projects/backups/`, benannte Projekte in
`.projects/projects.json`. Sichere das dauerhafte Plugin-Datenverzeichnis mit.
**Sicherung prüfen** öffnet einen Arbeitsflächen-Backup-Download mit Vorschau.
**Lokalen Entwurf prüfen** stellt einen ungespeicherten gemeinsamen Entwurf aus
diesem Browser wieder bereit; nach einem Neuladen wird er nicht automatisch geöffnet.

Der ursprüngliche lokale Projektstand bleibt im alten Browserspeicher erhalten.
Gemeinsame Arbeitsflächen erhalten einen separaten lokalen Entwurf. Einstellungen,
HA-Zugangsdaten, Plugin-Verwaltung, Palettenfavoriten und externe Plugin-Projekte
werden nicht mitübertragen. Eine beschädigte Serverdatei wird nicht ersetzt.
Grenzen: 100 Projekte, 4 MiB je Projekt und 64 MiB für die Projektdatei.

## Manuelle Installation und Updates

Kopiere ausschließlich `custom_components/atlas_frontend` aus dem Repository
nach `/config/custom_components/atlas_frontend`. Sichere einen vorhandenen
Ordner vor dem Austausch; andere Komponenten bleiben erhalten. Starte HA neu
und füge die Integration wie oben hinzu. `manifest.json` enthält die Version.

Bei Updates über HACS aktualisiere nur diese Integration und starte HA neu.
Die Laufzeitadresse bleibt im HA-Konfigurationseintrag erhalten. Der ATLAS-Server
wird unabhängig über seinen vorhandenen Installationsweg aktualisiert.
**Konfigurieren** an der Integration ändert die Adresse; exportiere ATLAS-Daten
vor einem bewussten Wechsel. Entfernen der Integration entfernt ihren eigenen
Panelzugang, nicht die ATLAS-Laufzeit, ihre Plugins oder ihre Projekte.

Ab Integration **0.1.306** werden unbekannte Konfigurationsformate beim
Migrationsversuch abgewiesen, ohne den Eintrag umzuschreiben. Die bisherige
Version **1.1** des Konfigurationsformats bleibt unverändert; die Paketversion
ist davon unabhängig. Eine Rückkehr zu einer älteren Integration ist nur bei
kompatiblem Datenformat geprüft. Sichere vor Updates HA-Konfiguration und
ATLAS-Daten; bei einer späteren Formatänderung gehört die passende Datensicherung
zur Wiederherstellung. Eine ungültige gespeicherte Laufzeitadresse wird als
Einrichtungsfehler gemeldet und kann über **Konfigurieren** korrigiert werden.

## HTTP, HTTPS und Einbettung

Wenn HA über HTTPS erreichbar ist, benötigt die eingebettete Laufzeit ebenfalls
HTTPS. Ein HTTP-Ziel zeigt stattdessen einen Hinweis und **Separat öffnen**.
Die Basisadresse darf keine Zugangsdaten, Abfrageparameter oder Fragmente
enthalten. Port 80 ist zulässig. Reverse-Proxy-Präfixe bleiben erhalten.

Ein Reverse Proxy muss die ATLAS-Unterpfade korrekt weiterleiten und die
Einbettung von der HA-Origin erlauben. Bei einer leeren Ansicht prüfe zuerst
**Separat öffnen**, Erreichbarkeit, Proxy-Weiterleitung und Frame-Schutzheader.
Eine automatisch ermittelte oder dauerhaft gespeicherte Ingress-Sitzungsadresse
ist nicht Teil dieser Integration; nutze für das Add-on weiterhin seinen
vorhandenen Ingress-Zugang.

Die Administratorpflicht des HA-Panels schützt nicht den direkten Zugriff auf
einen externen ATLAS-Server. Dessen vorhandene Zugriffsbeschränkung bleibt nötig.
Das neue Panel verwendet den Pfad `atlas-runtime` und ersetzt keinen fremden
Seitenleisteneintrag. Das JavaScript-Modul wird unter
`/atlas_frontend/frontend/atlas-homeassistant-panel.js` bereitgestellt;
es ist keine zusätzliche Lovelace-Ressource unter `/hacsfiles/atlas/`.

## Geprüfter Umfang

Isolierte Prüfungen verwenden Home Assistant Core **2026.10.1**, eine eigene
ATLAS-Laufzeit und Testdaten. Konfigurations-/Optionsdialog, Admin-Panel,
Neuladen, Neustart, statisches Modul und Erhalt anderer Panels werden geprüft.
Einrichtung und Einbettung über HACS sind auf Proxmox/x86_64 und Pi 5/ARM64
geprüft. Der isolierte Integrationswechsel **0.1.301 → 0.1.306**, Rückkehr zu
0.1.301 und erneutes Update erhalten denselben Konfigurationseintrag und die
anderen Panels über echte HA-Neustarts. Ein unbekanntes Testformat wird ohne
Änderung des Eintrags abgewiesen. Auf Pi 5 und Proxmox ist das HACS-Update auf
0.1.306 samt HA-Neustart, Panel, Live-Entitäten und Datenerhalt geprüft. Die
separate ATLAS-App bleibt bei dieser Integrationsprüfung auf 0.1.305.

Die zusätzliche stabile Version **2026.9.4** ist mit Integration und Laufzeit
**0.1.306** in einer frischen isolierten amd64-Installation geprüft:
Einrichtung/Optionen, Integrations-Neuladen, vollständiger HA-Neustart,
eingebetteter Hub, Administration und Editor, authentifizierte Versionserkennung
und Live-Entitätsauswahl. Konfigurationseintrag, andere Panels sowie Testprojekt,
Plugin-Daten und Konfigurationsdatei bleiben erhalten. Pi 5 und Proxmox wurden
für diese zusätzliche Prüfung nicht verändert. HACS-Download, Supervisor,
ARM64 und Integrations-Rollback wurden unter 2026.9.4 nicht erneut geprüft.

Die CI-Matrix prüft elf Integrationsverträge gegen **2026.9.4** und **2026.10.1**.
Das ersetzt die gesonderten Prüfungen mit laufendem HA nicht und bestätigt keinen
durchgehenden Versionsbereich. Weitere HA-Versionen und echte Umwandlungen
zwischen unterschiedlichen Datenformaten bleiben separate Qualifikationsschritte.

Grundlagen: [HA-Custom-Panels](https://developers.home-assistant.io/docs/frontend/custom-ui/creating-custom-panels/)
und [HACS-Integrationsstruktur](https://www.hacs.xyz/docs/publish/integration/).
