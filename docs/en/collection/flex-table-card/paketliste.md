---
title: flex-table-card package list
description: Practical example for Parcel to MQTT package lists as a flex-table-card.
---
<a id="flex-table-card-paketliste"></a>
<a id="current-focus"></a>

# Package list example {#paketlisten-beispiel}

This example shows a package list from a JSON sensor, as can be provided by `Parcel to MQTT` or similar adapters.

## Expected structure {#erwartete-struktur}

The sensor should contain a list in the `sendungen` attribute. At least these fields are helpful for each package:

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

## DHL table {#dhl-tabelle}

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

## Multiple providers {#mehrere-provider}

If there is a separate JSON sensor for each provider, each provider gets its own card.

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

For DHL, Hermes, DPD, GLS and UPS, `max_rows: 10` is usually enough. Amazon can stay on `15` if necessary.
