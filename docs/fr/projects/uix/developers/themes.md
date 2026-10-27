---
description: Informations pour les développeurs de thèmes et d'intégrations.
---
# Développeurs - Thèmes et intégrations

Si vous utilisez UI eXtension dans un thème, **n'incluez aucune partie de l'intégration UI eXtension dans votre thème**. Invitez toujours les utilisateurs à installer l'intégration en suivant le [guide de démarrage rapide de UI eXtension](../quick-start.md).

Si vous utilisez UI eXtension avec une autre intégration personnalisée, ajoutez UI eXtension comme dépendance dans votre `manifest.json`. Les utilisateurs devront ainsi installer UI eXtension avant de pouvoir utiliser votre intégration.

Pour toute question, lancez une [discussion GitHub](https://github.com/Lint-Free-Technology/uix/discussions).

## Recommandations pour les thèmes

Nommez clairement les variables de thème, limitez les règles globales et évitez de compliquer les styles locaux des cartes. Vérifiez toujours aussi les valeurs du mode sombre.

## Exemples complémentaires de la référence allemande {#german-reference-examples}

:::: details Afficher les configurations complémentaires
Ces configurations complètent la référence traduite ci-dessus. Elles reprennent les exemples techniques de la [page allemande](/projects/uix/developers/themes). Les clés, expressions, valeurs et textes de démonstration sont conservés tels quels ; remplacez les entités par les vôtres. Les limites de version indiquées dans la référence restent applicables.

### 1. Exemple {#reference-example-1}

```yaml
my_theme:
  uix-card-yaml: |
    ha-card {
      box-shadow: none;
    }
```

::::
