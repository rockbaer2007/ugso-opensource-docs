---
title: Zendure HA Entitäten
description: Wichtige Sensoren, Zahlen, Auswahlfelder, Schalter und Buttons der Zendure Integration.
---
# Entitäten

Die Integration erzeugt je nach Gerät unterschiedliche Entitäten. Nicht jedes Modell unterstützt jede Entität.

## Wichtige Sensoren

| Entität / Übersetzung | Zweck |
| --- | --- |
| `Batterieladezustand (SoC)` | Ladezustand des Akkus in Prozent |
| `Verfügbare Energie` | verfügbare Energie oberhalb des Mindest-SoC |
| `Gesamtkapazität Batterie` | erkannte Batteriekapazität |
| `Solarleistung` | gesamte Solar-Eingangsleistung |
| `PV1` bis `PV4 Solarleistung` | Solarleistung einzelner Eingänge |
| `Haus-Ausgangsleistung` | Leistung Richtung Haus |
| `Netz-Eingangsleistung` | Leistung vom Netz in das Gerät |
| `Batterieleistung` | berechnete Lade-/Entladeleistung |
| `Batterieladeleistung` | Leistung in den Akku |
| `Batterieentladeleistung` | Leistung aus dem Akku |
| `Verbleibende Zeit` | berechnete Lade- oder Entladezeit |
| `Verbindungsstatus` | Cloud, Local, zenSDK, HEMS oder fehlende Fuse Group |
| `BMS-Firmware` | Firmware der Batterie |
| `AC-Firmware` | AC-Firmware |
| `Master-Firmware` | Master-Firmware |
| `Roundtrip-Wirkungsgrad` | Verhältnis entladener zu geladener Energie |

## Energiezähler

| Entität / Übersetzung | Zweck |
| --- | --- |
| `Gesamte Ladeenergie` | aufsummierte Ladeenergie |
| `Gesamte Entladeenergie` | aufsummierte Entladeenergie |
| `Gesamte Hausenergie` | Energie Richtung Haus |
| `Gesamte Solarenergie` | erzeugte Solarenergie |
| `Gesamte Netzenergie` | Energie vom Netz |
| `Gesamte Off-Grid-Energie` | Off-Grid-Energie, falls unterstützt |
| `Schaltvorgänge` | Wechsel zwischen Zuständen |

## Zahlenfelder

| Entität / Übersetzung | Zweck |
| --- | --- |
| `AC-Eingangsgrenze` | maximale AC-Ladeleistung |
| `AC-Ausgangsgrenze` | maximale AC-Ausgangsleistung |
| `Manuelle Leistung` | Sollwert für den manuellen Manager-Modus |
| `SoC-Minimum` | untere Ladegrenze |
| `SoC-Zielwert` | oberer Ziel-SoC |

## Auswahlfelder

| Entität / Übersetzung | Optionen / Zweck |
| --- | --- |
| `AC-Betriebsmodus` | AC-Eingang oder AC-Ausgang |
| `DC Anschluss` | An/Ausgang oder Aus/Eingang |
| `Hub-Modus` | gekoppelt oder eigenständig |
| `HEMS-Status` | aktiv oder deaktiviert |
| `Auto. Batterieheizung` | aktiv oder deaktiviert |
| `Geräte-Sicherungsgruppe` | Fuse-Group-Auswahl |
| `Verbindungsart` | Cloud, lokal oder je nach Gerät zenSDK |
| `Betriebsmodus` | Aus, manuell, smart, nur laden, nur entladen, Solar speichern |
| `Bypass-Modus` | automatisch, immer aus, immer an |
| `Energie Export` | deaktiviert, erlaubt, verboten |
| `Lüftergeschwindigkeit` | automatisch, normal, schnell |

## Schalter und Buttons

| Entität / Übersetzung | Zweck |
| --- | --- |
| `LED` | LED/Lampe schalten |
| `AC Anschluss` | AC-Anschluss schalten |
| `Bestätigungston` | Ton aktivieren/deaktivieren |
| `Bypass-Modus zurücksetzen` | automatischen Bypass zurücksetzen |
| `Lüfter` | Lüfter schalten |
| `Reset Verbindung` | MQTT-/Verbindungsumstellung erneut anstoßen |

## Binärsensoren

| Entität / Übersetzung | Zweck |
| --- | --- |
| `Hauptschalter` | Hauptstatus |
| `WLAN-Status` | WLAN erreichbar |
| `Batterieheizung` | Heizung aktiv |
| `Energiesparmodus` | Rest-/Sparmodus |
| `Rückflussstatus` | Rückfluss erkannt |
| `Lokale Verbindung` | lokale Verbindung aktiv |
| `CT getrennt` | CT-Sensor getrennt |
| `Niedrige Temperatur` | niedrige Temperatur erkannt |
| `HEMS aktiv` | HEMS aktiv |

## Geräteabhängigkeit

Die Entitäten werden aus Geräteklasse, Firmware, Verbindungstyp und gemeldeten MQTT-/HTTP-Daten aufgebaut. Wenn eine Entität fehlt, ist das nicht automatisch ein Fehler; das Gerät oder die Verbindung liefert den Wert möglicherweise nicht.

