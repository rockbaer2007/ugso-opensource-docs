---
title: Runtime und Lebenszyklus
description: Runtime-Plugin-Vertrag und Modullebenszyklus in ATLAS.
---
# Runtime und Lebenszyklus

ATLAS Runtime stellt in TypeScript einen Plugin-Vertrag bereit. Ein Plugin enthält ein Manifest und eine asynchrone `activate`-Methode. `createRuntimeModuleFromPlugin()` bildet diesen Vertrag auf ein Runtime-Modul ab.

## Minimales Runtime-Plugin

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
    // Register plugin services or commands with the provided context.
  },
  async deactivate() {
    // Stop plugin activity and unregister temporary resources.
  },
  async dispose() {
    // Release resources owned by the plugin instance.
  },
};

export const module = createRuntimeModuleFromPlugin(plugin);
```

`activate` ist erforderlich. `deactivate` und `dispose` sind optional; wenn vorhanden, werden sie als Stop- und Dispose-Hooks des Runtime-Moduls verwendet. Die Manifestfelder `id`, `name` und `version` sind erforderlich. Optionale Metadaten umfassen lokalisierte Namen/Beschreibungen, Icon, Logo, Vorschaubild, Abhängigkeiten, Extension Points und bereitgestellte Funktionen.

## Katalog

`RuntimePluginCatalog` registriert Runtime-Plugins, weist doppelte IDs zurück und stellt Beschreibungen bereit. Über `findByExtensionPoint()` lassen sich Plugins nach Extension Point und über `findProviding()` nach bereitgestellter Funktion auffinden. `toRuntimeModules()` erzeugt die Runtime-Module für den Host.

Die Runtime-API und die installierbare HTML-Vorlage sind unterschiedliche Ebenen: Das Beispielprojekt aus der GitHub-Vorlage ist ein statisches Webplugin und wird durch den aktuellen generischen Installer nicht als ausführbares Runtime-Modul geladen. Runtime-Plugins benötigen eine Hostintegration, die den Runtime-Vertrag tatsächlich registriert.
