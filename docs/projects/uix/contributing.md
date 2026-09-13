---
description: Beiträge zur UIX-Dokumentation und zum Projekt
---
# Mitwirken

Die folgenden Hinweise beziehen sich auf Beiträge zum originalen UIX-Repository. Diese deutsche Dokumentation wird separat als inoffizielle Übersetzung gepflegt.

UIX-Dokumentation ist ein Bereich, in dem jede Nutzerin und jeder Nutzer helfen kann. Wenn Python in deiner Umgebung installiert ist, kannst du die Dokumentationsquellen bearbeiten und das Ergebnis lokal in Echtzeit ansehen.

## Dokumentation aktualisieren

Die UIX-Dokumentation wird aus Markdown-Dateien mit Zensical gebaut. So startest du die Dokumentationsseite lokal:

1. Repository klonen.
2. Optional eine Python-Umgebung anlegen und `zensical` installieren, falls es nicht global installiert ist.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install zensical
```

3. In den Dokumentationsordner wechseln und Zensical starten.

```bash
cd docs
zensical serve
```

Danach ist die lokale Dokumentationsseite unter `http://localhost:8000` erreichbar.

Du kannst Zensical auch auf einer anderen Adresse oder einem anderen Port starten:

```bash
zensical serve localhost:9000
```

## Pull Requests einreichen

Bitte beachte für Pull Requests:

- Füge `uix.js` nicht zu Commits hinzu. Diese Ressourcendatei wird beim Release gebaut. UIX kann hier nicht einfach Release-Assets nutzen, weil `uix.js` im Ordner `custom_components/uix` liegen muss.
- Füge Tests für neue visuelle Komponenten hinzu. Hinweise stehen in der `README.MD` im Testordner des Repositories.
- Verwende nach Möglichkeit Conventional-Commit-Namen. Das ist nicht zwingend, weil Pull Requests beim Mergen zusammengefasst und der Titel angepasst werden kann, hilft aber bei der Einordnung.
- Wenn es sich um eine Breaking Change handelt, erwähne im Commit-Footer oder Pull Request `BREAKING CHANGE: ...`.
- Verweise im Commit-Footer oder Pull Request auf behobene Issues, zum Beispiel `fixes #1234`.

## Externe Dokumentationsübersetzungen

Direkte Sprachübersetzungen werden nicht als normale Kopie in das Hauptrepository aufgenommen. Der bevorzugte Weg ist eine extern gepflegte Übersetzung, die in der Originaldokumentation registriert wird.

Wichtig für eine externe Übersetzung:

- Sie muss klar als Übersetzung gekennzeichnet sein.
- Sie sollte zur passenden UIX-Version passen.
- Bilder und Animationen sollten nach Möglichkeit aus der Originaldokumentation referenziert oder nach dem offiziellen Workflow erzeugt werden.
- Bei neuen UIX-Releases muss die Übersetzung nachgezogen werden, damit Nutzer keine veralteten Informationen für aktuell halten.

