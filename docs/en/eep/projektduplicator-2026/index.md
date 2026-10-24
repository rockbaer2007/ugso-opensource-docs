---
title: Projektduplicator 2026
description: Duplicate and edit EEP model projects with a multilingual interface, ZIP snapshots and manual GitHub updates.
---

# Projektduplicator 2026

Projektduplicator 2026 is UGSo Software’s standalone Windows tool for duplicating and editing EEP model projects. Its interface supports German, English, French and Dutch.

## Download and launch

- [Download Windows ZIP 4.6.6.59](https://github.com/rockbaer2007/projektduplicator-2026/releases/download/v4.6.6.59/Projektduplicator-2026-v4.6.6.59-windows.zip)
- [Release, SHA-256 checksum and source](https://github.com/rockbaer2007/projektduplicator-2026/releases/tag/v4.6.6.59)
- [GitHub repository](https://github.com/rockbaer2007/projektduplicator-2026)

Extract the entire ZIP to a writable folder and run `Projektduplicator_2017.exe`. The technical filename is retained for compatibility with existing settings. Windows with .NET Framework 4.8 is required; the solution builds in Visual Studio 2026.

## Features

- Duplicate EEP model projects and edit model information.
- Edit multilingual model names and descriptions and translate them using Google Translate.
- Change the interface language while the application is running.
- Create ZIP snapshots of projects in the configured backup folder.
- Use the existing update buttons to check GitHub releases manually, download and install after confirmation.

The Google web translator requires internet access and depends on Google’s webpage response format. It does not use an official Google API. Failed translations retain the existing texts.

## Settings and updates

Back up your projects before making changes. Close editors and save changes to path and spline lists before updating. No update check runs automatically at startup.

The updater verifies the package and SHA-256 checksum, backs up existing program files and settings, and restarts after installation succeeds. Existing projects, path lists and custom `info.txt` content are retained. A missing `info.txt` receives the bundled copy; an existing older copy is intentionally not replaced automatically.

## Verified version

Version 4.6.6.59 was approved by the user after local review. The Form1 designer was checked in Visual Studio. The description and credits in `info.txt` were reviewed in DE/EN/FR/NL. All 49 local checks passed, covering languages, field routing, package validation, data retention, cancellation, rollback and updater process handoff.

A real public GitHub update with installation and restart still needs a separate test. Existing checks use simulated GitHub responses and temporary installations.

## Source and notices

UGSo source is MIT licensed; dependencies retain their respective license terms and copyrights. See `LICENSE` and `THIRD-PARTY-NOTICES.md` in the repository. EEP and Google Translate belong to their respective rights holders.
