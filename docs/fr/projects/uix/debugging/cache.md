---
title: Vider le cache
---
# Vider le cache de l'interface Home Assistant

L’action personnalisée vide le cache de l’application frontend Home Assistant puis recharge le navigateur. Elle est utile lorsque la commande habituelle est cachée dans un menu de débogage. **`localStorage` reste intact**, notamment l’identifiant du navigateur Browser Mod. Vider ce cache ne revient pas à supprimer toutes les données du navigateur ou de l’application.

Cette précision corrige une contradiction du texte d’origine. Elle a été vérifiée dans [l’implémentation `clear_cache()` de la révision examinée](https://github.com/Lint-Free-Technology/uix/blob/26e54e6d4973231a393933e6479ed1b03cc86cd3/src/ll-custom-actions.ts#L224-L242).

Consultez l'action UIX [`clear_cache`](../extras/uix-actions.md#clear-cache-clearing-home-assistant-frontend-cache).
