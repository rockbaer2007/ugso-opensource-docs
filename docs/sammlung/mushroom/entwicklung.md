---
title: Mushroom Entwicklung und Uebersetzung
description: Entwicklungsserver, Build und Uebersetzungshinweise fuer Mushroom.
---
# Entwicklung Und Uebersetzung

## Home-Assistant-Demo Starten

Das Originalprojekt kann eine Home-Assistant-Demo per Docker starten:

```sh
npm run start:hass
```

Danach ist Home Assistant lokal unter `http://localhost:8123` erreichbar.

Unter Windows kann laut Originalprojekt alternativ dieser Befehl genutzt werden:

```sh
npm run start:hass-cmd
```

## Entwicklungsserver

Abhaengigkeiten installieren und Entwicklungsserver starten:

```sh
npm install
npm start
```

Der Server startet auf Port `4000`.

## Build

```sh
npm run build
```

Der Build erzeugt `mushroom.js` im `dist`-Ordner.

## Uebersetzungen Der Mushroom-Oberflaeche

Mushroom nutzt Weblate fuer UI-Uebersetzungen:

- [Mushroom auf Weblate](https://hosted.weblate.org/engage/mushroom/)

Neue Sprachdateien muessen Home-Assistant-kompatible BCP-47-Sprachcodes verwenden, zum Beispiel `de`, `fr`, `fr-CA` oder `zh-Hans`.
