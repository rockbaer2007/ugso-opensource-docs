"""Check every published menu destination in all locales after docs:build."""
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

root = Path(__file__).resolve().parents[1] / 'docs/.vitepress/dist'
html = (root / 'index.html').read_text(encoding='utf-8')
match = re.search(r'__VP_SITE_DATA__=JSON.parse\(("(?:\\.|[^"\\])*")\)', html)
assert match, 'Built site metadata missing'
data = json.loads(json.loads(match[1]))
assert not data['themeConfig'].get('socialLinks'), 'GitHub must only appear once, in the main menu'
errors = []
count = 0


def check(items, locale):
    global count
    for item in items:
        if 'items' in item:
            check(item['items'], locale)
        if 'link' not in item:
            continue
        count += 1
        link = item['link']
        if not link.startswith('/'):
            continue
        path = unquote(urlsplit(link).path).lstrip('/')
        candidates = [root / path, root / (path + 'index.html' if not path or path.endswith('/') else path + '.html')]
        if not any(candidate.is_file() for candidate in candidates):
            errors.append(f'{locale}: {item["text"]}: {link}')


for locale, config in data['locales'].items():
    nav = config['themeConfig']['nav']
    check(nav, locale)
    assert len(nav) == 10, f'{locale}: expected ten main destinations'
    assert nav[2]['text'] == 'Home Assistant', f'{locale}: Home Assistant menu missing'
    expected = {
        'de': ['Dashboards', 'Apps', 'Integrationen', 'Cards'],
        'en': ['Dashboards', 'Apps', 'Integrations', 'Cards'],
        'fr': ['Dashboards', 'Applications', 'Intégrations', 'Cartes'],
    }
    assert [group['text'] for group in nav[2]['items']] == expected['de' if locale == 'root' else locale]
    assert nav[3]['text'] == 'ATLAS' and nav[7]['text'] == 'UIX'
    prefix = '' if locale == 'root' else f'/{locale}'
    assert nav[4]['text'] == 'ioBroker'
    assert nav[4]['items'] == [{'text': 'Widgets', 'items': [
        {'text': 'UGSo Spezial', 'link': f'{prefix}/iobroker/widgets/ugso-spezial/'}
    ]}]
    assert any(group['text'] == 'Blog' for group in nav[6]['items']), f'{locale}: independent Blog menu missing'

assert not errors, '\n'.join(errors)
print(f'Navigation check passed: {count} menu destinations across DE/EN/FR.')
