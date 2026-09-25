---
title: Runtime and Lifecycle
description: The ATLAS Runtime plugin contract and module lifecycle.
---
# Runtime and Lifecycle

ATLAS Runtime provides a TypeScript plugin contract. A plugin has a manifest and an asynchronous `activate` method. `createRuntimeModuleFromPlugin()` adapts that contract to a Runtime module.

## Minimal Runtime plugin

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

`activate` is required. `deactivate` and `dispose` are optional; when present, they become the Runtime module's stop and dispose hooks. Manifest fields `id`, `name` and `version` are required. Optional metadata includes localized names/descriptions, icon, logo, preview, dependencies, extension points and provided features.

## Catalog

`RuntimePluginCatalog` registers Runtime plugins, rejects duplicate IDs and exposes descriptors. Use `findByExtensionPoint()` to find plugins by extension point and `findProviding()` to find plugins by provided feature. `toRuntimeModules()` creates Runtime modules for the host.

The Runtime API and the installable HTML template are separate layers: the GitHub template's example is a static web plugin and the current generic installer does not load it as an executable Runtime module. Runtime plugins need a host integration that actually registers the Runtime contract.
