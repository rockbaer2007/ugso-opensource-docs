---
title: Runtime et cycle de vie
description: Contrat des plugins Runtime et cycle de vie des modules ATLAS.
---
# Runtime et cycle de vie

ATLAS Runtime fournit un contrat de plugin en TypeScript. Un plugin possède un manifeste et une méthode asynchrone `activate`. `createRuntimeModuleFromPlugin()` adapte ce contrat à un module Runtime.

## Contrat vérifié et compatibilité

Au 16/10/2026 : App **0.1.312**, package `@atlas/runtime` **0.2.0-alpha.39**.
La référence A5 ci-dessous est historique. Restaurations natives complémentaires
et versions HA sont décrites dans [Versions et compatibilité](./compatibility).

Référence de la revue A5 : application HA `0.1.297`, Runtime `0.2.0-alpha.38`. Les régressions couvrent activation, arrêt/libération, catalogue, lecture des paquets et installation/restauration isolée du backend. Elles ne garantissent ni une API 1.0 stable ni toutes les versions d’hôte/HA.

- Les hooks Runtime concernent les plugins Runtime enregistrés dans l’hôte. Installer un plugin web statique n’exécute pas automatiquement `activate`/`deactivate`/`dispose`.
- Les points d’extension et fonctions fournies décrivent les plugins et permettent leur recherche dans le catalogue. Les capacités déclarées ne constituent pas une sandbox et n’accordent aucun accès aux fichiers ou secrets.
- L’état d’activation enregistré contrôle le Hub et les liens de lancement. Il ne bloque pas les fichiers bruts du plugin.

Conserver les identifiants publiés et augmenter la version du paquet à chaque modification publiée. Lors d’un changement de contrat, vérifier les formats de paquet/import pris en charge, le cycle de vie et la conservation des données ; documenter les migrations nécessaires et leurs effets dans les notes de version. Une matrice complète des versions/compatibilités reste une qualification ultérieure. Évaluer séparément le contrat Runtime et les formats de dépôt/paquet web.

## Plugin Runtime minimal

```ts
import {
  createRuntimeModuleFromPlugin,
  type RuntimePlugin,
} from "@atlas/runtime";

export const plugin: RuntimePlugin = {
  manifest: {
    id: "atlas.plugin.example",
    name: "Example Plugin",
    version: "0.1.0",
    description: "A small ATLAS Runtime plugin.",
    dependencies: [],
  },
  async activate(context) {
    // Enregistrer les services ou commandes avec le contexte fourni.
  },
  async deactivate() {
    // Arrêter le plugin et retirer les ressources temporaires.
  },
  async dispose() {
    // Libérer les ressources détenues par l'instance du plugin.
  },
};

export const module = createRuntimeModuleFromPlugin(plugin);
```

`activate` est obligatoire. `deactivate` et `dispose` sont facultatives ; si elles sont présentes, elles deviennent les hooks d'arrêt et de libération du module Runtime. Les champs `id`, `name` et `version` du manifeste sont obligatoires. Les métadonnées facultatives comprennent les noms et descriptions traduits, l'icône, le logo, l'aperçu, les dépendances, les points d'extension et les fonctions fournies.

## Catalogue

`RuntimePluginCatalog` enregistre les plugins Runtime, rejette les identifiants en double et fournit leurs descriptions. `findByExtensionPoint()` recherche les plugins par point d'extension ; `findProviding()` recherche ceux qui fournissent une fonction. `toRuntimeModules()` crée les modules destinés à l'hôte.

L'API Runtime et le modèle HTML installable sont deux niveaux distincts : l'exemple du modèle GitHub est un plugin web statique. L'installateur générique actuel ne le charge pas comme module Runtime exécutable. Un plugin Runtime nécessite une intégration hôte qui enregistre réellement le contrat Runtime.
