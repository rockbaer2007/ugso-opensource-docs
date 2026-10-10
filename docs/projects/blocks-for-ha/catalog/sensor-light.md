---
title: Sensor und Licht
---
<script setup>
import BlockPackageCode from '../../../.vitepress/theme/components/BlockPackageCode.vue'
import pkg from '../../../public/assets/blocks-for-ha/packages/ugso_sensor_tools-1.0.0.json'
const code = JSON.stringify(pkg, null, 2)
</script>

# Sensor und Licht

**1.0.0 · rockbaer2007 · Apache-2.0 · UGSo Blocks for HA ≥ 0.1.18**

| Block | Funktion |
| --- | --- |
| Sensorwert als Zahl | Liest den Zustand einer Sensorentität als Zahl. Nicht numerische Zustände ergeben 0. |
| Sensor über Grenze | Prüft einen numerischen Sensorzustand auf „größer als Grenze“. Unbekannte Zustände erfüllen die Bedingung nicht. |
| Licht mit Helligkeit | Erzeugt eine native `light.turn_on`-Aktion mit `brightness_pct`. 0–100 verwenden; das Licht muss Helligkeit unterstützen. |

Beispielentitäten `sensor.temperatur` und `light.wohnzimmer` ersetzen. Jinja wird in HA ausgewertet. [Import und Grenzen](../custom-blocks).

[ZIP herunterladen](/assets/blocks-for-ha/packages/ugso_sensor_tools-1.0.0.zip) · [JSON herunterladen](/assets/blocks-for-ha/packages/ugso_sensor_tools-1.0.0.json)

## Code einfügen

Code kopieren, im Editor **JSON prüfen** und **Übernehmen** wählen. Code und ZIP verwenden dieselbe Definition.

<BlockPackageCode :code="code" />
