---
title: flex-table-card Paketliste
description: Praxisbeispiel für Parcel to MQTT Paketlisten als flex-table-card.
---
# Paketlisten-Beispiel

Dieses Beispiel zeigt eine Paketliste aus einem JSON-Sensor, wie sie von `Parcel to MQTT` oder ähnlichen Adaptern bereitgestellt werden kann.

## Erwartete Struktur

Der Sensor sollte im Attribut `sendungen` eine Liste enthalten. Pro Paket sind mindestens diese Felder hilfreich:

```json
{
  "sendungen": [
    {
      "sendungsinfo": {
        "sendungsrichtung": "ANKOMMEND",
        "sendungsname": "Paketzentrum"
      },
      "sendungsdetails": {
        "sendungsverlauf": {
          "status": "Die Sendung wurde elektronisch angekuendigt.",
          "fortschritt": 1
        },
        "sendungsnummern": {
          "sendungsnummer": "00340434330872035559"
        }
      }
    }
  ]
}
```

## DHL-Tabelle

```yaml
type: custom:flex-table-card
title: DHL
entities:
  include: sensor.parcel_to_mqtt_parcel_dhl_json
max_rows: 15
columns:
  - name: Richtung
    data: sendungen.sendungsinfo.sendungsrichtung
    modify: x == "ANKOMMEND" ? "zu mir" : "von mir"
  - name: Name
    data: sendungen.sendungsinfo.sendungsname
  - name: Status
    data: sendungen.sendungsdetails.sendungsverlauf.status
  - name: Fortschritt
    data: sendungen.sendungsdetails.sendungsverlauf.fortschritt
    align: right
  - name: Nummer
    data: sendungen.sendungsdetails.sendungsnummern.sendungsnummer
css:
  table: "width: 100%; border-collapse: collapse;"
  thead th: "font-size: 13px; font-weight: 700; padding: 6px 8px;"
  tbody tr td: "font-size: 12px; line-height: 1.25; padding: 6px 8px;"
  "tbody tr:nth-child(odd)": "background-color: rgba(255,255,255,0.04);"
  "tbody tr:nth-child(even)": "background-color: rgba(255,255,255,0.08);"
  "tbody tr td:nth-child(5)": "font-family: monospace;"
```

## Mehrere Provider

Wenn pro Provider ein eigener JSON-Sensor existiert, bekommt jeder Provider eine eigene Karte.

```yaml
type: custom:flex-table-card
title: Amazon
entities:
  include: sensor.parcel_to_mqtt_parcel_amazon_json
max_rows: 15
columns:
  - name: Richtung
    data: sendungen.sendungsinfo.sendungsrichtung
    modify: x == "ANKOMMEND" ? "zu mir" : "von mir"
  - name: Name
    data: sendungen.sendungsinfo.sendungsname
  - name: Status
    data: sendungen.sendungsdetails.sendungsverlauf.status
  - name: Fortschritt
    data: sendungen.sendungsdetails.sendungsverlauf.fortschritt
    align: right
  - name: Nummer
    data: sendungen.sendungsdetails.sendungsnummern.sendungsnummer
```

Für DHL, Hermes, DPD, GLS und UPS reichen meist `max_rows: 10`. Amazon kann bei Bedarf auf `15` bleiben.

