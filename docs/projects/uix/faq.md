---
title: FAQ
---
# FAQ

## Wie migriere ich am besten von Card-mod?

Deinstalliere zuerst Card-mod. Falls dessen Ressource über `extra_module_url` geladen wird, entferne auch diesen Eintrag und starte HA neu. Folge anschließend dem [UIX-Schnellstart](./quick-start), einschließlich des Hinzufügens der Integration als Dienst. Beide Ressourcen sollen nicht parallel geladen werden.

::: warning UI Lovelace Minimalist kann Card-mod nachladen
Deaktiviere dort die Option `Include custom card resources it's depending on` und lade benötigte Custom Cards über Marketplace oder manuell. Durch die Ladereihenfolge kann UIX diesen Konflikt nicht selbst erkennen.
:::

::: tip UI eXtension ist ein Dienst
Marketplace fügt UI eXtension bei der Installation automatisch als Dienst hinzu. Prüfe bei Problemen unter **Einstellungen → Geräte & Dienste**, ob der Dienst vorhanden ist. Bei manueller Installation fügst du ihn selbst hinzu.
:::

## Ist UI eXtension ein direkter Ersatz für Card-mod?

Ja. Laut englischem Original ist UIX ein direkter Ersatz für Card-mod bis **4.2.1** und unterstützt dessen Karten- und Theme-Konfigurationen. Die Umstellung auf `uix:` und `uix-<thing>(-yaml)` ist empfohlen, aber nicht erforderlich. Bei gleichzeitig vorhandenen Konfigurationsschlüsseln hat `uix:` Vorrang. Das bedeutet Kompatibilität der Konfiguration, nicht paralleles Laden beider Ressourcen.

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

UIX registriert `uix.js` als zusätzliches Frontend-Modul und für CAST auch als Dashboard-Ressource. Beim Laden der Integration werden die Ressourcen automatisch mit ihrer Version versehen.

## Muss nach einem Upgrade manuell der Cache geleert werden?

UIX zeigt eine Meldung mit der Schaltfläche `Reload Now`, wenn ein Neuladen zum Aktualisieren des Caches nötig ist. Nach 60 Sekunden wird die Seite automatisch neu geladen, damit auch unbeaufsichtigte Kiosks ihr Frontend aktualisieren.

::: info
Wenn eine Änderung nach einem Update nicht sichtbar wird, hilft ein harter Browser-Reload oder das Leeren des Companion-App-Caches trotzdem als erster Test.
:::

## Kann die Reload-Meldung unterdrückt werden?

Nein. Die Meldung stellt sicher, dass der UIX-JavaScript-Code im Frontend zur Version der UIX-Integration passt. Sie erscheint, wenn UIX geändert und Home Assistant neu gestartet wurde, der Browser aber noch ein zwischengespeichertes UIX-Bundle einer anderen Version verwendet.

Nach 60 Sekunden wird die Seite automatisch neu geladen.

::: info UIX 9.0.0
UIX liefert bis zum nächsten Home-Assistant-Neustart weiterhin die beim Start geladene Version aus. Nach einem Update kannst du Home Assistant neu starten, sobald du die neue Version aktivieren möchtest. Die frühere Aufforderung an Administratoren, wegen eines vorzeitigen Frontend-Updates sofort neu zu starten, entfällt.
:::

## Wie deinstalliere ich UI eXtension?

### Marketplace

Öffne [UIX im Marketplace](https://my.home-assistant.io/redirect/marketplace_repository/?owner=Lint-Free-Technology&repository=uix&category=integration) und wähle im Dreipunktmenü **Deinstallieren**. Marketplace entfernt den Dienst und die Integrationsdateien.

::: warning Dienstkonfiguration wird entfernt
Dabei werden auch die Dienstkonfiguration mit Foundries, eigenen Seitenleisten-Einträgen und weiteren Einstellungen gelöscht. Dashboard- und Theme-YAML bleibt gespeichert, funktioniert ohne UIX aber nicht mehr.
:::

### Manuell

Entferne zuerst den UI-eXtension-Dienst unter **Geräte & Dienste**. Lösche anschließend den Ordner `uix` aus `custom_components`.
