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

Starting with test version **0.3.1**, an existing package with identical file contents appears in green as **Datei gespeichert** (file saved), including after restarting the packer. Export remains disabled. Different contents still trigger the overwrite protection. The wide **GitHub & Katalog …** button is directly below the checklist.

Since **Packer 0.3.0**, **GitHub & Katalog …** opens an exported `.wg` or `.tp` package for validation and publishing. Test version **0.3.1**, available below, includes this feature and the corrected saved-file status.

1. Install the [GitHub CLI](https://cli.github.com/) and sign in from a terminal with `gh auth login`. Enter your public repository and choose **Releases laden** (load releases).
2. Select a release tag and confirm **Paket auf GitHub veröffentlichen** (publish package on GitHub). To create a release, enable **Release für vorhandenen Git-Tag erstellen**; the Git tag must already exist on GitHub. Existing assets are never overwritten.
3. The download link is filled automatically. Alternatively, enter an existing HTTPS download link for a fixed `.wg` or `.tp` version and skip GitHub publishing.
4. Complete the license link, description, internal contact email and minimum Studio version. Choose **Nein / Ja / Unsicher** (No / Yes / Unsure) for new Studio features. Yes or Unsure requires a description and allows an unknown minimum version.
5. Read the [registration notice](https://visualstudio.ugso-software.de/privacy?lang=en), confirm processing and distribution rights, then choose **Im Katalog registrieren** (register in catalog). Review the recipient and details before sending. The original package is uploaded for automatic analysis.
6. Copy the private management link after a successful submission. The package appears in the catalog after manual review and approval. If the network result is uncertain, check whether the version was saved first; the packer never retries automatically.

The contact email goes internally to the catalog and optionally its configured review mailbox. Names, email and website are not published. The packer remembers only the repository and license link, never contact emails, GitHub tokens, consents or management links. Network tasks run in the background. Widget source folders may also contain `LICENSE.txt` and `README.md`.

## Application and file types

The Qt interface runs on Windows and Linux. **Register extensions** first previews the changes and, after confirmation, adds dedicated icons and Open With entries for `.wg` and `.tp` for the current user. It does not change an existing default application. The packer can inspect an existing package without installing it. Repeat file-type registration after moving the application.

Version **0.3.1** is available as a signed test release for Windows and Linux in the [package catalog](https://visualstudio.ugso-software.de/?kind=helper&lang=en):

| System | Download | SHA-256 |
| --- | --- | --- |
| Windows x86_64 | [Download ZIP](https://visualstudio.ugso-software.de/downloads/helpertools/HA-Grafik-Packer-0.3.1-windows-x86_64.zip) | `7047e6ee5bb2327cf80432d2c37e0f82516284c22c0d4910ff3d4d64950efd8a` |
| Linux x86_64 | [Download TAR.GZ](https://visualstudio.ugso-software.de/downloads/helpertools/HA-Grafik-Packer-0.3.1-linux-x86_64.tar.gz) | `e094331c7281957764dee38a8a117d932a2589581117daf68f1e146b71fd9a19` |

Extract the entire archive and run `HA-Grafik-Packer.exe` or `HA-Grafik-Packer`. Keep the `_internal` folder beside it; the Qt libraries there can be replaced separately. Both platform builds passed tests and a self-test after extraction. Linux needs system Qt libraries for EGL/OpenGL. License texts and notices are included in the archive.

## Verify a download

For version 0.3.1, download [SHA256SUMS-0.3.1](https://visualstudio.ugso-software.de/downloads/helpertools/SHA256SUMS-0.3.1) and [SHA256SUMS-0.3.1.sig](https://visualstudio.ugso-software.de/downloads/helpertools/SHA256SUMS-0.3.1.sig). The [OpenSSH allowed-signers file](https://raw.githubusercontent.com/rockbaer2007/ugso-opensource-docs/main/docs/public/keys/packer-allowed-signers) and [public release key](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/packer-release.pub) are distributed separately. The Ed25519 fingerprint is `SHA256:W3iUvKedcI4FWS1kMoBrLlrAF2GbsB4sELphG0uITLE`. The earlier checksum files without a version number belong to 0.2.0.

On Linux, verify the signature first, then the hashes in the download directory:

```sh
ssh-keygen -Y verify -f packer-allowed-signers -I packer-release -n ha-grafik-visual-studio-packer-release -s SHA256SUMS-0.3.1.sig < SHA256SUMS-0.3.1
sha256sum -c SHA256SUMS-0.3.1
```

On Windows, use the same signature parameters in `cmd.exe` with the shown input redirection. Then compare `certutil -hashfile FILENAME SHA256` with the value in `SHA256SUMS-0.3.1`. Obtain the key and allowed-signers file from the linked sources before verifying. The Packer source remains in a private development repository.
