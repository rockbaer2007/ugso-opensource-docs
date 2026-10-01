---
title: Tool-Paket-Schnittstelle
description: Lokale Editor-Tools für HA Grafik Visual Studio erstellen und installieren.
---

# Tool-Paket-Schnittstelle 0.1

Seit Studio-Version 0.1.89 kannst du ZIP-basierte Pakete mit der Endung `.tp` installieren. Bisherige `.tp.zip`-Dateien bleiben nutzbar; Endung und Manifest müssen zur Tool-Paketart passen.

Über **Einstellungen → Tools** installierst du ein lokales `*.tp.zip`. Installierte Tools erscheinen zusätzlich als Symbole in zwei Reihen der Editor-Werkzeugleiste; das Koffersymbol dort öffnet direkt den Tools-Tab zur Verwaltung. Tool-Pakete ergänzen den Editor, nicht die Widget-Palette oder Runtime. Schnittstelle 0.1 unterstützt eine deklarative Aktion: die Hintergrundfarbe der aktuellen Seite setzen. Ein Klick auf das Tool-Symbol oder **Ausführen** im Tools-Tab zeigt zunächst eine Vorschau; erst **Anwenden** übernimmt die Änderung. Sie lässt sich mit **Rückgängig** zurücknehmen und wird über den normalen Projektweg gespeichert. Bei der Installation wird keine Aktion ausgeführt.

## Paket aufbauen

Das ZIP enthält `manifest.json` in UTF-8 und optional referenzierte SVG- oder PNG-Bilder unter `icons/`. Andere Dateien sind nicht zulässig. Eine Paket-ID ist punktgetrennt; die Tool-ID liegt im Paket-Namensraum. Die Paketversion hat das Format `x.y.z`. Ein Tool-Paket enthält genau ein Tool.

```json
{
  "format": "ha-grafik-tool-package",
  "apiVersion": "0.1",
  "id": "beispiel.tools",
  "name": "Beispiel Tools",
  "version": "1.0.0",
  "license": "MIT",
  "tools": [{
    "id": "beispiel.tools/background",
    "definitionVersion": "0.1",
    "label": "Seitenfarbe",
    "description": "Setzt die Farbe der aktuellen Seite.",
    "context": "page",
    "capabilities": ["project.read", "project.write"],
    "action": { "kind": "set-page-background", "defaultColor": "#224466" }
  }]
}
```

`defaultColor` ist eine sechsstellige Hex-Farbe und lässt sich in der Vorschau ändern. Die genannten Fähigkeiten gelten nur für diese bestätigte Editor-Aktion. Sie geben Paket-Code keine allgemeine Schreibberechtigung. Paket oder Tool können optional ein Bild über `"icon": "icons/name.svg"` oder `.png` referenzieren. Die Datei muss im ZIP liegen; die Studio-Aktionsbuttons verwenden weiterhin SVG-Symbole.

Das ZIP darf höchstens 2 MB, das Manifest 200 KB und jedes Bild 50 KB groß sein. PNG-Bilder sind auf 1024 × 1024 Pixel begrenzt; SVG-Dateien werden auf passive Inhalte geprüft.

## Installieren und verwalten

1. Erstelle beispielsweise `seitenfarbe.tp` mit `manifest.json` und gegebenenfalls den referenzierten Bildern. Auch `seitenfarbe.tp.zip` wird weiter angenommen.
2. Wähle die Datei unter **Einstellungen → Tools**. Die Liste zeigt Paket-ID, Version, Lizenz und das enthaltene Tool.
3. Öffne für das Tool über sein Symbol in der Editor-Werkzeugleiste oder mit **Ausführen** im Tools-Tab die Vorschau und bestätige die gewünschte Seitenänderung mit **Anwenden**.

Pakete können im Tool-Tab entfernt werden. Eigene Skripte, Home-Assistant-Dienste, externe URLs, GitHub-Installation und Updates sind noch nicht Teil von 0.1. Die geplanten Kompatibilitäts- und Erweiterungsregeln stehen in den [Tool-Regeln im Quellcode](https://github.com/rockbaer2007/ugso-ha-mqtt-addons/blob/master/ha_grafik_visual_studio/docs/tool-rules.md).
