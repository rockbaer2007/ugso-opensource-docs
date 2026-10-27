---
title: Développement et traduction de Mushroom
description: Serveur de développement, instructions de compilation et de traduction pour Mushroom.
---
<a id="mushroom-developpement-und-ubersetzung"></a>
<a id="orientation-actuelle"></a>

# Développement et traduction {#entwicklung-und-ubersetzung}

## Lancer une démo de Home Assistant {#home-assistant-demo-starten}

Le projet original permet de lancer une démo de Home Assistant via Docker :

```sh
npm run start:hass
```

Ensuite, Home Assistant est accessible localement à l'adresse `http://localhost:8123`.

Sous Windows, selon le projet original, cette commande peut être utilisée comme alternative :

```sh
npm run start:hass-cmd
```

## Serveur de développement {#entwicklungsserver}

Installer les dépendances et lancer le serveur de développement :

```sh
npm install
npm start
```

Le serveur démarre sur le port `4000`.

## Compilation (Build) {#build}

```sh
npm run build
```

La compilation génère `mushroom.js` dans le dossier `dist`.

## Traductions de l'interface Mushroom {#ubersetzungen-der-mushroom-oberflache}

Mushroom utilise Weblate pour les traductions de l'interface utilisateur :

- [Mushroom sur Weblate](https://hosted.weblate.org/engage/mushroom/)

Les nouveaux fichiers de langue doivent utiliser des codes de langue BCP-47 compatibles avec Home Assistant, par exemple `de`, `fr`, `fr-CA` ou `zh-Hans`.
