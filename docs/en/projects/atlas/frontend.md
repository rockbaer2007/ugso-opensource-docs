# ATLAS in the Home Assistant frontend

Since **0.1.299**, ATLAS provides the optional **ATLAS Runtime** integration.
It registers its own HA administrator sidebar panel, opening Plugin Hub,
Expert Card Editor and Administration from the existing runtime. The panel
follows HA's DE/EN/FR language and light/dark appearance.

## Requirements and data preservation

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
restart, static module and preservation of unrelated panels. HACS download of
**0.1.299** on Proxmox is confirmed up to **Pending restart**. Setup and embedding
on that system, updates, further HA versions and native ARM64/Pi HACS installation
remain separate qualification steps.

References: [HA custom panels](https://developers.home-assistant.io/docs/frontend/custom-ui/creating-custom-panels/)
and [HACS integration structure](https://www.hacs.xyz/docs/publish/integration/).
