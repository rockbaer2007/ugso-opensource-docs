---
title: Vider le cache
---
# Vider le cache de l'interface Home Assistant

L’action personnalisée vide le cache de l’application frontend Home Assistant puis recharge le navigateur. Elle est utile lorsque la commande habituelle est cachée dans un menu de débogage. **`localStorage` reste intact**, notamment l’identifiant du navigateur Browser Mod. Vider ce cache ne revient pas à supprimer toutes les données du navigateur ou de l’application.

Cette précision corrige une contradiction du texte d’origine. Elle a été vérifiée dans [l’implémentation `clear_cache()` de la révision examinée](https://github.com/Lint-Free-Technology/uix/blob/26e54e6d4973231a393933e6479ed1b03cc86cd3/src/ll-custom-actions.ts#L224-L242).

Des styles anciens, des règles YAML qui ne prennent effet qu’après plusieurs rechargements ou un résultat différent entre navigateur et application Companion peuvent signaler un problème de cache. UIX peut aussi afficher une demande de rechargement après sa mise à jour.

Commencez par recharger Home Assistant, puis forcez le rechargement du navigateur. Dans l’application Companion, il peut être nécessaire de vider le cache de l’interface. Cela ne nécessite pas de supprimer toutes les données du navigateur ou de l’application.

Consultez l'action UIX [`clear_cache`](../extras/uix-actions.md#clear-cache-clearing-home-assistant-frontend-cache).
