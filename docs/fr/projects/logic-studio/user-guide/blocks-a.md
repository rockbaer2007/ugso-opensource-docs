# Blocks A

**Portée de 0.1.136 :** le nouveau déclencheur d’état et l’ordre automatique avec confirmation concernent **Blocks JS**. Le YAML de Blocks A conserve son pont d’événements natif. Les deux variantes de capteur restent disponibles ; autorisations et projets enregistrés conservés. La validation sans Entrée et **Vider le journal** appartiennent à l’interface commune du Studio. 99 tests locaux réussis ; aucun test réel sur HA pour 0.1.136.

**0.1.135 :** Les 51 champs d’entités directs des 285 blocs enregistrés dans Blocks A/JS ont été vérifiés pour la sélection HA. Le nouveau sélecteur multiple et les déclencheurs compacts concernent Blocks JS. Les champs de cibles HA structurés, les listes et les associations enregistrées dans Blocks A sont conservés. 68 tests Node et 12 tests serveur réussis ; aucun test réel sur HA pour cette version.

## Définir l’état du capteur {#sensorzustand-setzen}

### Saisir directement un nombre décimal {#sensor-dezimalzahl}

Depuis **0.1.134** : choisir **System → Définir l’état du capteur · Nombre décimal**, sélectionner un capteur et saisir directement la valeur. Valeur par défaut `0.5` ; saisir par exemple `33.25` avec un point décimal. Aucun arrondi à un entier ; les valeurs restent enregistrées après rechargement. Le bloc avec entrée de valeur reste disponible. Autorisation WRITE et attributs traités de la même façon. Blocks A nécessite l’application Studio active.

**Vérifié :** 72 tests locaux et, après sauvegarde sur HA 2026.11.3, `0.5` et `33.25` via Play dans Blocks JS et via les données d’événement générées et vérifiées de Blocks A. Les deux champs ont été confirmés après rechargement ; réglages et attributs conservés.

À partir de **0.1.133**, **System** propose **Définir l’état du capteur** :

1. Sélectionne un `sensor.*` existant avec le sélecteur d’entités de style HA.
2. Connecte un nombre, un texte ou un calcul à l’entrée de valeur (état de 255 caractères maximum).
3. Autorise le capteur dans **WRITE – cibles individuelles** (`runtime_write_entities`) dans la configuration de l’application. Conserve les entrées existantes. READ seul ne suffit pas.
4. Choisis **Vérifier les blocs → Ouvrir en YAML HA**. Vérifie puis installe toi-même l’automatisation dans Home Assistant.

Exemple d’action générée :

```yaml
actions:
  - event: logic_studio_set_sensor_state
    event_data:
      entity_id: sensor.example
      state: 43
```

L’application Studio active reçoit l’événement et vérifie WRITE. Sans l’application, il n’est pas traité. Cette entrée interne ne nécessite pas d’autorisation EVENT générale. Les erreurs apparaissent dans le journal de l’application ; émettre l’événement ne confirme pas la réussite de l’écriture.

Le bloc conserve l’unité, la classe d’appareil et les autres attributs. Il correspond à **Outils de développement → États**, ne commande aucun appareil et ne crée aucun capteur permanent. L’intégration responsable peut remplacer la valeur ultérieurement. L’aperçu YAML n’écrit rien.

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
