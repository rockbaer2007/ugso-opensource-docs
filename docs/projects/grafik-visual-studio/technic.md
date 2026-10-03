---
title: UGSo Technic
description: Das externe Technic-Widget-Set installieren und Window – Wall mit Home Assistant verbinden.
---

# UGSo Technic

**Inspiriert von den [ioBroker-Technic-Widgets von Sefina-DS](https://github.com/Sefina-DS/ioBroker.vis-2-widgets-technic).** Eigene Umsetzung für Home Assistant.

Ab **Studio 0.1.197** kannst du **UGSo Technic 1.0.0** installieren. Dieses erste Paket enthält **Window – Wall**. Die sechs weiteren Widgets des Originalsets sind noch nicht enthalten.

## Installieren

Lade [ugso.technic.wg](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/refs/heads/master/ha_grafik_visual_studio/packages/technic/ugso.technic.wg) herunter. Öffne **Einstellungen → Widget-Pakete → Lokales .wg / .wg.zip installieren** und wähle die Datei. Nach dem Neuladen erscheint das Set mit einer automatisch vergebenen freien Farbe. Es bleibt unabhängig von den integrierten Widgets und von Wetter und Heizung.

Der [Quellcode und reproduzierbare Paketbau](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/technic) sind öffentlich. Das Downloadpaket enthält `README.md` und `LICENSE.txt`, einschließlich des vollständigen MIT-Lizenztextes und des Herkunftshinweises `Copyright (c) 2026 Sefina-DS`.

## Window – Wall

Unter **Allgemein** stellst du Bezeichnung, **Bezeichnung anzeigen**, Position oben/unten, Icon-Größe (10–100 %), Griff links/rechts und Icon-Farbe ein. Die Standardgröße beträgt 120 × 160 Pixel. **Schreibgeschützt** sperrt die Bedienung.

Unter **Datenpunkte** gibt es drei unabhängige HA-Bindungen:

| Originalfeld | Studio-Feld | Home Assistant |
| --- | --- | --- |
| `oid_kontakt` | Öffnungskontakt: Entität | beispielsweise `binary_sensor.fenster_garage`; `on` bedeutet offen |
| `oid_rollo` | Rollo: cover-Entität | beispielsweise `cover.rollo_garage`; liest `current_position` |
| `oid_modus` | Modus: Entität | beispielsweise `input_boolean.rollo_manuell`; aus = Automatik, ein = Manuell |

Jede Bindung besitzt eine eigene Invertierung. **Rollo invertieren** dreht Anzeige und Schreibwert um (`100 − Position`). Im normalen Betrieb bedeutet 0 geschlossen und 100 offen. Ein unbekannter Wert bleibt auch nach Invertierung unbekannt. Der Kontakt wird ausschließlich gelesen. Ein optionales **A/M**-Symbol zeigt den Modus; `?` zeigt einen unbekannten Modus.

![Installiertes Technic-Set und HA-Bindungen im Editor](/images/grafik-visual-studio/technic-window-editor.png)

## Bedienung

In der Runtime öffnet ein Klick auf das Fenster einen Dialog mit Positionsregler, Schnellwerten **0 / 25 / 50 / 75 / 100 %** und optionalem Moduswechsel. Bedienung ist auch mit Tastatur möglich; Escape oder **Schließen** beendet den Dialog. Die Rollo-Aktion verwendet ausschließlich `cover.set_cover_position` für die ausgewählte Entität. Verfügbare Positionssteuerung (`supported_features` mit SET_POSITION) wird vor dem Schreiben geprüft. Der Modus schreibt nur an verfügbare `input_boolean`- oder `switch`-Entitäten. Ein Sensor bleibt eine Anzeige.

Der Modus-Helfer bildet nur den Schalter ab: Die eigentliche Rollo-Automatik musst du in Home Assistant einrichten. Es wird keine Automatisierung erzeugt oder deaktiviert. Fehlgeschlagene Aktionen zeigen einen Hinweis und lassen einen erneuten Versuch zu; ausstehende Aktionen werden nicht doppelt gesendet.

![Runtime-Dialog mit Rolloposition und Moduswechsel](/images/grafik-visual-studio/technic-window-runtime.png)

## Vorschau und Export

**Vorschau** bietet Fenster offen, Rolloposition und Manuell. Diese Werte gelten nur für ungebundene Anzeigen im Editor. Bei einer Bindung werden Live-Werte gelesen. In der Runtime bleiben ungebundene oder fehlende Werte unbekannt; sie werden nicht durch Vorschauwerte ersetzt. Im Editor lösen Klicks keine HA-Schaltaktionen aus.

Alle Anzeigeoptionen, drei Entitätsbindungen, Invertierungen, Vorschauwerte und Schreibschutz bleiben im Projekt und Widget-Export erhalten. Die Prüfung erfolgte mit simulierten HA-Entitäten; eine reale Rollo-Steuerung muss mit deiner Hardware getestet werden.
