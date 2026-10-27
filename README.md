# UGSo Open Source Docs

VitePress-Dokumentation für:

```text
https://opensource.ugso-software.de/
```

## Lokal starten

```powershell
npm install
npm run docs:dev
```

Lokal öffnen:

```text
http://localhost:5173/
```

## Sprachinventar / Language inventory / Inventaire des langues

DE: Nach Inhaltsänderungen die Sprachunterschiede prüfen und den Bericht aktualisieren.
EN: Review locale differences after content changes and refresh the report.
FR : Après une modification, vérifier les écarts entre langues et actualiser le rapport.

```powershell
python scripts/audit-doc-locales.py --write --review-date 2026-10-27
python scripts/audit-doc-locales.py
npm run docs:build
```

Das Datum durch das tatsächliche Prüfdatum ersetzen. Der Bericht listet fehlende
Seiten, Platzhalter und technische Prüfhinweise; er übersetzt keine Inhalte und
bestätigt keine vollständige sprachliche Gleichwertigkeit. Die drei erzeugten
Statusseiten und `docs/public/documentation-audit.json` zusammen committen.

## GitHub Pages einrichten

1. Repository zu GitHub pushen.
2. Unter `Settings -> Pages` die Quelle `GitHub Actions` auswählen.
3. Als Custom Domain eintragen:

```text
opensource.ugso-software.de
```

4. Beim Domainanbieter einen CNAME setzen:

```text
opensource -> rockbaer2007.github.io
```

Die Datei `docs/public/CNAME` ist bereits enthalten.

## Zwei Domains, eine Dokumentationsquelle / Two domains / Deux domaines

DE: `opensource.ugso-software.de` bleibt die bisherige Hauptveröffentlichung.
`ugso-opensource.net` erhält denselben geprüften DE/EN/FR-Build im separaten
Repository `rockbaer2007/ugso-opensource-net`. Nach erfolgreicher Veröffentlichung
der bisherigen Seite synchronisiert der Workflow die zweite Seite automatisch.
Die aufgerufene Domain bleibt in der Adresszeile; Canonical-Verweise bleiben zur
Vermeidung doppelter Suchmaschineneinträge bei der bisherigen Domain.

EN: Both domains serve the same verified DE/EN/FR build. Edit documentation only
in this repository. After the original Pages deployment succeeds, the workflow
publishes the same build to `rockbaer2007/ugso-opensource-net`. Navigation stays on
the requested domain; canonical links retain the original domain for search engines.

FR : Les deux domaines servent le même site DE/EN/FR vérifié. Modifier les sources
uniquement dans ce dépôt. Après le déploiement réussi du site existant, le workflow
publie le même résultat dans `rockbaer2007/ugso-opensource-net`. La navigation conserve
le domaine demandé ; les liens canoniques gardent le domaine initial pour les moteurs
de recherche.

### Betrieb / Operations / Exploitation

- Source: `.github/workflows/docs.yml`, job `mirror`.
- Target: `ugso-opensource-net`, branch `main`, Pages from `/`.
- Secret: `NET_MIRROR_DEPLOY_KEY`, SSH deploy key with write access only to the target repository.
- `deployment.json` records the source revision and locales on the second site.
- Re-run the workflow with `workflow_dispatch` to retry a failed mirror deployment.
- No STRATO, Home Assistant or other application credentials are needed by this workflow.
- DNS and HTTPS instructions: [DOMAIN-SETUP.md](DOMAIN-SETUP.md).
