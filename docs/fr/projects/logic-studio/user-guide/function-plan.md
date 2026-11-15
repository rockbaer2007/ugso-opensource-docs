# Plan fonctionnel

## Inverser un signal dans le plan fonctionnel

### 1. Ouvrir le plan et ajouter les blocs

Ouvre le plan fonctionnel dans l’arborescence. Cherche successivement `STATE_IN`, `NOT` et `STATE_OUT` dans la palette et clique sur chacun pour l’ajouter. Déplace les blocs par leur en-tête pour les placer de gauche à droite dans cet ordre.

### 2. Configurer l’entrée

Ouvre les propriétés de `STATE_IN` avec l’icône en forme de roue dentée. Saisis l’identifiant de ton capteur ou de ton entrée de test. La démo utilise `binary_sensor.bewegung`. Sélectionne le type `BOOL` et la valeur de démonstration `TRUE`.

### 3. Configurer la sortie

Dans les propriétés de `STATE_OUT`, saisis un identifiant de cible adapté. La démo utilise `light.flur`. Laisse le mode de sortie sur `BOOL`. Un signal booléen vaut `TRUE` ou `FALSE`.

### 4. Relier les broches

Glisse de la broche ronde **Q** de `STATE_IN` vers **IN** sur `NOT`. Relie ensuite **OUT** de `NOT` à **IN** sur `STATE_OUT`. Le canevas doit afficher trois blocs et deux connexions.

### 5. Lancer la simulation

Clique sur **Simuler**, l’icône en forme de fiole. L’entrée affiche `Demo: true`. Le bloc `NOT` inverse cette valeur et `STATE_OUT` affiche `Demo: false`. La simulation utilise des valeurs de démonstration et laisse la lampe réelle intacte.

### 6. Tester l’autre valeur

Règle la valeur de démonstration sur `FALSE`, puis simule à nouveau. La sortie doit afficher `true`. Le bouton de réinitialisation efface l’état de la simulation. Enregistre le projet pour conserver le plan.

[![Plan fonctionnel avec STATE_IN, NOT et STATE_OUT. L’entrée simulée est vraie et la sortie est fausse.](/images/logic-studio/user-guide/function-plan-walkthrough-fr.jpg)](/images/logic-studio/user-guide/function-plan-walkthrough-fr.jpg)

Si une liaison est refusée, vérifie les types des broches. S’il manque un identifiant d’entité, vérifie les propriétés de l’entrée et de la sortie. Utilise le bouton de simulation pour cet exercice. **Play** dans la barre du projet lance le moteur d’exécution.

## Fonctions

### Canevas

Déplace et relie les blocs. Utilise le zoom ou ajuste la vue à tout le plan.

### Paramètres

Sélectionne un bloc pour régler la durée d’une minuterie ou la cible d’un compteur.

### Liaisons HA

Choisis une entité pour le signal et une action HA autorisée pour la sortie.

### Simulation

Bascule les entrées simulées et observe les valeurs aux broches.

### Point d’arrêt et pas à pas

Mets la simulation en pause et avance d’un cycle pour examiner les valeurs.

### Disposition et épinglage

Organise le plan tout en conservant la position des blocs épinglés.

### Play et diagnostic en direct

Lance le plan enregistré et examine les valeurs et les erreurs.

### Compteurs et mémoires persistants

Active la sauvegarde pour conserver leurs valeurs après un redémarrage. Une modification du plan peut les réinitialiser.

## En cas de problème

Si une liaison est refusée, compare les types des broches.
