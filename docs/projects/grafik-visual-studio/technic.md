---
title: UGSo Technic
description: Das externe Technic-Widget-Set installieren und Window – Wall mit Home Assistant verbinden.
---

# UGSo Technic

**Inspiriert von den [ioBroker-Technic-Widgets von Sefina-DS](https://github.com/Sefina-DS/ioBroker.vis-2-widgets-technic).** Eigene Umsetzung für Home Assistant.

Ab **Studio 0.1.199** kannst du **UGSo Technic 1.2.0** installieren. Das Paket enthält **Window – Wall**, **Switch – Boolean** und **Dimmer – Light**. Die vier weiteren Widgets des Originalsets sind noch nicht enthalten. Version 1.2.0 kann über die Paketverwaltung als Erweiterung von 1.0.0 oder 1.1.0 installiert werden; bestehende Widgets bleiben erhalten.

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

## Switch – Boolean

Der Schalter entspricht den Einstellmöglichkeiten von `tplTechnicSchalterBoolean`. Standard: **Device**, Bezeichnung sichtbar unten, 120 × 160 Pixel, Power-Symbol bei 80 %, Farbe EIN `#2dd4b0`, Farbe AUS `#5f8f8a`.

**Datenpunkt (EIN/AUS)** bindet die HA-Entität. **Werttyp → Wahr / Falsch** liest `on`/`off` und schaltet verfügbare `switch`, `light` oder `input_boolean` über `turn_on`/`turn_off`. **0 / 1** liest ausschließlich 0 und 1 und schreibt Zahlenwerte an einen `input_number`-Helfer. Dessen Grenzen und Schrittweite müssen beide Werte zulassen. Sensoren bleiben Anzeigen; unbekannte, fehlende oder nicht verfügbare Zustände sind nicht schaltbar.

**Icon auswählen** bietet alle 16 Symbolarten: Auswahl, Desktop-PC, Power, Bettlampe, Hängelampe, runde Hängelampe, Schreibtischlampe, Spots, RGB-LED-Streifen, Tischlampe, Link, Lüfter, Schlüssel, Smartphone, Steckdose und TV. Es sind eigene geometrische SVG-Zeichnungen, keine übernommenen Grafik-Traces. Farbe EIN/AUS und Größe sind einstellbar. „Auswahl“ zeigt den Haken nur bei EIN.

Ein Klick auf das Symbol schaltet in der Runtime; die Bezeichnung bleibt sichtbar. Tastaturbedienung mit Tab und Enter/Leertaste ist möglich. **Schreibgeschützt** sperrt Änderungen. Laufende Aktionen werden nicht doppelt gesendet; Fehler zeigen einen Hinweis und erlauben einen erneuten Versuch. **EIN (Vorschau)** gilt nur ungebunden im Editor. Alle Einstellungen bleiben im Projekt und Export erhalten.

![Schalter nach dem Einschalten mit sichtbarer Beschriftung](/images/grafik-visual-studio/technic-switch-runtime.png)

## Dimmer – Light

Entspricht den Optionen von `tplTechnicReglerLicht`: Bezeichnung **Light**, sichtbar unten, Icon-Größe 80 %, 160 × 200 Pixel. **Farbe EIN** ist `#2ecfbf`, **Farbe AUS** `#5f8f8a`, **Regler-Hintergrund** `#0d1820`. Größe, Farben und Beschriftungsposition sind einstellbar; die Darstellung ist eine eigene SVG-Umsetzung.

**Ein/Aus: Entität** akzeptiert `light`, `switch` oder `input_boolean`. **Helligkeit: Entität (0–100)** akzeptiert eine dimmbare `light`-Entität oder einen `input_number`-Helfer. Für ein gewöhnliches HA-Licht trägst du **dieselbe light-Entität in beide Felder** ein. Der Host rechnet das HA-Attribut `brightness` von 0–255 in Prozent um. Bei AUS zeigt er 0 %. Ein Zahlenhelfer sollte min = 0, max = 100 und step = 1 haben. Sensoren können Werte anzeigen, werden aber nicht beschrieben.

**Ein/Aus mit Helligkeit verknüpfen** ist standardmäßig aktiv: EIN setzt 100 %, AUS setzt 0 %, Dimmen über 0 schaltet ein. Beide Bindungen müssen verfügbar und schreibbar sein. Bei derselben light-Entität wird ein einzelner HA-Aufruf erzeugt. Ohne Verknüpfung bleiben getrennte Bindungen unabhängig; eine HA-Helligkeitsaktion über `light.turn_on` schaltet das betreffende Licht dennoch ein. 0 % verwendet `light.turn_off`.

Ziehe den äußeren Kreisbogen oder nutze den Schieberegler mit Tastatur. Der Wert wird während des Ziehens lokal angezeigt und erst beim Loslassen übertragen. Der mittlere Power-Knopf schaltet EIN/AUS. Die Bezeichnung bleibt sichtbar. **Schreibgeschützt** sperrt Aktionen; unbekannte oder nicht dimmbare Entitäten sind nicht bedienbar. Fehlende Live-Werte werden nicht durch Vorschau ersetzt. **EIN (Vorschau)** und **Helligkeit (Vorschau)** gelten nur ungebunden im Editor.

Der Host prüft alle Ziele vor dem ersten Schreibvorgang. Bei getrennten Entitäten werden die HA-Aufrufe nacheinander ausgeführt; ein Anbieterfehler kann eine Aktion teilweise anwenden. Der Fehlerhinweis fordert zur Zustandsprüfung vor erneutem Versuch auf. Laufende Aktionen werden nicht doppelt gesendet. Die Bedienung wurde mit simulierten HA-Entitäten geprüft; reale Hardware muss separat getestet werden.

![Lichtregler in der Runtime bei 50 Prozent mit sichtbarer Beschriftung](/images/grafik-visual-studio/technic-light-runtime.png)

## Vorschau und Export

**Vorschau** bietet Fenster offen, Rolloposition und Manuell. Diese Werte gelten nur für ungebundene Anzeigen im Editor. Bei einer Bindung werden Live-Werte gelesen. In der Runtime bleiben ungebundene oder fehlende Werte unbekannt; sie werden nicht durch Vorschauwerte ersetzt. Im Editor lösen Klicks keine HA-Schaltaktionen aus.

Alle Anzeigeoptionen, drei Entitätsbindungen, Invertierungen, Vorschauwerte und Schreibschutz bleiben im Projekt und Widget-Export erhalten. Die Prüfung erfolgte mit simulierten HA-Entitäten; eine reale Rollo-Steuerung muss mit deiner Hardware getestet werden.
