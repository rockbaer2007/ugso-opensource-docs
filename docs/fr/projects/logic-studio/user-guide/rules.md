# Rules

## Créer une règle pour la lumière du couloir

### 1. Créer le projet

Choisis **Nouveau projet → Rules**, donne un nom au projet et ouvre l’**assistant**. Il comprend quatre étapes pour le déclencheur, les conditions, les actions et la vérification.

### 2. Définir le déclencheur

Choisis un déclencheur d’état. Saisis l’identifiant de ton capteur de mouvement ou de ta première entrée de test. La démo utilise `binary_sensor.bewegung`. Saisis `on` comme état d’arrivée et laisse l’état de départ, l’attribut et la durée minimale vides. Clique sur **Suivant**.

[![Déclencheur d'état dans l'assistant Rules, interface allemande](/images/logic-studio/user-guide/rules-trigger-de.jpg)](/images/logic-studio/user-guide/rules-trigger-de.jpg)

### 3. Passer les conditions

Avance sans ajouter de condition. Une condition sert à vérifier un critère supplémentaire, par exemple l’heure de la journée. Ici, le changement d’état suffit.

### 4. Ajouter une action

Dans **ALORS**, ajoute une action HA. Choisis `light.turn_on` et sélectionne la lampe de test comme cible. Dans la démo, c’est `light.flur`. Avec une deuxième entrée de test de type interrupteur, utilise `input_boolean.turn_on`. Laisse **SINON** vide, puis avance.

### 5. Vérifier le YAML

Sous `triggers`, vérifie l’entité et `to: "on"`. Sous `actions`, vérifie l’action et la cible. Applique les réglages, enregistre la règle, puis ouvre-la en YAML HA pour contrôler et exporter le brouillon.

### 6. Tester dans Home Assistant

Ajoute l’automatisation vérifiée à Home Assistant. Mets l’entité déclencheuse à `off`, puis à `on`. Vérifie que la bonne cible s’allume. La trace d’automatisation indique quel déclencheur et quelle action ont été exécutés.

[![Éditeur Rules avec le déclencheur d’état dans SI et l’action d’allumage dans ALORS](/images/logic-studio/user-guide/rules-walkthrough-fr.jpg)](/images/logic-studio/user-guide/rules-walkthrough-fr.jpg)

## Fonctions

### Assistant et palette

L’assistant guide la création. Tu peux aussi chercher et glisser un élément de la palette vers la section voulue.

### Déclencheurs

Choisis un état avec valeurs avant/après, attribut et durée, un seuil, une heure fixe ou issue d’une entrée, le soleil avec décalage, MQTT, un événement HA ou le démarrage de HA. Les zones et étiquettes regroupent les entités sélectionnées.

### Conditions

Vérifie un état, un nombre, un attribut, une heure ou un jour. ET exige toutes les conditions, OU au moins une et NON inverse le résultat.

### Déclenché par

Donne aux déclencheurs des identifiants comme `first` et `second`. Vérifie l’identifiant pour choisir entre ALORS et SINON.

### Modèle

En mode expert, ajoute une condition de modèle native HA. Son résultat indique si la condition est remplie.

### Actions et branches

Ajoute les actions dans l’ordre souhaité. Choisis une cible et des paramètres, ajoute un délai, attends un état, appelle un script ou envoie une notification.

### YAML et JSON Rules

Utilise le YAML dans HA et le JSON Rules pour rouvrir la règle dans l’éditeur.

## En cas de problème

Un seuil se déclenche à nouveau après une sortie puis une nouvelle entrée dans la plage.
