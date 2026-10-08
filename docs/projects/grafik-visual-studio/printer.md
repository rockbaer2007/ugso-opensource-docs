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

Die Anzahl bestimmt die Verteilung; es sind keine manuellen X-Positionen je Patrone nötig. Bei knappem Platz werden lange Namen gekürzt. Vollständige Namen und Werte stehen im Tooltip. Ab **Studio 0.1.263** erscheinen nur die gewählten Patronen in den Eigenschaften: bei 4 die Gruppen **Patrone 1–4**, bei 5 **Patrone 1–5**. Einstellungen ausgeblendeter Patronen bleiben gespeichert und erscheinen wieder, wenn die Anzahl erhöht wird.

## Eigenes Druckerfoto und Patronengröße

Ab **Studio 0.1.262** stehen unter **Druckermodell und Bild** zusätzlich eine freie Modellbezeichnung, die Auswahl **Standardgrafik / Eigenes Bild** und **Foto Ihres Druckers (URL oder /local/... Pfad)** bereit. Das Eintragen eines Bildpfads aktiviert das eigene Foto automatisch; auch Bild-URLs ohne Dateiendung werden unterstützt. Alternativ lädt **Bild hochladen** eine PNG-, JPEG-, WebP-, GIF- oder SVG-Datei bis 2 MB direkt ins Projekt. Hochgeladene Bilder sind im gespeicherten Projekt enthalten. Bei URLs und `/local/...`-Pfaden muss die Bildquelle auch in der Runtime erreichbar sein.

Das Foto wird proportional eingepasst. Bei fehlendem Bild oder Ladefehler erscheint die Standardgrafik. Status und Patronen bleiben unabhängig vom Foto aktiv; die Blattanimation gehört zur Standardgrafik. **Patronengröße** bietet **Volle Größe / Halbe Größe**, mit **Halbe Größe** als Vorgabe. Nur die Grafiken werden verkleinert, Beschriftungen und Prozentwerte behalten ihre Größe. Diese Einstellungen erscheinen auch bei bereits installiertem Printer-Paket; eine Neuinstallation des Pakets ist nicht nötig.

## Status und Messwerte

Die Sprache folgt automatisch der Studio-Einstellung **DE/EN**, einschließlich automatischer Übernahme aus Home Assistant. Eine separate Widget-Sprachauswahl gibt es nicht. Status, Hinweise und Eigenschaften werden übersetzt; eigene Beschriftungen, Modellnamen und Meldungen der Entität bleiben unverändert.

Bereit, Drucken, Ruhezustand, Hinweis, Gestoppt, Offline und unbekannt werden aus gängigen Statuswerten erkannt. Beim Drucken bewegt sich ein Blatt und die LED blinkt. Die Browseroption für reduzierte Bewegung schaltet diese Animationen ab. Fehler und Papierstau haben Vorrang; eine reine Füllstandswarnung beendet die Druckanimation nicht.

Editor und Runtime lesen dieselben aktuellen Home-Assistant-Werte. Fehlende oder ungültige Füllstände erscheinen als **—**, nicht als 0 %. Gültige Zahlen werden auf **0–100 %** begrenzt. Bei Werten kleiner oder gleich der Warnschwelle werden die betreffende Patrone und ihr Wert markiert; darunter erscheinen die betroffenen Namen.

## Weboberfläche

**URL der Weboberfläche (auto = vom Drucker)** blendet einen **Web ↗**-Link ein. Eine manuell eingetragene URL hat Vorrang. `auto` verwendet die erste HTTP-/HTTPS-Adresse aus `configuration_url`, `web_url`, `url`, `device_url` oder `printer_uri` der Statusentität. Fehlt eine solche Adresse, bleibt der Link verborgen; es erfolgt keine Gerätesuche. Ein leeres Feld blendet ihn ebenfalls aus. Die Weboberfläche öffnet sich in einem neuen Tab.

## Umfang dieser Version

Diese erste Version verwendet ausdrücklich ausgewählte Entitäten. Sie bietet keine automatische Geräte-/Patronensuche, Verschleißteile, Steckdosensteuerung oder Testdruck. Alle Anbindungen sind lesend. Die separat nutzbare Originalkarte bietet weitere Funktionen.
