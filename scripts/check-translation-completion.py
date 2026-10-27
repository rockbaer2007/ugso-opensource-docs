"""Verify the reviewed translation batch and immutable technical examples.

After a reviewed edit, --write refreshes hashes. Initial creation also requires
--records PATH to the reviewed source/target list. No translation service is used.
"""
import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
RECORD = DOCS / 'public/translation-completion.json'
FENCE = re.compile(r'^([ \t]*)(`{3,}|~{3,})[^\n]*\n.*?^\1\2[ \t]*$', re.M | re.S)


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def signature(text):
    prose = FENCE.sub('', text)
    return {
        'code': Counter(m[0] for m in FENCE.finditer(text)),
        'inline': Counter(re.findall(r'(?<!`)`([^`\n]+)`(?!`)', prose)),
        'images': Counter(re.findall(r'!\[[^\]]*\]\(([^)]+)\)', prose)),
        'html_images': Counter(re.findall(r'<img\b[^>]*\bsrc="([^"]+)"', prose)),
        'styles': Counter(re.findall(r'<style\b[^>]*>.*?</style>', text, re.S)),
        'encoded_examples': Counter(re.findall(r'data-code-b64="([^"]+)"', text)),
        'rows': len(re.findall(r'^\|.*\|\s*$', prose, re.M)),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--records', type=Path)
    args = parser.parse_args()
    if args.records and not args.write:
        parser.error('--records requires --write')
    if args.records:
        entries = json.loads(args.records.read_text(encoding='utf-8'))
        entries += [{'source': 'impressum/index.md', 'target': f'{lang}/impressum/index.md', 'mode': 'manual'} for lang in ['en', 'fr']]
    else:
        entries = json.loads(RECORD.read_text(encoding='utf-8'))['pages']
    pages = []
    for entry in entries:
        source = (DOCS / entry['source']).read_text(encoding='utf-8')
        target = (DOCS / entry['target']).read_text(encoding='utf-8')
        a, b = signature(source), signature(target)
        assert not (a['code'] - b['code']), (entry['target'], 'changed/missing code block')
        assert not (a['inline'] - b['inline']), (entry['target'], 'missing inline identifiers', a['inline'] - b['inline'])
        assert not (a['images'] - b['images']), (entry['target'], 'missing images')
        for key in ['html_images', 'styles', 'encoded_examples']:
            assert not (a[key] - b[key]), (entry['target'], 'changed/missing', key)
        assert b['rows'] >= a['rows'], (entry['target'], 'missing table rows')
        assert not re.search(r'UGSO(?:P\d|END\d|\d{5})', target), entry['target']
        current = {key: entry[key] for key in ['source', 'target', 'mode']}
        current.update(source_sha256=digest(source), target_sha256=digest(target),
                       source_code_blocks=sum(a['code'].values()), target_code_blocks=sum(b['code'].values()),
                       source_table_rows=a['rows'], target_table_rows=b['rows'])
        if not args.write:
            assert current == entry, ('Review translation after source/target edit', entry['target'])
        pages.append(current)
    gallery = DOCS / '.vitepress/theme/studio-gallery.json'
    gallery_data = json.loads(gallery.read_text(encoding='utf-8'))
    assert all(item[key].get('fr') for item in gallery_data for key in ['title', 'caption'])
    result = {
        'reviewed_at': '2026-10-27',
        'method': 'Translation-assisted public documentation, technical comparison with German sources and targeted manual corrections. Legal notices translated manually. Not a complete linguistic certification.',
        'coverage': {'english_placeholders_replaced': 37, 'french_placeholders_replaced': 91,
                     'french_missing_pages_added': 20, 'supplemented_pages': 14},
        'gallery_sha256': digest(gallery.read_text(encoding='utf-8')),
        'pages': pages,
    }
    if args.write:
        RECORD.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    else:
        assert result == json.loads(RECORD.read_text(encoding='utf-8')), 'Stale completion record'
    print(f'Translation completion check passed: {len(pages)} pages; code, identifiers, tables, images and FR gallery captions preserved.')


if __name__ == '__main__':
    main()
