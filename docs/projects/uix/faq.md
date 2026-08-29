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
| [Host/Element-Pfad-Auswahl](./concepts/dom#hostelement-pfad-auswahl) | Nein | Ja |
| [Express Search Selector](./concepts/dom#express-search-selector) | Nein | Ja |
| [Forge](./forge/) als Custom-Lovelace-Element | Nein | Ja |
| [Foundries](./forge/foundries) als wiederverwendbare Forges | Nein | Ja |
| [Makros](./using/templates#makros) für wiederverwendbare Jinja-Templates | Nein | Ja |
| [Sparks](./forge/sparks/) als gekapselte Erweiterungen für Forge-Elemente | Nein | Ja |
| [Frontend State Throttling](./extras/frontend-states-throttling) optional | Nein | Ja |
| [Dialog Styling Delay](./extras/dialog-styling-delay) optional | Nein | Ja |
| [Dashboard View Backgrounds](./using/view-backgrounds) | Nein | Ja |
| [Section Backgrounds](./using/section-backgrounds) | Nein | Ja |
| [Icon Styling mit Entity Override](./using/icons#override-fur-eine-entitat) | Nein | Ja |
| [Entitätsbilder stylen](./using/images) | Nein | Ja |
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

UIX erkennt typische Situationen, in denen Frontend-Cache oder Companion-App-Cache alte Ressourcen verwenden. In solchen Fällen kann UIX eine Reload-/Clear-Cache-Meldung anzeigen.

::: info
Wenn eine Änderung nach einem Update nicht sichtbar wird, hilft ein harter Browser-Reload oder das Leeren des Companion-App-Caches trotzdem als erster Test.
:::

## Wie deinstalliere ich UI eXtension?

Entferne UIX über HACS oder aus `custom_components/uix`, starte Home Assistant neu und entferne anschließend UIX-spezifische Theme-Variablen oder `uix:`-Blöcke aus Dashboards, wenn sie nicht mehr benötigt werden.
