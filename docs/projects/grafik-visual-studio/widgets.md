---
title: Widget-Übersicht
---

# Widget-Übersicht

Der aktuelle Widget-Katalog enthält **51 Einträge in vier Gruppen**. Die Namen entsprechen der Palette im Editor. Widgets mit Entitätsbindung lesen in der Runtime den aktuellen Home-Assistant-Zustand; ohne Entität verwenden sie Vorschauwerte oder ausdrücklich konfigurierte Dockpunktwerte. Schreibzugriff ist auf die unten genannten Widgets und Entitätstypen begrenzt. Externe Zustandsänderungen werden derzeit alle fünf Sekunden abgefragt. Eigene Änderungen an einem Regler wirken sofort auf Number und SVG-Line, während der Schreibauftrag an Home Assistant läuft.

Die Namen der VIS2-inspirierten Widgets bleiben auch bei deutscher Oberfläche auf Englisch. Frühere deutsche Palettennamen können weiterhin als Suchbegriffe dienen. Bereits gespeicherte eigene Widget-Namen bleiben unverändert.

Ab Studio 0.1.135 bleibt der technische Widget-Name in der Editoroberfläche. Auf der Arbeitsfläche und in der Runtime erscheinen nur eigene Beschriftungen; neue Widgets starten ohne voreingestellten Titel. Das gilt zentral auch für zukünftige Widget-Pakete und die LineBox. Beim Laden älterer Projekte werden bisherige Standardtitel einmal entfernt. Individuelle Beschriftungen bleiben erhalten; anschließend kannst du auch einen früheren Standardtext ausdrücklich wieder eintragen.

**Schreibfähige Widgets:** Switch, Icon Toggle Button, Bool Checkbox, Bool Select, Bool SVG und Bool HTML (control) schalten gebundene `switch`-, `light`- oder `input_boolean`-Entitäten. Bulb on/off schaltet diese Entitäten oder setzt einen `input_number`-Helfer auf sein konfiguriertes Minimum/Maximum. Slider schreibt nur `input_number`; Input val schreibt `input_number` oder `input_text`. State Element schreibt im Schaltermodus Ein/Aus und im Buttonmodus den nächsten konfigurierten Wert an eine passende schaltbare Entität oder einen Zahlen-/Texthelfer. Bei einer unpassenden oder nicht verfügbaren Entität ist die Bedienung gesperrt. Die übrigen Widgets schreiben keinen HA-Zustand.

## HA Grafik – Basis (44)

| Widget | Aktuelle Funktion |
| --- | --- |
| Tabs | Ab Studio 0.1.116: 1–20 horizontale oder vertikale Reiter; horizontal Standard, zentriert oder Gesamtbreite. Pro Tab Titel, Symbol oder Bild, Symbolgröße/-farbe und Überlauf X/Y. Der Inhalt ist eine eigene Widget-Fläche oder eine vorhandene Projektseite. Nur der aktive Inhalt wird in der Runtime eingebettet; die Auswahl bleibt lokal im Browser gespeichert. |

### Tabs bearbeiten

Ab Studio 0.1.122 bietet die Haupteinstellung **Tabs** den Regler **Inaktive Reiter abdunkeln (%)** von 0 bis 90. Bei 0 bleiben die Farben unverändert, bei 90 bleiben 10 % Helligkeit. Hintergrund, Text und Symbol der inaktiven Reiter werden gemeinsam abgedunkelt; der aktive Reiter und der Tab-Inhalt bleiben unverändert. Die Einstellung gilt horizontal und vertikal und wird im Projekt gespeichert.

Ab Studio 0.1.121 stellst du in der Haupteinstellung **Tabs** die **Textfarbe aktiv** und **Textfarbe nicht aktiv** getrennt ein. Sie gelten für die Beschriftung aller Reiter, abhängig von der aktuellen Auswahl. Bleibt ein Wert leer, wird die bisherige **Tab-Farbe** verwendet. Die Symbolfarbe je Tab bleibt unabhängig; die Tab-Farbe bestimmt weiterhin die aktive Markierung.

