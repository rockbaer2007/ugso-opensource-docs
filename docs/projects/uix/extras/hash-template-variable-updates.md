---
title: Hash-Template-Variable deaktivieren
description: Hash-Template-Variable und Updates deaktivieren.
---
# Hash-Template-Variable und Updates deaktivieren

UIX stellt Templates die Variable `hash` bereit. Sie enthält den Teil der URL nach `#`. UIX beobachtet außerdem `location-changed` und `popstate`, damit Templates neu gebunden werden, wenn sich der Hash ändert.

## Einstellung über die Integrations-UI

1. In Home Assistant zu **Settings -> Devices & Services -> UI eXtension -> Configure** gehen.
2. **Performance settings** öffnen.
3. **Disable hash template variable and updates** aktivieren.
4. Speichern.

## Verhalten bei aktivierter Option

- Die Template-Variable `hash` ist nicht verfügbar.
- UIX bindet Templates nicht wegen Hash-Änderungen neu.
- Bestehende Templates, die `hash` verwenden, sollten angepasst werden.

::: warning
Aktiviere diese Option nur, wenn du keine Hash-basierten UIX-Templates verwendest oder wenn Hash-Updates in deinem Dashboard unnötige Template-Aktualisierungen auslösen.
:::
