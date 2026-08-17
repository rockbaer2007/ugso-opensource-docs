# Configuration

```yaml
track17_api_key: ""
tracking_numbers: "00340434123456789012,1Z999AA10123456784"
interval: 60
max_parcels: 6
log_response_details: false
```

`track17_api_key` is the API key for 17TRACK.

`tracking_numbers` contains one or more tracking numbers separated by commas.

`interval` is the update interval in minutes.

`max_parcels` controls how many parcel slot entities are created through MQTT Discovery.

`log_response_details` writes raw responses to the app log for troubleshooting. Disable it again after testing.

Notifications are created through Home Assistant automations, for example when `sensor.parcel_in_zustellung` becomes greater than `0`.
