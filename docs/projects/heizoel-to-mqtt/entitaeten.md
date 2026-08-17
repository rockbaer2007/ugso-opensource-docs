# Entitäten

Die Entitäten werden per MQTT Discovery erstellt.

Für jede aktivierte Quelle und jede konfigurierte Liter-Menge entstehen:

- Preis pro 100 Liter
- Gesamtpreis
- Händler
- Lieferdauer
- Anzahl Angebote
- Anbieter 01 bis Anbieter 10

Zusätzlich gibt es:

- Heizöl Verbindung
- Heizöl letzte Aktualisierung

Die Anbieter-Entitäten enthalten den Namen des Anbieters als Zustand. Die Attribute enthalten Rang, Preis pro 100 Liter, Gesamtpreis, Lieferdauer, Lieferdatum, Bewertung und Währung.

Die Bestpreis-Detailattribute enthalten Quelle, Menge, PLZ, Händler, Lieferdatum, Bewertung und Angebotsanzahl.
