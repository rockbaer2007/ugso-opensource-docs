---
title: Widget-Übersicht
---

# Widget-Übersicht

Der aktuelle Widget-Katalog enthält **52 Einträge in vier Gruppen**. Die Namen entsprechen der Palette im Editor. Widgets mit Entitätsbindung lesen in der Runtime den aktuellen Home-Assistant-Zustand; ohne Entität verwenden sie Vorschauwerte oder ausdrücklich konfigurierte Dockpunktwerte. Schreibzugriff ist auf die unten genannten Widgets und Entitätstypen begrenzt. Externe Zustandsänderungen werden derzeit alle fünf Sekunden abgefragt. Eigene Änderungen an einem Regler wirken sofort auf Number und SVG-Line, während der Schreibauftrag an Home Assistant läuft.

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
| Bool SVG | Wählt nach dem aktuellen Zustand eines von zwei SVG-Motiven; kann eine schaltbare Entität oder einen passenden 0/1-Helfer steuern. |
| SVG shape | Zeichnet eine geometrische SVG-Form mit Farbe, Strichbreite, Rotation und Skalierung. |
| Input val | Text- oder Zahlen-Eingabefeld (150 × 70). Zahlenmodus mit optionalem min/max; Nur-lesend erlaubt auch Sensoren. Enter bestätigt immer. Auto-setzen schreibt nach der einstellbaren Eingabepause (Standard 1000 ms), auch mit withEnter. withEnter ergänzt eine Bestätigungstaste für ungesendete Eingaben. Ohne Auto-setzen schreibt das Verlassen des Feldes nichts. Schreibziele sind passende `input_number`-/`input_text`-Helfer; ohne Entität bleibt die Eingabe lokal. |
| View in widget | Bettet eine Studio-Projektseite ein (Standard 300 × 200); rekursive Einbettung wird verhindert. Für HA-Dashboards gibt es ein eigenes Widget unter Spezial. |
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
| HTML State | HTML-Schaltfläche, die bei jedem Klick einen festen Wert schreibt und optional eine URL aufruft. |
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

Die folgenden Bilder stammen aus deutschen Testprojekten. Frühere CSS-Häkchen sind in den Bildunterschriften gekennzeichnet; maßgeblich ist das im Text beschriebene aktuelle Verhalten.

### CSS-Vorgaben

![Verpflichtendes CSS Allgemein und optionale CSS-Bereiche](/images/grafik-visual-studio/html-navigation-css.png)

*CSS Allgemein ist angehakt und gesperrt; die übrigen CSS-Gruppen sind optional.*

Ab **0.1.154** bleibt **CSS Allgemein** bei allen Widgets verpflichtend aktiv, einschließlich bereits gespeicherter Projekte und zukünftiger Widget-Pakete. Position und Größe bleiben damit im Export erhalten. Frühere Hinweise auf deaktivierte CSS-Bereiche gelten ab dieser Version nur für die übrigen CSS-Gruppen.

### Input val / Eingegebener Wert

Ab **0.1.157** bietet der Zahlenmodus optionale **min/max**. **Auto-setzen** übernimmt nach der eingestellten Pause, standardmäßig **1000 ms**, auch bei aktiviertem **withEnter**. Enter bestätigt immer. **withEnter** ergänzt eine Bestätigungstaste für ungesendete Änderungen; ohne Auto-setzen schreibt das Verlassen des Feldes nichts. Manuelle Eingaben bleiben bis zur Bestätigung erhalten. Nur-lesend kann auch Sensorwerte anzeigen; zum Schreiben von Zahlen/Text sind passende `input_number`-/`input_text`-Helfer nötig. Im Editor wird nie nach HA geschrieben.

![Detail der Eingabeeinstellungen mit Zahlengrenzen und Auto-setzen](/images/grafik-visual-studio/input-value.png)

*Ausschnitt der Eingabeeinstellungen: min/max 0–1000, Verzögerung 1000 ms und Nur-lesend aktiviert.*

Mit Style sind „HTML voranstellen“ die Feldbeschriftung und „HTML anhängen“ der Hilfstext unter dem Feld. **Kein Style** zeigt stattdessen bereinigtes HTML vor und hinter einem einfachen Eingabefeld. Die Varianten sind standard, outlined und filled. Leere, ungültige oder außerhalb von min/max liegende Zahlen werden nicht geschrieben. Neue Widgets aktivieren nur CSS Allgemein; die Umsteigerhinweise lassen sich zentral abschalten.

