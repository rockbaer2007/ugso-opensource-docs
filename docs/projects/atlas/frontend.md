# ATLAS im Home-Assistant-Frontend

Ab **0.1.299** enthält ATLAS die optionale Integration **ATLAS Runtime**.
Sie registriert einen eigenen Seitenleisteneintrag für HA-Administratoren.
Darin öffnen sich Plugin Hub, Expert Card Editor und Administration der
vorhandenen ATLAS-Laufzeit. Die Oberfläche folgt der HA-Sprache DE/EN/FR
und der hellen oder dunklen Darstellung.

## Voraussetzungen und Datenerhalt

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
Weitere HA-Versionen, echte ARM64-Installation und der vollständige Download
über HACS auf Pi/Proxmox bleiben separate Qualifikationsschritte.

Grundlagen: [HA-Custom-Panels](https://developers.home-assistant.io/docs/frontend/custom-ui/creating-custom-panels/)
und [HACS-Integrationsstruktur](https://www.hacs.xyz/docs/publish/integration/).