Der Registrierungsweg für externe Übersetzungen ist in der offiziellen Dokumentation beschrieben: [External documentation translations](https://uix.lf.technology/contributing/#external-documentation-translations).

### Übersetzungs-Fork und Veröffentlichung

Im Übersetzungs-Fork bleiben die englischen Quellen unter `docs/source` unverändert. Die deutsche Übersetzung liegt unter `docs/source-de`. Der gemeinsame Dokumentationsworkflow wählt anhand von `docs/site.json` automatisch das passende Verzeichnis; `docs_dir` in `docs/mkdocs.yml` wird nicht geändert.

Beispiel für `docs/site.json`:

```json
{
  "schema": 1,
  "language": "de",
  "name": "Deutsch",
  "site_url": "https://example.github.io/uix-de/",
  "canonical_url": "https://uix.lf.technology",
  "translation_notice": "Diese unabhängige Übersetzung kann Ungenauigkeiten enthalten. Bitte beachten Sie {canonical}.",
  "translation_notice_link": "die kanonische englische Dokumentation"
}
```

`translation_notice` muss genau einen Platzhalter `{canonical}` enthalten. Der Workflow ersetzt ihn durch den Link mit dem Text aus `translation_notice_link`, setzt Sprache und Website-URL und erzeugt Metadaten und Footer. Veröffentlicht wird über **Deploy MkDocs to GitHub Pages**; GitHub Pages muss im Fork für GitHub Actions aktiviert sein.

Übersetzte Texte und eigene übersetzungsspezifische Medien werden unter CC BY 4.0 veröffentlicht. Code, Konfigurationen und fremde Materialien behalten ihre jeweiligen Lizenzen. Diese UGSo-Seite verwendet VitePress als unabhängigen Veröffentlichungsweg und erfüllt denselben öffentlichen Metadatenvertrag.

### Registrierung

Ein Registrierungs-PR im kanonischen UIX-Repository ändert ausschließlich `docs/translations.json`:

```json
{
  "schema": 1,
  "languages": [
    {
      "code": "de",
      "name": "Deutsch",
      "url": "https://docs.example.org/uix/de/",
      "metadata_url": "https://docs.example.org/uix/de/uix-docs.json",
      "curators": ["example-translator"]
    }
  ]
}
```

`code` ist ein kleingeschriebener ISO-639-1-Sprachcode und darf nicht `en` sein. `name` enthält möglichst den muttersprachlichen Sprachnamen. Beide URLs müssen endgültige, öffentliche HTTPS-Adressen sein; Weiterleitungen werden nicht verfolgt. Übersetzte Markdown-Dateien und generierte Dateien gehören nicht in diesen PR.

### Automatische Übersetzungshinweise

Das optionale Feld `curators` enthält GitHub-Namen ohne `@`. Eingetragene Kuratoren werden in der [Discussion für Übersetzungsaktualisierungen](https://github.com/Lint-Free-Technology/uix/discussions/581) erwähnt, sobald englische Quellen oder relevante Dokumentationswerkzeuge auf `dev` oder `master` geändert werden. Deshalb können mehrere E-Mails zu einer Seite eintreffen. Die Änderungen sollten bis zur letzten geprüften Revision gemeinsam abgeglichen werden.

Die Teilnahme ist freiwillig: Trage nur deinen eigenen Namen ein. Ohne `curators` bleibt eine Übersetzung gültig. Änderungen der Registrierung, Builds eines Übersetzungs-Forks und tägliche Health-Checks erzeugen diese Kuratorhinweise nicht. Pull Requests und der manuelle Preview-Modus des Workflows erzeugen nur einen Prüfbericht, keine öffentliche Nachricht.

### Metadaten und Sprachverweise

Die registrierte Metadaten-URL muss mindestens diesen Vertrag erfüllen:

```json
{
  "schema": 1,
  "project": "uix",
  "language": "de",
  "docs_version": "8.2.0",
  "source_revision": "v8.2.0"
}
```

Bei stabilen UIX-Releases muss die Hauptversion übereinstimmen; die aktuelle oder unmittelbar vorherige Minor-Version der Übersetzung ist zulässig. **Vorabversionen behalten das Kompatibilitätsfenster des letzten stabilen Releases:** Bei `8.3.0-beta.1` sind daher `8.1.x` und `8.2.x` zulässig. Erst mit dem stabilen Release `8.3.0` entfällt `8.1.x`.

Ungültige, nicht erreichbare, zu alte oder zukünftige Übersetzungen werden mit einer Warnung aus der Sprachauswahl ausgelassen und blockieren die englische Veröffentlichung nicht.

Zusätzlich wird `uix_sites.json` veröffentlicht. Die Datei beschreibt `schema`, `project`, `language`, `site_url`, `canonical_url` und die englische sowie eigene Alternative in `alternates` als `lang`/`url`-Paare. Im HTML müssen ein selbstreferenzierender `rel="canonical"`-Link sowie englische und eigene `hreflang`-Verweise vorhanden sein. Der tägliche Health-Check kontrolliert die Datei und diese HTML-Verweise; er meldet Probleme nur als Warnungen. Ein grüner Workflow kann deshalb trotzdem offene Warnungen enthalten.

Ein optionales `llms.txt` sollte erklären, dass die Seite eine unabhängige Übersetzung ist und bei technischer Genauigkeit, Syntax, Versionsfragen oder Widersprüchen die englische Dokumentation maßgeblich bleibt. Sprachverweise stellen keine redaktionelle Autorität her.

## Hinweise für Dokumentationsübersetzer

Externe Übersetzungen sollten sich am aktuellen Originalstand orientieren. Bei UIX ist das besonders wichtig, weil viele Beispiele direkt Home-Assistant-YAML enthalten und kleine Unterschiede das Verhalten ändern können.

Empfohlenes Vorgehen:

1. Original-Repository aktualisieren.
2. Änderungen der Dokumentation seit der letzten übersetzten Version prüfen.
3. Neue oder geänderte Seiten übersetzen.
4. Beispiele mit dem Original vergleichen.
5. Lokalen Build ausführen.
6. Versionshinweis und Link zur englischen Originalseite prüfen.

## Version und Originalquelle

Eine externe Übersetzung sollte sichtbar zeigen:

- für welche UIX-Version sie gepflegt wurde
- dass sie eine inoffizielle Übersetzung ist
- wo die englische Originaldokumentation liegt
- wann die Übersetzung zuletzt aktualisiert wurde

So können Nutzer bei Unsicherheit schnell gegen die Originaldokumentation prüfen.

## Bilder und Animationen

Das UIX-Projekt erzeugt viele Bilder und Animationen aus seinem eigenen visuellen Test- und Dokumentationsworkflow. Eine externe Übersetzung sollte diese Assets nicht unnötig duplizieren.

Wenn Bilder benötigt werden, sind diese Wege sinnvoll:

- Originalbilder extern verlinken, wenn das Projekt es erlaubt.
- Eigene Bilder klar als Beispiele der Übersetzung kennzeichnen.
- Keine veralteten Screenshots verwenden, wenn sich die UIX-Oberfläche geändert hat.

## Abgleich mit neuen Releases

Bei neuen Minor-Versionen sollte die Übersetzung neu geprüft werden. Besonders kritisch sind:

- neue Konfigurationsoptionen
- geänderte YAML-Beispiele
- neue Sparks oder Forge-Funktionen
- geänderte Theme-Variablen
- Hinweise zu Breaking Changes

## Pull-Request-Grenze

Für die Registrierung einer externen Übersetzung soll im UIX-Hauptrepository nur die dafür vorgesehene Registrierungsdatei geändert werden. Die eigentliche deutsche Dokumentation bleibt im eigenen Repository.

## Was nicht in einen normalen Beitrag sollte

Bitte vermeide bei Beiträgen zum Originalprojekt:

- automatisch gebaute Dateien, die beim Release erzeugt werden
- doppelte Bilder oder Animationen ohne klaren Grund
- große Formatierungsänderungen ohne fachliche Änderung
- Übersetzungsdateien direkt im Hauptrepository, wenn der externe Übersetzungsweg vorgesehen ist
- Beispiele, die nicht mit dem aktuellen UIX-Verhalten getestet wurden

Damit bleiben Pull Requests kleiner und für Maintainer leichter prüfbar.
