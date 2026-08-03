# ATLAS und Home Assistant

ATLAS besitzt mit `@atlas/homeassistant` ein eigenes Paket für die
Home-Assistant-nahe Integration. Der aktuelle Schwerpunkt liegt auf einem
Editor- und Export-Workflow für Home-Assistant-Karten, Live-Entitäten und
spätere HACS-Nutzung.

## Aktueller Umfang

- ATLAS Status Preview mit Theme- und Renderer-Anbindung
- lokale und live geladene Home-Assistant-Entitäten
- Verbindung über Home-Assistant-WebSocket
- Laden der Entitäten über `get_states`
- Laden der Lovelace-Ressourcen über `lovelace/resources`
- gemeinsamer Entity-Katalog für Typfilter und Suche
- Card-Ziele für Entities, Mushroom Template und Bubble Card
- Layouts `single`, `horizontal-stack` und `vertical-stack`
- JSON- und YAML-Export für Home-Assistant-Karten
- Atlas Card Packages für Editor-Roundtrips
- Import-Summary für importierte Karten

## Unterstützte Card-Ziele

| Auswahl | Home-Assistant-Typ | Abhängigkeit |
|---|---|---|
| Entities | `entities` | in Home Assistant enthalten |
| Mushroom Template | `custom:mushroom-template-card` | Mushroom |
| Bubble Button | `custom:bubble-card` | Bubble Card |

## Entity Picker und Suche

ATLAS besitzt jetzt einen wiederverwendbaren Entity-Katalog im Paket
`@atlas/homeassistant`. Dieser Katalog führt lokale Beispiel-Entitäten,
gespeicherte Gruppen und live geladene Home-Assistant-Entitäten zusammen.

Der Katalog liefert:

- eindeutige und sortierte Entity IDs
- Domain-Erkennung wie `sensor`, `binary_sensor`, `switch` oder `light`
- bevorzugte Shortcut-Reihenfolge für häufige Domains
- Labels aus Live-Entitäten, zum Beispiel Friendly Names
- Suche nach Entity ID oder Label, auch mit Teilbegriffen wie `Hyper`

Damit bleibt der Entity Picker nicht nur Demo-Code, sondern wird zu einer
gemeinsamen Grundlage für die spätere Home-Assistant-Frontend-Integration.

## HACS- und Ressourcenhinweise

ATLAS legt die erwarteten Ressourcenpfade direkt in den Export-Metadaten ab.
Die Demo kann dadurch anzeigen, ob eine Custom Card bereits in Home Assistant
registriert ist oder welcher Pfad noch fehlt.

| Card-Ziel | HACS-Hinweis | Erwarteter Ressourcenpfad |
|---|---|---|
| Entities | nicht erforderlich | in Home Assistant enthalten |
| Mushroom Template | HACS > Frontend > Mushroom | `/hacsfiles/lovelace-mushroom/mushroom.js` |
| Bubble Button | HACS > Frontend > Bubble Card | `/hacsfiles/Bubble-Card/bubble-card.js` |

Für Bubble Card ist der HACS-Ressourcenpfad absichtlich exakt so hinterlegt:

```text
/hacsfiles/Bubble-Card/bubble-card.js
```

Wichtig: Home Assistant läuft häufig auf Linux. Groß- und Kleinschreibung im
Pfad sind dort relevant.

ATLAS kann für Mushroom und Bubble Card außerdem einen kopierbaren
Lovelace-Ressourcen-Snippet erzeugen. Der kombinierte Snippet enthält die
ATLAS-Frontend-Resource und, wenn nötig, die gewählte Card-Abhängigkeit. Im
YAML-Format sieht das zum Beispiel für ATLAS Server plus Bubble Card so aus:

```yaml
- url: "/local/atlas/atlas-homeassistant-panel.js"
  type: "module"
- url: "/hacsfiles/Bubble-Card/bubble-card.js"
  type: "module"
```

Dieser Snippet ist für die Ressourcenregistrierung im Home-Assistant-Dashboard
gedacht. Bei der eingebauten Entities Card wird nur die ATLAS-Frontend-Resource
kopiert.

