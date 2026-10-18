---
title: Home Assistant Card Editor
description: Eigene Dokumentation zum ATLAS Home Assistant Card Editor mit Expert-Editor, Import, Export, Ressourcencheck und Home-Assistant-Anbindung.
---

# Home Assistant Card Editor

::: warning Native Negativprüfung mit App 0.1.321: CRC-Lücke offen
Auf .177/.68 mit HA 2026.10.2 sind nach frischen Vollbackups je 21 echte
Editorimporte geprüft. Fehlende, leere, nur aus Leerzeichen bestehende oder
widersprüchliche Namen in HACS-/Paketmanifesten, sieben fehlende Pflichtdateien
einschließlich deklarierter Sprachdateien, unlesbare/abgeschnittene ZIPs und
kaputtes Manifest-/Paket-JSON werden in 19 Fällen je Host korrekt abgelehnt.
Nach jeder Ablehnung und nach Neuladen ist die vollständige Editor-Konfiguration
bis auf den Exportzeitstempel unverändert. Das gültige Kontrollpaket besteht
jeweils mit 112/112.

Ein ZIP mit verändertem README-Inhalt und dadurch falscher CRC-Prüfsumme wird
jedoch auf beiden Hosts fälschlich mit 112/112 angenommen und ersetzt den lokalen
Editorstand. Ein unabhängiger ZIP-Leser bestätigt den CRC-Fehler. Die vorhandene
Prüfung belegt daher keine vollständige ZIP-Integrität. Die CRC-Prüfung ist noch
zu korrigieren; beschädigte Pakete aus dem unveränderten Original neu erzeugen.
Beide ursprünglichen Editorstände wurden aus den Sicherungen exakt
wiederhergestellt; Bestandsdateien, Projekte, Plugins und Papierkorb sind erhalten.
:::

::: info HACS-Titelprüfung ab App 0.1.321
Die beiden Titelprüfungen verwenden jetzt denselben Paketnamen wie die
Manifest-/Script-Prüfungen. Ein leerer oder nur aus Leerzeichen bestehender Name
der ersten Entity-Karte löst dadurch keinen falschen Titelfehler mehr aus.
Originalnamen und Archive werden nicht verändert. Alle 324 lokalen Pakettests
bestehen, darunter 28 neue Prüfungen für JSON/YAML, einzelne Karten, Stapel,
Conditionals und ungültige Manifestnamen. Die vier gesicherten Fehler-ZIPs und
vier Kontrollpakete bestehen unverändert mit 112/112; ihr Rückexport ist bytegleich.
Fehlende oder widersprüchliche Manifestnamen bleiben gesperrt. Das native Update
von 0.1.320 auf 0.1.321 ist auf .177/.68 mit HA 2026.10.2 nach frischen
Vollsicherungen bestanden. Die vier ursprünglichen JSON/YAML-Fehler-ZIPs ohne
Kontrollkarte erreichen im echten Editor jeweils 112/112; ihre Rückexporte sind
bytegleich. Alle acht Karten behalten Namen und Conditional-Bedingungen nach
Import und Neuladen exakt. Bestandsdaten, sieben Projekte und sechs Plugins je
Host sowie beide ursprünglichen lokalen Editorstände sind erhalten. Diese
Prüfung ergänzt die frühere HA-Darstellungsprüfung; neue HA-Ressourcen oder
Dashboards wurden dafür nicht angelegt.
:::

::: info Wörtliche Entity-Namen ab App 0.1.320
Ausdrücklich gesetzte Entity-Namen bleiben beim Import unverändert: `name: ''`,
reine Leerzeichen sowie äußere Leerzeichen und Tabulatoren. Nur ein fehlender
Name erhält weiterhin den bisherigen Ersatznamen. 296 lokale Pakettests bestehen,
darunter 37 neue Prüfungen gegen die unveränderte Originalquelle, JSON/YAML,
verschachtelte Conditionals, Entwurfswiederherstellung, Card-Pakete und HACS.
Bewusstes Umbenennen und Entity-Auswahl bleiben möglich. Bestandsdaten werden
nicht umgeschrieben; früher normalisierte Namen aus Original oder Backup neu
importieren. Das native Update von 0.1.319 auf 0.1.320 ist auf .177/.68 mit
HA 2026.10.2 nach Vollsicherungen bestanden: 64 JSON/YAML-Datei-/Einfügefälle
mit 128 Codeproben nach Import und Neuladen sowie 16 echte Card-Paket-Rundläufe
erhalten die Originalwerte exakt, auch in verschachtelten Conditionals.
Bestandsdaten und beide ursprünglichen lokalen Editorstände sind unverändert.
Der anschließende native HACS-Test auf beiden Hosts besteht mit einer benannten
Kontrollkarte vor den acht Namensfällen: vier JSON/YAML-ZIP-Rundläufe mit jeweils
112/112 Prüfungen und bytegleichen Rückexporten. 72 Export-/Referenzpaare in HA
stimmen vor und nach Neuladen überein (144 gerenderte Kartenproben). DOM-Texte
erhalten auch äußere Leerzeichen/Tabulatoren; HA fasst diese visuell durch normales
CSS zusammen, genauso bei nativen Referenzen. Die Scripts und Sprachdateien wurden
aus den echten ZIPs unverändert lokal geladen; keine neue HACS-Repository-Installation.
:::

::: warning HACS-Prüflücke bis einschließlich App 0.1.320
Beginnt das Paket direkt mit einem leeren Entity-Namen, meldet die Prüfung
110/112: `package-title-present` und `import-summary-title-present` schlagen trotz
eigenem Paketnamen fehl. Das betrifft auch ein Paket, dessen erste Karte einen
Namen nur aus Leerzeichen hat. Die gespeicherten Namenswerte bleiben erhalten;
der Bereitschaftsbericht ist hier aber nicht zuverlässig. Mit benannter
Kontrollkarte davor bestehen die acht unveränderten Namensfälle. Die Titelprüfung
ist ab 0.1.321 korrigiert und auf .177/.68 mit den Original-ZIPs nativ bestätigt.
Die native Fehlanzeige unter 0.1.320 ist mit leerem String reproduziert;
die Leerzeichenvariante ergibt sich aus der Verwendung von `trim()` im Prüfcode.
:::

::: info Einzelkarten-Korrektur ab App 0.1.319
Conditional-Karten werden als vollständiges Expert-Feld übernommen, einschließlich
aller Bedingungen und verschachtelten Karten. Einzelne Entity-Karten behalten
ihren eigenen Namen; bewusstes Umbenennen und die Entity-Auswahl bleiben möglich.
259 lokale Pakettests bestehen, darunter 19 neue Prüfungen des tatsächlichen
Editor-Umwandlungscodes, der Entwurfswiederherstellung und des JSON/YAML-/HACS-Exports.
Gespeicherte Daten werden nicht verändert. Bereits verlorene Inhalte aus der
Originalquelle oder Sicherung erneut importieren. Das native Update auf .177/.68
ist mit HA 2026.10.2 nach Vollsicherungen geprüft: 32 Fälle erhalten die
Originalstruktur über JSON/YAML-Datei-/Einfügeimport und Neuladen. Acht echte
Card-Pakete bestehen Export, Rückimport und Neuladen. Bestandsdaten und beide
ursprünglichen lokalen Editorstände sind unverändert.
:::

::: warning Grenze bis einschließlich App 0.1.319
Der Parser ersetzt `name: ''` weiterhin durch `Imported entity card` und entfernt
äußere Leerzeichen eines Entity-Namens. 16 zusätzliche Kontrollen bestätigen
diese Normalisierung auf beiden Hosts; sie gelten nicht als unveränderter Erhalt
des Originalnamens. Frühere lokale Tests verglichen erst nach der Normalisierung.
Normale eigene Namen und Conditional-Bedingungen sind mit 0.1.319 geprüft;
die entsprechenden Verluste unter 0.1.318 sind behoben. Dieser Durchlauf enthält
keinen neuen nativen HACS-ZIP- oder HA-Darstellungstest.
:::

