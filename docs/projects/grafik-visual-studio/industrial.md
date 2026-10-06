---
title: UGSo Industrie – Widgets
description: Installation und Einstellungen des externen Industriepakets für Grafik Visual Studio.
---

# UGSo Industrie – Widgets

Das externe Widget-Paket **UGSo Industrie 0.2.0** enthält **Gauge/Poti – 270°** und **Kippschalter – 1 bis 4**. Industriestyle ergänzt Gehäuse, Schraubenköpfe und Rahmen. Für alle hier beschriebenen Einstellungen einschließlich des Kippschalters wird **Studio 0.1.232 oder neuer** benötigt.

## Bilder

| Poti mit Strichskala | Gauge mit Farbring |
| --- | --- |
| ![Industrie-Poti mit Strichskala und Wertanzeige unten](/images/grafik-visual-studio/industrial-poti.png) | ![Industrie-Gauge mit Farbring und Solarleistung in der Mitte](/images/grafik-visual-studio/industrial-solar-gauge.png) |
| Ohne Eingang: virtueller Drehregler mit negativem Skalenminimum und **15 °C** unterhalb des Knopfes. | Mit Eingang: **823 W** Solarleistung auf einer Skala von 0–1000 W, farbige Bereiche und mittige Wertanzeige. |

Die Bilder zeigen die Runtime mit Beispieldaten, keine Live-Messungen.

## Installation

[Paketdatei herunterladen](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/master/ha_grafik_visual_studio/packages/industrial/ugso.industrial.wg) und unter **Einstellungen → Widget-Pakete → Lokal** installieren. Das Paket ist optional, verwendet API 0.2 und enthält keinen ausführbaren Paketcode. Das aktuelle Paket 0.2.0 benötigt Studio 0.1.232 für den Kippschalter. Wer weiterhin nur Gauge/Poti nutzt, kann das bisherige Paket 0.1.0 behalten; dessen Grundfunktion benötigt Studio 0.1.223 und neuere Feineinstellungen kommen durch Studio-Updates hinzu.

[Quellcode und Paket-Anleitung auf GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/industrial)

## Daten und Bedienung

Die folgenden Abschnitte zu Skala und Wertanzeige beschreiben Gauge/Poti. Der Kippschalter hat einen eigenen Abschnitt am Ende der Seite.

- **Ohne Eingang:** Poti-Bedienung in der Runtime per Maus, Touch oder Tastatur. Startwert und Bedien-Schrittweite sind einstellbar.
- **Mit Eingangs-Entität oder Koppelpunkt:** Gauge-Anzeige. Ein aktivierter Koppelpunkt hat Vorrang vor der Entität. Ein fehlender Eingang wird als fehlender Messwert angezeigt.
- **Ausgang:** `number.*` oder `input_number.*`, beim Loslassen oder während des Ziehens. Geänderte Gauge-Werte werden ebenfalls weitergegeben. Die Entität muss verfügbar und schreibbar sein; Ein- und Ausgangsentität dürfen nicht identisch sein.
- **Wert-Lines:** Sichtbare und optisch unsichtbare Verbindungen nutzen den vorhandenen Datenfluss.

Im Editor sind Bedienung und Schreibaktionen gesperrt; zum Steuern die Runtime öffnen.

## Skala und Farbbereiche

Wählbar sind **Strichskala** mit hervorgehobener Null und **Farbring**. Minimum, Maximum, Skalenteilung und unabhängige Bedien-Schrittweite sind einstellbar; negative Grenzen sind möglich.

Farbbereiche verwenden aufsteigende **Bis-Werte** innerhalb der Skala. Die letzte Farbe endet am Maximum. Für eine Solarleistung von 0 bis 1000 W können vier Bereiche beispielsweise bei **250 / 500 / 750 / 1000** enden. Nach Änderungen der Skalenlimits müssen die Farbgrenzen angepasst werden. Ungültige Grenzen unterdrücken einen geladenen Messwert nicht; eine Warnung bleibt im Tooltip.

## Wertanzeige

Der eigene Eigenschaftenbereich **Wertanzeige** enthält:

| Einstellung | Wirkung |
| --- | --- |
| Wert anzeigen | Messwert und Einheit im Instrument anzeigen. |
| Einheit | Eigene Einheit, etwa W. Leer übernimmt `unit_of_measurement` der Home-Assistant-Eingangsentity. |
| Position des Wertes | **Mitte** oder **Unten**; unten liegt unterhalb des Poti-Knopfes. |
| Schriftgröße (px) | Standard 12 px; bleibt beim Ändern der Widget-Größe konstant. |
| Schriftfarbe | Einstellbare Farbe, standardmäßig hell. |

Die Wert-/Einheitenanzeige wurde mit Studio 0.1.227 ergänzt, die eigenen Anzeige-Einstellungen mit 0.1.228.

## Gehäuse und Farben

