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
| `listen` | DOM-Event-Name, [Tinykeys](https://jamiebuilds.github.io/tinykeys/)-Binding oder Home-Assistant-Event-Bus-Event für den gewählten Realm. |
| `anchor` | Element, das geprüft und als Standardziel für Regeln und Direktiven genutzt wird. |
| `rules` | Optionale Bedingungen, die alle passen müssen, bevor Direktiven laufen. |
| `directives` | Geordnete Operationen, die bei passender Interaktion ausgeführt werden. |
| `enabled` | Standard ist `true`. Mit `false` bleibt die Interaktion in der Konfiguration, wird aber nicht registriert. |
| `reentrant` | Standard ist `true`. Mit `false` werden passende Events ignoriert, solange dieselbe Interaktion noch läuft. |
| `debug` | Mit `true` protokolliert UIX den Ablauf in der Browser-Konsole. |

Jede Interaktion ist unabhängig. Alle Regeln müssen passen, und Direktiven laufen nacheinander in der Reihenfolge der Konfiguration.

`reentrant: false` ist nützlich, wenn eine Interaktion dasselbe Event auslöst, durch das sie gestartet wurde. Die Interaktion gilt als aktiv, solange Anchors aufgelöst, Direktiven ausgeführt oder Wartezeiten verarbeitet werden.

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

Nach einer blockierenden Interaktion verwenden spätere `property`-, `event`- und `call`-Direktiven wieder das normale asynchrone Retry-Verhalten.

Für Interaktionen ohne `block` werden fehlende Interaction Anchors und Host-Element-Regel-Anchors alle 50 ms bis zu zwei Sekunden lang erneut gesucht. Das hilft zum Beispiel bei Dialogen, die erst nach dem auslösenden Event gerendert werden.

## Debugging

Setze `debug: true` auf einer Interaktion, um Listener-Aktivität, Anchor-Auflösung, Regelergebnisse und Direktiven vor und nach der Ausführung in der Browser-Konsole zu sehen.

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
