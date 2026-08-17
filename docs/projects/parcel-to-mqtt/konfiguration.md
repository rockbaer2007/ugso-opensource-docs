# Konfiguration

```yaml
dhl_tracking_numbers: "00340434123456789012,00340434123456789013"
interval: 60
max_parcels: 6
log_response_details: false
```

`dhl_tracking_numbers` enthält eine oder mehrere DHL-Sendungsnummern, mit Komma getrennt.

`interval` ist das Aktualisierungsintervall in Minuten.

`max_parcels` legt fest, wie viele Paket-Slot-Entitäten per MQTT Discovery angelegt werden.

`log_response_details` schreibt Rohantworten zur Fehlersuche ins Log. Diese Option sollte nach dem Testen wieder deaktiviert werden.

Benachrichtigungen werden über Home Assistant Automationen erstellt, zum Beispiel wenn `sensor.parcel_in_zustellung` größer als `0` wird.
