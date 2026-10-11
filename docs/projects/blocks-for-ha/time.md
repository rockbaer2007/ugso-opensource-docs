---
title: Datum und Zeit
description: Zeit-Blocks, HA-Zeitzone und Gegenüberstellung mit ioBroker.
---
# Datum und Zeit

## Zeitplan und Auslöser seit 0.1.60

Unter **Auslöser → Zeitplan** die CRON-Regel anklicken. Der Dialog bietet **Wizard / Einfach / CRON**, entsprechend den ioBroker-Popups. Einfach erzeugt Intervalle; der Wizard zusätzlich eine feste Uhrzeit mit numerischen Wochentagen. CRON hat Feldreiter und optional Sekunden. **OK** übernimmt eine gültige Regel; **Abbrechen** und Escape bewahren den bisherigen Wert. Die Darstellung folgt Hell/Dunkel. Alle Dialogtexte sind in DE/EN/FR verfügbar.

![Zeitplan](/assets/blocks-for-ha/blocks/de/ugso_schedule_trigger.png)

![CRON-Dialog](/assets/blocks-for-ha/schedule-de.png)

![CRON-Dialog dunkel](/assets/blocks-for-ha/schedule-dark-de.png)

Fünf Felder: Minute, Stunde, Monatstag, Monat, Wochentag. Sechs Felder beginnen mit Sekunden. Zahlen, Listen, Bereiche und Schritte sind möglich. Beispiele: `*/5 * * * *` alle fünf Minuten; `*/30 * * * * *` alle 30 Sekunden; `30 7 * * 1-5` werktags um 07:30. Sonntag ist 0 oder 7. Home Assistant führt die Automation in seiner Ortszeit aus; kein Browser-Timer. `/Schritte` beziehen sich auf das jeweilige Uhrzeitfeld: `*/7` Minuten beginnt in jeder Stunde wieder bei Minute 0.

Die Ausgabe verwendet native `time_pattern` oder `time`-Auslöser mit `weekday`. Monat und Monatstag müssen `*` sein. Datum, Gültigkeitsbereich, einmalige Termine und astronomische Tages-/Nachtfenster sind im Dialog noch nicht umgesetzt. Diese Regeln werden nicht stillschweigend ignoriert. Wochentagsregeln werden höchstens in 2000 einzelne Uhrzeiten aufgelöst; häufigere Regeln sind ausdrücklich abgewiesen. Kalender-Auslöser und HA-Bedingungen bleiben separat verfügbar. Projekt-JSON erhält die CRON-Regel, YAML die gleichwertige native HA-Struktur.

| ioBroker-Auslöser | Blocks for HA / HA-Umsetzung |
| --- | --- |
| Falls Objekt / Falls Objekte | Zustandsauslöser mit einer oder mehreren Entitäten; von/nach, Attribut und Haltezeit. Keine ioBroker-Objekt-IDs. |
| Auslösung durch / ack bestätigen | HA besitzt hier kein ioBroker-`ack`. Kein künstlicher Bestätigungsblock. |
| ↪ Wert / Meldung | Neuer Auslöserdatenblock: Wert, alter Wert, Entitäts-ID, Auslöser-ID/-typ, MQTT-Meldung/JSON und Ereignisdaten. Fehlende Daten ergeben `none`; Zahlen bei Bedarf umwandeln. |
| Astro mit Versatz | Sonnenauf-/untergang mit optionalem Minutenversatz. Weitere Sonnenbedingungen über native HA-Blöcke. |
| Zeitplan / CRON | Dialog wie oben, native HA-Ausführung. Keine dynamische Registrierung benannter ioBroker-Zeitpläne. |
| Nachricht empfangen | MQTT- oder HA-Ereignisauslöser mit Filter; kein direkter Empfang von ioBroker-Skriptnachrichten. |
| Log-Nachricht | HA-Ereignisauslöser mit `system_log_event`, sofern HA diese Ereignisse entsprechend bereitstellt. Kein eigenständiger ioBroker-Loglistener. |
| Datei-/Enum-Ereignisse | Keine direkte Umsetzung. Vorhandene HA-Integration bzw. deren Ereignisse/Entitäten verwenden. |
| Weitere native HA-Auslöser | MQTT, Template, Webhook, Gerät, Tag, Gespräch, Zone und Geolocation stehen jetzt direkt unter **Auslöser**, ohne Doppelung unter HA erweitert. |

![Auslöserdaten](/assets/blocks-for-ha/blocks/de/ugso_trigger_value.png)

