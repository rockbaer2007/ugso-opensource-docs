"""Inventory every DE/EN/FR documentation page; do not infer linguistic parity.

--write records source hashes, structural differences and a report in each locale.
Without --write, verify that the recorded inventory still matches the sources.
"""
import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
REPORT = DOCS / 'public/documentation-audit.json'
LOCALE_MAP = DOCS / '.vitepress/page-locales.json'
REVIEW = DOCS / 'public/documentation-review.json'
CONTENT_REVIEW = DOCS / 'public/documentation-content-review.json'
SLUGS = {
    'blog/beitragsvorlage.md': 'blog/post-template.md',
    'projects/atlas/uebersicht.md': 'projects/atlas/overview.md',
    'projects/atlas/entwicklungsstand.md': 'projects/atlas/development-status.md',
    'projects/atlas-plugins/gepruefte-plugins.md': 'projects/atlas-plugins/verified-plugins.md',
    'projects/grafik-visual-studio/tool-pakete.md': 'projects/grafik-visual-studio/tool-packages.md',
    'projects/grafik-visual-studio/widget-pakete.md': 'projects/grafik-visual-studio/widget-packages.md',
    'projects/hadash/ansicht-exportieren.md': 'projects/hadash/export-view.md',
    'projects/hadash/backups-und-json.md': 'projects/hadash/backups-and-json.md',
    'projects/hadash/dashboard-einlesen.md': 'projects/hadash/import-dashboard.md',
    'projects/hadash/erste-schritte.md': 'projects/hadash/getting-started.md',
    'projects/hadash/portable-nutzung.md': 'projects/hadash/portable-usage.md',
    'projects/ultimate-timer/funktionsweise.md': 'projects/ultimate-timer/how-it-works.md',
}
for project in ['fritzbox-to-mqtt', 'heizoel-to-mqtt', 'parcel-to-mqtt', 'ultimate-timer']:
    for german, english in [('beispiele', 'examples'), ('entitaeten', 'entities'),
                             ('konfiguration', 'configuration'), ('fehlersuche', 'troubleshooting')]:
        SLUGS[f'projects/{project}/{german}.md'] = f'projects/{project}/{english}.md'
COLLECTION = {'ha-empfehlungen': 'ha-recommendations', 'ha-integrationen': 'ha-integrations',
              'testsysteme': 'test-systems',
              'ha-2026-11-kompatibilitaet': 'ha-2026-11-compatibility',
              'hacs-dokus': 'hacs-docs', 'weitere-beispiele': 'interesting-examples'}
PLACEHOLDER = re.compile(r'has been (?:added|created) so the Open Source|Cette page française a été (?:ajoutée|créée)')


def translated(path):
    if path.startswith('sammlung/'):
        parts = path.split('/')
        parts[0] = 'collection'
        stem = parts[1].removesuffix('.md')
        if stem in COLLECTION:
            parts[1] = COLLECTION[stem] + '.md'
        return '/'.join(parts)
    return SLUGS.get(path, path)


def route(path):
    return '/' + (path.removesuffix('index.md') if path.endswith('index.md') else path.removesuffix('.md'))


def local_target(source, value):
    value = unquote(value.split(' ', 1)[0].strip('<>'))
    url = urlsplit(urljoin('https://docs.invalid/' + source, value))
    if url.netloc != 'docs.invalid' or not url.path:
        return True
    path = url.path.lstrip('/')
    if any(char in path for char in ['*', '{', '}']):
        return True
    candidates = [DOCS / path, DOCS / 'public' / path]
    if not Path(path).suffix:
        candidates += [DOCS / (path + '.md'), DOCS / path / 'index.md']
    return any(candidate.is_file() for candidate in candidates)


