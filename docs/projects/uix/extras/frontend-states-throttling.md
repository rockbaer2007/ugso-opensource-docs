---
title: Frontend State Throttling
description: Frontend-State-Updates drosseln.
---
# Frontend States Throttling

Frontend States Throttling reduziert, wie häufig State-Updates im Browser zu Re-Renders führen. Das kann bei Dashboards mit sehr vielen Entitäten, schnellen Sensoren oder leistungsschwachen Geräten helfen.

::: info Was wird gedrosselt?
Gedrosselt werden Frontend-State-Update-Verarbeitungen im Browser. Home Assistant selbst, Automationen und Backend-State-Änderungen werden dadurch nicht verlangsamt.
:::

## Aktivierung über die Integrations-UI

1. In Home Assistant zu **Settings -> Devices & Services -> UI eXtension -> Configure** gehen.
2. **Performance settings** öffnen.
3. **Throttle entity state updates** aktivieren.
4. Optional das **Throttle interval** einstellen.
5. Speichern.

## So funktioniert es

UIX sammelt schnelle State-Update-Signale im Browser und lässt Aktualisierungen nur in einem konfigurierten Mindestabstand durch. Dadurch sinkt die Zahl der Re-Renders.

### Letztes Update flushen

Wenn während eines Throttle-Fensters ein Update zurückgehalten wurde, wird das letzte Update nach Ablauf des Fensters nachgezogen. So bleibt die Anzeige aktuell, ohne jede Zwischenänderung sofort zu rendern.

## Clientseitige Override-API

`window.uixCoordinator` stellt eine Override-Methode bereit, mit der Integrationen wie Browser Mod pro Browser, Nutzer oder Gerät Einstellungen setzen können.

```js
window.uixCoordinator.setThrottleOverride(500)
window.uixCoordinator.setThrottleOverride(null)
```

### Mit Browser Mod verwenden

```yaml
# In der Browser-Mod-Konfiguration für eine bestimmte Browser-ID:
service: browser_mod.javascript
data:
  browser_id: kitchen-tablet
  code: |
    window.uixCoordinator?.setThrottleOverride(500)
```

### Mit custom:button-card verwenden

```yaml
# Throttling mit 500 ms für diese Browser-Session aktivieren:
tap_action:
  action: fire-dom-event
  uix:
    action: javascript
    data:
      code: window.uixCoordinator?.setThrottleOverride(500)

# Throttling-Override für diese Browser-Session deaktivieren:
hold_action:
  action: fire-dom-event
  uix:
    action: javascript
    data:
      code: window.uixCoordinator?.setThrottleOverride(null)
```

## Konfigurationsreferenz

| Einstellung | Standard | Beschreibung |
| --- | --- | --- |
| Throttle entity state updates | Aus | Aktiviert oder deaktiviert die State-Drosselung global. |
| Throttle interval | 200 ms | Mindestabstand zwischen State-Update-Re-Renders. Bereich: 50 bis 10.000 ms. |

## Wann sollte Throttling genutzt werden?

Nutze Throttling bei Dashboards mit vielen Karten, vielen schnell wechselnden Sensoren oder Geräten, auf denen das Frontend spürbar ruckelt.

::: warning
Ein zu großes Intervall kann Anzeigen träge wirken lassen. Starte konservativ, zum Beispiel mit 200 bis 500 ms, und prüfe die Bedienung danach im Alltag.
:::
