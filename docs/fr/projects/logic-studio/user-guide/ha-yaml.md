# HA-YAML

## Premier exemple

Ouvre une petite automatisation en brouillon YAML. Passe à la vue graphique, repère le déclencheur et les actions, puis reviens au YAML pour vérifier et exporter.

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
