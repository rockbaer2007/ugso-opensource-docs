---
title: Widget-Übersicht
---

# Widget-Übersicht

Der aktuelle Widget-Katalog enthält **45 Einträge in drei Gruppen**. Die Namen entsprechen der Palette im Editor. Einige Widgets verwenden derzeit Testwerte oder ändern Zustände nur lokal; eine vollständige Home-Assistant-Live-Anbindung ist noch nicht vorhanden. Ein Feld für eine Entity-ID allein bedeutet daher noch keine Steuerung der Entität.

## HA Grafik – Basis (43)

| Widget | Aktuelle Funktion |
| --- | --- |
| Link | Formatierbarer HTML-Inhalt als Link zu einer URL. |
| Note | Notizzettel mit Text beziehungsweise HTML und optional ausgeblendeter Ecke. |
| Screen Resolution | Zeigt die aktuelle Fensterauflösung an. |
| Red Number | Zahlenwert als farbiger Kreis oder Pin mit anpassbarem Radius. |
| Boolesches SVG | Wählt je nach Testzustand eines von zwei SVG-Motiven. |
| SVG Shape | Zeichnet eine geometrische SVG-Form mit Farbe, Strichbreite, Rotation und Skalierung. |
| Eingegebener Wert | Lokales Text- oder Zahlen-Eingabefeld mit Darstellungs- und Eingabeoptionen. |
| View in Widget | Bettet eine Projektseite ein; rekursive Einbettung wird verhindert. |
| View in widget 8 | Wählt eine von bis zu 50 Seiten anhand eines Index-Testwerts. |
| iframe | Bettet eine URL ein, sofern die Zielseite dies erlaubt; mit Rahmen-, Scroll- und Aktualisierungsoptionen. |
| iframe 8 | Wählt anhand eines Index-Testwerts einen von bis zu 20 konfigurierten Frames. |
| Image 8 | Wählt anhand eines Index-Testwerts eines von bis zu 50 Bildern. |
| AckFlag HTML | Zeigt zwei konfigurierbare HTML-Zustände; Home Assistant hat kein natives ioBroker-`ack`-Flag. |
| Schaltfläche (Icon Ein/Aus) | Schaltfläche mit getrennten Bildern für Ein und Aus; Zustandswechsel derzeit lokal. |
| Switch | Grafischer Ein/Aus-Schalter; Zustandswechsel derzeit lokal. |
| Checkbox | Ein/Aus-Auswahl; Zustandswechsel derzeit lokal. |
| Lampe ein/aus | Lampensymbol mit getrennten Ein-/Aus-Bildern; Zustandswechsel derzeit lokal. |
| Slider | Regler mit Minimum, Maximum und Schrittweite; Wertänderung derzeit lokal. |
| Zahlenwert | Zahl mit Einheit, Multiplikator, Nachkommastellen und Vor-/Nachsilbe. |
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
| Bool HTML-Steuerung | Anklickbare Ein/Aus-HTML-Anzeige; Wechsel derzeit lokal. |
| HTML State | Eigener HTML-Inhalt mit optionalem Klick-Link und Wertplatzhalter. |
| Table | Tabelle aus JSON-Testdaten mit Zeilenauswahl und Druckoption. |
| Full Screen | Schaltfläche für den Vollbildmodus der Oberfläche. |
| Bar | Horizontaler oder vertikaler Balken für einen Testwert. |
| HTML | Frei konfigurierbarer HTML-Inhalt. |
| HTML Navigation | Schaltfläche oder Link zu einer Projektseite, URL oder einem HA-Pfad. |
| Filter Dropdown | Filtert Runtime-Widgets anhand des in „Generell“ gesetzten Filterworts. |
| Text | Freies Textfeld ohne Entitätsbindung. |
| Rahmen | Rahmen mit Titel, Titelposition, Kopfbereich und Farben. |
| Messanzeige | Einfache Messwertanzeige mit Einheit. |
| Bild / Kamera | Zeigt eine konfigurierbare Bildquelle; noch keine Live-Kamera-Anbindung. |

## HA Grafik – Interaktiv (1)

| Widget | Aktuelle Funktion |
| --- | --- |
| Zustands-Element | Bis zu fünf Testzustände mit jeweils Icon, Bild, Text oder HTML; Schalter-, Button-, Nur-Anzeige- und Navigationsmodus. Die lokale Runtime-Interaktion ist vorhanden, HA-Schreibzugriff noch nicht. |

## HA Grafik – Spezial (1)

| Widget | Aktuelle Funktion |
| --- | --- |
| [SVG-Verbindungslinie („Zeichnen“)](./zeichnen) | Zeichnet und animiert Verbindungen zwischen Widgets, mit Andockpunkten, manuellem Mehrpunktpfad und gezielter Kopplung über Sammelpunkte. |
