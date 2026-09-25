---
title: Plugin Development
description: Technical starting point for developers building ATLAS plugins.
---
# Plugin Development

This section follows the development path for standalone ATLAS plugins, from the starter project through manifests and Runtime to publishing. Plugin contracts are still evolving; check the current template and repository format before publishing.

## Recommended workflow

1. Create a repository from the [official plugin template](../plugin-template).
2. Choose a unique, stable plugin ID and maintain the name, version, description, assets and required capabilities in the manifest.
3. Develop the plugin UI independently first. The current template includes a small HTML/CSS/JavaScript example page.
4. Build the package and catalog with `npm run build`, then validate them with `npm run check`.
5. Test the catalog through the ATLAS demo repository or Administration. Increment the plugin version for every published change.

## Guides

- [Manifest and capabilities](./manifest): metadata, IDs, versions, assets and declarations.
- [Runtime and lifecycle](./runtime): the Runtime plugin contract and activation, deactivation and cleanup.
- [Build, validate and publish](./publishing): package builder, catalog, GitHub Actions and release checklist.
- [Plugin Template](../plugin-template): step-by-step guide to the GitHub starter repository.
- [Repository Format](../repository-format): catalog fields and installable package format.

## Security boundaries

Declare only capabilities your plugin actually uses. A declaration documents the plugin's intent; it is not a sandbox and does not automatically grant access to Home Assistant or Atlas internals. Do not request credentials in plugin files or publish tokens and API keys.

The generic repository installer currently stores package files locally and does not execute arbitrary downloaded code. Treat tests as package and integration checks, not as proof of an isolated execution environment.
