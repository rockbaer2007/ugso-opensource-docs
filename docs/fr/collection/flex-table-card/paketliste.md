---
title: Liste des colis avec `flex-table-card`
description: 'Exemple pratique : listes de colis (via « Parcel to MQTT ») affichées avec `flex-table-card`.'
---
<a id="flex-table-card-paketliste"></a>
<a id="orientation-actuelle"></a>

# Exemple de liste de colis {#paketlisten-beispiel}

Cet exemple présente une liste de colis issue d'un capteur JSON, telle qu'elle peut être fournie par `Parcel to MQTT` ou des adaptateurs similaires.

## Structure attendue {#erwartete-struktur}

Le capteur doit contenir une liste dans l'attribut `sendungen`. Pour chaque colis, les champs suivants sont particulièrement utiles :

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

## Tableau DHL {#dhl-tabelle}

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

## Plusieurs transporteurs {#mehrere-provider}

Si un capteur JSON distinct existe pour chaque transporteur, chaque transporteur disposera de sa propre carte.

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

Pour DHL, Hermes, DPD, GLS et UPS, `max_rows: 10` suffit généralement. Amazon peut, si nécessaire, utiliser `15`.
