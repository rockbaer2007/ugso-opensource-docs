---
title: UGSo Calendar +
description: Eigenes Kalender-Widgetset mit automatischer Kalendererkennung, Terminliste und Detail-Popup.
---

# UGSo Calendar +

**UGSo Calendar + 0.1.0** ist ein eigenes externes Widgetset von **rockbaer2007** für **Grafik Visual Studio 0.1.266 oder neuer**. Es erkennt alle verfügbaren Home-Assistant-Kalender automatisch und zeigt kommende Termine als kompakte Karte oder ausgeklappte Liste. Alle Kalender sind zunächst aktiviert.

Die Runtime mit Beispieldaten:

![UGSo Calendar + mit farbigen Kalenderkacheln, Tagesgruppen und Terminliste](/images/grafik-visual-studio/calendar-plus.png)

## Originalprojekt

Vorbild ist **[calendar-card-plus von xBourner](https://github.com/xBourner/calendar-card-plus)**, veröffentlicht unter der [MIT-Lizenz](https://github.com/xBourner/calendar-card-plus/blob/main/LICENSE), Copyright (c) 2026 xBourner. UGSo Calendar + verwendet eine eigene Studio-Implementierung und ein eigenes Palettensymbol. Originalcode und Originalgrafiken sind nicht eingebunden. Das Set ist unabhängig von Industrial und der separat nutzbaren Lovelace-Originalkarte.

## Installieren

1. Studio auf **0.1.266 oder neuer** aktualisieren.
2. [ugso.calendar-plus.wg herunterladen](https://raw.githubusercontent.com/rockbaer2007/ugso-ha-mqtt-addons/master/ha_grafik_visual_studio/packages/calendar-plus/ugso.calendar-plus.wg).
3. Unter **Einstellungen → Widget-Pakete → Lokal** installieren.
4. **UGSo Calendar + → Kalender +** aus der Palette auf die Seite ziehen.

Das Paket enthält deklarative Daten, ein Symbol, Anleitung und MIT-Lizenz. Der feste Host-Renderer `calendar-plus` wird von Studio bereitgestellt; keine ausführbaren Paketskripte. [Quellcode und Paket-Anleitung](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/calendar-plus).

## Meine Kalender

Alle verfügbaren `calendar.*`-Entitäten werden erkannt, einschließlich Kalendern ohne Registry-Eintrag. In Home Assistant deaktivierte Registry-Einträge werden ausgelassen. Unter **Meine Kalender** erscheint für jeden Kalender ein eigener Bereich mit Entitäts-ID, **Einblenden/Ausblenden**, **Farbe** und optionaler **Hintergrundfarbe**. Es gibt keine manuell einzutragende Kalenderanzahl.

Die Auswahl und Farben bleiben anhand der Entitäts-ID gespeichert. Neu hinzugekommene Kalender sind automatisch eingeblendet; ausgeblendete Kalender werden nicht nach Terminen abgefragt. Die Anzahl erkannter Kalender ist nicht begrenzt. Abfragen erfolgen in Gruppen von höchstens 20 Kalendern über die Home-Assistant-Schnittstelle.

## Einstellungen

| Bereich | Einstellung |
| --- | --- |
| Konfiguration | Bezeichnung, Vorschau **1–90 Tage**, **1–20** sichtbare Termine, Ereignisse ausklappen, Detail-Popup, Trenner. |
| Gruppierung | Nach Tag, zusätzlich nach Kalender; optional leere Tage anzeigen. |
| Bevorstehende Ereignisse | Relative Zeit wie „Morgen“, „In 2 Tagen“ oder „Läuft“ ein-/ausblenden. |
| Text & Sichtbarkeit | Kalendername, Datum, Ort, Dauer, Uhrzeit und Wochentag einzeln schaltbar; Wochentag ausgeschrieben oder kurz, Monat/Wochentag in der Datumskachel tauschen. |
| Farben | Browser-Theme automatisch oder fest Hell/Dunkel, Akzentfarbe und Schriftgröße **10–24 px**. Kalenderfarben und Hintergründe separat je Kalender. |
| Größe | Vorgabe **480 × 460 px**, mindestens **260 × 180 px**; bei wenig Platz scrollt die Terminliste. |

Ohne ausgeklappte Liste bleibt ein Termin sichtbar. In der Runtime öffnet ein Klick auf einen Termin oder **Alle Termine** das Detail-Popup mit bis zu 100 Terminen. Dort erscheinen vollständiges Datum, Ort und Beschreibung, sofern vorhanden. Texte werden als Klartext dargestellt. **Schließen**, Escape oder ein Klick außerhalb schließen das Popup.

## Daten und Aktualisierung

Editor und Runtime lesen Termine über `calendar.get_events`. Ganztagstermine berücksichtigen das exklusive Enddatum; abgelaufene Termine werden entfernt. Die Aktualisierung erfolgt alle 60 Sekunden bei sichtbarer Seite sowie über **↻** in der Runtime. Die Kalendererkennung wird dabei ebenfalls erneuert.

„Keine Kalender gefunden“, „Alle Kalender ausgeblendet“, „Keine kommenden Termine“ und ein Ladefehler sind unterschiedliche Zustände. Ein Fehler wird nicht als leerer Kalender ausgegeben. Die Sprache folgt automatisch der Studio-Einstellung **DE/EN**; eigene Bezeichnungen und Termininhalte bleiben unverändert.

## Umfang dieser Version

Diese Version liest Termine. **Neuer Termin**, Bearbeiten und Löschen sind noch nicht enthalten. Kalender müssen in Home Assistant verfügbar sein; es gibt keine direkte ICS-/Google-Anmeldung. Die Originalkarte muss nicht zusätzlich in HACS installiert werden.
