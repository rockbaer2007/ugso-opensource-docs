---
title: Versions and Compatibility
description: Release numbering, data migrations and safe ATLAS/plugin updates.
---
# Versions and Compatibility

These release rules apply from 15 October 2026. They do not change existing installations or data formats. An automatic compatibility gate is not implemented yet.

## Which version matters?

| Version | Meaning |
| --- | --- |
| ATLAS App/runtime | Version of the delivered Docker, App/Add-on or Linux package. |
| HA integration | Version of `atlas_frontend`; record the HACS commit separately. |
| Framework | Independent version per `@atlas/*` package; not the App version. |
| Plugin | Independent version with a stable ID; manifest, catalog and package must agree. |
| Data format | Kind and format version of persisted data; a revision counts changes for conflict detection. |

The Card Editor ships with ATLAS. External plugins update independently. Equal version numbers across components do not prove compatibility.

## Release rules

Use `MAJOR.MINOR.PATCH`: PATCH for compatible fixes, MINOR for compatible features, and MAJOR for breaking contracts once a stable 1.x interface exists. Before 1.0, a breaking change requires a new MINOR and migration notes. Future incompatible changes must therefore not be another 0.1.x patch. Existing versions are not renamed.

Alpha versions explicitly identify test builds. Changed published package contents require a new version; documentation-only changes need no runtime bump. Record the source commit and tested combinations in release notes.

## What does ATLAS check today?

Repository fields `compatibility.atlas`, `host` and `homeAssistant` describe claimed compatibility. `atlas` refers to the App/runtime. These values are displayed but not enforced as installation gates. Missing metadata means **unverified**. Existing plugins remain usable.

Update discovery compares version text numerically; it is not a complete SemVer resolver. Separately, kernel module dependencies support exact numeric triples, `^` and `*`, but not general ranges or prereleases. Current caret matching keeps the same MINOR for major zero; `^0.0.3` also accepts `0.0.4`. Use exact versions for those modules.

Package and manifest ID/version are checked before replacement. Declared capabilities are neither automatic permissions nor a sandbox. A future compatibility gate must also validate server-side before replacement and account for existing packages without new metadata.

## Preserve and recover data

1. Before updates, back up HA and ATLAS data, or the standalone installation with data and installation identity. Also export local Admin settings, editor projects and shared plugin metadata. External plugin data and browser-only collections need separate backups.
2. Keep runtime address, persistent paths and identity stable. Encrypted settings are not automatically portable to another installation. A source backup does not replace a data backup.
3. Update one component at a time; restart HA after integration updates as documented. Then check settings, projects and active plugins.
4. Recover matching code **and** the corresponding data snapshot. An older program must not overwrite an unknown newer data format.

Future migrations require a read-only preview, original backup, validated transformation of a copy, explicit apply, conflict checks and atomic replacement. Unknown or damaged formats must not be replaced with empty data. Retries and failures must preserve data. These are requirements, not a claim that universal migration already exists.

The package installer restores the previous directory when a swap fails; after success it does not retain that directory as a rollback archive. Shared plugin backups contain metadata, not every package file or plugin's data.

## Verified scope

HACS commit updates and HA restarts passed on Pi 5 and Proxmox while preserving settings, projects and plugins. The integration stayed at 0.1.301 with unchanged integration source. Real version/schema migration and further HA versions remain unverified. New migrations require old/current/unknown-format, failure, conflict and restore tests.

The technical [source-repository version policy](https://github.com/rockbaer2007/atlas/blob/main/docs/project/specifications/VERSION_COMPATIBILITY_POLICY.md) provides detailed rules and boundaries.
