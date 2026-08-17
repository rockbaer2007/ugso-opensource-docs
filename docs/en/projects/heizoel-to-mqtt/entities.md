# Entities

Entities are created through MQTT Discovery.

For each enabled source and configured amount, the app creates:

- price per 100 liters
- total price
- dealer
- delivery days
- offer count
- provider 01 through provider 10

It also creates:

- Heizöl connection
- Heizöl last update

The provider entities expose the provider name as their state. Attributes contain rank, price per 100 litres, total price, delivery days, delivery date, rating and currency.

Best-price detail attributes contain source, amount, postal code, dealer, delivery date, rating and offer count.
