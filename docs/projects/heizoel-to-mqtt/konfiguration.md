# Konfiguration

Beispiel:

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

`plz` ist die Postleitzahl für die Preisabfrage.

`amount` ist eine kommagetrennte Liste von Liter-Mengen.

`interval` ist das Abrufintervall in Minuten. Minimum ist `30`.

`esyActive`, `hoDe` und `hoAt` aktivieren die einzelnen Quellen.

`deliveryTimes`, `payment_type`, `prod`, `unloading_points`, `hose` und `short_vehicle` entsprechen den Auswahlfeldern aus der ioBroker-Maske. Die Detailoptionen werden für Esyoil genutzt. Heizöl24 nutzt wie der Ursprungshinweis des ioBroker-Adapters vor allem PLZ und Menge.

Alte Optionsnamen aus `0.1.0`, zum Beispiel `postal_code`, `amounts`, `esyoil_enabled`, `heizoel24_de_enabled`, `heizoel24_at_enabled`, `product` und `delivery_times`, werden weiterhin als Fallback gelesen.

`log_response_details` schreibt Rohantworten der Anbieter ins App-Protokoll und sollte nur zur Fehlersuche aktiviert werden.

## Datenschutz

Die konfigurierte Postleitzahl, Menge und Lieferoptionen werden an die aktivierten Preisquellen gesendet.
