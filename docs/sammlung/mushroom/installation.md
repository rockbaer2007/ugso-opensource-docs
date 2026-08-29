---
title: Mushroom Installation
description: Mushroom ueber HACS oder manuell in Home Assistant installieren.
---
# Installation

## Installation Ueber HACS

Mushroom ist ueber HACS verfuegbar.

1. HACS installieren, falls es noch nicht vorhanden ist.
2. In Home Assistant HACS oeffnen.
3. Nach `Mushroom` suchen.
4. Repository herunterladen.
5. Browser neu laden, falls Home Assistant die neue Karte noch nicht anzeigt.

Direktlink fuer Home Assistant:

[Mushroom in HACS oeffnen](https://my.home-assistant.io/redirect/hacs_repository/?owner=piitaya&repository=lovelace-mushroom)

## Manuelle Installation

1. `mushroom.js` aus dem neuesten Release herunterladen.
2. Datei in den Home-Assistant-Ordner `config/www` legen.
3. Ressource im Dashboard eintragen.

Ressource ueber die Oberflaeche:

1. **Einstellungen** oeffnen.
2. **Dashboards** oeffnen.
3. Menue mit den weiteren Optionen oeffnen.
4. **Ressourcen** waehlen.
5. Ressource hinzufuegen.
6. URL auf `/local/mushroom.js` setzen.
7. Ressourcentyp auf `JavaScript Module` setzen.

::: tip Hinweis
Wenn der Menuepunkt **Ressourcen** nicht sichtbar ist, muss im Benutzerprofil der erweiterte Modus aktiviert werden.
:::

Ressource per YAML:

```yaml
lovelace:
  resources:
    - url: /local/mushroom.js
      type: module
```

## Nach Der Installation

Nach der Installation findest du die Karten beim Bearbeiten eines Dashboards unter den Custom Cards. Die Kartennamen beginnen typischerweise mit `Custom: Mushroom`.
