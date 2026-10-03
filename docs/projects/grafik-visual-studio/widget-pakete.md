---
title: Widget-Paket-Schnittstelle
description: Lokale Widget-Pakete für HA Grafik Visual Studio erstellen und installieren.
---

# Widget-Paket-Schnittstelle

Ab Studio 0.1.187 ergänzt **Schnittstelle 0.2** die Text-Widgets aus 0.1 um deklarative Diagramme. Das nachinstallierbare Set [Wetter und Heizung](weather-heating.md) nutzt diese Erweiterung. Externe Sets erhalten automatisch eine noch nicht belegte Palettenfarbe mit Abstand zu vorhandenen Farbtönen. Die Zuordnung bleibt in diesem Browser nach Neuladen, Entfernen und Neuinstallation erhalten; Basis und integrierte Sets behalten ihre Farben.

## Schnittstelle 0.1: Text

Seit Studio-Version 0.1.89 kannst du ZIP-basierte Pakete mit der Endung `.wg` installieren. Bisherige `.wg.zip`-Dateien bleiben nutzbar; Endung und Manifest müssen zur Widget-Paketart passen.

Über **Einstellungen → Widget-Pakete** installierst du ein lokales `*.wg.zip`. Die Schnittstelle 0.1 nimmt geprüfte, deklarative Text-Widgets auf. Nach dem Neuladen erscheinen sie als eigenes Set in der Widget-Palette und funktionieren im Editor und in der Runtime. Die Installation führt keinen Paket-Code aus.

## Paket aufbauen

Das ZIP enthält eine UTF-8-Datei `manifest.json` im Wurzelverzeichnis und optional darin referenzierte SVG- oder PNG-Bilder unter `icons/`. Andere Dateien sind nicht zulässig. Eine Paket-ID ist punktgetrennt, zum Beispiel `beispiel.widgets`; Widget-Typen liegen in ihrem Namensraum, etwa `beispiel.widgets/label`. Die Paketversion hat das Format `x.y.z`. Ein Paket enthält 1 bis 30 Widgets; jedes erscheint als eigener Eintrag im Paket-Set der Palette.

```json
{
  "format": "ha-grafik-widget-package",
  "apiVersion": "0.1",
  "id": "beispiel.widgets",
  "name": "Beispiel Widgets",
  "version": "1.0.0",
  "license": "MIT",
  "widgets": [{
    "type": "beispiel.widgets/label",
    "label": "Label",
    "defaults": { "text": "Hallo" },
    "propertyGroups": [{
      "label": "Inhalt",
      "fields": [{ "key": "text", "label": "Text", "type": "text" }]
    }],
    "render": { "kind": "text", "valueKey": "text" }
  }]
}
```

`valueKey` bezeichnet ein bearbeitbares Text- oder Zahlenfeld. Für Eigenschaften sind `text`, `number`, `checkbox`, `color`, `range` und `select` vorgesehen. Jede Eigenschaft braucht einen passenden Standardwert in `defaults`. Die gemeinsamen Bereiche **Generell** und **Sichtbarkeit** ergänzt das Studio selbst. Ein Paket oder Widget kann zusätzlich `"icon": "icons/name.svg"` beziehungsweise `.png` angeben; die Bilddatei muss dann im ZIP liegen. Ohne eigenes Widget-Bild erscheint das integrierte SVG-Textsymbol.

Das ZIP darf höchstens 2 MB, das Manifest 200 KB und jedes Bild 50 KB groß sein. PNG-Bilder sind auf 1024 × 1024 Pixel begrenzt; SVG-Dateien werden auf passive Formen und Attribute geprüft. Paket- und Widget-Bilder dürfen SVG oder PNG sein, während die Aktionsbuttons des Studios ihre SVG-Symbole behalten.

## Schnittstelle 0.2: Diagramm

Das Manifest verwendet `apiVersion: "0.2"` und `render: {"kind":"chart","valueKey":"headline"}`. `headline` ist ein deklariertes Textfeld mit Standardwert. Die Instanz speichert Definitionsversion 0.2. Manifest und Icons bleiben die einzigen zulässigen Paketdateien; das Studio zeichnet mit seinem eigenen SVG-Renderer.

Die festen Diagrammschlüssel und Grenzen stehen im [Diagrammvertrag](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/widget-rules.md#widget-paket-schnittstelle-02). Unterstützt werden bis zu zehn JSON-Reihen, Linien/Balken, linke/rechte Achse, Zeit-/Kategorieachse und lesende HA-Zustands-/Attributbindungen. Ausführbare Formatierer und Schreibaktionen sind nicht enthalten. Bestehende Text-Pakete aus 0.1 bleiben nutzbar.

## Installieren und verwalten

1. Erstelle das ZIP mit dem Dateinamen `mein-paket.wg` und den genannten Dateien. Auch `mein-paket.wg.zip` wird weiter angenommen.
2. Öffne **Einstellungen → Widget-Pakete** und wähle die lokale ZIP-Datei.
3. Prüfe den Eintrag mit Paket-ID, Version, API-Version, Widget-Anzahl und Lizenz. Lade die App über **Neuladen** erneut, damit das Set in der Palette erscheint.

Ein bereits installiertes Paket wird nicht überschrieben. **Entfernen** ist gesperrt, solange ein Widget-Typ des Pakets in einem Projekt verwendet wird. GitHub-Installation und Paket-Updates sind noch nicht verfügbar. Eigene Skripte, Home-Assistant-Zustandsbindungen und Schreibaktionen gehören ebenfalls nicht zu Schnittstelle 0.1.

Bestehende Widget-Grundfunktionen sollen bei späteren Erweiterungen erhalten bleiben. Die vollständigen Regeln und weitere geplante Fähigkeiten stehen in den [Widget-Regeln im Quellcode](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/widget-rules.md).
