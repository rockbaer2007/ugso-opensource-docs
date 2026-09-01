# ATLAS File Studio

ATLAS File Studio is the second independent ATLAS plugin. It is intended to edit files in approved Home Assistant paths without allowing free root access by default.

## Repository

- GitHub: `https://github.com/rockbaer2007/atlas-file-studio-plugin`
- Install page: `https://rockbaer2007.github.io/atlas-file-studio-plugin/install.html`
- Repository file: `https://raw.githubusercontent.com/rockbaer2007/atlas-file-studio-plugin/main/repository.json`

## Planned Scope

- file tree
- editor surface
- syntax highlighting
- YAML validation
- upload and download
- `/config` as default root
- add-on directory only after Administration approval
- no free root access by default

## Security Model

The first plugin contract describes a fixed access policy:

| Path | Default | Approval |
|---|---|---|
| `/config` | active | no additional approval |
| `/addons` | disabled | only through Atlas Administration |
| `/` | disabled | not allowed by default |

This lets the install and update flow be tested before real file access is enabled in the add-on runtime.
