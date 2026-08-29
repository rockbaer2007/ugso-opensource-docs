---
title: UIX Actions
description: UIX-spezifische Actions im Home-Assistant-Frontend.
---
# UIX Actions

UIX Actions erweitern Home-Assistant-Actions um zusätzliche Frontend-Funktionen. Sie können in normalen Home-Assistant-Action-Konfigurationen genutzt werden, wenn ein Element `fire-dom-event` auslöst und darunter ein `uix`-Action-Block steht.

::: info
UIX Actions laufen im Browser. Sie eignen sich für Frontend-Aktionen wie Cache leeren, More-info öffnen, Toast anzeigen oder JavaScript ausführen.
:::

Grundform:

```yaml
# ... card config
tap_action:
  action: fire-dom-event
  uix:
    action: toast
    data:
      message: Hallo von UIX
```

::: info
Die genaue Unterstützung hängt davon ab, ob die jeweilige Karte `fire-dom-event` weiterleitet. Viele Custom Cards tun das, Standardkarten je nach Action-Kontext.
:::

## `clear-cache`: Home-Assistant-Frontend-Cache leeren

| Konfiguration | Einstellung | Standard | Beschreibung |
| --- | --- | --- | --- |
| `action: clear-cache` | - | - | Leert den Home-Assistant-Application-Cache und lädt den Browser neu. |
| `data:` | - | - | Wird nicht verwendet. |

```yaml
tap_action:
  action: fire-dom-event
  uix:
    action: clear-cache
```

## `more-info`: More-info für eine Entität mit Startansicht öffnen

| Konfiguration | Einstellung | Standard | Beschreibung |
| --- | --- | --- | --- |
| `action: more-info` | - | - | Öffnet den Home-Assistant-More-info-Dialog mit den Optionen aus `data`. |
| `data:` | - | - | Entity- und View-Optionen für More-info. |
| | `entity` | - | Entity-ID, für die More-info geöffnet wird. |
| | `view` | `info` | Startansicht: `info`, `history`, `settings`, `related`, `add_to`, `details`. |

```yaml
tap_action:
  action: fire-dom-event
  uix:
    action: more-info
    data:
      entity: light.bed_light
      view: history
```

## `toast`: Home-Assistant-Toast anzeigen

| Konfiguration | Einstellung | Standard | Beschreibung |
| --- | --- | --- | --- |
| `action: toast` | - | - | Zeigt eine Home-Assistant-Toast-Benachrichtigung mit Optionen aus `data`. |
| `data:` | - | - | Toast-Optionen. |
| | `id` | - | ID der Toast-Nachricht. Gleiche ID ersetzt eine vorhandene Nachricht. |
| | `message` | **Pflicht** | String oder Übersetzungsobjekt mit `translationKey` und optionalen `args`. |
| | `duration` | `4000` | Dauer in ms. Werte unter 4000 werden auf 4000 gesetzt. `-1` zeigt den Toast unbegrenzt. |
| | `dismissable` | `false` | Zeigt ein Schließen-Icon. |
| | `bottomOffset` | `0` | Zusätzlicher Abstand vom unteren Fensterrand. |
| | `action` | - | Optionale Schaltfläche mit `action.tap_action`. |
| | `action.primary` | - | Rendert die Action-Schaltfläche im Primary-Stil. |
| | `action.text` | **Pflicht** | Text oder Übersetzungsobjekt für die Action. |
| | `action.tap_action` | **Pflicht** | Home-Assistant-Action-Konfiguration. |
| | `secondary_action` | - | Zweite Schaltfläche links neben `action`. |
| | `secondary_action.primary` | - | Rendert die zweite Schaltfläche im Primary-Stil. |
| | `secondary_action.text` | **Pflicht** | Text oder Übersetzungsobjekt für die zweite Action. |
| | `secondary_action.tap_action` | **Pflicht** | Home-Assistant-Action-Konfiguration. |

```yaml
tap_action:
  action: fire-dom-event
  uix:
    action: toast
    data:
      id: uix-demo
      message: UIX wurde ausgeführt
      duration: 5000
      dismissable: true
      action:
        text: Details
        tap_action:
          action: more-info
          entity: light.bed_light
```

## `javascript`: JavaScript in der Browser-Session ausführen

::: warning
Führe JavaScript nur aus vertrauenswürdigen UIX-Konfigurationen aus. JavaScript läuft im Browserkontext.
:::

| Konfiguration | Einstellung | Standard | Beschreibung |
| --- | --- | --- | --- |
| `action: javascript` | - | - | Führt JavaScript-Code mit Optionen aus `data` aus. |
| `data:` | - | - | JavaScript-Optionen. |
| | `code` | **Pflicht** | Auszuführender JavaScript-Code. |
| | `variables` | `{}` | Optionales Variablenobjekt. Jede benannte Variable ist als `variables.<name>` verfügbar. |

```yaml
tap_action:
  action: fire-dom-event
  uix:
    action: javascript
    data:
      variables:
        entity: light.bed_light
      code: |
        console.log('UIX JavaScript action', variables.entity)
```
