# Blocks JS

## Déclencheur d’état à plusieurs branches {#zustandstrigger-reihenfolge}

1. Dans **Déclencheurs → Si la valeur de l’entité change**, sélectionner l’entité.
2. Choisir **État** ou **Attribut**. Pour un volet, utiliser par exemple `current_position` ; `mi-ouvert` n’est un état que si l’entité fournit réellement ce texte.
3. Modifier les branches on/off. Choisir **Texte** ou **Nombre** pour chaque branche, par exemple `50` pour une position intermédiaire.
4. Glisser **autre état** dans l’éditeur à engrenage et ajouter éventuellement **sinon**. Le réordonnement conserve les actions associées. Les doublons empêchent le démarrage.
5. Placer les actions dans les branches, enregistrer puis démarrer **Play**. Un changement exécute la branche correspondante ; le simple démarrage ne la déclenche pas.

Les blocs existants de nouvelle/ancienne valeur fonctionnent aussi dans les branches d’état et d’attribut. Dans **Logique**, les valeurs de comparaison proposent on/off en plus des booléens vrai/faux.

**Écrire avant de lire :** les deux blocs de capteur JS attendent la confirmation HA avant les blocs suivants. Le débogage lit donc `1.5` après `on` et `0` après `off`. Les sorties HA normales attendent l’acceptation de la demande ; temporisateurs et callbacks explicites restent indépendants.

Les champs sont validés à la perte de focus sans Entrée. L’ancien code actif est signalé : **Enregistrer → Redémarrer le runtime**. À gauche du journal, **Vider le journal** retire les messages locaux et persistés de ce projet sans arrêter le processus. Les nouveaux messages restent enregistrés.

**Vérification :** 99 tests locaux, dont l’export dans le véritable runtime QuickJS avec réponses HA simulées et retardées. Aucun test réel sur HA pour 0.1.136 ; projets et autorisations conservés.

## Déclencheurs de changement et sélection d’entités {#entitaetsauswahl-kompakte-trigger}

Dans **Déclencheurs**, choisir un déclencheur pour une entité, plusieurs entités ou un attribut. Depuis **0.1.135**, ces blocs utilisent des lignes verticales compactes. Les longs libellés sont raccourcis ; les identifiants enregistrés restent complets.

1. Cliquer sur le champ d’entités du déclencheur multiple. Rechercher par nom ou identifiant ; sélectionner ou désélectionner plusieurs résultats.
2. **Appliquer** enregistre la sélection. **Fermer** abandonne les changements non confirmés. Les listes séparées par des virgules ou des espaces restent compatibles.
3. Utiliser la condition **a changé** et placer la logique et les sorties de débogage dans le déclencheur.
4. Enregistrer puis démarrer **Play**. Le contenu est exécuté à nouveau lorsque l’état change. Les blocs isolés ne s’exécutent qu’au démarrage.

La sélection n’accorde aucune autorisation runtime. Les entités surveillées nécessitent READ ; les cibles d’écriture nécessitent toujours WRITE. Pour un interrupteur, **État de l’entité** renvoie `on`/`off`. **Entité présente** vérifie uniquement l’existence.

**Vérifié :** 285 blocs, 51 champs d’entités directs et 80 tests locaux. Sélection et lignes compactes vérifiées en DE/EN/FR ; aucun test réel sur HA pour 0.1.135.

## Définir l’état du capteur {#sensorzustand-setzen}

### Saisir directement un nombre décimal {#sensor-dezimalzahl}

Depuis **0.1.134** : choisir **System → Définir l’état du capteur · Nombre décimal**, sélectionner un capteur et saisir directement la valeur. Valeur par défaut `0.5` ; saisir par exemple `33.25` avec un point décimal. Aucun arrondi à un entier ; les valeurs restent enregistrées après rechargement. Le bloc avec entrée de valeur reste disponible. Autorisation WRITE et attributs traités de la même façon. Blocks A nécessite l’application Studio active.

**Vérifié :** 72 tests locaux et, après sauvegarde sur HA 2026.11.3, `0.5` et `33.25` via Play dans Blocks JS et via les données d’événement générées et vérifiées de Blocks A. Les deux champs ont été confirmés après rechargement ; réglages et attributs conservés.

