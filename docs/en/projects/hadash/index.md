---
layout: home

hero:
  name: HADash
  text: Home Assistant Dashboard Toolkit
  tagline: Extract and back up dashboards and individual views from YAML, JSON and unencrypted Home Assistant backups.
  actions:
    - theme: brand
      text: Getting Started
      link: /en/projects/hadash/getting-started
    - theme: alt
      text: GitHub
      link: https://github.com/rockbaer2007/HADash

features:
  - icon: puzzle
    title: Back Up Individual Views
    details: Export as TXT, YAML or as a complete standalone dashboard.

  - icon: database
    title: Dashboards from Backups
    details: Process JSON data from unencrypted Home Assistant backups and the .storage folder.

  - icon: sync
    title: JSON to YAML
    details: Read dashboard configurations and save them as YAML.

  - icon: save
    title: Portable Application
    details: No classic installation required.
---

## Why HADash Exists

HADash was created from the need to back up individual Home Assistant dashboard
views separately.

It should also be possible to extract complete dashboards from old, unencrypted
Home Assistant backups or JSON files from the `.storage` folder and save them
again as YAML.

::: warning Preview
HADash is still under development. Feedback, bug reports and improvement ideas
are welcome.
:::
