---
title: ioBroker Blockly
description: Introduction à Blockly, intégré à l'adaptateur JavaScript d'ioBroker, à travers un exemple de démarrage officiel.
---
<a id="statut"></a>


# ioBroker Blockly {#iobroker-blockly}

Blockly est l'éditeur de scripts graphique de l'**adaptateur JavaScript d'ioBroker**. Les automatisations sont construites à l'aide de blocs, ce qui évite d'avoir à rédiger manuellement l'intégralité du code JavaScript.

::: info Documentation officielle
Cette page ne propose qu'une brève introduction. La description complète de tous les blocs ainsi que d'autres exemples sont disponibles dans la documentation officielle d'ioBroker.
:::

## Sources officielles {#offizielle-quellen}

- [ioBroker.javascript – dépôt officiel](https://github.com/ioBroker/ioBroker.javascript)
- [Documentation de l'adaptateur JavaScript (en allemand)](https://github.com/ioBroker/ioBroker.javascript/tree/master/docs/de)
- [Documentation complète de Blockly](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md)

## Exemple 1 : Commuter un point de données en fonction d'un autre point de données {#beispiel-1-datenpunkt-abhangig-von-einem-anderen-datenpunkt-schalten}

L'exemple d'introduction officiel illustre un scénario typique de détection de mouvement :

- Un point de données lié au mouvement sert de déclencheur.
- Lors d'un changement d'état, un point de données lié à l'éclairage est piloté.
- La valeur actuelle du détecteur de mouvement est transmise au point de données de l'éclairage.
- La détection d'un mouvement allume la lumière.
- L'absence de mouvement éteint la lumière.

[![Exemple Blockly officiel n° 1 pour ioBroker](https://raw.githubusercontent.com/ioBroker/ioBroker.javascript/master/docs/de/img/getting_started_1_de.png)](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md#beispiel-1)

<small>
Source de l'image et droits : L'image provient du dépôt officiel
<a href="https://github.com/ioBroker/ioBroker.javascript" target="_blank" rel="noopener">ioBroker.javascript</a>.
Les droits et les conditions de licence sont régis par le projet qui y est publié et par sa licence associée.
</small>

## Blocs Blockly nécessaires {#benotigte-blockly-blocke}

### 1. Déclencheur (Trigger) {#_1-trigger}

Dans la catégorie **Déclencheur** (Trigger), on utilise le bloc **Si objet** (Falls Objekt).

On y sélectionne le point de données correspondant au détecteur de mouvement.

### 2. Piloter un point de données {#_2-datenpunkt-steuern}

Dans la catégorie **Système**, on insère le bloc **Piloter** (Steuere).

Le point de données correspondant à l'éclairage est sélectionné comme cible.

### 3. Récupérer la valeur {#_3-wert-ubernehmen}

Le bloc « commander » (ou « piloter ») intègre la **valeur de l'ID d'objet**.

On y sélectionne à nouveau le point de données correspondant au mouvement. Ainsi, l'éclairage adopte l'état actuel (Vrai/Faux) du détecteur de mouvement.

## Processus simplifié {#vereinfachter-ablauf}

```text
Falls sich der Bewegungsmelder ändert
    setze den Zustand des Lichts
    auf den aktuellen Wert des Bewegungsmelders
```

## Importer le bloc Blockly {#blockly-importieren}

Le code XML complet, prêt à être importé, est fourni dans la documentation officielle, juste en dessous de l'**Exemple 1** :

[Ouvrir l'Exemple 1 avec le code XML Blockly](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md#beispiel-1)

Il suffit de copier ce code XML et de l'insérer dans l'éditeur Blockly via la fonction d'importation.

## Autres exemples officiels {#weitere-offizielle-beispiele}

La documentation officielle propose également :

- **Exemple 2 :** Allumer la lumière en cas de détection de mouvement et l'éteindre après dix minutes sans nouveau mouvement.
- **Exemple 3 :** Envoyer un e-mail lorsque la température extérieure dépasse un certain seuil.

[Voir tous les exemples officiels Blockly](https://github.com/ioBroker/ioBroker.javascript/blob/master/docs/de/blockly.md#getting-started)

## Partager vos propres exemples Blockly sur le blog {#eigene-blockly-beitrage-im-blog}

Pour vos propres exemples, la structure suivante est recommandée :

1. Décrire la tâche
2. Indiquer les ID d'objets nécessaires
3. Insérer une capture d'écran de la configuration Blockly
4. Fournir le code XML Blockly exporté
5. Expliquer les adaptations et les prérequis

Les captures d'écran sont stockées dans le projet de documentation ici :

```text
docs/public/images/blog/
```

Intégration dans l'article :

```md
![ioBroker Blockly](/images/blog/mein-blockly.png)
```

::: warning
Les ID d'objets présents dans les exemples doivent toujours être adaptés à votre propre système ioBroker.
:::
