---
title: Widget-Übersicht
---

# Widget-Übersicht

Zusätzlich nachinstallierbar: [Wetter und Heizung](weather-heating.md) mit **Allgemeines Diagramm** (ab 0.1.187), **Balkendiagramm für zwei Wochen** (ab 0.1.188), **Wetter-Widget** (ab 0.1.189), **Übersicht über Heizräume** (ab 0.1.190), **METEORED-Wetter-Widget** (ab 0.1.191), **Fensterstatus-Übersicht** (ab 0.1.192), **Meinen Vermieter informieren** (ab 0.1.193) und **Allgemeine Heizparameter** (ab 0.1.194). Das optionale Paket zählt nicht zu den 74 integrierten Widgets und erhält automatisch eine freie Set-Farbe.

Der aktuelle Widget-Katalog enthält **74 Einträge in fünf Gruppen**. Die Namen entsprechen der Palette im Editor. Widgets mit Entitätsbindung lesen in der Runtime den aktuellen Home-Assistant-Zustand; ohne Entität verwenden sie Vorschauwerte oder ausdrücklich konfigurierte Dockpunktwerte. Schreibzugriff ist auf die unten genannten Widgets und Entitätstypen begrenzt. Externe Zustandsänderungen werden derzeit alle fünf Sekunden abgefragt. Eigene Änderungen an einem Regler wirken sofort auf Number und SVG-Line, während der Schreibauftrag an Home Assistant läuft.

Die VIS2-inspirierten Basis-Widgets behalten ihre englischen Namen. Interaktive Widgets wie Terminkalender und Schieberegler verwenden übersetzte Palettennamen. Frühere Palettennamen können weiterhin als Suchbegriffe dienen. Bereits gespeicherte eigene Widget-Namen bleiben unverändert.

**HTML Logout wird nicht übernommen** und ist nicht als zukünftiges Studio-Widget vorgesehen.

Ab Studio 0.1.135 bleibt der technische Widget-Name in der Editoroberfläche. Auf der Arbeitsfläche und in der Runtime erscheinen nur eigene Beschriftungen; neue Widgets starten ohne voreingestellten Titel. Das gilt zentral auch für zukünftige Widget-Pakete und die LineBox. Beim Laden älterer Projekte werden bisherige Standardtitel einmal entfernt. Individuelle Beschriftungen bleiben erhalten; anschließend kannst du auch einen früheren Standardtext ausdrücklich wieder eintragen.

**Schreibfähige Widgets:** Switch, Icon Toggle Button, Bool Checkbox, Bool Select, Bool SVG und Bool HTML (control) schalten gebundene `switch`-, `light`- oder `input_boolean`-Entitäten. Bulb on/off schaltet diese Entitäten oder setzt einen `input_number`-Helfer auf sein konfiguriertes Minimum/Maximum. Slider, Schieberegler und Radialer Schieberegler schreiben nur `input_number`; Input val schreibt `input_number` oder `input_text`. Note schreibt im Notizdialog an einen `input_text`-Helfer ohne Attributauswahl. Universal Element schreibt im Schaltermodus seine false-/true-Werte und im Tastermodus den nächsten konfigurierten Wert an eine passende schaltbare Entität oder einen Zahlen-/Texthelfer. Bei einer unpassenden oder nicht verfügbaren Entität ist die Bedienung gesperrt. Checkbox und Schalten schreiben ihre konfigurierten Wertepaare an passende Schalter oder Zahlen-/Texthelfer. Dropdown wählt Optionen in `select`/`input_select` oder eigene Werte in Zahlen-/Texthelfern. Die übrigen Widgets schreiben keinen HA-Zustand.

## HA Grafik – Basis (46)

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
| Note | Notizzettel mit Entitätswert, Testtext, optional ausgeblendeter Ecke und Textdialog. |
| Screen Resolution | Zeigt die aktuelle Fensterauflösung an. |
| Red Number | Zahlenwert als farbiger Kreis oder Pin mit anpassbarem Radius. |
| Bool SVG | Wählt nach dem aktuellen Zustand eines von zwei SVG-Motiven; kann eine schaltbare Entität oder einen passenden 0/1-Helfer steuern. |
| SVG shape | Zeichnet eine geometrische SVG-Form mit Farbe, Strichbreite, Rotation und Skalierung. |
| Input val | Text- oder Zahlen-Eingabefeld (150 × 70). Zahlenmodus mit optionalem min/max; Nur-lesend erlaubt auch Sensoren. Enter bestätigt immer. Auto-setzen schreibt nach der einstellbaren Eingabepause (Standard 1000 ms), auch mit withEnter. withEnter ergänzt eine Bestätigungstaste für ungesendete Eingaben. Ohne Auto-setzen schreibt das Verlassen des Feldes nichts. Schreibziele sind passende `input_number`-/`input_text`-Helfer; ohne Entität bleibt die Eingabe lokal. |
| View in widget | Bettet eine Studio-Projektseite ein (Standard 300 × 200); rekursive Einbettung wird verhindert. Für HA-Dashboards gibt es ein eigenes Widget unter Spezial. |
| View in widget 8 | Wählt eine von bis zu 50 Seiten anhand des Indexzustands. |
| iFrame | Bettet eine URL ein, sofern die Zielseite dies erlaubt; mit Rahmen-, Scroll- und Aktualisierungsoptionen. |
| iFrame 8 | Wählt anhand des Indexzustands einen Frame aus [0] bis [20], mit eigener Sandbox-Einstellung je URL. |
| Image 8 | Wählt anhand des Indexzustands Bild [0] bis maximal Bild [200]. |
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
| Horizontal line | Horizontale Trennlinie mit einstellbaren Enden und Einrasten. |
| Vertical line | Vertikale Trennlinie mit einstellbaren Enden und Einrasten. |
| Gauge | Einfache Messwertanzeige mit Einheit. |
| Image | Bildquelle, Strecken und gesteuertes Neuladen; optionale native Browserinteraktionen. Standardgröße 200 × 130 px. |

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

### Image

**Allgemein** enthält Quelle, Strecken, Updatezeit (ms), Update bei Aufwachen, Update bei Viewwechsel, Addiere nichts zu URL und `allowUserInteractions`. **CSS Allgemein** bleibt aktiv; andere CSS-Gruppen starten deaktiviert.

- Ohne **Strecken** verwendet das Bild die volle Widget-Breite mit seinem ursprünglichen Seitenverhältnis. Überstehende Höhe wird abgeschnitten. Mit Strecken füllt es Breite und Höhe, auch wenn sich dadurch das Seitenverhältnis ändert.
- **Updatezeit 0** deaktiviert regelmäßiges Neuladen. Beispielsweise aktualisiert `51800` alle 51,8 Sekunden. Unveränderte Bilder werden durch andere Zustandswechsel nicht neu geladen; laufende Timer behalten ihren Takt. Unsichtbare Bilder werden nicht regelmäßig aktualisiert.
- **Update bei Aufwachen / Viewwechsel** lädt beim erneuten Aktivieren der Browserseite beziehungsweise beim Öffnen der Projektseite nach. **Addiere nichts zu URL** behält die URL unverändert; dabei kann der Browser seinen Cache verwenden. Ohne Haken ergänzt Studio einen Zeitstempel und erhält vorhandene URL-Parameter und Sprungmarken.
- **allowUserInteractions** erlaubt normale Browseraktionen wie Ziehen oder das Bild-Kontextmenü in der Runtime. Ohne Haken werden Zeigeraktionen zum darunterliegenden Element durchgereicht. Im Editor bleibt das Widget auswählbar und verschiebbar.

