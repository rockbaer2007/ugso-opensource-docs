# Konfiguration

Beispiel:

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

`postal_code` ist die Postleitzahl für die Preisabfrage.

`amounts` ist eine kommagetrennte Liste von Liter-Mengen.

`interval` ist das Abrufintervall in Minuten. Minimum ist `30`.

`esyoil_enabled`, `heizoel24_de_enabled` und `heizoel24_at_enabled` aktivieren die einzelnen Quellen.

`log_response_details` schreibt Rohantworten der Anbieter ins App-Protokoll und sollte nur zur Fehlersuche aktiviert werden.

## Datenschutz

Die konfigurierte Postleitzahl, Menge und Lieferoptionen werden an die aktivierten Preisquellen gesendet.
