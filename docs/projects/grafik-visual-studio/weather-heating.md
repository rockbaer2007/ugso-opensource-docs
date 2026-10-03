---
title: Wetter und Heizung
description: Das optionale Diagramm-Widget-Paket installieren und konfigurieren.
---

# Wetter und Heizung

Ab **Studio 0.1.189** kannst du das Paket **Wetter und Heizung 1.2.0** nachinstallieren. Es enthält **Allgemeines Diagramm**, **Balkendiagramm für zwei Wochen** und **Wetter-Widget**. Funktionsreferenz ist [ioBroker.vis-2-widgets-weather-and-heating](https://github.com/rg-engineering/ioBroker.vis-2-widgets-weather-and-heating); das Studio verwendet eine eigene SVG-Umsetzung. Weitere Wetter- und Heizungswidgets sowie ioBroker-spezifische Adapterbindungen sind noch nicht enthalten.

## Installieren

Lade [ugso.weather-heating.wg](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/refs/heads/master/ha_grafik_visual_studio/packages/weather-heating/ugso.weather-heating.wg) herunter. Öffne **Einstellungen → Widget-Pakete → Lokales .wg / .wg.zip installieren** und wähle die Datei. Nach dem Neuladen erscheint ein eigenes Set mit automatisch vergebener Farbe. Die Farbzuordnung bleibt in diesem Browser erhalten, auch bei Entfernen und Neuinstallation. Die 74 integrierten Widgets bleiben verfügbar.

## Diagramm konfigurieren

Ein installiertes Paket 1.0.0 oder 1.1.0 kannst du über denselben Import auf 1.2.0 aktualisieren. Vorhandene Diagramme und Projektwerte bleiben erhalten. Updates dürfen ausschließlich neue Widgets ergänzen; Änderungen bestehender Definitionen oder Downgrades werden abgewiesen.

Unter **Allgemein** findest du Überschrift, Anzahl der Serien (1–10), Legende und Darstellung ohne Karte. Die erste Reihe kann die allgemeine Entität verwenden. Jede Gruppe **Daten [N]** bietet eine eigene Entität, ein optionales Attribut, Vorschau-JSON, X-/Y-Schlüssel, Name, Einheit, Farbe, Linie/Balken, linke/rechte Wertachse und Differenzberechnung. Mit einer Entitätsbindung liest das Diagramm ausschließlich deren Zustand oder Attribut. Fehlen Live-Daten, wird kein Vorschau-JSON eingesetzt. Es schreibt keine HA-Zustände.

Beispiel für Vorschau-JSON oder ein HA-Attribut:

```json
[
  {"x":"2026-10-03T08:00:00","value":12},
  {"x":"2026-10-03T09:00:00","value":18},
  {"x":"2026-10-03T10:00:00","value":15}
]
```

Standard-Schlüssel sind `x` und `value`; eigene Schlüssel und Paare `[x,y]` sind möglich. **Zeit** erwartet ISO-Datumsangaben oder Unix-Millisekunden. **Kategorie** zeigt Texte, beispielsweise Jahreszahlen. Zeitpunkte werden vor der Differenzberechnung sortiert. Fehlende Werte unterbrechen die Linie und Differenzfolge; die erste Differenz hat keinen Vorgänger. Linke und rechte Achse werden unabhängig skaliert.

**X-Achse** bietet den Beschriftungsstandard `ddd HH:mm`. Unterstützte Tokens: `YYYY`, `MM`, `DD`, `ddd`, `HH`, `mm`, `ss`. Farben stehen unter **WIDGET → CSS Diagramm**. Bis zu 20.000 Eingabezeilen werden akzeptiert; große Reihen werden auf höchstens 500 Punkte pro Reihe reduziert. Das Widget ruft keine HA-Historie ab: Die gewählte Entität muss das Datenarray bereits bereitstellen.

![Installiertes Set mit Diagrammvorschau](/images/grafik-visual-studio/weather-heating-chart.png)

## Balkendiagramm für zwei Wochen

Die Gruppen **Aktuelle Woche** und **Vorwoche** enthalten je sieben HA-Entitäten für Montag bis Sonntag sowie bearbeitbare Vorschauwerte. Das Widget vergleicht die Tagespaare nebeneinander. Es berechnet keine Wochenhistorie selbst und verschiebt keine Werte beim Wochenwechsel: Deine Sensoren müssen jeweils den passenden Tageswert bereitstellen.

**Wochenwerte anzeigen** entspricht funktional der Originaloption „Sichtbar“: ausgeschaltet zeigt das Widget ausschließlich Vorschauwerte; eingeschaltet liest es ausschließlich die 14 Tagesentitäten. Ungebundene, nicht verfügbare oder nicht numerische Live-Werte ergeben keine Balken. Null ist ein gültiger Wert. Die gesamte Widget-Sichtbarkeit regelst du weiterhin unter **Sichtbarkeit**.

Unter **Allgemein** stellst du Überschrift und Farbe, Legendentextfarbe, Einheit, Wochenfarben, Achsenbeschriftungsfarbe, Y-Achse links/rechts, 0–5 Dezimalstellen, Legende und **Ohne Karte** ein. **X-Achse** hat eine eigene Farbe. Einheiten und formatierte Werte erscheinen in Legende und Balkenhinweisen; die Wochentage folgen der App-Sprache. Farben werden gemäß deinen Einstellungen verwendet.

![Zwei-Wochen-Balkendiagramm im installierten Set](/images/grafik-visual-studio/weather-heating-two-weeks.png)

## Wetter-Widget

**Datenquelle** bietet `home-assistant`, `json` und `individual`. **Datenstruktur** wählt fünf Tageswerte (`daily`) oder bis zu 24 Stundenwerte (`hourly`). Die Quellen ersetzen die ioBroker-Instanz- und OID-Auswahl durch HA-Bindungen.

Bei `home-assistant` wählst du eine `weather.*`-Entität. Der Studio-Server liest die Vorhersage über [weather.get_forecasts](https://www.home-assistant.io/integrations/weather/). Erfolgreiche Antworten werden fünf Minuten zwischengespeichert; nach Fehlern erfolgt frühestens nach einer Minute ein neuer Versuch. Die Wetterintegration muss den gewählten Vorhersagetyp unterstützen. Temperatur- und Niederschlagseinheiten stammen aus deren Attributen. Ein echter HA-Abruf erfordert die laufende Add-on-/Supervisor-Anbindung.

Bei `json` liest das Widget das gewählte **Vorhersageattribut (JSON)**; leer bedeutet Entitätszustand. Erwartet wird ein Array, beispielsweise:

```json
[{"datetime":"2026-10-03T12:00:00Z","temperature":18,"templow":10,"precipitation":0,"cloud_coverage":25,"precipitation_probability":40}]
```

Bei `individual` bindest du **Tagesdatum [1–5]** beziehungsweise **Zeitpunkte [1–24]** sowie die zugehörigen Temperatur-, Regen-, Wolken- und Wahrscheinlichkeitswerte an einzelne Sensoren. Zeitangaben sind ISO-Daten oder Unix-Millisekunden. Tagesansichten verwenden nur die ersten fünf Bindungen jeder Wertegruppe. Ungültige Zeitpunkte werden ausgelassen, fehlende Werte unterbrechen Linien; Null ist gültig. Ohne gebundene Wetter-/JSON-Entität zeigen die ersten beiden Quellen die bearbeitbaren Vorschau-Daten. Fehlende Live-Daten ersetzen sie niemals durch Vorschauwerte.

**Temperatur**, **Regen**, **Wolken** und **Regenwahrscheinlichkeit** sind einzeln aktivierbar. Jede Gruppe hat Farben und eine linke/rechte Wertachse; Regen erscheint als Balken. **Im zweiten Diagramm anzeigen** erzeugt eine eigene Diagrammfläche. Unterschiedliche Einheiten auf derselben Achse werden automatisch getrennt. **Sonne oder Wolken** zeigt Wolkenbedeckung oder deren Gegenanteil in Prozent, keine Sonnenstunden. Fehlende Anbieterwerte werden nicht aus Wetterzuständen geschätzt. Name, optionale Standort-Entität, Legende, Farben, X-Datumsformat, Größe und **Ohne Karte** sind einstellbar.

![Wetter-Widget mit Temperatur und Regen](/images/grafik-visual-studio/weather-heating-weather.png)

Der reproduzierbare Paketbau und das geprüfte Manifest stehen im [Quellcode](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/weather-heating). Der [Paketvertrag](widget-pakete.md) beschreibt Schnittstelle 0.2.
