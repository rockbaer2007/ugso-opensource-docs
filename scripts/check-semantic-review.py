"""Verify hash-bound editorial content reviews; never approve new pages automatically."""
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    record = json.loads((ROOT / 'docs/public/documentation-semantic-review.json').read_text(encoding='utf-8'))
    technical = json.loads((ROOT / 'docs/public/documentation-content-review.json').read_text(encoding='utf-8'))
    scope = {p['target'] for p in technical['pages']}
    assert record['scope_pages'] == len(scope)
    pages = record['pages']
    assert len({page['target'] for page in pages}) == len(pages)
    assert Counter(p['locale'] for p in pages) == record['coverage']
    for page in pages:
        assert page['target'] in scope
        assert page['assessment'] and page['method'] and page['reviewed_at']
        for kind in ['source', 'target']:
            text = (ROOT / 'docs' / page[kind]).read_text(encoding='utf-8')
            assert hashlib.sha256(text.encode('utf-8')).hexdigest() == page[kind + '_sha256'], ('Content review needs rechecking', page[kind])
    print(f'Editorial content review passed: {len(pages)} reviewed locale pages; {len(scope) - len(pages)} still pending.')


if __name__ == '__main__':
    main()
