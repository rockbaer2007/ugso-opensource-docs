---
title: Widget and tool package packer
description: Validate and create .wg and .tp packages for HA Grafik Visual Studio.
---

# Widget and tool package packer

Packages and helper tools are provided centrally at [visualstudio.ugso-software.de](https://visualstudio.ugso-software.de/?lang=en). This open-source page provides descriptions and instructions; downloads are provided by the package catalog.

The packer creates a widget package (`.wg`) or tool package (`.tp`) for HA Grafik Visual Studio from a source folder. Both files are ZIP archives with a dedicated extension. Before export, the packer validates the manifest, package structure, referenced SVG/PNG images and limits of the [widget package interface](./widget-packages) or [tool package interface](./tool-packages). Packages for the current 0.1 interfaces contain no executable code.

## Create a package

1. Put `manifest.json` at the root of a source folder. Referenced images belong under `icons/`. The two interface pages show the required fields and examples.
2. Select **Widget package** or **Tool package** in the packer, then choose the source folder and an existing export folder.
3. Review the validation list, package ID, version, license and target name. **Export** becomes available only for a valid package and unused target name. Existing files are not overwritten.
4. Install the resulting `.wg` or `.tp` file in Studio under **Settings → Widget packages** or **Settings → Tools**. The older `.wg.zip` and `.tp.zip` extensions remain supported.

The packer uses the same validation rules as its bundled Studio importer. Packer 0.3.0 supports up to 64 widgets per package; a tool package contains exactly one tool in interface 0.1. Studio also validates every imported package independently.

## GitHub and direct registration

New in **Packer 0.3.0**: **GitHub & Katalog …** opens an exported `.wg` or `.tp` package for validation and publishing. This version is being tested; the signed downloads below are still 0.2.0 and do not yet include this feature.

1. Install the [GitHub CLI](https://cli.github.com/) and sign in from a terminal with `gh auth login`. Enter your public repository and choose **Releases laden** (load releases).
2. Select a release tag and confirm **Paket auf GitHub veröffentlichen** (publish package on GitHub). To create a release, enable **Release für vorhandenen Git-Tag erstellen**; the Git tag must already exist on GitHub. Existing assets are never overwritten.
3. The download link is filled automatically. Alternatively, enter an existing HTTPS download link for a fixed `.wg` or `.tp` version and skip GitHub publishing.
4. Complete the license link, description, internal contact email and minimum Studio version. Choose **Nein / Ja / Unsicher** (No / Yes / Unsure) for new Studio features. Yes or Unsure requires a description and allows an unknown minimum version.
5. Read the [registration notice](https://visualstudio.ugso-software.de/privacy?lang=en), confirm processing and distribution rights, then choose **Im Katalog registrieren** (register in catalog). Review the recipient and details before sending. The original package is uploaded for automatic analysis.
6. Copy the private management link after a successful submission. The package appears in the catalog after manual review and approval. If the network result is uncertain, check whether the version was saved first; the packer never retries automatically.

The contact email goes internally to the catalog and optionally its configured review mailbox. Names, email and website are not published. The packer remembers only the repository and license link, never contact emails, GitHub tokens, consents or management links. Network tasks run in the background. Widget source folders may also contain `LICENSE.txt` and `README.md`.

## Application and file types

The Qt interface runs on Windows and Linux. **Register extensions** first previews the changes and, after confirmation, adds dedicated icons and Open With entries for `.wg` and `.tp` for the current user. It does not change an existing default application. The packer can inspect an existing package without installing it. Repeat file-type registration after moving the application.

Version **0.2.0** is available as an early test release in the [package catalog](https://visualstudio.ugso-software.de/?kind=helper&lang=en):

| System | Download | SHA-256 |
| --- | --- | --- |
| Windows x86_64 | [Download ZIP](https://visualstudio.ugso-software.de/downloads/helpertools/HA-Grafik-Packer-0.2.0-windows-x86_64.zip) | `7ab24f0d69fec36e15037edf1e4c3c34c29296be4491f16b65801a3e9fa22b9c` |
| Linux x86_64 | [Download TAR.GZ](https://visualstudio.ugso-software.de/downloads/helpertools/HA-Grafik-Packer-0.2.0-linux-x86_64.tar.gz) | `baa80a8bbc7c5b78f5d16f59fe3c3bc80c8bd3076cb9a17178f5362a207045c9` |

Extract the entire archive and run `HA-Grafik-Packer.exe` or `HA-Grafik-Packer`. Keep the `_internal` folder beside it; the Qt libraries there can be replaced separately. The Linux build also passed in a fresh Ubuntu 24.04 Docker container and needs system Qt libraries for EGL/OpenGL. License texts and notices are included in the archive.

## Verify a download

Download [SHA256SUMS](https://visualstudio.ugso-software.de/downloads/helpertools/SHA256SUMS) and [SHA256SUMS.sig](https://visualstudio.ugso-software.de/downloads/helpertools/SHA256SUMS.sig) from the same release. The [OpenSSH allowed-signers file](https://raw.githubusercontent.com/rockbaer2007/ugso-opensource-docs/main/docs/public/keys/packer-allowed-signers) and [public release key](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/packer-release.pub) are distributed separately. The Ed25519 fingerprint is `SHA256:W3iUvKedcI4FWS1kMoBrLlrAF2GbsB4sELphG0uITLE`.

On Linux, verify the signature first, then the hashes in the download directory:

```sh
ssh-keygen -Y verify -f packer-allowed-signers -I packer-release -n ha-grafik-visual-studio-packer-release -s SHA256SUMS.sig < SHA256SUMS
sha256sum -c SHA256SUMS
```

On Windows, use the same signature parameters in `cmd.exe` with the shown input redirection. Then compare `certutil -hashfile FILENAME SHA256` with the value in `SHA256SUMS`. Obtain the key and allowed-signers file from the linked sources before verifying. The Packer source remains in a private development repository; GitHub's automatic “Source code” archives for this release contain the **Studio** repository.