**Überlauf X** und **Überlauf Y** bieten ab Studio 0.1.120 die Auswahl `none`, `visible`, `hidden`, `scroll`, `auto`, `initial` und `inherit`. `none` entfernt die eigene CSS-Vorgabe, `visible` lässt überstehenden Inhalt sichtbar, `hidden` schneidet ihn ab, `scroll` aktiviert Scrollleisten und `auto` zeigt sie bei Bedarf. `initial` verwendet den CSS-Ausgangswert, `inherit` übernimmt die Vorgabe des übergeordneten Elements. Ohne gespeicherte Auswahl bleibt `auto` der Standard. CSS kann die beiden Achsen gemeinsam beeinflussen, insbesondere wenn `visible` mit einer scrollbaren anderen Achse kombiniert wird.

Ab Studio 0.1.119 kannst du unter jedem **Tab [n]** die **Tab-Hintergrundfarbe** unabhängig einstellen. Sie färbt den jeweiligen Reiter in horizontalen und vertikalen Layouts; die Markierung des aktiven Tabs bleibt sichtbar.

Füge **Tabs** aus der Palette ein und stelle Breite und Höhe einmal am Hauptwidget ein. In **Tab [1]**, **Tab [2]** usw. wählst du die Inhaltsart. **Tabfläche bearbeiten** öffnet die eigene Fläche mit der normalen Widget-Palette oder die referenzierte Projektseite. **Zurück zum Tabs-Widget** führt zum Hauptwidget zurück. Die eigene Inhaltsgröße ergibt sich aus dem Hauptwidget abzüglich 44 px für horizontale Reiter beziehungsweise bis zu 120 px für vertikale Reiter (höchstens die halbe Widget-Breite). Eigene Flächen gehören zum Widget und erscheinen nicht als separate Projektseiten. Vorhandene Seiten bleiben gemeinsam genutzte Referenzen; Änderungen wirken auf alle Einbettungen.

Ab Studio 0.1.124 werden aktive Tab-Inhalte direkt aus dem geöffneten Projekt dargestellt, ohne einen iFrame oder erneutes Laden beim Tabwechsel. Ein Klick auf die Inhaltsfläche öffnet ihre Bearbeitung; nach der Rückkehr sind auch ungespeicherte Änderungen sofort sichtbar. Speichere weiterhin vor dem Öffnen einer separaten Runtime, insbesondere bei deaktiviertem Auto-Save. Die Runtime fragt Entitätswerte auch für die aktiven Tab-Inhalte ab. Größere vorhandene Seiten werden ohne automatische Skalierung angezeigt; Überlauf X/Y steuert die Scrollbarkeit. Bei verringerter Tabanzahl bleiben die ausgeblendeten eigenen Inhalte gespeichert und erscheinen bei erneuter Erhöhung wieder. Kopieren, Gruppieren sowie Export/Import erhalten eigene Inhalte; Kopien bekommen neue Widget- und Gruppen-IDs. Zyklische Seiteneinbettungen werden verhindert. Weitere Tabs-Widgets innerhalb eigener Tabflächen sind zunächst nicht unterstützt. Die Umsetzung ist eigenständig; ein VIS2-Import ist damit nicht verbunden.

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
| Number | Zeigt den formatierten Zahlenwert mit Multiplikator und Nachkommastellen, bei fehlendem Entitätswert `--`. Ab Studio 0.1.125 werden **HTML voranstellen** und **HTML anhängen (Singular/Plural)** auch bei gebundener HA-Entität im Editor und in der Runtime angezeigt und bei Sofortaktualisierungen erhalten. Singular gilt für den mit dem Multiplikator berechneten Wert 1, sonst Plural; ohne HTML-Nachtext dient die konfigurierte Einheit als Ersatz. Der Vorschautitel wird ohne Entität angezeigt. Getrennt vom grafischen Widget „Red Number“. |
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
| Bool HTML | Zeigt je nach Zustand einen von zwei HTML-Inhalten, mit optionalem HTML davor und dahinter. |
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

### Table

