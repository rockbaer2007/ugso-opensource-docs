"""Verify the recorded full-file technical comparison, without certifying translation.

No write mode: assessments must be reviewed before their hashes are updated.
"""
import hashlib
import importlib.util
import json
import sys
import argparse
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / 'docs/public/documentation-content-review.json'
sys.dont_write_bytecode = True


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


class BuiltPage(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.references = set()
        self.in_main = False
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'main':
            self.in_main = True
        if self.in_main:
            if tag == 'a' and 'href' in attrs:
                self.references.add(attrs['href'])
            if tag == 'img' and 'src' in attrs:
                self.references.add(attrs['src'])

    def handle_endtag(self, tag):
        if tag == 'main':
            self.in_main = False


def check_built_links(pages):
    dist = ROOT / 'docs/.vitepress/dist'
    cache = {}
    checked = 0

    def read(path):
        if path not in cache:
            cache[path] = BuiltPage(path)
        return cache[path]

    for page in pages:
        built = dist / Path(page['target']).with_suffix('.html')
        assert built.is_file(), ('Missing built page', built)
        base = 'https://docs.invalid/' + page['target'].removesuffix('.md')
        for reference in read(built).references:
            url = urlsplit(urljoin(base, reference))
            if url.scheme not in {'http', 'https'} or url.netloc not in {
                'docs.invalid', 'opensource.ugso-software.de', 'ugso-opensource.net'
            }:
                continue
            path = unquote(url.path).lstrip('/')
            candidates = [dist / path]
            if not Path(path).suffix:
                candidates += [dist / (path + '.html'), dist / path / 'index.html']
            if path.endswith('/'):
                candidates += [dist / path / 'index.html']
            target = next((candidate for candidate in candidates if candidate.is_file()), None)
            assert target, ('Missing built link/image/download', page['target'], reference)
            if url.fragment and target.suffix == '.html':
                assert unquote(url.fragment) in read(target).ids, ('Missing anchor', page['target'], reference)
            checked += 1
    print(f'Built content links passed: {checked} local references, including anchors, images and downloads.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--built', action='store_true', help='Also verify links and anchors in the VitePress build.')
    args = parser.parse_args()
    record = json.loads(RECORD.read_text(encoding='utf-8'))
    pages = record['pages']
    assert len({page['target'] for page in pages}) == len(pages)
    assert Counter(page['locale'] for page in pages) == record['coverage']
    spec = importlib.util.spec_from_file_location('locale_audit', ROOT / 'scripts/audit-doc-locales.py')
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    for page in pages:
        for kind in ['source', 'target']:
            path = ROOT / 'docs' / page[kind]
            assert digest(path.read_text(encoding='utf-8')) == page[kind + '_sha256'], ('Technical comparison needs rechecking', page[kind])
        inspected = audit.inspect(page['target'])
        assert inspected['status'] == 'content-present', page['target']
        assert not inspected['unresolved_local_references'], (page['target'], inspected['unresolved_local_references'])
        assert page['assessment'] and page['language_scope']
        differences = page['differences']
        if any(differences.values()):
            assert page['difference_assessment'], page['target']
    print(f"Content comparison passed: {len(pages)} hash-bound EN/FR file pairs; technical comparison, not linguistic certification.")
    if args.built:
        check_built_links(pages)


if __name__ == '__main__':
    main()
