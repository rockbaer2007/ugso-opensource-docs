---
title: ATLAS and Accueil Assistant
description: Page française préparée pour ATLAS and Accueil Assistant dans la documentation UGSo Open Source.
---
# ATLAS et Home Assistant

## Connexion sur tablette et smartphone

L'URL Home Assistant doit être accessible depuis chaque navigateur. Si
`homeassistant.local` fonctionne sur PC mais pas sur tablette, la résolution
locale du nom peut être indisponible. Ouvrez d'abord l'adresse IP de votre
installation HA sur l'appareil concerné, par exemple
`http://192.168.178.177:80`. Remplacez cette IP d'exemple par votre adresse.

Si HA est accessible ainsi, renseignez cette adresse dans `home_assistant_url`
de la configuration de l'application ATLAS, enregistrez puis redémarrez ATLAS.
Conservez le jeton d'accès existant. Pour ATLAS autonome, modifiez plutôt l'URL
dans Administration et enregistrez les réglages.

**Le port 80 est accepté.** `http://HOTE:80` et `http://HOTE` sont équivalents ;
`ws://HOTE/api/websocket` utilise aussi le port 80. ATLAS n'impose pas le port
8123. Utilisez le port réellement configuré et une adresse HTTPS adaptée si
vous utilisez HTTPS. `WebSocket closed with code 1006` ne prouve pas à lui seul
que le jeton est invalide : vérifiez aussi l'accessibilité, la résolution du nom
et un éventuel proxy. Lors du test sur tablette Android, remplacer `.local`
par l'adresse IP accessible a rétabli la connexion.

## Liens des plugins dans la barre latérale de Home Assistant

À partir de l’App/Add-on ATLAS `0.1.236`, la boîte de dialogue de la barre
latérale génère une URL de lancement stable via le port `4176`, par exemple :

```text
http://<HOTE_ATLAS>:4176/launch/atlas.plugin.file-studio
```

Si un plugin figure déjà dans la barre latérale de Home Assistant, rouvrez la
boîte de dialogue correspondante dans ATLAS, copiez la **nouvelle URL** proposée
et remplacez l’ancienne valeur `url` dans l’entrée `panel_iframe` du plugin.
Vous pouvez aussi recopier et remplacer tout le bloc YAML. Redémarrez ensuite
Home Assistant pour recharger la configuration de la barre latérale. Le chemin
Home Assistant, par exemple `/atlas-studio/0`, ne change pas : c’est l’URL du
panel intégré qu’il faut actualiser. Le port `4176` doit être accessible depuis
le navigateur utilisé pour accéder à Home Assistant.