### String / Zeichenfolge

![String-Vorschau mit 43-Pixel-Lampensymbol und formatierten Vor- und Nachtexten](/images/grafik-visual-studio/string.png)

*Editorbeispiel mit 43-px-Symbol, fettem Vorsatz und kursivem Nachsatz; der Quellwert bleibt normaler Text.*

[Bild in voller Größe öffnen](/images/grafik-visual-studio/string.png)

Ab **0.1.156** haben **HTML voranstellen**, **HTML anhängen** und **Testtext** den HTML-Editor. Der Entitätswert und Testtext werden trotzdem als normaler Text dargestellt: `<b>Test</b>` im Testtext zeigt die Tags wörtlich. Nur Vor- und Nachsatz werden als bereinigtes HTML formatiert. Ein nicht leerer Testtext übersteuert die Quelle im Editor; in der Runtime gilt die Quelle. Ohne Entität bleibt der Runtime-Wert leer, fehlende Entität oder fehlendes Attribut ergibt `--`.

Für den ioBroker-Datenpunkt `…attribute.friendly_name` wählst du die zugehörige **Home-Assistant-Entität** und trägst unter **HA-Attribut (leer: Zustand)** `friendly_name` ein. Ein leeres Attributfeld zeigt den Zustand. Dafür ist kein Helfer nötig; die Auswahl liest nur. Der optionale Ausgangspunkt gibt denselben Quellwert weiter, ohne Vor-/Nachsatz oder Editor-Testtext.

**Icon** verwendet die vorhandene Icon-/Bildauswahl. **Symbolgröße in Pixel** erscheint nur bei gewähltem Icon, bietet 5–200 px und startet bei 24 px. Der Exportwert `43` ergibt ein 43 × 43 px großes Symbol. Neue Widgets starten mit leeren Inhalten, 100 × 30 px und ausschließlich aktiviertem CSS Allgemein; für größere Symbole die Widget-Höhe entsprechend anpassen. Die Umsteigerhinweise zu Attributen und Testtext sind zentral abschaltbar.

### HTML

![HTML-Editor mit Aktualisierungsintervall](/images/grafik-visual-studio/html.png)

*Frühere HTML-Testansicht mit 500-ms-Intervall. Seit 0.1.154 bleibt CSS Allgemein verpflichtend aktiv.*

**HTML** zeigt eigenen HTML-Inhalt mit dem vorhandenen HTML-Editor. `<b>Hallo</b><i> Susi</i>` ergibt **Hallo** und ein kursives *Susi*. **Updatezeit (ms)** baut diesen Inhalt im eingestellten Abstand neu auf; `0`, leer oder `null` deaktiviert die periodische Aktualisierung. Der Bereich reicht bis 180000 ms in Schritten von 100 ms. Dies ist keine HA-Abfragezeit und benötigt keinen Helfer.

Studio bereinigt das HTML: Eingebettete Skripte und Event-Handler werden nicht ausgeführt. Das unterscheidet sich vom VIS2-Original und wird als abschaltbarer Umsteigerhinweis erklärt. `{value}` ist kein Platzhalter. Neue Widgets beginnen mit leerem HTML, 200 × 130 px und ausschließlich aktiviertem CSS Allgemein; vorhandene Inhalte bleiben erhalten. Der optionale Ausgangspunkt ist weiterhin verfügbar.

### HTML navigation

**HTML** ist die frei formatierbare Beschriftung; **View zum Navigieren** wählt eine Projektseite. Ein Klick oder Enter/Leertaste wechselt nur in der Runtime dorthin, ohne HA-Schreibziel oder Helfer. Ohne Ziel bleibt die Beschriftung sichtbar. Neue Widgets starten mit leerem HTML, 200 × 130 px und nur **CSS Allgemein** aktiviert. Gespeicherte URL-/HA-Pfad-Ziele und alte Beschriftungen bleiben nutzbar.

**Unteransicht** aus VIS2 ist für spezielle Navigationssysteme wie Jaeger Design vorgesehen und in Studio noch nicht angebunden; das Feld ist deaktiviert. Es bezeichnet keinen Studio-Tab. Die abschaltbaren Umsteigerhinweise erklären diese Einschränkung und die HTML-Bereinigung.

