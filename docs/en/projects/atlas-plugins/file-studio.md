# ATLAS File Studio

ATLAS File Studio is the second independent ATLAS plugin. It is intended to edit files in approved Home Assistant paths without allowing free root access by default.

## Repository

- GitHub: `https://github.com/rockbaer2007/atlas-file-studio-plugin`
- Install page: `https://rockbaer2007.github.io/atlas-file-studio-plugin/install.html`
- Repository file: `https://raw.githubusercontent.com/rockbaer2007/atlas-file-studio-plugin/main/repository.json`

## Current State

File Studio is published as an installable ATLAS plugin and can be tested through the demo repository in Administration and Hub.

- current plugin version: `0.1.36`
- current Home Assistant App/Add-on version: `0.1.128`
- file tree for the approved `/config` area
- flexible two-column surface with optional maximum width and height limits
- compact toolbar below `Dateibaum /config`, keeping icons out of the right file
  list in narrower layouts
- file and folder actions next to the path: create file, create folder, refresh and collapse all folders
- editor surface with a locally bundled CodeMirror 6 editor
- large files scroll inside the editor surface so the lower status row stays visible
- syntax highlighting for YAML, JSON, JavaScript, TypeScript and Markdown
- YAML validation before saving with Home Assistant hints for common files such as `configuration.yaml`, `automations.yaml`, `scripts.yaml` and packages, including common root keys, automation/script structure and directly entered secret values
- save the currently opened file
- automatic backups before saving, a history list of recent backups, comparison
  with the current state and restore of a selected backup
- save locally, drag-and-drop upload, multi-file upload and download
- download names are counted up in the browser, for example `configuration.yaml`, `configuration-1.yaml`, `configuration-2.yaml`
- upload conflicts can be replaced, renamed or cancelled in a File Studio dialog
- multi-select delete, copy and move actions
- trash restore instead of immediate permanent deletion; the right-side toolbar
  icon is gray when empty and red when entries exist
- favorites bar for frequently used files and folders
- colored file-type icons with compact type badges
- search with type filters, optional content search, matching line and content preview
- opt-in problem report in a File Studio dialog with preview and a prepared GitHub issue link; the report does not include Home Assistant tokens, provider API keys or file contents
- ZIP content preview without extraction
- `/config` as default root
- additional path approvals for `www`, `custom_components`, `addons` and `parent-of-config`
- add-on directory only after Administration or Add-on approval
- no free root access by default

The editor library is shipped with the plugin. File Studio therefore does not need a CDN for the code editor and remains traceably versioned in the Home Assistant add-on runtime.

## Security Model

The first plugin contract describes a fixed access policy:

| Path | Default | Approval |
|---|---|---|
| `/config` | active | no additional approval |
| `/config/www` | visible as capability | through Atlas Administration or Add-on option |
| `/config/custom_components` | visible as capability | through Atlas Administration or Add-on option |
| `/addons` | disabled | through Atlas Administration or Add-on option |
| `parent-of-config` | disabled | only through deliberate admin approval |
| `/` | disabled | not allowed by default |

`/config` is the normal Home Assistant configuration area. It contains files such as `configuration.yaml`, `automations.yaml`, dashboards, themes, blueprints, scripts and local web files under `www`.

`/addons` is used for local Home Assistant add-ons. It can contain custom add-on folders with files such as `config.yaml`, `Dockerfile`, startup scripts, icons and documentation. Because changes there can directly affect installable add-ons, File Studio keeps this area locked by default and only shows it after explicit approval in Atlas Administration.

In Home Assistant App/Add-on mode, these approvals come from the Add-on configuration. In Docker or Linux installs, Atlas Administration controls the same file capabilities. Plugins receive approved path context only, not raw long-lived secrets.

## Home Assistant Update Note

Every visible ATLAS update bumps the Home Assistant App/Add-on version. Home Assistant compares the installed version (`old`) with the repository version (`target`). For this build, `target` should be at least `0.1.128`. If Home Assistant still shows an older target version, reload repository information in the Add-on Store and then update or restart ATLAS.

This lets the install and update flow be tested before real file access is enabled in the add-on runtime.

## Next Expansion Steps

- further Home Assistant YAML assistance, for example real schema/service checks against a connected Home Assistant instance
- archive support after ZIP: read and extract `.rar` including RAR5, `.tar`,
  `.tar.gz`, `.tgz`, `.gz` and `.gzip`
- archive extraction should start with safe content listing and targeted
  single-file extraction, followed later by a guarded extract-all action
- optional icon/logo studio workflow with SVG and PNG output
- saving icon SVGs under `/config/www/custom_local_icons/` when the matching Home Assistant integration is used
- show a switch between `/config` and the Automation Exporter output folder when
  ATLAS Automation Exporter / Editor is installed
