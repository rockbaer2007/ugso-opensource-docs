# Demo Repository

The demo repository is the real test source for the ATLAS installation flow:

`https://github.com/rockbaer2007/atlas-plugin-repository-demo`

## Purpose

- add a plugin repository in Administration
- validate the repository marker
- show available plugins in Hub and Administration
- compare versions and surface updates
- test the installation transition page
- load ATLAS File Studio as the second real plugin entry
- verify Home Assistant app install and update behavior against real GitHub repositories

## Installation Page

The public page is hosted on GitHub Pages:

`https://rockbaer2007.github.io/atlas-plugin-repository-demo/install.html`

The button copies the ATLAS repository URL and explains that it must be pasted into ATLAS Administration. It does not open the Home Assistant add-on store because ATLAS plugins and Home Assistant add-ons use different repository formats.

## Update Test

Every functional change to the plugin package must increment the plugin version. Only then can Administration detect an update compared with the installed version.

This also applies to test packages: when UI, manifest, icons, package contents or behavior change, the published repository version must be incremented.