### filter - dropdown

![Filtereditor mit HEX-Farben und Standardauswahl](/images/grafik-visual-studio/filter-editor.png)

*Zwei Einträge: Der erste hat ein Icon und HEX-Farben, der zweite ist die Standardauswahl.*

[Bild in voller Größe öffnen](/images/grafik-visual-studio/filter-editor.png)

Ab **0.1.155** bearbeitet **editor → Bearbeiten** die Einträge mit Wert, Titel, Symbol, Bild, Textfarbe, aktiver Farbe und Standardauswahl. Einträge lassen sich hinzufügen, löschen und mit den Pfeiltasten im Dialog umsortieren. Bei Einfachauswahl kann nur ein Eintrag Standard sein; Mehrfachauswahl erlaubt mehrere. **Anwenden** übernimmt die Änderungen, **Abbrechen** verwirft sie.

Farben werden als **HEX** gespeichert: `rgba(120,112,160,1)` entspricht `#7870A0`, `rgba(65,77,25,1)` entspricht `#414D19`. Optional ist ein Alphakanal als `#RRGGBBAA` möglich. Das Farbfeld kann auch geleert werden. **Aktive Farbe** ist bei den Tasten die Textfarbe des ausgewählten Eintrags; der Hintergrund folgt der Variante. Symbol hat Vorrang vor Bild.

**Typ** bietet Dropdown-Menü, horizontale oder vertikale Tasten. Tasten haben outlined/contained/text; Dropdowns standard/outlined/filled sowie optional Name, Autofokus und Klein. Die Dropdown-Liste zeigt Icons/Bilder und unterstützt Tastaturbedienung. **Keine Option Kein Filter** blendet die Rücksetzoption aus; ihr Text ist ansonsten frei wählbar.

Filterwerte passen zu **Filterwort** der Widgets auf derselben Seite. Komma oder Semikolon im Wert kann mehrere Filterwörter ansprechen. Widgets ohne Filterwort bleiben sichtbar. Standardauswahl und Filterung gelten in der Runtime; im Editor bleiben die Widgets bearbeitbar. Jede Seite hat eine eigene Auswahl. Es wird kein HA-Helfer benötigt. Neue Filter starten mit leerer Eintragsliste, 200 × 50 px und nur CSS Allgemein aktiv. Bestehende einfache Listen bleiben verwendbar.

### Bar

![Umgekehrter blauer Balken mit Rand- und Schatteneinstellungen](/images/grafik-visual-studio/bar.png)

*Frühere Testansicht: Der umgekehrte Balken wächst von rechts. CSS Allgemein bleibt heute verpflichtend aktiv.*

[Bild in voller Größe öffnen](/images/grafik-visual-studio/bar.png)

**Bar** zeigt einen Zahlenwert innerhalb von **Minimum** und **Maximum** als farbigen Balken. Bei 0–1000 entspricht 300 einem Füllstand von 30 %. Werte außerhalb des Bereichs werden auf 0–100 % begrenzt; bei gleichem Minimum und Maximum bleibt der Balken leer. Eine HA-Sensorentität wie Solarleistung passt hier: Das Widget liest nur und benötigt keinen zusätzlichen Helfer.

Horizontal wächst der Balken von links, vertikal von oben. **Wert umkehren** wechselt den Ursprung zu rechts beziehungsweise unten; 30 % bleiben dabei 30 %. **Rand** erwartet CSS, etwa `2px solid blue`; die einzelne `2` aus dem Export ist keine vollständige Randdefinition. **Durchsichtigkeit (Schatten/CSS)** entspricht dem VIS2-Feld `shadow` und erwartet einen CSS-Schatten wie `2px 2px 4px #0008`, keinen Transparenzwert. Alte gespeicherte Studio-Deckkraftwerte bleiben wirksam.

Neue Balken starten blau, horizontal, mit 0–100, 200 × 130 px und ausschließlich aktiviertem CSS Allgemein. Umsteigerhinweise erklären die Felder und sind über **Umsteigerhinweise anzeigen** abschaltbar. Der optionale Ausgangspunkt bleibt verfügbar.