**Static JSON (ohne ID)** enthält ein Array von Zeilenobjekten. Eine gebundene HA-Entität liefert stattdessen ihren JSON-Zustand in der Runtime. Beim Beispiel `[{"Title":"first","Value":1,"_Description":"Value1"},{"Title":"second","Value":2,"_Description":"Value2"}]` erscheinen die Spalten **Title** und **Value**. Attribute mit `_` bleiben als Metadaten verborgen; `_btn…` erzeugt eine Bestätigungsschaltfläche. Zellen dürfen HTML enthalten, das vor der Anzeige bereinigt wird.

**Kolumnanzahl** blendet Einstellungen für Spaltentitel, CSS-Breite und Attributzuordnung ein. Eine ausdrückliche Attributzuordnung kann auch Metadaten anzeigen. **Kein Header**, **Zeige Scrollbar** und **Maximale Zeilenanzahl** steuern die Darstellung. Neue Tabellen starten mit deaktivierten CSS-Bereichen. Ein Druckbutton erscheint erst mit einem Text in **btn_print**; **view_for_print** wählt optional die Druckseite.

**Ereignis ID** liest einzelne JSON-Zeilen. Der anfänglich vorhandene Zustand wird nicht als neues Ereignis übernommen. Änderungen ergänzen die Ereignisliste; gleiche `_id` ersetzen eine vorhandene Ereigniszeile. **Neues Ereignis am Anfang** gilt für diese Ereignisliste und dreht die Grundtabelle nicht um. Ereignisse und Auswahl gelten für die laufende Runtime-Sitzung.

Eine Zeilenauswahl schreibt das Zeilenobjekt als JSON in **Ausgewählt ID** (`input_text`) und zeigt `_detail` im **Detailed widget**. Bestätigungsbuttons schreiben `_ack_id` oder das Zeilenobjekt in **Bestätigung ID**. HA-Ziele müssen verfügbare, passende Zahlen-/Texthelfer sein; deren Typ- und Längenlimits gelten weiterhin. Im Editor werden keine HA-Werte geschrieben.

### Bool Checkbox

Die Checkbox zeigt den Zustand der gebundenen Home-Assistant-Entität. In der Runtime kann sie `switch`, `light` und `input_boolean` schalten; ohne verfügbare, passende Entität ist sie gesperrt. Im Editor dient sie nur als Vorschau.

**HTML voranstellen** und **HTML anhängen** ergänzen die Checkbox um Text oder HTML. **Autofokus** gilt nur in der Runtime. Neue Widgets beginnen mit leeren HTML-Feldern, deaktiviertem Autofokus und deaktivierten CSS-Bereichen. Bestehende Einstellungen bleiben erhalten.

### Bool HTML

Ab **0.1.146** stehen **HTML voranstellen**, **HTML anhängen**, **HTML bei 'false'** und **HTML bei 'true'** zur Verfügung, jeweils mit HTML-Editor. Der Entitätszustand wählt den Inhalt; ohne Entität dient **Testzustand** als Vorschau. Boolean `true`, Zahl `1` sowie die Texte `true`, `on`, `ein`, `yes` und `1` wählen den true-Inhalt; andere Zustände wählen false. Vorangestelltes und angehängtes HTML erscheinen unabhängig davon. Die Studio-HTML-Bereinigung gilt für alle vier Felder.

Neue Widgets beginnen mit leeren HTML-Feldern und deaktivierten CSS-Bereichen. Bereits konfigurierte Inhalte bleiben erhalten. **Bool HTML** zeigt nur an und schaltet keine Entität; dafür gibt es **Bool HTML (control)**.

### ValueList HTML

Ab **0.1.144** wählt **Testwert (nur Editor)** einen Index aus den vorhandenen Listeneinträgen. **Livewert / Vorschauzustand** zeigt auch im Editor den normalen Widgetzustand. Ein Testwert ändert weder den gespeicherten Vorschauzustand noch den HA-Wert; die Runtime verwendet immer den gebundenen Entitätszustand beziehungsweise den ungebundenen Vorschauzustand.

