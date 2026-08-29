---
title: Dialog Styling Delay
description: UIX-Dialog-Styling verzögert anwenden.
---
# Dialog Styling Delay

Dialog Styling Delay verschiebt das Anwenden von UIX-Styles auf Dialoge, bis der Dialog vollständig angezeigt wird. Das hilft bei Dialogen, deren DOM erst nach der Öffnungsanimation vollständig verfügbar ist.

## Aktivierung über die Integrations-UI

1. In Home Assistant zu **Settings -> Devices & Services -> UI eXtension -> Configure** gehen.
2. **Performance settings** öffnen.
3. **Delay UIX styling for dialogs until fully shown** aktivieren.
4. Speichern.

## So funktioniert es

Normalerweise versucht UIX, Dialog-Styling direkt beim Erstellen oder Anzeigen des Dialogs anzuwenden. Manche Home-Assistant-Dialoge oder Custom-Dialoge montieren ihre internen Elemente aber erst etwas später. Mit Dialog Styling Delay wartet UIX, bis der Dialog vollständig gezeigt wird.

::: info
Die Option betrifft Dialog-Styling, nicht normale Karten- oder View-Styles. Sie kann besonders bei More-info-Dialogen, adaptiven Dialogen oder Custom-Dialogen helfen.
:::

## Clientseitige Override-API

`window.uixCoordinator` stellt eine Methode bereit, mit der das Verhalten pro Browser überschrieben werden kann.

```js
window.uixCoordinator.setDialogApplyAfterShowOverride(true)
window.uixCoordinator.setDialogApplyAfterShowOverride(false)
window.uixCoordinator.setDialogApplyAfterShowOverride(null)
```

### Mit Browser Mod verwenden

```yaml
# In der Browser-Mod-Konfiguration für eine bestimmte Browser-ID:
service: browser_mod.javascript
data:
  browser_id: wall-tablet
  code: |
    window.uixCoordinator?.setDialogApplyAfterShowOverride(true)
```

### Mit custom:button-card verwenden

```yaml
# Dialog Styling Delay für diese Browser-Session aktivieren:
tap_action:
  action: fire-dom-event
  uix:
    action: javascript
    data:
      code: window.uixCoordinator?.setDialogApplyAfterShowOverride(true)

# Override wieder löschen:
hold_action:
  action: fire-dom-event
  uix:
    action: javascript
    data:
      code: window.uixCoordinator?.setDialogApplyAfterShowOverride(null)
```

## Konfigurationsreferenz

| Einstellung | Standard | Beschreibung |
| --- | --- | --- |
| Delay UIX styling for dialogs until fully shown | Aus | Wenn aktiviert, wendet UIX Dialog-Styles nach Abschluss der Öffnungsanimation an statt sofort. |

## Wann sollte Dialog Styling Delay genutzt werden?

Nutze die Option, wenn Dialog-Styles manchmal nicht greifen, erst nach erneutem Öffnen sichtbar werden oder nur bei bestimmten Browsern/Companion-App-Sessions zuverlässig erscheinen.

::: warning
Die Verzögerung kann sichtbar sein, wenn sehr starke Dialog-Styles angewendet werden. Aktiviere sie nur, wenn sie ein echtes Timing-Problem löst.
:::

## Reihenfolge der Einstellungen

UIX kann Dialog Styling Delay aus mehreren Quellen erhalten. Entscheidend ist die konkrete Browser-Session.

| Quelle | Wirkung |
| --- | --- |
| Integrations-UI | Globaler Standard für alle Browser |
| `setDialogApplyAfterShowOverride(true)` | Aktiviert Delay nur für diese Browser-Session |
| `setDialogApplyAfterShowOverride(false)` | Deaktiviert Delay nur für diese Browser-Session |
| `setDialogApplyAfterShowOverride(null)` | Entfernt den Session-Override und nutzt wieder den globalen Standard |

Der Override ist besonders nützlich für Wandtablets oder Companion-App-Sessions, wenn nur ein Gerät Timing-Probleme zeigt.

## Typische Dialoge

| Dialogtyp | Wann Delay helfen kann |
| --- | --- |
| More-info | Inhalte werden erst nach Öffnung vollständig montiert |
| Browser-Mod-Dialog | Custom-Inhalte erscheinen verzögert |
| Adaptive Dialoge | Layout ändert sich während der Öffnungsanimation |
| Custom-Card-Dialoge | Interne Shadow Roots entstehen erst nach dem ersten Render |

## Testablauf

1. Dialog ohne Delay öffnen und prüfen, ob UIX-Styling direkt greift.
2. Delay global oder per Browser-Override aktivieren.
3. Home Assistant im Browser hart neu laden.
4. Dialog erneut öffnen und vergleichen.
5. Wenn nur ein Gerät betroffen ist, global wieder deaktivieren und den Browser-Override nutzen.

## Rückgängig machen

Global wird die Option wieder in der Integrations-UI deaktiviert. Ein lokaler Override wird so entfernt:

```js
window.uixCoordinator.setDialogApplyAfterShowOverride(null)
```

Danach gilt wieder der globale Wert aus der Integration.
