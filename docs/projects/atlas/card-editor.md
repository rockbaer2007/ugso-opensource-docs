---
title: Home Assistant Card Editor
description: Eigene Dokumentation zum ATLAS Home Assistant Card Editor mit Simple-Modus, Expert-Modus, Import, Export, Ressourcencheck und Home-Assistant-Anbindung.
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

## Modi

Der Editor trennt zwei Arbeitsweisen.

| Modus | Zweck |
|---|---|
| Simple | schnelle Card-Erzeugung aus ausgewählten Entitäten und Layouts |
| Expert | freie Editor-Fläche mit 12-Spalten-Raster, Drag-and-drop, Größenänderung und Container-Cards |

Im Simple-Modus stehen Entitätsauswahl, Card-Ziel, Layout und YAML-Vorschau im
Vordergrund. Im Expert-Modus werden Cards aus der linken Card-Liste auf eine
Home-Assistant-ähnliche Rasterfläche gelegt.

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
kein sicheres Card-Mapping kennt. Sie werden sichtbar gemacht, aber nicht
automatisch als vollständig konfigurierbare Card behandelt.

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

Der Editor weist darauf hin, dass Tabbed Card V2 eine eigene Card ist und sich
vom ursprünglichen `kinghat/tabbed-card` ableitet, aber als eigenständige
ATLAS-Variante geführt wird.

## Aktueller Status

Der Card Editor ist ein aktiver Entwicklungsstand. Simple- und Expert-Modus,
Import/Export, Entity-Auswahl, Ressourcenprüfung und Container-Cards sind
bereits testbar. Weitere Custom-Card-Mappings aus gescannten HACS-Ressourcen
werden schrittweise ergänzt.

