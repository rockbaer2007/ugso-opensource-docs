# Blocks JS

## Premier exemple

Le test lit l’état simulé d’une entité et l’affiche dans le journal.

1. Choisis **Nouveau projet → Blocks JS**. Dans **Système**, glisse le bloc **Journal** sur le canevas.
2. Glisse **État de** dans l’entrée libre du bloc de journal. Choisis ton entité de test. La capture utilise `binary_sensor.bewegung`.
3. Lance un **test** et consulte le **journal**. La démonstration affiche l’état et le message `on`. Le script lit et affiche la valeur.

[![Blocks JS avec un bloc d’état relié au journal](/images/logic-studio/user-guide/blocks-js-fr.png)](/images/logic-studio/user-guide/blocks-js-fr.png)

## Fonctions

### Système, actions et Sendto

Lis des états, commande des cibles autorisées, envoie des messages ou consulte l’historique. Une entrée dynamique peut accepter un identifiant obtenu dans une boucle.

### Déclencheurs, temps et temporisations

Démarre sur changement d’état, événement solaire ou horaire. Utilise des règles CRON simples ou nommées, des délais, des intervalles et leurs blocs d’arrêt.

### Blocs de valeurs

Les catégories conversion, objet, logique, mathématiques, texte, listes et couleur produisent des valeurs. Les boucles répètent des opérations.

### Variables et fonctions

Les variables conservent des valeurs intermédiaires. Les fonctions regroupent des étapes et peuvent renvoyer une valeur.

### Import ioBroker

Colle l’export en mode expert et lis le rapport. Associe explicitement les entités et consulte les indications de chaque bloc.

### Blocs HTTP importés

Choisis une commande REST HA autorisée. Configure l’URL, le délai et les en-têtes dans HA. Le bloc POST indique le Content-Type importé.

### Test et Play

Commence par la simulation. Enregistre avant Play et vérifie les résultats réels dans le journal.

## Vérifier un import étape par étape

1. Active le **mode expert** dans le menu du projet. Dans l’éditeur, ouvre les outils experts et choisis l’import ioBroker.
2. Colle le XML Blockly ou un export JavaScript ioBroker contenant les données Blockly. Vérifie l’import et repère les blocs à associer.
3. Ouvre l’import comme projet et suis les indications affichées sur les blocs concernés. Pour un POST importé, choisis la commande REST HA qui définit les en-têtes et le délai.
4. Enregistre et lance d’abord un **test**. Utilise ensuite **Play** pour l’exécution réelle, vérifie le **journal** et termine avec **Stop**.

## En cas de problème

Adapte les blocs signalés avant l’exécution.
