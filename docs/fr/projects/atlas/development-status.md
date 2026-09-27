---
title: État du développement
description: État actuel du développement d'ATLAS.
---
# État du développement

## État actuel

ATLAS est en cours de développement. L'application Home Assistant comprend
l'Administration, le Hub des plugins et le Card Editor ; File Studio et
Automation Exporter / Editor sont distribués comme plugins indépendants.

La version actuelle de l'application Home Assistant est `0.1.262`.
L'Administration et le Hub des plugins proposent des interfaces en allemand,
anglais et français. Leur préférence de langue enregistrée est partagée entre
les deux interfaces, y compris lorsque leurs ports sont différents. Le
paramètre `language` d'une URL reste prioritaire pour la page ouverte.

## Suite du travail

- Étendre progressivement la traduction aux interfaces de plugins qui déclarent
  leurs propres textes localisés.
- Continuer à intégrer les fonctions Renderer et Theme dans des parcours visibles
  de l'application.
- Stabiliser les API et les contrats avant une version de production.

::: info État évolutif
La feuille de route évolue avec le développement. Consultez les pages ATLAS et
Plugins ATLAS pour connaître les fonctions documentées.
:::