## Export-Modell

ATLAS trennt den HA-Card-Export in drei Ebenen:

1. **Card-Konfiguration**: das eigentliche Home-Assistant-Card-Objekt.
2. **Export-Manifest**: Dateiname, Format, MIME-Type, Ziel, Layout und
   Abhängigkeit.
3. **Export-Payload**: Manifest plus serialisierter JSON- oder YAML-Inhalt.

Dadurch nutzen Kopieren und Download denselben geprüften Inhalt.

## Atlas Card Packages

Zusätzlich zum direkten YAML/JSON-Export kann ATLAS ein portables JSON-Paket
erzeugen. Dieses Paket ist für spätere Editor- und HACS-nahe Workflows gedacht.
Wird ein Paket aus dem Expert-Modus exportiert, enthält es zusätzlich den
Editorplan. Beim späteren Import kann ATLAS dadurch die platzierten Felder
wiederherstellen und automatisch in den Expert-Modus wechseln.

```json
{
  "version": 1,
  "kind": "atlas.homeassistant.card",
  "manifest": {
    "name": "Office Light",
    "filename": "office-light-bubble-single.yaml",
    "format": "yaml",
    "mimeType": "text/yaml",
    "target": "bubble",
    "layout": "single"
  },
  "content": "type: \"custom:bubble-card\"\n..."
}
```

In der Demo enden diese Dateien auf:

```text
.atlas-card.json
```

Der gleiche Import kann rohe Home-Assistant-Karten als JSON/YAML und Atlas Card
Packages einlesen.

Vor dem eigentlichen Import kann ATLAS Artefakte prüfen und einordnen:

- ATLAS Card Package
- rohe Home-Assistant-Card als JSON oder YAML
- möglicher externer Card-Builder-Export
- unbekannter Inhalt

Externe Card-Builder-ähnliche Dateien werden dabei nicht automatisch importiert.
Sie benötigen zuerst ein bewusstes Kompatibilitäts-Mapping und eine
Lizenzprüfung.

Aus dieser Prüfung entsteht eine Import-Entscheidung für die Oberfläche:

- **Import**: unterstützte ATLAS- oder Home-Assistant-Artefakte.
- **Review**: externe Card-Builder-ähnliche Artefakte.
- **Reject**: unbekannte oder nicht sicher einordenbare Inhalte.

Für den Review-Fall liefert ATLAS bereits strukturierte Prüfpunkte: Lizenzgrenze,
erkannte visuelle Blöcke, erkannte Entity-Slots und den nächsten Schritt zur
Schema-Zuordnung. Eine Oberfläche kann daraus später einen Dialog bauen, bevor
ein externes Artefakt in ATLAS-Felder umgewandelt wird.

Zusätzlich kann ATLAS eine Mapping-Vorschau erzeugen. Häufige externe
Blocktypen werden dabei ATLAS-Templates zugeordnet: State-ähnliche Blöcke zu
State Buttons, Switch-ähnliche Blöcke zu Switch Buttons und horizontale oder
vertikale Layout-Blöcke zu passenden Stack-Templates. Nicht erkannte Blöcke
bleiben sichtbar und müssen manuell bewertet werden.

Aus einer Mapping-Vorschau kann ATLAS außerdem eine geprüfte Field-Preview für
die Expert-Fläche erzeugen. Die Felder werden im Raster platziert, enthalten
aber zunächst leere Entitäten und bleiben review-pflichtig. So kann die
Oberfläche eine Umwandlung zeigen, ohne sie still zu importieren.

Die Card-Editor-Demo nutzt diese Prüfung inzwischen direkt vor dem HA-Card-Import.
Unterstützte ATLAS-Packages und rohe Home-Assistant-Cards werden importiert,
externe Card-Builder-ähnliche Dateien zeigen eine Review-Ausgabe, und unbekannte
Artefakte werden vor dem Parsen abgelehnt.
Die ATLAS Status Preview bleibt als Renderer-, Theme- und Entitäts-Smoke-Test
erhalten, liegt aber jetzt im einklappbaren Diagnostics-Bereich und steht nicht
mehr im Hauptfluss des Card-Editors. Ob Diagnostics geöffnet ist, wird mit der
lokalen Demo-Konfiguration gespeichert.

