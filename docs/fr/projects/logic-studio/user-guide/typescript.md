# TypeScript

## Premier exemple

La capture montre une erreur volontaire. Une variable de type `number` reçoit le texte `'42'`.

1. Choisis **Nouveau projet → TypeScript** et saisis le code affiché. La deuxième ligne, `ha.log(String(zahl));`, écrit la valeur sous forme de texte.
2. Lance un **test**. Le journal indique qu’un texte ne peut pas être affecté à un nombre. Utilise le lien vers la ligne 1 pour retrouver l’erreur.
3. Retire les guillemets autour de `42` et relance le test. Le journal affiche `42`.

[![Erreur de type dans une affectation TypeScript et lien vers la ligne 1](/images/logic-studio/user-guide/typescript-fr.png)](/images/logic-studio/user-guide/typescript-fr.png)

## Fonctions

### Types

Un type indique les valeurs autorisées. `number` attend un nombre et `string` du texte.

### Vérification des types

Elle contrôle les déclarations, les affectations et les appels. Corrige la ligne marquée et relance la vérification.

### Complétion et signatures

Suis les suggestions de l’API et vérifie les arguments attendus.

### Test et erreurs

Teste avec des valeurs simulées. Les erreurs d’exécution renvoient à la ligne TypeScript d’origine.

### Fonctions globales et démarrage automatique

Choisis les fonctions exportées par les scripts globaux et configure le démarrage automatique par projet.

### Play et journal

Enregistre avant Play. Consulte les résultats et les erreurs dans le journal.

## En cas de problème

Convertis en nombre le texte lu dans un état avant de calculer.