### HTML State

![HTML State mit festem Wert und Umsteigerhinweisen](/images/grafik-visual-studio/html-state.png)

*Das Beispiel zeigt Hallo und sendet off; die kleinen Hinweise erklären Schreibziele und Browser-URL-Aufrufe.*

**HTML** ist der angezeigte Inhalt. **Wert** ist ein fester Schreibwert: Bei jedem Klick wird derselbe Wert gesendet, unabhängig vom aktuellen Zustand. Dein Beispiel mit `Hallo` und `off` zeigt „Hallo“ und sendet bei jedem Klick einen Aus-Befehl an eine passende schaltbare HA-Entität. Ein Sensor ist kein Schreibziel. Zahlen benötigen einen passenden `input_number`-Helfer, Text einen `input_text`-Helfer; `switch`, `light` und `input_boolean` unterstützen passende Ein-/Aus-Werte. Nicht verfügbare oder ungeeignete Ziele werden nicht beschrieben.

**Rufe URL bei Klick** sendet optional einen HTTP(S)-GET-Aufruf vom Browser. Die Ansicht bleibt geöffnet. Dieser Aufruf funktioniert auch ohne HA-Schreibziel und wird nicht über einen ioBroker-Server ausgeführt; Browserregeln, HTTPS und Netzwerkzugriff gelten weiterhin. Eine undurchsichtige Browserantwort bestätigt nicht den Erfolg des Zielsystems. Im Editor werden weder Werte geschrieben noch URLs aufgerufen. In der Runtime sind Klick, Enter und Leertaste möglich.

Neue Widgets beginnen mit leeren Feldern und ausschließlich aktiviertem CSS Allgemein. Bisherige Inhalte bleiben erhalten; der alte Vorschauwert wird als fester Wert übernommen, solange kein neuer **Wert** gesetzt ist. HTML wird bereinigt angezeigt; `{value}` ist hier kein Platzhalter. Umsteigerhinweise an Entität und URL lassen sich zentral in den Einstellungen abschalten.

### Umsteigerhinweise

![Abschaltbarer roter Umsteigerhinweis unter einer Entität](/images/grafik-visual-studio/migration-hints.png)

*Bool-Select-Beispiel mit Hinweis unter der Entitätsauswahl. Diese Editorhinweise lassen sich zentral abschalten.*

Unter **Einstellungen → Allgemein → Umsteigerhinweise anzeigen** lassen sich die Hinweise zentral ein- und ausschalten. Die Auswahl wird pro Projekt gespeichert; standardmäßig sind sie aktiv. Sie stehen direkt unter betroffenen Editorfeldern und erklären passende HA-Schaltziele oder Helfer, JSON-/Indexquellen und noch nicht angebundene Extrasteuerung. Reine Anzeige benötigt keinen zusätzlichen Schreibhelfer. Die Texte sind 10 px groß, ohne Fettdruck, hellrot auf dunklem beziehungsweise dunkelrot auf hellem Editorhintergrund. In der Runtime erscheinen sie nicht.

### Table

![Tabelle mit den Spalten Title und Value](/images/grafik-visual-studio/table.png)

*Static-JSON-Beispiel: Die Metadaten _Description erscheinen nicht in den beiden sichtbaren Spalten.*

**Static JSON (ohne ID)** enthält ein Array von Zeilenobjekten. Eine gebundene HA-Entität liefert stattdessen ihren JSON-Zustand in der Runtime. Beim Beispiel `[{"Title":"first","Value":1,"_Description":"Value1"},{"Title":"second","Value":2,"_Description":"Value2"}]` erscheinen die Spalten **Title** und **Value**. Attribute mit `_` bleiben als Metadaten verborgen; `_btn…` erzeugt eine Bestätigungsschaltfläche. Zellen dürfen HTML enthalten, das vor der Anzeige bereinigt wird.

**Kolumnanzahl** blendet Einstellungen für Spaltentitel, CSS-Breite und Attributzuordnung ein. Eine ausdrückliche Attributzuordnung kann auch Metadaten anzeigen. **Kein Header**, **Zeige Scrollbar** und **Maximale Zeilenanzahl** steuern die Darstellung. Neue Tabellen starten mit nur CSS Allgemein aktiviert. Ein Druckbutton erscheint erst mit einem Text in **btn_print**; **view_for_print** wählt optional die Druckseite.

