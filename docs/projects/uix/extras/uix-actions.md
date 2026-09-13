---
title: UIX Actions
description: UIX-Actions für Cache, More-info, Toasts, JavaScript und Aktionen mit Code-Abfrage.
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

## `locked_action`: Aktion erst nach Code oder Bestätigung ausführen

::: info Verfügbar ab UIX 8.3.0-beta.2
Diese Ergänzung gehört zur 8.3-Vorabversion, nicht zur stabilen Basis 8.2.0.
:::

`locked_action` führt eine normale Home-Assistant-Action erst aus, nachdem der aktuelle Benutzer die konfigurierte Sperre passiert hat. Das eignet sich beispielsweise für Neustarts, Tore oder wichtige Einstellungen, ohne die gesamte Karte in einen Forge Lock zu hüllen.

```yaml
type: button
name: Home Assistant neu starten
tap_action:
  action: fire-dom-event
  uix:
    action: locked_action
    data:
      locks:
        - code: 1234
          admins: true
      locked_action:
        action: perform-action
        perform_action: homeassistant.restart
```

::: warning Schutz vor versehentlicher Bedienung
Die Sperre wirkt im Frontend und ist keine Berechtigungsgrenze. Wer das Dashboard bearbeiten oder seine geladene Konfiguration untersuchen kann, sieht den Code und die geschützte Action. Für Zugriffsschutz sind Home-Assistant-Berechtigungen und serverseitige Kontrollen erforderlich.
:::

### Konfiguration

| Schlüssel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `locked_action` | object | — | **Pflicht:** Home-Assistant-Action nach bestandener Sperre. |
| `locks` | list | `[]` | Geordnete Liste der Sperreinträge; siehe [Zuordnung](#zuordnung-der-sperren). |
| `permissive` | boolean | `false` | Bei `true` dürfen Benutzer ohne passenden Eintrag die Aktion ausführen. |
| `entity` | string | — | Entity-ID für eine verschachtelte Action, die eine Karten-Entity verwendet. |
| `code_dialog` | object | — | Beschriftungen für die Code-/Passphrase-Abfrage. |
| `id` | string oder number | — | Stabile Kennung für Fehlversuche und Sperrzeiten; bei `retry_delay` oder `max_retries` dringend empfohlen. Pro geschützter Action eine eigene ID verwenden. |

`locked_action` akzeptiert normale Home-Assistant-Action-Objekte, darunter `perform-action`, `toggle`, `more-info`, `navigate` und `fire-dom-event`.

### Zuordnung der Sperren

`locks` wird in Reihenfolge geprüft. Der erste passende aktive Eintrag bestimmt die Abfrage. Passt kein aktiver Eintrag, erlaubt der erste passende Eintrag mit `active: false` die Aktion ohne Abfrage.

| Konfiguration | Passende Benutzer |
| --- | --- |
| `users` vorhanden | Benutzer mit einem Namen in der Liste; mit `admins: true` zusätzlich alle Administratoren. |
| Ohne `users` | Alle Nicht-Administratoren außer den unter `except` genannten Benutzern. |
| Ohne `users`, mit `admins: true` | Alle Benutzer außer den unter `except` genannten Benutzern. |

`admins` erweitert die Zuordnung: Ohne diese Option sind Administratoren ausgeschlossen, sofern sie nicht in `users` stehen. Passt kein Sperreintrag, erlaubt `permissive: true` die Aktion. Beim Standard `permissive: false` umgehen Administratoren die Bediensperre; Nicht-Administratoren dürfen die Aktion nicht ausführen.

### Schlüssel eines Sperreintrags

| Schlüssel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `active` | boolean | `true` | `false` erlaubt passenden Benutzern die Aktion ohne Abfrage. |
| `code` | string oder number | — | Einzugebender Code. Rein numerische Codes öffnen den HA-Ziffernblock, andere Werte ein Passwortfeld. |
| `pin` | string oder number | — | Alias für `code`. |
| `confirmation` | string, boolean oder object | — | Bestätigung nach einer eventuellen Code-Abfrage. `true` verwendet den HA-Standardtext; ein String eigenen Text, ein Objekt `title` und `text`. |
| `users` | Liste von Strings | — | Namen der Benutzer, für die der Eintrag gilt. |
| `admins` | boolean | `false` | Bezieht zusätzlich Administratoren ein; ohne `users` gilt der Eintrag dadurch für alle Benutzer. |
| `except` | Liste von Strings | — | Ausgenommene Benutzernamen bei Einträgen ohne `users`. |
| `retry_delay` | number oder string | — | Wartezeit nach falschem Code; Zahl in Millisekunden oder String mit Einheit, etwa `"10s"`. |
| `max_retries` | number | — | Erlaubte Fehlversuche vor der längeren Sperre. |
| `max_retries_delay` | number oder string | `30000` | Sperrdauer nach `max_retries`; Millisekunden oder etwa `"30s"` / `"5m"`. |

### Code-Dialog

Mit `code_dialog` werden die Texte für Code- und Passphrase-Abfragen angepasst:

| Schlüssel | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `title` | string | Home-Assistant-Standard | Dialogtitel. |
| `submit_text` | string | Home-Assistant-Standard | Beschriftung der Bestätigungsschaltfläche. |
| `cancel_text` | string | Home-Assistant-Standard | Beschriftung der Abbruchschaltfläche. |

### Fehlversuche und Sperrzeiten

Fehlversuche bleiben in der aktuellen Browser-Session gespeichert. Eine explizite `id` erhält die Zuordnung auch dann, wenn ein Template oder eine Custom Card das Bedienelement neu erzeugt. Gleiche IDs teilen denselben Fehlversuchszähler; verschiedene geschützte Aktionen sollten deshalb verschiedene IDs haben.

```yaml
tap_action:
  action: fire-dom-event
  uix:
    action: locked_action
    data:
      id: restart-home-assistant
      code_dialog:
        title: Administrator-PIN eingeben
        submit_text: Neu starten
      locks:
        - code: 1234
          admins: true
          max_retries: 3
          max_retries_delay: 5m
      locked_action:
        action: perform-action
        perform_action: homeassistant.restart
```
