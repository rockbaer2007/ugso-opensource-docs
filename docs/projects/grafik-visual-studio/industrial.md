---
title: UGSo Industrie – Widgets
description: Installation und Einstellungen des externen Industriepakets für Grafik Visual Studio.
---

# UGSo Industrie – Widgets

Das externe Widget-Paket **UGSo Industrie 0.11.6** enthält sechzehn Widgets: **Gauge/Poti – 270°**, **Kippschalter – 1 bis 4**, **Wippschalter – 1 bis 4**, **LCD – 20×4**, **LCD – 16×2**, **Linear-Gauge / Schieberegler** und **Zählwerk** in normaler und schmaler Ausführung, **7-Segment – LED**, **16-Segment – LED**, **16-Segment – LCD**, **Industrie-Uhr – Nixie / LED / LCD**, **Industrie-Wetter – LCD / LED**, **Blindelement** sowie **Heizung – Kessel und Öltank**. Industriestyle ergänzt Gehäuse, Schraubenköpfe und Rahmen. Das Heizungswidget mit der detaillierten Grafik benötigt **Studio 0.1.253 oder neuer**.

**Updatehinweis:** Version 0.11.4 konnte wegen geänderter Widgetbeschriftungen nicht über eine bestehende Installation installiert werden. Verwende stattdessen **0.11.5** als lokale `.wg`-Datei; sie bewahrt die veröffentlichten Widgetverträge und Entitätsbindungen. Studio **0.1.259** zeigt die Vorlauf-Einstellungen unter der neuen Bezeichnung an, ohne gespeicherte Gruppenschlüssel zu ändern.

## Bilder

| Poti mit Strichskala | Gauge mit Farbring |
| --- | --- |
| ![Industrie-Poti mit Strichskala und Wertanzeige unten](/images/grafik-visual-studio/industrial-poti.png) | ![Industrie-Gauge mit Farbring und Solarleistung in der Mitte](/images/grafik-visual-studio/industrial-solar-gauge.png) |
| Ohne Eingang: virtueller Drehregler mit negativem Skalenminimum und **15 °C** unterhalb des Knopfes. | Mit Eingang: **823 W** Solarleistung auf einer Skala von 0–1000 W, farbige Bereiche und mittige Wertanzeige. |

Die Bilder zeigen die Runtime mit Beispieldaten, keine Live-Messungen.

## Installation

Alle Entitätsfelder des Sets besitzen eine **…**-Schaltfläche zum Öffnen der **Home-Assistant-Entitätenauswahl**. Gewünschte Entität suchen, auswählen und mit **Einfügen** in das aktive Feld übernehmen. Ab **Studio 0.1.250** gilt das auch für **Eingang: Entität** und **Ausgang: Entität** in jedem Kipp-/Wippschalterkanal. Die Auswahl wird dem jeweiligen Kanal zugeordnet. Für vorhandene Pakete genügt das Studio-Update.

[Paketdatei herunterladen](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/master/ha_grafik_visual_studio/packages/industrial/ugso.industrial.wg) und unter **Einstellungen → Widget-Pakete → Lokal** installieren. Zuerst Studio auf **0.1.253 oder neuer** aktualisieren, danach Paket **0.11.3** installieren. Für die detaillierte Grafik genügt das Studio-Update mit vorhandenem Paket 0.11.1/0.11.2. Anschließend den Browser mit **Strg+F5** neu laden. Das Paket ist optional, verwendet API 0.2 und enthält keinen ausführbaren Paketcode. Alle sechzehn bisherigen Widget-Definitionen bleiben beim Update erhalten.

[Quellcode und Paket-Anleitung auf GitHub](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/industrial)

## Heizung – Kessel und Öltank

![Detailliertes Heizungswidget mit dynamischen Temperaturen, zwei Pumpen, Brenner, Störung und Tankfüllstand](/images/grafik-visual-studio/industrial-heating.png)

Die detaillierte transparente PNG-Vorlage zeigt einen dunkelroten Heizkessel, zwei grüne Pumpen, blauen Brenner und Kupfertank nebeneinander. Temperaturen, Statusanzeigen, Warnsymbol, Tankfüllhöhe und Pfeile sind dynamische SVG-Elemente. Grafik und Anzeigen verwenden dasselbe Koordinatensystem mit den tatsächlichen Bildmaßen **1683×935** und skalieren gemeinsam. Dadurch bleiben die Anzeigen auch beim Ziehen oder Ändern der Größe am zugehörigen Bauteil.

