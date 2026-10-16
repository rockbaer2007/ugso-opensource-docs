---
title: Home Assistant Card Editor
description: Eigene Dokumentation zum ATLAS Home Assistant Card Editor mit Expert-Editor, Import, Export, Ressourcencheck und Home-Assistant-Anbindung.
---

# Home Assistant Card Editor

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
Pi 5 und Proxmox wurden dafür nicht verändert. Dies ist kein
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

Der Card Editor ist ein aktiver Entwicklungsstand. Expert-Workflow,
Import/Export, Entity-Auswahl, Ressourcenprüfung, Container-Cards und lokale
Custom-Card-Mappings für gescannte Lovelace-Ressourcen sind bereits testbar.
Weitere geprüfte Custom-Card-Mappings werden schrittweise ergänzt.