À partir de **0.1.133**, **System** propose **Définir l’état du capteur**. Sélectionne un `sensor.*` existant avec le sélecteur de style HA et connecte un nombre, un texte ou un calcul à l’entrée de valeur. Les nombres doivent être finis ; les textes sont limités à 255 caractères.

Le capteur nécessite l’autorisation WRITE, par exemple dans `runtime_write_entities`. Exemple de code généré :

```js
ha.setSensorState("sensor.example", 40 + 2);
```

**Test** simule l’écriture. **Enregistrer → Play** l’exécute dans le moteur Studio. L’unité, la classe d’appareil et les autres attributs sont conservés. Aucun appareil n’est commandé et aucun capteur permanent n’est créé. L’intégration responsable peut remplacer la valeur ultérieurement. Les autorisations WRITE manquantes et les erreurs d’écriture apparaissent dans le journal d’exécution.

Lors du test réel sur HA après sauvegarde, le calcul a produit **42 W**. Une écriture ultérieure a été refusée après retrait de l’autorisation temporaire ; les autorisations initiales ont été conservées.

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

### Vérifier si un ID ioBroker calculé existe

Si ton script ioBroker construit un ID à partir de plusieurs fragments de texte, utilise le bloc importé `state_exists_var` pour le vérifier.

1. Dans la vérification de l’import, saisis l’ID ioBroker calculé complet et l’ID d’entité HA correspondant dans **Correspondance des ID (JSON)**, par exemple `{"0_userdata.0.jardin.pompe":"switch.pompe_jardin"}`. Ce champ est aussi disponible dans le bloc importé.
2. Autorise l’entité associée dans `runtime_read_entities` dans les réglages de l’application si elle ne dispose pas encore d’une autorisation d’écriture.
3. Enregistre le projet et clique sur **Play**. Une entité HA existante renvoie `true`. Une entité associée mais absente renvoie `false`. Si aucune association n’existe pour l’ID calculé, l’exécution s’arrête et le journal indique cet ID. Ajoute l’association dans le bloc, puis relance le projet.

### Importer un point de données ioBroker comme assistant HA

Si ton export Blockly contient le bloc de création d’un point de données (`createState`), tu peux stocker sa valeur dans un assistant Home Assistant. L’assistant apparaît dans **Paramètres → Appareils et services → Assistants**.

1. Dans les outils experts, ouvre l’import ioBroker, colle l’export et vérifie l’importation.
2. Choisis l’une des trois options pour l’identifiant ioBroker :
   - **Associer un assistant** utilise un assistant existant et conserve sa valeur actuelle.
   - **Créer un assistant** propose un interrupteur, un assistant numérique ou un assistant texte selon le type de données. Vérifie et confirme le nom. La création nécessite un compte administrateur HA. Une valeur initiale fixe compatible est appliquée une seule fois. Pour une valeur initiale calculée, tu peux préparer un assistant dans HA puis l’associer.
   - **Associer plus tard** laisse l’association en attente. Ouvre le projet et sélectionne une entité HA compatible dans le bloc importé avant de lancer le script.
3. Vérifie que les blocs de création, de lecture et de mise à jour du même identifiant ioBroker utilisent la même entité HA. Ouvre l’import comme projet et enregistre-le.
4. Autorise l’assistant dans les options de l’application sous `runtime_read_entities` et, pour les mises à jour, sous `runtime_write_entities`. Lance le script enregistré avec **Play**. Le script lit la valeur actuelle de l’assistant, y compris après une modification dans Home Assistant.

L’exemple crée un assistant numérique avec **17**. Au premier lancement, le script journalise **17** et écrit **42**. Après le redémarrage du script, le journal affiche **42**. Tu peux ainsi vérifier que la valeur initiale a été appliquée uniquement à la création de l’assistant. [Exemple Blockly](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/ha-logic-studio-pro-v0.1.122/ha_logic_studio_pro/tests/fixtures/iobroker-create-state.xml)

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
