---
title: Installation de Mushroom
description: Installez Mushroom via HACS ou manuellement dans Home Assistant.
---
<a id="mushroom-installation"></a>
<a id="orientation-actuelle"></a>

# Installation {#installation}

## Installation via HACS {#installation-uber-hacs}

Mushroom est disponible via HACS.

1. Installez HACS si ce n'est pas déjà fait.
2. Ouvrez HACS dans Home Assistant.
3. Recherchez `Mushroom`.
4. Téléchargez le dépôt.
5. Actualisez votre navigateur si Home Assistant n'affiche pas encore la nouvelle carte.

Lien direct pour Home Assistant :

[Ouvrir Mushroom dans HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=piitaya&repository=lovelace-mushroom)

## Installation manuelle {#manuelle-installation}

1. Téléchargez `mushroom.js` depuis la dernière version publiée.
2. Placez le fichier dans le dossier `config/www` de Home Assistant.
3. Ajoutez la ressource au tableau de bord.

Ajout de la ressource via l'interface :

1. Ouvrez **Paramètres**.
2. Ouvrez **Tableaux de bord**.
3. Ouvrez le menu des options supplémentaires.
4. Sélectionnez **Ressources**.
5. Ajoutez une ressource.
6. Définissez l'URL sur `/local/mushroom.js`.
7. Définissez le type de ressource sur `JavaScript Module`.

::: tip Remarque
Si l'élément de menu **Ressources** n'est pas visible, le mode avancé doit être activé dans le profil utilisateur.
:::

Ressource via YAML :

```yaml
lovelace:
  resources:
    - url: /local/mushroom.js
      type: module
```

## Après l'installation {#nach-der-installation}

Une fois l'installation terminée, vous trouverez les cartes dans la section « Cartes personnalisées » (Custom Cards) lors de la modification d'un tableau de bord. Les noms des cartes commencent généralement par `Custom: Mushroom`.
