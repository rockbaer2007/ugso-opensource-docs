---
title: Capteur et lampe
---

<script setup>
import BlockPackageCode from '../../../../.vitepress/theme/components/BlockPackageCode.vue'
import pkg from '../../../../public/assets/blocks-for-ha/packages/ugso_sensor_tools-1.0.0.json'
const code = JSON.stringify(pkg, null, 2)
</script>

# Capteur et lampe

**1.0.0 · rockbaer2007 · Apache-2.0 · UGSo Blocks for HA ≥ 0.1.18**

| Bloc | Fonction |
| --- | --- |
| Valeur numérique du capteur | Lit un état comme nombre. État non numérique : 0. |
| Capteur au-dessus du seuil | Vérifie un seuil numérique. Les états inconnus ne satisfont pas la condition. |
| Lampe avec luminosité | Produit `light.turn_on` avec `brightness_pct`. Valeurs 0–100 ; lampe compatible requise. |

Remplacer `sensor.temperatur` et `light.wohnzimmer`. Jinja est évalué dans HA. Les libellés de ce paquet restent en allemand, langue définie par son auteur. [Import et limites](../custom-blocks).

[Télécharger le ZIP](/assets/blocks-for-ha/packages/ugso_sensor_tools-1.0.0.zip) · [Télécharger le JSON](/assets/blocks-for-ha/packages/ugso_sensor_tools-1.0.0.json)

## Coller le code

Copier le JSON, sélectionner **JSON prüfen** puis **Übernehmen** dans l’éditeur. Code et ZIP contiennent la même définition.

<BlockPackageCode :code="code" french />
