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

In Home Assistant werden die Konfigurationsfelder bei deutscher Oberflächensprache mit deutschen Namen und Beschreibungen angezeigt.

Alte Optionsnamen aus `0.1.0` für PLZ, Menge, Sorte und Liefertermin werden weiterhin als Fallback gelesen. Die Anbieter-Schalter heißen nur noch `esyActive`, `hoDe` und `hoAt`.

`log_response_details` schreibt Rohantworten der Anbieter ins App-Protokoll und sollte nur zur Fehlersuche aktiviert werden.

## Datenschutz

Die konfigurierte Postleitzahl, Menge und Lieferoptionen werden an die aktivierten Preisquellen gesendet.