Ab Studio **0.1.231** steht direkt unter **Industriestyle** die Checkbox **Schrauben aktivieren**. Schrauben sind standardmäßig eingeschaltet und lassen sich bei aktivem Industriestyle separat ausschalten. Erneutes Einschalten von Industriestyle aktiviert auch die Schrauben wieder. Ohne Industriestyle sind keine Schrauben sichtbar und die Checkbox ist deaktiviert.

**Industriestyle** ergänzt vier Schraubenköpfe, den Gehäusehintergrund und den Rahmen. Skalen- und Zeigerfarbe sind getrennt einstellbar. **CSS Allgemein → Eckenradius (px)** steuert die Rahmenrundung.

Ab Studio 0.1.230 gilt für **Rahmenbreite anpassen**:

- **Ohne Haken:** bisherige Rahmenbreite von 2 px.
- **Mit Haken:** eigene **Rahmenbreite (px)** von 1 bis 16 px einstellen.
- Der eigene Wert bleibt beim Abschalten gespeichert; der Rahmen bleibt sichtbar.

**Rahmenfarbe** ist separat wählbar. Bei ausgeschaltetem Industriestyle wird kein Gehäuserahmen angezeigt.

## Größe

Das Widget beginnt bei **64 × 64 px**. Die seit Studio 0.1.226 standardmäßig aktivierte Checkbox **Verhältnis 1:1** hält Breite und Höhe beim Eingeben und Ziehen gleich. Ohne Haken sind die Maße unabhängig, jeweils mindestens 64 px. Erneutes Aktivieren übernimmt das größere Maß für beide Seiten.

## Gehäuse-Snappunkte

Seit Studio 0.1.224 bietet **Gehäuse-Snappunkte** vier einzeln aktivierbare Ecken und einen gemeinsamen Abstand für alle Seiten. Bei je 1 px entsteht eine 2-px-Fuge; einzelne Widgets rasten beim Verschieben ein.

Die Farbe liegt unter **Einstellungen → Allgemein → Editor und Andockpunkte → Farbe der Gehäuse-Snappunkte**. Signalanschlüsse bleiben getrennt. Automatische Anschlussverlegung an freie Gehäuseseiten folgt später.

## Kippschalter – 1 bis 4

Ab Paket **0.2.0** und Studio **0.1.232** stehen ein bis vier unabhängig bedienbare Schalter nebeneinander zur Verfügung. **Anzahl Schalter** legt das Verhältnis Breite/Höhe von **1:1 bis 4:1** fest. Minimum sind 64 px Höhe und 64 px Breite je Kanal; die Maße bleiben beim Eingeben und Ziehen proportional.

![Vier Industrie-Kippschalter mit kleinen LEDs und drei Schildvarianten](/images/grafik-visual-studio/industrial-switches.png)

*Runtime mit Beispieldaten: eigene Beschriftungen, grüne LEDs und Schilder ON/OFF, 1/0 und EIN/AUS. Ab Studio 0.1.233 stammt der Metallhebel aus der von rockbaer2007 bereitgestellten transparenten PNG und ist in beiden Stellungen vollständig sichtbar. Die LED bleibt eine CSS-Zeichnung. Das Studio-Update genügt; Paket 0.2.0 muss nicht erneut installiert werden.*

Jeder Bereich **Schalter 1** bis **Schalter 4** enthält eine feste **Beschriftung**, **Schildbeschriftung** mit **ON/OFF**, **1/0** oder **EIN/AUS**, Startzustand und eigene LED-Farben für Ein und Aus. Die LED liegt oberhalb der Beschriftung; die Schildtexte ändern sich nicht durch Entitäten. Schriftgröße und Schriftfarbe stehen unter **Beschriftung**.

| Anschluss je Kanal | Verhalten |
| --- | --- |
| Eingang: Entität | Zustand für Hebel und LED. Ohne Eingang wird eine konfigurierte Ausgangsentität als Rückmeldung verwendet. |
| Eingangs-Koppelpunkt | Oben in der jeweiligen Schalterspalte, einzeln aktivierbar; hat Vorrang vor der Entität. |
| Ausgang: Entität | Schaltet `switch.*`, `light.*` oder `input_boolean.*`. Ohne getrennten Ausgang wird eine geeignete Eingangsentity geschaltet. |
| Ausgangs-Koppelpunkt | Unten in der jeweiligen Schalterspalte, einzeln aktivierbar. Liefert den letzten Bedienbefehl als booleschen Wert; vor der ersten Bedienung den aktuellen Zustand. |

Ohne Bindung arbeitet der Schalter lokal. Fehlende Rückmeldung sperrt die Bedienung. Im Editor werden keine Befehle gesendet. Gehäuse-, Schrauben-, Rahmen- und Gehäuse-Snappunkt-Einstellungen gelten auch für dieses Widget. Für den neuen Kippschalter das Paket lokal auf **0.2.0 aktualisieren**; die bestehenden Gauge/Poti-Definitionen bleiben erhalten.
