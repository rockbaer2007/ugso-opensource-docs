# Konfiguration

```yaml
dhl_tracking_numbers: "00340434123456789012,00340434123456789013"
hermes_tracking_numbers: "12345678901234"
gls_tracking_numbers: ""
gls_postal_code: ""
interval: 60
max_parcels: 6
log_response_details: false
```

`dhl_tracking_numbers` enthält eine oder mehrere DHL-Sendungsnummern, mit Komma getrennt.

`hermes_tracking_numbers` enthält eine oder mehrere Hermes-Sendungsnummern, mit Komma getrennt.

`gls_tracking_numbers` und `gls_postal_code` sind bereits als Konfigurationsfelder vorhanden. GLS Deutschland wird noch nicht aktiv abgefragt, weil dafür eine anonyme Guest-Bearer-Session implementiert werden muss.

`interval` ist das Aktualisierungsintervall in Minuten.

`max_parcels` legt fest, wie viele Paket-Slot-Entitäten per MQTT Discovery angelegt werden.

`log_response_details` schreibt Rohantworten zur Fehlersuche ins Log. Diese Option sollte nach dem Testen wieder deaktiviert werden.

Benachrichtigungen werden über Home Assistant Automationen erstellt, zum Beispiel wenn `sensor.parcel_in_zustellung` größer als `0` wird.
