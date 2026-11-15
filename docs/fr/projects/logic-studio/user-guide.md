# Guide d’utilisation

Ce guide s’adresse aux débutants. Ouvre HA Logic Studio Pro dans Home Assistant, sélectionne **Nouveau projet**, puis choisis un éditeur et un nom. Pour les exemples, crée un interrupteur dans **Paramètres → Appareils et services → Entrées**. Les exemples utilisent `input_boolean.studio_test`. Utilise l’identifiant réel de ton entrée.

## Quel éditeur choisir ?

- **Plan fonctionnel** pour les signaux, minuteries et compteurs sur un canevas.
- **Rules** pour les règles SI → ALORS ou SINON.
- **Blocks A** pour assembler des automatisations Home Assistant à partir de blocs.
- **Blocks JS** pour assembler des scripts et importer des projets ioBroker.
- **JavaScript** ou **TypeScript** pour écrire des scripts.
- **HA-YAML** pour modifier, vérifier et visualiser des automatisations et des scripts.

## Commandes communes

- **Enregistrer** conserve les modifications. Le bouton orange signale des modifications en attente. Le bouton gris indique que tout est enregistré.
- **Annuler** abandonne les modifications depuis le dernier enregistrement et restaure la version enregistrée.
- **Test** utilise la simulation dans les éditeurs de scripts. Dans le plan fonctionnel, tu peux basculer les entrées simulées.
- **Play** démarre la version enregistrée dans le moteur d’exécution pour le plan fonctionnel, Blocks JS, JavaScript et TypeScript. Les actions HA autorisées peuvent y modifier les entités réelles. **Stop** arrête l’exécution.
- **Vérifier** indique les problèmes avant l’export ou l’exécution. **Exporter** crée un fichier que tu peux utiliser dans Home Assistant.
- Le **mode expert** du menu du projet affiche des outils supplémentaires. Le **journal** affiche les résultats et les erreurs du projet ouvert.

## Éditeurs

- [Plan fonctionnel](./user-guide/function-plan)
- [Rules](./user-guide/rules)
- [Blocks A](./user-guide/blocks-a)
- [Blocks JS](./user-guide/blocks-js)
- [JavaScript](./user-guide/javascript)
- [TypeScript](./user-guide/typescript)
- [HA-YAML](./user-guide/ha-yaml)
- [Signaler un problème et contribuer](./user-guide/feedback)
