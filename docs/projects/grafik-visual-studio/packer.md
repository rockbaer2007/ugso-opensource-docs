---
title: Packer für Widget- und Tool-Pakete
description: Pakete für HA Grafik Visual Studio prüfen und als .wg oder .tp erstellen.
---

# Packer für Widget- und Tool-Pakete

Der Packer erstellt aus einem Quellordner ein Widget-Paket (`.wg`) oder Tool-Paket (`.tp`) für HA Grafik Visual Studio. Beide Dateien sind ZIP-Archive mit eigener Endung. Vor dem Export prüft der Packer das Manifest, die Paketstruktur, referenzierte SVG-/PNG-Bilder und die Grenzen der [Widget-Paket-Schnittstelle](./widget-pakete) beziehungsweise [Tool-Paket-Schnittstelle](./tool-pakete). Paketdateien enthalten in der aktuellen Schnittstelle 0.1 keinen ausführbaren Code.

## Paket erstellen

1. Lege `manifest.json` im Wurzelverzeichnis eines Quellordners ab. Referenzierte Bilder gehören unter `icons/`. Die beiden Schnittstellenseiten zeigen die Felder und Beispiele.
2. Wähle im Packer **Widget-Paket** oder **Tool-Paket**, dann den Quellordner und einen vorhandenen Exportordner.
3. Prüfe die Ergebnisliste sowie Paket-ID, Version, Lizenz und Zielname. **Exportieren** wird erst bei gültigem Paket und freiem Zielnamen aktiv. Der Packer überschreibt keine vorhandene Datei.
4. Installiere die erzeugte `.wg`- oder `.tp`-Datei im Studio unter **Einstellungen → Widget-Pakete** oder **Einstellungen → Tools**. Die bisherigen Endungen `.wg.zip` und `.tp.zip` bleiben verwendbar.

Ein Widget-Paket kann 1 bis 30 Widgets enthalten; ein Tool-Paket enthält in Schnittstelle 0.1 genau ein Tool. Der Packer prüft mit denselben Regeln wie der Studio-Importer. Das Studio prüft jedes importierte Paket zusätzlich selbst.

## Programm und Dateiendungen

Die Qt-Oberfläche läuft unter Windows und Linux. Der Button **Endungen registrieren** zeigt zuerst eine Vorschau und richtet nach Bestätigung eigene Icons und „Öffnen mit“-Einträge für `.wg` und `.tp` beim aktuellen Benutzer ein. Eine bestehende Standard-App wird nicht geändert. Der Packer kann ein vorhandenes Paket zur Prüfung öffnen, ohne es zu installieren. Nach dem Verschieben des Programms muss die Dateityp-Registrierung erneut ausgeführt werden.

Version **0.2.0** ist als früher Test-Release im [Studio-Repository](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/tag/grafik-packer-v0.2.0) erhältlich:

| System | Download | SHA-256 |
| --- | --- | --- |
| Windows x86_64 | [ZIP herunterladen](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/download/grafik-packer-v0.2.0/HA-Grafik-Packer-0.2.0-windows-x86_64.zip) | `7ab24f0d69fec36e15037edf1e4c3c34c29296be4491f16b65801a3e9fa22b9c` |
| Linux x86_64 | [TAR.GZ herunterladen](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/download/grafik-packer-v0.2.0/HA-Grafik-Packer-0.2.0-linux-x86_64.tar.gz) | `baa80a8bbc7c5b78f5d16f59fe3c3bc80c8bd3076cb9a17178f5362a207045c9` |

Entpacke das Archiv vollständig und starte `HA-Grafik-Packer.exe` beziehungsweise `HA-Grafik-Packer`. Der Ordner `_internal` muss daneben bleiben; er enthält auch die separat austauschbaren Qt-Bibliotheken. Der Linux-Build wurde zusätzlich in einem frischen Ubuntu-24.04-Docker-Container geprüft und benötigt Qt-Systembibliotheken für EGL/OpenGL. Lizenztexte und Hinweise liegen im Archiv.

## Download prüfen

Lade aus demselben Release [SHA256SUMS](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/download/grafik-packer-v0.2.0/SHA256SUMS) und [SHA256SUMS.sig](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/releases/download/grafik-packer-v0.2.0/SHA256SUMS.sig) herunter. Die [Vertrauensdatei für OpenSSH](https://raw.githubusercontent.com/rockbaer2007/ugso-opensource-docs/main/docs/public/keys/packer-allowed-signers) und der [öffentliche Release-Schlüssel](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/packer-release.pub) werden getrennt vom Release bereitgestellt. Der Ed25519-Fingerabdruck ist `SHA256:W3iUvKedcI4FWS1kMoBrLlrAF2GbsB4sELphG0uITLE`.

Prüfe zuerst die Signatur. Unter Linux im Downloadordner:

```sh
ssh-keygen -Y verify -f packer-allowed-signers -I packer-release -n ha-grafik-visual-studio-packer-release -s SHA256SUMS.sig < SHA256SUMS
sha256sum -c SHA256SUMS
```

Unter Windows funktionieren dieselben Signaturparameter in `cmd.exe` mit der gezeigten Eingabeumleitung. Vergleiche danach `certutil -hashfile DATEINAME SHA256` mit dem Wert in `SHA256SUMS`. Lade Schlüssel und Vertrauensdatei vor dem Prüfen von den oben verlinkten Quellen. Der Packer-Quellcode bleibt im privaten Entwicklungs-Repository; die von GitHub automatisch angebotenen „Source code“-Archive dieses Releases gehören zum **Studio**.
