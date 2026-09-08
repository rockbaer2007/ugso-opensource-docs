---
title: Home Assistant Card Editor
description: Eigene Dokumentation zum ATLAS Home Assistant Card Editor mit Expert-Editor, Import, Export, Ressourcencheck und Home-Assistant-Anbindung.
---

# Home Assistant Card Editor

Der **ATLAS Home Assistant Card Editor** ist die erste sichtbare
Referenzanwendung im ATLAS-Umfeld. Er dient dazu, Home-Assistant-Cards visuell
zu entwerfen, vorhandene YAML-Cards zu importieren und exportierbare Card-Pakete
oder HACS-nahe Bundles vorzubereiten.

Die lokale Demo läuft standardmäßig auf:

```text
http://127.0.0.1:4174/
```

Die Verbindungseinstellungen werden über die Atlas Administration verwaltet:

```text
http://127.0.0.1:4175/
```

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

### Tabbed Card V2 Styling

Tabbed Card V2 übernimmt weiterhin die Material-Tab-Variablen und ergänzt
eigene Variablen für Tab-Hintergründe:

| Name | Standard | Beschreibung |
| --- | --- | --- |
| `--mdc-theme-primary` | `--primary-color` | Text, Indikator und Akzentfarbe des aktiven Tabs. |
| `--mdc-tab-text-label-color-default` | `--secondary-text-color` | Textfarbe inaktiver Tabs. Für Transparenz sollte ein `rgba(...)`-Wert mit Alpha-Kanal genutzt werden. |
| `--mdc-typography-button-font-size` | `14px` | Schriftgröße der Tab-Beschriftung. |
| `--tabbed-card-v2-tabbar-background` | `transparent` | Hintergrund der gesamten Tab-Leiste. |
| `--tabbed-card-v2-active-background` | `transparent` | Hintergrund des aktiven Tabs. |
| `--tabbed-card-v2-inactive-background` | `transparent` | Hintergrund inaktiver Tabs. |
| `--tabbed-card-v2-hover-background` | `--secondary-background-color` | Hintergrund beim Hover oder Fokus eines Tabs. |

Beispiel:

```yaml
type: custom:tabbed-card-v2
styles:
  --mdc-theme-primary: "#ff9800"
  --mdc-tab-text-label-color-default: "rgba(255,255,255,0.75)"
  --tabbed-card-v2-tabbar-background: "rgba(0,0,0,0.18)"
  --tabbed-card-v2-active-background: "rgba(255,152,0,0.22)"
  --tabbed-card-v2-inactive-background: "rgba(255,255,255,0.06)"
  --tabbed-card-v2-hover-background: "rgba(255,255,255,0.12)"
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
