---
title: UGSo Energy – Widgets
description: Energiefluss, Verbrauch, Batteriespeicher und Preise als externes Widgetset für Home Assistant.
---

# UGSo Energy – Widgets

**UGSo Energy 0.1.0** ist ein eigenes externes Set für **Grafik Visual Studio 0.1.255 oder neuer**. Es gehört nicht zum Industrial-Paket. Entitätenauswahl und Livewerte funktionieren im Editor und in der Runtime; die Zeitraumwahl bedient die Runtime lokal, ohne Zustände in Home Assistant zu schreiben.

## Originalprojekt und Herkunft

Vorbild ist [ioBroker.vis-2-widgets-energy](https://github.com/ioBroker/ioBroker.vis-2-widgets-energy) von **bluefox / GermanBluefox und Mitwirkenden**, veröffentlicht unter der **MIT-Lizenz**. Die [Originaldokumentation](https://github.com/ioBroker/ioBroker.vis-2-widgets-energy/tree/main/docs/de) erklärt die ioBroker-Version. Geprüfter Quellstand: [d0a53871](https://github.com/ioBroker/ioBroker.vis-2-widgets-energy/commit/d0a53871ea7e57c5100de2a1f2ef7b2ee82059c7), 7. Oktober 2026.

UGSo Energy ist eine **eigenständige Home-Assistant-Anpassung von rockbaer2007**, keine unveränderte Portierung oder offizielle ioBroker-Veröffentlichung. Renderer, Symbole und HA-Anbindung sind neu implementiert; React-/vis-2-Quellcode und Originalbilder werden nicht eingebunden. Quelle und Lizenz stehen auch in der Paket-Anleitung.

## Bilder

Die Bilder zeigen die Runtime mit **Testdaten**, keine Live-Messungen.

![Energiefluss zwischen Netz, Haus, PV, Batteriespeicher und Wallbox](/images/grafik-visual-studio/energy-distribution.png)

| Batteriespeicher | Dynamischer Strompreis |
| --- | --- |
| ![Batterie mit Ladezustand, Leistung und Restzeit](/images/grafik-visual-studio/energy-battery.png) | ![Stündliche Strompreise mit günstigsten und teuersten Stunden](/images/grafik-visual-studio/energy-price.png) |

## Installation

1. Studio auf **0.1.255 oder neuer** aktualisieren und mit **Strg+F5** neu laden.
2. [ugso.energy.wg herunterladen](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/master/ha_grafik_visual_studio/packages/energy/ugso.energy.wg).
3. Unter **Einstellungen → Widget-Pakete → Lokal** installieren. Das Set erscheint als **UGSo Energy** in der Widgetpalette.
4. Widget einfügen und die Messquellen mit **…** aus der Home-Assistant-Entitätenauswahl übernehmen.

Die Datei enthält acht deklarative Widgets, eigene SVG-Palettensymbole und Lizenz/Anleitung. Ausführbarer Paketcode ist nicht enthalten. [Quellcode und Paket-Anleitung](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/energy).

## Die acht Widgets

| Widget | Funktion und Messquellen |
| --- | --- |
| Energiefluss | Haus und Netz plus **1–10 Zusatzknoten**. Je Knoten Name, Farbe, Leistungsentität, Multiplikator, umkehrbare Flussrichtung und optional zweiter Wert mit Einheit. Flussanimation abschaltbar. |
| Energieverbrauch | Bis **sechs Recorder-Reihen** als Balken oder Linien, Zählerdifferenzen oder Summe einzelner Verbrauchsmengen; Stunden/Tag/Monat nach Zeitraum. |
| Verbrauchsvergleich | Aktuelle Werte von bis **sechs Geräten**, Balken/Linie/Kreis, Sortierung, Farbe und Einheit je Reihe. Unterschiedliche Einheiten werden nicht auf derselben Achse verrechnet. |
| Zeitauswahl | Tag, Woche, Monat oder Jahr, Datum sowie Zurück/Heute/Weiter. Ein Wähler kann mehrere Verlauf-Widgets derselben Seite steuern. |
| Autarkie und Eigenverbrauch | Zwei Ringe aus Erzeugung, Netzbezug/Einspeisung und optional Hausverbrauch. Ohne Hausquelle wird die Bilanz berechnet. |
| Batteriespeicher | Ladezustand, Leistung, Kapazität, gespeicherte Energie und rechnerische Zeit bis voll/leer. Vorzeichen für Laden wählbar, Leistung in W oder kW. |
| Energiekosten | Verbrauch × Bezugspreis + Grundgebühr pro Kalendertag − Einspeisevergütung; aktuelle Energiezähler oder Recorder-Zeitraum. Währung einstellbar. |
| Dynamischer Strompreis | JSON aus Zustand oder Attribut, Stundenbalken, aktuelle/günstige/teure Stunden und Durchschnitt. Negative Preise bleiben erhalten. |

## Einheiten und unbekannte Werte

**Multiplikatoren sind ausdrücklich einzustellen**: z. B. `0.001` für Wh → kWh oder W → kW. Ein W-Sensor wird nicht automatisch zu einem Energiezähler. Autarkie benötigt Werte derselben Art und Einheit: entweder Leistungen oder Energie desselben Zeitraums.

Netz positiv = Bezug, negativ = Einspeisung. Eine konfigurierte separate Einspeisequelle ersetzt die negative Netzkomponente. Energiefluss: positive Knotenwerte fließen standardmäßig zum Haus, negative davon weg; für Verbraucher oder anders herum zählende Batterien **Flussrichtung umkehren** aktivieren.

Ohne konfigurierte oder gültige Quelle erscheint **—**. Unbekannte Werte werden nicht durch erfundene Vorschauwerte ersetzt. Bei Nenner 0 bleiben Quoten unbekannt. Restzeit ist eine Schätzung aus aktueller Leistung und Kapazität, keine Vorhersage der Anlage.

## Recorder und Zeitauswahl

Für Verlauf und historische Kosten muss Home Assistant die numerischen Entitäten im **Recorder** speichern. In **ID der Zeitauswahl** die Widget-ID des Wählers derselben Seite eintragen, z. B. `widget-3`. Ohne Verknüpfung gelten eigener Zeitraum und Datum. Leer = aktuelles Datum.

**counter** berechnet Zählerdifferenzen mit gehaltenen Recorder-Zuständen. Unbekannte Zustände oder ein Zähler-Reset erzeugen eine Lücke; Rücksetzungen werden nicht als Verbrauch gerechnet. **sum** summiert einzelne Verbrauchsmengen und ist ungeeignet für kumulative Zähler. Laufende Zeiträume enthalten nur bereits erfasste Daten; zukünftige Abschnitte bleiben unbekannt. Eine Kosten-Gesamtsumme erscheint nur bei vollständigen gültigen Daten im bereits erfassten Teil.

Grenzen: **366 Tage**, **sechs Entitäten**, **20.000 Zustände je Reihe**. Zu große Antworten werden mit Hinweis abgebrochen. Zeitraumgrenzen folgen der lokalen Browserzeitzone. Alte Zeiträume können wegen der Recorder-Aufbewahrung fehlen. Diese Version verwendet **keine HA-Langzeitstatistiken**, keine ioBroker-History und keine automatische Leistungsintegration. Grundgebühren gelten für den ausgewählten Kalenderzeitraum; im Live-Kostenmodus müssen die Zählerwerte dazu passen.

## Preisdaten

Unterstützt werden Arrays im Zustand oder einem ausgewählten Attribut, auch in `prices`, `today`, `data`, `values` oder `result` verschachtelt. Zeitfelder werden aus `startsAt`, `start_timestamp`, `start`, `date`, `x` erkannt; Preisfelder aus `total`, `marketprice`, `price`, `value`, `y`. Andere Namen lassen sich eintragen. Zeitstempel können ISO, Sekunden oder Millisekunden sein. Ein Zahlenarray entspricht den Stunden des heutigen lokalen Tages.

Preisfaktor zur Quelle einstellen: **100** für EUR/kWh → ct/kWh, **0.1** für EUR/MWh → ct/kWh. Nur ab jetzt, Stundenanzahl sowie günstige/teure Stunden und deren Farben sind einstellbar.

## Unterschiede zum Original

Die acht Widgetarten orientieren sich am Original; Einstellungen und Anbindung sind an Studio und Home Assistant angepasst. Diese erste Version bietet lokale Zeitraumwahl und Recorder-Zustände, keine ioBroker-OIDs oder History-Instanzen, keine vollständige Übernahme aller vis-2-Layout-/Diagrammoptionen und keine direkten Geräteschreibfunktionen.
