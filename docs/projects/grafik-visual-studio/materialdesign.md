---
title: Material Design
description: Externes Material-Design-Widget-Set für Grafik Visual Studio.
---

# Material Design

## Originalsymbole (Paket 1.0.1, Studio ab 0.1.216)

Alle 49 Widgets verwenden jetzt die ursprüngliche MDI-Symbolzuordnung als lokale SVGs: blau auf einer weißen Kachel mit abgerundeten Ecken. Es werden keine Icon-Fonts oder externen Bildanfragen benötigt. Das Paket enthält die Pictogrammers-/Apache-2.0-Lizenzhinweise zusätzlich zur MIT-Lizenz. Studio 0.1.216 erlaubt reine Icon-Updates; Standardwerte, Eigenschaftsgruppen und Renderer bleiben geschützt. Bereits registrierte Version 1.0.0 bleibt unverändert; für die neuen Symbole Paket 1.0.1 mit Mindestversion 0.1.216 registrieren. Die Katalog-Webseite benötigt kein weiteres Update.

## Vollständiger Widget-Katalog (Paket 1.0.0, Studio ab 0.1.215)

Das externe Paket enthält **49 Widget-Einträge**. Neben Farbvorschau und Dialogen stehen alle Button-/Icon-Button-Varianten, Input, Select, Autocomplete, Checkbox, Switch, Slider, Slider Round, Value, HTML Card, Icon, Installed Version, linearer/runder Fortschritt, List, Icon List, Table, Alerts, vier Diagramme, Calendar, Top App Bar, Grid/Masonry Views und beide Advanced-View-Varianten bereit.

**Autocomplete:** Menüpunkte im Editor, JSON-Liste, Semikolon-Werteliste oder Optionen der Home-Assistant-Entität wählen. Schreiben erlaubt freie Eingaben; Auswählen verwirft unbekannte Texte. Die Liste filtert beim Tippen und unterstützt Pfeiltasten, Enter und Escape. Erweiterte Optionen ergänzen Eingabelayout, Anhänge, Untertext, Zähler, Symbole und Menüfarben/-schriften. „Felder neu aus der Entität befüllen“ übernimmt Namen, Einheit, Optionen und verfügbare Reglergrenzen.

**Daten und Aktionen:** Schaltaktionen nutzen switch/input_boolean, Zahlen und Texte input_number/input_text, Auswahl select/input_select. Sensoren und Attribute bleiben Anzeigen. Ohne Entität dienen Werte und Aktionen der lokalen Vorschau. Listen können Editor- oder JSON-Zeilen anzeigen; Tabellen lassen sich über ihre Überschriften sortieren. Alerts quittieren eine lokale Warteschlange, eine schreibbare JSON-Entität oder eine getrennte Quittierungs-Entität. JSON Chart liest `axisLabels/graphs`, `labels/datasets` oder Punktlisten. Der Verlauf liest HA Recorder für bis zu zehn Entitäten und 1–168 Stunden. Kalender und Seitenlayouts verwenden die vorhandenen Studio-Funktionen; rekursive Seitenketten werden verhindert.

Für den gemeinsamen Vergleich steht ein [importierbares Vergleichsprojekt](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign/blob/main/comparison/materialdesign-widgetvergleich.json) mit neun Widget-Seiten und einer Referenzansicht bereit. Es enthält keine echten HA-Entitäten. Die genaue Originaloptik und Detailoptionen werden anschließend Widget für Widget verglichen. ioBroker-Theme-IDs, Adapter-Datenpunkte und Binding-Ausdrücke werden nicht automatisch importiert; mehrere Y-Achsen, gestapelte Balken, ioBroker-Timer-Sperren und HTML in Listentexten fehlen derzeit. HTML-Karten zeigen HTML isoliert in einer Sandbox.

Zur erneuten Registrierung Paket **1.0.0**, Mindestversion **0.1.215** und MIT angeben. Die Webseite benötigt **0.1.13**, das den neuen `material-widget`-Renderer sowie Pakete mit bis zu 64 Widgets/40 Eigenschaftsgruppen und 500 KB Manifest erkennt. Bereits veröffentlichte Versionen bleiben unverändert. Die ersten drei Widget-Definitionen bleiben kompatibel für das Update von 0.3.0.

## Dialog iFrame (Paket 0.3.0, Studio ab 0.1.214)

Das dritte Widget öffnet eine HTTP-/HTTPS-Quelle oder einen relativen Pfad im Dialog. **Allgemein**, **iFrame Einstellungen** und **Layout Dialog** bleiben im kompakten Modus sichtbar. Erweiterte Optionen zeigen zusätzlich Button-, Kopfzeilen- und Fußzeilenlayout; vorhandene Werte bleiben beim Ausblenden erhalten.