**Ereignis ID** liest einzelne JSON-Zeilen. Der anfänglich vorhandene Zustand wird nicht als neues Ereignis übernommen. Änderungen ergänzen die Ereignisliste; gleiche `_id` ersetzen eine vorhandene Ereigniszeile. **Neues Ereignis am Anfang** gilt für diese Ereignisliste und dreht die Grundtabelle nicht um. Ereignisse und Auswahl gelten für die laufende Runtime-Sitzung.

Eine Zeilenauswahl schreibt das Zeilenobjekt als JSON in **Ausgewählt ID** (`input_text`) und zeigt `_detail` im **Detailed widget**. Bestätigungsbuttons schreiben `_ack_id` oder das Zeilenobjekt in **Bestätigung ID**. HA-Ziele müssen verfügbare, passende Zahlen-/Texthelfer sein; deren Typ- und Längenlimits gelten weiterhin. Im Editor werden keine HA-Werte geschrieben.

### Bool Select

![Bool Select mit ausgewähltem Zustand Läuft](/images/grafik-visual-studio/bool-select.png)

*Runtime-Beispiel mit vorangestelltem Tor: und ausgewähltem Text Läuft.*

Das Auswahlfeld hat zwei Einträge mit **Text bei 'false'** und **Text bei 'true'**. Es liest boolesche und numerische Zustände: `0` gilt als false, andere Zahlen als true. HA-Zustände `off`/`on` werden passend zugeordnet. **HTML voranstellen**, **HTML anhängen** und **Autofokus** sind vorhanden; Autofokus gilt nur in der Runtime.

Eine Auswahl schreibt `0` oder `1` in einen passenden `input_number`- oder `input_text`-Helfer. Bei `switch`, `light` und `input_boolean` wird ein entsprechender HA-Schaltbefehl gesendet. Ungeeignete oder nicht verfügbare Ziele sind gesperrt. Ohne Entität ist eine lokale Runtime-Vorschau möglich; im Editor wird nicht geschrieben. Neue Widgets starten mit leeren Text-/HTML-Feldern, deaktiviertem Autofokus und ausschließlich aktiviertem CSS Allgemein. Bestehende Beschriftungen bleiben erhalten.

### Bool SVG

![Bool SVG mit Stern-Motiv und Nur Anzeige](/images/grafik-visual-studio/bool-svg.png)

Unter **Allgemein** stehen die HA-Entität, **Nur Anzeige**, **SVG bei false**, **SVG bei true** und **Durchsichtigkeit**. Die SVG-Felder lassen sich im Code-Editor bearbeiten. Neue Widgets sind 85 × 85 px groß und verwenden die beiden Stern-Motive der VIS2-Vorlage. SVG-Koordinaten und eigene `transform`-Angaben bleiben erhalten; die Widgetgröße skaliert den Inhalt nicht automatisch.

`false`, `off` und numerische Null wählen das false-Motiv; Zahlen ungleich Null das true-Motiv. Beim Schalten numerischer Werte gilt der VIS2-Schwellwert 0,5: darunter wird 1, ab 0,5 wird 0 geschrieben. Schaltbare HA-Entitäten erhalten Ein/Aus; Zahlen- oder Textwerte benötigen einen passenden `input_number`-/`input_text`-Helfer. **Nur Anzeige** verhindert das Schreiben, auch Sensoren können dann als Quelle dienen. Im Editor wird niemals geschaltet.

Die Durchsichtigkeit reicht von 0 bis 1. Im Editor bleiben mindestens 20 % sichtbar, damit das Widget bearbeitbar bleibt; in der Runtime gilt auch vollständige Transparenz. **CSS Allgemein** ist für Position und Größe aktiv, die übrigen CSS-Gruppen sind bei neuen Widgets deaktiviert. Die optionalen Umsteigerhinweise erklären die Schreibziele und das Verhalten der Durchsichtigkeit.

### Red Number

![Red Number mit HTML-Vortext und benutzerdefinierten Farben](/images/grafik-visual-studio/red-number.png)

*Vergrößerte Beispielanzeige mit lokalem Vorschauwert 125; Standardgröße neuer Widgets ist 52 × 30 px.*

