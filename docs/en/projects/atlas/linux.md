---
title: Linux and systemd
description: Install, update and back up ATLAS on Linux.
---

# Linux and systemd

The Linux installer introduced in ATLAS **0.1.298** uses the same combined app
server as Docker and the HA app. Administration and Card Editor run together;
external plugins remain separately installable. The optional native
[ATLAS Runtime integration](/en/projects/atlas/frontend) is also implemented
and verified through a custom HACS repository on Pi 5 and Proxmox.

## Requirements

- Linux with running systemd, Node.js 22 or newer and root access for installation.
- A Linux-built runtime matching the target CPU architecture, libc and Node ABI.
- Three free ports: 4176 for the app, 4175 and 4174 for internal surfaces.
- Space for at least two runtime releases and data backups.

The builder supports AMD64 and ARM64 and uses Debian Bookworm/glibc.
Alpine/musl packages are not interchangeable. Native package preparation is also
verified on Raspberry Pi OS / Debian 13.7 Trixie with glibc on a Raspberry Pi 4
(`aarch64`, 4 GB RAM).

Qualification as of 2026-10-15: Debian 12 AMD64 LXC and the native Pi 4 with
Node.js 22.23.3 and ATLAS 0.1.303/0.1.304. On the Pi, all 17 installer tests,
installation, version update, rollback, backup, service restart and automatic
recovery after an unhealthy update pass. Synthetic plugin/project data and
configuration are preserved. Ports remained loopback-only during that first
check. Subsequent qualification passes LAN access on4176, an actual Pi 4 OS
reboot, autostart and persistent HA connection recovery from 0.1.305.
Further distributions and hardware require separate qualification.

The installer uses the `atlas` system account. It refuses an existing account
with a different home or primary group and does not silently adopt another
ATLAS installation.

## Preparing a package

On a Linux build host with the existing build dependencies:

```sh
corepack enable
pnpm install --frozen-lockfile
pnpm build
pnpm test:linux
pnpm linux:prepare
```

The result is `output/linux-runtime`: built app, dependencies, reference
plugin and `atlas-linux-runtime.json`. Existing output directories are not overwritten.

Alternatively, build outside the target LXC with Docker:

```sh
docker build -f packaging/linux/Dockerfile --target export --output type=local,dest=output/linux-export .
```

The export includes a runtime archive, manifest, checksums and the Node binary
with license from the official Node image. Verify provenance and SHA-256
values before use. Use a compatible Node installation; do not blindly
replace an existing Node version. Preserve relative `node_modules` symlinks
during transfer and extraction.

## Installation

With a verified extracted package and compatible Node version:

```sh
sudo node /path/linux-runtime/scripts/atlas-linux-installer.mjs install --source /path/linux-runtime
sudo systemctl status atlas
curl --fail http://127.0.0.1:4176/health
```

The installer validates the package, architecture and native modules, creates
a backup, installs a separate release and starts the service. Readiness requires
both surfaces, the expected app version and Linux distribution target.
Occupied ports are not freed by stopping unrelated services.

## Persistent data

| Path | Contents |
| --- | --- |
| `/opt/atlas/releases/` | Separate runtime releases. |
| `/opt/atlas/current` | Symbolic link to the current runtime. |
| `/opt/atlas/installation.json` | Installation record and previous release. |
| `/var/lib/atlas/` | Persistent data, plugins, identity, file history and trash. |
| `/etc/atlas/atlas.env` | Protected configuration, preserved during updates. |
| `/etc/systemd/system/atlas.service` | Managed service unit. |
| `/etc/systemd/system/atlas.service.d/` | Local systemd overrides. |
| `/var/backups/atlas/` | Timestamped backups. |

Editor projects and parts of Administration live in the browser. Export them
separately through their respective interfaces. A server backup does not capture
browser storage. Keep the same browser address, data location and installation
identity across updates so locally bound encrypted credentials remain valid.
Docker/HA data is not silently migrated to a new installation.

## Update and rollback

```sh
sudo node /path/new-package/scripts/atlas-linux-installer.mjs update --source /path/new-package
sudo node /opt/atlas/current/scripts/atlas-linux-installer.mjs rollback
```

ATLAS is stopped and backed up before updating. The environment file, installed
plugins and local unit overrides remain intact. The current link switches the
runtime. A failed candidate restores the previous runtime. Previously stopped
installations remain stopped after validation; existing boot enablement is preserved.

Rollback changes program files, not user data. Future data migrations need
separate backwards-compatibility review. Old releases and backups are not
automatically deleted. Use `systemctl edit atlas` for overrides rather than
editing the managed unit directly.

## Backup and recovery

```sh
sudo node /opt/atlas/current/scripts/atlas-linux-installer.mjs backup
sudo node /opt/atlas/current/scripts/atlas-linux-installer.mjs status
```

A stopped-service backup includes data, configuration, unit, overrides and the
installation record. A previously active service restarts afterwards.
Backups are root-only and may contain credentials. Back up external paths,
SSH keys outside ATLAS data and browser projects separately.

For manual recovery, stop ATLAS, back up the current state again and restore
the selected data/configuration backup at its original paths with appropriate
ownership. Preserve the installation identity, provide a matching runtime
and check `/health`. Copying a backup to a different installation does not
unlock secrets bound there. A VM/LXC snapshot before first installation also
allows recovery of the entire host.

## Network and plugins

Since ATLAS 0.1.305, saving Linux Administration settings also persists the
remembered HA connection server-side using AES-GCM. Restoration after service
and host restarts therefore works over LAN HTTP without browser Web Crypto.
After updating, enter the existing token once in Administration and save;
earlier versions may have retained it only in memory.

The encrypted `admin-connection.enc.json` file and private
`admin-connection.enc.json.key` reside beside `admin-device.json` in the private
ATLAS data directory. Files use Linux mode `0600`; encrypted data is bound to
the installation identity. A complete data backup must retain all three files
and be treated as confidential. Copying only the runtime directory or browser
export does not include this key. “Forget token” also removes the remembered
HA token from server-side state. Unreadable encrypted data is not overwritten
automatically.

All surfaces default to loopback; Terminal is disabled. The installer opens
no firewall. An administrator may deliberately change `ATLAS_APP_HOST` for
LAN access and restrict that access; internal ports remain local.
Administration must not be exposed unprotected to the internet.

File Studio requires matching Linux file permissions and approved paths.
Home Assistant files on another host are not mounted automatically.
SSH and Oh My Posh for the external Terminal are optional additional
requirements, not included in the Linux package.

## Test scope

Installer regressions use disposable data to verify preservation, backup,
failed updates, rollback, service state, non-overwriting installation and
path/ABI validation. A container test with a simulated service does not
replace native systemd testing. Native evidence and open platforms are recorded
in [Development Status](/en/projects/atlas/development-status).