def inspect(path):
    file = DOCS / path
    if not file.is_file():
        return {'path': path, 'status': 'missing'}
    raw = file.read_text(encoding='utf-8')
    body = re.sub(r'\A---\r?\n.*?\r?\n---\r?\n', '', raw, flags=re.S)
    examples = len(re.findall(r'^\s*```[^\n]*\n', body, re.M)) // 2
    prose = re.sub(r'^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$', '', body, flags=re.S | re.M)
    versions = set(re.findall(r'(?<![\w.])v?(\d+\.\d+\.\d+(?:-(?:alpha|beta|rc|dev|mydev)(?:\.[A-Za-z0-9]+)*)?)(?!\d|\.\d)', prose))
    # German dates and grammatical compounds such as "0.1.330-Prüfung"
    # must not become spurious software versions.
    versions = sorted(v for v in versions if not re.fullmatch(r'(?:0?[1-9]|[12]\d|3[01])\.(?:0?[1-9]|1[0-2])\.(?:19|20)\d\d', v))
    references = re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', prose)
    references += re.findall(r'\b(?:href|src)=["\']([^"\']+)["\']', prose)
    broken = sorted({ref for ref in references if not ref.startswith('#') and not local_target(path, ref)})
    return {'path': path, 'status': 'placeholder' if PLACEHOLDER.search(raw) else 'content-present',
            'sha256': hashlib.sha256(raw.encode()).hexdigest(),
            'words': len(re.findall(r'\w+', re.sub('<[^>]+>', '', prose))),
            'headings': len(re.findall(r'^#{1,6} ', body, re.M)),
            'examples': examples, 'versions': versions, 'unresolved_local_references': broken}


def inventory(reviewed_at):
    reviewed = {entry['target']: entry for entry in json.loads(REVIEW.read_text(encoding='utf-8'))['pages']} if REVIEW.exists() else {}
    content_reviews = {entry['target']: entry for entry in json.loads(CONTENT_REVIEW.read_text(encoding='utf-8'))['pages']} if CONTENT_REVIEW.exists() else {}
    sources = sorted(p.relative_to(DOCS).as_posix() for p in DOCS.rglob('*.md')
                     if p.relative_to(DOCS).parts[0] not in ['en', 'fr', '.vitepress', 'public']
                     and p.name != 'documentation-status.md')
    rows = []
    matched = {'de': set(), 'en': set(), 'fr': set()}
    for source in sources:
        row = {'source': source, 'locales': {}}
        for locale in ['de', 'en', 'fr']:
            path = source if locale == 'de' else f'{locale}/{translated(source)}'
            item = inspect(path)
            matched[locale].add(path)
            if locale != 'de' and item['status'] == 'content-present':
                de = row['locales']['de']
                item['review_signals'] = {
                    'versions_only_in_de': sorted(set(de['versions']) - set(item['versions'])),
                    'versions_only_in_translation': sorted(set(item['versions']) - set(de['versions'])),
                    'fewer_examples': item['examples'] < de['examples'],
                    'substantially_shorter': de['words'] >= 100 and item['words'] < de['words'] * 0.55,
                    'fewer_headings': item['headings'] < de['headings'],
                }
                entry = reviewed.get(path)
                if entry:
                    current = entry['source_sha256'] == de['sha256'] and entry['target_sha256'] == item['sha256']
                    item['review'] = {'status': 'reviewed' if current else 'needs-recheck',
                                      'disposition': entry['disposition'], 'reason': entry['reason']}
                content_entry = content_reviews.get(path)
                if content_entry:
                    current = content_entry['source_sha256'] == de['sha256'] and content_entry['target_sha256'] == item['sha256']
                    item['content_review'] = {
                        'status': 'technically-compared' if current else 'needs-recheck',
                        'reviewed_at': content_entry['reviewed_at'],
                        'assessment': content_entry['assessment'],
                        'language_scope': content_entry['language_scope'],
                    }
            row['locales'][locale] = item
        rows.append(row)
    extras = {}
    summary = {}
    for locale in ['de', 'en', 'fr']:
        files = {p.relative_to(DOCS).as_posix() for p in (DOCS / (locale if locale != 'de' else '')).rglob('*.md')
                 if p.relative_to(DOCS).parts[0] not in ['.vitepress', 'public']
                 and (locale != 'de' or p.relative_to(DOCS).parts[0] not in ['en', 'fr'])
                 and p.name != 'documentation-status.md'}
        extras[locale] = sorted(files - matched[locale])
        counts = Counter(row['locales'][locale]['status'] for row in rows)
        summary[locale] = dict(counts, existing_pages=len(files), unmatched_pages=len(extras[locale]),
                              review_signals=sum(any(row['locales'][locale].get('review_signals', {}).values()) for row in rows),
                              reviewed_findings=sum(row['locales'][locale].get('review', {}).get('status') == 'reviewed' for row in rows),
                              technically_compared=sum(row['locales'][locale].get('content_review', {}).get('status') == 'technically-compared' for row in rows),
                              open_review_signals=sum(
                                  row['locales'][locale].get('content_review', {}).get('status') == 'needs-recheck'
                                  or (any(row['locales'][locale].get('review_signals', {}).values())
                                      and row['locales'][locale].get('review', {}).get('status') != 'reviewed')
                                  for row in rows))
    return {'reviewed_at': reviewed_at, 'hash_format': 'SHA-256 of UTF-8 text with normalized LF line endings', 'scope': 'All Markdown pages, excluding these generated reports. Structural and technical inventory, not a sentence-by-sentence translation certification or an upstream-release audit.',
            'source_pages': len(sources), 'summary': summary, 'unmatched_pages': extras, 'pages': rows}