Unter **iFrame Einstellungen** die Quelle und horizontalen/vertikalen Scrolloptionen setzen. **Nahtlos** entfernt den Rahmen. Standardmäßig ist die Sandbox mit Scripts/Formularen aktiv; **Sandbox deaktivieren** entfernt diese Einschränkung ausdrücklich. Scrollverhalten hängt bei fremden Seiten vom Browser und deren Inhalt ab. CSP oder X-Frame-Options der Zielseite können das Einbetten verhindern. Studio stellt dafür keinen Proxy bereit.

Button oder boolesche Entität, Vollbildschwelle und Schließverhalten entsprechen dem Seiten-Dialog. Im Editor wird kein Dialog geöffnet. Die ioBroker-Theme-Objekte werden durch das Studio-Seitenthema ersetzt.

Zur Registrierung von Paket **0.3.0** Mindestversion **0.1.214** angeben. Der Katalog benötigt Webseiten-Update **0.1.12**, das `material-iframe-dialog` als bekannten Renderer erkennt. Die bereits freigegebene Version 0.2.0 bleibt unverändert.

## Dialog (Paket 0.2.0, Studio ab 0.1.211)

Das zweite Widget öffnet eine andere lokale Studio-Seite im Dialog. Unter **Allgemein → Ansicht** die Zielseite auswählen. Im Editor dient der Klick zur Auswahl; in der Runtime öffnet er das Fenster. Die aktuelle Seite und rekursive Einbettungen sind gesperrt.

Ohne **Erweiterte Optionen anzeigen** sind nur Allgemein und Layout Dialog sichtbar. Mit dieser Option erscheinen Button Layout, Layout Kopfzeile und Layout der Schaltflächen in der Dialogfußzeile. Ausblenden erhält die eingetragenen Werte. Breite, Höhe, Randabstand, Farben, Überlagerung und die Vollbild-Schwelle lassen sich einstellen. Schließen funktioniert über den Button, Escape und wahlweise Außenklick.

Alternativ öffnet eine boolesche Entität das Fenster. Beim Schließen wird `switch` oder `input_boolean` ausgeschaltet. Andere Entitäten bleiben unverändert; nach lokalem Schließen öffnet erst ein neuer Aus/Ein-Wechsel. Vibration und Klicksound hängen von Browser und Gerät ab. Symbole verwenden Text/Unicode, ohne ioBroker-Bildkatalog oder Theme-Objekte zu importieren.

Für Paket 0.2.0 muss die Katalog-Webseite den Renderer `material-dialog` akzeptieren. Das lokale Update ersetzt ausschließlich `src/package.php`; anschließend Version 0.2.0 mit Mindestversion 0.1.211 über die Registrierungsmaske einreichen und prüfen/freigeben.

Das externe [UGSo Material Design](https://github.com/rockbaer2007/ha-grafik-visual-studio-materialdesign) startet mit **Preview Color Schemes**. Paket **0.1.0** benötigt Studio **0.1.210** oder neuer und steht unter MIT. Es ist inspiriert von [ioBroker VIS2 Material Design](https://github.com/typhosj/ioBroker.vis2-materialdesign); Lizenz und Copyright von typhosj und Scrounger sind enthalten.

Die Vorschau zeigt alle **26 Farbreihen**. Klassisch verwendet eine weiße Oberfläche; Material 3 unterstützt helle und dunkle Oberflächen. Die Farbfelder bleiben in allen Stilen unverändert. Überschrift und Widgetgröße lassen sich einstellen; weitere Reihen und breite Paletten sind per Scrollen erreichbar.

- **Gestaltungsstil:** Klassisch, Material 3 oder Projektstandard.
- **Projektstandard:** unter Einstellungen → Allgemein → Material Design auswählen.
- **Farbschema:** Projektstandard folgt dem hellen/dunklen Seitenthema; Hell und Dunkel überschreiben es für dieses Widget.

Das Widget liest keine Home-Assistant-Entität und schreibt keine Zustände. Die ioBroker-Bindung `__mdwThemeDark` wird durch das Studio-Seitenthema ersetzt. „Thema verwenden“ aus ioBroker ist kein Theme-Import in Studio.

## Paketregistrierung testen

Das fertige `.wg` und SHA-256 liegen im Repository unter `dist/`. Über **Registrierung Widget** im [Paketkatalog](https://visualstudio.ugso-software.de/?lang=de) das Paket mit ID `ugso.materialdesign`, Version `0.1.0`, Lizenz MIT, Repository-Link und Mindestversion `0.1.210` einreichen. Erst nach Prüfung und Freigabe erscheint es im Studio-Katalog. Es wird nicht als mitgeliefertes Paket automatisch eingetragen.

Für die lokale Prüfung: Einstellungen → Widget-Pakete → Lokal. Für GitHub: den direkten Link zur `.wg`-Datei verwenden. Weitere Widgets folgen schrittweise anhand der Screenshots und Exporte.
