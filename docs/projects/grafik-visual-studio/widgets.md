---
title: Widget-Übersicht
---

# Widget-Übersicht

Der aktuelle Widget-Katalog enthält **47 Einträge in drei Gruppen**. Die Namen entsprechen der Palette im Editor. Widgets mit Entitätsbindung lesen in der Runtime den aktuellen Home-Assistant-Zustand; ohne Entität verwenden sie Vorschauwerte. Schreibzugriff ist auf die unten genannten Widgets und Entitätstypen begrenzt. Externe Zustandsänderungen werden derzeit alle fünf Sekunden abgefragt. Eigene Änderungen an einem Regler wirken sofort auf Number und SVG-Line, während der Schreibauftrag an Home Assistant läuft.

Die Namen der VIS2-inspirierten Widgets bleiben auch bei deutscher Oberfläche auf Englisch. Frühere deutsche Palettennamen können weiterhin als Suchbegriffe dienen. Bereits gespeicherte eigene Widget-Namen bleiben unverändert.

**Schreibfähige Widgets:** Switch, Icon Toggle Button, Bool Checkbox, Bool Select, Bool SVG und Bool HTML (control) schalten gebundene `switch`-, `light`- oder `input_boolean`-Entitäten. Bulb on/off schaltet diese Entitäten oder setzt einen `input_number`-Helfer auf sein konfiguriertes Minimum/Maximum. Slider schreibt nur `input_number`; Input val schreibt `input_number` oder `input_text`. State Element schreibt im Schaltermodus Ein/Aus und im Buttonmodus den nächsten konfigurierten Wert an eine passende schaltbare Entität oder einen Zahlen-/Texthelfer. Bei einer unpassenden oder nicht verfügbaren Entität ist die Bedienung gesperrt. Die übrigen Widgets schreiben keinen HA-Zustand.

## HA Grafik – Basis (44)

| Widget | Aktuelle Funktion |
| --- | --- |
| Tabs | Ab Studio 0.1.116: 1–20 horizontale oder vertikale Reiter; horizontal Standard, zentriert oder Gesamtbreite. Pro Tab Titel, Symbol oder Bild, Symbolgröße/-farbe und Überlauf X/Y. Der Inhalt ist eine eigene Widget-Fläche oder eine vorhandene Projektseite. Nur der aktive Inhalt wird in der Runtime eingebettet; die Auswahl bleibt lokal im Browser gespeichert. |

### Tabs bearbeiten

Ab Studio 0.1.121 stellst du in der Haupteinstellung **Tabs** die **Textfarbe aktiv** und **Textfarbe nicht aktiv** getrennt ein. Sie gelten für die Beschriftung aller Reiter, abhängig von der aktuellen Auswahl. Bleibt ein Wert leer, wird die bisherige **Tab-Farbe** verwendet. Die Symbolfarbe je Tab bleibt unabhängig; die Tab-Farbe bestimmt weiterhin die aktive Markierung.

**Überlauf X** und **Überlauf Y** bieten ab Studio 0.1.120 die Auswahl `none`, `visible`, `hidden`, `scroll`, `auto`, `initial` und `inherit`. `none` entfernt die eigene CSS-Vorgabe, `visible` lässt überstehenden Inhalt sichtbar, `hidden` schneidet ihn ab, `scroll` aktiviert Scrollleisten und `auto` zeigt sie bei Bedarf. `initial` verwendet den CSS-Ausgangswert, `inherit` übernimmt die Vorgabe des übergeordneten Elements. Ohne gespeicherte Auswahl bleibt `auto` der Standard. CSS kann die beiden Achsen gemeinsam beeinflussen, insbesondere wenn `visible` mit einer scrollbaren anderen Achse kombiniert wird.

Ab Studio 0.1.119 kannst du unter jedem **Tab [n]** die **Tab-Hintergrundfarbe** unabhängig einstellen. Sie färbt den jeweiligen Reiter in horizontalen und vertikalen Layouts; die Markierung des aktiven Tabs bleibt sichtbar.