Trenne Einträge mit Semikolon oder Zeilenumbrüchen: `Test;test2;test3` ergibt die Indizes 0, 1 und 2. Kommas bleiben Teil des Textes: `Test, test2, test3` ist ein Eintrag. Schreibe ein Semikolon innerhalb eines HTML-Eintrags als `§§`, etwa in einem CSS-Stil oder einer HTML-Entität. **HTML voranstellen** und **HTML anhängen** umgeben den ausgewählten Eintrag; HTML wird nach den Studio-Regeln bereinigt. Fehlende, ungültige oder außerhalb der Liste liegende Zustände zeigen keinen Listeneintrag. Neue ValueList-HTML-Widgets haben alle CSS-Bereiche standardmäßig deaktiviert; bestehende Einstellungen bleiben erhalten.

### ValueList HTML Style

Ab **0.1.145** bietet das Widget einzelne Bereiche **Wert [0]** bis **Wert [n]** mit HTML-Inhalt und zugehörigem CSS-Stil. **Werteanzahl bis** ist der höchste Index: `2` ergibt drei Einträge, `0` genau einen. Studio erlaubt maximal Index 50. Vorhandene Listenfelder aus älteren Projekten dienen weiterhin als Fallback.

**Testwert (nur Editor)** wählt einen Eintrag ausschließlich für die Vorschau. Die Runtime liest den Index aus der gebundenen Entität oder dem ungebundenen Vorschauzustand; `true` und `false` entsprechen 1 und 0. Der Index ist kein Messwertbereich: Bei Einträgen `10`, `20`, `30` zeigt Zustand `2` den Text `30`; Zustand `30` liegt außerhalb einer Liste bis Index 2 und zeigt keinen Eintrag.

Der Stil gilt auch für das vorangestellte und angehängte HTML. Verwende vollständige CSS-Deklarationen, zum Beispiel `font-weight: bold; color: #29c8b5; font-size: 20px;`. `bold` allein hat keine Wirkung. Studio akzeptiert die freigegebenen Darstellungsstile ohne externe CSS-URLs. Allgemeine CSS-Bereiche sind bei neuen Widgets deaktiviert; die Stile der einzelnen Werte bleiben davon unabhängig nutzbar.

## HA Grafik – Interaktiv (1)


| Widget | Aktuelle Funktion |
| --- | --- |
| State Element | Bis zu fünf Zustände mit jeweils Icon, Bild, Text oder HTML; Schalter-, Button-, Nur-Anzeige- und Navigationsmodus. Liest eine gebundene Entität und kann im Schalter-/Buttonmodus passende Entitäten schreiben. |

## HA Grafik – Datenfluss (3)

| Widget | Aktuelle Funktion |
| --- | --- |
| [Wert-Verbindung](./datenfluss) | Gerichtete interne Wertübertragung; einfache Linie im Editor, unsichtbar in der Runtime. |
| [Wert-Konverter](./datenfluss) | Konvertiert Zahlen, Text, Schaltzustände und Einheiten mit eigenem Dialog und Typvorschau; unsichtbar in der Runtime. |
| [Wert-Berechnung](./datenfluss) | Gleiche vier Rechnungen wie SVG LineBox Math; standardmäßig unsichtbar in der Runtime. |

## HA Grafik – Spezial (3)

| Widget | Aktuelle Funktion |
| --- | --- |
| [SVG-Line](./svg-line) | Zeichnet und animiert Verbindungen zwischen Widgets, mit Andockpunkten, manuellem Mehrpunktpfad und gezielter Kopplung über Sammelpunkte. |
| [SVG LineBox Math](./svg-linebox-math) | Sichtbares Quadrat mit 16 Anschlüssen A–P. Eigene Formel oder Durchschnitt belegter Eingänge; Mehrfachbelegung wird je Anschluss summiert. Interne Wertweitergabe ohne zusätzliche HA-Entität. |
| [SVG LineBox](./svg-linebox) | Im Editor sichtbarer Verteiler: Zahlenwerte eingehender Linien summieren und an Ausgangslinien sowie optional an einen HA-Zahlenhelfer weitergeben. Ein einstellbarer Kreis verdeckt in der Runtime die verbundenen Linienenden. |
