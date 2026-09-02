# ATLAS File Studio

ATLAS File Studio is the second independent ATLAS plugin. It is intended to edit files in approved Home Assistant paths without allowing free root access by default.

## Repository

- GitHub: `https://github.com/rockbaer2007/atlas-file-studio-plugin`
- Install page: `https://rockbaer2007.github.io/atlas-file-studio-plugin/install.html`
- Repository file: `https://raw.githubusercontent.com/rockbaer2007/atlas-file-studio-plugin/main/repository.json`

## Current State

File Studio is published as an installable ATLAS plugin and can be tested through the demo repository in Administration and Hub.

- current plugin version: `0.1.32`
- current Home Assistant App/Add-on version: `0.1.94`
- file tree for the approved `/config` area
- flexible two-column surface with optional maximum width and height limits
- file and folder actions next to the path: create file, create folder, refresh and collapse all folders
- editor surface with a locally bundled CodeMirror 6 editor
- syntax highlighting for YAML, JSON, JavaScript, TypeScript and Markdown
- YAML validation before saving with Home Assistant hints for common files such as `configuration.yaml`, `automations.yaml`, `scripts.yaml` and packages
- save the currently opened file
- automatic backups before saving, a history list of recent backups, comparison
  with the current state and restore of a selected backup
- save locally, drag-and-drop upload, multi-file upload and download
- download names are counted up in the browser, for example `configuration.yaml`, `configuration-1.yaml`, `configuration-2.yaml`
- upload conflicts can be replaced, renamed or cancelled in a File Studio dialog
- multi-select delete, copy and move actions
- search with type filters, optional content search, matching line and content preview
- opt-in problem report in a File Studio dialog with preview and a prepared GitHub issue link; the report does not include Home Assistant tokens, provider API keys or file contents
- ZIP content preview without extraction
- `/config` as default root
- add-on directory only after Administration approval
- no free root access by default

The editor library is shipped with the plugin. File Studio therefore does not need a CDN for the code editor and remains traceably versioned in the Home Assistant add-on runtime.

## Security Model

The first plugin contract describes a fixed access policy:

| Path | Default | Approval |
|---|---|---|
| `/config` | active | no additional approval |
| `/addons` | disabled | only through Atlas Administration |
| `/` | disabled | not allowed by default |

`/config` is the normal Home Assistant configuration area. It contains files such as `configuration.yaml`, `automations.yaml`, dashboards, themes, blueprints, scripts and local web files under `www`.

`/addons` is used for local Home Assistant add-ons. It can contain custom add-on folders with files such as `config.yaml`, `Dockerfile`, startup scripts, icons and documentation. Because changes there can directly affect installable add-ons, File Studio keeps this area locked by default and only shows it after explicit approval in Atlas Administration.

This lets the install and update flow be tested before real file access is enabled in the add-on runtime.

## Next Expansion Steps

- further Home Assistant YAML assistance, for example real schema/service checks against a connected Home Assistant instance
- improved file type icons inspired by VS Code Icons
- archive support after ZIP: read and extract `.rar` including RAR5, `.tar`,
  `.tar.gz`, `.tgz`, `.gz` and `.gzip`
- archive extraction should start with safe content listing and targeted
  single-file extraction, followed later by a guarded extract-all action
- optional icon/logo studio workflow with SVG and PNG output
- saving icon SVGs under `/config/www/custom_local_icons/` when the matching Home Assistant integration is used