Füge **Tabs** aus der Palette ein und stelle Breite und Höhe einmal am Hauptwidget ein. In **Tab [1]**, **Tab [2]** usw. wählst du die Inhaltsart. **Tabfläche bearbeiten** öffnet die eigene Fläche mit der normalen Widget-Palette oder die referenzierte Projektseite. **Zurück zum Tabs-Widget** führt zum Hauptwidget zurück. Die eigene Inhaltsgröße ergibt sich aus dem Hauptwidget abzüglich 44 px für horizontale Reiter beziehungsweise bis zu 120 px für vertikale Reiter (höchstens die halbe Widget-Breite). Eigene Flächen gehören zum Widget und erscheinen nicht als separate Projektseiten. Vorhandene Seiten bleiben gemeinsam genutzte Referenzen; Änderungen wirken auf alle Einbettungen.

Speichere vor der Vorschau oder Runtime, insbesondere bei deaktiviertem Auto-Save: Die eingebetteten Inhalte werden aus dem gespeicherten Projekt geladen. Größere vorhandene Seiten werden ohne automatische Skalierung angezeigt; Überlauf X/Y steuert die Scrollbarkeit. Bei verringerter Tabanzahl bleiben die ausgeblendeten eigenen Inhalte gespeichert und erscheinen bei erneuter Erhöhung wieder. Kopieren, Gruppieren sowie Export/Import erhalten eigene Inhalte; Kopien bekommen neue Widget- und Gruppen-IDs. Zyklische Seiteneinbettungen werden verhindert. Weitere Tabs-Widgets innerhalb eigener Tabflächen sind zunächst nicht unterstützt. Die Umsetzung ist eigenständig; ein VIS2-Import ist damit nicht verbunden.

### Weitere Basis-Widgets