Neue Widgets beginnen mit 52 × 30 px. **Allgemein** bietet die HA-Entität, **type** (Kreis/Pin), drei HTML-Felder mit Code-Editor, Hintergrund und beim Kreis zusätzlich Randfarbe sowie Grenzradius (0–100, Standard 16). Der Kreis verwendet einen 3-px-Rand; der Pin zeigt eine Markierungsform ohne Kreisrand. Farben werden über HEX-Farbwähler eingestellt; bestehende RGB(A)-Farben bleiben darstellbar.

**HTML voranstellen** steht vor der Zahl. Bei genau 1 gilt **HTML anhängen (Singular)**, sonst **HTML anhängen (Plural)**. Der Zahlenwert wird aus dem Zustand gelesen. In der Runtime wird die Anzeige bei 0, false oder fehlendem gültigen Zahlenwert ausgeblendet. Im Editor bleibt sie sichtbar; ohne Quelle erscheint `--`. Lange HTML-Texte benötigen eine entsprechend größere Widgetfläche.

Das Widget liest nur und benötigt keinen zusätzlichen HA-Helfer. Der vorhandene Ausgangspunkt bleibt als Wertquelle nutzbar, auch wenn die Null-Anzeige ausgeblendet ist. **CSS Allgemein** bleibt aktiv, übrige CSS-Gruppen starten deaktiviert. Der optionale Umsteigerhinweis erklärt das Ausblenden.

### SVG shape

![SVG shape mit Kreis und getrennten Skalierungsreglern](/images/grafik-visual-studio/svg-shape.png)

Die Form wird direkt als SVG gezeichnet; Bilddateien, HA-Entitäten oder zusätzliche Helfer werden nicht benötigt. Neue Widgets sind **100 × 100 px** groß. Unter **Allgemein** stehen Linie, Dreieck, Quadrat, Pentagon, Sechseck, Achteck, Kreis, Stern, Pfeil und benutzerdefiniertes Polygon zur Auswahl. Beim benutzerdefinierten Polygon wird zusätzlich die **Punkteanzahl** von 3 bis 20 angeboten; sie erzeugt ein regelmäßiges Polygon, keine frei eingegebenen Koordinaten.

**Linienfarbe** und **Füllfarbe** werden als HEX gewählt. Die **Linienbreite** reicht von 0 bis 100 (Standard 5), **Drehen** von 0 bis 360 Grad. **Breitenskala** und **Höhenskala** sind getrennt von 0 bis 1 in Schritten von 0,05 einstellbar. Drehung und Skalierung erfolgen um die Formmitte; bei der Linie gilt wie im VIS2-Vorbild nur die Drehung, ihre Strichbreite wird beim Vergrößern nicht mitskaliert.

Der Stern verwendet sich kreuzende Kanten, der Pfeil zeigt ohne Drehung nach oben. Die Strichbreite verkleinert den verfügbaren Radius von Kreis und Polygonen. Sehr breite Striche können kleine Formen vollständig ausfüllen; negative Radien werden verhindert. **CSS Allgemein** bleibt für Position und Größe aktiv; alle übrigen CSS-Gruppen sind bei neuen Widgets deaktiviert. Editor und Runtime zeichnen dieselbe Geometrie.

### Bool Checkbox

Die Checkbox zeigt den Zustand der gebundenen Home-Assistant-Entität. In der Runtime kann sie `switch`, `light` und `input_boolean` schalten; ohne verfügbare, passende Entität ist sie gesperrt. Im Editor dient sie nur als Vorschau.

**HTML voranstellen** und **HTML anhängen** ergänzen die Checkbox um Text oder HTML. **Autofokus** gilt nur in der Runtime. Neue Widgets beginnen mit leeren HTML-Feldern, deaktiviertem Autofokus und ausschließlich aktiviertem CSS Allgemein. Bestehende Einstellungen bleiben erhalten.

### Bool HTML

![Bool HTML mit Editoren für true und false](/images/grafik-visual-studio/bool-html.png)

*Frühere Testansicht der vier HTML-Felder. CSS Allgemein bleibt heute verpflichtend aktiv.*

