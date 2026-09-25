---
title: Build, Validate and Publish
description: Prepare and validate ATLAS plugin packages and repository catalogs.
---
# Build, Validate and Publish

The [Plugin Template](../plugin-template) automates repeatable steps for a plugin's GitHub repository.

## Build the package and catalog

```sh
npm run build
npm run check
```

The build creates an installable package from the manifest and synchronizes the plugin entry in `repository.json`. Checks validate IDs, package paths and metadata in the generated package. A GitHub Actions workflow runs the build and checks on pushes and pull requests.

## Release steps

1. Increment the manifest `version` for every functional or visible release.
2. Run `npm run build` and `npm run check`.
3. Confirm the manifest, catalog and generated package use the same ID and version.
4. Review package files, asset paths, external requests and declared capabilities.
5. Enable GitHub Pages for `main` if the catalog should be available through Pages. The raw file will then be available at `https://raw.githubusercontent.com/<owner>/<repo>/main/repository.json`.
6. Add the catalog URL in ATLAS Administration and test the preview and package installation.

Keep the plugin ID stable after the first publication. Large binary assets do not belong in the text-based package format; host them separately and reference them by URL.

## Installation status

The generic ATLAS repository installer currently stores downloaded package files locally. It does not automatically execute arbitrary plugin code in the package. A successful package build therefore confirms package structure, not executable installation or a security review of the plugin code.