**Breite:Höhe 7:4 Rasterfelder**, mit den additiven Gehäuseabständen: bei 1 px Abstand mindestens **460×262 px**, voreingestellt **908×518 px**. Bestehende 4:6- und 6:4-Widgets wechseln beim Öffnen in dieses Format und behalten ihre Rasterzellengröße und Entitätszuordnungen. Die Grafik wird lokal mit Studio ausgeliefert. Die Abbildung zeigt lokale Testwerte.

| Anzeige | Entität und Einstellungen |
| --- | --- |
| Vorlauftemperatur | Numerische Entität, ausblendbar, eigene Textfarbe |
| Rücklauftemperatur | Numerische Entität, ausblendbar, eigene Textfarbe; Anzeige unter dem orangefarbenen Rohr |
| Kessel-, Warmwasser-, Kaltwassertemperatur | Je eine numerische Entität und eigene Textfarbe |
| Heizkreispumpe, Zirkulationspumpe, Brenner | Je eine Boolean-Entität; Statusanzeige separat ausblendbar |
| Störung | Boolean-Entität; Warnsymbol neben Kesseltemperatur, ausblendbar |
| Tankfüllstand | Numerischer Sensor in Prozent **0–100 %**, Füllhöhe und Zahlenwert |

Alle **zehn Entitäten** besitzen die Home-Assistant-Auswahl. Boolean-Werte `on/off`, `true/false` und `1/0` werden erkannt; die sichtbare Beschriftung ist wählbar als **EIN/AUS**, **ON/OFF** oder **1/0**. Temperaturen übernehmen die Einheit der Entität und lassen sich unabhängig einfärben. Die Grundfarben entsprechen der Vorlage: rot für Temperaturen, orange für Rücklauf, blau für Kaltwasser, grün für eingeschalteten Status, gelb für Störung und rosa für Füllstand.

Ab **Studio 0.1.260** liegt der linke rote Anschluss höher. Der orange Rücklauf verläuft davor mit leichtem Knick parallel zum Anschluss am Kessel; sein Pfeil sitzt links und zeigt nach rechts zum Kessel. Unter **Rücklauf** sind Entität, Anzeige sichtbar, Textfarbe und Flusspfeil einstellbar. Bestehende Widgets erhalten die Eigenschaften durch das Studio-Update; **Industrial 0.11.6** ergänzt die Anleitung und bewahrt die Paketverträge. Vorhandene eigene Füllstandsfarben bleiben erhalten; der alte orange Standard wird einmalig rosa.

**Flusspfeile** für Vorlauf, Zirkulation, Warmwasser, Kaltwasser und die dünne kupferfarbene **Ölleitung zum Brenner** sind einzeln abschaltbar. Die rechte Pumpe befindet sich in einer senkrechten Leitung direkt vom Kessel nach oben. Warm- und Kaltwasser bleiben separate Leitungen. Der Tank-Sensor muss Prozent liefern; Liter werden nicht automatisch umgerechnet. Werte außerhalb 0–100 % begrenzen nur die Füllhöhe, der Originalwert bleibt als Zahl sichtbar.

Fehlende oder ungültige Werte zeigen einen Strich; ein unbekannter Störungszustand zeigt ein Fragezeichen. Ohne Entitäten werden keine Messwerte erfunden. **Beispieldaten ohne Entitäten** sind optional und standardmäßig ausgeschaltet. Das Widget ist eine Anzeige und sendet keine Schaltbefehle. Es besitzt nur Gehäuse-Andockpunkte; Industriestyle, Schrauben, Rahmen und angepasster Hintergrund stehen wie im übrigen Set zur Verfügung.

## Blindelement

![Leeres Industriegehäuse mit darüberliegendem Eingabefeld](/images/grafik-visual-studio/industrial-blank-panel.png)

Universelles Hintergrund-Widget als Gehäuse oder gestaltbare Fläche für Widgets aus **allen Widgetsets**. Darüber lassen sich beispielsweise Eingaben, Schalter, Anzeigen und andere Bedienelemente platzieren. Unter **Größe** wählen **Abschnitte** und **Abschnitte senkrecht** jeweils **1 bis 12**: maximal **12:12 Rasterfelder**. Eine Rasterzelle ist mindestens 64×64 px groß. Die Gesamtbreite/-höhe enthält die Zwischenabstände der Einzelwidgets: bei 1 px **Abstand rundherum** ergeben sich pro Richtung **64 / 130 / 196 / 262 px**. Eingabe und Ziehen skalieren beide Richtungen zusammen; eine geänderte Abschnittszahl erhält die Rasterzellengröße.

