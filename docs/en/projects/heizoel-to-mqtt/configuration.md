# Configuration

Example:

```yaml
plz: "10115"
amount: "1000,2000,3000"
interval: 60
esyActive: true
deliveryTimes: normal
payment_type: ec
prod: normal
unloading_points: 1
hose: fortyMetre
short_vehicle: withTrailer
hoDe: true
hoAt: false
log_response_details: false
```

`plz` is the postal code used for price lookups.

`amount` is a comma-separated list of liter amounts.

`interval` is the polling interval in minutes. The minimum is `30`.

`esyActive`, `hoDe` and `hoAt` enable the individual sources.

`deliveryTimes`, `payment_type`, `prod`, `unloading_points`, `hose` and `short_vehicle` mirror the selection fields from the ioBroker mask. The detailed options are used for Esyoil. Heizöl24 mainly uses postal code and amount, matching the original ioBroker adapter note.

Old `0.1.0` option names such as `postal_code`, `amounts`, `esyoil_enabled`, `heizoel24_de_enabled`, `heizoel24_at_enabled`, `product` and `delivery_times` are still accepted as fallback.

`log_response_details` writes raw provider responses to the app log and should only be enabled for troubleshooting.

## Privacy

The configured postal code, amount and delivery options are sent to the enabled price sources.
