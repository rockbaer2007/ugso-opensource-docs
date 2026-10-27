---
title: Mushroom development and translation
description: Development server, build and translation notes for Mushroom.
---
<a id="mushroom-development-und-ubersetzung"></a>
<a id="current-focus"></a>

# Development and translation {#entwicklung-und-ubersetzung}

## Start Home Assistant demo {#home-assistant-demo-starten}

The original project can launch a Home Assistant demo via Docker:

```sh
npm run start:hass
```

Home Assistant can then be accessed locally under `http://localhost:8123`.

According to the original project, this command can be used under Windows as an alternative:

```sh
npm run start:hass-cmd
```

## Development server {#entwicklungsserver}

Install dependencies and start development server:

```sh
npm install
npm start
```

The server starts on port `4000`.

## Build {#build}

```sh
npm run build
```

The build creates `mushroom.js` in the `dist` folder.

## Translations of the Mushroom interface {#ubersetzungen-der-mushroom-oberflache}

Mushroom uses Weblate for UI translations:

- [Mushroom on Weblate](https://hosted.weblate.org/engage/mushroom/)

New language files must use Home Assistant compatible BCP-47 language codes, for example `de`, `fr`, `fr-CA`, or `zh-Hans`.
