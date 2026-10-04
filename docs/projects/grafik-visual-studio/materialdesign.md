---
title: Material Design
description: Externes Material-Design-Widget-Set für Grafik Visual Studio.
---

# Material Design

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
