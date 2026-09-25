---
title: ATLAS Terminal
description: ATLAS browser terminal with ANSI colors, optional SSH, Oh My Posh themes and a server-served Nerd Font.
---
# ATLAS Terminal

ATLAS Terminal is a standalone plugin repository for an authenticated browser terminal. It provides ANSI colors, an adjustable font size, selectable Oh My Posh themes and an optional SSH connection to a server-configured target.

## Repository and Installation

- GitHub: [rockbaer2007/atlas-terminal-plugin](https://github.com/rockbaer2007/atlas-terminal-plugin)
- Install page: [Add ATLAS Terminal](https://rockbaer2007.github.io/atlas-terminal-plugin/install.html)
- Repository manifest: [repository.json](https://raw.githubusercontent.com/rockbaer2007/atlas-terminal-plugin/main/repository.json)
- Plugin version: `0.1.5`

In ATLAS Administration, open **Plugins → Add repository**, choose **Plugin**, and enter the manifest URL. Review the repository and install the plugin package. The ATLAS host must provide a compatible Terminal backend.

## Features

- browser terminal with ANSI colors
- locally adjustable font size
- selectable Oh My Posh themes for local Bash sessions
- Meslo LGM Nerd Font is served by Home Assistant; clients do not need a local font installation
- optional SSH target with a server-configured host, user, key and `known_hosts`
- host-key verification stays enabled; the browser cannot select an arbitrary SSH target
- independently versioned frontend in the plugin repository
- collapsible token settings: they close on connect and reopen after disconnecting or when the session ends
- local shell sessions start at filesystem root `/` inside the ATLAS container instead of `/app`; SSH keeps the target server's default directory

## Setting up the Nerd Font

Place `MesloLGMNerdFontMono-Regular.ttf` and `MesloLGMNerdFontMono-Bold.ttf` in `/config/www/fonts/` or directly in `/config/www/`. Home Assistant serves them at `/local/fonts/` or `/local/`, and the terminal loads the font files from there.

## Requirements and Security

The repository contains the plugin frontend, but it is **not a standalone SSH server or a Home Assistant add-on**. The ATLAS host provides the shell, Supervisor and WebSocket functions. Its compatibility declaration lists ATLAS `>=0.2.0-alpha.79` and Home Assistant `>=2026.8`. Loading the Meslo font from Home Assistant requires App/Add-on `0.1.214` or newer; the root working directory and collapsible token settings require `0.1.215` or newer.

The terminal is disabled by default. Enable it only after configuring a strong, random access token of at least 32 URL-safe characters on the ATLAS host. The local shell runs with the permissions of the ATLAS process. In Home Assistant App/Add-on mode, Supervisor permissions may also enable administrative `ha` commands. Treat terminal access as administrative access.

The access token stays in local browser storage and is sent during connection setup through the WebSocket subprotocol, not in a URL. The token settings collapse when a session connects and reopen after disconnecting or when the session ends. They are open on first load if no token is saved. Scripts from the same website can access this storage. Use the terminal only in a trusted browser profile.

## Status and License

The plugin is listed as **experimental** because it requires a compatible ATLAS backend. It is licensed under [MIT](https://github.com/rockbaer2007/atlas-terminal-plugin/blob/main/LICENSE).
