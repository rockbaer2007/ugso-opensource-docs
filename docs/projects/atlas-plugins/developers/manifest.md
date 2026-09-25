---
title: Manifest und Fähigkeiten
description: IDs, Versionen, Metadaten und Fähigkeiten eines ATLAS-Plugins.
---
# Manifest und Fähigkeiten

Das Plugin-Manifest beschreibt Identität, Anzeigeinformationen und Einstiegspunkt eines Plugins. In der [offiziellen Vorlage](../plugin-template) liegt das Beispiel unter `plugins/atlas-plugin/atlas-plugin.json`.

## Beispiel

```json
{
  "id": "atlas.plugin.lights",
  "name": "Light Controls",
  "nameI18n": {
    "de": "Lichtsteuerung",
    "en": "Light Controls"
  },
  "version": "1.0.0",
  "description": "Controls selected lights.",
  "status": "active",
  "order": 100,
  "entry": "/plugin-assets/atlas-plugin/index.html",
  "icon": "icon.svg",
  "logo": "logo.svg",
  "preview": "preview.svg",
  "capabilities": ["homeassistant.entities.read"]
}
```

## Felder

- `id`: global eindeutige Plugin-Kennung. Nach der Veröffentlichung stabil halten; die Vorlage verwendet kleingeschriebene, punktgetrennte IDs.
- `name` und `nameI18n`: Standardname und optionale lokalisierte Namen.
- `version`: veröffentlichte Plugin-Version. Für jede veröffentlichte Änderung erhöhen.
- `description` und `descriptionI18n`: kurze Standard- und lokalisierte Beschreibung.
- `status` und `order`: Status- und Sortierhinweise für Katalog und Oberfläche.
- `entry`: relative URL des Plugin-Einstiegs. Lokale Plugins mit `index.html` können in Atlas automatisch eine Start-URL erhalten, wenn kein `entry` angegeben ist.
- `icon`, `logo`, `preview`: relative Asset-Pfade, die in Katalog und Administration verwendet werden.
- `capabilities`: dokumentiert, welche Funktionen das Plugin benötigt. Nur tatsächlich verwendete Einträge deklarieren.

Das Manifest im Pluginpaket ist von `repository.json` zu unterscheiden: Der Katalog enthält zusätzlich pro Plugin Felder wie Paket-URL, Manifest-Fallback, Kompatibilität und Katalog-Beschreibungen. Siehe [Repository-Format](../repository-format).

## Fähigkeiten sparsam angeben

Fähigkeiten müssen konkret begründet sein. Füge keine Platzhalter- oder pauschalen Admin-Berechtigungen hinzu. Die aktuelle Installation führt heruntergeladenen Plugin-Code noch nicht aus; eine Fähigkeitsangabe stellt daher keine technische Zugriffssperre oder Sandbox dar.
