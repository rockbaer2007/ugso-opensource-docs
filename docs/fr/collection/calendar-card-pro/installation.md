---
title: Installation de Calendar Card Pro
description: Installez Calendar Card Pro via HACS ou manuellement.
---
<a id="calendar-card-pro-installation"></a>
<a id="orientation-actuelle"></a>

# Installation {#installation}

## Installation via HACS {#hacs-installation}

L'utilisation de HACS est la méthode recommandée.

1. Vérifiez si HACS est installé. 2. Ouvrez **HACS** dans Home Assistant.
3. Accédez à la section **Frontend**.
4. Ouvrez **Custom Repositories**.
5. Ajoutez le dépôt : `https://github.com/alexpfau/calendar-card-pro`
6. Définissez le type sur `Dashboard`.
7. Installez Calendar Card Pro.
8. Videz le cache du navigateur et rechargez Home Assistant.

Lien direct :

[Ouvrir Calendar Card Pro dans HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=alexpfau&repository=calendar-card-pro&category=plugin)

## Installation manuelle {#manuelle-installation}

En cas d'installation manuelle, les deux fichiers de la version doivent être téléchargés :

- `calendar-card-pro.js`
- `editor.js`

Les deux fichiers doivent être placés dans le même sous-dossier, par exemple :

```text
/config/www/calendar-card-pro/
```

Ensuite, seul `calendar-card-pro.js` doit être ajouté en tant que ressource. La carte chargera elle-même l'éditeur lorsque cela sera nécessaire.

```yaml
url: /local/calendar-card-pro/calendar-card-pro.js
type: module
```

::: tip Pourquoi un dossier dédié ?
`editor.js` est un nom de fichier générique. L'utilisation d'un sous-dossier dédié permet d'éviter les conflits de noms avec d'autres cartes installées manuellement.
:::

## Exigences {#voraussetzungen}

Calendar Card Pro nécessite au moins une entité de calendrier dans Home Assistant, par exemple :

```text
calendar.family
calendar.work
calendar.personal
```

Sans intégration de calendrier, il n'y a aucun événement que la carte puisse afficher.