::: info Import-Vorprüfung ab App 0.1.318
Die Vorprüfung verwendet jetzt denselben Parser wie der tatsächliche Import,
einschließlich verschachtelter Karten und Paket-/Exportpayload-Inhalte.
Nicht unterstützte Markdown-Karten werden bereits vor einer Änderung des
Editorstands abgelehnt. Dies ergänzt keine Markdown-Unterstützung. Unterstützte
einzelne Entity- und Conditional-Karten werden auch als JSON erkannt; YAML wird
strukturiert geprüft. 240 lokale Pakettests bestehen, darunter 27 neue
Paritätsprüfungen. Das native Update auf .177/.68 ist nach Vollsicherungen
geprüft: 24 Markdown-Ablehnungen über Datei-/Einfügeimport erhalten den Editorcode,
acht verschachtelte JSON/YAML-Importe erhalten die Struktur. Vorhandene Daten und
ursprüngliche lokale Editorstände bleiben erhalten, auch nach Neuladen. Die oben
genannten alten Einzelkartenverluste sind mit 0.1.319 erneut geprüft und behoben;
die Namensnormalisierung ist ab 0.1.320 korrigiert und auf .177/.68 nativ geprüft.
:::

::: info Erweiterte Conditional-Anzeige geprüft am 18.10.2026
Mit ATLAS 0.1.317 und HA 2026.10.2 stimmen native Referenzen sowie aus JSON
und YAML exportierte Scripts in 1.008 Sichtbarkeitsprüfungen überein: 14 Varianten,
sechs Zustandsfälle und Browserbreiten von 898 und 2560 CSS-Pixeln auf den beiden
freigegebenen Testsystemen. Geprüft sind implizites UND, verschachteltes UND/ODER/
NICHT, `state`-/`state_not`-Listen, `entity_id`, strikte numerische Grenzen mit
Null und Entitätsbezug, Bildschirm- und Benutzerbedingungen sowie verschachtelte
Conditional-Karten. Speichern und Wiederöffnen erhalten JSON und YAML exakt.
Beide Formate bestehen auf beiden Hosts den echten HACS-Rückimport mit je
112/112 Paketprüfungen und bytegleichem Rückexport. Ursprüngliche lokale
Editorstände und erfasste Bestandsdaten sind erhalten; eigene Testartefakte sind
bereinigt, Testdateien bleiben im Papierkorb wiederherstellbar.
Die Benutzerprüfung umfasst die tatsächlich angemeldete und eine ausgeschlossene
Test-ID. Das ist keine Freigabe aller Karten- oder Bedingungstypen; die Blätter
dieser Matrix sind Core-Entity-Karten. Ein Markdown-Blatt wurde vom tatsächlichen
Import abgelehnt, obwohl die Vorprüfung es als importierbar bezeichnete.
Neue Netzwerktests sind ausschließlich auf 192.168.178.177 und 192.168.178.68
zulässig; frühere Berichte über andere Hosts sind historische Nachweise.
:::

Der **ATLAS Home Assistant Card Editor** ist die erste sichtbare
Referenzanwendung im ATLAS-Umfeld. Er dient dazu, Home-Assistant-Cards visuell
zu entwerfen, vorhandene YAML-Cards zu importieren und exportierbare Card-Pakete
oder HACS-nahe Bundles vorzubereiten.

Seit HA-App **0.1.286** bleiben beim Neuladen und beim JSON-/HACS-Import auch
Template-Zuordnung und Bezugsgrößen für die Größenänderung erhalten. Ein
HACS-Paket lässt sich wieder importieren, wenn der Projektname vom Titel der
ersten Karte abweicht: Verglichen werden die Namen der beiden Paket-Manifeste.
Der Inhalt der Karten und die bestehenden Einstellungen bleiben erhalten.

Der Ablauf Administration → Plugin Hub → HA-Verbindung → Expert-Editor →
Export/Wiederimport wurde in DE/EN/FR mit einem simulierten HA-Endpunkt,
isoliertem Browserprofil und Testplugin geprüft, einschließlich Neuladen und
Container-Neustart. Ergänzende native Prüfungen auf Pi 5 und Proxmox sind
inzwischen abgeschlossen; Umfang und verbleibende Grenzen stehen im
[Entwicklungsstand](/projects/atlas/entwicklungsstand).

Die lokale Demo läuft standardmäßig auf:

```text
http://127.0.0.1:4174/
```

Die Verbindungseinstellungen werden über die Atlas Administration verwaltet:

```text
http://127.0.0.1:4175/
```

## Problem melden (ab 0.1.287)

„Problem melden“ erstellt zunächst lokal eine Vorschau. „Bericht kopieren“
übernimmt den geprüften Text; bei fehlender Zwischenablage bleibt die Vorschau
zum manuellen Kopieren erhalten. Der GitHub-Knopf öffnet nur das Issue-Formular
mit einer Anleitung. Der Bericht wird nicht automatisch übertragen und steht
nicht in der GitHub-URL.

Der Filter entfernt Geheimnisse in strukturierten Feldern, zitierter JSON-/YAML-
Ausgabe, URL-Zugangsdaten und Token-Fragmenten sowie den bekannten HA-Sitzungstoken
in anderem Berichtstext. Cookies und Browser-Speicher werden nicht ausgelesen;
Statusangaben zu konfigurierten Schlüsseln sind ausschließlich Ja/Nein-Werte.
Prüfe vor dem Teilen dennoch Kartentexte, Entitäten und persönliche Angaben.
Das Öffnen des Berichts ändert keine Projekte, Einstellungen oder Plugins.

## Expert-Workflow

Der Editor startet direkt im Expert-Workflow. Der frühere sichtbare
Simple-Modus und der Simple/Expert-Umschalter wurden entfernt. Import,
HA-Card-Import, YAML-Einfügen, Ressourcen-Debug und Entitätsauswahl bleiben als
Werkzeuge erhalten.

Cards werden aus der linken Card-Liste auf eine Home-Assistant-ähnliche
Rasterfläche gelegt. Dort können sie verschoben, bearbeitet, verschachtelt und
als Home-Assistant-YAML exportiert werden.

## Home-Assistant-Anbindung

Der Card Editor kann über Atlas Administration eine Home-Assistant-URL und einen
Access Token übernehmen. Der Token wird nicht dauerhaft in den Editor
geschrieben, sondern nur als Sitzungsübergabe verwendet.

Aktuell unterstützt der Editor:

- Verbindung über die Home-Assistant-WebSocket-API
- Laden von Entitäten über `get_states`
- lokalen Cache für Entitäten und Entitätstypen
- Anzeige des Synchronisationsstatus direkt unter der Verbindung
- Suche und Filter nach Domain, Name oder Entity ID
- Lovelace-Ressourcencheck über Browser-WebSocket und Admin-WebSocket-Proxy

Der Ressourcen-Debug kann über `Ressourcen-Debug anzeigen` eingeblendet werden.
Dort sieht man, ob der Browser-WebSocket, der Admin-WebSocket-Proxy oder ein
Fallback hängt.

## Card-Liste

Die Expert-Cardliste enthält Core-Cards und erkannte Community-Cards. Sie kann
lokale Templates, bekannte HACS-Ressourcen und scan-only Ressourcen anzeigen.

Unterstützte Basis-Cards sind unter anderem:

- Entität
- Entitäten
- Übersicht / Glance
- Button
- Raster
- Sensor
- Vertikaler Stapel
- Horizontaler Stapel
- Thermostat
- Verknüpfung
- Webseite
- Mushroom Template
- Bubble Card
- Tabbed Card V2

Scan-only-Einträge zeigen registrierte Lovelace-Ressourcen, für die ATLAS noch
kein fest eingebautes Card-Mapping kennt. Sie können lokal einem passenden
`custom:*` Lovelace-Card-Typ zugeordnet werden. Nach dieser Zuordnung werden
sie als gemappte Custom Card in der Palette aktiv, können per Drag-and-drop
platziert werden und behalten ihren Resource-Pfad beim Ressourcen-Export.
Nicht benötigte Palette-Einträge, etwa JavaScript-Hilfsressourcen ohne eigene
Card, können lokal als versteckt markiert werden. Versteckte Cards verschwinden
aus der normalen Liste, bleiben aber über die vollständige Liste sichtbar und
können dort wieder eingeblendet werden.
Unter den Import-Werkzeugen gibt es zusätzlich eine opt-in Option für
automatische Cardtypzuordnung. Sie versucht unbekannte registrierte Ressourcen
aus dem Dateinamen einem `custom:*` Card-Typ zuzuordnen und ist deshalb mit
einem roten Sicherheitshinweis versehen.

