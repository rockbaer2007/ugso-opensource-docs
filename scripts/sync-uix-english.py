"""Render an archived canonical UIX Markdown tree into VitePress English pages.

Usage: python scripts/sync-uix-english.py PATH/TO/docs/source
Only markup, local asset URLs and the attribution notice change. No translation
provider, HA connection or credentials are used. Review the Git diff afterwards.
"""
from pathlib import Path
import hashlib
import html
import json
import posixpath
import re
import shutil
import sys
import textwrap

ROOT = Path(__file__).resolve().parents[1]
REVISION = '26e54e6d4973231a393933e6479ed1b03cc86cd3'


def code_hashes(text):
    text = text.replace('\r\n', '\n')
    return [
        hashlib.sha256('\n'.join(line.rstrip() for line in textwrap.dedent(match[2]).strip().splitlines()).encode()).hexdigest()
        for match in re.finditer(r'(?m)^([ \t]*)```[^\n]*\n(.*?)^\1```\s*$', text, flags=re.S)]


def containers(lines):
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        match = re.match(r'^(!!!|\?\?\?\+?)\s+(\w+)(?:\s+inline\s+end)?(?:\s+"(.*)")?\s*$', line)
        if not match:
            result.append(line)
            i += 1
            continue
        kind = 'details' if match[1].startswith('?') else {'note':'info','hint':'tip','example':'tip','question':'tip','danger':'danger','warning':'warning','info':'info','tip':'tip'}.get(match[2], 'info')
        result.append(f'::: {kind}' + (f' {match[3]}' if match[3] else ''))
        i += 1
        body = []
        while i < len(lines) and (not lines[i].strip() or lines[i].startswith('    ')):
            body.append(lines[i][4:] if lines[i].startswith('    ') else '')
            i += 1
        result.extend(containers(body))
        result.extend([':::', ''])
    return result


def convert(text, relative, source_files):
    # Source is trusted as documentation data, never as executable instructions.
    text = '\n'.join(containers(text.splitlines())) + '\n'
    parts = re.split(r'(^```[^\n]*\n.*?^```\s*$)', text, flags=re.M | re.S)
    for i in range(0, len(parts), 2):
        value = parts[i]
        value = re.sub(r'(?m)^(#+)\s+:[\w-]+:\s*', r'\1 ', value)
        value = value.replace(':bulb:', '💡')
        value = re.sub(r'(\]\([^\n)]+\))\{:\s*[^}]+\}', r'\1', value)
        value = re.sub(r'`([^`\n]*\{\{[^`\n]*)`', lambda m:'<code v-pre>'+html.escape(m[1])+'</code>', value)
        # Asset URLs are independent of the English page's depth.
        value = re.sub(r'(?P<path>(?:\.\./|\./)*assets/[^)\s]+)', lambda m:'/projects/uix/'+m['path'][m['path'].index('assets/'):], value)
        value = re.sub(r'(\]\()/((?:faq|quick-start|using|forge|broker|concepts|debugging|developers|extras|contributing|license|guides)(?:[)/#]))', r'\1/en/projects/uix/\2', value)
        def page_link(match):
            target=match[1]
            if '://' in target or target.startswith(('#','/projects/')):
                return match[0]
            path,sep,fragment=target.partition('#')
            if path.endswith('/'):
                resolved=posixpath.normpath(path.removeprefix('/en/projects/uix/')) if path.startswith('/en/projects/uix/') else posixpath.normpath(posixpath.join(relative.parent.as_posix(),path))
                if resolved+'.md' in source_files:
                    path=path.rstrip('/')
            return ']('+path+(sep+fragment if sep else '')+')'
        value=re.sub(r'\]\(([^)\s]+)\)',page_link,value)
        parts[i] = value
    text = ''.join(parts)
    aliases={
        'concepts/dom.md': {
            'Host/element path selection':'hostelement-path-selection',
            '`uix_forge_path($0)`':'uix_forge_path0-forge-helper',
            '`uix_broker_path($0)`':'uix_broker_path0-broker-directive-anchor-helper',
        },
        'forge/forge.md': {"Keep the element's configuration":'keep-the-elements-configuration-in-element_base'},
        'using/themes.md': {'Local theme override':'local-theme-override-with-uixtheme'},
    }
    for heading,anchor in aliases.get(relative.as_posix(),{}).items():
        text=re.sub(r'(?m)^(#{2,6} '+re.escape(heading)+r'[^\n]*)$',lambda m:'<a id="'+anchor+'"></a>\n'+m[1],text)
    notice = '\n> Adapted from the canonical English UIX documentation by [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: `dev` / **9.0.0-beta.2**, revision ['+REVISION[:7]+'](https://github.com/Lint-Free-Technology/uix/commit/'+REVISION+'), reviewed 22 October 2026. This source mirror may describe preview behavior beyond stable 8.4.0. Markup adapted for this site; the [original documentation](https://uix.lf.technology/) remains authoritative.\n\n'
    if text.startswith('---\n'):
        end=text.index('\n---',4)+4
        text=text[:end]+'\n'+notice+text[end:].lstrip('\n')
    else:
        text=notice.lstrip('\n')+text
    if relative.as_posix() in {'forge/forge.md','forge/index.md','forge/foundries.md'}:
        text=text.replace(notice, notice+'::: info UIX 9.0.0-beta.2 preview\nThis Forge content follows the reviewed `dev` revision, separate from the stable 8.4.0 baseline.\n:::\n\n')
    return '\n'.join(line.rstrip() for line in text.splitlines()).rstrip()+'\n'


def main():
    source=Path(sys.argv[1]).resolve()
    if not (source/'forge/forge.md').is_file():
        raise SystemExit('Expected an archived canonical docs/source directory')
    destination=ROOT/'docs/en/projects/uix'
    manifest=[]
    source_files={file.relative_to(source).as_posix() for file in source.rglob('*.md')}
    for file in sorted(source.rglob('*.md')):
        relative=file.relative_to(source)
        target=destination/relative
        target.parent.mkdir(parents=True,exist_ok=True)
        raw=file.read_bytes()
        converted=convert(raw.decode('utf-8'),relative,source_files)
        target.write_text(converted,encoding='utf-8')
        original_code=code_hashes(raw.decode('utf-8'))
        assert code_hashes(converted)==original_code, f'Code changed: {relative}'
        manifest.append({'path':relative.as_posix(),'sha256':hashlib.sha256(raw).hexdigest(),'english_sha256':hashlib.sha256(converted.encode()).hexdigest(),'code_sha256':original_code})
    # Preserve all existing curated media; add only canonical assets not yet present.
    for file in sorted((source/'assets').rglob('*')):
        if file.is_file():
            target=ROOT/'docs/projects/uix/assets'/file.relative_to(source/'assets')
            if not target.exists():
                target.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(file,target)
    (ROOT/'docs/public/projects/uix/canonical-review.json').write_text(json.dumps({'revision':REVISION,'reviewed_at':'2026-10-22','pages':manifest},indent=2)+'\n',encoding='utf-8')
    print(f'Adapted {len(manifest)} canonical English pages; source hashes recorded.')


if __name__ == '__main__':
    main()