Referenzen: [Originale ioBroker-Triggerblöcke](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_trigger.ts), [native HA-Auslöser](https://www.home-assistant.io/docs/automation/trigger/). Die Oberfläche orientiert sich am Original; Ausführung und Daten bleiben HA-spezifisch.

Seit **0.1.11** enthält die Kategorie sieben zusätzliche Blocks. [Alle Blocks mit Bildern](./blocks#datum-und-zeit-seit-0-1-11). Die Oberfläche verwendet die originale Blockly-Library; die Übersetzung nach HA-Jinja ist eine eigene UGSo-Implementierung. Referenz sind die [Zeit-Blocks des ioBroker-JavaScript-Adapters](https://github.com/ioBroker/ioBroker.javascript/blob/master/src-editor/src/Components/blockly-plugins/blocks/blocks_time.ts) und die [Blockly-Blockdefinitionen](https://docs.blockly.com/guides/create-custom-blocks/define/block-definitions/).

## ioBroker / UGSo Blocks für HA

| ioBroker | Unser Block / Umsetzung |
| --- | --- |
| Aktuelle Zeit ist …, feste Uhrzeit | **Uhrzeitvergleich** mit kleiner, kleiner/gleich, größer, größer/gleich, gleich, zwischen und nicht zwischen. Das Endfeld erscheint bei Zeiträumen. |
| Aktuelle Zeit mit Checkbox und andockbarem Wert | **Uhrzeitvergleich mit Eingängen**: Text-Blocks für Start/Ende. Haken aus: zusätzlicher Datumswert-Anschluss für die zu vergleichende Zeit. |
| Aktuelle Zeit als Datum-Objekt oder formatierter Wert | **Aktuelle Zeit als Datumswert** und separater **Formatierungsblock**. Diese Trennung verhindert, dass formatierte Texte versehentlich als Datumswerte verrechnet werden. |
| Berechnete Zeit | **Kalenderbeginn**: Tag, nächster Tag, Woche (Montag), Monat und Jahr. Weitere ioBroker-Kalendergrenzen sind noch nicht vorhanden. |
| Aktuelle Zeit von Astroereignis plus Offset | **Nächste Sonnenzeit**: Aufgang, Untergang, Morgen-/Abenddämmerung, Höchststand und Sonnenmitternacht, mit positivem/negativem Minutenoffset. |
| Zeit berechnen, Basis ± Zahl, Einheit | **Zeit berechnen**: Datumswert ± Zahl; Millisekunden, Sekunden, Minuten, Stunden oder Tage. |

## Anschlüsse und Bedienung

Zeitvergleiche liefern **Boolean** und passen in Bedingungen, UND/ODER/NICHT oder Falls. Datumswerte besitzen einen **Time-Anschluss**: Aktuelle Zeit, Kalenderbeginn, Sonnenzeit und Zeitberechnung lassen sich untereinander verschachteln. Zahlen gehören in Offset/Betrag; formatierte Uhrzeiten als Text in die andockbaren Vergleichsgrenzen. Formatierung bietet HH:mm, HH:mm:ss, ISO-Datum, deutsches Datum, Datum/Uhrzeit, ISO mit Zeitzone und Unix-Sekunden.

Beispiel: **Aktuelle Zeit → Zeit berechnen (+ 30 Minuten) → Zeit formatieren (HH:mm)**, anschließend als Variable setzen. Das erzeugte Template lautet:

```jinja
{{ (now() + timedelta(minutes=30)).strftime("%H:%M") }}
```

**Zwischen 22:00 und 06:00** schließt die Nacht über Mitternacht ein. Der Start gehört dazu, das Ende nicht. Gleiche Grenzen bedeuten einen leeren Zeitraum; „nicht zwischen“ ist dessen Gegenteil. Feste Uhrzeiten müssen HH:mm oder HH:mm:ss sein. Dynamische Textgrenzen müssen zur Laufzeit dasselbe Format liefern; ungültige Werte erzeugen einen HA-Template-Fehler. Der Vergleich arbeitet auf Sekunden; „gleich 12:00“ bedeutet 12:00:00 und ist kein zuverlässiger Zeit-Auslöser.

## Ausführung und Grenzen

Die erzeugten Templates werden **in Home Assistant** ausgewertet. Der Browser baut das YAML und führt keine eigene laufende Zeitsteuerung aus. Die Funktionen verwenden die konfigurierte HA-Zeitzone: [HA-Datums-/Zeitfunktionen](https://www.home-assistant.io/template-functions/#date-time). Kalenderbeginn nutzt lokale Mitternacht; Tage folgen der lokalen Kalenderrechnung, auch bei Sommerzeitwechsel. Eine Rechnung „+ 24 Stunden“ garantiert bei einem Zeitwechsel keine 24 real verstrichenen UTC-Stunden.

Sonnenwerte kommen aus den Attributen der [HA-Sun-Integration](https://www.home-assistant.io/integrations/sun/#sensors). Diese liefern das **nächste Ereignis**, nicht stets das Ereignis des heutigen Tages. Die UTC-Angabe wird vor Berechnung/Formatierung in HA-Ortszeit umgewandelt. Fehlende Werte, etwa bei nicht verfügbarer Integration oder einem nicht berechenbaren Ereignis, ergeben einen Template-Fehler; es wird keine Ersatzzeit erfunden.

Ein Zeitvergleich prüft die Uhrzeit **beim Durchlaufen der Bedingung**. Er startet die Automation nicht und wartet nicht bis zur passenden Uhrzeit. Dafür einen Uhrzeit- oder Sonnen-Auslöser verwenden. Der neue Sonnenwert-Block ersetzt keinen Sonnen-Auslöser.

**Blocks-Projekt (JSON)** erhält Form, Auswahl und dynamische Eingänge. Beim **YAML-Öffnen** bleiben diese Zeittemplates inhaltlich erhalten, erscheinen aber als allgemeine Template-Blocks. Ein zuvor in einer HA-Variable gespeicherter Datumswert kann als Text vorliegen; unser Variablen-Leseblock hat deshalb keinen Time-Anschluss. Datumswerte direkt verschachteln oder seit **0.1.12** den Variablen-Leseblock über **Nach Datum/Zeit** konvertieren. [Konvertierung und Einheiten](./conversion). Konvertierte Laufzeitzahlen können jetzt auch in Betrag und Sonnenoffset andocken.

Prüfung: Blockly-/YAML-Rundläufe, typisierte Anschlüsse, dynamische Felder sowie Jinja-Prüfungen für Nachtgrenzen und Sommerzeit. Eine Ausführung auf einem echten HA-System ist noch nicht verifiziert.