Außerdem zeigt die Demo eine erste Expert-Editor-Vorschau. Sie verwendet die
gemeinsame, klickbare Template-Palette, erlaubt die Auswahl einer Card-Familie,
platziert Felder im begrenzten Raster und rendert daraus verschachtelten
Home-Assistant-Card-Code. Hinzugefügte Felder werden mit Entfernen-Aktion
aufgelistet, damit die Vorschau gezielt angepasst werden kann. Das ist noch
keine finale Drag-and-drop-Oberfläche, aber der erste sichtbare Schritt in diese
Richtung.

Der Importpfad akzeptiert jetzt auch verschachtelte Home-Assistant-Karten. Eine
reale `vertical-stack`-Karte kann also `horizontal-stack`-Zeilen,
`grid`-Container, `conditional`-Karten und einzelne Karten enthalten; ATLAS
behält die unterstützte Struktur und extrahiert die enthaltenen Entitäten.
Bubble-Header oder Separatoren ohne Entity werden ebenfalls akzeptiert.
Handgebaute Bubble-Switch-Spalten und `empty-column`-Karten werden ebenfalls
erkannt. Erweiterte Bubble-Card-Details wie `modules`, `styles`, `grid_options`,
Slider und Sub-Buttons sind als spätere Erhaltungsschicht geplant.

## Geplanter Card-Layout-Editor

ATLAS soll sich in Richtung eines visuellen Editors entwickeln, mit dem Nutzer
eine Home-Assistant-Card per Drag-and-drop aufbauen können. Dabei sollen
Cardname und JavaScript-Dateiname getrennt bleiben: Ein Nutzer kann also zum
Beispiel eine Card `Energy Kitchen` nennen und daraus später eine installierbare
Datei `energy-kitchen.js` erzeugen, statt auf einen festen Namen wie
`atlas-card.js` beschränkt zu sein.

Für den späteren HACS-Card-Paket-Export ist außerdem vorgesehen, Demo-Entitäten
wie `binary_sensor.atlas_status` und `sensor.atlas_temperature` als sichere
Vorgabe mitzugeben. Die Oberfläche soll dabei klar darauf hinweisen, dass diese
Beispiel-Entitäten durch eigene Home-Assistant-Entitäten ersetzt werden müssen.

Der Editor soll zwei Arbeitsweisen anbieten:

- **Simple**: schnelle Button-Stacks für normale Card-Exporte.
- **Expert**: freie Editor-Fläche, auf der Felder positioniert werden können.
  Pro Feld soll der Card-Typ wählbar sein, zum Beispiel Entities, Bubble Card
  oder Mushroom Template.

Aus dem Editor-Plan kann ATLAS künftig die tatsächlich genutzten Card-Ziele
ableiten. Bei einem gemischten Expert-Layout erkennt ATLAS dadurch gemeinsam,
ob zum Beispiel Mushroom und Bubble Card als HACS-Ressourcen benötigt werden,
während reine Entities-Felder keine zusätzliche Custom-Card-Resource brauchen.

Zusätzlich kann ein Editor-Plan jetzt in eine Home-Assistant-Card-Konfiguration
übersetzt werden. Simple nutzt die gewählte Ziel-Card direkt. Expert sortiert
belegte Felder nach Zeile und Spalte. Mehrere Felder in derselben Zeile werden
zu einem `horizontal-stack`; mehrere Zeilen werden mit einem `vertical-stack`
zusammengefasst. Ein einzelnes Feld kann außerdem selbst als `horizontal-stack`
oder `vertical-stack` markiert werden und mehrere Einträge enthalten. Wenn ein
Expert-Plan noch keine belegten Felder enthält, nutzt ATLAS die Demo-Entitäten
als sicheren Fallback.

