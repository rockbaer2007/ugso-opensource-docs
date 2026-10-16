# ATLAS in the Home Assistant frontend

Since **0.1.299**, ATLAS provides the optional **ATLAS Runtime** integration.
It registers its own HA administrator sidebar panel, opening Plugin Hub,
Expert Card Editor and Administration from the existing runtime. The panel
follows HA's DE/EN/FR language and light/dark appearance.

## Requirements and data preservation

As of 2026-10-16: **App 0.1.312**, **integration 0.1.306**, versioned independently.
Introduction and test versions below are not instructions to downgrade a newer
App. Full HAOS recovery and deliberate address changes are covered in the
[backup guide](../atlas-plugins/file-studio); browser-local data still needs its own export.

ATLAS must already run as an App/Add-on, Docker container or
[Linux/systemd service](/en/projects/atlas/linux). HACS installs the HA integration;
the Node server and external plugins stay in their existing runtime.
The add-on's existing Ingress entry is not replaced.

Back up HA before installing. Also export ATLAS projects and Administration
settings in ATLAS. Keep the runtime's existing browser address: browser projects,
cookies and encrypted settings are bound to the address or installation identity.
Changing hostname, scheme or port does not automatically migrate data.

Browsers may also separate storage for an externally embedded runtime from
its separately opened storage. If existing projects or encrypted settings
are absent in the panel, use **Open separately** at the previous address
and export them there; the integration does not move or delete those data.
[Storage partitioning reference](https://privacysandbox.google.com/cookies/storage-partitioning).

## HACS installation

1. Open HACS and its custom repositories.
2. Add `https://github.com/rockbaer2007/atlas` with type **Integration**.
3. Download **ATLAS Runtime** and restart Home Assistant.
4. Open **Settings → Devices & services → Add integration → ATLAS Runtime**.
5. Enter the existing browser-accessible runtime base URL, for example
   `http://atlas-server:4176/` or `https://atlas.example.org/atlas/`.

The integration does not request HA tokens or provider keys. Configure the HA
connection in ATLAS Administration. Panel code does not send HA authentication
or entity data to the embedded window. Ordinary HA state updates do not reload it.

This is a custom HACS repository; general HACS catalog inclusion is not claimed.
Select repository type **Integration**, not Dashboard. Exported HACS card
packages remain a separate workflow.

### HACS reports “Unknown error”

Check the corresponding entry in **Settings → System → Logs**. During the first
Proxmox download, `hacs_repository_download` raised
`AttributeError: 'NoneType' object has no attribute 'data'`: HACS could not find
its repository entry before the package download began. Reload the HACS page,
open **ATLAS Runtime** again and retry the download. In the verified case,
the status then changed to **Pending restart**. This confirms the download;
setup after restarting HA is a separate step. Other “Unknown error” causes
require their corresponding log entry.

## Shared plugin management since 0.1.300

App/Ingress and Runtime can store repository lists, imported plugin metadata and
activation state in the same ATLAS server. Update the **ATLAS App/runtime** to
0.1.300 first; updating only the HACS integration is insufficient.

1. Open the original **ATLAS App access** containing all your plugins.
2. Open Administration → Plugin Manager → **Shared plugin management**.
3. Choose **Adopt local state** and review repository/plugin/activation counts
   and listed conflicts.
4. Conflicts keep server values by default. Choose local values only when you
   deliberately want them adopted.
5. Click **Back up and adopt**. A download backs up plugin metadata; the server
   also backs up its previous state and incoming metadata before an atomic save.
6. Reopen Runtime or use **Load server state**. Subsequent changes are saved to
   the server; open Administration pages check every 15 seconds. Concurrent
   writes using an outdated revision are rejected.

Empty adoption never removes existing server entries. Legacy local management
remains valid until the first confirmed adoption, which does not delete old
browser data. Unsaved changes receive a separate local recovery copy and can
be previewed for adoption again. **Inspect backup** previews a metadata export
or server snapshot; adoption merges entries.

State is stored at `ATLAS_PLUGIN_DATA_ROOT/.management/state.json`, with backups
in `.management/backups/`. App/Add-on and Docker use the persistent plugin data
directory. Include it in runtime backups. No packages are automatically installed
or removed. HA tokens, provider keys, filesystem permissions, editor projects
and settings owned by external plugins are outside this migration.

## Shared editor projects since 0.1.301

Update the ATLAS App/runtime to **0.1.301**. Open the original App editor containing
your project. Under **Shared editor projects**, choose **New server project →
Preview and save**, review name and field count, then **Back up and apply**.
Choose **New server project** again for another local project. Identical names
are allowed and never automatically replace other projects.

In Runtime: **Load project list**, select the project, **Preview opening**, review
and **Back up and apply**. Snapshots contain Expert fields and their Card
configurations, project/script names, surface size and grid size. Save edits
explicitly with **Preview and save**. Revision checks detect concurrent edits
to the same project. Another browser never automatically replaces your workspace.

Before opening/saving, the current workspace is backed up to
`ATLAS_PLUGIN_DATA_ROOT/.projects/workspaces/` and downloaded. Previous server
states are in `.projects/backups/`; named projects use `.projects/projects.json`.
Include the persistent plugin data directory in backups. **Inspect backup**
previews a downloaded workspace backup. **Inspect local draft** recovers unsaved
shared work from this browser; it is not automatically opened after a reload.

The original local project remains in its existing browser storage. Shared work
uses a separate local draft. Settings, HA credentials, plugin management, palette
favorites and external plugin projects are not transferred. Damaged server files
are never replaced. Limits: 100 projects, 4 MiB per project and 64 MiB store size.

## Manual installation and updates

Copy only `custom_components/atlas_frontend` from the repository into
`/config/custom_components/atlas_frontend`. Back up an existing directory before
replacing it; retain other components. Restart HA and add the integration as above.
`manifest.json` contains the version.

For HACS updates, update this integration and restart HA. Its runtime URL remains
in the HA config entry. Update the ATLAS server independently through its existing
deployment path. The integration's **Configure** action changes the address;
export ATLAS data before a deliberate address change. Removing the integration
removes its own panel access, not the ATLAS runtime, plugins or projects.

From integration **0.1.306**, migration checks reject unknown configuration
schemas without rewriting the entry. The existing schema **1.1** is unchanged;
package versions are independent of schema versions. Returning to an older
integration is only qualified with a compatible schema. Back up HA configuration
and ATLAS data before updates; a later schema change requires its matching data
backup for recovery. An invalid stored runtime URL produces a setup error and
can be corrected through **Configure**.

## HTTP, HTTPS and embedding

HTTPS HA needs an HTTPS runtime for embedding. An HTTP target displays guidance
and **Open separately** instead. The base URL must not contain credentials,
query parameters or fragments. Port 80 is valid; reverse-proxy prefixes are retained.

A reverse proxy must forward ATLAS subpaths correctly and permit framing from
the HA origin. For a blank view, check **Open separately**, reachability, proxy
routing and frame protection headers. Automatic discovery or persistent storage
of an Ingress session address is outside this integration; continue using the
add-on's existing Ingress access.

The panel's HA administrator requirement does not protect direct access to an
external ATLAS server. Keep its existing access restrictions. The new panel uses
`atlas-runtime` and does not replace another sidebar entry. Its module is served
at `/atlas_frontend/frontend/atlas-homeassistant-panel.js`; it is not an additional
Lovelace resource under `/hacsfiles/atlas/`.

## Verified scope

Isolated checks use Home Assistant Core **2026.10.1**, a separate ATLAS runtime
and fixture data. They cover config/options flows, the admin panel, reload,
restart, static module and preservation of unrelated panels. HACS setup and
embedding are verified on Proxmox/x86_64 and Pi 5/ARM64. The isolated integration
cycle **0.1.301 → 0.1.306**, rollback to 0.1.301 and re-update preserve the same
config entry and unrelated panels across real HA restarts. An unknown fixture
schema is rejected without modifying its entry. On Pi 5 and Proxmox, the HACS
update to 0.1.306, HA restart, panel, live entities and data preservation pass.
The separate ATLAS App stays on 0.1.305 during this integration qualification.

The additional stable version **2026.9.4** is verified with integration and runtime
**0.1.306** in a fresh isolated amd64 installation: config/options, integration
reload, full HA restart, embedded Hub, Administration and Editor, authenticated
version discovery and live entity selection. The config entry, unrelated panels,
fixture project, plugin data and configuration file are preserved. Pi 5 and
Proxmox were unchanged for this additional check. HACS download, Supervisor,
ARM64 and integration rollback were not repeated on 2026.9.4.

The CI matrix checks eleven integration contracts against **2026.9.4** and
**2026.10.1**. This does not replace separate running-HA checks or establish an
inclusive version range. Further HA versions and actual conversion between
different data schemas remain separate qualification steps.

References: [HA custom panels](https://developers.home-assistant.io/docs/frontend/custom-ui/creating-custom-panels/)
and [HACS integration structure](https://www.hacs.xyz/docs/publish/integration/).