Bild über die Studio-Dateiauswahl oder eine URL wählen. VIS2-Pfade wie `_PRJ_NAME/001_cheerful.png` müssen durch den entsprechenden Studio-Dateipfad ersetzt werden. Kein HA-Helfer nötig. Bestehende Projekte mit einer URL-Entität werden weiterhin gelesen; eine HA-Kamera-API wird dadurch nicht angebunden. Die kleinen roten Umsteigerhinweise sind über die zentrale Einstellung ein- und ausschaltbar.

![Image mit Strecken und proportionaler Darstellung im Vergleich](/images/grafik-visual-studio/image.png)

Funktionale Referenz: [VIS2 Image](https://github.com/ioBroker/ioBroker.vis-2/blob/master/packages/iobroker.vis-2/src-vis/src/Vis/Widgets/Basic/BasicImage.tsx).

### Image 8

Die HA-Entität liefert den Bildindex; `false`/`off` entspricht 0, `true`/`on` entspricht 1. Ohne Entität oder bei einem fehlenden Zustand wird **Bild [0]** verwendet. Die Entität wird im Editor und in der Runtime nur gelesen; ein zusätzlicher HA-Helfer ist nicht nötig.

**Werteanzahl bis** bezeichnet den höchsten Index und ist auf **200** begrenzt: 0 ergibt einen Eintrag, 200 ergibt **201 Einträge von Bild [0] bis Bild [200]**. Jede Bildgruppe besitzt eine Quelle mit Dateiauswahl und kann kopiert, gelöscht, verschoben oder deaktiviert werden. Der letzte Eintrag bleibt erhalten; bei Index 200 ist Kopieren deaktiviert. Leere, deaktivierte oder ungültige Indizes zeigen kein Bild; vorhandene Quellen werden nicht automatisch neu nummeriert. Beim Verringern der Grenze bleiben die ausgeblendeten Quellen erhalten, bis sie ausdrücklich gelöscht werden.

Neue Widgets sind **200 × 130 px** groß. Strecken, Updatezeit, Aufwachen, Viewwechsel, unveränderte URL und normale Browseraktionen entsprechen **Image**. Ein unverändertes Bild wird bei anderen Zustandsänderungen nicht neu geladen; laufende Refresh-Timer behalten ihren Takt. **CSS Allgemein** bleibt aktiv, andere CSS-Gruppen starten deaktiviert. Die kleinen roten Umsteigerhinweise lassen sich zentral ein- und ausschalten.

![Image 8 mit höchstem Bildindex 200 und Refresh-Einstellungen](/images/grafik-visual-studio/image8.png)

Funktionale Referenz: [VIS2 Image 8](https://github.com/ioBroker/ioBroker.vis-2/blob/master/packages/iobroker.vis-2/src-vis/src/Vis/Widgets/Basic/BasicImage8.tsx).

### iFrame

![iFrame mit eingebetteter UGSo-Website und Aktualisierungsoptionen](/images/grafik-visual-studio/iframe.png)

Neue Widgets haben **600 × 320 px**. Unter **Allgemein** stehen Quelle, Updatezeit (ms), Kein Sandkasten, Update bei Aufwachen, Update bei Viewwechsel, Addiere nichts zu URL, Scroll X/Y und Kein Rahmen. **CSS Allgemein** bleibt aktiv; die übrigen CSS-Gruppen starten deaktiviert. Im Editor lässt sich das Widget auswählen und verschieben, ohne dass die eingebettete Seite die Mausbedienung übernimmt.

**Updatezeit 0** deaktiviert regelmäßiges Neuladen. Werte bis 180000 ms aktivieren ein Intervall. **Update bei Aufwachen** lädt nach Rückkehr zum sichtbaren Browserfenster neu; **Update bei Viewwechsel** gilt beim Anzeigen der Studio-Seite. Änderungen anderer Widgetwerte laden eine unveränderte Einbettung nicht neu. Ohne **Addiere nichts zu URL** ergänzt eine Aktualisierung den Zeitstempelparameter `_gvs`; vorhandene URL-Parameter und Sprungmarken bleiben erhalten. Mit Haken wird dieselbe URL erneut geladen.

Standardmäßig beschränkt eine Sandbox die eingebettete Seite auf Skripte und Formulare. **Kein Sandkasten** entfernt diese Einschränkung. Anmeldung, Cookies und Einbettungsregeln der Zielseite gelten weiterhin; eine Seite kann die Einbettung per Browserrichtlinie verweigern. Scroll X/Y setzen die gewünschten Überlaufoptionen, die tatsächlich verfügbaren Scrollleisten hängen auch vom Browser und Inhalt der Zielseite ab. Bei fremden Domains kann Studio deren interne Scrollachsen nicht erzwingen. **Kein Rahmen** entfernt den iFrame-Rand.

Es wird kein HA-Zustand geschrieben und kein HA-Helfer benötigt. Die optionalen Umsteigerhinweise erklären Sandbox und Aktualisierung. Ein iFrame verweist auch nach einem Export auf seine Quelle; die fremde Website wird nicht als lokale Kopie eingebettet.

### iFrame 8

![iFrame 8 mit URL und Sandbox je Eintrag](/images/grafik-visual-studio/iframe8.png)

*Editor-Beispiel mit lokaler SVG-URL für Frame [0].*

Die zustandsabhängige Variante verwendet die HA-Entität als URL-Index. `false`/`off` wählen [0], `true`/`on` wählen [1]; Zahlen wählen den entsprechenden nummerierten Eintrag. Ohne Entität starten neue Widgets mit Frame [0]. Ungültige, negative oder zu große Indizes sowie leere oder deaktivierte Einträge zeigen keinen Frame. Die Entität wird nur gelesen; ein zusätzlicher HA-Helfer ist nicht nötig.

**Werteanzahl bis** ist der höchste Index, nicht die Anzahl: Standard 2 ergibt [0], [1], [2]; Maximum 20 ergibt **21 Einträge von [0] bis [20]**. Die Gruppen **frames [n]** enthalten **URL falls Wert [n]** und **Kein Sandkasten [n]**. Sie können aktiviert/deaktiviert, kopiert, gelöscht und umgeordnet werden. Beim Reduzieren der höchsten Nummer bleiben ausgeblendete Einträge erhalten. Die Nummern entsprechen direkt dem Entitätswert; Umordnen verändert diese Zuordnung.

Standardgröße ist **600 × 320 px**. Aktualisierungsintervall, Aufwachen, Viewwechsel, unveränderte URL, Scroll X/Y und Rahmen funktionieren wie bei **iFrame**. Die Sandbox wird je Eintrag gewählt. Eine unveränderte URL mit unveränderter Sandbox wird bei Änderungen anderer Widgets nicht erneut geladen. Bei anderer URL oder Sandbox wird die Einbettung ersetzt. **CSS Allgemein** bleibt aktiv; die übrigen CSS-Gruppen starten deaktiviert. Die optionalen Umsteigerhinweise erklären Index, Sandbox und Aktualisierung.

### Note

**Allgemein** enthält Home-Assistant-Entität, HA-Attribut, HTML voranstellen, HTML anhängen, Testtext und Ecke ausblenden. Das zusätzliche Attributfeld ersetzt ioBroker-Attributdatenpunkte: Für `friendly_name` die passende HA-Entität wählen und `friendly_name` eintragen. Ein leeres Attributfeld liest den Zustand.

Ein nicht leerer **Testtext** ersetzt im Editor den Entitätswert. In der Runtime wird ausschließlich der Entitätswert beziehungsweise das Attribut angezeigt; fehlt er, bleibt der mittlere Text leer. Voranstellen und Anhängen bleiben sichtbar. Wie im VIS2-Note-Quellcode werden auch die als HTML bezeichneten Felder als Text dargestellt; `<b>` erzeugt hier keine Fettschrift. Zeilenumbrüche bleiben erhalten.

**Ecke ausblenden** steuert nur die untere rechte Ecke und ist kein Schreibschutz. Ohne Haken zeigt sie die Rahmenfarbe. Neue Notizen sind **100 × 70 px** groß, mit 5 px Eckenradius, grauem 1 px Rahmen und gelbem Hintergrund `#FFFF69CC`. Größe und Farben bleiben über CSS anpassbar; **CSS Allgemein** bleibt aktiv, andere CSS-Gruppen starten deaktiviert.

Ein Klick in der Runtime öffnet den Notizdialog. Ein verfügbarer **input_text-Helfer ohne Attributauswahl** erlaubt Bearbeiten, Leeren und Übernehmen; seine maximale Textlänge wird beachtet. Geschrieben wird nur der Notiztext, ohne Voranstellen und Anhängen. Sensoren und Attribute bleiben lesbar, bieten aber kein Schreibziel. Ohne passendes Schreibziel ist das Textfeld im Dialog nur lesbar und Übernehmen deaktiviert. Abbrechen und Escape schließen den Dialog ohne Schreiben. Die kleinen roten Helferhinweise lassen sich über **Umsteigerhinweise anzeigen** ein- und ausschalten.

![Note mit Testtext und Vergleich der ausgeblendeten und sichtbaren Ecke](/images/grafik-visual-studio/note.png)

Funktionale Referenz: [VIS2 Note](https://github.com/ioBroker/ioBroker.vis-2/blob/master/packages/iobroker.vis-2/src-vis/src/Vis/Widgets/Basic/BasicNote.tsx).

### Horizontal line / Vertical line

Die zwei Trennlinien sind reine Anzeige und benötigen keinen HA-Helfer. Horizontal line startet mit **200 × 16 px**, Vertical line mit **16 × 200 px**. Unter **CSS Trennlinie** stehen Dicke (1–100 px, Standard 2), HEX-Farbe, Rahmenfarbe, Rahmenbreite und Enden zur Verfügung: **Eckig** (Standard), **Rund** oder **Spitz (pfeilartig)** an beiden Enden. Eine erhöhte Dicke vergrößert bei Bedarf die Querabmessung des Widgets; beim anschließenden Verkleinern begrenzt die Widgetfläche die sichtbare Dicke.

Ab **0.1.183** besitzen die Trennlinien keine **Andockpunkte** und keinen **Datenfluss**. **Snapfunktion aktivieren** unter **CSS Trennlinie** schaltet das geometrische Einrasten zu; bei neuen Linien ist es ausgeschaltet. Bereits aktivierte Snap-Einstellungen bleiben erhalten. Beim einzelnen Ziehen, Skalieren eines Linienendes oder Bearbeiten der Geometrie werden Enden innerhalb von **8 Seitenpixeln** auf die Mitte einer rechtwinkligen Trennlinie gesetzt. Das funktioniert an beliebigen Stellen entlang der anderen Linie, auch für T-Verbindungen. Parallel verlaufende Linien rasten nicht ein. Gemeinsames Verschieben mehrerer Widgets verändert ihre relativen Abstände nicht. Frei gesetzte CSS-Positionen/-Größen und CSS-Transformationen deaktivieren das Einrasten.

Gespeichert werden die tatsächlichen Koordinaten und die Liniengestaltung, auch im Widget- und Projekt-Export. Die Verbindung ist keine dauerhafte Bindung: Wird eine Linie später wegbewegt, folgt die andere nicht automatisch. **CSS Allgemein** und **CSS Trennlinie** bleiben für das Speichern aktiv. Der optionale Umsteigerhinweis folgt der zentralen Einstellung **Umsteigerhinweise anzeigen**.

![Trennlinien mit T-Verbindung, pfeilartigen Enden und CSS-Einstellungen](/images/grafik-visual-studio/separator-lines.png)

![Aktivierte Snapfunktion ohne Andockpunkte und Datenfluss im Trennlinien-Editor](/images/grafik-visual-studio/separator-snap.png)

*Die Snapfunktion verbindet an beliebigen Stellen der jeweils anderen Trennlinie. Alte Dock- und Datenflusseinstellungen werden beim Laden und Speichern entfernt.*

### Border

Border zeichnet einen Rahmen mit Titel und optionalem Kopfbereich. Neue Widgets sind **100 × 70 px** groß, mit einem grauen (`#888888`) Rahmen von 1 px und sichtbarem Überlauf. **Allgemein** enthält die sechs Standardfelder: Titel, Titelhintergrund, Titel-Oben-Abstand, Titel-Links-Abstand, Kopfhöhe und Kopffarbe. Farben werden als HEX gewählt.

Die Titelposition ist absolut zum Rahmen: Standard **oben −10 px, links 20 px**, ohne zusätzliche vertikale Verschiebung. Der Titel darf einfache HTML-Formatierungen wie `<b>Titel</b>` enthalten; Skripte, Event-Handler und aktive Einbettungen werden entfernt. Schrift und Rahmen lassen sich über die passenden CSS-Gruppen gestalten.

**Kopfhöhe 0** blendet den Kopfbereich aus. Ohne eigenen Titelhintergrund erhält der Titel dann eine schwarze Fläche im dunklen beziehungsweise eine weiße Fläche im hellen Seitenthema. Bei sichtbarem Kopfbereich bleibt der Titelhintergrund ohne eigene Farbe transparent; eine leere Kopffarbe verwendet ebenfalls Schwarz oder Weiß passend zum Thema. Im Beispiel links ist nur der Titelhintergrund gesetzt, rechts zusätzlich ein 30 px hoher Kopfbereich.

Rahmen und Titel benötigen keine HA-Entität und keinen Helfer. **CSS Allgemein** bleibt für Position und Größe aktiv; die anderen CSS-Gruppen starten deaktiviert. Optionale kleine rote Umsteigerhinweise lassen sich zentral ein- und ausschalten.

![Border mit Titelposition und optionalem Kopfbereich](/images/grafik-visual-studio/border.png)

Funktionale Referenz: [VIS2 Border](https://github.com/ioBroker/ioBroker.vis-2/blob/master/packages/iobroker.vis-2/src-vis/src/Vis/Widgets/Basic/BasicFrame.tsx).

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

## HA Grafik – Interaktiv (11)


| Widget | Aktuelle Funktion |
| --- | --- |
| Universal Element | Standardzustand und bis zu 20 bedingte Zustände; Symbol, Bild, Text oder HTML. Schalten, Taster, Anzeige und Navigation mit Einzel- oder getrennten Tasten. |
| Calendar | Monatsansicht mit Datumsauswahl, Heute-Markierung, Tagessperren und Kalenderwochen. |
| Terminkalender | Termine in Monats-, Wochen-, Tages-, Jahres- und Listenansichten; mehrere Quellen und Farbregeln. |
| Checkbox | Eigene false-/true-Werte, Zustandstexte, vier Textpositionen und Boxgestaltung. |
| Schieberegler | Horizontaler/vertikaler Zahlenregler mit Wertetikett, Schrittmarkierungen und getrennten Stilen für Spur und Daumen. |
| Tabelle | JSON-Tabelle mit Spaltenformaten, Formeln, Sortierung, Filtern, Seitenaufteilung und Zeilenfarben. |
| Lauftext | Statischer Text oder HA-Zustand als fortlaufender Ticker mit Richtung, Geschwindigkeit und Hover-Pause. |
| Werteliste | Text in einzelne Listeneinträge aufteilen; acht Zeichenarten, Nummerierung, eigene Zeichen und Abstände. |
| Schalten | Eigene false-/true-Werte und Zustandstexte; getrennte Spur-/Daumenstile mit Stilübernahme. |
| Radialer Schieberegler | Zahlenregler mit Start-/Endwinkel, Wert und Bezeichnung sowie eigenen Spur-/Daumenstilen. |
| Dropdown | HA- oder eigene Optionen mit Titel, bedingtem Hintergrund und getrennten Menü-/Widget-Schatten. |

### Dropdown

Ab **0.1.182** bietet **Dropdown** unter **Interaktiv** eine Optionsauswahl mit optionalem Titel, standardmäßig **300 × 50 px**. Bei HA-`select` und `input_select` kommen die Optionen aus dem Attribut `options`. **Eigene Optionen verwenden** erlaubt bis zu **200 Wert-/Textpaare**; doppelte Werte erscheinen einmal. Die beiden Anzeigehäkchen wählen Wert, Text oder die Kombination; gleiche Texte werden nicht doppelt angezeigt. Sind beide aus, bleibt der Wert zur eindeutigen Auswahl sichtbar.

- **Schreiben:** `select`/`input_select` verwenden ausschließlich aktuell erlaubte Optionen. Eigene Zahlenwerte schreiben an `input_number`, Texte bis 255 Zeichen an `input_text`. Unpassende Optionen werden gesperrt. Sensoren, fehlende Zustände, Schreibschutz und der Editor bleiben ohne Schreibzugriff; ohne Entität funktioniert eine lokale Auswahl.
- **Hintergrundfarb-Bedingungen:** bis zu **20 Regeln**, mit sechs Vergleichsoperatoren. Die erste passende Regel gewinnt. Ohne zusätzliche Hintergrund-Entität gilt der ausgewählte Wert; sonst deren Zustand. Unbekannte oder nicht verfügbare Zustände lösen keine Farbregel aus.
- **CSS Dropdown:** Schriftgröße, Text-, Hintergrund-, Hervorhebungs- und Rahmenfarbe, Rahmenbreite/-radius sowie Titelgröße/-farbe und vier Titelabstände. Der Titel kann die aktive Bedingungsfarbe übernehmen. **Dropdown-Schatten** gestaltet Auswahl und offenes Menü; **Widget-Schatten** den gesamten Bereich inklusive Titel. Beide haben X/Y-Versatz, Unschärfe, Ausdehnung und Farbe.
- **Vom Widget:** übernimmt ausschließlich die Darstellung eines anderen Dropdowns, einschließlich Titelstil und Schatten. Titeltext, Optionsliste, Entität und Regeln bleiben lokal. Gemeinsame Kopien erhalten passende Stilreferenzen; Zyklen werden abgefangen.
- **Bedienung:** Klick oder Pfeiltaste öffnet das Menü. Pfeiltasten, Pos1/Ende, Enter/Leertaste und Escape bedienen die Liste; Tab verlässt sie. Lange Einträge umbrechen im Menü, große Listen scrollen. Schreibschutz zeigt den Wert ohne Auswahlpfeil.

Alle Einstellungen, eigenen Optionen, Regeln und Referenzen bleiben in Projekt-, Widget- und Paketexporten erhalten. Die Optionsliste ist ein eigenes Studio-Menü, damit Farben und Schatten einheitlich wirken.

![Dropdowns mit bedingtem Hintergrund, Schreibschutz, geöffnetem Menü und übernommenem Stil](/images/grafik-visual-studio/dropdown.png)

Funktionsreferenz: [inventwo Dropdown für VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/en/widgets/dropdown-widget.md). Die HA-Anbindung und Darstellung sind eigenständig umgesetzt.

### Radialer Schieberegler

Ab **0.1.181** steht unter **Interaktiv** der **Radiale Schieberegler** bereit. Neue Widgets starten mit **200 × 200 px**, Bereich **0–100**, Schritt **1**, Startwinkel **225°** und Endwinkel **135°**. **0° liegt oben**; der Bogen läuft im Uhrzeigersinn, standardmäßig über **270°**. Gleiche Winkel ergeben einen Vollkreis; **270° bis 90°** ergibt einen oberen Halbkreis.

- **Allgemein:** HA-Entität, Minimum, Maximum, Schritt, Start-/Endwinkel, Wert anzeigen, Bezeichnung anzeigen, Bezeichnung und Schreibschutz. Ohne Entität dient der Vorschauwert als Ausgangswert.
- **CSS Radialregler – Spur:** Spurfarbe, aktive Farbe, Breite **1–50 px** sowie Schattenfarbe, X/Y-Versatz und Unschärfe.
- **CSS Radialregler – Daumen:** Farbe, Größe **1–50 px** und eigener Schatten.
- **CSS Radialregler – Wert:** Wertgröße **8–100 px**, Wertfarbe, Bezeichnungsgröße **8–50 px** und Bezeichnungsfarbe. Zahlen werden bei Platzmangel verkleinert; lange Bezeichnungen gekürzt. Der vollständige Text bleibt als zugänglicher Name des Reglers erhalten.
- **Vom Widget:** Spur und Daumen können unabhängig von einem anderen Radialregler übernommen werden. Wertanzeige, Bezeichnung und Wertebereich bleiben lokal. Zyklen werden abgefangen; gemeinsame Kopien erhalten passende neue Referenzen.
- **Bedienung:** Ziehen oder Pfeiltasten ändern um einen Schritt, Bild auf/ab um zehn Schritte, Pos1/Ende wählen Minimum/Maximum. Die Bogenlücke wählt den näheren Endwert. Ein abgebrochener Ziehvorgang stellt den Ausgangswert wieder her und schreibt nichts.
- **HA:** Nur verfügbare `input_number`-Helfer werden beschrieben, beim Loslassen beziehungsweise Tastendruck. Grenzen und Schritt müssen zum Helfer passen. Sensoren und Schreibschutz erlauben ausschließlich Anzeige; fehlende Werte erscheinen als Gedankenstrich. Ohne Entität bleiben Änderungen lokal. Im Editor wird nichts geschrieben.

Alle Einstellungen und Stilreferenzen bleiben in Projekt-, Widget- und Paketexporten erhalten.

![Radialregler mit Standardbogen, Dezimalwert, Halbkreis und schreibgeschütztem Vollkreis](/images/grafik-visual-studio/radial-slider.png)

Funktionsreferenz: [inventwo Radial Slider für VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/en/widgets/radial-slider-widget.md). Studio verwendet eine eigene Umsetzung.


### Schalten

Ab **0.1.180** ergänzt **Schalten** unter **Interaktiv** den bisherigen Basis-**Switch**. Neue Widgets starten mit **70 × 40 px**, Textposition **Ende**, **12 px** Spur und **16 px** Daumen. Leere **Wert false/true** verwenden Boolean-Werte; eigene Zahlen oder Texte erlauben andere Wertepaare. **Text falsch/wahr** wird passend zum Zustand rechts, links, oben oder unten angezeigt und bleibt reiner Text.

- **CSS Schalten – Spur:** getrennte Farben für false/true, Spurbreite **1–50 px**, Rundung **1–100 %** sowie X-/Y-Versatz, Unschärfe, Ausdehnung und getrennte Schattenfarben je Zustand.
- **CSS Schalten – Daumen:** getrennte Farben für false/true, Größe **1–50 px**, Rundung **1–100 %** und eigene Schatteneinstellungen. 100 % ergibt eine runde Form.
- **Vom Widget:** übernimmt Spur und Daumen unabhängig von einem anderen Schalten-Widget. Wertbindung und Texte bleiben lokal; zyklische Verweise enden sicher. Gemeinsames Kopieren ordnet die Verweise den kopierten Widgets zu.
- **Bedienung:** Klick auf Schalter oder Text, alternativ Leertaste. Die Runtime schreibt passende Werte an verfügbare `switch`-, `light`-, `input_boolean`-, `input_number`- oder `input_text`-Entitäten. Sensoren, unpassende Wertepaare, fehlende Zustände und der Editor bleiben nicht schreibfähig. Ohne Entität kannst du lokal umschalten.

Schrift und Textfarbe kommen aus den üblichen CSS-Gruppen. Alle Werte, Zustandstexte, Stilfelder und Verweise bleiben im Projekt und Widget-/Paket-Export erhalten.

![Schalten mit vier Textpositionen, unabhängiger Spurübernahme und gesperrter Sensoranzeige](/images/grafik-visual-studio/styled-switch.png)

Funktionsreferenz: [inventwo Switch für VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/en/widgets/switch-widget.md). Studio verwendet eine eigene Implementierung.

### Werteliste

Ab **0.1.179** ergänzt **Werteliste** unter **Interaktiv** die bisherigen Basis-Widgets **ValueList Text/HTML/HTML Style**. Neue Widgets starten mit **200 × 150 px**, Komma als Trennzeichen, aktivem Entfernen äußerer Leerzeichen und Ignorieren leerer Einträge. Mit HA-Entität gilt deren Zustand; ohne Entität verwendest du **Text (manuell)**. Die Liste liest ausschließlich und zeigt Text wörtlich an.

- **Trennzeichen:** Zeichen oder mehrstellige Zeichenfolge; `\\n` für Zeilen und `\\t` für Tabulatoren. Ein leeres Trennzeichen zeigt den gesamten Text als einen Eintrag. Windows-Zeilenumbrüche werden berücksichtigt.
- **Leerzeichen entfernen** und **Leere Einträge ignorieren** arbeiten unabhängig. Bei ausgeschalteter Filterung bleiben leere Zeilen sichtbar; Nummern folgen den angezeigten Einträgen.
- **Darstellung:** Punkt, Kreis, Quadrat, Strich, Pfeil, Nummerierung, kein Zeichen oder eigenes Zeichen/Emoji. Zeichenfarbe ist unabhängig von der Textfarbe. Ohne Zeichen entfallen Zeichenfarbe und Zeichenabstand; das eigene Zeichenfeld erscheint nur bei dieser Auswahl.
- **Abstände:** Zeichen zu Text **0–50 px** (Standard **8**), Zeilen **0–50 px** (Standard **4**), Innenabstand **0–200 px** (Standard **4**). Lange Einträge brechen um; umfangreiche Listen lassen sich innerhalb des Widgets scrollen.

Schrift, Textfarbe und Hintergrund stellst du über die normalen CSS-Gruppen ein. Alle Einstellungen bleiben im Projekt und im Widget-/Paket-Export erhalten.

![Wertelisten mit Punkten, Nummerierung, eigenen Zeichen und umgebrochenem Text](/images/grafik-visual-studio/interactive-value-list.png)

Funktionsreferenz: [inventwo Werteliste für VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/en/widgets/value-list-widget.md). Studio verwendet eine eigene Implementierung.

### Lauftext

Ab **0.1.178** findest du **Lauftext** unter **Interaktiv**. Neue Widgets starten mit **300 × 40 px**, Richtung **Links**, **80 px/s**, **3 Textkopien** und **50 px Abstand**. Ohne Entität gilt **Lauftext (statisch)**; mit Entität hat der HA-Zustand Vorrang. Der Inhalt bleibt reiner Text und schreibt keine HA-Werte.

- **Richtung:** Links oder Rechts; Geschwindigkeit **10–500 px/s**. Sie bleibt auch bei mehr Kopien konstant.
- **Textkopien:** **1–200**; kurze Texte werden zusätzlich so oft wiederholt, dass der Bereich gefüllt bleibt. **Abstand zwischen Kopien**: **0–1000 px**.
- **Bei Hover pausieren:** hält die Animation unter dem Mauszeiger an und setzt sie beim Verlassen fort. Unveränderte Texte laufen bei HA-Aktualisierungen ohne Neustart weiter.
- **Darstellung:** Hintergrund sowie Schrift, Textfarbe, Größe und Abstände über die normalen CSS-Einstellungen. Im Editor steht der Text still. **Reduzierte Bewegung beachten** ist standardmäßig aktiv: Bei der entsprechenden Systemeinstellung bleibt auch die Runtime statisch; die Option lässt sich pro Widget abschalten.

Alle Einstellungen bleiben im Projekt und im Widget-/Paket-Export erhalten.

![Lauftext mit Energie- und Wettermeldungen sowie automatisch ergänzten kurzen Textkopien](/images/grafik-visual-studio/marquee.png)

Funktionsreferenz: [inventwo Lauftext für VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/de/widgets/marquee-widget.md). Studio verwendet eine eigene Implementierung.

### Tabelle

Ab **0.1.177** ergänzt **Tabelle** unter **Interaktiv** die bisherige Basis-**Table**. Neue Widgets starten mit **400 × 300 px**, automatischen Spalten, sichtbarer Kopfzeile und ohne Seitenaufteilung. Daten sind eine JSON-Liste von Objekten, zum Beispiel:

```json
[{"raum":"Küche","temperatur":25.4,"leistung":120,"aktiv":true}]
```

Die Runtime liest die gebundene HA-Entität oder das ausdrücklich ausgewählte **HA-Attribut**. Für längere Listen sollte ein Attribut verwendet werden. Ohne Entität und im Editor gelten die JSON-Testdaten. Die Tabelle liest ausschließlich; Sortieren, Filtern und Seitenwechsel schreiben keine HA-Werte.

- **Spalten:** 0 erkennt die Schlüssel automatisch; bis zu 50 Spalten lassen sich konfigurieren. Möglich sind Ausblenden, Schlüssel, Titel, Breite, Ausrichtung, Präfix/Suffix und Platzhalter. Formate: Text, Zahl mit Dezimal-/Tausendertrennzeichen, Boolean als gesperrte Checkbox, Datum/Uhrzeit mit eigenem Muster, Bild, URL und IP-Adresse. Inhalte werden als Text behandelt; Bilder und Links benötigen eine erlaubte URL.
- **Formeln:** rechnen mit Zahlenfeldern der Zeile, beispielsweise `leistung * 2`. Unterstützt werden `+ - * / % **` und Klammern. Es wird kein JavaScript ausgeführt; ungültige Formeln verwenden den Platzhalter. Eigene Datumsmuster unterstützen `YYYY`, `YY`, `MM`, `M`, `DD`, `D`, `hh`, `h`, `mm`, `ss`, `sss`, `WD`, `WDL`, `KW` und `K`.
- **Sortierung und Filter:** Standardsortierung nach Schlüssel und Richtung; optional bis zu 20 Standardsortierungen mit Priorität. Klicks auf sortierbare Kopfzeilen wechseln aufsteigend/absteigend/ohne Sortierung. Automatische Spalten sind sortierbar; manuelle Spalten bieten eigene Sortier- und Filteroptionen. Filter wählen die zugelassenen Zellwerte. Die Zeilenbegrenzung gilt nach Filtern und Sortieren, vor der Seitenaufteilung. Kopfzeilen können beim Scrollen fixiert werden.
- **Zeilenbedingungen:** bis zu 20 Regeln nach Schlüssel oder Spaltenindex ab 0, mit sechs Vergleichsoperatoren. Die erste passende Regel bestimmt Hintergrund, Textfarbe der ganzen Zeile und/oder der Bedingungsspalte. **Summenzeile markieren** zieht eine Doppellinie über der letzten Ergebniszeile; Summen müssen bereits in den Daten stehen.
- **CSS Tabelle:** neutrale Gruppen **Darstellung**, **Rahmenradius**, **Rahmen** und **Äußerer Schatten**, mit HEX-Farben, Zeilen-/Kopfhöhen, Zeilenrändern, getrennten Ecken und Randseiten. **Vom Widget** übernimmt jede Gruppe unabhängig von einer anderen Tabelle; gemeinsam kopierte Widgets erhalten passende Verweise. **CSS Allgemein** bleibt aktiviert.

Der Widget-JSON-Export enthält Spalten, Regeln, Stile und Quellenbindung. Benötigte HA-Entitäten, Attribute und referenzierte Stilwidgets müssen am Ziel vorhanden sein. Ohne Entitätsbindung bleiben die gespeicherten JSON-Daten nutzbar. Kleine Umsteigerhinweise lassen sich zentral abschalten.

![Interaktive Tabelle mit Sortierung, Zeilenbedingungen, berechneter Leistung und Seitenaufteilung](/images/grafik-visual-studio/interactive-table.png)

Funktionsreferenz: [inventwo Tabelle für VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/de/widgets/table-widget.md). Studio verwendet eine eigene Implementierung.

### Schieberegler

Ab **0.1.176** steht unter **Interaktiv** ein eigener **Schieberegler** bereit. Der bisherige **Slider** unter Basis bleibt erhalten. Neue Widgets starten mit **150 × 40 px**, Bereich **0–100**, Schritt **1**, horizontaler Ausrichtung und sichtbaren Min./Max.-Werten.

- **Allgemein:** optionale Überschrift mit Abstand, Einheit, HA-Entität, Mindest-/Maximalwert, Schritt und Vorschauwert. Vertikale Regler steigen von unten nach oben. Das Wertetikett erscheint beim Bedienen, immer oder nie. Überschrift und Einheit werden als Text angezeigt.
- **Schrittmarkierungen:** automatisch im eingestellten Markierungsabstand oder an eigenen Positionen aus einer Kommaliste, zum Beispiel `-20,0,20,50,80`. Markierungen sind unabhängig vom Bedienschritt und können innerhalb der Spur oder oben/unten bzw. links/rechts stehen. Dichte Skalen werden auf höchstens 201 Markierungen ausgedünnt; Zahlenbeschriftungen passen sich der Widgetgröße an.
- **CSS Schieberegler – Spur / Daumen:** HEX-Farben, Spurbreite, Daumengröße, Rundung in Prozent und getrennte Schatten mit X/Y-Versatz, Unschärfe und Ausdehnung. Der Spurtyp bietet Normal, Umgekehrt oder Keine aktive Spur. Daumengröße **0** blendet den Daumen aus. **Vom Widget** übernimmt jede Gruppe unabhängig von einem anderen Schieberegler; gemeinsam kopierte Widgets erhalten passende interne Verweise. **CSS Allgemein** bleibt aktiviert.
- **Bedienung:** zum Schreiben ist ein verfügbarer `input_number`-Helfer nötig. Minimum, Maximum und Schritt müssen zum Helfer passen. Sensoren und nicht verfügbare Entitäten werden nur angezeigt. **Schreibgeschützt** verhindert Änderungen. Ohne Entität bleibt der Wert lokal; im Editor wird nichts geschrieben. HA-Schreibaufträge werden beim Abschluss einer Änderung gesendet.

Beim Widget-JSON-Export werden sämtliche Regleroptionen, Stile und Entitätsbindungen gespeichert. Die Entität und referenzierte Stil-Quellwidgets müssen am Ziel ebenfalls vorhanden sein. Für Überschrift, Wertetikett und Skala kann ein größeres Widget sinnvoll sein.

![Horizontaler und vertikaler Schieberegler, Fortschrittsanzeige und eigene Markierungen](/images/grafik-visual-studio/styled-slider.png)

Funktionsreferenz: [inventwo Schieberegler für VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/de/widgets/slider-widget.md). Studio verwendet eine eigene Implementierung.

### Checkbox

Ab **0.1.175** ergänzt **Checkbox** unter **Interaktiv** die bisherige **Bool Checkbox** aus Basis. Neue Widgets starten mit **70 × 40 px**, **24 px** Boxgröße und Textposition **Ende**.

- **Allgemein:** HA-Entität, false-/true-Werte, Text falsch/wahr, Textposition und Testzustand. Leere Werte verwenden `false` und `true`. Die Positionen Ende/Start/Oben/Unten setzen den Text rechts/links/oberhalb/unterhalb der Box. Texte werden als Text angezeigt.
- **CSS Checkbox – Stil:** optionale HEX-Boxfarben für inaktiv/aktiv, Boxgröße von 0 bis 50 px und **Vom Widget** für die Stilübernahme einer anderen Checkbox. Zyklische Verweise enden sicher; gemeinsam kopierte Widgets erhalten passende interne Verweise. Schrift und Textfarbe folgen den allgemeinen CSS-Einstellungen. **CSS Allgemein** bleibt aktiviert.
- **Bedienung:** Ohne Entität wird lokal geschaltet. `switch`, `light` und `input_boolean` unterstützen boolesche Werte bzw. on/off und 0/1. Zahlenpaare benötigen `input_number`, Textpaare `input_text`. Sensoren, nicht verfügbare Entitäten und unpassende Wertepaare bleiben schreibgeschützt. Im Editor wird nichts geschrieben. Laufende HA-Schreibaufträge sperren die Checkbox vorübergehend.

Beim JSON-Export werden Werte, Texte, Stil und Entitätsbindung gespeichert. Die Entitäten müssen am Ziel existieren; referenzierte Stil-Quellwidgets müssen ebenfalls enthalten sein. Die kleinen roten Hinweise folgen **Umsteigerhinweise anzeigen**.

![Checkbox mit Zustandstext und Stilübernahme](/images/grafik-visual-studio/checkbox.png)

Funktionsreferenz: [inventwo Checkbox für VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/de/widgets/checkbox-widget.md). Studio verwendet eine eigene Implementierung.

### Calendar

**Calendar** ist eine Monatsansicht zur Datumsauswahl, keine Terminanzeige. Neue Widgets starten mit **320 × 350 px**, Tageszellen von **36 px**, Montag als Wochenbeginn und Hervorhebung des heutigen Tages. **Allgemein** enthält die HA-Entität, das Werteformat, ein Testdatum nur für den Editor, Schreibschutz, Vergangenheits-/Zukunftssperre, Monats-/Jahresnavigation, Wochenbeginn, Kalenderwochen und Zellgröße (20–80 px).

- **Zeitstempel (Zahl, ms):** Millisekunden seit Epoch, zum Schreiben in einen `input_number`-Helfer. Wähle dessen Wertebereich ausreichend groß. Die Datumsauswahl schreibt Mitternacht in der lokalen Browser-Zeitzone.
- **ISO-Datum:** `JJJJ-MM-TT`, zum Schreiben in einen `input_text`-Helfer. Ein Sensor kann das Datum liefern, wird aber nicht beschrieben. Nur verfügbare Helfer im passenden Format erlauben die Datumsauswahl; Schreibschutz sperrt auch die Navigation.
- Ohne Entität bleibt die Auswahl lokal in der Runtime und wird nicht in das Projekt geschrieben. **Testdatum** wird ausschließlich im Editor verwendet; die Runtime ignoriert es. Der Editor schreibt keine Datumswerte und sperrt die Kalenderbedienung.
- Vergangene und zukünftige Tage werden relativ zum lokalen heutigen Datum gesperrt. Heute bleibt auswählbar. **ISO-8601** berücksichtigt Kalenderwochen am Jahreswechsel; **Einfach** setzt KW 1 auf die Woche mit dem 1. Januar und berücksichtigt den gewählten Wochenbeginn.

Die sechs neutralen Gruppen **CSS Kalender – Kopfzeile / Wochentage / Tag / Ausgewählter Tag / Heute / Kalenderwoche** bieten HEX-Farben, Tagesradius und den Schatten des ausgewählten Tages. Nicht gesetzte Textfarben verwenden die Studio-Themenfarben. **Vom Widget** übernimmt ausschließlich den jeweiligen Bereich eines anderen Calendar-Widgets; zyklische oder ungültige Verweise enden ohne Endlosschleife. Bei gemeinsamem Kopieren werden interne Verweise angepasst; beim Export müssen referenzierte Kalender mit enthalten sein. **CSS Allgemein** bleibt aktiviert und speichert Position und Größe. Die kleinen roten Helferhinweise folgen **Umsteigerhinweise anzeigen**.

Monat und Jahr können direkt gewählt werden. Ist Monats-/Jahresnavigation deaktiviert, bleiben in der Runtime die Pfeile für den vorherigen und nächsten Monat verfügbar. Ein fehlgeschlagener HA-Schreibauftrag zeigt einen Fehler und erlaubt einen erneuten Versuch.

![Calendar mit Datumsauswahl, Heute-Markierung und Kalenderwochen](/images/grafik-visual-studio/calendar.png)

Funktionsreferenz: [Kalender von inventwo für VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/de/widgets/calendar-widget.md). Studio verwendet eine eigene Implementierung ohne Abhängigkeit vom ioBroker-Paket.

### Terminkalender

Ab **0.1.174** zeigt der **Terminkalender** Termine ausschließlich lesend an. Die Standardgröße ist **600 × 500 px**. Zur Auswahl stehen Monat, Woche mit Stundenraster, Tag, Jahr mit zwölf Monaten und Listen für Tag, Woche, Monat oder Jahr. Kopfzeile und Navigation lassen sich getrennt abschalten. Wochenbeginn, ISO-/einfache Kalenderwochen und die Uhrzeit-Linie sind einstellbar. **Max. Termine pro Tag** begrenzt die sichtbaren Einträge; `0` zeigt alle. Weitere Termine öffnen sich über **+N weitere**.

- **Termine (HA-Entität):** `calendar.*` lädt den sichtbaren Zeitraum über [calendar.get_events](https://www.home-assistant.io/integrations/calendar/). Der normale Kalenderzustand enthält keine vollständige Terminliste. Andere HA-Entitäten können eine JSON-Liste als Zustand liefern.
- **Termine (JSON, ohne Entität):** Eine direkt gespeicherte JSON-Liste dient als lokale Quelle. Unterstützt werden `title` / `summary` / `event`, `start` / `_date`, optional `end` / `_end`, `allDay` / `_allDay` und `color` / `_calColor`. Beginn und Ende sind ISO-Datum, ISO-Datum mit Uhrzeit oder Millisekunden. Ein reines Datum gilt als ganztägig; dessen Ende ist exklusiv. Fehlendes oder mit dem Beginn identisches Ende nutzt die Standarddauer.
- **Weitere Kalender:** Bis zu 20 Quellen mit HA-Entität, optionaler HEX-Quellfarbe und Legendentext. Sobald die Anzahl größer als `0` ist, ersetzen diese Quellen das einzelne Entitätsfeld und die lokale JSON-Liste. Leere Quellen liefern keine Termine. Die Legende lässt sich abschalten.
- **Termin-Farbregeln:** Bis zu 20 Regeln vergleichen einen Titelteil ohne Beachtung der Groß-/Kleinschreibung. Die erste passende Regel setzt die Hintergrundfarbe. Die Quellfarbe bleibt als linker Streifen bzw. Punkt in Listen sichtbar.

```json
[{"title":"Familienausflug","start":"2026-10-03","end":"2026-10-05","color":"#3686BD"}]
```

Die sechs neutralen Gruppen **CSS Terminkalender – Kopfzeile / Wochentage / Tag / Heute / Termin-Kacheln / Rahmen** bieten HEX-Farben, Schriftgrößen, Radien, Rahmen und Hover-Farben für Navigationsbuttons. **Vom Widget** übernimmt den jeweiligen Bereich eines anderen Terminkalenders; zyklische Verweise enden sicher. **CSS Allgemein** bleibt aktiviert. Umsteigerhinweise folgen dem zentralen Schalter. Editor-Vorschauen schreiben keine Termine und lassen sich weiterhin ziehen und skalieren.

HA-Kalender werden beim Zeitraumwechsel und frühestens nach 60 Sekunden erneut gelesen; JSON-Entitätszustände folgen der normalen Abfrage alle fünf Sekunden. Fehler werden im Widget angezeigt. `.ics`-Dateien werden über eine HA-Kalenderintegration eingebunden. Es gibt keine Termin-Erstellung, -Bearbeitung oder -Löschung.

Beim Widget-Export werden Konfiguration und direkt eingetragenes JSON mitgenommen, aber keine live abgerufenen HA-Termine. Am Ziel müssen die verwendeten Entitäten verfügbar sein; referenzierte CSS-Quellwidgets müssen ebenfalls mitgeliefert werden.

![Terminkalender mit Farbregeln und zusätzlichem Termin-Popup](/images/grafik-visual-studio/event-calendar.png)

Funktionsreferenz: [inventwo-Terminkalender für VIS2](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/de/widgets/event-calendar-widget.md). Studio verwendet eine eigene Datenanbindung und den lokal mitgelieferten [FullCalendar 6.1.21](https://legacy.fullcalendar.io/v6/) unter MIT-Lizenz; das ioBroker-Paket ist nicht erforderlich.

### Universal Element

![Beschriftungen bleiben nach dem Klick in allen drei betroffenen Widgets sichtbar](/images/grafik-visual-studio/captions-after-click.png)

Ab Studio **0.1.195** übernimmt ein leerer Zustandstext den Text des Standardzustands, danach den optionalen Titel. So bleibt etwa „Licht Garage“ beim Schalten sichtbar, auch bei getrennten Tasten. Nichtleere Zustandstexte ersetzen weiterhin den Standardtext. Bei **Checkbox** und **Schalten** übernimmt ein leerer Zustandstext den anderen Zustandstext, danach den Titel. Für eine Anzeige ohne Beschriftung bleiben alle Textfelder und der Titel leer. Der Editorname wird nicht eingeblendet.

Der frühere Name **State Element** bleibt als Suchbegriff erhalten. Bestehende Projekte verwenden weiterhin denselben Widget-Typ `universal-button`.

- **Allgemein:** HA-Entität, Bedienung, Modus, false-/true-Werte und Navigations-URL. Ohne Entität arbeitet das Element lokal. Ein Sensor ist kein Schreibziel; Zahlen und Text benötigen passende `input_number`-/`input_text`-Helfer. Nur Anzeige und Navigation schreiben keinen HA-Zustand.
- **Klick-Feedback:** Dauer in Millisekunden und sechs optionale Farben; `0` deaktiviert die Rückmeldung. Sie bleibt während des Zustandswechsels sichtbar. „Klick durchlassen“ reicht Mausklicks in der Runtime an darunterliegende Elemente weiter und deaktiviert die eigene Bedienung.
- **Standardzustand / Zustände und Inhalte:** Der erste passende aktive Zustand gewinnt; ohne Treffer erscheint der Standardzustand. Regeln vergleichen die Widget-Entität oder eine andere HA-Entität mit `==`, `!=`, `>`, `>=`, `<` oder `<=`. Zustände lassen sich kopieren, löschen, verschieben und deaktivieren. Eine kleinere Anzahl behält die ausgeblendeten Einträge. „Klick deaktivieren wenn aktiv“ sperrt nur den aktuell passenden Zustand. Text kann zusätzlich zum Symbol oder Bild angezeigt werden; das Blinkintervall `0` bedeutet kein Blinken.
- **Text / Inhalt / Ausrichtung:** Textdekoration, getrennte Außenabstände, Größe, Drehung und Spiegelung des Inhalts; Zeile oder Spalte, Verteilung, Text- und Inhaltsausrichtung sowie umgekehrte Reihenfolge. Eine ausdrücklich gewählte Inhaltsart im Bereich „Inhalt“ gilt für alle Zustände. Zustandsgröße `0` verwendet die Widget-Größe des Inhalts.
- **Transparenz / Abstand:** Hintergrund und Inhalt haben eigene Opazitäten; vier Innenabstände sind unabhängig einstellbar.
- **Ecken / Rahmen / Äußerer Schatten / Innerer Schatten / Form:** Vier abgerundete oder abgeschrägte Ecken, getrennte Rahmenbreiten und Rahmenstil sowie Schatten mit Versatz, Unschärfe, Größe und Farbe. Formen reichen vom Rechteck bis zum Stern und eigenen Polygonen. Polygonpunkte werden als Prozentpaare eingegeben; ungültige Eingaben fallen auf das Rechteck zurück. Formdrehung und Formradius betreffen Polygone; die normalen Ecken gelten für Rechtecke.

**Vom Widget** übernimmt die Einstellungen des jeweiligen Bereichs dauerhaft von einem anderen Universal Element. Änderungen am Quellwidget wirken sofort; fehlende Quellen und zyklische Verweise führen zu lokalen Einstellungen statt einer Endlosschleife. Farbverweise übernehmen die Standardfarben des Quellwidgets. Der Haken „eigene Farbe“ schaltet einen HEX-Farbwert ein; ohne Haken bleibt die Farbe vererbt. Beim gemeinsamen Kopieren werden interne Verweise angepasst; beim Export müssen die referenzierten Widgets mit enthalten sein. **CSS Allgemein** bleibt aktiv, damit Position und Größe gespeichert werden. Die kleinen roten Umsteigerhinweise lassen sich zentral ausblenden.

![Universal Element mit neutralen Einstellungsbereichen und mehreren Darstellungsformen](/images/grafik-visual-studio/universal-element.png)

Die Funktionen orientieren sich an der [VIS2-Universal-Dokumentation von inventwo](https://github.com/inventwo/ioBroker.vis-2-widgets-inventwo/blob/main/docs/en/widgets/universal/styling-and-shapes.md). Studio verwendet eine eigene Implementierung und benötigt das ioBroker-Paket nicht.

## HA Grafik – Gauges (10)

Ab **0.1.186** gibt es ein eigenes, goldbraun hinterlegtes Instrumenten-Set. Als Funktionsreferenz dient der [aktuelle Quellcode von ioBroker.vis-2-widgets-gauges](https://github.com/ioBroker/ioBroker.vis-2-widgets-gauges/tree/main/src-widgets/src), der zehn Typen enthält. Die README des Referenzprojekts zeigt nur die ersten drei. Studio zeichnet die Instrumente selbst als SVG; ioBroker ist nicht erforderlich. Es handelt sich um eigenständige Studio-Widgets, nicht um einen direkten Import der ioBroker-Konfiguration.

| Widget | Funktion und besondere Einstellungen |
| --- | --- |
| Farbmesser | Farbige Bogenabschnitte, Zeiger, Bogenwinkel und Min./Max.-Beschriftungen. |
| Wasserstand | Kreisförmige Füllstandsanzeige mit einstellbarer Wellenhöhe und optionaler Animation. |
| Batterie | Horizontale oder vertikale Batterie, bis zu 20 Zellen, Ladezustand-Entität und Ladesymbol. |
| Bogenmesser | Fortschrittsbogen, Drehung, bis zu 100 Segmente, Füllung ab Null und Zielwert-Entität. |
| Kompass | Grad und Himmelsrichtung, Nordversatz, Richtungsumkehr, mitdrehende Skala und Geschwindigkeits-Entität. |
| Linearmesser | Horizontaler oder vertikaler Balken beziehungsweise Zeiger mit Haupt-/Unterteilungen und Zielmarkierung. |
| Rundinstrument | Zeigerinstrument mit Farbband, beschrifteter Skala, Bogenwinkel, Drehung und Instrumentenrahmen. |
| Ringe | Bis zu acht getrennte Entitäten mit eigenen Bereichen, Farben, Bezeichnungen und Einheiten; Legende unten, seitlich oder ausgeblendet. |
| Tank | Zylinder, Rechteck oder liegender Tank mit Skala, Füllstand, optionalem Prozentwert und Wellen. |
| Thermometer | Säule und Kugel mit eigenem Wertebereich; Skala links, rechts oder beidseitig. |

Alle Instrumente lesen HA-Zustände und schreiben keine Werte. Ohne Entität gilt der Vorschauwert; eine fehlende oder nicht verfügbare gebundene Entität wird als **—** angezeigt. Werte außerhalb des Bereichs bleiben als Zahl sichtbar, während die Füllung auf 0–100 % begrenzt wird. Ein ungültiger Wertebereich zeigt ebenfalls **—**. Zahlen, Einheiten, Nachkommastellen, Bezeichnung, aktive Farbe, Skalen-/Spur-/Zeiger-/Textfarben und Größen sind konfigurierbar. Bis zu zehn Farbstufen werden nach ihren Obergrenzen sortiert; die erste passende Stufe gilt einschließlich ihres Grenzwerts. Alle Einstellungen und Entitätsbindungen werden im Projekt- und Widget-JSON gespeichert.

Bei Ringen wird die Hauptentität durch die einzelnen Ring-Entitäten ersetzt. Ladezustand, Geschwindigkeit und Zielmarkierungen werden zusammen mit den Hauptwerten abgefragt. Wellen laufen nur in der Runtime und respektieren die Einstellung für reduzierte Bewegung. Die Null- und Vollanzeige bleibt ohne Wellen exakt.

![Alle zehn Gauges als eigenständige Studio-Instrumente](/images/grafik-visual-studio/gauges.png)

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