COPY = {
 'de': {
  'title': 'Sprachstand der Dokumentation',
  'intro': 'Die Dokumentation ist **noch nicht auf demselben Stand**. Die französische Startseite wurde an Aufbau, Markenbilder, Schaltflächen und Inhalt der deutschen Startseite angepasst.',
  'scope': 'Geprüft wurden sämtliche Markdown-Inhaltsseiten, ohne diese drei erzeugten Berichtsseiten: vorhandene Sprachfassungen, Platzhalter, Versionsnennungen, Überschriften, Codebeispiele und auflösbare lokale Seiten-/Bildverweise. Unterschiedliche Versionslisten oder Textlängen sind Prüfhinweise, kein automatischer Beweis für veraltete Inhalte. „Inhalt vorhanden“ bestätigt keine vollständige oder sprachlich geprüfte Übersetzung. Das Inventar prüft Upstream-Releases nicht automatisch; separat dokumentierte Quellenabgleiche wie bei UIX bleiben maßgeblich.',
  'head': 'Vollständiges Seiteninventar', 'column': 'Deutsche Referenz',
  'statuses': {'missing': 'Fehlt', 'placeholder': 'Platzhalter', 'content-present': 'Inhalt vorhanden'},
  'signal': 'Prüfhinweise', 'summary': 'Bestandsaufnahme',
  'counts': ['Sprache', 'Seiten vorhanden', 'Fehlende Seiten', 'Platzhalter', 'Weitere Prüfhinweise'],
  'details': 'Der vollständige JSON-Bericht enthält für jede Seite die Pfade, SHA-256-Prüfsummen, Versionsunterschiede, Strukturwerte und nicht aufgelöste lokale Verweise.',
  'priority': 'Zuerst fehlen in FR 19 Seiten von Grafik Visual Studio und die MQTT-Client-Seite. Darüber hinaus müssen die Platzhalter in Sammlung, Blog, HA-Apps und älteren Projektbereichen inhaltlich übersetzt werden. Bestehende vollständige Übersetzungen und die separat geprüfte UIX-Dokumentation bleiben erhalten.',
 },
 'en': {
  'title': 'Documentation language status',
  'intro': 'The documentation is **not yet at the same level in all languages**. The French home page now follows the German page’s layout, brand images, buttons and content.',
  'scope': 'Every Markdown content page was inventoried, excluding these three generated reports: locale coverage, placeholder text, version mentions, headings, code examples and resolvable local page/image references. Different version lists or text lengths are review signals, not automatic evidence of outdated content. “Content present” does not certify a complete or linguistically reviewed translation. The inventory does not automatically audit upstream releases; separately documented source comparisons, such as UIX, remain authoritative for that scope.',
  'head': 'Complete page inventory', 'column': 'German reference',
  'statuses': {'missing': 'Missing', 'placeholder': 'Placeholder', 'content-present': 'Content present'},
  'signal': 'Review signals', 'summary': 'Inventory',
  'counts': ['Language', 'Existing pages', 'Missing pages', 'Placeholders', 'Other review signals'],
  'details': 'The complete JSON report records paths, SHA-256 hashes, version differences, structural metrics and unresolved local references for every page.',
  'priority': 'French is missing 19 Grafik Visual Studio pages and the MQTT Client page. Placeholder pages in the collection, blog, HA apps and older project sections also require translation. Existing full translations and the separately reviewed UIX documentation are preserved.',
 },
 'fr': {
  'title': 'État des traductions de la documentation',
  'intro': 'La documentation **n’est pas encore au même niveau dans les trois langues**. La page d’accueil française reprend désormais la structure, les images des marques, les boutons et le contenu de la page allemande.',
  'scope': 'Toutes les pages de contenu Markdown ont été inventoriées, à l’exclusion de ces trois rapports générés : langues disponibles, textes provisoires, versions mentionnées, titres, exemples de code et références locales aux pages et images. Des versions ou longueurs différentes sont des points à examiner, pas une preuve automatique d’obsolescence. « Contenu présent » ne garantit pas une traduction complète ou vérifiée sur le plan linguistique. Cet inventaire ne contrôle pas automatiquement les versions en amont ; les comparaisons de sources documentées séparément, comme pour UIX, restent la référence pour leur périmètre.',
  'head': 'Inventaire complet des pages', 'column': 'Référence allemande',
  'statuses': {'missing': 'Absente', 'placeholder': 'Texte provisoire', 'content-present': 'Contenu présent'},
  'signal': 'Points à examiner', 'summary': 'Inventaire',
  'counts': ['Langue', 'Pages existantes', 'Pages absentes', 'Textes provisoires', 'Autres points à examiner'],
  'details': 'Le rapport JSON complet contient, pour chaque page, les chemins, empreintes SHA-256, différences de versions, indicateurs de structure et références locales non résolues.',
  'priority': 'Il manque en français 19 pages de Grafik Visual Studio et la page du client MQTT. Les textes provisoires de la collection, du blog, des applications HA et des anciens projets doivent également être traduits. Les traductions complètes existantes et la documentation UIX vérifiée séparément sont conservées.',
 }
}


