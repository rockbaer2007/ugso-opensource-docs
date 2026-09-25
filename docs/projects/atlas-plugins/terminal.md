---
title: ATLAS Terminal
description: ATLAS-Browser-Terminal mit ANSI-Farben, optionalem SSH, Oh-My-Posh-Themes und serverseitiger Nerd-Font.
---
# ATLAS Terminal

ATLAS Terminal ist ein eigenständiges Plugin-Repository für ein authentifiziertes Browser-Terminal. Es bietet ANSI-Farben, eine einstellbare Schriftgröße, auswählbare Oh-My-Posh-Themes und optional eine SSH-Verbindung zu einem serverseitig festgelegten Ziel.

## Repository und Installation

- GitHub: [rockbaer2007/atlas-terminal-plugin](https://github.com/rockbaer2007/atlas-terminal-plugin)
- Installationsseite: [ATLAS Terminal hinzufügen](https://rockbaer2007.github.io/atlas-terminal-plugin/install.html)
- Repository-Manifest: [repository.json](https://raw.githubusercontent.com/rockbaer2007/atlas-terminal-plugin/main/repository.json)
- Plugin-Version: `0.1.5`

Füge in ATLAS Administration unter **Plugins → Repository hinzufügen** den Typ **Plugin** hinzu und verwende die Manifest-URL. Prüfe das Repository und installiere anschließend das Plugin-Paket. Der ATLAS-Host muss ein kompatibles Terminal-Backend enthalten.

## Funktionen

- Browser-Terminal mit ANSI-Farben
- lokal einstellbare Schriftgröße
- Oh-My-Posh-Themes für lokale Bash-Sitzungen
- Meslo LGM Nerd Font wird vom Home-Assistant-Server geladen; Clients benötigen keine lokale Font-Installation
- optionales SSH-Ziel mit serverseitig konfiguriertem Host, Benutzer, Schlüssel und `known_hosts`
- Hostschlüsselprüfung bleibt aktiv; das Browserfenster kann kein beliebiges SSH-Ziel angeben
- eigenständige Versionierung des Frontends im Plugin-Repository
- einklappbare Token-Einstellungen: beim Verbinden geschlossen, nach dem Trennen oder Sitzungsende wieder geöffnet
- lokale Shell-Sitzungen starten im Dateisystem-Root `/` des ATLAS-Containers statt in `/app`; SSH behält das Standardverzeichnis des Zielservers

## Nerd Font einrichten

Lege `MesloLGMNerdFontMono-Regular.ttf` und `MesloLGMNerdFontMono-Bold.ttf` in `/config/www/fonts/` oder direkt in `/config/www/` ab. Home Assistant stellt sie unter `/local/fonts/` beziehungsweise `/local/` bereit. Das Terminal lädt die Schriftdateien von dort.

## Voraussetzungen und Sicherheit

Das Repository enthält das Plugin-Frontend, ist aber **kein eigenständiger SSH-Server und kein Home-Assistant-Add-on**. Shell-, Supervisor- und WebSocket-Funktionen stellt der ATLAS-Host bereit. Die Kompatibilitätserklärung nennt ATLAS `>=0.2.0-alpha.79` und Home Assistant `>=2026.8`. Das Laden der Meslo-Schrift aus Home Assistant benötigt mindestens App/Add-on `0.1.214`; das Root-Startverzeichnis und die einklappbaren Token-Einstellungen benötigen `0.1.215` oder neuer.

Das Terminal ist standardmäßig deaktiviert. Aktiviere es erst, nachdem auf dem ATLAS-Host ein starkes, zufälliges Zugriffstoken mit mindestens 32 URL-sicheren Zeichen eingerichtet wurde. Die lokale Shell läuft mit den Berechtigungen des ATLAS-Prozesses. Im Home-Assistant-App/Add-on-Betrieb können Supervisor-Berechtigungen auch administrative `ha`-Befehle ermöglichen. Behandle den Terminalzugriff daher wie administrativen Zugriff.

Das Zugriffstoken bleibt im lokalen Browserspeicher und wird beim Verbindungsaufbau über das WebSocket-Subprotokoll, nicht über eine URL, übertragen. Die Token-Einstellungen klappen beim Verbinden ein und nach dem Trennen oder Sitzungsende wieder aus. Ohne gespeichertes Token sind die Einstellungen beim ersten Aufruf geöffnet. Skripte derselben Website können auf diesen Speicher zugreifen. Verwende das Terminal nur in einem vertrauenswürdigen Browserprofil.

## Status und Lizenz

Das Plugin wird als **experimentell** geführt, da es ein passendes ATLAS-Backend voraussetzt. Die Lizenz ist [MIT](https://github.com/rockbaer2007/atlas-terminal-plugin/blob/main/LICENSE).
