---
title: Mushroom Fehlersuche
description: Typische Probleme mit Mushroom Cards und erste Schritte zur Fehlerbehebung.
---
# Fehlersuche

## Neue Aenderungen Sind Nicht Sichtbar

1. Pruefen, ob Home Assistant aktuell ist.
2. Pruefen, ob die neueste Mushroom-Version in HACS installiert ist.
3. Browser-Konsole pruefen, ob wirklich die erwartete Mushroom-Version geladen wird.
4. Cache leeren.
5. Mushroom-Ressource entfernen.
6. Mushroom aus HACS deinstallieren.
7. Mushroom erneut installieren.
8. Browser und Home-Assistant-App neu laden.

Direktlink zu den Lovelace-Ressourcen:

[Home Assistant Ressourcen oeffnen](https://my.home-assistant.io/redirect/lovelace_resources/)

## Card-Mod Funktioniert Nicht

Das Mushroom-Repository bietet keinen allgemeinen Support fuer `card-mod`-Konfigurationen.

Der Maintainer verweist auf diesen Status-Thread:

- [State of card-mod support](https://github.com/piitaya/lovelace-mushroom/issues/1366)

## Karte Wird Nicht Gefunden

Typische Ursachen:

- Ressource fehlt oder zeigt auf den falschen Pfad.
- Browsercache laedt noch eine alte Datei.
- HACS-Installation wurde nicht vollstaendig geladen.
- YAML nutzt einen falschen Kartentyp.

Beispiel fuer einen korrekten manuellen Ressourceneintrag:

```yaml
resources:
  - url: /local/mushroom.js
    type: module
```
