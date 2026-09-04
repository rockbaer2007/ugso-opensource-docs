---
title: Broker
description: UIX-Broker-Interaktionen konfigurieren und Konfigurationsquellen verwalten.
---
# UIX Broker

::: info Verfügbar ab UIX 8.2.0-beta.2
UIX Broker gehört zum aktuellen Entwicklungszweig.
:::

Eine Interaktion besteht aus `realm`, `listen`, einem Interaktions-`anchor`, optionalen `rules` und einer geordneten Liste von `directives`.

```yaml
uix_broker:
  - realm: shortcut
    debug: true
    listen: "$mod+Shift+Y"
    anchor: '&home-assistant'
    directives:
      - type: action
        action: fire-dom-event
        uix:
          action: toast
          data:
            message: Shortcut pressed
```

Siehe [Realms](./realms), [Interaction Anchors](./interaction-anchors), [Rules](./rules) und [Directives](./directives) für die einzelnen Teile einer Interaktion.

## Optionen einer Interaktion

| Schlüssel | Beschreibung |
| --- | --- |
| `realm` | Wo UIX lauscht: `browser`, `shortcut` oder `server`. |
| `listen` | DOM-Event-Name, [Tinykeys](https://jamiebuilds.github.io/tinykeys/)-Binding oder Home-Assistant-Event-Bus-Event für den gewählten Realm. Im `browser`-Realm darf dies auch eine Liste von DOM-Event-Namen sein. |
| `anchor` | Element, das geprüft und als Standardziel für Regeln und Direktiven genutzt wird. |
| `rules` | Optionale Bedingungen, die alle passen müssen, bevor Direktiven laufen. |
| `directives` | Geordnete Operationen, die bei passender Interaktion ausgeführt werden. |
| `enabled` | Standard ist `true`. Mit `false` bleibt die Interaktion in der Konfiguration, wird aber nicht registriert. |
| `reentrant` | Standard ist `true`. Mit `false` werden passende Events ignoriert, solange dieselbe Interaktion noch läuft. |
| `debug` | Mit `true` protokolliert UIX den Ablauf in der Browser-Konsole. |

Jede Interaktion ist unabhängig. Alle Regeln müssen passen, und Direktiven laufen nacheinander in der Reihenfolge der Konfiguration.

Nutze eine `listen`-Liste im Browser-Realm, wenn dieselbe Interaktion auf mehrere Browser-Events reagieren soll:

```yaml
- realm: browser
  listen:
    - uix-broker-ready
    - uix-update
  anchor: '&home-assistant'
  directives:
    - type: call
      method: requestUpdate
```

Listen werden nur im `browser`-Realm unterstützt. `shortcut`- und `server`-Interaktionen lauschen jeweils auf ein einzelnes Binding oder einen einzelnen Event-Namen.

`reentrant: false` ist nützlich, wenn eine Interaktion dasselbe Event auslöst, durch das sie gestartet wurde. Die Interaktion gilt als aktiv, solange Anchors aufgelöst, Direktiven ausgeführt oder Wartezeiten verarbeitet werden.

## Broker-Ready-Event

Nachdem UIX Broker seine Konfiguration angewendet hat, löst er auf `window` das Browser-Event `uix-broker-ready` aus. Das Event wird ausgelöst, nachdem Broker seine Browser-Realm-Listener registriert hat. Eine Interaktion kann auf dieses Event lauschen, um eine anfängliche UI-Anpassung anzuwenden. Es wird außerdem nach jedem Broker-Konfigurations-Reload ausgelöst.

Siehe [Werkzeug-Button zum Sidebar-Titel hinzufügen](./examples#werkzeug-button-zum-sidebar-titel-hinzufuegen) für ein Beispiel mit diesem Event.

## Konfigurationsquellen

Interaktionen können auf mehreren Wegen konfiguriert werden:

1. Im UIX-Optionsdialog: **Settings -> Devices & services -> UIX -> Configure -> Configure Broker**.
2. In einer oder mehreren registrierten YAML-Dateien: **Settings -> Devices & services -> UIX -> Configure -> Manage Broker files**.

Eine YAML-Datei enthält eine Top-Level-Liste `uix_broker`:

```yaml
uix_broker:
  - realm: browser
    listen: click
    anchor: target
    rules:
      - home-assistant
    directives:
      - type: block
```

Über **Manage Broker files** können Dateien registriert, entfernt oder neu geladen werden. Pfade dürfen absolut sein oder relativ zum Home-Assistant-Konfigurationsverzeichnis liegen. Dateien werden in Registrierungsreihenfolge gelesen, danach werden über die UI konfigurierte Interaktionen angehängt. Alle Interaktionen werden als eine Liste an verbundene Browser ausgeliefert.

YAML-Dateien nutzen dieselbe Home-Assistant-YAML-Auflösung wie Foundries, inklusive `!include` und `!secret`. Die Aktion **UIX Broker** unter **Tools -> YAML** lädt registrierte Broker-Dateien neu und meldet Datei-Fehler. Bei YAML-Dashboards lädt auch die eingebaute **Refresh**-Aktion registrierte Broker-Dateien neu.

## Synchrone und asynchrone Ausführung

Captured-Data- und Browser-Identity-Regeln laufen synchron vor der Auflösung des Interaction Anchors. Event-Pfad-Anchors werden ebenfalls synchron aufgelöst. Dadurch kann eine Browser-Interaktion mit `block` ein Event früh genug stoppen.

Da die Direktive `block` synchron laufen muss, benötigen Interaktionen mit `block` sofort verfügbare Interaction Anchors und Host-Element-Regel-Anchors. UIX Broker macht hier nur eine synchrone Suche. Ist ein Anchor nicht verfügbar, wird die Interaktion übersprungen.

Nach einer blockierenden Interaktion verwenden spätere `property`-, `event`-, `call`- und `button`-Direktiven wieder das normale asynchrone Retry-Verhalten.

Für Interaktionen ohne `block` werden fehlende Interaction Anchors und Host-Element-Regel-Anchors alle 50 ms bis zu zwei Sekunden lang erneut gesucht. Das hilft zum Beispiel bei Dialogen, die erst nach dem auslösenden Event gerendert werden.

## Debugging

Setze `debug: true` auf einer Interaktion, um Listener-Aktivität, Anchor-Auflösung, jedes Regelergebnis und jede Direktive vor und nach der Ausführung in der Browser-Konsole zu sehen. Der Nach-Ausführung-Eintrag einer `template`- oder `javascript`-Direktive enthält außerdem ihr gespeichertes Ergebnis. Debug-Meldungen sind mit Realm und Listen-Wert der Interaktion gekennzeichnet.

```yaml
- realm: browser
  listen: click
  anchor: target
  debug: true
  rules:
    - ".action-button"
  directives:
    - type: event
      name: another-event
```

## Reaktive Interaktionen

UIX-Broker-Direktiven vom Typ [`template` und `javascript`](directives) laufen nur, wenn ihre Interaktion läuft; sie abonnieren keine Statusänderungen. Wenn eine Interaktion auf Entity-Statusänderungen reagieren soll, legst du eine Hilfsinteraktion an, die auf `state_changed` lauscht. Mit einer [Regel](./rules) filterst du die gewünschte Entity und nutzt eine `event`-Direktive, um ein eigenes Browser-Event auszulösen. Dieses Browser-Event fügst du anschließend der `listen`-Liste der eigentlichen Interaktion hinzu.

Server-Realm-zu-Browser-Realm-Hilfsinteraktion:

```yaml
  - realm: server
    listen: state_changed
    anchor: "&home-assistant"
    directives:
      - type: event
        name: uix-update-my-interaction
        rules:
          - type: captured
            path: data.entity_id
            match:
              or:
                - switch.bed_light
                - light.bed_light
```

Browser-Realm-Interaktion:

```yaml
  - realm: browser
    listen:
      - uix-broker-ready
      - uix-update-my-interaction
    anchor: "&home-assistant $ home-assistant-main $ ha-sidebar"
    # ... Regeln und Direktiven
```

Ein vollständiges Beispiel findest du unter [Light-Button am Home-Dashboard-Menüpunkt der Sidebar](./examples#light-button-am-home-dashboard-menupunkt-der-sidebar).