| Widget | Aktuelle Funktion |
| --- | --- |
| link | Formatierbarer HTML-Inhalt als Link zu einer URL. |
| Note | Notizzettel mit Text beziehungsweise HTML und optional ausgeblendeter Ecke. |
| Screen Resolution | Zeigt die aktuelle Fensterauflösung an. |
| Red Number | Zahlenwert als farbiger Kreis oder Pin mit anpassbarem Radius. |
| Bool SVG | Wählt nach dem aktuellen Zustand eines von zwei SVG-Motiven; kann eine schaltbare Entität steuern. |
| SVG shape | Zeichnet eine geometrische SVG-Form mit Farbe, Strichbreite, Rotation und Skalierung. |
| Input val | Umrandetes Text- oder Zahlen-Eingabefeld. Liest und schreibt in der Runtime einen gewählten `input_number`- oder `input_text`-Helfer; ohne Entität bleibt die Eingabe lokal. „Auto-setzen“ schreibt nach einer kurzen Eingabepause, „withEnter“ nur bei Enter. |
| View in widget | Bettet eine Projektseite ein; rekursive Einbettung wird verhindert. |
| View in widget 8 | Wählt eine von bis zu 50 Seiten anhand des Indexzustands. |
| iFrame | Bettet eine URL ein, sofern die Zielseite dies erlaubt; mit Rahmen-, Scroll- und Aktualisierungsoptionen. |
| iFrame 8 | Wählt anhand des Indexzustands einen von bis zu 20 konfigurierten Frames. |
| Image 8 | Wählt anhand des Indexzustands eines von bis zu 50 Bildern. |
| AckFlag HTML | Zeigt zwei konfigurierbare HTML-Zustände; Home Assistant hat kein natives ioBroker-`ack`-Flag. |
| Icon Toggle Button | Schaltfläche mit getrennten Bildern für Ein und Aus; kann eine schaltbare Entität steuern. |
| Switch | Grafischer Ein/Aus-Schalter; kann eine schaltbare Entität steuern. |
| Bool Checkbox | Ein/Aus-Auswahl; kann eine schaltbare Entität steuern. |
| Bulb on/off | Lampensymbol mit getrennten Ein-/Aus-Bildern; steuert eine schaltbare Entität oder einen Zahlenhelfer. |
| Slider | Regler mit Minimum, Maximum und Schrittweite; Min-/Max-Beschriftungen sind per Checkbox zuschaltbar. Die Grenzen sollten zum Helfer passen, etwa `-200` bis `200`. Ein gewählter `input_number`-Helfer liefert den aktuellen Wert; beim Ziehen aktualisiert der Regler abhängige Number- und SVG-Line-Widgets sofort und schreibt beim Loslassen nach Home Assistant. Ohne Entität bleibt die Änderung lokal. Ab Studio 0.1.114 sind Schienenfarbe, aktive Farbe, Schienenstärke und Rundung sowie Reglerfarbe, Größe und Rundung getrennt einstellbar. Der Spurtyp bietet Normal (Minimum bis Wert), Umgekehrt (Wert bis Maximum) oder keine aktive Spur. Schiene und Regler haben eigene Schatten mit X/Y-Versatz, Unschärfe, Ausdehnung und CSS-/RGBA-Farbe. Rundung: 0 % eckig, 100 % vollständig gerundet; Schatten mit allen Größenwerten 0 sind aus. Skalenmarkierungen bleiben oben/unten mit optionalen Zahlen verfügbar. |
| Number | Ohne Entität Vorschau mit Titel, Einheit, Multiplikator, Nachkommastellen und Vor-/Nachsilbe. Mit gewählter HA-Entität zeigt Editor und Runtime nur den formatierten aktuellen Zahlenwert; bei fehlendem Wert `--`. Getrennt vom grafischen Widget „Red Number“. |
| String | Textwert mit optionalem Icon und HTML vor oder nach dem Wert. |
| String (unescaped) | Stellt einen HTML-Wert mit Vor- und Nachsatz dar. |
| String img src | Zeigt ein Bild aus einer URL im Zustand. |
| TimesValue | Formatiert einen Zeitwert aus dem Zustand. |
| Timestamp Value | Formatiert einen Zeitstempel aus dem Zustand. |
| Timestamp | Formatiert den Zeitpunkt der letzten HA-Aktualisierung. |
| Last change Timestamp | Formatiert den Zeitpunkt der letzten HA-Zustandsänderung. |
| ValueList Text | Zeigt einen über den Indexzustand ausgewählten Listeneintrag als Text. |
| ValueList HTML | Zeigt einen über den Indexzustand ausgewählten Listeneintrag als HTML. |
| ValueList HTML Style | Zeigt einen HTML-Listeneintrag mit zugeordnetem CSS-Stil. |
| Bool HTML | Zeigt je nach Zustand einen von zwei HTML-Inhalten. |
| Bool Select | Ein/Aus-Auswahl mit anpassbaren Beschriftungen; kann eine schaltbare Entität steuern. |
| Bool HTML (control) | Anklickbare Ein/Aus-HTML-Anzeige; kann eine schaltbare Entität steuern. |
| HTML State | Eigener HTML-Inhalt mit optionalem Klick-Link und Wertplatzhalter. |
| Table | Tabelle aus JSON-Daten mit Zeilenauswahl und Druckoption; ein gebundener HA-Zustand muss JSON-Zeilen enthalten. |
| Full Screen | Schaltfläche für den Vollbildmodus der Oberfläche. |
| Bar | Horizontaler oder vertikaler Balken für einen Zahlenwert. |
| HTML | Frei konfigurierbarer HTML-Inhalt. |
| HTML navigation | Schaltfläche oder Link zu einer Projektseite, URL oder einem HA-Pfad. |
| filter - dropdown | Filtert Runtime-Widgets anhand des in „Generell“ gesetzten Filterworts. |
| Text | Freies Textfeld ohne Entitätsbindung. |
| Border | Rahmen mit Titel, Titelposition, Kopfbereich und Farben. |
| Gauge | Einfache Messwertanzeige mit Einheit. |
| Image | Zeigt eine konfigurierbare Bildquelle oder eine URL aus dem Entitätszustand; noch keine Live-Kamera-Anbindung. |

## HA Grafik – Interaktiv (1)

| Widget | Aktuelle Funktion |
| --- | --- |
| State Element | Bis zu fünf Zustände mit jeweils Icon, Bild, Text oder HTML; Schalter-, Button-, Nur-Anzeige- und Navigationsmodus. Liest eine gebundene Entität und kann im Schalter-/Buttonmodus passende Entitäten schreiben. |

## HA Grafik – Spezial (2)

| Widget | Aktuelle Funktion |
| --- | --- |
| [SVG-Line](./svg-line) | Zeichnet und animiert Verbindungen zwischen Widgets, mit Andockpunkten, manuellem Mehrpunktpfad und gezielter Kopplung über Sammelpunkte. |
| [SVG LineBox](./svg-linebox) | Im Editor sichtbarer Verteiler: Zahlenwerte eingehender Linien summieren und an Ausgangslinien sowie optional an einen HA-Zahlenhelfer weitergeben. Ein einstellbarer Kreis verdeckt in der Runtime die verbundenen Linienenden. |
