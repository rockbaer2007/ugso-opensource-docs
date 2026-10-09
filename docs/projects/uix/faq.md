---
title: FAQ
---
# FAQ

## Wie migriere ich am besten von Card-mod?

Für eine saubere Migration sollte UI eXtension als Service installiert werden. Danach können bestehende Card-mod-Konfigurationen schrittweise geprüft und in UIX-Strukturen überführt werden. Beginne mit einzelnen Karten oder Views, prüfe das Ergebnis im Browser und migriere dann Theme-Variablen und komplexere Shadow-DOM-Pfade.

::: tip UI eXtension als Service hinzufügen
Wenn UIX als Home-Assistant-Integration installiert ist, kümmert sich UIX selbst um die Frontend-Ressource. Dadurch entfallen typische Probleme mit manuell gepflegten Ressourcen-URLs.
:::

## Ist UI eXtension ein direkter Ersatz für Card-mod?

UIX unterstützt viele Card-mod-artige Styling-Situationen und kann in vielen Dashboards als Ersatz verwendet werden. Es ist aber nicht nur ein identischer Drop-in-Ersatz, weil UIX eigene Patches, Theme-Variablen, Forge, Foundries, Sparks und Debug-Hilfen mitbringt.

## Ist UI eXtension nur Card-mod mit anderer Dokumentation?

Nein. UIX nutzt eine eigene Architektur und eigene Frontend-Patches. Es adressiert neuere Home-Assistant-Strukturen, Dialoge, Theme-Variablen, DOM-Hilfen und erweiterte Funktionen, die über reines CSS-Injection-Styling hinausgehen.

## Gibt es eine Liste der Unterschiede zwischen Card-mod und UI eXtension?

| Funktion | Card-mod | UIX |
| --- | :---: | :---: |
| Korrektes Laden von `...-yaml` Theme-Variablen | Nein seit HA 2026.8.0 | Ja |
| Korrekte Behandlung von `...-more-info(-yaml)` | Nein seit HA 2026.3.0 | Ja |
| Adaptive Dialogs für `...-dialog(-yaml)` patchen | Nein seit HA 2026.3.0 | Ja |
| [DOM-Inspektionshelfer](./concepts/dom#dom-inspektionshelfer) | Nein | Ja |
| [Host/Element-Pfad-Auswahl](./concepts/dom#host-element-pfad-auswahl) | Nein | Ja |
| [Express Search Selector](./concepts/dom#express-search-selector) | Nein | Ja |
| [Forge](./forge/) als Custom-Lovelace-Element | Nein | Ja |
| [Foundries](./forge/foundries) als wiederverwendbare Forges | Nein | Ja |
| [Makros](./using/templates#makros) für wiederverwendbare Jinja-Templates | Nein | Ja |
| [Sparks](./forge/sparks/) als gekapselte Erweiterungen für Forge-Elemente | Nein | Ja |
| [Broker](./broker/) für deklarative Frontend-Interaktionen | Nein | Ja |
| [Frontend State Throttling](./extras/frontend-states-throttling) optional | Nein | Ja |
| [Dialog Styling Delay](./extras/dialog-styling-delay) optional | Nein | Ja |
| [Dashboard View Backgrounds](./using/view-backgrounds) | Nein | Ja |
| [Section Backgrounds](./using/section-backgrounds) | Nein | Ja |
| [Icon Styling mit Entity Override](./using/icons#override-fur-eine-entitat) | Nein | Ja |
| [Entitätsbilder stylen](./using/images) | Nein | Ja |
| [Custom Panels stylen](./using/custom-panels), auch in iFrames | Nein | Ja |
| [App- und Ingress-Panels stylen](./using/apps), auch in iFrames | Nein | Ja |
| Reload-/Clear-Cache-Popup | Nein | Ja |
| Umfangreiche Doku mit visuellen Beispielen | Begrenzt | Ja |
| Mod-Card | Ja | Ja |
| CSS-Styling in Themes | Ja | Ja |
| Reload-/Clear-Cache-Service oder Action | Ja | Ja |
| Variablen wie aktueller Benutzer | Ja | Ja |
| CSS-Styling | Ja | Ja |
| Ressourcen-URL | Ja | Nicht nötig |

## Hat UI eXtension Ressourcen-URL-Probleme?

UIX wird als Integration bereitgestellt und muss normalerweise nicht als manuelle Lovelace-Ressource gepflegt werden. Dadurch werden viele Fehler vermieden, die bei falscher Ressourcen-URL, Browsercache oder HACS-Pfad entstehen können.

## Muss nach einem Upgrade manuell der Cache geleert werden?

UIX zeigt eine Meldung mit der Schaltfläche `Reload Now`, wenn ein Neuladen zum Aktualisieren des Caches nötig ist. Nach 60 Sekunden wird die Seite automatisch neu geladen, damit auch unbeaufsichtigte Kiosks ihr Frontend aktualisieren.

::: info
Wenn eine Änderung nach einem Update nicht sichtbar wird, hilft ein harter Browser-Reload oder das Leeren des Companion-App-Caches trotzdem als erster Test.
:::

## Kann die Reload-Meldung unterdrückt werden?

Nein. Die Meldung stellt sicher, dass der UIX-JavaScript-Code im Frontend zur Version der UIX-Integration passt. Sie erscheint, wenn UIX geändert und Home Assistant neu gestartet wurde, der Browser aber noch ein zwischengespeichertes UIX-Bundle einer anderen Version verwendet.

Nach 60 Sekunden wird die Seite automatisch neu geladen.

::: info Vorschau: UIX 9.0.0-beta.0
Der aktuelle `dev`-Stand liefert bis zum nächsten Home-Assistant-Neustart weiterhin die beim Start geladene UIX-Version aus. Nach einem Update kannst du Home Assistant neu starten, sobald du die neue Version aktivieren möchtest. Die frühere Aufforderung an Administratoren, wegen eines vorzeitigen Frontend-Updates sofort neu zu starten, entfällt. Dieses Verhalten ist nicht Bestandteil der stabilen Basis 8.4.0.
:::

## Wie deinstalliere ich UI eXtension?

Entferne UIX über HACS oder aus `custom_components/uix`, starte Home Assistant neu und entferne anschließend UIX-spezifische Theme-Variablen oder `uix:`-Blöcke aus Dashboards, wenn sie nicht mehr benötigt werden.
