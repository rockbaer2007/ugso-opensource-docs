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

## Roadmap

Die Home-Assistant-Integration zielt auf zwei Nutzungsarten:

- ATLAS als eigenständiger Server oder Editor
- ATLAS als Home-Assistant-Frontend-Integration, später auch HACS-nah

Die aktuellen Card Packages sind ein Zwischenschritt auf dem Weg zu einem
installierbaren und wieder importierbaren HA-Card-Editor.
