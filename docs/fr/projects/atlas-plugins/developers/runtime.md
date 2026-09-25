---
title: Runtime et cycle de vie
description: Contrat des plugins Runtime et cycle de vie des modules ATLAS.
---
# Runtime et cycle de vie

ATLAS Runtime fournit un contrat de plugin en TypeScript. Un plugin possède un manifeste et une méthode asynchrone `activate`. `createRuntimeModuleFromPlugin()` adapte ce contrat à un module Runtime.

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
