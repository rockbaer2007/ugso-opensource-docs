---
title: Dépannage de Mushroom
description: Problèmes courants avec Mushroom Cards et premières étapes pour les résoudre.
---
<a id="mushroom-depannage"></a>
<a id="orientation-actuelle"></a>

# Dépannage {#fehlersuche}

## Les nouvelles modifications ne sont pas visibles {#neue-anderungen-sind-nicht-sichtbar}

1. Vérifiez si Home Assistant est à jour.
2. Vérifiez si la dernière version de Mushroom est installée via HACS.
3. Vérifiez dans la console du navigateur si la version attendue de Mushroom est bien celle qui est chargée.
4. Videz le cache.
5. Supprimez la ressource Mushroom.
6. Désinstallez Mushroom via HACS.
7. Réinstallez Mushroom.
8. Rechargez le navigateur et l'application Home Assistant.

Lien direct vers les ressources Lovelace :

[Ouvrir les ressources Home Assistant](https://my.home-assistant.io/redirect/lovelace_resources/)

## Card-mod ne fonctionne pas {#card-mod-funktioniert-nicht}

Le dépôt Mushroom ne propose pas de support général pour les configurations `card-mod`.

Le mainteneur renvoie vers ce fil de discussion dédié :

- [État du support de card-mod](https://github.com/piitaya/lovelace-mushroom/issues/1366)

## La carte est introuvable {#karte-wird-nicht-gefunden}

Causes courantes :

- La ressource est manquante ou pointe vers un mauvais chemin.
- Le cache du navigateur charge encore un ancien fichier.
- L'installation via HACS n'a pas été entièrement chargée.
- Le code YAML utilise un type de carte incorrect.

Exemple d'ajout manuel correct d'une ressource :

```yaml
resources:
  - url: /local/mushroom.js
    type: module
```
