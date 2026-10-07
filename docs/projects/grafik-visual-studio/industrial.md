---
title: UGSo Industrie – Widgets
description: Installation und Einstellungen des externen Industriepakets für Grafik Visual Studio.
---

# UGSo Industrie – Widgets

Das externe Widget-Paket **UGSo Industrie 0.4.0** enthält **Gauge/Poti – 270°**, **Kippschalter – 1 bis 4**, **Wippschalter – 1 bis 4**, **LCD – 20×4** und **LCD – 16×2**. Industriestyle ergänzt Gehäuse, Schraubenköpfe und Rahmen. Für die neuen LCDs wird **Studio 0.1.238 oder neuer** benötigt.

## Bilder

| Poti mit Strichskala | Gauge mit Farbring |
| --- | --- |
| ![Industrie-Poti mit Strichskala und Wertanzeige unten](/images/grafik-visual-studio/industrial-poti.png) | ![Industrie-Gauge mit Farbring und Solarleistung in der Mitte](/images/grafik-visual-studio/industrial-solar-gauge.png) |
| Ohne Eingang: virtueller Drehregler mit negativem Skalenminimum und **15 °C** unterhalb des Knopfes. | Mit Eingang: **823 W** Solarleistung auf einer Skala von 0–1000 W, farbige Bereiche und mittige Wertanzeige. |

Die Bilder zeigen die Runtime mit Beispieldaten, keine Live-Messungen.

## Installation

[Paketdatei herunterladen](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/master/ha_grafik_visual_studio/packages/industrial/ugso.industrial.wg) und unter **Einstellungen → Widget-Pakete → Lokal** installieren. Zuerst Studio auf **0.1.238 oder neuer** aktualisieren, danach Paket **0.4.0** installieren. Das Paket ist optional, verwendet API 0.2 und enthält keinen ausführbaren Paketcode. Bestehende Gauge/Poti-, Kippschalter- und Wippschalter-Definitionen bleiben beim Update erhalten.

[Quellcode und Paket-Anleitung auf GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/industrial)

## LCD – 20×4 und 16×2

Die Displays imitieren eine **5×8-Punktmatrix-Schrift** mit schwarzem Bildschirmrand. Die Schrift wird dynamisch aus Bildpunkten aufgebaut und ist Bestandteil von Studio; eine externe Schriftinstallation ist nicht erforderlich. Groß- und Kleinbuchstaben, Zahlen, Satzzeichen, Umlaute, ß, €, °, µ, Ω, Pfeile und ✓ sind enthalten. Nicht unterstützte Zeichen erscheinen als `?`.

| 20×4 Gelb/Weiß | 20×4 Blau/Weiß |
| --- | --- |
| ![LCD mit gelbem Hintergrund und weißer Punktmatrix-Schrift](/images/grafik-visual-studio/industrial-lcd-yellow.png) | ![LCD mit blauem Hintergrund und weißer Punktmatrix-Schrift](/images/grafik-visual-studio/industrial-lcd-blue.png) |

| 16×2 Blau/Weiß | Display ausgeschaltet |
| --- | --- |
| ![LCD mit 16 Zeichen je Zeile und zwei Zeilen](/images/grafik-visual-studio/industrial-lcd-small.png) | ![Ausgeschaltetes LCD mit sichtbarem Industriegehäuse](/images/grafik-visual-studio/industrial-lcd-off.png) |

Die Bilder zeigen Beispieldaten. **Beide Größen bieten Gelb/Weiß und Blau/Weiß.** Das feste Verhältnis wird beim Eingeben und Ziehen beibehalten: 20×4 startet bei **192×64 px** (Höhe/Breite **1:3**), 16×2 bei **192×32 px** (**0,5:3**, halbe Rasterhöhe). Größere Darstellungen skalieren den Bildschirm und die Zeichen gemeinsam.

### Zeilen und Entitäten

Jede der vier beziehungsweise zwei Zeilen hat **eine eigene Entität** mit Entitätsauswahl. **Text / Präfix** steht vor dem Entitätswert; ohne Entität bildet dieses Feld den gesamten festen Zeileninhalt. Beispiel: `Temp: ` + Sensorwert `-20.24` + automatische Einheit `°C` ergibt mit einer Nachkommastelle `Temp: -20.2 °C`.

**Einheit aus Entität** übernimmt `unit_of_measurement` aus Home Assistant. Eine eingetragene Einheit hat Vorrang. **Nachkommastellen** unterstützt `auto` oder 0–6 Stellen für Zahlen; Textzustände bleiben Text. Fehlende oder nicht verfügbare Entitätswerte erscheinen als `?`. Lange Texte werden nach 20 beziehungsweise 16 Zeichen abgeschnitten; der Tooltip enthält die vollständigen Zeilen. Es gibt keinen Zeilenumbruch und keine eigenen Daten-Koppelpunkte für die Zeilen.

### Display Ein/Aus und Gehäuse

