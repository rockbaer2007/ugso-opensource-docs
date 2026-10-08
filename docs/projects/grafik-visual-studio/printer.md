---
title: UGSo Printer – Drucker und Patronen
description: Eigenständiges Drucker-Widgetset mit Status und bis zu sechs automatisch gleichmäßig verteilten Patronen.
---

# UGSo Printer

**UGSo Printer 0.1.0** ist ein eigenes externes Widgetset von **rockbaer2007** für **Grafik Visual Studio 0.1.261 oder neuer**. Es zeigt einen Drucker mit aktuellem Status und **1–6 Patronen oder Tonern**. Die Patronengrafiken verteilen sich automatisch in gleich breiten Spalten über die verfügbare Widgetbreite, auch nach Größenänderungen.

Das Bild zeigt die Runtime mit Testdaten.

![UGSo Printer mit sechs Patronen und Warnmarkierung](/images/grafik-visual-studio/printer-six.png)

## Originalprojekt

Vorbild ist [HA Printer Card von ADNPolymerase](https://github.com/ADNPolymerase/ha-printer-card), veröffentlicht unter der [MIT-Lizenz](https://github.com/ADNPolymerase/ha-printer-card/blob/main/LICENSE). Das Original ist eine Lovelace-Karte. UGSo Printer verwendet eine eigene SVG-Zeichnung, einen eigenen Studio-Renderer und ausdrücklich gewählte Home-Assistant-Entitäten. Originalcode und Originalgrafiken sind nicht eingebunden. Es gehört zu einem eigenen Set in der Palette und nicht zu Industrial.

## Installieren

1. Grafik Visual Studio auf **0.1.261 oder neuer** aktualisieren.
2. [ugso.printer.wg herunterladen](https://raw.githubusercontent.com/rockbaer2007/ugso-ha-mqtt-addons/master/ha_grafik_visual_studio/packages/printer/ugso.printer.wg).
3. Unter **Einstellungen → Widget-Pakete → Lokal** installieren.
4. **UGSo Printer → Drucker** aus der Palette einfügen und die Status- sowie Füllstandsentitäten mit **…** auswählen.

Das Paket enthält eine deklarative Widgetdefinition, ein eigenes Palettensymbol, Anleitung und MIT-Lizenz. Ausführbarer Paketcode ist nicht enthalten. [Quellcode und Paket-Anleitung](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/printer).

## Einstellungen

| Bereich | Einstellung |
| --- | --- |
| Drucker | Bezeichnung, Statusentität, Modell `mfp` (Multifunktion), `inkjet` (Tintenstrahl) oder `office` (Bürodrucker). |
| Patronen | Anzahl **1–6**, Darstellung als Tintenpatrone oder Toner, Warnschwelle **0–100 %**, Standard **20 %**. |
| Patrone 1–6 | Eigene Füllstandsentität in Prozent, Beschriftung und Farbe. Die ersten N Einträge sind aktiv. Spätere Bindungen bleiben gespeichert und werden erst bei erhöhter Anzahl wieder abgefragt. |
| Statusmeldung | Ausblendbar. Optionale separate Entität, sonst `state_message` bzw. `state_reason` der Druckerentität. |
| Zusatzwerte | Optionale Entitäten für Leistung und Seitenzähler. |
| Farben und Größe | Hintergrund-, Schrift- und Druckstatusfarbe. Standard **480 × 440 px**, Mindestgröße **240 × 280 px**. |

Die Anzahl bestimmt die Verteilung; es sind keine manuellen X-Positionen je Patrone nötig. Bei knappem Platz werden lange Namen gekürzt. Vollständige Namen und Werte stehen im Tooltip. Die sechs Eigenschaftsgruppen bleiben verfügbar, damit sich weitere Patronen vorbereiten lassen.

## Status und Messwerte

Bereit, Drucken, Ruhezustand, Hinweis, Gestoppt, Offline und unbekannt werden aus gängigen Statuswerten erkannt. Beim Drucken bewegt sich ein Blatt und die LED blinkt. Die Browseroption für reduzierte Bewegung schaltet diese Animationen ab. Fehler und Papierstau haben Vorrang; eine reine Füllstandswarnung beendet die Druckanimation nicht.

Editor und Runtime lesen dieselben aktuellen Home-Assistant-Werte. Fehlende oder ungültige Füllstände erscheinen als **—**, nicht als 0 %. Gültige Zahlen werden auf **0–100 %** begrenzt. Bei Werten kleiner oder gleich der Warnschwelle werden die betreffende Patrone und ihr Wert markiert; darunter erscheinen die betroffenen Namen.

## Umfang dieser Version

Diese erste Version verwendet ausdrücklich ausgewählte Entitäten. Sie bietet keine automatische Geräte-/Patronensuche, Verschleißteile, Steckdosensteuerung, Testdruck oder Drucker-Weblinks. Alle Anbindungen sind lesend. Die separat nutzbare Originalkarte bietet weitere Funktionen.
