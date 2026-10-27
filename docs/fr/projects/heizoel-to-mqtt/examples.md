<a id="exemples"></a>
<a id="statut"></a>

# Exemples {#beispiele}

## Carte « Fournisseur » Mushroom {#mushroom-anbieter-card}

Cette carte Lovelace affiche un fournisseur avec le prix au litre, le prix pour 100 litres et le prix total. La couleur varie en fonction du prix au litre.

Prérequis : Mushroom doit être installé dans Home Assistant. `card_mod` est facultatif et sert uniquement pour la bordure et l'arrière-plan.

![Carte « Mushroom » pour les prix du fioul domestique via MQTT](/images/heizoel-to-mqtt.png)

```yaml
type: custom:mushroom-template-card
entity: sensor.heizol_to_mqtt_esyoil_3000l_anbieter_01
primary: |
  {{ states('sensor.heizol_to_mqtt_esyoil_3000l_anbieter_01') }}
secondary: >
  💶 {{ states('sensor.heizol_to_mqtt_esyoil_3000l_anbieter_01_preis_pro_liter') }}
  €/L   📦 {{ states('sensor.heizol_to_mqtt_esyoil_3000l_anbieter_01_preis_pro_100l') }}
  € / 100L   🧾 Gesamt: {{ states('sensor.heizol_to_mqtt_esyoil_3000l_anbieter_01_gesamtpreis') }} €
icon: mdi:oil
multiline_secondary: true
grid_options:
  columns: 12
  rows: auto
color: >
  {% set p = states('sensor.heizol_to_mqtt_esyoil_3000l_anbieter_01_preis_pro_liter') | float(0) %}
  {% if p < 1.00 %}
    green
  {% elif p < 1.20 %}
    orange
  {% else %}
    red
  {% endif %}
vertical: true
features_position: bottom
card_mod:
  style: |
    ha-card {
      background: var(--ha-card-background, var(--card-background-color));
      border: 0.2px solid var(--primary-color);
      border-radius: 12px;
    }
```
