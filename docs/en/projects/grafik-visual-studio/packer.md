---
title: Widget and tool package packer
description: Validate and create .wg and .tp packages for HA Grafik Visual Studio.
---

# Widget and tool package packer

The packer creates a widget package (`.wg`) or tool package (`.tp`) for HA Grafik Visual Studio from a source folder. Both files are ZIP archives with a dedicated extension. Before export, the packer validates the manifest, package structure, referenced SVG/PNG images and limits of the [widget package interface](./widget-packages) or [tool package interface](./tool-packages). Packages for the current 0.1 interfaces contain no executable code.

## Create a package

1. Put `manifest.json` at the root of a source folder. Referenced images belong under `icons/`. The two interface pages show the required fields and examples.
2. Select **Widget package** or **Tool package** in the packer, then choose the source folder and an existing export folder.
3. Review the validation list, package ID, version, license and target name. **Export** becomes available only for a valid package and unused target name. Existing files are not overwritten.
4. Install the resulting `.wg` or `.tp` file in Studio under **Settings → Widget packages** or **Settings → Tools**. The older `.wg.zip` and `.tp.zip` extensions remain supported.

A widget package may contain 1 to 30 widgets; a tool package contains exactly one tool in interface 0.1. The packer uses the same validation rules as the Studio importer. Studio also validates every imported package independently.

## Application and file types

The Qt interface runs on Windows and Linux. **Register extensions** first previews the changes and, after confirmation, adds dedicated icons and Open With entries for `.wg` and `.tp` for the current user. It does not change an existing default application. The packer can inspect an existing package without installing it. Repeat file-type registration after moving the application.

Version **0.2.0** is available as an early test [release in the Studio repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/grafik-packer-v0.2.0):

| System | Download | SHA-256 |
| --- | --- | --- |
| Windows x86_64 | [Download ZIP](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/download/grafik-packer-v0.2.0/HA-Grafik-Packer-0.2.0-windows-x86_64.zip) | `7ab24f0d69fec36e15037edf1e4c3c34c29296be4491f16b65801a3e9fa22b9c` |
| Linux x86_64 | [Download TAR.GZ](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/download/grafik-packer-v0.2.0/HA-Grafik-Packer-0.2.0-linux-x86_64.tar.gz) | `baa80a8bbc7c5b78f5d16f59fe3c3bc80c8bd3076cb9a17178f5362a207045c9` |

Extract the entire archive and run `HA-Grafik-Packer.exe` or `HA-Grafik-Packer`. Keep the `_internal` folder beside it; the Qt libraries there can be replaced separately. The Linux build also passed in a fresh Ubuntu 24.04 Docker container and needs system Qt libraries for EGL/OpenGL. License texts and notices are included in the archive.

## Verify a download

Download [SHA256SUMS](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/download/grafik-packer-v0.2.0/SHA256SUMS) and [SHA256SUMS.sig](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/download/grafik-packer-v0.2.0/SHA256SUMS.sig) from the same release. The [OpenSSH allowed-signers file](https://raw.githubusercontent.com/rockbaer2007/ugso-opensource-docs/main/docs/public/keys/packer-allowed-signers) and [public release key](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/packer-release.pub) are distributed separately. The Ed25519 fingerprint is `SHA256:W3iUvKedcI4FWS1kMoBrLlrAF2GbsB4sELphG0uITLE`.

On Linux, verify the signature first, then the hashes in the download directory:

```sh
ssh-keygen -Y verify -f packer-allowed-signers -I packer-release -n ha-grafik-visual-studio-packer-release -s SHA256SUMS.sig < SHA256SUMS
sha256sum -c SHA256SUMS
```

On Windows, use the same signature parameters in `cmd.exe` with the shown input redirection. Then compare `certutil -hashfile FILENAME SHA256` with the value in `SHA256SUMS`. Obtain the key and allowed-signers file from the linked sources before verifying. The Packer source remains in a private development repository; GitHub's automatic “Source code” archives for this release contain the **Studio** repository.
