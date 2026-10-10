---
title: Sensor and light
---
<script setup>
import BlockPackageCode from '../../../../.vitepress/theme/components/BlockPackageCode.vue'
import pkg from '../../../../public/assets/blocks-for-ha/packages/ugso_sensor_tools-1.0.0.json'
const code = JSON.stringify(pkg, null, 2)
</script>

# Sensor and light

**1.0.0 · rockbaer2007 · Apache-2.0 · UGSo Blocks for HA ≥ 0.1.18**

| Block | Function |
| --- | --- |
| Numeric sensor value | Reads a sensor state as a number. Non-numeric states become 0. |
| Sensor above threshold | Tests a numeric sensor state against a threshold. Unknown states do not pass. |
| Light with brightness | Generates native `light.turn_on` with `brightness_pct`. Use 0–100; the light must support brightness. |

Replace sample entities `sensor.temperatur` and `light.wohnzimmer`. HA evaluates Jinja. Package labels remain in their original German language. [Import and limits](../custom-blocks).

[Download ZIP](/assets/blocks-for-ha/packages/ugso_sensor_tools-1.0.0.zip) · [Download JSON](/assets/blocks-for-ha/packages/ugso_sensor_tools-1.0.0.json)

## Paste code

Copy the code, select **JSON prüfen** and **Übernehmen** in the editor. Code and ZIP contain the same definition.

<BlockPackageCode :code="code" english />
