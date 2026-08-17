# Entities

Entities are created through MQTT Discovery.

General entities:

- Parcel connection
- Parcel last update
- Parcel shipments
- Parcel total
- Parcel in transit
- Parcel out for delivery
- Parcel delivered
- Parcel exception
- Parcel unknown

Parcel slots:

- Parcel 01
- Parcel 02
- further slots up to the configured amount

Each parcel slot uses the status as its state and exposes attributes for tracking number, carrier, status group, last event, last event time and destination country.

The JSON list of all parcels is exposed as an attribute on the `Parcel Sendungen` sensor.