## Container-Cards

Der Expert-Modus unterstützt Container-Cards für:

- `vertical-stack`
- `horizontal-stack`
- `custom:tabbed-card-v2`

Cards können per Drag-and-drop in diese Container gelegt werden. Bei Tabbed Card
V2 werden Tabs konfiguriert und enthaltene Cards je Tab verwaltet. Bei Stack-
Cards bleiben enthaltene Cards als eigene Elemente erhalten und werden in der
Infobox als Liste angezeigt.

## Import

Der Editor kann Home-Assistant-Card-Konfigurationen importieren:

- YAML aus Datei
- YAML aus Zwischenablage
- JSON
- ATLAS Card Package
- HACS-Bundle mit eingebettetem `atlas/*.atlas-card.json`

Beim Import erkennt ATLAS `card_mod`- und `uix`-Styles. Entity-Styles werden den
jeweiligen Entitäten zugeordnet; globale Styles bleiben als eigener Style-Block
erkennbar. Der ursprüngliche YAML-Code soll so weit wie möglich erhalten bleiben
und nur bei echten Änderungen angepasst werden.

Handgeschriebene `custom:tabbed-card-v2`-Cards mit `tabs[].card`,
verschachtelten `horizontal-stack`-/`vertical-stack`-Bereichen und rohen Custom
Cards werden erkannt und direkt im Expert-Modus als Containerstruktur geöffnet.

## Export

Der Editor kann verschiedene Artefakte erzeugen:

- Home-Assistant-YAML
- Expert-HA-Card-YAML
- Card-Script
- Card-Paket
- HACS-nahes Bundle
- Ressourcenliste

Beim HA-Card-Export kann gewählt werden, ob Styles als `card_mod` oder als
`uix` ausgegeben werden. Exportdateien erhalten bei Namenskollisionen wie in
Windows automatisch eine Zählung.

### Geprüfter HACS-Bundle-Durchlauf

Mit App **0.1.307** ist ein gemischtes Core-/Bubble-/Mushroom-Projekt unter
HA Core **2026.10.1** isoliert geprüft: ZIP-Import, echter Browser-Download,
Wiederimport und erneuter Export erhalten Felder, Rasterdaten und
Card-Konfiguration. Das erneut exportierte ZIP ist im Test bytegleich.
Die Bundle-Prüfung vergleicht den Projektnamen mit dem geprüften Paketnamen;
abweichende Namen innerer Cards erzeugen keine falschen Titelkonflikte mehr.

Das exportierte Script wurde mit Bubble **3.4.2** und Mushroom **5.2.3** in
echtem HA dargestellt, einschließlich Live-Zustandswechsel. Die HA-Darstellung
verwendet generierte Stacks; erhaltene Rasterdaten garantieren keine identische
Pixelgeometrie. Die isolierte Bereitstellung erfolgte über `/local/`; ein
HACS-Repository-Download wird dadurch nicht bestätigt.

### Sprachdateien im exportierten Script

Ab App **0.1.308** lädt das generierte Card-Script `locales/en.json` und die
gewählte Sprache relativ zur eigenen Script-Adresse. JavaScript und den
benachbarten Ordner `locales/` gemeinsam auf derselben HA-Adresse bereitstellen;
die Lovelace-Ressource muss vom Typ `module` sein. Die Card folgt der HA-Sprache.
Mit `language: de` oder `language: fr` in der Card-Konfiguration lässt sich diese
Wahl überschreiben; `de-DE` und `fr-FR` verwenden die jeweilige Basissprache.

Titel, Demo-Entitäten-Hinweis und eigene Fehlermeldung verwenden die Sprachdatei.
Fehlende, ungültige oder unvollständige Texte fallen einzeln auf `en.json`, dann
auf eingebautes EN zurück. Das Script funktioniert auch ohne Sprachdateien.
Ein abweichender eigener `title` oder `replacement_hint` hat Vorrang. Eigene
Feldnamen und Entitäts-IDs bleiben erhalten; HA-/Community-Texte übersetzt HA.
Dateien werden pro Sprache einmal je Seitenaufruf geladen. Nach Änderungen
die Seite neu laden; nach Script-Updates gegebenenfalls den Ressourcen-URL mit
einer neuen Versionsabfrage versehen.

EN/DE/FR werden unabhängig von der Editor-Sprache exportiert. DE/FR enthalten
ohne ausgeführten Übersetzungsadapter gekennzeichnete englische Fallbacks und
benötigen Übersetzung/Prüfung.

### Gemeinsame HACS-Auslieferung ab 0.1.309

Das exportierte ZIP enthält `hacs.json` im Hauptverzeichnis sowie Script und
Sprachdateien unter `dist/`, beispielsweise `dist/energy-kitchen.js` und
`dist/locales/en.json`. Das vollständige ZIP in ein eigenes GitHub-Repository
namens `energy-kitchen` entpacken und dieses in HACS als Dashboard-Repository
hinzufügen. Script-Dateiname ohne `.js` und Repository-Name stimmen dabei überein.
Nicht das ATLAS-Integrationsrepository dafür verwenden.

HACS installiert den Inhalt von `dist/` nach `www/community/energy-kitchen/`.
Die Ressource lautet `/hacsfiles/energy-kitchen/energy-kitchen.js`; die JSON-Dateien
liegen daneben in `locales/`. HACS registriert die Modulressource im Speicher-Modus;
im YAML-Modus die im Bundle dokumentierte Ressource selbst eintragen.

Das Script nicht zusätzlich ins Repository-Hauptverzeichnis kopieren und keinen
einzelnen JavaScript-Release-Anhang veröffentlichen: HACS kann diesen statt
`dist/` auswählen. Das Export-ZIP ist kein `zip_release`-Installationspaket.
HACS 2.0.5 kann bei Script-Dateinamen, die mit `dist` beginnen, Sprachdateien
auslassen; ATLAS stoppt diesen Export mit einer Meldung. Einen anderen
HACS-Script-Dateinamen wählen. Vorhandene Projekte bleiben erhalten.

Der echte GitHub-/HACS-Weg ist zusätzlich unter isoliertem HA 2026.10.1 mit
HACS 2.0.5 geprüft: GitHub-Gerätefreigabe durch den Benutzer, Registrierung als
benutzerdefiniertes Dashboard-Repository und Download vom Zweig `main`.
Script und EN/DE/FR werden bytegenau installiert; HACS registriert die
Modulressource automatisch. Ältere ATLAS-Bundles bleiben importierbar.

