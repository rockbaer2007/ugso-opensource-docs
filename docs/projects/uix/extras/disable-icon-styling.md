---
title: Icon-Styling deaktivieren
description: Icon-Styling-Patching deaktivieren.
---
# Icon-Styling-Patching deaktivieren

Diese Option verhindert, dass UIX Icon-Styling-Patches anwendet. Sie ist hilfreich, wenn eine Integration oder Custom Card eigene Icon-Logik nutzt und UIX diese nicht beeinflussen soll.

## Einstellung über die Integrations-UI

1. In Home Assistant zu **Settings -> Devices & Services -> UI eXtension -> Configure** gehen.
2. **Performance settings** oder den passenden Optionsbereich öffnen.
3. **Disable icon styling patching** aktivieren.
4. Speichern.

## Verhalten bei aktivierter Option

- UIX überschreibt keine Icons über `--uix-icon` oder `--uix-icon-for-<entity_id>`.
- UIX überschreibt keine Icon-Farben über `--uix-icon-color` oder `--uix-icon-color-for-<entity_id>`.
- Andere UIX-Styling-Funktionen bleiben verfügbar.
