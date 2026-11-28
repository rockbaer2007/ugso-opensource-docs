# JavaScript

Depuis **0.1.136**, les API d’écriture HA renvoient des promesses. Pour garantir l’ordre, utiliser `await ha.setSensorState("sensor.example", 1.5);` puis lire avec `ha.readState("sensor.example")`. L’API du capteur attend la confirmation HA et fournit la valeur confirmée dans l’état lisible. `await ha.callAction(...)` attend l’acceptation de la demande, pas un mouvement physique de l’appareil. Temporisateurs et callbacks explicites restent des continuations indépendantes. 99 tests locaux réussis ; Test réel supplémentaire le 28 novembre 2026 après sauvegarde complète sur HA 2026.11.3 (.193, port 80) : branches d’état/d’attribut de Blocks JS, écriture avant débogage, saisie décimale sans Entrée, avertissement d’ancien code et effacement du journal. Valeurs de test restaurées, projets et autorisations conservés ; exemples arrêtés. [Résultats du test réel](../#zustandstrigger-reihenfolge).

## Premier exemple

Une ligne de code écrit un message dans le journal.

1. Choisis **Nouveau projet → JavaScript** et remplace le code d’exemple par `ha.log('Studio-Test');`.
2. Lance le **test** en haut à droite. Tu peux essayer le code avant de l’enregistrer.
3. Dans le **journal**, cherche `Studio-Test` dans le champ `message`. Clique sur **Enregistrer** pour conserver le brouillon.

[![Test JavaScript affichant Studio-Test dans le journal](/images/logic-studio/user-guide/javascript-fr.png)](/images/logic-studio/user-guide/javascript-fr.png)

## Fonctions

### Complétion et signatures

Commence à écrire un nom d’API pour afficher les suggestions et les arguments attendus.

### Valeurs de test et simulation

Utilise des états simulés et vérifie les résultats et les erreurs.

### Ligne d’erreur

Va à la ligne indiquée dans le code source et examine l’expression.

### Fonctions globales

Exporte une fonction d’un script global et sélectionne ce script dans le projet qui l’utilise.

### Play et démarrage automatique

Enregistre, puis lance Play. Active le démarrage automatique par projet si le projet doit redémarrer après un redémarrage de l’application.

### Journal d’exécution

Consulte les entrées après un redémarrage de l’application. Leur durée et leur taille sont limitées.

## En cas de problème

Si HA refuse une action, vérifie les cibles et actions autorisées dans les options.
