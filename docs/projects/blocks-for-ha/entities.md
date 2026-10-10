---
title: Home-Assistant-Entitäten
description: Entitäten aus HA laden, suchen und in Blocks übernehmen.
---
# Entitäten auswählen

Seit **0.1.17** öffnen die Entitätsfelder der vorhandenen Blocks einen Suchdialog. Die HA-App lädt beim Öffnen des Editors die aktuelle Entitätsliste. **Entitäten laden** in der Werkzeugleiste und **Neu laden** im Dialog aktualisieren sie.

![Entitätsauswahl mit Suchergebnis](/assets/blocks-for-ha/entity-picker.png)

Das Bild verwendet simulierte Testentitäten. Die Oberfläche bleibt deutsch; die Entitätsnamen kommen aus deiner HA-Installation.

## Bedienung

1. Auf die Entitäts-ID im Block klicken.
2. Nach Name oder ID suchen. Mehrere Suchwörter müssen alle passen. Die ersten 150 Treffer werden angezeigt; bei großen Listen die Suche eingrenzen.
3. Ein Ergebnis auswählen und **Übernehmen** drücken. Erst dann wird der Block geändert. **Abbrechen** oder Escape lässt ihn unverändert.
4. Alternativ eine ID wie `light.wohnzimmer` direkt eingeben. Das funktioniert auch ohne Verbindung oder für nicht geladene Entitäten.

Die Liste zeigt Name, ID und aktuellen Zustand mit Einheit. Diese Zustände sind eine **Momentaufnahme**, keine laufende Überwachung und keine Sensor-Wertblocks für die Automation.

| Block | Auswahl |
| --- | --- |
| Zustand-/Zahlenauslöser und Bedingungen | Alle geladenen Entitäten |
| Licht mit Farbe/Helligkeit | Nur `light` |
| HA-Script | Nur `script` |
| Helfer | Aktuell gewählter Typ: `input_boolean`, `counter` oder `timer` |
| Ein/Aus/Umschalten, Entität aktualisieren, generische HA-Aktion | Alle geladenen Entitäten; Unterstützung der Aktion weiterhin in HA prüfen |

Ein leerer Zielwert ist ausschließlich bei der generischen HA-Aktion erlaubt. Der Dialog übernimmt eine einzelne Entitäts-ID. Bereichs-/Geräteauswahl, Mehrfachziele und eine Live-Auswahl installierter Aktionen folgen später. Ein ID-Wechsel ersetzt keine frei eingegebenen IDs in Jinja oder JSON-Daten.

## HA-App und Daten

Repository im HA-App-Store aktualisieren, **Version 0.1.17** installieren und die App neu starten. Die App benötigt `homeassistant_api: true` und verwendet den serverseitigen `SUPERVISOR_TOKEN` für einen lesenden Aufruf an `http://supervisor/core/api/states`. Im Editor ist keine Token-Eingabe nötig. [Offizielle HA-App-Kommunikation](https://developers.home-assistant.io/docs/apps/communication/), [REST-API](https://developers.home-assistant.io/docs/api/rest/).

Der Browser erhält nur ID, Anzeigename, Domain, Zustand und Einheit. Weitere Attribute, Zugangsdaten und HA-Konfiguration werden nicht weitergegeben. Der Endpunkt erlaubt nur das Lesen der Entitätsliste und führt keine HA-Aktionen aus. Der Server folgt keinen Weiterleitungen mit Zugangsdaten.

Die Liste stammt aus der HA-Zustandsliste, nicht aus der gesamten Entitätsregistrierung. Deaktivierte oder noch nicht verfügbare Entitäten ohne Zustand können fehlen. `unknown`/`unavailable` werden angezeigt, wenn sie in der Liste vorhanden sind. Bei einem Ladefehler wird die bisherige Liste verworfen; bestehende Block-IDs bleiben erhalten.

Im JSON-Projekt und im YAML steht weiterhin nur die ausgewählte ID. Katalog, Namen, Zustandsvorschau und Zugangsdaten werden nicht im Browser gespeichert oder exportiert. 111 Blocktypen bleiben erhalten. Vor einem Update das eigene Browserprojekt über **Projekt sichern** herunterladen; ein Quellcode-Backup enthält keine Browsersitzung.

## Lokale Entwicklung

`npm run dev` allein arbeitet mit manuellen IDs. Für eine Verbindung zusätzlich Python 3 starten: `npm run entities`. Nur im Serverprozess die Umgebungsvariablen `BLOCKS_HA_URL` (Basisadresse ohne `/api`, etwa `http://homeassistant.local:8123`) und `BLOCKS_HA_TOKEN` setzen. Der Vite-Server auf `127.0.0.1:4180` leitet die Abfrage an die lokale Bridge auf `127.0.0.1:9001` weiter. Keine Zugangsdaten in Quellcode oder Projektdateien eintragen.

Die Docker-Version startet Bridge und Weboberfläche gemeinsam. Außerhalb von HA mit gesetzten Zugangsdaten nur lokal binden oder eine authentifizierte vorgeschaltete Oberfläche verwenden; eigenständige Benutzeranmeldung ist noch nicht enthalten. In HA schützt Ingress den Zugriff.

## Prüfung

Geprüft sind Projekt-/YAML-Kompatibilität, Suche, Filter, Abbrechen, manuelle Eingabe, Fehlerfälle, mobiles Layout und die vollständige Docker-Kette gegen einen simulierten HA-Server. Ein praktischer Test in einer echten HA-Installation steht noch aus. Die Entitätsauswahl bestätigt nicht, dass eine konkrete Aktion vom gewählten Gerät unterstützt wird.
