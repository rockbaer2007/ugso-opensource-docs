---
title: ATLAS Plugin Template
description: Create an ATLAS plugin from the official GitHub template.
---
# ATLAS Plugin Template

The [official ATLAS Plugin Template on GitHub](https://github.com/rockbaer2007/atlas-plugin-template) is a ready-to-use repository for a single ATLAS plugin. Use GitHub's **Use this template** action to create your own repository.

## Plugin generator in Administration

ATLAS Administration includes an initial plugin generator. It creates an install package from the plugin ID, name, description, version, entry path and capabilities, with an editable HTML/CSS/JavaScript starter, plus a `repository.json` catalog file. Review the generated content and paths and add the files to your repository; the generator does not create a GitHub repository or publish anything automatically.

## Quick start

1. Open the template repository and choose **Use this template** → **Create a new repository**.
2. Clone your new repository and edit `plugins/atlas-plugin/atlas-plugin.json`. Set a unique plugin ID, name, version, description and only the capabilities the plugin actually needs.
3. Replace the example app in `plugins/atlas-plugin/` and replace `icon.svg`, `logo.svg` and `preview.svg` with your plugin assets.
4. Build and validate the package locally:

   ```sh
   npm run build
   npm run check
   ```

5. Update `repository.json` and `install.html` for your repository. The package builder copies the ID, name, version, descriptions and asset paths from the manifest and keeps the catalog in sync.
6. Enable GitHub Pages for the `main` branch. The catalog will then be available at `https://raw.githubusercontent.com/<owner>/<repo>/main/repository.json`.
7. Add the catalog URL in ATLAS Administration and install the plugin for testing.

## Included

The template contains a small example plugin, manifest, repository catalog, installation page, package builder, validation and a GitHub Actions workflow. The workflow runs the build and checks on pushes and pull requests.

Bump the plugin version for every release and run `npm run build` afterwards. Keep the plugin ID stable after publication. Review permissions and declared capabilities before publishing.

## Current installation scope

The generic repository installer currently stores package files locally. It does not automatically execute arbitrary plugin code downloaded from a repository. The package format stores plugin files as text; larger binary assets should be hosted separately and referenced by URL.

See [Repository Format](./repository-format) for catalog and package details. Template repository: [rockbaer2007/atlas-plugin-template](https://github.com/rockbaer2007/atlas-plugin-template).
