---
title: Calendar Card Pro Installation
description: Calendar Card Pro über HACS oder manuell installieren.
---
# Installation

## HACS Installation

Der empfohlene Weg ist HACS.

1. Pruefen, ob HACS installiert ist.
2. In Home Assistant **HACS** öffnen.
3. Zu **Frontend** wechseln.
4. **Custom Repositories** öffnen.
5. Repository eintragen: `https://github.com/alexpfau/calendar-card-pro`
6. Typ auf `Dashboard` setzen.
7. Calendar Card Pro installieren.
8. Browsercache leeren und Home Assistant neu laden.

Direktlink:

[Calendar Card Pro in HACS oeffnen](https://my.home-assistant.io/redirect/hacs_repository/?owner=alexpfau&repository=calendar-card-pro&category=plugin)

## Manuelle Installation

Bei manueller Installation müssen beide Release-Dateien geladen werden:

- `calendar-card-pro.js`
- `editor.js`

Beide Dateien gehören in denselben Unterordner, zum Beispiel:

```text
/config/www/calendar-card-pro/
```

Danach wird nur `calendar-card-pro.js` als Ressource eingetragen. Die Karte lädt den Editor selbst, wenn er benötigt wird.

```yaml
url: /local/calendar-card-pro/calendar-card-pro.js
type: module
```

::: tip Warum ein eigener Ordner?
`editor.js` ist ein allgemeiner Dateiname. Ein eigener Unterordner verhindert Namenskonflikte mit anderen manuell installierten Karten.
:::

## Voraussetzungen

Calendar Card Pro benötigt mindestens eine Kalenderentität in Home Assistant, zum Beispiel:

```text
calendar.family
calendar.work
calendar.personal
```

Ohne Kalenderintegration gibt es keine Termine, die die Karte anzeigen kann.
