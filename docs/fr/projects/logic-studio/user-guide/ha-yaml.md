# HA-YAML

## Premier exemple

Le modèle présente une automatisation qui allume la lumière du couloir lorsqu’un mouvement est détecté.

1. Choisis **Nouveau projet → HA-YAML**, sélectionne **Automatisation HA**, ouvre le modèle et donne un nom au brouillon.
2. Sélectionne **YAML**. `triggers` contient le déclencheur d’état. `actions` contient `light.turn_on` avec `light.flur` comme cible. Remplace les identifiants par ceux de ton système pour utiliser l’exemple dans HA.
3. Clique sur **Valider**. Si une ligne est marquée, lis le diagnostic et corrige cette ligne.
4. Passe à **Graphique**. La liaison relie le détecteur à l’action d’allumage. **Exporter** enregistre le YAML dans un fichier.

[![Source HA-YAML montrant le déclencheur, l’action et la cible](/images/logic-studio/user-guide/ha-yaml-source-fr.png)](/images/logic-studio/user-guide/ha-yaml-source-fr.png)

[![Vue graphique reliant le déclencheur de mouvement à l’action](/images/logic-studio/user-guide/ha-yaml-graph-fr.png)](/images/logic-studio/user-guide/ha-yaml-graph-fr.png)

## Fonctions

### Import YAML et JSON

Ouvre ou colle du YAML. L’import JSON accepte les données d’automatisation HA et les exports FLODE compatibles.

### Syntaxe et structure

Les couleurs facilitent la lecture. La vérification marque les erreurs de syntaxe, entités inconnues, champs d’action invalides et problèmes de structure dans `choose`.

### Sélecteurs

Place le curseur à l’endroit voulu, puis sélectionne une entité ou une action pour insérer son identifiant.

### Vue graphique

Déplace, zoome ou ajuste la vue. Les sorties nommées de `choose` indiquent les branches.

### Export YAML et JSON

Utilise le YAML dans HA et la vue JSON pour exporter le JSON. Un brouillon YAML inchangé peut conserver les champs inconnus et les données Blueprint.

### Lien HA

Associe éventuellement une automatisation ou un script existant pour afficher son état et utiliser les commandes disponibles.

## En cas de problème

Vérifie les retraits et les noms des champs aux lignes marquées. Modifie le YAML pour changer le graphe.
