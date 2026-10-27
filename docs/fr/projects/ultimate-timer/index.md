---
layout: home
hero:
  name: Ultimate Timer
  text: Blueprint Home Assistant V3.2.4
  tagline: Minuteur hybride performant avec une logique d'arrêt (STOP) robuste, un état DONE persistant, une prise en charge multi-instance et MQTT.
  actions:
  - theme: brand
    text: Importer dans Home Assistant
    link: https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/rockbaer2007/ha-ultimate-timer-blueprint/main/blueprints/automation/ultimate_timer_v3_2_4.yaml
  - theme: alt
    text: GitHub
    link: https://github.com/rockbaer2007/ha-ultimate-timer-blueprint
features:
- icon: ⏱️
  title: Durée flexible
  details: Durée du minuteur au format hh:mm:ss.
- icon: ⏹️
  title: Arrêt (STOP) fiable
  details: Le minuteur peut être arrêté proprement à tout moment.
- icon: 🎯
  title: État DONE persistant
  details: L'état DONE reste actif jusqu'à ce que la réinitialisation quotidienne soit effectuée.
- icon: 🔁
  title: Multi-instance
  details: Plusieurs minuteurs indépendants peuvent être utilisés en parallèle.
- icon: 🔀
  title: « Helpers » ou MQTT
  details: Gestion des états via les « Helpers » (assistants) de Home Assistant ou via MQTT.
- icon: 🛡️
  title: Fonctionnement stable
  details: Logique RUNNING et STOP révisée, sans écrasement mutuel.
---
<a id="index"></a>
<a id="statut"></a>


## Aperçu {#ubersicht}

L'**Ultimate Timer V3.2.4 FINAL CLEAN** est un « blueprint » (modèle) d'automatisation pour Home Assistant, conçu pour des minuteurs réutilisables.

Cas d'utilisation typiques :

- Pompes de piscine et de bassin
- Arrosage
- « Watchdogs » (surveillance/garde-chiens)
- Exécutions différées
- Appareils pilotés par minuterie
- Minuteurs réutilisables pour tableaux de bord

[Accéder directement à l'installation](/fr/projects/ultimate-timer/installation)

## Aperçu {#vorschau}

![Configuration du blueprint](/images/ultimate-timer/preview_blueprint.png)
