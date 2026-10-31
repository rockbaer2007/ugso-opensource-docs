"""Check built UIX translation links, language metadata and copyable templates."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import hashlib
import json
import sys
from datetime import date


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "docs/.vitepress/dist"
SOURCE = ROOT / "docs/projects/uix"
SITE = "https://opensource.ugso-software.de"
ENGLISH = "https://uix.lf.technology/"
TRANSLATION_ONLY = {"translation-status.md"}


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.hrefs = []
        self.links = []
        self.code = []
        self.images = []
        self.text = []
        self.in_pre = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.hrefs.append(attrs["href"])
        if tag == "link":
            self.links.append(attrs)
        if tag == "img" and "src" in attrs:
            self.images.append(attrs["src"])
        if tag == "pre":
            self.in_pre = True

    def handle_endtag(self, tag):
        if tag == "pre":
            self.in_pre = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_pre:
            self.code.append(data)


def page_url(relative):
    relative = relative.removesuffix("index.md") if relative.endswith("/index.md") or relative == "index.md" else relative.removesuffix(".md")
    return SITE + "/projects/uix/" + relative


def main():
    errors = []
    pages = {}
    sources = sorted(SOURCE.rglob("*.md"))
    for source in sources:
        relative = source.relative_to(SOURCE).as_posix()
        built = DIST / "projects/uix" / Path(relative).with_suffix(".html")
        if not built.is_file():
            errors.append(f"Missing built page: {relative}")
            continue
        page = Page(built.read_text(encoding="utf-8"))
        url = page_url(relative)
        pages[url] = page
        if any(entity in "".join(page.code) for entity in ("&#123;", "&#125;")):
            errors.append(f"Escaped Jinja delimiters in copyable code: {relative}")
        if not any(link.get("rel") == "canonical" and link.get("href") == url for link in page.links):
            errors.append(f"Wrong or missing self-canonical: {relative}")
        if relative not in TRANSLATION_ONLY | {"extras/style-custom-panels.md"}:
            english_path = relative.removesuffix("index.md") if relative.endswith("index.md") else relative.removesuffix(".md") + "/"
            for language, href in (("de", url), ("en", ENGLISH + english_path)):
                if not any(link.get("rel") == "alternate" and link.get("hreflang") == language and link.get("href") == href for link in page.links):
                    errors.append(f"Wrong or missing hreflang={language}: {relative}")

    for locale in ("en", "fr"):
        locale_source = ROOT / f"docs/{locale}/projects/uix"
        for source in sorted(locale_source.rglob("*.md")):
            relative = source.relative_to(locale_source).as_posix()
            built = DIST / f"{locale}/projects/uix" / Path(relative).with_suffix(".html")
            if not built.is_file():
                errors.append(f"Missing {locale} built page: {relative}")
                continue
            page = Page(built.read_text(encoding="utf-8"))
            url = page_url(relative).replace("/projects/uix/", f"/{locale}/projects/uix/")
            pages[url] = page
            if not any(link.get("rel") == "canonical" and link.get("href") == url for link in page.links):
                errors.append(f"Wrong self-canonical: {url}")

    manifest = json.loads((ROOT / "docs/public/projects/uix/canonical-review.json").read_text(encoding="utf-8"))
    if len(manifest["pages"]) != 65:
        errors.append("Canonical review does not cover all 65 source pages")
    for entry in manifest["pages"]:
        for prefix in ("projects/uix", "en/projects/uix", "fr/projects/uix"):
            if not (ROOT / "docs" / prefix / entry["path"]).is_file():
                errors.append(f"Canonical page missing in {prefix}: {entry['path']}")
        english = ROOT / "docs/en/projects/uix" / entry["path"]
        if hashlib.sha256(english.read_text(encoding="utf-8").encode()).hexdigest() != entry["english_sha256"]:
            errors.append(f"Canonical English adaptation changed without resync: {entry['path']}")

    metadata = json.loads((ROOT / "docs/public/projects/uix/uix-docs.json").read_text(encoding="utf-8"))
    if metadata["docs_version"] != metadata["stable_version"]:
        errors.append("UIX stable and documentation metadata versions differ")
    release = f"https://github.com/Lint-Free-Technology/uix/releases/tag/v{metadata['stable_version']}"
    revision = f"https://github.com/Lint-Free-Technology/uix/commit/{metadata['source_revision']}"
    for url, page in pages.items():
        relative = url.split('/projects/uix/', 1)[1]
        if relative == 'extras/style-custom-panels':
            relative = 'extras/style-frame-panels'
        if relative != 'translation-status':
            english_path = relative if not relative or relative.endswith('/') else relative+'/'
            for language, href in (
                ('en', ENGLISH+english_path),
                ('de', SITE+'/projects/uix/'+relative),
                ('fr', SITE+'/fr/projects/uix/'+relative),
            ):
                if not any(link.get('rel') == 'alternate' and link.get('hreflang') == language and link.get('href') == href for link in page.links):
                    errors.append(f'Wrong hreflang={language}: {url}')
        if release not in page.hrefs or revision not in page.hrefs:
            errors.append(f"Version footer does not match release metadata: {url}")
        visible_text = ''.join(page.text)
        if metadata['preview_version'] not in visible_text or metadata['preview_source_revision'][:7] not in visible_text:
            errors.append(f"Preview version/revision missing from page/footer: {url}")
        reviewed = date.fromisoformat(metadata['reviewed_at'])
        review_dates = (reviewed.strftime('%d %B %Y').lstrip('0'),
                        reviewed.strftime('%d/%m/%Y'), reviewed.strftime('%d.%m.%Y'))
        if not any(date in visible_text for date in review_dates):
            errors.append(f"Current review date missing from page/footer: {url}")
        if any(entity in "".join(page.code) for entity in ("&#123;", "&#125;")):
            errors.append(f"Escaped Jinja delimiters in copyable code: {url}")
        for src in page.images:
            target = urlsplit(urljoin(url, src))
            if target.netloc == urlsplit(SITE).netloc and not (DIST / unquote(target.path.lstrip('/'))).is_file():
                errors.append(f"Missing image: {url} -> {src}")
        for href in page.hrefs:
            target = urlsplit(urljoin(url, href))
            if target.netloc != urlsplit(SITE).netloc or not target.path.startswith(("/projects/uix/", "/fr/projects/uix/", "/en/projects/uix/")):
                continue
            target_url = SITE + target.path.removesuffix(".html")
            target_url = target_url.removesuffix("index") if target_url.endswith("/index") else target_url
            if target_url not in pages:
                if Path(target.path).suffix:
                    continue  # Downloads and images are not documentation pages.
                errors.append(f"Missing page target: {url} -> {href}")
            elif target.fragment and unquote(target.fragment) not in pages[target_url].ids:
                errors.append(f"Missing fragment: {url} -> {href}")

    tooltip = pages.get(SITE + "/projects/uix/forge/sparks/tooltip")
    if tooltip and "{{ states(config.element.entity) }}" not in "".join(tooltip.code):
        errors.append("Tooltip example does not preserve its Jinja expression")
    for error in sorted(set(errors)):
        print(error)
    if errors:
        return 1
    print(f"UIX docs check passed: {len(pages)} pages, copyable templates, local links and language metadata.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