In der Demo blendet Expert den einfachen Card-Layout-Wähler und den normalen
HA-Card-Code aus. Export, Package-Export, Kopieren und Ressourcen-Kopieren
verwenden dann den Expert-HA-Card-Code aus der Editor-Fläche.
Auch `Panel group`, `Group name`, `Card target`, `Card layout` sowie die
Gruppen-Aktionsbuttons werden im Expert-Modus ausgeblendet, weil die
Editor-Fläche dort die zu exportierende Card-Struktur direkt bestimmt.
Expert nutzt dafür ein eigenes Feld `Expert card name` für Kopieren, Export und
Paket-Dateinamen.

Für die Bedienung ist eine seitliche Template-Palette vorgesehen. Dort können
visuelle Bausteine wie Entity List, State Button, Switch Button,
`vertical-stack` und `horizontal-stack` angeboten werden. In der Demo ist daraus
bereits eine linke Palette mit Simple/Expert-Umschaltung geworden: Der Nutzer
kann einen Baustein anklicken oder per Drag-and-drop in die Editor-Fläche
ziehen. Hinzugefügte Felder erscheinen als verschiebbare Kacheln auf der
Rasterfläche. Die Fläche nutzt jetzt ein größeres, sichtbares 12-Spalten-Raster,
das näher an Home Assistant erinnert. Beim Verschieben vorhandener Felder nutzt
ATLAS das echte innere Raster und erhält den Punkt, an dem die Kachel gegriffen
wurde; dadurch lassen sich Felder nach oben ziehen, ohne seitlich zu springen.
Das sichtbare Raster liegt auf derselben inneren Fläche wie die Kacheln, mit
kleinerem Kachelabstand für dichteres Stapeln. Fokussierte Kacheln lassen sich
zusätzlich per Pfeiltasten um je eine Rasterzelle verschieben; im
Bearbeiten-Modus ändert `Shift` plus Pfeiltaste die Größe des ausgewählten
Feldes in 1er-Schritten. Jeder Baustein in der linken
Palette kann eigene Spalten von 1 bis 12 oder `full` sowie Zeilen `auto` oder
1 bis 8 vorgeben. Entity List, State Button, Switch Button, `horizontal-stack` und
`vertical-stack` starten mit derselben Standardfläche; Horizontal-Stacks können
bei mehreren ausgewählten Entitäten entsprechend breiter werden. Die Palette
kann geladene Lovelace-Ressourcen nutzen, um Custom-Card-Familien als
installiert, fehlend oder ungeprüft zu markieren. Beim Platzieren auf der
Expert-Fläche klemmt ATLAS Spalte, Zeile und Größe an die erlaubten
Rastergrenzen, damit Elemente nicht außerhalb der gültigen Fläche landen.
Platzierte Felder können ausgewählt und über einen Bearbeiten-Modus angepasst
werden. Erst im Bearbeiten-Modus erscheint der rechte untere Anfasser, mit dem
die Feldgröße innerhalb des 12-Spalten-Rasters verändert wird.
Die Titel platzierter Felder sind editierbar. Dieser Titel wird im Export als
Entities-Title, Bubble-Button-Name oder Mushroom-Primary-Text verwendet. Ein
Apply-Button übernimmt den manuell editierten Titel in das ausgewählte Feld.
Der bestehende Übernahme-Button kann zusätzlich den aktuell gewählten
Home-Assistant-Entitätsnamen direkt als Titel einsetzen.
Im Expert-Modus weist eine Entitätsauswahl aus Picker oder Entitätsliste die
Entität dem aktuell ausgewählten Editor-Feld zu und füllt den Titel mit dem
Entitätsnamen vor.
Für Bubble-Felder zeigt ATLAS zusätzlich einen Bubble-Button-Type-Dropdown.
Aktuell unterstützt sind `state`, `switch`, `slider` und `name`; der Wert wird
als `button_type` in den generierten Bubble-Card-Code geschrieben.
Die linke Expert-Palette trennt Core- und Community-Cards. Einzelne Cards
können per Häkchen als Favoriten markiert und über `Save favorites`
gespeichert werden. Sobald Favoriten gespeichert sind, blendet ATLAS alle
anderen Cards aus. `Show all cards` öffnet die vollständige Liste erneut,
ohne die gespeicherten Favoriten zu löschen. Dadurch können mehrere Favoriten
bequem nachträglich ausgewählt und danach gemeinsam gespeichert werden.
`Scan HA cards` liest die aktuell registrierten Lovelace-Ressourcen aus Home
Assistant und ergänzt erkannte Community-Cards wie Mushroom und Bubble Card in
der Palette. Home Assistant liefert darüber keine vollständige Options-Registry
für jede beliebige Custom-Card, aber installierte Ressourcen lassen sich so als
Ausgangspunkt erkennen. Andere registrierte Lovelace-Ressourcen werden als
Scan-only-Einträge sichtbar, bis ATLAS dafür ein sicheres Card-Mapping kennt.
Bereits gemappte Ressourcen werden dedupliziert, damit sie nicht noch einmal
als Scan-only-Kopie erscheinen.
Die Core-Liste enthält jetzt Entität, Entitäten, Button, Raster, Sensor,
Stapel, Querstapel, Thermostat, Verknüpfung und Webseite. Die Webseite wird im
Export als Home-Assistant-`iframe`-Card geschrieben.
Beim Verbinden mit Home Assistant fordert ATLAS diese Ressourcenliste
automatisch an. Gespeicherte Favoriten blenden alle nicht ausgewählten Cards
aus, inklusive gescannter `/hacsfiles/`-Einträge, bis `Show all cards` oder
`Reset favorites` genutzt wird. Scan-only-HACS- und HA-Ressourcen können
ebenfalls als Favoriten markiert werden, auch bevor ATLAS dafür ein ziehbares
Card-Mapping kennt. Hilfsressourcen wie Card-Tools, Dashboards, Strategien,
Navigationshelfer, Icon-Pakete und bekannte Nicht-Card-Ressourcen werden beim
Palette-Scan ausgeblendet.
Ein Reset-Button zeigt wieder die vollständige Liste. Die Palette selbst ist
scrollbar und nutzt kompakte zweispaltige Template-Zeilen: Card-Name und
Favoritenstatus stehen links, Layout-Details und Größensteuerung rechts.
Spalten- und Zeilenvorgaben der Templates werden mit der lokalen
Demo-Konfiguration gespeichert und können über `Reset sizes` wieder auf die
Standardwerte zurückgesetzt werden.
Ausgewählte Editorfelder können mit der Maus oder über Breite und Höhe in
1er-Schritten verändert werden, bis zu fünf Rasterzellen über die
Template-Standardgröße hinaus. Die Editorfläche selbst hat unten rechts einen
sichtbaren Anfasser und kann in beide Richtungen um bis zu fünf Rasterschritte
vergrößert werden; die aktuelle Größe bleibt der Standard. Ein Reset-Button
setzt die Editorfläche wieder auf die Standardgröße zurück.
Der gewählte Simple/Expert-Modus, platzierte Expert-Felder, das ausgewählte
Feld und die vergrößerte Editorfläche werden lokal im Browser gespeichert und
nach einem Neuladen wiederhergestellt.
Die Expert-Zusammenfassung nennt Felder, befüllte Felder, leere Platzhalter,
belegte Reihen, aktuelle Surface-Ausdehnung, Überschneidungen, Card-Ziele und
Layouttypen, bevor der generierte HA-Card-Code kopiert oder exportiert wird.
Überlappende Editorfelder werden direkt auf der Fläche markiert.
`Auto arrange` packt Felder in Zeilen- und Spaltenreihenfolge auf die ersten
freien Rasterplätze und reduziert Überschneidungen, ohne den Card-Inhalt zu
verändern.

