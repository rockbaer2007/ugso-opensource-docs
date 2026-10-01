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

Standalone applications have been built and self-tested on Windows and Linux; the Linux build also passed in a fresh Ubuntu 24.04 Docker container. Linux needs the usual Qt system libraries for EGL and OpenGL. **These are still unsigned internal test builds. There is no public packer download yet.** Public download links will follow only with a signed release and a published verification key. The packer source is maintained in a private development repository; the package rules and Studio interfaces are publicly documented.

The [public release key](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/packer-release.pub) is distributed separately. Its Ed25519 fingerprint is `SHA256:W3iUvKedcI4FWS1kMoBrLlrAF2GbsB4sELphG0uITLE`. Obtain the key from this documentation before verifying a release; the private key is not published.
