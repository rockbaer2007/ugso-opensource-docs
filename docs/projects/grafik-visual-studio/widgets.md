---
title: Widget-Übersicht
---

# Widget-Übersicht

Der aktuelle Widget-Katalog enthält **46 Einträge in drei Gruppen**. Die Namen entsprechen der Palette im Editor. Einige Widgets verwenden derzeit Testwerte oder ändern Zustände nur lokal; eine vollständige Home-Assistant-Live-Anbindung ist noch nicht vorhanden. Ein Feld für eine Entity-ID allein bedeutet daher noch keine Steuerung der Entität.

Die Namen der VIS2-inspirierten Widgets bleiben auch bei deutscher Oberfläche auf Englisch. Frühere deutsche Palettennamen können weiterhin als Suchbegriffe dienen. Bereits gespeicherte eigene Widget-Namen bleiben unverändert.

## HA Grafik – Basis (43)

| Widget | Aktuelle Funktion |
| --- | --- |
| link | Formatierbarer HTML-Inhalt als Link zu einer URL. |
| Note | Notizzettel mit Text beziehungsweise HTML und optional ausgeblendeter Ecke. |
| Screen Resolution | Zeigt die aktuelle Fensterauflösung an. |
| Red Number | Zahlenwert als farbiger Kreis oder Pin mit anpassbarem Radius. |
| Bool SVG | Wählt je nach Testzustand eines von zwei SVG-Motiven. |
| SVG shape | Zeichnet eine geometrische SVG-Form mit Farbe, Strichbreite, Rotation und Skalierung. |
| Input val | Lokales Text- oder Zahlen-Eingabefeld mit Darstellungs- und Eingabeoptionen. |
| View in widget | Bettet eine Projektseite ein; rekursive Einbettung wird verhindert. |
| View in widget 8 | Wählt eine von bis zu 50 Seiten anhand eines Index-Testwerts. |
| iFrame | Bettet eine URL ein, sofern die Zielseite dies erlaubt; mit Rahmen-, Scroll- und Aktualisierungsoptionen. |
| iFrame 8 | Wählt anhand eines Index-Testwerts einen von bis zu 20 konfigurierten Frames. |
| Image 8 | Wählt anhand eines Index-Testwerts eines von bis zu 50 Bildern. |
| AckFlag HTML | Zeigt zwei konfigurierbare HTML-Zustände; Home Assistant hat kein natives ioBroker-`ack`-Flag. |
| Icon Toggle Button | Schaltfläche mit getrennten Bildern für Ein und Aus; Zustandswechsel derzeit lokal. |
| Switch | Grafischer Ein/Aus-Schalter; Zustandswechsel derzeit lokal. |
| Bool Checkbox | Ein/Aus-Auswahl; Zustandswechsel derzeit lokal. |
| Bulb on/off | Lampensymbol mit getrennten Ein-/Aus-Bildern; Zustandswechsel derzeit lokal. |
| Slider | Regler mit Minimum, Maximum und Schrittweite; Wertänderung derzeit lokal. |
| Number | Zahl mit Einheit, Multiplikator, Nachkommastellen und Vor-/Nachsilbe; getrennt vom grafischen Widget „Red Number“. |
| String | Textwert mit optionalem Icon und HTML vor oder nach dem Wert. |
| String (unescaped) | Stellt einen HTML-Testwert mit Vor- und Nachsatz dar. |
| String img src | Zeigt ein Bild aus einer URL im Testwert. |
| TimesValue | Formatiert einen Zeitwert aus dem Testzustand. |
| Timestamp Value | Formatiert einen Zeitstempel aus dem Testzustand. |
| Timestamp | Formatiert den hinterlegten Zeitpunkt der letzten Aktualisierung. |
| Last change Timestamp | Formatiert den hinterlegten Zeitpunkt der letzten Änderung. |
| ValueList Text | Zeigt einen ausgewählten Listeneintrag als Text. |
| ValueList HTML | Zeigt einen ausgewählten Listeneintrag als HTML. |
| ValueList HTML Style | Zeigt einen HTML-Listeneintrag mit zugeordnetem CSS-Stil. |
| Bool HTML | Zeigt je nach Testzustand einen von zwei HTML-Inhalten. |
| Bool Select | Auswahlfeld für Ein/Aus mit anpassbaren Beschriftungen. |
| Bool HTML (control) | Anklickbare Ein/Aus-HTML-Anzeige; Wechsel derzeit lokal. |
| HTML State | Eigener HTML-Inhalt mit optionalem Klick-Link und Wertplatzhalter. |
| Table | Tabelle aus JSON-Testdaten mit Zeilenauswahl und Druckoption. |
| Full Screen | Schaltfläche für den Vollbildmodus der Oberfläche. |
| Bar | Horizontaler oder vertikaler Balken für einen Testwert. |
| HTML | Frei konfigurierbarer HTML-Inhalt. |
| HTML navigation | Schaltfläche oder Link zu einer Projektseite, URL oder einem HA-Pfad. |
| filter - dropdown | Filtert Runtime-Widgets anhand des in „Generell“ gesetzten Filterworts. |
| Text | Freies Textfeld ohne Entitätsbindung. |
| Border | Rahmen mit Titel, Titelposition, Kopfbereich und Farben. |
| Gauge | Einfache Messwertanzeige mit Einheit. |
| Image | Zeigt eine konfigurierbare Bildquelle; noch keine Live-Kamera-Anbindung. |

## HA Grafik – Interaktiv (1)

| Widget | Aktuelle Funktion |
| --- | --- |
| State Element | Bis zu fünf Testzustände mit jeweils Icon, Bild, Text oder HTML; Schalter-, Button-, Nur-Anzeige- und Navigationsmodus. Die lokale Runtime-Interaktion ist vorhanden, HA-Schreibzugriff noch nicht. |

## HA Grafik – Spezial (2)

| Widget | Aktuelle Funktion |
| --- | --- |
| [SVG-Line](./zeichnen) | Zeichnet und animiert Verbindungen zwischen Widgets, mit Andockpunkten, manuellem Mehrpunktpfad und gezielter Kopplung über Sammelpunkte. |
| [Linebox](./zeichnen#linebox-als-unsichtbarer-verteiler) | Im Editor sichtbarer, in der Runtime unsichtbarer Verteiler: aktive Andockpunkte als Eingang, Nullstellung oder Ausgang festlegen, Zahlenwerte eingehender Linien summieren und optional an Ausgangslinien weitergeben. |
