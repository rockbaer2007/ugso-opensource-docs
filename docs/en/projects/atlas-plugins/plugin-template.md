---
title: ATLAS Plugin Template
description: Create an ATLAS plugin from the official GitHub template.
---
# ATLAS Plugin Template

The [official ATLAS Plugin Template on GitHub](https://github.com/rockbaer2007/atlas-plugin-template) is a ready-to-use repository for a single ATLAS plugin. Use GitHub's **Use this template** action to create your own repository.

## Plugin generator in Administration

ATLAS Administration includes a plugin generator for ID, name, description, version, entry path and capabilities. Choose an MDI icon from the locally bundled catalog or a custom PNG up to 512 KiB; the package includes the graphic and required license notices. PNG colors and transparency survive. It generates an editable HTML/CSS/JavaScript starter, package, `repository.json` and localized `README.md`, also downloadable separately. Review contents and paths before publication. The generator creates no GitHub repository and publishes nothing automatically. Supported manually imported packages are installed on the App server after compatibility checks and served under `/plugin-assets/<slug>/`. Their UI runs when opened in the browser; Runtime hooks are not automatically registered. Keep `entry` and package paths consistent.

Plugins with their own language selector inherit the saved ATLAS language preference when launched. A `language` parameter in the plugin URL takes precedence. If a plugin does not support the selected language, it uses its configured fallback language.

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
6. After pushing, the catalog is available at `https://raw.githubusercontent.com/<owner>/<repo>/main/repository.json` without GitHub Pages. Enable GitHub Pages separately if you want to publish `install.html`.
7. Add the catalog URL in ATLAS Administration and install the plugin for testing.

## Included

The template contains a small example plugin, manifest, repository catalog, installation page, package builder, validation and a GitHub Actions workflow. The workflow runs the build and checks on pushes and pull requests.

Bump the plugin version for every release and run `npm run build` afterwards. Keep the plugin ID stable after publication. Review permissions and declared capabilities before publishing.

## Current installation scope

The App server installs validated repository and imported packages in persistent plugin storage and serves static web files under `/plugin-assets/<slug>/`. Opening them runs their JavaScript in the browser; arbitrary Node modules or Runtime hooks are not automatically registered. Installation is not a sandbox: review package contents and browser code before opening. Package files contain text or explicitly marked Base64 assets; up to 300 files and 20 MB per package. Host larger binary assets separately.

See [Repository Format](./repository-format) for catalog and package details. Template repository: [rockbaer2007/atlas-plugin-template](https://github.com/rockbaer2007/atlas-plugin-template).
