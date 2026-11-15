# Blocks A

## Premier exemple

L’automatisation allume la lumière du couloir lorsque le capteur de mouvement passe à `on`.

1. Choisis **Nouveau projet → Blocks A** et donne un nom au projet. Le bloc **Automatisation** apparaît sur le canevas.
2. Ouvre **Déclencheurs** et glisse un déclencheur d’état dans **Quand**. La capture utilise `binary_sensor.flur_bewegung` et l’état `on`. Choisis ton propre capteur ou une entrée de test.
3. Ouvre **Actions** et place une action dans **Alors**. La capture utilise `light.flur` et **allumer**. Tu peux choisir une deuxième entrée de test comme cible. Laisse **Seulement si** vide pour cet exemple.
4. Clique sur le drapeau pour vérifier les blocs. Si la vérification réussit, choisis **Ouvrir en YAML HA** et contrôle `triggers` et `actions` avant d’exporter.

[![Blocks A avec un déclencheur dans Quand et une action dans Alors](/images/logic-studio/user-guide/blocks-a-fr.png)](/images/logic-studio/user-guide/blocks-a-fr.png)

## Fonctions

### Palette et connexions

Choisis un bloc selon son rôle. La forme des connexions indique où placer une valeur ou une action.

### Déclencheurs et conditions

Un déclencheur démarre l’automatisation. Une condition peut vérifier si l’autre entrée est désactivée.

### Actions

Empile les actions dans leur ordre d’exécution.

### Sélecteurs HA

Choisis une entité, une action, un appareil, une zone, une étiquette ou un étage. Vérifie l’identifiant correspondant dans le YAML.

### Brouillon HA-YAML

Ouvre l’automatisation générée en brouillon. Le nom de son projet source y est affiché.

### Export

Vérifie le YAML et utilise-le dans HA. Teste le déclencheur et consulte la trace de l’automatisation.

## En cas de problème

Si une liste est vide, vérifie que le système HA connecté contient les éléments recherchés.
