"""Verify hash-bound editorial content reviews; never approve new pages automatically."""
import hashlib
import argparse
import importlib.util
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--built', action='store_true')
    args = parser.parse_args()
    record = json.loads((ROOT / 'docs/public/documentation-semantic-review.json').read_text(encoding='utf-8'))
    inventory = json.loads((ROOT / 'docs/public/documentation-audit.json').read_text(encoding='utf-8'))
    scope = {row['locales'][locale]['path'] for row in inventory['pages'] for locale in ['en', 'fr']}
    assert record['scope_pages'] == len(scope)
    pages = record['pages']
    canonical = json.loads((ROOT / 'docs/public/projects/uix/canonical-review.json').read_text(encoding='utf-8'))
    canonical_pages = {p['path']: p for p in canonical['pages']}
    assert len({page['target'] for page in pages}) == len(pages)
    assert Counter(p['locale'] for p in pages) == record['coverage']
    for page in pages:
        assert page['target'] in scope
        assert page['assessment'] and page['method'] and page['reviewed_at']
        if 'canonical_reference' in page:
            reference = page['canonical_reference']
            assert reference['revision'] == canonical['revision'], ('Canonical reference changed', page['target'])
            assert reference['source_sha256'] == canonical_pages[reference['path']]['sha256'], ('Canonical content changed', page['target'])
        for kind in ['source', 'target']:
            text = (ROOT / 'docs' / page[kind]).read_text(encoding='utf-8')
            assert hashlib.sha256(text.encode('utf-8')).hexdigest() == page[kind + '_sha256'], ('Content review needs rechecking', page[kind])
    print(f'Editorial content review passed: {len(pages)} reviewed locale pages; {len(scope) - len(pages)} still pending.')
    if args.built:
        spec = importlib.util.spec_from_file_location('content_links', ROOT / 'scripts/check-content-review.py')
        helper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(helper)
        helper.check_built_links(pages)


if __name__ == '__main__':
    main()
