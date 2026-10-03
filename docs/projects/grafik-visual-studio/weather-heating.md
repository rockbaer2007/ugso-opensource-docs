---
title: Wetter und Heizung
description: Das optionale Diagramm-Widget-Paket installieren und konfigurieren.
---

# Wetter und Heizung

**Inspiriert von den ioBroker-Widgets „Wetter und Heizung“ von [rg-engineering](https://github.com/rg-engineering/ioBroker.vis-2-widgets-weather-and-heating).** Die Studio-Widgets sind eine eigene Umsetzung für Home Assistant.

Ab **Studio 0.1.194** kannst du das Paket **Wetter und Heizung 1.7.0** nachinstallieren. Es enthält **Allgemeines Diagramm**, **Balkendiagramm für zwei Wochen**, **Wetter-Widget**, **Übersicht über Heizräume**, **METEORED-Wetter-Widget**, **Fensterstatus-Übersicht**, **Meinen Vermieter informieren** und **Allgemeine Heizparameter**. Funktionsreferenz ist [ioBroker.vis-2-widgets-weather-and-heating](https://github.com/rg-engineering/ioBroker.vis-2-widgets-weather-and-heating); das Studio verwendet eigene Darstellungen. Weitere Wetter- und Heizungswidgets sowie ioBroker-spezifische Adapterbindungen sind noch nicht enthalten.

## Installieren

Lade [ugso.weather-heating.wg](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/raw/refs/heads/master/ha_grafik_visual_studio/packages/weather-heating/ugso.weather-heating.wg) herunter. Öffne **Einstellungen → Widget-Pakete → Lokales .wg / .wg.zip installieren** und wähle die Datei. Nach dem Neuladen erscheint ein eigenes Set mit automatisch vergebener Farbe. Die Farbzuordnung bleibt in diesem Browser erhalten, auch bei Entfernen und Neuinstallation. Die 74 integrierten Widgets bleiben verfügbar.

## Diagramm konfigurieren

Ein installiertes Paket 1.0.0 bis 1.6.0 kannst du über denselben Import auf 1.7.0 aktualisieren. Vorhandene Widgets und Projektwerte bleiben erhalten. Updates dürfen ausschließlich neue Widgets ergänzen; Änderungen bestehender Definitionen oder Downgrades werden abgewiesen.

## Allgemeine Heizparameter

Das Widget zeigt acht Zeilen: **Heizperiode aktiv**, **Heute Feiertag**, **Anwesend**, **Jetzt feiern**, **Gäste anwesend**, **Urlaub zu Hause**, **Urlaub abwesend** und **Kaminmodus**. Unter **Heizparameter-Entitäten** weist du jeder Zeile ihre eigene HA-Entität zu. Die optional gewählte Raum-Entität erscheint als Text über den Schaltern; sie wird nicht verändert. Die ursprüngliche `heatingcontrol.0`-Instanz ist nicht erforderlich.

In der Runtime sind verfügbare `input_boolean.*` und `switch.*` mit Zustand `on`/`off` schaltbar. Jede Aktion setzt ausschließlich die angeklickte Entität ein oder aus. Sensoren, beispielsweise `binary_sensor.*`, dienen nur als Anzeige. Während eines Schaltbefehls bleibt die entsprechende Entität gesperrt; Fehler werden über den bestehenden Studio-Schaltstatus gemeldet. **Allgemein → Schreibgeschützt** sperrt alle Schaltaktionen. **Ohne Karte** entfernt den äußeren Kartenhintergrund.

Ungebundene Zeilen sind in der Runtime deaktiviert und als **Ungebunden** markiert. Fehlende oder nicht verfügbare gebundene Werte zeigen **Unbekannt** mit einem gestreiften Schalter. Es wird kein Vorschauwert als Live-Wert eingesetzt. Die Checkboxen unter **Vorschau** gelten ausschließlich im ungebundenen Editor; auch dort werden keine Schaltbefehle gesendet.

Alle neun Entitätsbindungen, Vorschauwerte, Schreibschutz und Darstellungsoptionen bleiben in Projekt und Widget-Export erhalten. Das Widget bündelt deine vorhandenen HA-Entitäten; es berechnet keine Heizzeiten, Feiertage oder Anwesenheit und enthält keine eigene Heizregelung.

![Allgemeine Heizparameter und ihre Entitätsbindungen](/images/grafik-visual-studio/weather-heating-params.png)

## Meinen Vermieter informieren

Das Widget bietet **Priorität** (Information, Wichtig, Dringend), **Nachricht** und **Senden**. Im Editor ist es eine Vorschau. In der Runtime wird ausschließlich beim bewussten Senden an Home Assistant übergeben. Leere Nachrichten und wiederholte Klicks während einer laufenden Übergabe werden abgefangen. Bei einem Fehler bleibt die Nachricht zum erneuten Versuch erhalten; bei HA-Annahme wird sie geleert. Die Annahme bestätigt keine Zustellung.

Unter **Allgemein** findest du **Ohne Karte**, **Nachrichtentyp**, **HA-Benachrichtigungsaktion**, **Benachrichtigungs-Entität** und **Betreff / Nachrichtenüberschrift**. Beispiel: Aktion `notify.send_message` mit deiner konkreten Entität `notify.vermieter`. Alternativ kannst du eine eingerichtete benannte Aktion wie `notify.vermieter_email` verwenden; dann bleibt das Entitätsfeld leer. Das unspezifische `notify.notify` wird nicht akzeptiert. Empfänger, Zugangsdaten und Anbieter richtest du in HA ein, nicht im Widget. Siehe [HA-Benachrichtigungen](https://www.home-assistant.io/integrations/notify/).

Die Nachrichtentypen E-Mail, WhatsApp, Signal, Pushbullet und Jira beschreiben den eingerichteten Kanal. Die Auswahl installiert keinen Anbieter und wechselt das HA-Ziel nicht automatisch. Die originale ioBroker-Instanz `email.0` wird durch deine HA-Aktion ersetzt. Im Original ist bisher nur der E-Mail-Versand implementiert; die Studio-Darstellung verwendet für alle eingerichteten Kanäle denselben HA-Vertrag.

Überschrift und Priorität werden als Text vor die Nachricht gesetzt, beispielsweise `Meinen Vermieter informieren` und `[urgent]`. Die Priorität ist keine anbieterspezifische Zustell- oder Alarmstufe. Grenzen: 10.000 Nachrichtenzeichen, 200 Überschriftszeichen. Entwürfe bleiben bei HA-Zustandsaktualisierungen erhalten, jedoch nur im aktuellen Formular: Seitenwechsel oder Neuladen verwirft sie. Projekt-/Widget-Exporte enthalten die Konfiguration, keine eingegebenen Nachrichten.

![Nachrichtenformular und HA-Zielkonfiguration im Editor](/images/grafik-visual-studio/weather-heating-landlord.png)

## Fensterstatus-Übersicht

Unter **Fensterliste** wählst du eine HA-Entität und optional ein Attribut mit einer JSON-Liste. Der Originaldatenpunkt heißt `WindowStatesHtmlTableVis2`, enthält jedoch JSON. Ohne Entitätsbindung verwendet das Widget die bearbeitbare Vorschau:

```json
[
  {"room":"Wohnzimmer","sinceText":"seit","changed":"03.10.2026 12:30","isOpen":true},
  {"room":"Küche","sinceText":"seit","changed":"03.10.2026 11:00","isOpen":false}
]
```

`isOpen` akzeptiert Boolean-Werte, 1/0 und die Texte `true`/`false`, `on`/`off`, `open`/`closed`. Fehlt der Status, erkennt das Widget die alten Icon-Namen `fts_window_1w_open.svg` und `fts_window_1w.svg`, ohne Bilddateien zu laden. Sonst erscheint **Unbekannt**. Raum- und Änderungstexte werden als Text angezeigt, nicht als HTML. Grenzen: 200.000 Zeichen JSON, 500 Räume und 512 Zeichen pro Textfeld.

**Offene Räume: Entität** und ein optionales Attribut liefern eine separate, nicht negative ganzzahlige Anzahl. Gezählt werden Räume mit offenen Fenstern. Ohne diese Bindung wird die Anzahl nur aus einer nicht leeren Liste mit vollständig bekannten Zuständen abgeleitet. Fehlende gebundene Daten verwenden keine Vorschau; eine unbekannte Anzahl wird ausdrücklich angezeigt.

Unter **Farben** stehen Überschrift, Statuszeile, Raumname offen/geschlossen, letzte Änderung offen/geschlossen und Raumhintergrund. Offen verwendet standardmäßig Rot, geschlossen Grün und dessen Änderungszeit Blau. Die Zuordnung folgt den Feldnamen; die vertauschte Zuordnung des Originals wird nicht übernommen. Statt des ioBroker-Themewerts `background.paper` gibt es eine eigene Hintergrundfarbe. **Allgemein → Ohne Karte** entfernt den äußeren Kartenhintergrund. Einstellungen bleiben in Projekt und Widget-Export erhalten.

Deine HA-Entität muss die JSON-Liste bereits bereitstellen; das Widget aggregiert keine einzelnen Fenstersensoren und schreibt keine HA-Zustände. Ein `heatingcontrol`-Adapter ist nicht erforderlich.

![Fensterstatus-Übersicht mit offenen und geschlossenen Räumen](/images/grafik-visual-studio/weather-heating-windows.png)

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

## Übersicht über Heizräume

Ab **0.1.190** zeigt dieses Widget eine fertige HTML-Raumtabelle, entsprechend dem Original-Datenpunkt `RoomStatesHtmlTable`. Unter **Raumtabelle** wählst du eine HA-Entität und optional ein **Tabellenattribut**. Ohne Attribut wird der Zustand gelesen. Bei einer Bindung verwendet das Widget ausschließlich diesen Live-Wert; fehlende oder nicht verfügbare Werte zeigen **Keine Raumtabelle verfügbar**. Ohne Entitätsbindung lässt sich **Vorschau-Raumtabelle (HTML)** bearbeiten, auch über den HTML-Editor.

Das Widget erzeugt keine Raumdaten oder Heizprofile und steuert keine Thermostate. Eine ioBroker-Instanz wie `heatingcontrol.0` wird nicht benötigt; die gewählte HA-Quelle muss die Tabelle bereits als HTML-String bereitstellen. Lange HTML-Inhalte gehören üblicherweise in ein Attribut statt in den Zustand.

**Allgemein → Ohne Karte**, **Farben → Überschriftenfarbe**, Größe und die gemeinsamen CSS-Einstellungen sind verfügbar. Tabellen, Textformatierung, Zellspannen und ausgewählte Farben/Abstände werden übernommen. Skripte, Ereignishandler, Formulare, Einbettungen und externe Ressourcen werden entfernt. Eingaben sind auf 200.000 Zeichen, die Darstellung auf 5.000 Knoten und 40 Verschachtelungsebenen begrenzt. Große Tabellen scrollen innerhalb des Widgets. Alle Einstellungen bleiben im Widget-/Projektexport erhalten.

![Heizraumübersicht mit Vorschautabelle](/images/grafik-visual-studio/weather-heating-rooms.png)

## METEORED-Wetter-Widget

Ab **0.1.191** findest du unter **Allgemein** die Optionen **Ohne Karte**, **Meteored-Widget-ID** und **Neuladen aktivieren**. Erstelle dein Widget bei [Meteored / daswetter.com](https://www.daswetter.com/widget/) und trage ausschließlich dessen ID ein, keinen vollständigen HTML-Code und keine URL. Erlaubt sind 1–128 Buchstaben, Ziffern, Unterstriche oder Bindestriche. Gib beim Anbieter die Domain frei, unter der du die Runtime tatsächlich aufrufst.

Die Runtime lädt den offiziellen Loader `https://api.meteored.com/widget/loader/ID` in einem separaten Frame. Internetzugriff und eine gültige Anbieter-Konfiguration sind erforderlich. **Neuladen aktivieren** ist standardmäßig eingeschaltet und lädt einmal pro Stunde neu. Ausschalten beendet den Timer; ID-Wechsel und Entfernen räumen den alten Timer auf. Normale Runtime-Neuzeichnungen starten den Frame und seinen Timer nicht erneut. Im Editor siehst du eine Konfigurationsvorschau; eine leere oder ungültige ID lädt nichts.

Der Frame hat `sandbox="allow-scripts"`; die Loader-Seite erhält dieselbe Sandbox über ihren HTTP-Header. Meteored-Code läuft damit ohne Zugriff auf den Studio-DOM. Das Widget benötigt keine HA-Entität und übernimmt Standort, Sprache und Gestaltung aus deiner Meteored-Konfiguration. Alle drei Optionen sowie Größe und CSS bleiben im Export erhalten. Eine vollständige Prüfung der Anbieteranzeige benötigt deine echte Widget-ID und freigegebene Domain.

![METEORED-Konfiguration im Editor](/images/grafik-visual-studio/weather-heating-meteored.png)

Der reproduzierbare Paketbau und das geprüfte Manifest stehen im [Quellcode](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/tree/master/ha_grafik_visual_studio/packages/weather-heating). Der [Paketvertrag](widget-pakete.md) beschreibt Schnittstelle 0.2.
