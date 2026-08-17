# Entities

Entities are created through MQTT Discovery.

For each enabled source and configured amount, the app creates:

- price per 100 liters
- total price
- dealer
- delivery days
- offer count
- provider 01 through provider 10
- provider 01 through provider 10 total price
- provider 01 through provider 10 price per liter
- provider 01 through provider 10 price per 100l

It also creates:

- Heizöl connection
- Heizöl last update

Each offer creates four entities: provider name, total price, price per liter and price per 100l. Attributes contain rank, delivery days, delivery date, rating and currency.

Best-price detail attributes contain source, amount, postal code, dealer, delivery date, rating and offer count.
