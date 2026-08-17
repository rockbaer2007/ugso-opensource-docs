# Configuration

Example:

```yaml
postal_code: "10115"
amounts: "1000,2000,3000"
interval: 60
esyoil_enabled: true
heizoel24_de_enabled: true
heizoel24_at_enabled: false
unloading_points: 1
payment_type: ec
product: normal
delivery_times: normal
hose: fortyMetre
short_vehicle: withTrailer
log_response_details: false
```

`postal_code` is the postal code used for price lookups.

`amounts` is a comma-separated list of liter amounts.

`interval` is the polling interval in minutes. The minimum is `30`.

`esyoil_enabled`, `heizoel24_de_enabled` and `heizoel24_at_enabled` enable the individual sources.

`log_response_details` writes raw provider responses to the app log and should only be enabled for troubleshooting.

## Privacy

The configured postal code, amount and delivery options are sent to the enabled price sources.
