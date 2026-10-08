---
title: UGSo Calendar +
description: Eigenes Kalender-Widgetset mit automatischer Kalendererkennung, Terminliste und Detail-Popup.
---

# UGSo Calendar +

**UGSo Calendar + 0.1.1** ist ein eigenes externes Widgetset von **rockbaer2007** für **Grafik Visual Studio 0.1.267 oder neuer**. Es erkennt alle verfügbaren Home-Assistant-Kalender automatisch und zeigt kommende Termine als kompakte Karte oder ausgeklappte Liste. Alle Kalender sind zunächst aktiviert.

Die Runtime mit Beispieldaten:

![UGSo Calendar + mit farbigen Kalenderkacheln, Tagesgruppen und Terminliste](/images/grafik-visual-studio/calendar-plus.png)

## Originalprojekt

Vorbild ist **[calendar-card-plus von xBourner](https://github.com/xBourner/calendar-card-plus)**, veröffentlicht unter der [MIT-Lizenz](https://github.com/xBourner/calendar-card-plus/blob/main/LICENSE), Copyright (c) 2026 xBourner. UGSo Calendar + verwendet eine eigene Studio-Implementierung und ein eigenes Palettensymbol. Originalcode und Originalgrafiken sind nicht eingebunden. Das Set ist unabhängig von Industrial und der separat nutzbaren Lovelace-Originalkarte.

## Installieren

1. Studio auf **0.1.267 oder neuer** aktualisieren.
2. [ugso.calendar-plus.wg herunterladen](https://raw.githubusercontent.com/rockbaer2007/ugso-ha-mqtt-addons/master/ha_grafik_visual_studio/packages/calendar-plus/ugso.calendar-plus.wg).
3. Unter **Einstellungen → Widget-Pakete → Lokal** installieren.
4. **UGSo Calendar + → Kalender +** aus der Palette auf die Seite ziehen.

Das Paket enthält deklarative Daten, ein Symbol, Anleitung und MIT-Lizenz. Der feste Host-Renderer `calendar-plus` wird von Studio bereitgestellt; keine ausführbaren Paketskripte. [Quellcode und Paket-Anleitung](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/calendar-plus).

## Meine Kalender

Alle verfügbaren `calendar.*`-Entitäten werden erkannt, einschließlich Kalendern ohne Registry-Eintrag. In Home Assistant deaktivierte Registry-Einträge werden ausgelassen. Unter **Meine Kalender** erscheint für jeden Kalender ein eigener Bereich mit Entitäts-ID, einer **Checkbox rechts oben zum Anzeigen/Ausblenden**, **Farbe** und optionaler **Hintergrundfarbe**. Es gibt keine manuell einzutragende Kalenderanzahl.

Ab Studio **0.1.268** heißt die Gruppe **Kacheleinstellungen** (zuvor „Farben“). **Kalenderkachelgröße** bietet vier feste Größen: **Sehr klein 36 × 44 px**, **Klein 44 × 52 px**, **Mittel 58 × 64 px** (Standard) und **Groß 76 × 82 px**. Die Auswahl gilt für Terminliste und Detail-Popup. Kopftext mindestens **12 px**, Tagesziffer mindestens **24 px**, unabhängig von der allgemeinen Schriftgröße. Auch schmale Widgets behalten die gewählte Größe. Vorhandene Pakete 0.1.0/0.1.1 erhalten die Einstellungen mit dem Studio-Update; eine Neuinstallation ist nicht nötig. Der Kalender benötigt keine Datenfluss-Einstellungen oder Ein-/Ausgangspunkte.

Die Auswahl und Farben bleiben anhand der Entitäts-ID gespeichert. Neu hinzugekommene Kalender sind automatisch eingeblendet; ausgeblendete Kalender werden nicht nach Terminen abgefragt. Die Anzahl erkannter Kalender ist nicht begrenzt. Abfragen erfolgen in Gruppen von höchstens 20 Kalendern über die Home-Assistant-Schnittstelle.

## Einstellungen

Ab Studio **0.1.269** bieten die **Kacheleinstellungen** zusätzlich **Schriftgröße oben** (Monat/Wochentag, bis 72 px) und **Schriftgröße unten** (Tageszahl, bis 120 px). **0 = automatisch** verwendet die Vorgaben der gewählten Kachelgröße. Eigene Werte dürfen kleiner sein und werden bei Platzmangel automatisch begrenzt. Die gespeicherten Wunschwerte bleiben erhalten, sodass größere Kacheln wieder größere Schrift nutzen können.

Der farbige Kopfbereich wächst mit der oberen Schrift und etwas Innenabstand, bleibt jedoch auf **höchstens ein Drittel der Kachelhöhe** begrenzt. Die Tageszahl wird in den restlichen Bereich eingepasst. Die Kachelgröße bleibt unverändert. Diese Einstellungen gelten für Terminliste und Detail-Popup und benötigen kein neues Widget-Paket.

| Bereich | Einstellung |
| --- | --- |
| Konfiguration | Bezeichnung, Vorschau **1–90 Tage**, **1–20** sichtbare Termine, Ereignisse ausklappen, Detail-Popup, Trenner. |
| Gruppierung | Nach Tag, zusätzlich nach Kalender; optional leere Tage anzeigen. |
| Bevorstehende Ereignisse | Relative Zeit wie „Morgen“, „In 2 Tagen“ oder „Läuft“ ein-/ausblenden. |
| Text & Sichtbarkeit | Kalendername, Datum, Ort, Dauer, Uhrzeit und Wochentag einzeln schaltbar; Wochentag ausgeschrieben oder kurz, Monat/Wochentag in der Datumskachel tauschen. |
| Kacheleinstellungen | Vier Kachelgrößen, Browser-Theme automatisch oder fest Hell/Dunkel, Akzentfarbe und Schriftgröße **10–24 px**. Kalenderfarben und Hintergründe separat je Kalender. |
| Größe | Vorgabe **480 × 460 px**, mindestens **260 × 180 px**; bei wenig Platz scrollt die Terminliste. |

Ohne ausgeklappte Liste bleibt ein Termin sichtbar. In der Runtime öffnet ein Klick auf einen Termin oder **Alle Termine** das Detail-Popup mit bis zu 100 Terminen. Dort erscheinen vollständiges Datum, Ort und Beschreibung, sofern vorhanden. Texte werden als Klartext dargestellt. **Schließen**, Escape oder ein Klick außerhalb schließen das Popup.

## Daten und Aktualisierung

Editor und Runtime lesen Termine über `calendar.get_events`. Ganztagstermine berücksichtigen das exklusive Enddatum; abgelaufene Termine werden entfernt. Unter **Konfiguration → Automatisch aktualisieren (60 s)** lässt sich die regelmäßige Aktualisierung abschalten (Vorgabe: an). Beim Runtime-Seitenaufruf werden Kalender und Termine frisch geladen, auch bei deaktivierter Automatik. **↻** aktualisiert weiterhin manuell. Die Kalendererkennung wird dabei ebenfalls erneuert.

Aktualisierungen ersetzen nur die Terminlisten und erhalten Scrollpositionen sowie ein geöffnetes Detail-Popup. Zustandsänderungen anderer Live-Widgets bauen den unveränderten Kalender nicht neu auf. Beim Verlassen der Seite endet dessen Aktualisierung.

„Keine Kalender gefunden“, „Alle Kalender ausgeblendet“, „Keine kommenden Termine“ und ein Ladefehler sind unterschiedliche Zustände. Ein Fehler wird nicht als leerer Kalender ausgegeben. Die Sprache folgt automatisch der Studio-Einstellung **DE/EN**; eigene Bezeichnungen und Termininhalte bleiben unverändert.

## Umfang dieser Version

Diese Version liest Termine. **Neuer Termin**, Bearbeiten und Löschen sind noch nicht enthalten. Kalender müssen in Home Assistant verfügbar sein; es gibt keine direkte ICS-/Google-Anmeldung. Die Originalkarte muss nicht zusätzlich in HACS installiert werden.
