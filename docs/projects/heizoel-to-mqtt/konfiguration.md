# Konfiguration

Beispiel:

```yaml
plz: "10115"
amount: "1000,2000,3000"
interval: 60
esyActive: true
deliveryTimes: ohne
payment_type: "EC-Karte"
prod: Normal Schwefelarm
unloading_points: 1
hose: 40m
short_vehicle: mit Anhänger möglich
hoDe: true
hoAt: false
log_response_details: false
```

`plz` ist die deutsche oder österreichische Postleitzahl für die Preisabfrage.

`amount` ist eine kommagetrennte Liste von Liter-Mengen.

`interval` ist das Abrufintervall in Minuten. Minimum ist `30`.

`esyActive`, `hoDe` und `hoAt` aktivieren die einzelnen Quellen.

`deliveryTimes`, `payment_type`, `prod`, `unloading_points`, `hose` und `short_vehicle` entsprechen den Auswahlfeldern aus der ioBroker-Maske. Die Detailoptionen werden für Esyoil genutzt. Heizöl24 nutzt wie der Ursprungshinweis des ioBroker-Adapters vor allem PLZ und Menge.

Die App ist nur für Deutschland und Österreich vorgesehen. Verwende deutsche oder österreichische Postleitzahlen passend zu den aktivierten Anbietern.

`deliveryTimes` nutzt die sichtbaren Werte aus der ioBroker-Maske: `ohne`, `7:00 - 12:00 Uhr`, `12:00 - 17:00 Uhr`, `2 Wochentage (Express)`, `3 - 5 Wochentage (Mo.-Fr.)` und `6 - 10 Wochentage (Mo.-Fr.)`.

`prod` nutzt die sichtbaren Sorten aus der ioBroker-Maske: `Normal Schwefelarm`, `Premium Schwefelarm`, `Klimaneutral Premium`, `Klimaneutral Normal`, `Bio 10`, `Bio 15` und `Bio 10 Premium`.

`payment_type` nutzt die sichtbaren Zahlungsarten aus der ioBroker-Maske: `EC-Karte`, `Barzahlung`, `Ratenkauf`, `Rechnung`, `Lastschrift` und `Vorkasse`.

`hose` bietet die Werte `40m`, `60m` und `80m`. Bereits gespeicherte alte Werte mit Leerzeichen, zum Beispiel `40 m`, werden akzeptiert, damit Home Assistant bestehende Konfigurationen speichern kann. `short_vehicle` wird in Home Assistant als `Tankwagen` angezeigt und bietet `mit Anhänger möglich` oder `ohne Anhänger`.

In der deutschen Home-Assistant-Oberfläche wird `esyActive` als `EasyOil aktivieren` angezeigt. `hoDe` und `hoAt` heißen dort `Heizöl24 Deutschland aktivieren (Nur PLZ und Menge wird übernommen)` und `Heizöl24 Österreich aktivieren (Nur PLZ und Menge wird übernommen)`.

In Home Assistant werden die Konfigurationsfelder bei deutscher Oberflächensprache mit deutschen Namen und Beschreibungen angezeigt.

Alte Optionsnamen aus `0.1.0` für PLZ, Menge, Sorte und Liefertermin werden weiterhin als Fallback gelesen. Die Anbieter-Schalter heißen nur noch `esyActive`, `hoDe` und `hoAt`.

`log_response_details` schreibt Rohantworten der Anbieter ins App-Protokoll und sollte nur zur Fehlersuche aktiviert werden.

## Datenschutz

Die konfigurierte Postleitzahl, Menge und Lieferoptionen werden an die aktivierten Preisquellen gesendet.
