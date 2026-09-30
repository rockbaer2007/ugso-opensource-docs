---
title: ATLAS Icon Bibliothek
description: Home-Assistant-Iconsets suchen, durchsuchen und Icon-Namen kopieren.
---
# ATLAS Icon Bibliothek

Die ATLAS Icon Bibliothek ist ein eigenständiges Plugin zum Suchen und Durchsuchen von Iconsets. Die Icons erscheinen in einem Raster mit bis zu 20 Spalten; bei großen Sets lädt die Oberfläche nur den sichtbaren Ausschnitt. Ein Klick kopiert den vollständigen Namen wie `mdi:home` oder `atlas:home`.

## Iconsets laden

Der Plugin-Paket enthält den MDI-Katalog. Icon-Studio-Sammlungen können als JavaScript-Datei vom PC importiert oder über File Studio aus `/config/www/` geladen werden. Der Scanner kann dort unterstützte, von Icon Studio erzeugte Dateien finden und Dateien mit gleichem Präfix zusammenfassen. Importierte Sammlungen werden lokal im Browser gespeichert.

Einige ältere Home-Assistant-Iconsets stellen über `window.customIcons` eine Icon-Namensliste bereit und können damit angezeigt werden. Die neuere `window.customIconsets`-Schnittstelle bietet keinen allgemeinen Mechanismus, um alle Icon-Namen eines beliebigen Sets aufzulisten. Solche Sets lassen sich nur anzeigen, wenn sie zusätzlich eine lesbare Namensliste bereitstellen.

Für den Zugriff auf `/config/www/` muss dieser Pfad in File Studio freigegeben sein. Das Plugin benötigt dafür keinen Home-Assistant-Token.

## Installation und Quellcode

Im ATLAS Plugin-Manager das externe Repository hinzufügen:

```text
https://raw.githubusercontent.com/rockbaer2007/atlas-icon-library-plugin/main/repository.json
```

Der Quellcode und die Entwicklungshinweise stehen im [GitHub-Repository](https://github.com/rockbaer2007/atlas-icon-library-plugin).
