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

Eigenständige Programme wurden für Windows und Linux gebaut und jeweils mit einem Selbsttest geprüft; der Linux-Build lief zusätzlich in einem frischen Ubuntu-24.04-Docker-Container. Unter Linux werden die üblichen Qt-Systembibliotheken für EGL und OpenGL benötigt. **Diese Builds sind noch unsignierte interne Testversionen. Es gibt derzeit keinen öffentlichen Packer-Download.** Öffentliche Downloadlinks folgen erst mit einem signierten Release und veröffentlichtem Prüfschlüssel. Der Packer-Quellcode wird in einem privaten Entwicklungs-Repository gepflegt; die Paketregeln und Studio-Schnittstellen sind öffentlich dokumentiert.

Der [öffentliche Release-Schlüssel](/keys/packer-release.pub) ist separat bereitgestellt. Sein Ed25519-Fingerabdruck lautet `SHA256:W3iUvKedcI4FWS1kMoBrLlrAF2GbsB4sELphG0uITLE`. Lade den Schlüssel aus dieser Dokumentation, bevor du ein Release prüfst; der private Schlüssel wird nicht veröffentlicht.
