# Rules

## Premier exemple

Dans l’assistant, choisis un déclencheur d’état, ton entrée de test et `on`. Ajoute une action ALORS pour activer une seconde entrée. Exporte le YAML et vérifie-le dans HA.

## Fonctions

### Assistant et palette

L’assistant guide la création. Tu peux aussi chercher et glisser un élément de la palette vers la section voulue.

### Déclencheurs

Choisis un état avec valeurs avant/après, attribut et durée, un seuil, une heure fixe ou issue d’une entrée, le soleil avec décalage, MQTT, un événement HA, le démarrage de HA, une zone ou une étiquette.

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
