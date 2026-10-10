---
title: Home-Assistant-Entitäten
description: Entitäten aus HA laden, suchen und in Blocks übernehmen.
---
# Entitäten auswählen

Seit **0.1.44** öffnen passende Aktions- und Zielfelder der einfachen und erweiterten Blocks eine durchsuchbare Auswahl. Ein kleiner Pfeil markiert diese Felder. **HA-Auswahl laden** in der Werkzeugleiste und **Neu laden** im Dialog aktualisieren die lesenden Kataloge.

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

Aktionsfelder zeigen die von HA gemeldeten Aktionen. Entitätsziele berücksichtigen die Domains der Aktionsbeschreibung oder des Aktionsnamens. Die Zielauswahl folgt `entity_id`, `device_id`, `area_id`, `floor_id` oder `label_id`: Entitäten, Geräte, Bereiche, Etagen oder Labels. Die letzten vier Kataloge werden nicht anhand der Aktion gefiltert. **Mehrere Ziele auswählen** erlaubt Listen in unterstützten Feldern. Freie IDs, JSON-Listen und unterstützte Jinja-Templates bleiben möglich; mehrzeiliger Jinja-Text wird vollständig erhalten. Ein Zielartwechsel schreibt vorhandene IDs nicht um.

Szenen und Helfer bieten passende Entitätsdomains; erweiterte numerische Grenzen zusätzlich Sensoren und Zahlenhelfer, Zeitfelder Zeithelfer und Sensoren. Manuelle Zahlen/Uhrzeiten bleiben möglich. Fachliche Dropdowns bleiben erhalten. Variablennamen, Trigger-IDs, Attribute, freier Text und komplexe Daten erhalten keine pauschale HA-Auswahl. Ein ID-Wechsel ersetzt keine Referenzen in frei eingegebenen Jinja- oder JSON-Daten. Ohne Aktionskatalog erscheinen ausdrücklich gekennzeichnete gängige Beispiele; fehlende Zielkataloge erlauben manuelle IDs.

## HA-App und Daten

Repository im HA-App-Store aktualisieren, **Version 0.1.44** installieren und die App neu starten. Die App benötigt `homeassistant_api: true` und verwendet den serverseitigen `SUPERVISOR_TOKEN`. Entitäten und Aktionen werden über die [REST-API](https://developers.home-assistant.io/docs/api/rest/) gelesen, Zielregistrierungen über die [WebSocket-API](https://developers.home-assistant.io/docs/api/websocket/). Fehlende Registry-Berechtigungen betreffen nur die jeweilige Liste. Im Editor ist keine Token-Eingabe nötig.

Der Browser erhält nur Auswahlmetadaten: ID, Anzeigename, Domains und bei Entitäten Zustand/Einheit. Weitere Attribute und Zugangsdaten werden nicht weitergegeben. Die Endpunkte lesen ausschließlich Kataloge und führen keine HA-Aktionen aus. Der Server folgt keinen Weiterleitungen mit Zugangsdaten.

Die Liste stammt aus der HA-Zustandsliste, nicht aus der gesamten Entitätsregistrierung. Deaktivierte oder noch nicht verfügbare Entitäten ohne Zustand können fehlen. `unknown`/`unavailable` werden angezeigt, wenn sie in der Liste vorhanden sind. Bei einem Ladefehler wird die bisherige Liste verworfen; bestehende Block-IDs bleiben erhalten.

Im JSON-Projekt und im YAML stehen die gewählten Feldwerte. Katalog, Namen, Zustandsvorschau und Zugangsdaten werden nicht gespeichert oder exportiert. Alle 163 Blocktypen bleiben erhalten. Vor einem Update das eigene Browserprojekt über **Projekt sichern** herunterladen; ein Quellcode-Backup enthält keine Browsersitzung.

## Lokale Entwicklung

Die Python-Abhängigkeit einmal mit `python -m pip install --require-hashes -r requirements.txt` installieren. Docker installiert sie automatisch.

`npm run dev` allein arbeitet mit manuellen IDs. Für eine Verbindung zusätzlich Python 3 starten: `npm run entities`. Nur im Serverprozess die Umgebungsvariablen `BLOCKS_HA_URL` (Basisadresse ohne `/api`, etwa `http://homeassistant.local:8123`) und `BLOCKS_HA_TOKEN` setzen. Der Vite-Server auf `127.0.0.1:4180` leitet die Abfrage an die lokale Bridge auf `127.0.0.1:9001` weiter. Keine Zugangsdaten in Quellcode oder Projektdateien eintragen.

Die Docker-Version startet Bridge und Weboberfläche gemeinsam. Außerhalb von HA mit gesetzten Zugangsdaten nur lokal binden oder eine authentifizierte vorgeschaltete Oberfläche verwenden; eigenständige Benutzeranmeldung ist noch nicht enthalten. In HA schützt Ingress den Zugriff.

## Prüfung

Geprüft sind Projekt-/YAML-Kompatibilität, Suche, Filter, Abbrechen, manuelle Eingabe, Fehlerfälle, mobiles Layout und die vollständige Docker-Kette gegen einen simulierten HA-Server. Ein praktischer Test in einer echten HA-Installation steht noch aus. Die Entitätsauswahl bestätigt nicht, dass eine konkrete Aktion vom gewählten Gerät unterstützt wird.
