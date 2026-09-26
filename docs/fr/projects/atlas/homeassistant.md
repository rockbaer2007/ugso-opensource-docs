---
title: ATLAS and Accueil Assistant
description: Page française préparée pour ATLAS and Accueil Assistant dans la documentation UGSo Open Source.
---
# ATLAS et Home Assistant

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
