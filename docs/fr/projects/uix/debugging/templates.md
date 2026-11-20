# Débogage des modèles

Vous pouvez déboguer les modèles UIX Jinja2 en plaçant le commentaire <code v-pre>{# uix.debug #}</code> n'importe où dans votre modèle. Vous verrez les messages de débogage lors de la liaison du modèle, de la mise à jour de valeur, de la réutilisation, de la déliaison et du désabonnement final. Chaque modèle reste abonné dans le cache pendant 20 secondes afin de faciliter l'application des modèles et d'améliorer légèrement la vitesse lorsque vous passez d'une vue à l'autre ou utilisez le même modèle sur des cartes de vues différentes.

## Vérifier un modèle

Si un modèle ne fonctionne pas, vérifiez les noms d’entités, les valeurs `none` inattendues et les chaînes YAML. Procédez ainsi :

1. Remplacez temporairement le résultat du modèle par une valeur fixe.
2. Vérifiez que la règle CSS fonctionne avec cette valeur.
3. Rétablissez la condition du modèle.
4. Contrôlez les guillemets et les types de données.

Un modèle qui ne produit aucune valeur peut générer du CSS invalide. Prévoyez alors une valeur de repli.

## Exemples complémentaires de la référence allemande {#german-reference-examples}

:::: details Afficher les configurations complémentaires
Ces configurations complètent la référence traduite ci-dessus. Elles reprennent les exemples techniques de la [page allemande](/projects/uix/debugging/templates). Les clés, expressions, valeurs et textes de démonstration sont conservés tels quels ; remplacez les entités par les vôtres. Les limites de version indiquées dans la référence restent applicables.

### 1. Exemple {#reference-example-1}

```yaml
uix:
  style: |
    ha-card {
      opacity: {{ 1 if is_state('light.bed_light', 'on') else 0.4 }};
    }
```

::::