Nur die vier einzeln aktivierbaren **Gehäuse-Snappunkte** sind vorhanden. Keine Entität, Wertanzeige oder Daten-Ein-/Ausgänge. Industriestyle, Schrauben, Rahmenfarbe, optional angepasste Rahmenbreite, Eckenradius und CSS stehen wie bei den anderen Industrieelementen zur Verfügung. Der voreingestellte **CSS z-index -1** legt das Blindelement unter normale Widgets. Darübergelegte Elemente bleiben separat bedienbar und verschiebbar; das Blindelement gruppiert sie nicht automatisch. Für eigene Hintergründe lässt sich Industriestyle abschalten und CSS verwenden. Das Bild zeigt ein lokales Beispiel.

## Industrie-Wetter: LCD / LED

| LCD | LED |
| --- | --- |
| ![Industrie-Wetter in LCD-Optik mit 18,6 Grad und Pixelsymbol](/images/grafik-visual-studio/industrial-weather-lcd.png) | ![Industrie-Wetter mit blau leuchtender LED-Pixelanzeige](/images/grafik-visual-studio/industrial-weather-led.png) |

Die Bilder zeigen Beispieldaten aus einer simulierten Wetterentität. **Wetterentität** bindet eine Home-Assistant-Entität `weather.*`: Zustand als eigenes Pixelsymbol und Text, Temperatur groß, darunter Luftfeuchtigkeit und Wind. Symbole decken Sonne, klare Nacht, Wolken, Regen, Schnee/Schneeregen, Hagel, Gewitter, Nebel, Wind und außergewöhnliches Wetter ab. Temperatur- und Windeinheiten stammen aus Home Assistant und werden ohne Umrechnung angezeigt; Groß-/Kleinschreibung der Einheiten bleibt erhalten.

