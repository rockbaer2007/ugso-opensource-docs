# Entitäten

Die Entitäten werden per MQTT Discovery erstellt.

Für jede aktivierte Quelle und jede konfigurierte Liter-Menge entstehen:

- Preis pro 100 Liter
- Gesamtpreis
- Händler
- Lieferdauer
- Anzahl Angebote
- Anbieter 01 bis Anbieter 06
- Anbieter 01 bis Anbieter 06 Gesamtpreis
- Anbieter 01 bis Anbieter 06 Preis pro Liter
- Anbieter 01 bis Anbieter 06 Preis pro 100l

Zusätzlich gibt es:

- Heizöl Verbindung
- Heizöl letzte Aktualisierung

Pro Angebot entstehen damit vier Entitäten: Name des Anbieters, Gesamtpreis, Preis pro Liter und Preis pro 100l. Die Attribute enthalten Rang, Lieferdauer, Lieferdatum, Bewertung und Währung.

Die Bestpreis-Detailattribute enthalten Quelle, Menge, PLZ, Händler, Lieferdatum, Bewertung und Angebotsanzahl.
