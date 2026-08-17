# Entitäten

Die Entitäten werden per MQTT Discovery erstellt.

Allgemeine Entitäten:

- Parcel Verbindung
- Parcel letzte Aktualisierung
- Parcel Sendungen
- Parcel Gesamt
- Parcel Angemeldet
- Parcel Unterwegs
- Parcel In Zustellung
- Parcel Abholstelle
- Parcel Zugestellt
- Parcel Rücksendung
- Parcel Problem
- Parcel Unbekannt

Paket-Slots:

- Parcel 01
- Parcel 02
- weitere Slots bis zur konfigurierten Anzahl

Jeder Paket-Slot hat den Status als Zustand und Attribute für Sendungsnummer, Anbieter, Statusgruppe, letztes Ereignis, Zeitpunkt des letzten Ereignisses und Zielland.

Die JSON-Liste aller Sendungen liegt als Attribut am Sensor `Parcel Sendungen`.
