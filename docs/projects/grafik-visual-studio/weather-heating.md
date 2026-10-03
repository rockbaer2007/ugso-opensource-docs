---
title: Wetter und Heizung
description: Das optionale Diagramm-Widget-Paket installieren und konfigurieren.
---

# Wetter und Heizung

Ab **Studio 0.1.187** kannst du das Paket **Wetter und Heizung 1.0.0** nachinstallieren. Es enthält zunächst **Allgemeines Diagramm**. Funktionsreferenz ist [ioBroker.vis-2-widgets-weather-and-heating](https://github.com/rg-engineering/ioBroker.vis-2-widgets-weather-and-heating); das Studio verwendet eine eigene SVG-Umsetzung. Weitere Wetter- und Heizungswidgets sowie ioBroker-spezifische Adapterbindungen sind noch nicht enthalten.

## Installieren

Lade [ugso.weather-heating.wg](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/refs/heads/master/ha_grafik_visual_studio/packages/weather-heating/ugso.weather-heating.wg) herunter. Öffne **Einstellungen → Widget-Pakete → Lokales .wg / .wg.zip installieren** und wähle die Datei. Nach dem Neuladen erscheint ein eigenes Set mit automatisch vergebener Farbe. Die Farbzuordnung bleibt in diesem Browser erhalten, auch bei Entfernen und Neuinstallation. Die 74 integrierten Widgets bleiben verfügbar.

## Diagramm konfigurieren

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

Der reproduzierbare Paketbau und das geprüfte Manifest stehen im [Quellcode](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/weather-heating). Der [Paketvertrag](widget-pakete.md) beschreibt Schnittstelle 0.2.