Ab **0.1.146** stehen **HTML voranstellen**, **HTML anhängen**, **HTML bei 'false'** und **HTML bei 'true'** zur Verfügung, jeweils mit HTML-Editor. Der Entitätszustand wählt den Inhalt; ohne Entität dient **Testzustand** als Vorschau. Boolean `true`, Zahl `1` sowie die Texte `true`, `on`, `ein`, `yes` und `1` wählen den true-Inhalt; andere Zustände wählen false. Vorangestelltes und angehängtes HTML erscheinen unabhängig davon. Die Studio-HTML-Bereinigung gilt für alle vier Felder.

Neue Widgets beginnen mit leeren HTML-Feldern und ausschließlich aktiviertem CSS Allgemein. Bereits konfigurierte Inhalte bleiben erhalten. **Bool HTML** zeigt nur an und schaltet keine Entität; dafür gibt es **Bool HTML (control)**.

### ValueList HTML

Ab **0.1.144** wählt **Testwert (nur Editor)** einen Index aus den vorhandenen Listeneinträgen. **Livewert / Vorschauzustand** zeigt auch im Editor den normalen Widgetzustand. Ein Testwert ändert weder den gespeicherten Vorschauzustand noch den HA-Wert; die Runtime verwendet immer den gebundenen Entitätszustand beziehungsweise den ungebundenen Vorschauzustand.

Trenne Einträge mit Semikolon oder Zeilenumbrüchen: `Test;test2;test3` ergibt die Indizes 0, 1 und 2. Kommas bleiben Teil des Textes: `Test, test2, test3` ist ein Eintrag. Schreibe ein Semikolon innerhalb eines HTML-Eintrags als `§§`, etwa in einem CSS-Stil oder einer HTML-Entität. **HTML voranstellen** und **HTML anhängen** umgeben den ausgewählten Eintrag; HTML wird nach den Studio-Regeln bereinigt. Fehlende, ungültige oder außerhalb der Liste liegende Zustände zeigen keinen Listeneintrag. Neue ValueList-HTML-Widgets haben nur CSS Allgemein standardmäßig aktiviert; bestehende Einstellungen bleiben erhalten.

### ValueList HTML Style

Ab **0.1.145** bietet das Widget einzelne Bereiche **Wert [0]** bis **Wert [n]** mit HTML-Inhalt und zugehörigem CSS-Stil. **Werteanzahl bis** ist der höchste Index: `2` ergibt drei Einträge, `0` genau einen. Studio erlaubt maximal Index 50. Vorhandene Listenfelder aus älteren Projekten dienen weiterhin als Fallback.

**Testwert (nur Editor)** wählt einen Eintrag ausschließlich für die Vorschau. Die Runtime liest den Index aus der gebundenen Entität oder dem ungebundenen Vorschauzustand; `true` und `false` entsprechen 1 und 0. Der Index ist kein Messwertbereich: Bei Einträgen `10`, `20`, `30` zeigt Zustand `2` den Text `30`; Zustand `30` liegt außerhalb einer Liste bis Index 2 und zeigt keinen Eintrag.

Der Stil gilt auch für das vorangestellte und angehängte HTML. Verwende vollständige CSS-Deklarationen, zum Beispiel `font-weight: bold; color: #29c8b5; font-size: 20px;`. `bold` allein hat keine Wirkung. Studio akzeptiert die freigegebenen Darstellungsstile ohne externe CSS-URLs. Bei neuen Widgets ist nur CSS Allgemein standardmäßig aktiviert; die Stile der einzelnen Werte bleiben davon unabhängig nutzbar.

### View in widget 8

Seit **0.1.160** bettet dieses Widget abhängig vom Zustand einer HA-Entität eine **Studio-Projektseite** ein. Es liest nur; ein zusätzlicher HA-Helfer ist nicht erforderlich. Die auswählbaren Seiten werden unter **Seite [0]**, **Seite [1]** usw. zugeordnet. **Werteanzahl bis** ist der höchste Index: `1` ergibt zwei Einträge, `0` genau einen; Studio erlaubt maximal Index 50.

`false`/`off` wählt Index 0, `true`/`on` Index 1. Ganzzahlige Zustände wählen den entsprechenden Index. Leere, nicht verfügbare, gebrochene oder außerhalb der Liste liegende Werte wählen keine Seite. Ohne Entität gilt bei neuen Widgets Index 0. Der Editor zeigt die gewählte Seite als Textvorschau; die Runtime bettet sie ein. Ein unverändertes Ziel wird bei Zustandsaktualisierungen nicht neu geladen. Fehlende Seiten und rekursive Einbettungen werden verhindert.

