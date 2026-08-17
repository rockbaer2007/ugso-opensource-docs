# Configuration

```yaml
dhl_tracking_numbers: "00340434123456789012,00340434123456789013"
hermes_tracking_numbers: "12345678901234"
gls_tracking_numbers: ""
gls_postal_code: ""
interval: 60
max_parcels: 6
log_response_details: false
```

`dhl_tracking_numbers` contains one or more DHL tracking numbers separated by commas.

`hermes_tracking_numbers` contains one or more Hermes tracking numbers separated by commas.

`gls_tracking_numbers` and `gls_postal_code` are already available as configuration fields. GLS Germany is not polled yet because it still needs an anonymous guest bearer session.

`interval` is the update interval in minutes.

`max_parcels` controls how many parcel slot entities are created through MQTT Discovery.

`log_response_details` writes raw responses to the app log for troubleshooting. Disable it again after testing.

Notifications are created through Home Assistant automations, for example when `sensor.parcel_in_zustellung` becomes greater than `0`.