def render_report(report, locale):
    text = dict(COPY[locale])
    text['counts'] = list(text['counts'])
    text['counts'][-1] = {'de': 'Offene Prüfhinweise', 'en': 'Open review findings', 'fr': 'Points restant à examiner'}[locale]
    complete = all(not counts.get('missing') and not counts.get('placeholder') for counts in report['summary'].values())
    if complete:
        text['intro'] = {
            'de': 'Alle deutschen Referenzseiten sind jetzt auch in EN und FR mit Inhalt vorhanden. Die 128 Platzhalter wurden ersetzt und die 20 fehlenden französischen Seiten ergänzt.',
            'en': 'All German reference pages now have English and French content. The 128 placeholder pages have been replaced and the 20 missing French pages added.',
            'fr': 'Toutes les pages de référence allemandes disposent désormais de contenu en anglais et en français. Les 128 pages provisoires ont été remplacées et les 20 pages françaises manquantes ajoutées.'
        }[locale]
        text['priority'] = {
            'de': 'Die Ergänzungen wurden mit Übersetzungsunterstützung erstellt und technisch gegen die deutsche Vorlage geprüft: Code, Bezeichner, Tabellen und Bilder. 14 weitere Inhaltslücken wurden als ergänzende Referenz geschlossen; vorhandene Seiten und Links bleiben erhalten. Das ist keine vollständige sprachliche Zertifizierung. Verbleibende Prüfhinweise betreffen auch bewusst unterschiedliche Zusammenfassungen und historische Versionsangaben.',
            'en': 'The additions were created with translation assistance and checked technically against the German source: code, identifiers, tables and images. Fourteen further content gaps were filled with supplementary references while preserving existing pages and links. This is not a complete linguistic certification. Remaining review signals also include intentionally different summaries and historical version mentions.',
            'fr': 'Les ajouts ont été réalisés avec une aide à la traduction et vérifiés techniquement par rapport à la source allemande : code, identifiants, tableaux et images. Quatorze autres lacunes ont été comblées par des références complémentaires, en conservant les pages et liens existants. Il ne s’agit pas d’une certification linguistique complète. Les points à examiner comprennent aussi des résumés volontairement différents et des versions historiques.'
        }[locale]
    lines = ['---', f'title: {text["title"]}', 'sidebar: false', 'aside: false', '---', '',
             f'# {text["title"]}', '', f'DE / EN / FR · {report["reviewed_at"]}', '', text['intro'], '', text['scope'], '',
             f'## {text["summary"]}', '', '| ' + ' | '.join(text['counts']) + ' |', '| --- | ---: | ---: | ---: | ---: |']
    for language, counts in report['summary'].items():
        lines.append(f'| {language.upper()} | {counts["existing_pages"]} | {counts.get("missing", 0)} | {counts.get("placeholder", 0)} | {counts["open_review_signals"]} |')
    if sum(counts['reviewed_findings'] for counts in report['summary'].values()):
        lines += ['', {
            'de': f'**Technischer Abgleich vom {report["reviewed_at"]}:** Vorhandene Einzelbewertungen sind an die aktuellen Datei-Prüfsummen gebunden; Änderungen erfordern eine erneute Prüfung. Echte Lücken und widersprüchliche Angaben werden korrigiert, bewusst unterschiedliche Versionshistorien und redaktionelle Gliederungen mit Begründung eingeordnet. Die Tabelle zeigt die noch offenen Hinweise; der JSON-Bericht behält die automatischen Rohsignale bei. „0 offen“ bedeutet geprüft und eingeordnet, nicht wortgleiche Übersetzungen. [Dokumentierte Einzelbewertungen](/documentation-review.json).',
            'en': f'**Technical comparison of {report["reviewed_at"]}:** Existing assessments are bound to current file hashes; changes require another review. Actual gaps and contradictions are corrected, while intentional differences in version history and editorial structure have recorded explanations. The table shows outstanding findings; raw automatic signals remain in the JSON report. “0 open” means reviewed and classified, not word-for-word identity. [Recorded assessments](/documentation-review.json).',
            'fr': f'**Comparaison technique du {report["reviewed_at"]} :** les évaluations sont liées aux empreintes actuelles des fichiers ; toute modification exige une nouvelle revue. Les lacunes et contradictions sont corrigées, tandis que les différences voulues d’historique et de structure sont justifiées. Le tableau indique les points encore ouverts ; le JSON conserve les signaux automatiques bruts. « 0 restant » signifie examiné et classé, pas une identité mot à mot. [Évaluations documentées](/documentation-review.json).'
        }[locale], '']
    lines += ['', text['priority'], '', text['details'], '', '[JSON](/documentation-audit.json)', '',
              '[UIX DE](/projects/uix/translation-status) · [UIX EN](/en/projects/uix/translation-status) · [UIX FR](/fr/projects/uix/translation-status)', '',
              f'## {text["head"]}', '', f'| {text["column"]} | EN | FR |', '| --- | --- | --- |']
    if CONTENT_REVIEW.exists():
        counts = report['summary']
        note = {
            'de': f'**Erweiterter Abgleich vom 20.11.2026: {counts["en"]["technically_compared"]} EN- und {counts["fr"]["technically_compared"]} FR-Seiten.** Alle zuvor nur als „Inhalt vorhanden“ ausgewiesenen Dateien wurden vollständig technisch mit ihrer Referenz verglichen: Versionen, Codeblöcke, technische Bezeichner und Verweise. Abweichungen wurden einzeln eingeordnet; eine automatische Sprachsuche wurde durch die Korrektur der gefundenen englischen Textreste ergänzt. **„Technisch abgeglichen“ ist keine vollständige sprachliche oder satzweise Inhaltsfreigabe.** „Unterschied geprüft“ bleibt die frühere Bewertung struktureller Abweichungen. „Erneut prüfen“ erscheint, sobald sich eine der beiden Dateien ändert. [Prüfumfang und Einzelbewertungen](/documentation-content-review.json).',
            'en': f'**Extended comparison of 2026-11-20: {counts["en"]["technically_compared"]} EN and {counts["fr"]["technically_compared"]} FR pages.** Every file previously labelled only “Content present” was technically compared in full against its reference: versions, code blocks, technical identifiers and links. Differences were individually classified; automatic language screening was followed by corrections to the English prose found in French pages. **“Technically compared” is not a full linguistic or sentence-by-sentence content approval.** “Difference reviewed” retains the earlier structural assessment. “Recheck required” appears when either file changes. [Scope and individual assessments](/documentation-content-review.json).',
            'fr': f'**Comparaison étendue du 20 novembre 2026 : {counts["en"]["technically_compared"]} pages EN et {counts["fr"]["technically_compared"]} pages FR.** Tous les fichiers auparavant marqués uniquement « Contenu présent » ont été comparés intégralement à leur référence sur le plan technique : versions, blocs de code, identifiants et liens. Les différences ont été classées individuellement ; la détection automatique de langue a été suivie de la correction des passages anglais trouvés dans les pages françaises. **« Comparaison technique effectuée » ne constitue pas une validation linguistique complète ni une vérification du contenu phrase par phrase.** « Différence examinée » conserve l’évaluation structurelle antérieure. « À revérifier » apparaît dès qu’un des fichiers change. [Périmètre et évaluations](/documentation-content-review.json).',
        }[locale]
        # Explain the labels before readers reach the page table.
        index = next(i for i, line in enumerate(lines) if line == f'## {text["head"]}')
        fixes = {
            'de': 'Korrigiert wurden französische UIX-Textreste in Konzepten, Makros, Themes und Kamera-Hintergründen, ein JavaScript-Syntaxfehler im Entwicklerbeispiel sowie sieben Sprungmarken und zwei Videolinks. Die Rückfallregel für `active: false` beim Lock Spark ist in DE/FR präzisiert. Beispiele, Medien und vorhandene Anker bleiben erhalten.',
            'en': 'Corrections include English prose left in French UIX concepts, macros, themes and camera backgrounds, a JavaScript syntax error in the developer example, seven anchor links and two video links. The Lock Spark active:false fallback is clarified in DE/FR. Examples, media and existing anchors are preserved.',
            'fr': 'Corrections : passages anglais dans les concepts, macros, thèmes et arrière-plans caméra UIX français, erreur de syntaxe JavaScript dans l’exemple développeur, sept liens d’ancrage et deux liens vidéo. La règle de repli active:false du spark Lock est précisée en DE/FR. Les exemples, médias et ancres existants sont conservés.',
        }[locale]
        lines[index:index] = [note, '', fixes, '']
    for row in report['pages']:
        cells = [f'[{row["source"]}]({route(row["source"])})']
        for language in ['en', 'fr']:
            item = row['locales'][language]
            status = text['statuses'][item['status']]
            content_status = item.get('content_review', {}).get('status')
            if content_status:
                status = ({'de': 'Technisch abgeglichen', 'en': 'Technically compared', 'fr': 'Comparaison technique effectuée'} if content_status == 'technically-compared' else {'de': 'Erneut prüfen', 'en': 'Recheck required', 'fr': 'À revérifier'})[locale]
            if any(item.get('review_signals', {}).values()):
                status += ' · ' + ({'de': 'Unterschied geprüft', 'en': 'Difference reviewed', 'fr': 'Différence examinée'}[locale] if item.get('review', {}).get('status') == 'reviewed' else text['signal'])
            cells.append(status if item['status'] == 'missing' else f'[{status}]({route(item["path"])})')
        lines.append('| ' + ' | '.join(cells) + ' |')
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--review-date', help='Reviewed date in YYYY-MM-DD format; otherwise preserve the recorded date.')
    args = parser.parse_args()
    recorded = json.loads(REPORT.read_text(encoding='utf-8')) if REPORT.exists() else {}
    reviewed_at = args.review_date or recorded.get('reviewed_at', '2026-10-27')
    date.fromisoformat(reviewed_at)
    report = inventory(reviewed_at)
    locale_map = {}
    for row in report['pages']:
        targets = {locale.upper(): route(item['path']) for locale, item in row['locales'].items()
                   if item['status'] != 'missing'}
        for target in targets.values():
            locale_map[target] = targets
    if args.write:
        LOCALE_MAP.write_text(json.dumps(locale_map, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        for locale in COPY:
            target = DOCS / (locale if locale != 'de' else '') / 'documentation-status.md'
            target.write_text(render_report(report, locale), encoding='utf-8')
    else:
        assert json.loads(LOCALE_MAP.read_text(encoding='utf-8')) == locale_map, 'Stale page locale map.'
        assert report == recorded, 'Documentation inventory changed; review and regenerate with --write.'
        for locale in COPY:
            target = DOCS / (locale if locale != 'de' else '') / 'documentation-status.md'
            assert target.read_text(encoding='utf-8') == render_report(report, locale), f'Stale report: {target}'
    print(json.dumps({'source_pages': report['source_pages'], 'summary': report['summary'], 'unmatched_pages': report['unmatched_pages']}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