Neue Widgets starten mit **300 × 200 Pixeln** und ausschließlich aktiviertem **CSS Allgemein**. Die zentral abschaltbaren Umsteigerhinweise erläutern Index und Seitenabhängigkeit. Im Widget-JSON-Export sind die referenzierten Projektseiten nicht enthalten; für den geplanten vollständigen Projekt-Export müssen sämtliche benötigten Seiten mitgeliefert werden. Das Widget ist von **Dashboard in widget** zu unterscheiden, das ein HA-Dashboard öffnet.

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

## HA Grafik – Spezial (4)

| Widget | Aktuelle Funktion |
| --- | --- |
| Dashboard in widget | Bettet ein HA-Dashboard in der Runtime ein. Größe 32–800 × 32–640 Pixel, Standard 300 × 200. Der Editor zeigt eine auswählbare Vorschau. |
| [SVG-Line](./svg-line) | Zeichnet und animiert Verbindungen zwischen Widgets, mit Andockpunkten, manuellem Mehrpunktpfad und gezielter Kopplung über Sammelpunkte. |
| [SVG LineBox Math](./svg-linebox-math) | Sichtbares Quadrat mit 16 Anschlüssen A–P. Eigene Formel oder Durchschnitt belegter Eingänge; Mehrfachbelegung wird je Anschluss summiert. Interne Wertweitergabe ohne zusätzliche HA-Entität. |
| [SVG LineBox](./svg-linebox) | Im Editor sichtbarer Verteiler: Zahlenwerte eingehender Linien summieren und an Ausgangslinien sowie optional an einen HA-Zahlenhelfer weitergeben. Ein einstellbarer Kreis verdeckt in der Runtime die verbundenen Linienenden. |

### Dashboard in widget

::: warning Export in eine externe Runtime
Für Visualisierungen innerhalb von Home Assistant vorgesehen. Wenn ein Export in die externe Runtime geplant ist, dieses Widget möglichst nicht verwenden. Das eingebundene Dashboard wird nicht mit exportiert und benötigt weiterhin Home Assistant sowie eine Browser-Anmeldung.

Seit **0.1.159** steht dieser Hinweis dauerhaft in den Widget-Einstellungen, unabhängig von „Umsteigerhinweise anzeigen“. Beim JSON-Export ausgewählter Widgets erscheint er ebenfalls, wenn ein Dashboard enthalten ist; eigene Tab-Flächen werden mitgeprüft. Der Dialog nennt die betroffenen Widgets und bietet **Trotzdem exportieren** oder **Abbrechen**. Exportiert wird nur die Dashboard-Bindung. Der vollständige Projekt-Export für die externe Runtime ist weiterhin geplant.
:::

![HA-Dashboard-Vorschau im Editor für lovelace Ansicht 0](/images/grafik-visual-studio/dashboard-widget.png)

*Editor-Vorschau für /lovelace/0. Das lokale Testbild zeigt kein angemeldetes HA-Dashboard.*

**Dashboard** öffnet über „…“ die Liste der HA-Dashboards. Alternativ lässt sich ein Pfad wie `/lovelace` oder `/dashboard-solar` direkt eingeben. **Dashboard-Ansicht** wählt optional einen Ansichtspfad oder eine Zahl, etwa `energie` oder `0`. Im HA-Ingress bleibt **HA-Basis-URL** leer. Bei direktem Studio-Zugriff wird dort die HA-Adresse eingetragen, beispielsweise `https://ha.example.org`.

Die Anmeldung nutzt die normale HA-Browsersitzung. Das Widget speichert keinen Token; die Dashboard-Auswahl gibt nur Titel und Pfade zurück. Andere Ursprünge können durch Browser- oder Einbettungsregeln blockiert werden. Eine erneute Anmeldung kann erforderlich sein. Normale Studio-Zustandsaktualisierungen laden ein bereits eingebettetes Dashboard nicht neu. Neue Widgets aktivieren nur CSS Allgemein; Umsteigerhinweise sind zentral abschaltbar. „View in widget“ bleibt für Studio-Seiten zuständig.
