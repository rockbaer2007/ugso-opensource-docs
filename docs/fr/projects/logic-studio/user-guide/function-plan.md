# Plan fonctionnel

## Premier exemple

Ajoute une entrée numérique et une sortie dans un nouveau plan. Relie les broches, lance la simulation et bascule l’entrée. La sortie doit suivre.

Le canevas affiche les blocs reliés et une mini-carte en bas à droite.

![Plan fonctionnel avec blocs reliés et mini-carte](/images/logic-studio/0.1.8-react-flow-193.jpg)

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