## Externe Referenz: Home Assistant Card Builder

Das Projekt
[`studiobts/home-assistant-card-builder`](https://github.com/studiobts/home-assistant-card-builder)
ist eine wichtige externe Referenz für visuelle Home-Assistant-Card-Editoren.
Es bietet bereits einen Drag-and-drop-Builder, ein Blocksystem, ein eigenes
Home-Assistant-Panel und einen Renderer.

ATLAS übernimmt daraus aktuell keinen Quellcode. Das Projekt steht unter
AGPL-3.0, daher würde ein echter Fork oder eine abgeleitete Nutzung klare
Lizenz- und Attribution-Pflichten auslösen. Für ATLAS ist der geplante Weg:
eigenständige Verträge und UI-Modelle bauen, das Original klar nennen und
später optional Import-/Export-Kompatibilität oder einen bewusst
gekennzeichneten Fork prüfen.

Der Interop-Plan trennt drei Pfade:

- **Inspiration**: öffentliche Produktideen und dokumentiertes Verhalten fließen
  in eigenständige ATLAS-Verträge ein.
- **Import/Export-Kompatibilität**: später kann ATLAS dokumentierte Artefakte
  prüfen und eigene Mappings anbieten, ohne Quellcode zu kopieren.
- **Fork/Derivative**: nur als bewusste Entscheidung mit AGPL-3.0-Erfüllung,
  sichtbarer Attribution und vollständiger Lizenzprüfung.

## Import-Summary

Beim Import normalisiert ATLAS die Karte in eine Zusammenfassung:

- Titel
- Entitäten
- Format
- Ziel
- Layout
- Abhängigkeit
- Information, ob die Quelle ein Atlas Card Package war

Damit bleibt die eigentliche Editor-Logik im Paket `@atlas/homeassistant` und
nicht verstreut in der Oberfläche.

## Lovelace-Ressourcenprüfung

Wenn ATLAS mit Home Assistant verbunden ist, kann die Demo Lovelace-Ressourcen
abrufen und prüfen, ob Mushroom oder Bubble Card registriert sind.

Mögliche Zustände:

- `not-required`: Entities Card benötigt keine Custom-Card-Ressource
- `unchecked`: noch nicht geprüft
- `installed`: erwartete Ressource gefunden
- `missing`: erwartete Ressource fehlt

## ATLAS als Home-Assistant-Frontend

ATLAS unterscheidet jetzt auch die Resource, die ATLAS selbst in Home Assistant
verfügbar macht. Das ist getrennt von der gewählten Card-Abhängigkeit.

| Nutzungsart | Zweck | Erwarteter Ressourcenpfad |
|---|---|---|
| ATLAS Server | selbst gehosteter ATLAS-Editor oder Panel | `/local/atlas/atlas-homeassistant-panel.js` |
| ATLAS HACS | geplante HACS-Frontend-Integration | `/hacsfiles/atlas/atlas-homeassistant-panel.js` |

Die neue Integrationsplanung kann dadurch gemeinsam prüfen:

- ist die ATLAS-Frontend-Resource registriert?
- ist die gewählte Card-Resource installiert?
- fehlen bei Mushroom oder Bubble Card zusätzliche HACS-Pfade?
- ist der gesamte Export bereit für Home Assistant?
- welche JSON- oder YAML-Resources sollen in Home Assistant registriert werden?

Damit ist der nächste Schritt in Richtung “ATLAS direkt in Home Assistant
nutzen oder als HACS-nahe Integration installieren” vorbereitet.

## Aktuelle Demo

Im ATLAS-Repo lässt sich die Demo nach dem Build starten:

```sh
pnpm build
node examples/status-demo/server.mjs
```

Standardadresse:

```text
http://127.0.0.1:4173/
```

In der Codex-Arbeitsumgebung wurde zuletzt häufig Port `4174` genutzt:

```text
http://127.0.0.1:4174/
```

Auf breiten Bildschirmen nutzt die Demo kompakte Zwei- und Drei-Spalten-Raster
für Verbindung, Card-Konfiguration und Entity-Picker, damit zusammengehörige
Eingaben nebeneinander statt über die gesamte Seitenbreite laufen.

## Roadmap

Die Home-Assistant-Integration zielt auf zwei Nutzungsarten:

- ATLAS als eigenständiger Server oder Editor
- ATLAS als Home-Assistant-Frontend-Integration, später auch HACS-nah

Die aktuellen Card Packages sind ein Zwischenschritt auf dem Weg zu einem
installierbaren und wieder importierbaren HA-Card-Editor.
