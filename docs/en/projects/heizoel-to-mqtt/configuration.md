# Configuration

Example:

```yaml
plz: "10115"
amount: "1000,2000,3000"
interval: 60
esyActive: true
deliveryTimes: ohne
payment_type: EC-Karte
prod: Normal Schwefelarm
unloading_points: 1
hose: 40
short_vehicle: mit Anhänger möglich
hoDe: true
hoAt: false
log_response_details: false
```

`plz` is the German or Austrian postal code used for price lookups.

`amount` is a comma-separated list of liter amounts.

`interval` is the polling interval in minutes. The minimum is `30`.

`esyActive`, `hoDe` and `hoAt` enable the individual sources.

`deliveryTimes`, `payment_type`, `prod`, `unloading_points`, `hose` and `short_vehicle` mirror the selection fields from the ioBroker mask. The detailed options are used for Esyoil. Heizöl24 mainly uses postal code and amount, matching the original ioBroker adapter note.

The app is intended for Germany and Austria only. Use German or Austrian postal codes that match the selected providers.

`deliveryTimes` uses the visible values from the ioBroker mask: `ohne`, `7:00 - 12:00 Uhr`, `12:00 - 17:00 Uhr`, `2 Wochentage (Express)`, `3 - 5 Wochentage (Mo.-Fr.)` and `6 - 10 Wochentage (Mo.-Fr.)`.

`prod` uses the visible oil product names from the ioBroker mask: `Normal Schwefelarm`, `Premium Schwefelarm`, `Klimaneutral Premium`, `Klimaneutral Normal`, `Bio 10`, `Bio 15` and `Bio 10 Premium`.

`payment_type` uses the visible payment names from the ioBroker mask: `EC-Karte`, `Barzahlung`, `Ratenkauf`, `Rechnung`, `Lastschrift` and `Vorkasse`.

`hose` is entered as a number in metres. Internally, it is mapped to the matching EasyOil hose class. `short_vehicle` is shown in Home Assistant as `Tankwagen` and offers `mit Anhänger möglich` or `ohne Anhänger`.

In the German Home Assistant UI, `esyActive` is shown as `EasyOil aktivieren`. `hoDe` and `hoAt` are shown as `Heizöl24 Deutschland aktivieren (Nur PLZ und Menge wird übernommen)` and `Heizöl24 Österreich aktivieren (Nur PLZ und Menge wird übernommen)`.

Home Assistant shows translated configuration labels and descriptions when the active UI language is German or English.

Old `0.1.0` option names for postal code, amount, product and delivery time are still accepted as fallback. Provider toggles now only use `esyActive`, `hoDe` and `hoAt`.

`log_response_details` writes raw provider responses to the app log and should only be enabled for troubleshooting.

## Privacy

The configured postal code, amount and delivery options are sent to the enabled price sources.