**Regenwahrscheinlichkeit anzeigen** und **Tagesminimum/-maximum anzeigen** ergänzen die unterste Zeile, links Regen, rechts Minimum / Maximum. Diese Angaben kommen aus der täglichen Vorhersage für den aktuellen Tag nach Browser-Ortszeit. Vorhersagen werden über die vorhandene HA-Schnittstelle geladen und fünf Minuten zwischengespeichert. Aktuelle Messwerte und Vorhersagen sind bei Home Assistant getrennt; siehe [HA-Wetterentität und Vorhersagen](https://developers.home-assistant.io/docs/core/entity/weather/). Unterstützt die Integration keine tägliche Vorhersage, zeigen die Zusatzwerte Striche, während aktuelle Werte weiter angezeigt werden.

Unter **Zusätzliche Sensoren** kann jeder Wert durch eine eigene Entität ersetzt werden: Temperatur, Luftfeuchtigkeit, Windgeschwindigkeit, Regenwahrscheinlichkeit, Tagesminimum und Tagesmaximum. Ein eingetragener Sensor hat für diesen Wert Vorrang, auch wenn er nicht verfügbar ist; es wird dann kein anderer Wert untergeschoben. Ohne Sensor gilt die Wetterentität beziehungsweise Tagesvorhersage. Fehlende Werte sind **--**, unbekannter Zustand erhält ein Fragezeichen-Symbol. **Beispieldaten ohne Wetterentität** ist ausdrücklich zuschaltbar und zeigt **DEMO**; bei gebundener Wetterentität wird niemals automatisch auf Beispieldaten umgeschaltet.

**Anzeigeart → LCD / LED**: LCD mit Segment-/Hintergrundfarbe, LED mit frei wählbarer Leuchtfarbe. Der schwarze Bildschirmrand und die Gehäuseeigenschaften entsprechen den übrigen Industrieanzeigen. **2:4-Raster**, standardmäßig **262×130 px** bei **1 px Abstand rundherum**: Höhe = 2 × Rasterzelle + 2 × Abstand, Breite = 4 × Rasterzelle + 6 × Abstand. Die Rasterzelle bleibt mindestens 64 px groß. Eingabe, Ziehen und Abstandsänderungen erhalten die Ausrichtung zu zwei Reihen mit jeweils vier Einzelwidgets. Lange Angaben werden gekürzt; der Tooltip enthält die vollständigen Texte.

Ein/Aus funktioniert über **Display Ein/Aus: Entität** oder einen einzeln aktivierbaren **oberen Koppelpunkt** (`display-power`) mit Vorrang. Ohne Bindung gilt der Vorschauzustand; fehlende oder unbekannte Ein/Aus-Werte lassen den Bildschirm dunkel. Sichtbare und unsichtbare Kippschalter-Verbindungen werden unterstützt. Kein Messwert-Eingang, Ausgang oder Schreibbefehl; vier Gehäuse-Ecken, Abstand, Schrauben, Rahmenfarbe, optionale Rahmenbreite und Eckenradius bleiben verfügbar.

## Industrie-Uhr: Nixie / LED / LCD

![Industrie-Uhr mit sechs Nixieröhren und orange leuchtender Zeit 12:34:58](/images/grafik-visual-studio/industrial-clock-nixie.png)

| LED | LCD |
| --- | --- |
| ![Industrie-Uhr mit blauer LED-Leuchtfarbe](/images/grafik-visual-studio/industrial-clock-led.png) | ![Industrie-Uhr mit dunklen LCD-Segmenten auf grünem Hintergrund](/images/grafik-visual-studio/industrial-clock-lcd.png) |

Ein Widget mit **Anzeigeart → Nixieröhre / LED / LCD**. Nixie imitiert Glasröhren, Schutzgitter und übereinanderliegende Drahtziffern mit orangefarbenem Leuchten. LED zeigt leuchtende Siebensegmentziffern mit frei wählbarer **LED-Leuchtfarbe**. LCD bietet **LCD-Segmentfarbe** und **LCD-Hintergrundfarbe**. Die Bilder zeigen eine festgehaltene Beispielzeit.

**Sekunden anzeigen** wechselt zwischen **HH:MM:SS** und **HH:MM**, im 24-Stunden-Format. **Doppelpunkte blinken** lässt die Trennzeichen im Sekundentakt blinken; abschaltbar für ruhige Anzeigen. **Zeitzone** bietet Browser-Ortszeit, UTC oder Europe/Berlin mit automatischer Sommer-/Winterzeit. Zeitquelle ist die Browser-Uhr. Es gibt keine erforderliche Zeit-Entität und keinen Daten-Ausgang. Ein gemeinsamer Takt aktualisiert ausschließlich den Uhrinhalt; Auswahl und Eingabefokus im Editor bleiben erhalten.

| Ansicht | HH:MM:SS | HH:MM | Mindesthöhe |
| --- | --- | --- | --- |
| Nixie | 518×128 px | 388×128 px | 64 px |
| LED / LCD | 262×64 px | 196×64 px | 32 px |

Standardmaße gelten bei **1 px Abstand rundherum**. Die Breite entspricht vier beziehungsweise drei Rastereinheiten einschließlich Zwischenräumen: Breite = Höhe × Rastereinheiten + 2 × Abstand × (Rastereinheiten − 1). Größe bleibt bei Eingabe und Ziehen proportional. Beim Wechsel zu Nixie wird die Höhe verdoppelt, zurück zu LED/LCD halbiert; eine eigene Vergrößerung bleibt relativ erhalten. Sekunden- und Abstandsänderungen passen die Breite an.

Gehäuse, Schrauben, Rahmenfarbe, optionale Rahmenbreite, Eckenradius und vier einzeln aktive Gehäuse-Snappunkte bleiben verfügbar. **Display Ein/Aus: Entität** oder ein einzeln aktivierbarer **oberer Ein/Aus-Koppelpunkt** (`display-power`) steuert die Uhranzeige; der Koppelpunkt hat Vorrang. Ohne Bindung gilt **Ohne Eingang eingeschaltet**. Unbekannte oder fehlende Ein/Aus-Werte lassen sie dunkel, Uhrzeit und Gehäuse bleiben erhalten. Kippschalter-Verbindungen können sichtbar oder unsichtbar sein. Die Nixie-Grafiken sind eigene SVG-Zeichnungen; die bereitgestellte OmniGraffle-Vorlage wird nicht verteilt.

## Segmentanzeigen: LED und LCD

| 7-Segment-LED | 16-Segment-LED | 16-Segment-LCD |
| --- | --- | --- |
| ![Rote 7-Segment-LED mit 647,25 Watt](/images/grafik-visual-studio/industrial-segment-0.png) | ![Blaue 16-Segment-LED mit Eingangswert 56,78 und Ampere-Anzeige](/images/grafik-visual-studio/industrial-segment-1.png) | ![Grüne 16-Segment-LCD mit SOLAR 12.3 und Volt-Anzeige](/images/grafik-visual-studio/industrial-segment-2.png) |

Die Bilder verwenden Beispieldaten. Alle drei Anzeigen haben **1–10 feste Stellen**. Das Minuszeichen belegt eine Stelle, ein Dezimalpunkt wird an die vorherige Stelle angehängt. Die 7-Segment-LED zeigt Zahlen mit einstellbaren Nachkommastellen und optionalen führenden Nullen. Rundung erfolgt vor der Prüfung der Stellenzahl; Überlauf oder fehlende Werte zeigen Striche. Die 16-Segment-Anzeigen zeigen Zahlen und Text in Großbuchstaben. Längere Texte werden gekürzt, der vollständige Inhalt steht im Tooltip; nicht unterstützte Zeichen erscheinen als Fragezeichen. Unterstützt werden A–Z, 0–9, Leerzeichen, Punkt, Minus, Unterstrich, Fragezeichen, Plus, Schrägstriche, Doppelpunkt, Gleichheits- und Gradzeichen.

**Inhalt: Entität** liefert den Messwert beziehungsweise Text. Ohne Bindung gilt **Vorschauwert / Text**. Alternativ wird der **Wert-Eingangs-Koppelpunkt links** (`value-input`) einzeln aktiviert; er hat Vorrang vor der Entität. Ein zweiter, unabhängig aktivierbarer Koppelpunkt **oben** (`display-power`) oder **Display Ein/Aus: Entität** steuert die Anzeige. Der Ein/Aus-Koppelpunkt hat Vorrang; ohne Bindung gilt **Ohne Eingang eingeschaltet**. Fehlende oder unbekannte Ein/Aus-Werte lassen die Anzeige dunkel. Sichtbare und unsichtbare Wert-Verbindungen funktionieren, beispielsweise vom Kippschalter. Diese Anzeigen haben keine Ausgänge oder Schreibbefehle.

Rechts stehen **W, A und V untereinander**. Unter **Einheiten-LED** ist ausschließlich **Aus / W / A / V** wählbar: maximal eine Beschriftung leuchtet. Die übrigen bleiben dunkel sichtbar. **Segment- und Einheitenfarbe** gilt für Ziffern, Text und gewählte Einheit gemeinsam. LED-Modi imitieren leuchtende Segmente mit leichtem Lichtschein, LCD verwendet kontrastierende Segmente auf einem einstellbaren Hintergrund. Die Einheit wird bewusst ausgewählt und nicht automatisch aus Entitätsattributen abgeleitet.

Die Standardgröße beträgt **262×64 px** im **1:4-Raster**, alternativ **196×64 px** im **1:3-Raster**, jeweils bei **1 px Abstand rundherum**. Wie bei Schaltern und linearen Anzeigen gilt: Breite = Höhe × Rastereinheiten + 2 × Abstand × (Rastereinheiten − 1). Eingabe und Ziehen halten das Verhältnis ein. Für zehn gut lesbare Stellen empfiehlt sich 1:4; bei Bedarf lässt sich das ganze Widget vergrößern. Gehäuse, Schrauben, Rahmenfarbe, optionale Rahmenbreite, vier einzeln aktivierbare Gehäuse-Ecken und Abstand bleiben verfügbar.

Die Segmentgeometrie ist eine eigene SVG-Zeichnung und benötigt keine installierte Schrift. Die bereitgestellte **16Segments Basic.otf** ist laut eingebetteter Lizenz nur privat nutzbar und wird deshalb nicht im öffentlichen Paket verteilt.

## Zählwerk / Odometer

Das Zählwerk ist eine eigenständige, rein lesende Industrieanzeige mit mechanischen Ziffernrollen. Ein Zahlenwert kommt aus einer **Entität** oder über den einzeln aktivierbaren **Eingangs-Koppelpunkt links** (`value-input`). Der aktivierte Koppelpunkt hat Vorrang; ohne Bindung erscheint der Vorschauwert. Sichtbare und unsichtbare Wert-Verbindungen werden unterstützt. Es gibt keinen Ausgang und keine Schreibbefehle.

| Normal 1:3 | Normal 1:4 |
| --- | --- |
| ![Zählwerk mit fünf Ganzzahlstellen, zwei Nachkommastellen und kWh](/images/grafik-visual-studio/industrial-odo-normal-3.png) | ![Breites Zählwerk mit Eingang über eine Wert-Verbindung](/images/grafik-visual-studio/industrial-odo-normal-4.png) |

| Schmal 0,5:3 | Schmal 0,5:4 |
| --- | --- |
| ![Schmales Zählwerk mit halber Ziffernhöhe](/images/grafik-visual-studio/industrial-odo-slim-3.png) | ![Breites schmales Zählwerk](/images/grafik-visual-studio/industrial-odo-slim-4.png) |

Die Bilder verwenden Beispieldaten. Bei **1 px Abstand rundherum** gelten **196×64 / 262×64 px** für normale und **196×32 / 262×32 px** für schmale Widgets. Die Breite enthält die Lücken zwischen drei beziehungsweise vier Einzelwidgets wie bei den linearen Anzeigen. **Breite in Rastereinheiten**, Eingabe, Ziehen und Änderungen des Abstands berücksichtigen diese Ausrichtung.

Die **Ziffernfensterhöhe** beträgt fest 62,5 % der Widgethöhe: **40 px** bei 64 px, **20 px** bei 32 px. 1:3 und 1:4 nutzen die gleiche Höhe; die schmalen Formate exakt die Hälfte. Mehr Stellen verändern Ziffernbreite und Abstände, nicht die Höhe.

**Ganzzahlstellen** ist fest auf 1–12, **Nachkommastellen** auf 0–6 einstellbar. Das Komma oder der Punkt besitzt einen schmalen Zwischenraum. Beispiel: fünf Ganzzahlstellen und zwei Nachkommastellen ergeben `00123,45`. Ohne **Führende Nullen** bleiben deren Plätze leer. **Platz für Minuszeichen** reserviert dauerhaft eine Position vor den Ziffern; negative Werte ohne diesen Platz werden als Überlauf behandelt.

Eine eingetragene **Einheit** hat Vorrang vor `unit_of_measurement` der Entität beziehungsweise der Einheit der Wert-Verbindung. Die Einheit bleibt rechts neben dem Ziffernfenster. **Schriftfarbe** und **Einheiten-Schriftgröße** sind einstellbar; lange Einheiten werden gekürzt. Industriestyle, standardmäßig aktive Schrauben, Rahmenfarbe, optionale Rahmenbreite, vier einzeln aktive Gehäuse-Ecken und Abstand bleiben verfügbar.

In der Runtime rollen geänderte Ziffern für 350 ms, einschließlich Übertrag von 09 auf 10. Die Browser-Einstellung für reduzierte Bewegung deaktiviert diese Animation. Fehlende oder nicht verfügbare Werte zeigen **Striche**; ein Wert außerhalb der Stellenzahl zeigt **#**. Rundung erfolgt vor der Überlaufprüfung, beispielsweise wird `99999,999` bei fünf Ganzzahl- und zwei Nachkommastellen als Überlauf erkannt. Die Breite bleibt dabei konstant.

## Linear-Gauge / Schieberegler

Ab **Studio 0.1.241** aktualisiert die Entitätsauswahl sofort den Anzeigemodus: Unter **Skala → Darstellung → Farbbalken** stehen Farbskala und Farbbereiche bereit. Ohne Eingang bleibt ausschließlich Strichskala. Paket 0.6.0 kann weiterverwendet werden.

Mit **Eingangsentität** oder aktiviertem **Datenfluss-Eingang** arbeitet das Widget als Anzeige: ein **Dreieck** markiert den Wert. Wählbar sind **Strichskala** oder **Farbbalken** mit eigenen Farbbereichen. Ohne Eingang wird es zum **Schieberegler mit rechteckigem Griff und ausschließlich Strichskala**. Auch eine zuvor gespeicherte Farbbalken-Einstellung erzeugt im Schieberegler keinen Farbbalken.

| Schieberegler mit Strichskala | Linear-Gauge mit Farbbalken |
| --- | --- |
| ![Linearer Schieberegler mit rechteckigem Griff und Strichskala](/images/grafik-visual-studio/industrial-linear-slider.png) | ![Linear-Gauge mit Dreieck und konfigurierten Farbbereichen](/images/grafik-visual-studio/industrial-linear-gauge.png) |

| Schmaler Schieberegler | Schmales Linear-Gauge |
| --- | --- |
| ![Schmale lineare Bedienung mit Strichskala](/images/grafik-visual-studio/industrial-linear-slim.png) | ![Schmale lineare Anzeige mit Dreieck](/images/grafik-visual-studio/industrial-linear-slim-gauge.png) |

Die Bilder verwenden Beispieldaten. Unter **Größe → Breite in Rastereinheiten** stehen 2, 3 und 4 zur Auswahl:

| Ausführung | Höhe/Breite | Mindestgrößen (Breite × Höhe) |
| --- | --- | --- |
| Normal | 1:2 / 1:3 / 1:4 | 130×64 / 196×64 / 262×64 px |
| Schmal | 0,5:2 / 0,5:3 / 0,5:4 | 130×32 / 196×32 / 262×32 px |

Die Tabelle gilt für **1 px Abstand rundherum**. Die Gesamtbreite berücksichtigt die Lücken zwischen einzelnen Widgets: **Rasterbreite × Einheiten + 2 × Abstand × (Einheiten − 1)**. Rasterbreite ist die Höhe, bei der schmalen Ausführung die doppelte Höhe. Ohne Abstand ergeben sich 128/192/256 px. Damit fluchten die Außenkanten mit zwei, drei oder vier einzelnen Widgets; Änderungen am Abstand passen die Breite automatisch an.

Beim Eingeben oder Ziehen werden beide Maße im gewählten Verhältnis skaliert. **Minimum**, **Maximum**, **Skalenteilung** und **Bedien-Schrittweite** sind getrennt einstellbar; negative Werte sind erlaubt, Null wird hervorgehoben. **Skalenwerte anzeigen** ergänzt die Endpunkte und bei freiem Platz Null. Für den Farbbalken gelten die gleichen bis zu acht Farbbereiche wie beim Gauge/Poti. Ungültige Bereiche zeigen keine erfundenen Farben; fehlende Eingangswerte zeigen keinen Zeiger.

Die Wertanzeige übernimmt Einheit und Schriftgestaltung wie beim Gauge/Poti. **Mitte** platziert sie mittig oberhalb der linearen Skala, **Unten** unterhalb. Industriestyle, Schrauben, Rahmenfarbe, optionale Rahmenbreite, vier einzeln aktivierbare Gehäuse-Ecken, Abstand und zentrale Koppelpunktfarben gelten ebenfalls.

In der Runtime lässt sich der Griff mit Maus, Touch oder Tastatur bewegen. Pfeiltasten ändern um einen Bedien-Schritt, Bild auf/ab um zehn Schritte, Pos1/Ende springen zum Minimum/Maximum. Ausgabe erfolgt **beim Loslassen** oder **während des Ziehens**. Eine `number`-/`input_number`-Entität oder ein Ausgangspunkt mit sichtbarer/unsichtbarer Wert-Verbindung übernimmt den Wert. Der Editor sendet keine Bedienbefehle. Ein aktivierter Datenfluss-Eingang hat Vorrang vor der Eingangsentität und bleibt auch bei fehlendem Wert im Anzeigemodus.

## LCD – 20×4 und 16×2

Die Displays imitieren eine **5×8-Punktmatrix-Schrift** mit schwarzem Bildschirmrand. Die Schrift wird dynamisch aus Bildpunkten aufgebaut und ist Bestandteil von Studio; eine externe Schriftinstallation ist nicht erforderlich. Groß- und Kleinbuchstaben, Zahlen, Satzzeichen, Umlaute, ß, €, °, µ, Ω, Pfeile und ✓ sind enthalten. Nicht unterstützte Zeichen erscheinen als `?`.

| 20×4 Gelb/Weiß | 20×4 Blau/Weiß |
| --- | --- |
| ![LCD mit gelbem Hintergrund und weißer Punktmatrix-Schrift](/images/grafik-visual-studio/industrial-lcd-yellow.png) | ![LCD mit blauem Hintergrund und weißer Punktmatrix-Schrift](/images/grafik-visual-studio/industrial-lcd-blue.png) |

| 16×2 Blau/Weiß | Display ausgeschaltet |
| --- | --- |
| ![LCD mit 16 Zeichen je Zeile und zwei Zeilen](/images/grafik-visual-studio/industrial-lcd-small.png) | ![Ausgeschaltetes LCD mit sichtbarem Industriegehäuse](/images/grafik-visual-studio/industrial-lcd-off.png) |

Die Bilder zeigen Beispieldaten. **Beide Größen bieten Gelb/Weiß und Blau/Weiß.** Ab **Studio 0.1.242** ist das 16×2-Display normal groß mit **192×64 px**; das 20×4-Display doppelt so breit und hoch mit **384×128 px**. Beide behalten Höhe/Breite **1:3** beim Eingeben und Ziehen. Kleinere gespeicherte Displays werden beim Laden auf diese Mindestgrößen angehoben. Größere Darstellungen skalieren den Bildschirm und die Zeichen gemeinsam. Die blauen und gelben Hintergründe sind dunkler, die weißen Bildpunkte kräftiger. Paket 0.6.0 bleibt unverändert; ein Studio-Update genügt.

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

Alle Kippschalter-Eigenschaften gelten auch hier: Beschriftung, zusätzliche Schilder ON/OFF, 1/0, EIN/AUS oder Benutzerdefiniert, LED-Farben, Entitäten, E1–E4/A1–A4, sechs Gehäuse-Snappunkte, Schrauben, Rahmen und Abstand. Das aufgedruckte O/I bleibt Bestandteil der Grafik. Größe 1:1 bis 4:1, mindestens 64 px je Kanal. Bedienung erfolgt nur in der Runtime.

## Gauge/Poti: Daten und Bedienung

Ab **Studio 0.1.282** steuert der aktive Datenfluss-Ausgang auch Tempo und Richtung einer angeschlossenen SVG-Line. Eine zusätzliche Home-Assistant-Ausgangsentität ist dafür nicht nötig: Das Feld **Ausgang: number/input_number-Entität** bleibt bei rein lokalen Verbindungen leer; ein Startwert wie `0` gehört ins Vorschauwertfeld. Für Home-Assistant-Schreibaktionen wähle dagegen eine verfügbare `number.*`- oder `input_number.*`-Entität.

Für sichtbar wertabhängiges Tempo: Animation einschalten, **Poti / SVG LineBox-Teiler** beispielsweise auf **10** setzen und automatische Poti-/LineBox-Teileranpassung ausschalten. 10 ergibt 1 Zyklus/s, 20 ergibt 2; 0 steht still, negative Werte laufen rückwärts. Mit Teiler 1 erreichen alle Beträge ab 20 die Höchstgeschwindigkeit. Weitere Details unter [SVG-Line](./svg-line); [Editorbild und Animation](./bildergalerie) zeigen den Aufbau.

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

Ab **Studio 0.1.248** bieten **alle Industrie-Widgets** die Checkbox **Hintergrund anpassen** mit **Gehäuse-Hintergrundfarbe**. Ohne Haken bleibt der bisherige Standardverlauf von dunkelgrau nach anthrazit erhalten. Mit Haken wird eine einheitliche eigene Farbe verwendet; Vorgabe **#263238**. Die Farbauswahl ist nur bei aktiviertem Haken bedienbar. Nach dem Abschalten kehrt der Standardhintergrund zurück, die gewählte Farbe bleibt für später gespeichert. Das gilt für Editor und Runtime, auch wenn Industriestyle abgeschaltet ist. Bildschirm-, LCD-, Segment-, LED- und Skalenfarben werden weiter separat eingestellt. Das Studio-Update genügt auch mit einem älteren installierten Industriepaket; Paket 0.10.3 aktualisiert die Anleitung.

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

Ab **Studio 0.1.249** gibt es pro Schalter **Schildbeschriftung → Benutzerdefiniert** mit **Text bei AUS** und **Text bei EIN**. Zum Beispiel Überschrift **Pumpe**, AUS-Text **1**, EIN-Text **2**, oder **Kalt/Warm**. Die vier Kanäle haben unabhängige Texte; leere eigene Texte bleiben leer. Lange Schildtexte werden gekürzt, der Tooltip zeigt den vollständigen Text des aktuellen Zustands. Das gilt ebenfalls für den Wippschalter; dessen aufgedruckte O/I-Symbole bleiben in der Grafik. **Nur die Beschriftung ändert sich:** Entitätsaktionen und E-/A-Koppelpunkte bleiben boolesch (`false`/`true`); die Texte „1“/„2“ werden nicht als Zahlenwerte ausgegeben und wählen nicht automatisch zwei Entitäten. Vorhandene Schildvarianten bleiben verfügbar. Das Studio-Update genügt mit bestehenden Industriepaketen.

Ab **Studio 0.1.236** wird beim Kippschalter der Zwischenabstand in die Blockbreite eingerechnet: **Höhe × Schalteranzahl + 2 × Abstand rundherum × (Schalteranzahl − 1)**. Bei 64 px Höhe und 1 px Abstand rundherum sind die Breiten **64 / 130 / 196 / 262 px**. Schaltermitten sowie E/A-Anschlüsse fluchten damit mit einzelnen Widgets darunter. Eingabe und Ziehen berücksichtigen den Zuschlag. Diese Anpassung gilt zunächst nur für den Kippschalter; Wippschalter bleiben unverändert. Ein Studio-Update genügt, Paket 0.3.0 bleibt unverändert.

Ab Paket **0.2.0** und Studio **0.1.232** stehen ein bis vier unabhängig bedienbare Schalter nebeneinander zur Verfügung. **Anzahl Schalter** legt das Verhältnis Breite/Höhe von **1:1 bis 4:1** fest. Minimum sind 64 px Höhe und 64 px Breite je Kanal; die Maße bleiben beim Eingeben und Ziehen proportional.

![Vier Industrie-Kippschalter mit kleinen LEDs und drei Schildvarianten](/images/grafik-visual-studio/industrial-switches.png)

*Runtime mit Beispieldaten: eigene Beschriftungen, grüne LEDs und Schilder ON/OFF, 1/0 und EIN/AUS. Ab Studio 0.1.233 stammt der Metallhebel aus der von rockbaer2007 bereitgestellten transparenten PNG und ist in beiden Stellungen vollständig sichtbar. Die LED bleibt eine CSS-Zeichnung. Das Studio-Update genügt; Paket 0.2.0 muss nicht erneut installiert werden.*

Jeder Bereich **Schalter 1** bis **Schalter 4** enthält eine feste **Beschriftung**, **Schildbeschriftung** mit **ON/OFF**, **1/0**, **EIN/AUS** oder **Benutzerdefiniert**, Startzustand und eigene LED-Farben für Ein und Aus. Die LED liegt oberhalb der Beschriftung; die Schildtexte ändern sich nicht durch Entitäten. Schriftgröße und Schriftfarbe stehen unter **Beschriftung**.

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
