# Beispiele

## Paketliste mit flex-table-card

![Parcel to MQTT flex-table-card](/images/parcel-to-mqtt/parcel-flex-table-card.png)

```yaml
type: custom:flex-table-card
title: Pakete
entities:
  include: sensor.parcel_to_mqtt_parcel_dhl_json
columns:
  - name: Richtung
    data: sendungen
    modify: x.sendungsinfo.sendungsrichtung
  - name: Name
    data: sendungen
    modify: x.sendungsinfo.sendungsname
  - name: Status
    data: sendungen
    modify: x.sendungsdetails.sendungsverlauf.status
  - name: Fortschritt
    data: sendungen
    modify: x.sendungsdetails.sendungsverlauf.fortschritt
  - name: Nummer
    data: sendungen
    modify: x.sendungsdetails.sendungsnummern.sendungsnummer
```

## Mushroom Paket Card

```yaml
type: vertical-stack
cards:
  - type: custom:mushroom-title-card
    title: Pakete
    subtitle: Parcel to MQTT
  - type: horizontal-stack
    cards:
      - type: custom:mushroom-entity-card
        entity: sensor.parcel_gesamt
        name: Gesamt
        icon: mdi:package-variant-closed
        layout: vertical
      - type: custom:mushroom-entity-card
        entity: sensor.parcel_in_zustellung
        name: Zustellung
        icon: mdi:truck-delivery
        layout: vertical
      - type: custom:mushroom-entity-card
        entity: sensor.parcel_problem
        name: Problem
        icon: mdi:package-alert
        layout: vertical
  - type: custom:mushroom-template-card
    entity: sensor.parcel_01
    primary: >
      {{ state_attr('sensor.parcel_01', 'carrier') or 'Parcel 01' }}
    secondary: >
      {{ states('sensor.parcel_01') }}
      {% set event = state_attr('sensor.parcel_01', 'last_event') %}
      {% if event %} · {{ event }}{% endif %}
    icon: mdi:package-variant-closed
    multiline_secondary: true
    color: >
      {% set group = state_attr('sensor.parcel_01', 'status_group') %}
      {% if group == 'delivered' %}
        green
      {% elif group == 'out_for_delivery' %}
        blue
      {% elif group == 'exception' %}
        red
      {% else %}
        orange
      {% endif %}
```
