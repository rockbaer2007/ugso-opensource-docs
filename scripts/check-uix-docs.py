"""Check built UIX translation links, language metadata and copyable templates."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import sys


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
        if tag == "pre":
            self.in_pre = True

    def handle_endtag(self, tag):
        if tag == "pre":
            self.in_pre = False

    def handle_data(self, data):
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
        if relative not in TRANSLATION_ONLY:
            english_path = relative.removesuffix("index.md") if relative.endswith("index.md") else relative.removesuffix(".md") + "/"
            for language, href in (("de", url), ("en", ENGLISH + english_path)):
                if not any(link.get("rel") == "alternate" and link.get("hreflang") == language and link.get("href") == href for link in page.links):
                    errors.append(f"Wrong or missing hreflang={language}: {relative}")

    for url, page in pages.items():
        for href in page.hrefs:
            target = urlsplit(urljoin(url, href))
            if target.netloc != urlsplit(SITE).netloc or not target.path.startswith("/projects/uix/"):
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
