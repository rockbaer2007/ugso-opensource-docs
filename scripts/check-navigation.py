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
    check(config['themeConfig']['nav'], locale)

assert not errors, '\n'.join(errors)
print(f'Navigation check passed: {count} menu destinations across DE/EN/FR.')
