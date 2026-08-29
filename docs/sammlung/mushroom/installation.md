---
title: Mushroom Installation
description: Mushroom über HACS oder manuell in Home Assistant installieren.
---
# Installation

## Installation Über HACS

Mushroom ist über HACS verfügbar.

1. HACS installieren, falls es noch nicht vorhanden ist.
2. In Home Assistant HACS öffnen.
3. Nach `Mushroom` suchen.
4. Repository herunterladen.
5. Browser neu laden, falls Home Assistant die neue Karte noch nicht anzeigt.

Direktlink für Home Assistant:

[Mushroom in HACS oeffnen](https://my.home-assistant.io/redirect/hacs_repository/?owner=piitaya&repository=lovelace-mushroom)

## Manuelle Installation

1. `mushroom.js` aus dem neuesten Release herunterladen.
2. Datei in den Home-Assistant-Ordner `config/www` legen.
3. Ressource im Dashboard eintragen.

Ressource über die Oberfläche:

1. **Einstellungen** öffnen.
2. **Dashboards** öffnen.
3. Menü mit den weiteren Optionen öffnen.
4. **Ressourcen** wählen.
5. Ressource hinzufügen.
6. URL auf `/local/mushroom.js` setzen.
7. Ressourcentyp auf `JavaScript Module` setzen.

::: tip Hinweis
Wenn der Menüpunkt **Ressourcen** nicht sichtbar ist, muss im Benutzerprofil der erweiterte Modus aktiviert werden.
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
