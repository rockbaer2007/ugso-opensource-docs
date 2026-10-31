"""Record/verify UIX source coverage and technical identifiers, not linguistic certification.

Write after a reviewed update: --write --source PATH/TO/ARCHIVED/docs/source
Verify recorded translation hashes and table identifiers: no arguments.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
RECORD = DOCS / "public/projects/uix/translation-review.json"


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def table_keys(text):
    text = re.sub(r"(?ms)^```[^\n]*\n.*?^```", "", text)
    return sorted({key for line in text.splitlines() if line.startswith("|")
                   for key in re.findall(r"`([^`]+)`", line.split("|", 2)[1])})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--source", type=Path)
    parser.add_argument("--review-date", help="Review date for --write (YYYY-MM-DD)")
    args = parser.parse_args()
    canonical = json.loads((DOCS / "public/projects/uix/canonical-review.json").read_text(encoding="utf-8"))
    if args.write and not args.source:
        parser.error("--write requires the archived canonical --source tree")
    previous = None if args.write else json.loads(RECORD.read_text(encoding="utf-8"))
    if previous and previous["source_revision"] != canonical["revision"]:
        raise SystemExit("Translation review uses a different canonical revision")
    previous_pages = {p["path"]: p for p in previous["pages"]} if previous else {}
    result = []
    for entry in canonical["pages"]:
        path = entry["path"]
        english = (DOCS / "en/projects/uix" / path).read_text(encoding="utf-8")
        if digest(english) != entry["english_sha256"]:
            raise SystemExit(f"Unreviewed English adaptation: {path}")
        if args.source:
            source = args.source / path
            if hashlib.sha256(source.read_bytes()).hexdigest() != entry["sha256"]:
                raise SystemExit(f"Canonical source differs: {path}")
        item = {"path": path, "source_sha256": entry["sha256"], "table_identifiers": table_keys(english)}
        for locale, base in (("de", "projects/uix"), ("fr", "fr/projects/uix")):
            text = (DOCS / base / path).read_text(encoding="utf-8")
            missing = [key for key in item["table_identifiers"] if key not in text]
            if missing:
                raise SystemExit(f"Missing {locale} technical identifiers in {path}: {missing}")
            item[locale + "_sha256"] = digest(text)
            item[locale + "_example_blocks"] = len(re.findall(r"(?ms)^```[^\n]*\n.*?^```", text))
            if previous and previous_pages.get(path, {}).get(locale + "_sha256") != item[locale + "_sha256"]:
                raise SystemExit(f"Translation changed since the recorded review: {locale}/{path}")
        result.append(item)
    if len(result) != 65:
        raise SystemExit("Expected the reviewed 65 canonical source pages")
    if args.write:
        RECORD.write_text(json.dumps({
            "reviewed_at": date.fromisoformat(args.review_date).isoformat() if args.review_date else date.today().isoformat(),
            "source_revision": canonical["revision"],
            "scope": "Editorial technical-reference review; page coverage, table identifiers, defaults and selected missing examples",
            "limitations": "Translations retain editorial summaries. Not sentence-by-sentence identity, independent linguistic certification or a Home Assistant runtime test.",
            "pages": result,
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"UIX translation check passed: {len(result)} DE/FR page pairs, source coverage, technical identifiers and recorded hashes.")


if __name__ == "__main__":
    main()
