"""Verify all reviewed findings and the requested EEP/package overview assets."""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
FENCE = re.compile(r'^```[^\n]*\n.*?^```', re.M | re.S)


def digest(path):
    return hashlib.sha256(path.read_text(encoding='utf-8').encode()).hexdigest()


def main():
    review = json.loads((DOCS / 'public/documentation-review.json').read_text(encoding='utf-8'))
    assert Counter(p['locale'] for p in review['pages']) == {'en': 74, 'fr': 47}
    assert len({p['target'] for p in review['pages']}) == 121
    for page in review['pages']:
        for kind in ['source', 'target']:
            assert digest(DOCS / page[kind]) == page[kind + '_sha256'], ('Review needs updating', page[kind])
        assert page['disposition'] and page['reason'], page['target']
    for entry in review['example_supplements']:
        source = (DOCS / entry['source']).read_text(encoding='utf-8')
        target = (DOCS / entry['target']).read_text(encoding='utf-8')
        assert all(code in target for code in set(FENCE.findall(source))), ('Missing source configuration', entry['target'])
    for locale, lang in [('', 1), ('en/', 2), ('fr/', 3)]:
        text = (DOCS / locale / 'eep/index.md').read_text(encoding='utf-8')
        quote = re.search(r'^> ', text, re.M)
        assert quote and text.index('/images/eep/eep18-banner.png') < text.index('/images/eep/eep18-layout.png') < quote.start()
        assert f'https://eepshopping.de/?lang={lang}' in text
        assert '© Trend Verlag Freiburg' in text
        assert '[Mein EEP Forum](http://www.eepforum.de/index.php?page=Portal)' in text
        assert 'eep-brand-logo' in text and '{#eep}' in text
        for name in ['eep18-banner.png', 'eep18-layout.png', 'logo-eep.png']:
            assert (DOCS / 'public/images/eep' / name).is_file()
    icons = json.loads((DOCS / 'public/images/packages/sources.json').read_text(encoding='utf-8'))
    for path, heading, status in [
        ('sammlung/ha-integrationen.md', 'Fertige Dokumentationen', 'Vollständig'),
        ('en/collection/ha-integrations.md', 'Completed documentation', 'Complete'),
        ('fr/collection/ha-integrations.md', 'Documentations terminées', 'Complète'),
    ]:
        text = (DOCS / path).read_text(encoding='utf-8')
        assert heading in text and status in text and 'Frosted Glass' in text, path
    for item in icons.values():
        asset = DOCS / 'public' / item['asset'].lstrip('/')
        content = asset.read_text(encoding='utf-8').encode() if item['hash_format'] == 'UTF-8 with normalized LF' else asset.read_bytes()
        assert hashlib.sha256(content).hexdigest() == item['sha256'], asset
    for page in ['en/projects/uix/debugging/cache.md', 'fr/projects/uix/debugging/cache.md']:
        text = (DOCS / page).read_text(encoding='utf-8')
        assert 'localStorage' in text and 'll-custom-actions.ts#L224-L242' in text
    print(f"Documentation review passed: 121 findings, {sum(p['added_examples'] for p in review['example_supplements'])} reference configurations, EEP language links/image order/copyright and {len(icons)} unchanged package icons.")


if __name__ == '__main__':
    main()