Ohne Bindung gilt **Ohne Eingang eingeschaltet**. **Display Ein/Aus: Entität** kann beispielsweise eine `switch`- oder `input_boolean`-Entität sein. Alternativ **Ein/Aus-Koppelpunkt aktivieren**: Ein einzelner Eingang oben mittig (`display-power`) übernimmt `on/off`, `true/false` oder `1/0`. Verbinde einen Kippschalter- oder Wippschalter-Ausgang über eine sichtbare oder unsichtbare Wert-Verbindung mit diesem Eingang.

Der aktivierte Koppelpunkt hat Vorrang vor der Entität. Ohne gültigen Eingang bleibt der Bildschirm dunkel; ein ausgeschaltetes Display zeigt keine Schrift, das Gehäuse bleibt sichtbar. Das LCD liest Zustände und sendet keine Schaltbefehle. Es besitzt **keinen Ausgang**.

Unter **Gehäuse und Farben** stehen Industriestyle, standardmäßig aktive Schrauben, Rahmenfarbe und optionale Rahmenbreite bereit. Die vier **Gehäuse-Snappunkte an den Ecken** sind einzeln aktivierbar. Abstand rundherum und die zentralen Farben für Eingangs- und Gehäusepunkte gelten wie bei den anderen Industriewidgets. Schriftgröße folgt dem festen Raster; die Schriftfarbe bleibt im gewählten Farbmodus Weiß.

## Wippschalter – 1 bis 4

Ab **Studio 0.1.237** gilt auch beim Wippschalter: **Breite = Höhe × Schalteranzahl + 2 × Abstand rundherum × (Schalteranzahl − 1)**. Bei 64 px Höhe und 1 px Abstand sind die Breiten **64 / 130 / 196 / 262 px**. Schaltermitten und E/A-Anschlüsse fluchten mit einzeln angedockten Widgets. Eingabe und Ziehen berücksichtigen den Abstand. Ein Studio-Update genügt; Paket 0.3.0 bleibt unverändert.

Ab Paket **0.3.0** und Studio **0.1.235** ist der Wippschalter eine Kopie des Kippschalters mit transparenten PNG-Grafiken. Unter **Schalter 1** bis **Schalter 4 → Schalterfarbe** wird **Weiß/Grau**, **Rot**, **Schwarz** oder **Grün** je Kanal gewählt. Ein Widget kann unterschiedliche Farben kombinieren; die Grafik wechselt mit dem Ein-/Aus-Zustand.

![Vier Wippschalter mit unabhängig gewählten Farben](/images/grafik-visual-studio/industrial-rockers.png)

Alle Kippschalter-Eigenschaften gelten auch hier: Beschriftung, zusätzliche Schilder ON/OFF, 1/0 oder EIN/AUS, LED-Farben, Entitäten, E1–E4/A1–A4, sechs Gehäuse-Snappunkte, Schrauben, Rahmen und Abstand. Das aufgedruckte O/I bleibt Bestandteil der Grafik. Größe 1:1 bis 4:1, mindestens 64 px je Kanal. Bedienung erfolgt nur in der Runtime.

## Gauge/Poti: Daten und Bedienung

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

Ab **Studio 0.1.236** wird beim Kippschalter der Zwischenabstand in die Blockbreite eingerechnet: **Höhe × Schalteranzahl + 2 × Abstand rundherum × (Schalteranzahl − 1)**. Bei 64 px Höhe und 1 px Abstand rundherum sind die Breiten **64 / 130 / 196 / 262 px**. Schaltermitten sowie E/A-Anschlüsse fluchten damit mit einzelnen Widgets darunter. Eingabe und Ziehen berücksichtigen den Zuschlag. Diese Anpassung gilt zunächst nur für den Kippschalter; Wippschalter bleiben unverändert. Ein Studio-Update genügt, Paket 0.3.0 bleibt unverändert.

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

### Anschlüsse E1–E4 und A1–A4

Ab **Studio 0.1.234** heißen die Signalpunkte im Editor **E1–E4** (Eingang oberhalb des jeweiligen Schalters) und **A1–A4** (Ausgang unterhalb). Bei weniger Schaltern erscheinen nur deren Anschlüsse. Die Punkte sind je Schalter einzeln aktivierbar; Eingangs- und Ausgangsfarbe kommen aus den zentralen Editor-Einstellungen. Bestehende Verbindungen bleiben erhalten.

Unter **Gehäuse-Snappunkte** besitzt der Kippschalter sechs getrennte, einzeln aktivierbare Punkte: vier Ecken sowie **Links Mitte** und **Rechts Mitte**. Zusammen mit den Signalanschlüssen sind damit **8 / 10 / 12 / 14 Punkte** für ein bis vier Schalter verfügbar. Gehäusepunkte dienen dem Einrasten mit dem eingestellten Abstand und verwenden die Gehäuse-Snappunktfarbe; sie übertragen keine Schaltwerte. Punkte und Anschlussbeschriftungen erscheinen nur im Editor. Ein Studio-Update genügt; Paket **0.2.0** bleibt unverändert.
