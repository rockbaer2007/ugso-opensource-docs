---
title: Runtime und Lebenszyklus
description: Runtime-Plugin-Vertrag und Modullebenszyklus in ATLAS.
---
# Runtime und Lebenszyklus

ATLAS Runtime stellt in TypeScript einen Plugin-Vertrag bereit. Ein Plugin enthält ein Manifest und eine asynchrone `activate`-Methode. `createRuntimeModuleFromPlugin()` bildet diesen Vertrag auf ein Runtime-Modul ab.

## Geprüfter Vertrag und Kompatibilität

Aktueller Stand am 16.10.2026: App **0.1.312**, Paket `@atlas/runtime`
**0.2.0-alpha.39**. Die folgende A5-Basis ist historisch. Ergänzende native
Paket-Wiederherstellungen und HA-Versionen sind unter
[Versionen und Kompatibilität](./compatibility) dokumentiert.

Stand der A5-Abschlussprüfung: HA-App `0.1.297`, Runtime `0.2.0-alpha.38`. Die Regressionen prüfen Aktivierung, Stop/Dispose, Katalog, Paketparser und isolierte Backend-Installation/-Wiederherstellung. Sie garantieren keine stabile 1.0-API oder beliebige Host-/HA-Versionen.

- Runtime-Hooks gelten für im Host registrierte Runtime-Plugins. Ein installiertes statisches Webplugin erhält dadurch keine automatische `activate`-/`deactivate`-/`dispose`-Ausführung.
- Extension Points und bereitgestellte Funktionen dienen der Beschreibung und Katalogsuche. Fähigkeitsangaben sind keine Sandbox und gewähren keinen Zugriff auf Dateien oder Geheimnisse.
- Der gespeicherte Aktivierungsstatus steuert Hub und Startlinks. Er sperrt den Zugriff auf rohe Plugin-Assets nicht.

Halte veröffentlichte Plugin-IDs stabil und erhöhe bei veröffentlichten Änderungen die Paketversion. Prüfe bei Vertragsänderungen unterstützte Paket-/Importformate, Lebenszyklus und den Erhalt vorhandener Daten; dokumentiere notwendige Migrationen und Auswirkungen in Release-Hinweisen. Eine umfassende Versions-/Kompatibilitätsmatrix bleibt Folgequalifikation. Runtime-Vertrag und Repository/Webpaketformat sind getrennt zu bewerten.

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