Als öffentliches Beispiel dient das ausdrücklich als Test gekennzeichnete
[Card-Export-Repository](https://github.com/rockbaer2007/atlas-hacs-delivery-card).
In HACS über das Hauptmenü **Benutzerdefinierte Repositories** öffnen, diese
GitHub-Adresse eintragen, Typ **Dashboard** wählen und **hinzufügen** klicken.
Danach **Locale test card** öffnen, **Herunterladen** bestätigen und den Browser
neu laden. Die Ressource ist
`/hacsfiles/atlas-hacs-delivery-card/atlas-hacs-delivery-card.js`.
In `v0.1.0` sind DE/FR gekennzeichnete englische Fallbacks. `v0.1.1` enthält
manuell übersetzte Testtexte: „Wohnzimmer 0.1.1“ und „Salon 0.1.1“.
Das ist kein Nachweis einer automatischen Übersetzung. Bubble Card und Mushroom
werden für dessen gemischte Beispiel-Card zusätzlich benötigt.

Auch der getaggte Durchlauf `v0.1.0` → `v0.1.1` → `v0.1.0` ist unter
HA 2026.10.1/HACS 2.0.5 isoliert geprüft. Vorher ein vollständiges Backup sichern.
Im Repository-Menü **Informationen aktualisieren** wählen. HACS erkennt die
neue Version als ausstehende Aktualisierung; über **Erneut herunterladen** die
angebotene Version installieren und anschließend den Browser neu laden.
Für die geprüfte manuelle Neuinstallation der alten Version unter
**Erneut herunterladen** den Abschnitt **Benötigst du eine andere Version?**
öffnen, bei **Release** `v0.1.0` wählen, herunterladen und erneut laden.
HACS empfiehlt dort ausdrücklich die Wiederherstellung eines Backups statt
dieser Versionsauswahl zum Zurücksetzen. Die Neuinstallation ersetzt nur die
Card-Dateien; sie stellt keine migrierten Daten aus einem Backup wieder her.

Beide Releases verwenden `dist/` ohne einzelnen JavaScript-Release-Anhang.
Script und alle drei Sprachdateien entsprechen nach jedem Schritt exakt dem
gewählten Tag. Die Modulressource behält ihre ID; HACS ändert ihren `hacstag`.
Andere Ressourcen, Einstellungen, Projekte und Abhängigkeiten bleiben erhalten.
Die alte Version funktioniert auch nach einem Neustart des Testsystems.
HACS bietet `v0.1.1` danach weiterhin als Update an; die Auswahl sperrt spätere
Updates nicht dauerhaft.

Das ist eine benutzerdefinierte Registrierung, kein Eintrag in der zentralen
HACS-Standardliste. Pi 5 und Proxmox wurden für diese Prüfung nicht verändert.

### Fehlgeschlagene und unterbrochene Updates

Ab ATLAS **0.1.310** prüfen neu generierte Card-Scripts EN und alle beim Export
ausgewählten Sprachdateien, auch inaktive Sprachen. Fehlt eine Datei oder ist
sie nicht lesbar bzw. ungültiges JSON mit unpassenden Sprachmetadaten, erscheint
ein kompakter Hinweis mit den betroffenen Dateipfaden. Der Reparaturtext ist
unabhängig von diesen Dateien fest in DE/EN/FR eingebaut. Card und Live-Zustände
bleiben mit dem bisherigen Sprach-Fallback nutzbar.

In HACS das vollständige Card-Paket erneut herunterladen, dann den Browser neu
laden; bei Bedarf die Sicherung wiederherstellen. Nach erfolgreicher Reparatur
und Neuladen verschwindet der Hinweis. Alte bereits installierte Scripts müssen
neu exportiert und ausgeliefert werden.

Ab **0.1.311** tragen neu exportierte Scripts und Sprachdateien zusätzlich eine
gemeinsame deterministische Paketkennung (`_meta.packageId` in den Sprachdateien).
Eine fremde oder fehlende Kennung löst ebenfalls den Reparaturhinweis aus;
betroffene Texte werden nicht angewendet, EN beziehungsweise eingebautes Englisch
bleibt als Fallback verfügbar. Beim Übersetzen die Kennung beibehalten. Keine
Kennungen aus anderen Paketen übernehmen, um einen Hinweis zu unterdrücken.
Die Prüfung erkennt versehentlich gemischte Exporte, ist aber keine Signatur
und erkennt keine Textänderungen mit unveränderter Kennung. Identische Exporte
haben dieselbe Kennung. Alte Scripts werden nicht nachträglich geändert.
Es gibt keine automatische Reparatur oder Wiederherstellung.
Die neue Paketprüfung ist zuerst isoliert mit HA 2026.10.1/HACS 2.0.5 geprüft:
gemischtes EN/FR, fehlende Kennung, weiter gerenderte Cards und Reparatur nach
Neuladen. Pi 5 und Proxmox blieben bei dieser isolierten Prüfung auf 0.1.310.

Anschließend sind App-Update und Paketprüfung auf beiden Hosts mit 0.1.311
getestet: eigene `/local/`-Cards, gemischtes EN/FR, fehlende FR-Kennung und
Reparatur nach Neuladen. Bestehende Einstellungen, Projekte und geprüfte Dateien
bleiben erhalten. Separater damaliger Befund: Der File-Studio-Papierkorb lag im
austauschbaren App-Container. Ausschließlich unsere alten Testordner waren dort
vorhanden; sie wurden aus PC-Kopien mit ursprünglichen Metadaten rekonstruiert.
App 0.1.312 korrigiert die Ablage; Containerwechsel und Sicherungsrückkehr sind
isoliert geprüft. Vor dem ersten Update müssen die alten Ablagen noch im alten
Container übernommen und gesichert werden; siehe [File Studio](../atlas-plugins/file-studio.md).
Anschließend sind Übernahme und Update auf 0.1.312 auch auf Pi 5 und Proxmox
mit Datenerhalt geprüft. Dies ist kein
erneuter nativer HACS-Repository-Installationstest.

Das Update auf 0.1.310 und diese Prüfung sind auch auf Proxmox und Pi 5 nach
frischen Backups getestet: eigene neue Test-Cards, fehlendes FR sowie EN und
Wiederherstellung nach Neuladen, bei erhaltenen Einstellungen, Projekten und
externen Plugins. Die native Prüfung verwendet separate `/local/`-Testressourcen,
keine erneute GitHub-/HACS-Installation. Ein vorübergehender Lesefehler kann
ebenfalls einen Hinweis auslösen; auf Proxmox verschwand ein solcher erster
Vorschauhinweis nach frischem Neuladen. Ein Hinweis allein beweist keinen
dauerhaften Dateidefekt.

Unter isoliertem HA 2026.10.1/HACS 2.0.5 wurden Fehler gezielt in einer eigenen
Testkopie ausgelöst: Das neue Script wurde echt von GitHub geladen und geschrieben,
danach wurden Sprachdownloads als fehlgeschlagen gemeldet oder der Prozess vor
deren Abschluss hart beendet. Nur diese HACS-Testkopie enthielt die Testinstrumentierung.

Bei einem gemeldeten Downloadfehler zeigt HACS einen Fehler und stellt die alte
Card einschließlich EN/DE/FR automatisch wieder her. Beim harten Prozessabbruch
bleiben dagegen das neue Script und fehlende Sprachdateien zurück, auch nach
Neustart. HACS kann dabei noch die alte installierte Version anzeigen. Der
eingebaute EN-Fallback lässt die Card trotzdem erscheinen; sichtbare Darstellung
und Versionsanzeige allein beweisen daher keine vollständige Installation.

Nach Beheben der Fehlerursache wurde **Erneut herunterladen** mit dem bekannten
alten Release erfolgreich geprüft. Danach den Browser neu laden und Script,
alle Sprachdateien, Ressourcenregistrierung und Darstellung kontrollieren.
Eine eigene vollständige Docker-HA-Konfigurationssicherung wurde zusätzlich in
ein neues leeres Testvolume zurückgespielt: alle 2.500 gesicherten Dateien vor
dem Start bytegleich, danach HACS, Cards und Live-Zustände wieder funktionsfähig.
Einstellungen, Dashboard und Abhängigkeiten blieben erhalten.

Die temporäre HACS-Sicherung ersetzt kein eigenes Backup. Automatische Reparatur
nach Prozessabbruch wird nicht zugesichert. Das ist ein kontrollierter Fehlertest
und eine Docker-Volume-Wiederherstellung, kein Nachweis für jeden Netz-/Datenträgerfehler,
eine HAOS-Backup-Wiederherstellung oder andere HACS-Versionen.

## Tabbed Card V2

Tabbed Card V2 wird im Editor als eigene ATLAS-Card behandelt und exportiert
als:

```yaml
type: custom:tabbed-card-v2
```

Erwartete Ressource:

```text
/hacsfiles/tabbed-card-v2/tabbed-card-v2.js
```

Voraussetzung für den Export: Die **ATLAS Tabbed Card V2** muss in Home
Assistant installiert sein. Sie gehört zur ATLAS-Plugin-/Card-Linie und wird
über das ATLAS-Repository bereitgestellt:

`https://github.com/rockbaer2007/atlas`

Der Editor weist darauf hin, dass Tabbed Card V2 eine eigene Card ist und sich
vom ursprünglichen `kinghat/tabbed-card` ableitet, aber als eigenständige
ATLAS-Variante geführt wird.

Der eingebaute Home-Assistant-Editor der Card kann YAML oder JSON direkt
übernehmen. Mehrzeilige YAML-Blöcke wie `>-` und `|-` bleiben dabei als
mehrzeilige Werte erhalten, damit Mushroom-Template-Chips, Jinja-Ausdrücke und
`card_mod`-Styles nicht beim Übernehmen zerstört werden.

Die Deckkraftwerte für aktive und inaktive Tab-Hintergründe werden vor dem
Tabwechsel als stabile Farbwerte gerendert. Dadurch bleiben transparente
Tab-Hintergründe auch nach dem Umschalten zwischen Tabs erhalten.

### Tabbed Card V2 Styling

Tabbed Card V2 übernimmt weiterhin die Material-Tab-Variablen und ergänzt
eigene Variablen für Tab-Hintergründe, Rundungen und Abstände:

| Name | Standard | Beschreibung |
| --- | --- | --- |
| `--mdc-theme-primary` | `--primary-color` | Text, Indikator und Akzentfarbe des aktiven Tabs. |
| `--mdc-tab-text-label-color-default` | `--secondary-text-color` | Textfarbe inaktiver Tabs. Für Transparenz sollte ein `rgba(...)`-Wert mit Alpha-Kanal genutzt werden. |
| `--mdc-typography-button-font-size` | `14px` | Schriftgröße der Tab-Beschriftung. |
| `--tabbed-card-v2-card-background` | Home-Assistant-Card-Hintergrund | Hintergrund der äußeren Card. Für Glas-/Overlay-Layouts `transparent` nutzen. |
| `--tabbed-card-v2-card-border` | Home-Assistant-Card-Rahmen | Rahmen der äußeren Card. |
| `--tabbed-card-v2-card-border-radius` | Home-Assistant-Card-Rundung | Rundung der äußeren Card. |
| `--tabbed-card-v2-content-padding-side` | `0` | Gleicher Abstand links und rechts innerhalb des Card-Inhalts. |
| `--tabbed-card-v2-content-padding-bottom` | `0` | Unterer Abstand innerhalb des Card-Inhalts. |
| `--tabbed-card-v2-tabbar-background` | `transparent` | Hintergrund der gesamten Tab-Leiste. |
| `--tabbed-card-v2-active-background` | `transparent` | Hintergrund des aktiven Tabs. |
| `--tabbed-card-v2-active-background-opacity` | `100` | Deckkraft des aktiven Tab-Hintergrunds von `0` bis `100`. |
| `--tabbed-card-v2-inactive-background` | `transparent` | Hintergrund inaktiver Tabs. |
| `--tabbed-card-v2-inactive-background-opacity` | `100` | Deckkraft inaktiver Tab-Hintergründe von `0` bis `100`. |
| `--tabbed-card-v2-hover-background` | `--secondary-background-color` | Hintergrund beim Hover oder Fokus eines Tabs. |
| `--tabbed-card-v2-tab-border-radius-top` | `0` | Rundung oben links und oben rechts pro Tab. |
| `--tabbed-card-v2-tab-border-radius-bottom` | `0` | Rundung unten links und unten rechts pro Tab. |
| `--tabbed-card-v2-tabs-padding-left` | `0` | Abstand links vor dem ersten Tab. |
| `--tabbed-card-v2-tabs-padding-top` | `0` | Abstand oberhalb der Tab-Leiste. |
| `--tabbed-card-v2-tabs-gap` | `0` | Abstand zwischen den Tabs. |
| `--tabbed-card-v2-indicator-inset` | `0` | Horizontaler Innenabstand des aktiven Tab-Indikators. |
| `--tabbed-card-v2-indicator-border-radius` | `0` | Rundung des aktiven Tab-Indikators. |

![Tabbed Card V2 Styling im Home-Assistant-Editor](/images/atlas/tabbed-card-v2-0.1.7.png)

![Tabbed Card V2 Ergebnis mit abgerundeten Tabs](/images/atlas/tabbed-card-v2-result-0.1.7.png)

Beispiel:

```yaml
type: custom:tabbed-card-v2
styles:
  --mdc-theme-primary: "#ff9800"
  --mdc-tab-text-label-color-default: "rgba(255,255,255,0.75)"
  --tabbed-card-v2-card-background: "transparent"
  --tabbed-card-v2-card-border: "0.2px solid var(--primary-color)"
  --tabbed-card-v2-card-border-radius: "12px"
  --tabbed-card-v2-content-padding-side: "16px"
  --tabbed-card-v2-content-padding-bottom: "16px"
  --tabbed-card-v2-tabbar-background: "rgba(0,0,0,0.18)"
  --tabbed-card-v2-active-background: "#ff9800"
  --tabbed-card-v2-active-background-opacity: 35
  --tabbed-card-v2-inactive-background: "#ffffff"
  --tabbed-card-v2-inactive-background-opacity: 8
  --tabbed-card-v2-hover-background: "rgba(255,255,255,0.12)"
  --tabbed-card-v2-tab-border-radius-top: "12px"
  --tabbed-card-v2-tab-border-radius-bottom: "6px"
  --tabbed-card-v2-tabs-padding-left: "8px"
  --tabbed-card-v2-tabs-padding-top: "8px"
  --tabbed-card-v2-tabs-gap: "6px"
  --tabbed-card-v2-indicator-inset: "10px"
  --tabbed-card-v2-indicator-border-radius: "999px"
tabs:
  - attributes:
      label: Light
    card:
      type: button
      entity: light.bed_light
```

## Aktueller Status

::: info Update und Gesamtprojekt auf Proxmox und Pi 5 mit 0.1.317 geprüft
Nach frischen HA-Sicherungen bestehen auch die nativen Updates und der
Gesamtprojekt-Durchlauf mit verschachtelten Core-, Bubble- und Mushroom-Karten:
Speichern/Wiederöffnen, YAML/JSON, echte HACS-Rückimporte mit bytegleichen
Rückexporten und je 112/112 Paketprüfungen. Fehlende numerische Conditional-Grenzen
werden abgelehnt; `above: -1`, Jinja und CSS bleiben erhalten. Conditional blendet
bei -2 aus und bei 18 wieder ein. Texte, SVG-Symbole und Farben ändern sich live.
756 CSS-Vergleiche stimmen mit nativen Referenzkarten überein. Je zwei
Hell-/Dunkel-Wechsel ohne Neuladen erhalten alle 19 beobachteten Instanzen.
Nach geordneten HA-Core-Neustarts verbinden sich die Editoren automatisch;
frische Jinja-Updates funktionieren ohne Neuladen. Auf dem Pi wurde der kurze
Zwischenstatus nicht erfasst; die anschließende Verbindung und Aktualisierung
sind geprüft. Umfang: Chrome auf dem PC, HA 2026.10.1, Mushroom 5.2.3,
Proxmox mit vorhandenem UIX 8.4.0/Bubble 3.4.2, Pi mit getrenntem temporärem
Card-Mod 4.2.1/Bubble 3.4.1. Die reguläre Kartenansicht dient als CSS-Referenz;
eine HA-Panelansicht kann eigene Radien überschreiben. Lokale Editorstände und
ursprüngliche Standardthemes sind wiederhergestellt; die Testdateien bleiben
im Papierkorb wiederherstellbar. Frühere Exporte müssen neu erzeugt werden.
:::

::: info Gesamtprojekt-Durchlauf mit 0.1.317 isoliert bestanden
Conditional-Importe erhalten vollständige Bedingungsdaten: numerische Grenzen
wie `above: -1` und `below: 0`, Zustandslisten und verschachtelte logische
Bedingungen bleiben in YAML/JSON und HACS erhalten. Fehlende oder ungültige
numerische Grenzen blockieren Import und Paketfreigabe mit einem Fehlerhinweis.
Der geprüfte Gesamtprojekt-Durchlauf umfasst Speichern/Wiederöffnen, echte
HACS-Rückimporte mit bytegleichen Rückexporten, dynamische Jinja-Texte/Symbole/
Farben, bedingtes Aus-/Einblenden, acht Theme-Wechsel ohne Neuladen und 972
CSS-Vergleiche. Nach HA-Ausfall verbinden sich beide Editoren ohne Neuladen
erneut; frische Template-Updates funktionieren. Card-Mod 4.2.1 und UIX 8.4.0
wurden getrennt mit HA 2026.10.1, Bubble 3.4.2 und Mushroom 5.2.3 in Chrome auf
dem PC geprüft. Vorhandene Daten bleiben erhalten; bei dieser isolierten Prüfung
blieben Pi 5 und Proxmox noch bei 0.1.316. Bereits verlorene Grenzen lassen sich nur aus der
ursprünglichen Quelle/Sicherung wiederherstellen. Bestehende Scripts neu exportieren.
Die Prüfung ersetzt keine vollständige Validierung aller HA-Bedingungstypen.
:::

::: info Theme-Wechsel auf Proxmox und Pi 5 geprüft am 17.10.2026
Nach frischen HA-Sicherungen ist der Wechsel ohne Neuladen auch auf beiden
Hosts mit ATLAS 0.1.316 und HA 2026.10.1 geprüft: Card-Mod 4.2.1 und UIX 8.4.0
jeweils getrennt, mit Mushroom 5.2.3 und Bubble 3.4.2 auf Proxmox bzw. 3.4.1
auf dem Pi. Je Engine und Host wechseln zwölf native/exportierte Core-, Bubble-
und Mushroom-Karten siebenmal zwischen benutzerdefiniertem und Standardtheme.
1.920 CSS-Vergleiche bestehen; Dokument und Karteninstanzen bleiben gleich.
Vererbte Farben/Radien folgen dem Theme, feste Überschreibungen bleiben erhalten.
Die Prüfschaltflächen nutzen den nativen HA-Theme-Handler. Einrichtung und
Engine-Wechsel liegen außerhalb der Messfolgen ohne Neuladen. Die ursprünglichen
Standardthemes und Erweiterungseinstellungen sind wiederhergestellt; vorhandene
Dateien, Projekte und Plugins bleiben erhalten. Native Prüfungen verwenden
passive Sensoren und Chrome auf dem PC, keinen ARM64-Browser-Benchmark.
:::

::: info Theme-Wechsel ohne Neuladen isoliert geprüft am 17.10.2026
Mit ATLAS 0.1.316 und HA 2026.10.1 wechseln bereits angezeigte Core-, Bubble-
und Mushroom-Karten zwischen Hell und Dunkel, ohne Seite oder Karten neu aufzubauen.
Card-Mod 4.2.1 und UIX 8.4.0 wurden getrennt mit Bubble 3.4.2 und Mushroom 5.2.3
geprüft: je sieben Wechsel zwischen benutzerdefiniertem und Standardtheme,
insgesamt 960 Vergleiche berechneter CSS-Werte. Vererbte Farben und Radien wechseln;
feste Kartenüberschreibungen bleiben unverändert. Native Referenz und exportiertes
Script stimmen überein; Dokument- und Kartenidentitäten bleiben durchgehend gleich.
Die isolierten Prüfschaltflächen verwenden den nativen HA-Theme-Handler;
Profilnavigation oder Neuladen gehören nicht zur Messfolge. Vorherige Daten,
neun Projekte und bestehende Dateien bleiben erhalten. Pi 5 und Proxmox wurden
nicht abgefragt oder verändert. Andere Themes, Browser und Versionen benötigen
eigene Prüfungen; ein erneuter HACS-UI-Rundlauf ist nicht Teil dieser Prüfung.
:::

::: info Bubble-CSS und UIX-Vererbung korrigiert in 0.1.316
0.1.315 verlor Bubble-CSS als Zeichenkette unter `styles: |` beim normalen
YAML-/JSON-Kartenimport. 0.1.316 erhält diesen Text samt Leerraum, Zeilenumbrüchen
und leerer Zeichenkette bei Einzelkarten, verschachtelten Karten, HACS-Export
und Rückimport. Bisherige `styles`-Objekte bleiben unterstützt.

Neu erzeugte Scripts verwenden für Wurzelkarten mit `uix`/`card_mod` den normalen
Home-Assistant-Kartenwrapper. Dadurch kann UIX auch den Wurzel-Stack ohne eigenes
`ha-card` gestalten; seine CSS-Variablen werden an die Unterkarten vererbt.
Style-Blöcke werden weder flach zusammengeführt noch auf andere Karten kopiert.

Isoliert geprüft mit HA 2026.10.1, Bubble 3.4.2, Mushroom 5.2.3 und UIX 8.4.0:
Core/Bubble/Mushroom stimmen in Hell, Dunkel und nach Neuladen mit der nativen
Referenz überein (180 Vergleiche berechneter CSS-Werte). Die Elternfarbe ist
absichtlich anders als die Ersatzfarbe: grüne/violette Rahmen werden jetzt
korrekt vererbt. Bubble-Überschreibungen behalten Hintergrund, 3-px-Rahmen und
9-px-Radius. Speichern/Öffnen und HACS-UI-Rückimport/Rückexport sind geprüft;
112/112 Paketprüfungen und bytegleiche ZIPs ergänzen die sichtbare Prüfung.

**Für vorhandene Cards:** Nach dem Update das ursprüngliche Projekt erneut
exportieren und Script sowie zugehörige Sprachdateien gemeinsam ersetzen.
Bereits verlorenes Bubble-CSS aus Original-YAML/JSON oder einer Sicherung neu
importieren; das Update kann verworfenen Inhalt nicht rekonstruieren. Gespeicherte
Projekte und Dateien werden nicht automatisch umgeschrieben.

Nach frischen HA-Sicherungen ist auch das Update von 0.1.315 auf 0.1.316 auf
Proxmox und Pi 5 geprüft: je sechs Core-/Bubble-/Mushroom-Karten mit UIX 8.4.0,
HA 2026.10.1, Mushroom 5.2.3 und Bubble 3.4.2 (Proxmox) bzw. 3.4.1 (Pi).
240 berechnete CSS-Vergleiche einschließlich Neuladen bestehen; YAML-/JSON-Stile
bleiben erhalten, HACS-Rückexporte sind bytegleich und bestehen je 112/112
Paketprüfungen. Die ursprünglichen lokalen Editorstände sind vollständig
wiederhergestellt. Geprüft wird im vorhandenen dunklen Theme mit passiven Sensoren;
andere HA-/Styling-Versionen benötigen eigene Prüfungen. Die isolierte Prüfung
bereits angezeigter Karten bei Theme-Wechseln ist oben gesondert beschrieben.
:::

::: info Native CSS-Prüfung auf Proxmox und Pi 5, 17.10.2026
Nach frischen HA-Sicherungen und zusätzlichen ATLAS-Dateikopien wurden
Card-Mod 4.2.1 und UIX 8.4.0 auch auf beiden echten Hosts getrennt geprüft:
HA 2026.10.1, Mushroom 5.2.3, ATLAS-App 0.1.315. Erzeugtes ATLAS-Script und
native Referenz stimmen bei dynamischen Jinja-Farben/Rahmen, 3-Pixel-
Shadow-DOM-Abstand, Hintergrund und Rundungen überein. Die Farben wechseln
beim natürlichen Minutenwechsel ohne Neuladen. Es werden nur passive Sensoren
gelesen und eigene Testkarten verwendet; keine Geräte werden geschaltet.

UIX wendet den 17-Pixel-Radius an und bevorzugt bei konkurrierenden Blöcken
`uix` (37 statt 31 Pixel). Card-Mod ignoriert `uix`. `uix_style` bewirkt bei
beiden Erweiterungen weiterhin keine 7-Pixel-Innenabstände. Neuladen ist mit
beiden Erweiterungen geprüft. Die vorhandene Browser-Skalierung kann berechnete
Rahmenbreiten auf physische Pixel runden; Export und Referenz bleiben identisch.

Der Erweiterungswechsel benötigte HA-Neustarts. Vorhandenes UIX auf Proxmox ist
wieder aktiviert; zusätzliche Pi-Integration und eigene Testressourcen sind
nach der Prüfung entfernt. Eigene Testdateien liegen im Papierkorb.
Einstellungen, ursprüngliche
Dateien, jeweils vier vorhandene ATLAS-Projekte und sechs Plugins bleiben
erhalten. Es gibt keine neue ATLAS-Version. Die Prüfung gilt für die genannten
Versionen und Regeln, nicht für beliebiges CSS oder alle Themes.
:::

::: info CSS-Darstellung isoliert geprüft, 17.10.2026
Mit App 0.1.315, HA 2026.10.1 und Mushroom 5.2.3 wurden **Card-Mod 4.2.1**
und **UIX 8.4.0** in getrennten HA-Testinstanzen geprüft. Die erzeugten ATLAS-
Scripts zeigen dieselben berechneten Stile wie die entsprechenden nativen Karten:
Jinja-Farbe und 4-Pixel-Rahmen wechseln ohne Neuladen blau → rot → blau;
Shadow-DOM-Schriftabstand beträgt 3 Pixel. Der UIX-Radius beträgt 17 Pixel.
Eine Core-Referenz bestätigt Hintergrund, 6-Pixel-Rahmen und 23-Pixel-Radius.
Neuladen und Neustart sind geprüft; Karten derselben Entität ohne Stil bleiben
unverändert. Pi 5 und Proxmox wurden für diese Prüfung nicht verändert.

**Grenzen:** `uix_style` bleibt als importiertes Datenobjekt erhalten, hat in
diesen Versionen aber keine CSS-Wirkung. Für UIX `uix: { style: ... }` verwenden.
Bei gleichzeitigem `card_mod` und `uix` bevorzugt UIX den `uix`-Block; ATLAS
vereinigt beide nicht. Card-Mod führt `uix` nicht aus. Die UIX-Exportwahl bleibt
eine strukturelle Konvertierung und übersetzt keine CSS-Selektoren oder Jinja-
Variablen. Die frühere Bezeichnung „UIX legacy“ im Test war nur ein Kartenname,
kein Nachweis eines unterstützten Alias.

In **CSS-Templates** dieser Erweiterungen `config.entity` verwenden; Mushrooms
eigene Text-/Symbol-/Farbtemplates können dagegen `entity` verwenden.
`mushroom-state-info$` passt nicht zur geprüften Mushroom-Version. Der geprüfte
Selektor lautet `ha-tile-info$`; interne DOM-Strukturen können sich ändern.

```yaml
type: custom:mushroom-template-card
entity: input_boolean.deine_testentitaet
primary: "{{ 'An' if is_state(entity, 'on') else 'Aus' }}"
card_mod: # Bei UIX stattdessen uix:
  style:
    .: |
      ha-card {
        border: 4px solid {{ 'red' if is_state(config.entity, 'on') else 'blue' }};
      }
    ha-tile-info$: |
      .info { letter-spacing: 3px; }
```

Card-Mod muss als Frontend-Modul geladen sein. UIX wird als Integration
installiert und unter **Geräte & Dienste** hinzugefügt, anschließend die Seite
neu laden. Beide Erweiterungen nicht zusammen laden: siehe
[UIX-Migration](https://github.com/Lint-Free-Technology/uix/blob/v8.4.0/docs/source/faq.md),
[UIX-Einrichtung](https://github.com/Lint-Free-Technology/uix/blob/v8.4.0/docs/source/quick-start.md)
und [Card-Mod](https://github.com/thomasloven/lovelace-card-mod/tree/v4.2.1).
Die Prüfung deckt die genannten Regeln ab, nicht beliebiges CSS oder alle Themes.
Originalvorlagen und Bestandsdaten sind gesichert; nur eigene Testkopien wurden
angepasst. Es war keine Änderung des ATLAS-Laufzeitcodes nötig.
:::

::: info Update auf 0.1.315 auf Proxmox und Pi 5 geprüft, 17.10.2026
Nach frischen HA-Sicherungen bestehen auf beiden Hosts das Update von 0.1.313
auf 0.1.315 und die Export-/Rückimportprüfung: YAML/Card-Mod sowie JSON mit
UIX-Auswahl erreichen jeweils 112/112 Paketprüfungen und einen bytegleichen
Rückexport. Root- und Kartenstile, mehrzeiliges CSS, Shadow-DOM-Selektoren,
Jinja und `uix_style` bleiben korrekt zugeordnet. Auch die Stilobjekte im
erzeugten Script stimmen mit dem Paketinhalt überein.

Vorhandene Einstellungen, Dateien, drei bisherige Serverprojekte je Host,
sechs aktive Plugins, Papierkorb und Historie bleiben erhalten. Die lokalen
Editorstände sind exakt wiederhergestellt; die neuen Testprojekte liegen
separat vor. Direkter Hub und eingebettetes Runtime-Panel zeigen weiterhin
sechs aktive Plugins. HA bleibt 2026.10.1, die Integration 0.1.306.
Es wurden keine HA-Dashboards, Ressourcen oder Gerätetests angelegt.
Die Ausführung beliebiger CSS-Regeln durch Card-Mod/UIX bleibt eine separate
Prüfung mit den jeweils installierten Erweiterungen.
:::

::: info Importierte Card-Mod-/UIX-Stile ab 0.1.315, isoliert geprüft am 17.10.2026
Importierte `card_mod`-, `uix`- und `uix_style`-Objekte bleiben an ihrer
jeweiligen Karte: im Editor, in YAML/JSON, im HACS-Paket und im erzeugten Script.
Das gilt auch für verschachtelte Karten, mehrzeiliges CSS, Shadow-DOM-Selektoren
und Jinja-Werte. Karten mit derselben Entität erhalten keine fremden Stilblöcke.
YAML- und JSON-HACS-Rundläufe bestehen mit 112/112 Prüfungen und bytegleichem
Rückexport; auch der JSON-Einzelkartenimport ist im Browser geprüft.

Die Exportwahl **uix:** wandelt `card_mod` strukturell in `uix` um, auch für
JSON und Scripts. Vorhandene `uix`-/`uix_style`-Objekte bleiben erhalten.
Ist an derselben Karte bereits `uix` vorhanden, werden beide Blöcke behalten;
ATLAS überschreibt oder vereinigt sie nicht. **card-mod** erhält die importierten
Schlüssel, konvertiert UIX also nicht zurück. Das bestätigt den Datenerhalt,
nicht die Ausführung beliebiger CSS-Regeln durch jede Card-Mod-/UIX-Version.
Die benötigte Stil-Erweiterung muss in HA eingerichtet sein.

Bestandsdateien, Projekte und Plugins bleiben unverändert. Stile, die frühere
Versionen bereits verworfen haben, benötigen einen erneuten Import der
Originaldatei oder einer Sicherung. Die isolierte Prüfung ließ Pi 5 und Proxmox
unverändert; der anschließende native Folgetest ist oben separat dokumentiert.
:::

::: info YAML-/JSON-HACS-Rundlauf ab 0.1.314, isoliert geprüft am 17.10.2026
Wähle unter **Card-Format** YAML oder JSON, exportiere das HACS-Bundle und
importiere die vollständige `.hacs.zip` über **HA-Card importieren** zurück.
Beide Formate bestehen dieselben 112 Paketprüfungen. Formatwahl, Editor-Felder
und Mushroom-Text-, Symbol- und Farbvorlagen einschließlich mehrzeiliger Werte
bleiben erhalten; der erneute Export ist je Format bytegleich.

Der Container `atlas/*.atlas-card.json` und die Sprachdateien bleiben JSON;
`manifest.format` beschreibt den darin enthaltenen YAML- oder JSON-Card-Code.
Das erzeugte Script bleibt JavaScript. Vorhandene gültige YAML-Bundles brauchen
keine Konvertierung. Die Diagnosekennung heißt jetzt `package-format-supported`
statt `package-format-json`. Beschädigte Inhalte und fehlende Sprachdateien
werden weiterhin abgewiesen. Die damals fehlende Übernahme importierter
`card_mod`-Stile ist ab 0.1.315 korrigiert, siehe oben. Pi 5 und Proxmox wurden bei
dieser isolierten Prüfung nicht verändert; ihr Update auf 0.1.314 steht noch aus.
:::

::: info Mushroom-Importkorrektur in 0.1.313, isoliert geprüft am 17.10.2026
Normale YAML-/JSON-Importe erhalten bei Einzelkarten und verschachtelten
Mushroom-Template-Karten `primary`, `secondary`, `icon`, `color` und das ältere
`icon_color`. Einzelkarten bleiben Mushroom-Karten. Mehrzeilige YAML-Werte
behalten Einrückungen und Leerzeilen; fehlerhaftes YAML wird abgewiesen.

Speichern, Neuladen und HACS-Bundle-Export/Import erhalten die geprüften
Ausdrücke. In HA 2026.10.1 mit Mushroom 5.2.3 ändern die exportierten Karten
Texte, Symbole und Farben mit den Testzuständen und verbinden sich nach einem
Transportabbruch automatisch wieder. HA wertet Jinja aus; ATLAS erhält den Code.
„Titel übernehmen“ ersetzt bewusst `primary`, eine Entitätsänderung erhält
die übrigen Vorlagen. Bereits durch ältere Importe verlorene Angaben lassen
sich nur aus dem Original wiederherstellen. Original-YAML/JSON deshalb behalten.

Die Prüfung bestätigt die genannten Eigenschaften und Testfälle, keine
beliebigen Mushroom-Optionen oder Jinja-Programme. `icon_color` ist auf Erhalt
geprüft; der Laufzeittest verwendet das aktuelle `color`. Es gibt keine neuen
Jinja-Eingabefelder. Die isolierte Korrekturprüfung veränderte Pi 5 und Proxmox
nicht.
:::

::: info Update auf 0.1.313 auch auf Proxmox und Pi 5 geprüft, 17.10.2026
Nach frischen HA-Backups und PC-Abzügen bestehen auf beiden Hosts alle vier
Importwege: YAML/JSON, jeweils Einzelkarte und Stapel. Texte, Symbole und
Farbvorlagen einschließlich Leerzeilen bleiben exakt erhalten. Speichern,
Wiederöffnen und tatsächlicher HACS-Export/Import bestehen; die jeweiligen
Rückexporte sind bytegleich und die JSON-Paketprüfung besteht mit 112/112.

In echten, ungespeicherten HA-Kartenvorschauen wechseln Texte, Symbolformen
und berechnete Farben durch Jinja-Minutenwechsel ohne Neuladen. Es werden nur
passive Sensorwerte gelesen, keine Geräte geschaltet. Die bisherigen 225/229
ATLAS-Dateien, jeweils zwei ursprüngliche Serverprojekte, sechs Plugins,
Einstellungen, Papierkorb und Historie bleiben erhalten. Beide vollständigen
lokalen Editor-Konfigurationen mit je 36 Feldern sind anschließend bis auf den
Exportzeitstempel exakt wiederhergestellt. Eigene Testprojekte bleiben separat.
Die HACS-Integration bleibt 0.1.306; diese Prüfung erfordert keinen HA-Neustart.
Beliebige Mushroom-Optionen oder Jinja-Programme sind damit nicht qualifiziert.
:::

::: info Isolierter 60-Minuten-Dauertest am 17.10.2026
ATLAS 0.1.312 mit HA 2026.10.1 hat einen vollständigen Stundenlauf mit 36
unterschiedlichen lokalen Testentitäten bestanden: je zwölf Core-, Bubble-
und Mushroom-Karten. 720 Aktualisierungsrunden mit 10.080 Serviceaufrufen und
25.920 angeforderten Zielaktualisierungen liefen ohne Servicefehler.
Nach Transportabbrüchen von 15, 45 und 90 Sekunden verbinden sich beide
Browseransichten automatisch wieder, ohne Neuladen während der Stunde.
Alle Felder und Karten bleiben erhalten; die 36 HA-Endzustände stimmen.
Speichern, Wiederöffnen und tatsächlicher Browserexport/-import sind geprüft;
die beiden Exporte sind bytegleich. Ursprüngliche Testdateien, Projekte,
Plugin-Einstellungen, Papierkorb und Historie bleiben erhalten.
Die vollständige ATLAS-Prozessgruppe lag in den ab Minute sechs erfassten
Stichproben bei 168,1–168,6 MiB, der HA-Container während der Stunde bei
652–681 MiB. Chrome wurde nur insgesamt einschließlich anderer Tabs gemessen;
daraus folgt keine Aussage zum Speicherverbrauch einzelner Karten.
Die Stunde nutzt ein generiertes Testpaket; der tatsächliche Browserexport wird
anschließend gesondert verglichen. Dynamische eigene Mushroom-Jinja-Texte,
ARM64-Leistung und Produktionskapazität sind damit nicht geprüft.
Pi 5 und Proxmox wurden weder abgefragt noch verändert.
:::

::: info 36-Karten-Durchlauf auf Proxmox und Pi 5 am 16.10.2026
Nach frischen HA-Sicherungen wurden mit ATLAS 0.1.312 und HA 2026.10.1 auf
beiden Hosts je zwölf Core-, Bubble- und Mushroom-Karten geprüft. Speichern,
Neuladen und Wiederöffnen sowie Import des tatsächlichen Browserexports erhalten
alle 36 Felder und die Kartenkonfiguration. Die beiden Exporte pro Host sind
bei gleicher EN/DE/FR-Auswahl bytegleich. Bestehende lokale Editor-Konfigurationen
wurden anschließend vollständig wiederhergestellt und verglichen.
Nach einem echten Proxmox-VM-Neustart und einer vom Benutzer ausgeführten
Pi-LAN-Unterbrechung verbinden sich die geöffneten Editoren ohne Neuladen wieder;
die HA-Ansichten zeigen weiterhin alle 36 Karten ohne Fehlkarte.
Diese Hostprüfung verwendet passive vorhandene Sensoren und umfasst keine
360 künstlichen Zustandswechsel. Die Karten rendert Chrome auf dem PC;
das ist kein ARM64-Browser- oder CPU/RAM-Benchmark. Bestehende ATLAS-Dateien,
Projekte, Plugins, Papierkorb und Historie bleiben erhalten. Beim VM-Neustart
wurde separat ein geänderter HACS-Abfrageparameter der vorhandenen
selfhst-Ressource beobachtet und beibehalten.
:::

::: info Größeres Projekt isoliert geprüft am 16.10.2026
Mit ATLAS 0.1.312 und HA 2026.10.1 wurden 36 Expert-Felder geprüft: je zwölf
Core-, Bubble- und Mushroom-Karten mit zwei lokalen Testentitäten. Speichern,
Neuladen und Öffnen des Serverprojekts sowie HACS-Bundle-Export/Import erhalten
alle Felder und die Kartenkonfiguration; wiederholte Exporte mit gleicher
Sprachauswahl sind bytegleich. HA rendert alle 36 Karten ohne Fehlkarte.
Während 360 Zustandswechseln in gut drei Minuten verbinden sich Editor und,
beim längsten Ausfall, auch die HA-Ansicht nach Transportabbrüchen von rund
12, 24 und 62 Sekunden automatisch wieder. Vorhandene Testdaten bleiben erhalten.
Pi 5 und Proxmox wurden nicht abgefragt oder verändert. Das ist ein begrenzter
Funktionstest, kein Hardware-Benchmark oder Nachweis für beliebige Projektgrößen.
Der tatsächliche Browserexport wurde vollständig an einem neuen Ressourcenpfad
geprüft; beim manuellen Austausch unter derselben URL kann ein altes Script im
Browsercache mit neuen Sprachdateien kollidieren und den Reparaturhinweis auslösen.
:::

Der Card Editor ist ein aktiver Entwicklungsstand. Expert-Workflow,
Import/Export, Entity-Auswahl, Ressourcenprüfung, Container-Cards und lokale
Custom-Card-Mappings für gescannte Lovelace-Ressourcen sind bereits testbar.
Weitere geprüfte Custom-Card-Mappings werden schrittweise ergänzt.
