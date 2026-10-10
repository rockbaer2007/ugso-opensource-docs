---
title: Themes und Zoom
description: Gespeicherte Theme-Auswahl und zusätzlicher Einpassen-Knopf im Blockly-Editor.
---
# Themes und Zoom

Seit **0.1.27** erhalten UGSo-Blocks in Standard/Dark weiße Beschriftungen. Mittlere blaue und braune Flächen werden dafür etwas dunkler, mit mindestens **4,5:1** Kontrast. Bei originalen hellen Modern-/Tritanopia-Farben wird passend kontrastreiche dunkle Schrift verwendet. Eingabefelder bleiben separat lesbar. Die Blockbilder im Katalog sind für DE/EN/FR mit dieser Korrektur neu erzeugt.

Seit **0.1.16** enthält die Werkzeugleiste über der Arbeitsfläche eine **Theme-Auswahl**. Sie betrifft den Blockly-Bereich einschließlich Kategorien, Blockauswahl und Blocks. Die Blockly-Palette ist unabhängig von der App-Darstellung. Es bleiben 111 Blocktypen.

| Auswahl | Darstellung | Originalquelle |
| --- | --- | --- |
| UGSo Standard | Bisherige UGSo-Gruppenfarben, dunkles Menü und helle Blockauswahl | Eigene UGSo-Anpassung auf Blockly Classic |
| Dark | Dunkle Arbeitsfläche, dunkle Blockauswahl und davon abgesetztes Kategorienmenü | [theme-dark](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-dark) |
| Modern | Originale Modern-Palette mit kräftigeren Rändern und UGSo-Erweiterungsgruppen | [theme-modern](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-modern) |
| Tritanopia | Originalpalette für die Standardgruppen und zusätzliche Farben für HA-spezifische Gruppen | [theme-tritanopia](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/theme-tritanopia) |

Tritanopia ist für Menschen mit entsprechender Farbsehschwäche gedacht. Auch eigene UGSo-Blocks und Kategorien verwenden jetzt Theme-Stile statt fest gesetzter Farben. Helle Blocks erhalten dunkle Beschriftungen, dunkle Blocks helle; Eingabefelder bleiben separat lesbar. Die ausgewählte Kategorie hat unabhängig von der Palette einen dunklen Hintergrund mit heller Schrift. Kategorienamen und Blocktexte bleiben zur Orientierung sichtbar. Dies ist keine vollständige Barrierefreiheitszertifizierung.

![Dark im UGSo-Editor](/assets/blocks-for-ha/themes/de/dark.png)

![Tritanopia im UGSo-Editor](/assets/blocks-for-ha/themes/de/tritanopia.png)

## Wechseln und speichern

Das Theme wird direkt umgeschaltet, ohne die Arbeitsfläche neu aufzubauen. Blocks, Verbindungen, Anordnung und YAML bleiben erhalten. Die Auswahl wird getrennt vom Projekt in diesem Browser gespeichert und nach dem Neuladen wieder verwendet. Projektdateien und YAML übertragen diese Anzeigeeinstellung nicht auf andere Browser. Unbekannte Einstellungen fallen auf UGSo Standard zurück; bei gesperrtem Browser-Speicher funktioniert der Wechsel für die aktuelle Sitzung.

Der vorhandene **Geras-Renderer** bleibt für alle Themes aktiv, damit Anschlussgeometrie und Bedienung erhalten bleiben. Das originale Modern-Theme empfiehlt Zelos/Thrasos; hier wird seine Farb-/Randpalette mit Geras verwendet und geprüft. Ein Renderer-Wechsel ist keine zusätzliche Option dieser Version.

## Alle Blocks einpassen

Das originale [zoom-to-fit](https://github.com/raspberrypifoundation/blockly-samples/tree/main/plugins/zoom-to-fit) ergänzt das Vier-Pfeile-Symbol neben den Zoom-Reglern. Ein Klick passt die Blocks an die verfügbare Arbeitsfläche an. Der Knopf ist auch mit Tab erreichbar und per Enter/Leertaste bedienbar. Zoom verändert die Ansicht, nicht die Automation.

Der obere Button **Einpassen** bleibt bestehen und begrenzt die Vergrößerung auf die kompakte Standardgröße. Das Plugin verwendet das normale Blockly-Einpassen innerhalb der vorhandenen Zoomgrenzen. Auf kleinen Bildschirmen kann die Theme-Werkzeugleiste umbrechen; die Arbeitsfläche lässt sich weiter verschieben.

Alle vier zusätzlichen Originalplugins sind auf **13.3.0** festgelegt, mit Blockly **13.3.0** eingebunden und unter Apache-2.0 lizenziert. Die sechs bisherigen Originalplugins bleiben auf 13.2.0. Die Pakete werden lokal ausgeliefert; keine externen Theme-Dateien oder CDN-Abhängigkeit. Originalquellen und Lizenzhinweise stehen auch im [Blockkatalog](./blocks).

Geprüft: vier Themes, Schrift auf hellen Tritanopia-Blocks, unveränderte Projekt-/YAML-Ausgabe, gespeicherte Auswahl, unbekannte/gesperrte Speichereinstellungen, Einpassen und mobile Breite. Die HA-Ausführung wird durch diese Anzeigeänderung nicht verändert.

## App-Darstellung: Hell, Dunkel oder System

Seit **0.1.22** bietet **Darstellung** im Kopfbereich **Hell**, **Dunkel** und **System** für die gesamte umgebende App-Oberfläche: Kopfbereich, Panels, Formulare, YAML-Ausgabe, Dialoge, Entitätsauswahl und eigenen Block-/Template-Editor. Standard ist System; Änderungen der Betriebssystem-/Browser-Farbpräferenz werden sofort übernommen. Eine manuelle Auswahl überschreibt die Systemvorgabe. Die Einstellung wird lokal in diesem Browser gespeichert; bei gesperrtem Browser-Speicher funktioniert die Umschaltung weiterhin für die aktuelle Seite.

Die Blockly-Themes bleiben separat in der Werkzeugleiste wählbar, einschließlich Modern und Tritanopia. Darstellung verändert weder Blocks noch erzeugtes YAML oder Projekte. Das originale Built-with-Blockly-Badge wechselt automatisch zur passenden hellen/dunklen Variante.
