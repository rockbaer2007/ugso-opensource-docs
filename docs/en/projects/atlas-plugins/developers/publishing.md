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

Follow the [version and compatibility rules](./compatibility), including backups, migration boundaries and recovery.

1. Increment the manifest `version` for every functional or visible release.
2. Run `npm run build` and `npm run check`.
3. Confirm the manifest, catalog and generated package use the same ID and version.
4. Review package files, asset paths, external requests and declared capabilities.
5. Publish the catalog by pushing to `main`: `https://raw.githubusercontent.com/<owner>/<repo>/main/repository.json`. GitHub Pages is not required for the raw file; optionally enable it to publish `install.html`.
6. Add the catalog URL in ATLAS Administration and test the preview and package installation.

Keep the plugin ID stable after the first publication. Large binary assets do not belong in the text-based package format; host them separately and reference them by URL.

## Installation status

The App server installs validated repository and imported packages in persistent plugin storage and serves static web files under `/plugin-assets/<slug>/`. Opening them runs their JavaScript in the browser; arbitrary Node modules or Runtime hooks are not automatically registered. Installation is not a sandbox: review package contents and browser code before opening. Building a package alone does not replace runtime or security testing.
