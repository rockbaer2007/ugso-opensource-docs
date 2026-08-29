---
title: Mushroom Entwicklung und Übersetzung
description: Entwicklungsserver, Build und Übersetzungshinweise für Mushroom.
---
# Entwicklung Und Übersetzung

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

Abhängigkeiten installieren und Entwicklungsserver starten:

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

## Übersetzungen Der Mushroom-Oberfläche

Mushroom nutzt Weblate für UI-Übersetzungen:

- [Mushroom auf Weblate](https://hosted.weblate.org/engage/mushroom/)

Neue Sprachdateien müssen Home-Assistant-kompatible BCP-47-Sprachcodes verwenden, zum Beispiel `de`, `fr`, `fr-CA` oder `zh-Hans`.
