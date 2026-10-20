---
title: Dashboard User Manager
description: Assign users to all HA views or individual views with checkboxes, backups and DE/EN/FR.
---
# Dashboard User Manager

**Version 0.1.6 · DE / EN / FR · MIT · experimental**

A standalone HA app: select a dashboard, display users as columns and views as rows, and edit assignments using checkboxes. ATLAS is not required. The interface uses 90 vw and 90 vh, with rotated names, narrow user columns and horizontal scrolling when needed.

![Dashboard User Manager 0.1.4 on HA test host .177 using automatic English](/images/dashboard-user-manager/ha-177-en-0.1.4.png)

Actual screenshot from test host .177, 20 October 2026: automatic HA language, 18 views and four users. The existing dashboard was not changed for this screenshot.

## Filter and preselect dashboards

Since 0.1.6, a migrated HA overview appears once: the `lovelace` entry and its legacy default access are merged. Preferences previously saved through either entry are preserved. Equal titles with different actual dashboard paths remain separate; titles alone do not identify duplicates. Older dashboard backups remain compatible. This follows [HA’s default access mapping](https://github.com/home-assistant/core/blob/2026.10.2/homeassistant/components/lovelace/websocket.py).

![Dashboard selection 0.1.5 with checkboxes on .177](/images/dashboard-user-manager/selection-177-en-0.1.5.png)

The dropdown contains only successfully loaded dashboards with at least one view. Confirmed empty entries and app panels without views are hidden. Load errors are listed separately by dashboard name and are not treated as empty; retry with **Reload**. YAML or generated dashboards with views remain marked **read-only**.

**Dashboard selection** opens a dialog with a checkbox for each available dashboard, **Select all**, **Clear all**, **Cancel** and **Apply selection**. Only checked entries appear in the dropdown. Preferences are stored per browser and HA address without changing dashboards or user assignments. An empty selection is valid. Add new dashboards to an existing saved selection when needed. Previously selected entries retain their preference during load errors.

Keeping the current dashboard preserves unsaved assignments. Excluding it asks for confirmation before discarding unsaved changes. If browser storage is blocked, an error is shown and the app does not pretend that the selection was saved.

## Install through UGSo HA Apps

Create a full HA backup first. Add this repository under **Settings → Apps → App store → Repositories**:

```text
https://github.com/rockbaer2007/ugso-ha-mqtt-addons
```

Install **Dashboard-Benutzerverwaltung**, start it and open it through HA Ingress. Only active HA administrators can use the interface. No additional LAN port or manually entered token. Requires Home Assistant with Supervisor and a manually managed dashboard. YAML and generated dashboards are read-only.

Adding the repository does not change an existing **local app**. Local and repository apps have different identifiers and separate private data. Before deliberately switching sources, create a full backup including the old app and download its JSON backups. Do not uninstall the local app without preserving its data; use only one app at a time for editing.

## Assign users

1. Select a dashboard. All its views, including subviews, are listed.
2. Select **webuser**, for example, in the column header to check that user for every editable view. Clearing the header removes the user from these views.
3. Adjust individual view checkboxes. A dash in the header means partially selected.
4. Choose **Save changes**. Only then does the app create a backup and write the change. **Reset selection** discards unsaved changes only.

**Green U = user, red A = administrator.** These actions do not change account roles. Original dashboard, view and user names, cards, layouts, paths and untouched views are preserved. Previous user IDs are not silently removed. Edited views use fixed user lists; users created later are not automatically added.

::: warning Visibility is not access control
This app controls view tab visibility. Direct URLs remain accessible; it does not replace HA access permissions. See the [official HA documentation](https://www.home-assistant.io/dashboards/views/#visible).
:::

## Automatic language

**Automatic (Home Assistant)** follows the HA interface language. If the surrounding HA frame cannot be read, the preferred browser language is used. Unsupported languages fall back to English. You can also select DE, EN or FR at the top; this preference is stored for that browser only.

Labels, help, dialogs, status messages, dates, accessibility text and server responses are translated. Switching language preserves unsaved checkboxes. Custom names and stored dashboard data are never translated. No cloud translation or extra keys are required.

## Backups and conflicts

Before every change, a complete dashboard JSON is written to `/data/backups/` in private app storage. Use **Download JSON** to keep a PC copy. These files contain all card configuration and should be treated as confidential. App updates preserve this storage; download it or include the app in a full HA backup before uninstalling.

The app compares the dashboard and user list with the loaded state and reads the result back after saving. Intervening changes block the save. HA has no atomic compare-and-save operation: avoid simultaneous edits in another editor during the short save phase.

Restore first creates another backup and is blocked if the dashboard was edited after the corresponding change. If a save is unconfirmed, do not retry blindly; compare the current state with the backup.

## Update a local ZIP installation

After a full backup, copy all new source files into `/addons/dashboard_user_manager/` and run in the HA terminal:

```sh
touch /addons/dashboard_user_manager/config.yaml
ha store reload
ha apps info local_dashboard_user_manager
```

Once `version_latest` shows the new version, update the app in HA. `touch` changes the timestamp only, helping Supervisor detect files extracted from older ZIPs with preserved timestamps. Do not uninstall. Repository apps update through their repository.

## Verification and limits

Version 0.1.5 tested on .177 after a fresh full backup: empty map hidden, unconfigured overview error shown separately, cancellation and persisted empty/re-enabled selection verified after reload. Dialog visually checked in DE/EN/FR. No user assignments saved; all four Lovelace files unchanged. All 26 Python and ten Node checks and amd64/aarch64 Docker builds passed.

The user successfully tested bulk and individual assignments, saving and reloading in 0.1.3. After a full backup, the local app on .177 was updated to 0.1.4. Automatic language selection follows German → English → French → German without reloading the app. Names and assignments are preserved; all four Lovelace files, including “Test für APP”, have the same SHA-256 hashes as the backup after testing. Offline frontend, API, preservation and conflict tests also pass. No production system was modified. Full HA backup restoration of the app remains unverified. An unconfigured default dashboard may return `config_not_found`; select an existing manually managed dashboard instead.

- [App source and package on GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/dashboard_user_manager)
- [UGSo HA Apps](/en/projects-mqtt/)
- [Deutsch](/projects/dashboard-user-manager/) · [Français](/fr/projects/dashboard-user-manager/)
