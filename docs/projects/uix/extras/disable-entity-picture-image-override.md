---
title: Entity-Picture-Override deaktivieren
description: Overrides für Entitätsbilder deaktivieren.
---
# Entity-Picture-Image-Overrides deaktivieren

Diese Option verhindert, dass UIX Entitätsbilder ersetzt. Das ist nützlich, wenn eine Karte, Integration oder Kamera eigene Bildlogik nutzt und UIX diese Bilder nicht überschreiben soll.

## Einstellung über die Integrations-UI

1. In Home Assistant zu **Settings -> Devices & Services -> UI eXtension -> Configure** gehen.
2. Den passenden Optionsbereich öffnen.
3. **Disable entity picture image overrides** aktivieren.
4. Speichern.

## Verhalten bei aktivierter Option

- UIX wendet `--uix-image` und `--uix-image-for-<entity_id>` nicht mehr als Bild-Override an.
- Bestehende Kartenbilder und Entitätsbilder bleiben unverändert.
- Andere UIX-Styling- und Theme-Funktionen bleiben verfügbar.
