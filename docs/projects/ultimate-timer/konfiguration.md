# Konfiguration

## Eingaben

| Feld | Beschreibung |
|---|---|
| Use MQTT | Nutzt MQTT anstelle von Helpern |
| Start Trigger | Startet den Timer |
| Stop Trigger | Stoppt den Timer vorzeitig |
| Running State | Zeigt den laufenden Timer an |
| Done State | Zeigt einen abgelaufenen Timer an |
| MQTT Running Topic | MQTT-Thema für RUNNING |
| MQTT Done Topic | MQTT-Thema für DONE |
| Duration | Timerdauer im Format `hh:mm:ss` |
| Reset Time | Uhrzeit für den täglichen Reset |

## Helper-Betrieb

Für den normalen Helper-Betrieb werden benötigt:

- ein Start-Helper
- optional ein Stop-Helper
- ein Running-Helper
- ein Done-Helper

Dafür eignen sich `input_boolean`-Entitäten.

## MQTT-Betrieb

Bei aktiviertem MQTT-Modus werden RUNNING und DONE über die konfigurierten Topics veröffentlicht.

Standardwerte:

```text
timer/running/set
timer/done/set
```

## Beispiel für die Dauer

```text
00:05:00
```

entspricht fünf Minuten.
