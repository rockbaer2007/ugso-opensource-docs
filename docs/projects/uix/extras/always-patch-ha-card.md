---
title: Always patch ha-card
description: Experimentelle Option, um ha-card immer zu patchen.
---
# Always patch ha-card

::: info Verfügbar ab UIX 8.2.0-beta.1
Diese Option ist experimentell.
:::

Standardmäßig patcht UIX `ha-card` nicht, wenn in der ersten Frontend- oder Custom-Komponente im übergeordneten DOM-Baum keine Kartenkonfiguration gefunden wird. Diese experimentelle Option erlaubt, `ha-card` immer zu patchen, damit die Theme-Variable `uix-card(-yaml)` angewendet werden kann. `ha-card` ohne Konfiguration kann zum Beispiel in Konfigurations- oder Custom Panels vorkommen.

Wenn `ha-card` ohne Konfiguration gepatcht wird, fügt UIX die Klasse `type-generic-card` zu `ha-card` hinzu.

## Einstellung über die Integrations-UI

Die Option ist standardmäßig **nicht gesetzt**.

1. In Home Assistant zu **Settings -> Devices & Services -> UI eXtension -> Configure** gehen.
2. **Experimental settings** im Menü wählen.
3. **Always patch ha-card** aktivieren.
4. Speichern.

Die Einstellung ist sofort für alle verbundenen Browser-Sessions verfügbar. Ein Neuladen der Seite kann nötig sein, damit die Änderung sichtbar wird.

## Verhalten bei aktivierter Option

- `ha-card` wird immer gepatcht, auch wenn keine Kartenkonfiguration verfügbar ist.
- Wird `ha-card` auf diese Weise gepatcht, erhält es die Klasse `type-generic-card`.
