---
title: ATLAS Terminal
description: Eigenständiges ATLAS-Plugin für ein authentifiziertes Browser-Terminal mit ANSI-Farben und optionalem SSH-Ziel.
---
# ATLAS Terminal

ATLAS Terminal ist ein eigenständiges Plugin-Repository für ein authentifiziertes Browser-Terminal. Es bietet ANSI-Farben, eine einstellbare Schriftgröße und optional eine SSH-Verbindung zu einem serverseitig festgelegten Ziel. Die Darstellung des Prompts ist von Oh My Posh inspiriert.

## Repository und Installation

- GitHub: [rockbaer2007/atlas-terminal-plugin](https://github.com/rockbaer2007/atlas-terminal-plugin)
- Installationsseite: [ATLAS Terminal hinzufügen](https://rockbaer2007.github.io/atlas-terminal-plugin/install.html)
- Repository-Manifest: [repository.json](https://raw.githubusercontent.com/rockbaer2007/atlas-terminal-plugin/main/repository.json)
- Plugin-Version: `0.1.1`

Füge in ATLAS Administration unter **Plugins → Repository hinzufügen** den Typ **Plugin** hinzu und verwende die Manifest-URL. Prüfe das Repository und installiere anschließend das Plugin-Paket. Der ATLAS-Host muss ein kompatibles Terminal-Backend enthalten.

## Funktionen

- Browser-Terminal mit ANSI-Farben
- lokal einstellbare Schriftgröße
- optionales SSH-Ziel mit serverseitig konfiguriertem Host, Benutzer, Schlüssel und `known_hosts`
- Hostschlüsselprüfung bleibt aktiv; das Browserfenster kann kein beliebiges SSH-Ziel angeben
- eigenständige Versionierung des Frontends im Plugin-Repository

## Voraussetzungen und Sicherheit

Das Repository enthält das Plugin-Frontend, ist aber **kein eigenständiger SSH-Server und kein Home-Assistant-Add-on**. Shell-, Supervisor- und WebSocket-Funktionen stellt der ATLAS-Host bereit. Die Kompatibilitätserklärung nennt ATLAS `>=0.2.0-alpha.76` und Home Assistant `>=2026.8`.

Das Terminal ist standardmäßig deaktiviert. Aktiviere es erst, nachdem auf dem ATLAS-Host ein starkes, zufälliges Zugriffstoken mit mindestens 32 URL-sicheren Zeichen eingerichtet wurde. Die lokale Shell läuft mit den Berechtigungen des ATLAS-Prozesses. Im Home-Assistant-App/Add-on-Betrieb können Supervisor-Berechtigungen auch administrative `ha`-Befehle ermöglichen. Behandle den Terminalzugriff daher wie administrativen Zugriff.

Das Zugriffstoken bleibt im lokalen Browserspeicher und wird beim Verbindungsaufbau über das WebSocket-Subprotokoll, nicht über eine URL, übertragen. Skripte derselben Website können auf diesen Speicher zugreifen. Verwende das Terminal nur in einem vertrauenswürdigen Browserprofil.

## Status und Lizenz

Das Plugin wird als **experimentell** geführt, da es ein passendes ATLAS-Backend voraussetzt. Die Lizenz ist [MIT](https://github.com/rockbaer2007/atlas-terminal-plugin/blob/main/LICENSE).
