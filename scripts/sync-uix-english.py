"""Render an archived canonical UIX Markdown tree into VitePress English pages.

Usage: python scripts/sync-uix-english.py PATH/TO/docs/source
Markup, local URLs and attribution are adapted. Explicit, source-bound editorial
corrections below also repair a known syntax error and an index description. No translation
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
REVISION = 'fb36536e5836d595637fbf3bc253d5fc0d3ed8d6'
REVIEWED_AT = '2026-11-20'
SOURCE_VERSION = '9.1.0'
SOURCE_BRANCH = 'dev'


def code_hashes(text):
    text = text.replace('\r\n', '\n')
    return [
        hashlib.sha256('\n'.join(line.rstrip() for line in textwrap.dedent(match[2]).strip().splitlines()).encode()).hexdigest()
        for match in re.finditer(r'(?m)^([ \t]*)```[^\n]*\n(.*?)^\1```\s*$', text, flags=re.S)]


def reviewed_corrections(text, raw, relative):
    """Fail closed if either frozen upstream passage changes."""
    path = relative.as_posix()
    expected_sources = {
        'developers/cards.md': 'b015e562376a5bb3b6c437b48d2b0a1c461419490667859b1c2bad9963806d1d',
        'forge/sparks/index.md': '97178ef31bb7b5b88e10e2cc7531e020b80328d3ca7ddb5a46d035ba2585ec70',
        'concepts/application.md': '24be57e32f05eed9eafede271b99958f51dd94d3435666a2ba5a79f24c7f242a',
        'forge/sparks/tile-icon.md': 'eaf8210dbf464eca19c3a96113bc5f9812128c2dd5803e6df91cb728dc4376a5',
        'forge/sparks/state-badge.md': 'dd8b0527f0d457131335d7538ccb5e5a02c524848ad13af5a20ef73e68ed0361',
        'forge/sparks/more-info.md': '6e157b4563e761900f14f0d013f483fbeb0d2b040008c050a1eb806622ad738c',
        'extras/frontend-states-throttling.md': 'bd12e71948743dd03086bd30dddebb223b34ea619548d3ed87d52a85b3d4a00b',
        'forge/sparks/button.md': '3e7eff524e19c14bed60b7c7ab8dfaad080faa638b2e15f1d760be1535d3268b',
        'using/templates.md': '95ffe84883d1b2fd65c4de38551d7c0c5e46da4bf7f5328ee10c20b3b4875ab2',
    }
    if path not in expected_sources:
        return text
    normalized = raw.decode('utf-8').replace('\r\n', '\n')
    assert hashlib.sha256(normalized.encode()).hexdigest() == expected_sources[path], f'Editorial source needs review: {path}'
    if path == 'developers/cards.md':
        old = '    shadow // whether the styles should be based in the #shadow-root of el. Default: true'
        assert text.count(old) == 1
        text = text.replace(old, old.replace('shadow //', 'shadow, //'))
        old = '  )\n}\n```'
        assert text.count(old) == 1
        text = text.replace(old, '  );\n});\n```')
        marker = 'The UIX configuration is an object with the following optional properties:'
        assert text.count(marker) == 1
        text = text.replace(marker, '**Editorial correction (2026-11-20):** The first example adds the missing argument comma and closes the promise callback. The frozen upstream example contains these syntax errors; its original source hashes remain recorded.\n\n' + marker)
    elif path == 'forge/sparks/index.md':
        old = 'insert an interactive `ha-button` element as a sibling after any element within the forged element.'
        assert text.count(old) == 1
        text = text.replace(old, 'insert an interactive `ha-button` element as a sibling before or after a target element within the forged element.')
    elif path == 'concepts/application.md':
        assert text.count('`UIX-card`') == 1
        text = text.replace('`UIX-card`', '`uix-card`')
    elif path == 'using/templates.md':
        old='Templates in the `/config/custom_template` folder'
        assert text.count(old)==1
        text=text.replace(old, 'Templates in the `/config/custom_templates` folder')
        text += ('\nEditorial path correction (2026-11-20): the frozen source tip omitted the final '
                 '`s` in `custom_templates`; the import examples already use the correct plural. '
                 'See [Home Assistant custom templates](https://www.home-assistant.io/docs/templating/custom-templates/).\n')
    elif path == 'extras/frontend-states-throttling.md':
        text += ('\n::: info Editorial clarification (2026-11-20)\n'
                 '`setThrottleOverride(null)` clears the session override and restores server defaults; '
                 'it does not necessarily disable throttling. Use `setThrottleOverride({ enable: false })` '
                 'to disable it for the session even when enabled on the server.\n:::\n')
    elif path in ('forge/sparks/more-info.md', 'forge/sparks/button.md'):
        text += ('\n::: warning Editorial source-code clarification (2026-11-20)\n'
                 'At this frozen revision, target lookup prefers `after` (including the Blank Card default), '
                 'while a nonempty `before` selects insertion before that resolved target. Do not combine '
                 'both selectors or rely on an empty `after` to disable the Blank Card default. '
                 'For predictable Blank Card placement, use explicit `after`. This is a source-code finding, '
                 'not a new browser test. [Frozen implementation](https://github.com/Lint-Free-Technology/uix/blob/'
                 + REVISION + '/src/forge/sparks/uix-spark-'+relative.stem+'.ts).\n:::\n')
        if path.endswith('/button.md'):
            old='If you wish to target `before` using Blank card config, set explicitly to `""`.'
            assert text.count(old)==1
            text=text.replace(old, 'See the editorial placement limitation below.')
            old='Button `appearance` can be one of `accent`, `filled`, `plain`.'
            assert text.count(old)==1
            text=text.replace(old, 'Button `appearance` can be one of `accent`, `filled`, `outlined`, `plain`.')
            text += '\nIcon-only buttons use `neutral` and `plain` defaults, as specified in the configuration table; the general `brand`/`accent` defaults apply to labelled buttons.\n'
    else:
        old = 'If you wish to target `before` using Blank card config, set explicitly to `""`.'
        assert text.count(old) == 1
        text = text.replace(old, 'Blank Card `before` placement has a known limitation at this revision; see the editorial note below.')
        marker = '## Basic usage'
        source_name = 'uix-spark-tile-icon.ts' if path.endswith('/tile-icon.md') else 'uix-spark-state-badge.ts'
        note = ('::: warning Editorial source-code clarification (2026-11-20)\n'
                'At the frozen documented revision, an empty `after` falls back to the default Blank Card target. '
                'It does not disable that fallback, so setting an empty `after` is not a reliable workaround for `before` on Blank Card. '
                'Use explicit `after` placement there. This is a source-code finding, not a new browser runtime test. '
                '[Frozen implementation](https://github.com/Lint-Free-Technology/uix/blob/'+REVISION+'/src/forge/sparks/'+source_name+').\n:::\n\n')
        assert text.count(marker) == 1
        text = text.replace(marker, note+marker)
        if path.endswith('/tile-icon.md'):
            old = 'Exactly one of `after` or `before` must be provided, and exactly one icon source (`icon`, `icon_path`, `image_url`, or `entity`) must be provided.'
            assert text.count(old) == 1
            text = text.replace(old, 'Choose one placement, `after` or `before`, and provide an icon source (`icon`, `icon_path`, `image_url`, or `entity`). An `entity` may additionally use `icon` to override its symbol. The original exactly-one-source statement conflicts with this supported combination.')
            text = text.replace(marker, marker+'\n\nWith `entity`, the native default tap action may toggle or activate a supported entity even without an explicit action. Set `tap_action: {action: none}` when the icon should only display state. This follows the frozen shared tile-icon helper.\n')
        else:
            old = '| `entity` | `string` | ✅ |'
            assert text.count(old) == 1
            text = text.replace(old, '| `entity` | `string` | required for native entity state |')
            text = text.replace(marker, marker+'\n\nFor an entity-state badge, provide `entity`. A fixed `override_icon` or `override_image` can also supply badge content without an entity; the original table incorrectly marked `entity` as mandatory for every case. This clarification follows the frozen implementation.\n')
    return text


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
    notice = '\n> Adapted from the canonical English UIX documentation by [Lint-Free-Technology/uix](https://github.com/Lint-Free-Technology/uix), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source: `'+SOURCE_BRANCH+'` / **'+SOURCE_VERSION+'**, revision ['+REVISION[:7]+'](https://github.com/Lint-Free-Technology/uix/commit/'+REVISION+'), reviewed '+REVIEWED_AT+'. Stable baseline on this site: **9.1.0**. Requires Home Assistant 2026.11.0 or later. Markup adapted for this site; the [original documentation](https://uix.lf.technology/) remains authoritative.\n\n'
    if text.startswith('---\n'):
        end=text.index('\n---',4)+4
        text=text[:end]+'\n'+notice+text[end:].lstrip('\n')
    else:
        text=notice.lstrip('\n')+text
    return '\n'.join(line.rstrip() for line in text.splitlines()).rstrip()+'\n'


def main():
    source=Path(sys.argv[1]).resolve()
    if not (source/'forge/forge.md').is_file():
        raise SystemExit('Expected an archived canonical docs/source directory')
    destination=ROOT/'docs/en/projects/uix'
    record_path=ROOT/'docs/public/projects/uix/canonical-review.json'
    previous=json.loads(record_path.read_text(encoding='utf-8'))
    # Preserve reviewed editorial clarifications only while their canonical source
    # is byte-identical. Upstream changes require a fresh manual review.
    corrections=previous.get('editorial_corrections', {})
    corrected={entry['path']: entry for entry in previous['pages'] if entry['path'] in corrections.get('paths', [])}
    manifest=[]
    source_files={file.relative_to(source).as_posix() for file in source.rglob('*.md')}
    for file in sorted(source.rglob('*.md')):
        relative=file.relative_to(source)
        target=destination/relative
        target.parent.mkdir(parents=True,exist_ok=True)
        raw=file.read_bytes()
        converted=convert(raw.decode('utf-8'),relative,source_files)
        if relative.as_posix() in corrected:
            entry=corrected[relative.as_posix()]
            equivalent_sources={hashlib.sha256(value).hexdigest() for value in
                                (raw, raw.replace(b'\r\n',b'\n'), raw.replace(b'\r\n',b'\n').replace(b'\n',b'\r\n'))}
            existing=target.read_text(encoding='utf-8')
            assert hashlib.sha256(existing.encode()).hexdigest()==entry['english_sha256'], f'Editorial page changed: {relative}'
            if entry['sha256'] in equivalent_sources:
                converted=re.sub(r'(?m)^> Adapted from the canonical English UIX documentation.*$',
                                 lambda _: next(line for line in converted.splitlines() if line.startswith('> Adapted from')), existing)
            else:
                # Manually reviewed timeout update at this frozen revision. Keep
                # the established cache clarification, without discarding new prose.
                assert relative.as_posix() == 'extras/uix-actions.md', f'Editorial correction needs review: {relative}'
                start='## `clear-cache` - clearing Home Assistant Frontend cache\n\n'
                end='\n| config | setting | default | description |'
                old_body=existing.split(start,1)[1].split(end,1)[0]
                converted=re.sub(re.escape(start)+r'.*?(?='+re.escape(end)+r')', lambda _: start+old_body, converted, count=1, flags=re.S)
                corrections['reviewed_at']=REVIEWED_AT
        original_code=code_hashes(raw.decode('utf-8'))
        assert code_hashes(converted)==original_code, f'Code changed before reviewed corrections: {relative}'
        converted=reviewed_corrections(converted,raw,relative)
        adapted_code=code_hashes(converted)
        item={'path':relative.as_posix(),'sha256':hashlib.sha256(raw).hexdigest(),'english_sha256':hashlib.sha256(converted.encode()).hexdigest(),'code_sha256':original_code}
        if relative.as_posix() == 'developers/cards.md':
            assert adapted_code[1:] == original_code[1:] and len(adapted_code) == len(original_code)
            item['english_code_sha256']=adapted_code
            item['code_correction']={'reviewed_at':REVIEWED_AT,'block':1,'reason':'Missing argument comma and promise-callback delimiters repaired; all remaining code blocks unchanged.'}
        else:
            assert adapted_code == original_code, f'Unapproved code change: {relative}'
        target.write_text(converted,encoding='utf-8')
        manifest.append(item)
    # Refresh canonical assets while retaining additional curated media.
    for file in sorted((source/'assets').rglob('*')):
        if file.is_file():
            target=ROOT/'docs/projects/uix/assets'/file.relative_to(source/'assets')
            if not target.exists() or target.read_bytes() != file.read_bytes():
                target.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(file,target)
            # Markdown download links to videos are not bundled like images.
            # Publish their stable URLs used by the canonical adaptations.
            if file.suffix.lower() == '.mp4':
                public_target=ROOT/'docs/public/projects/uix/assets'/file.relative_to(source/'assets')
                public_target.parent.mkdir(parents=True,exist_ok=True)
                if not public_target.exists() or public_target.read_bytes() != file.read_bytes():
                    shutil.copyfile(file,public_target)
    record_path.write_text(json.dumps({'revision':REVISION,'reviewed_at':REVIEWED_AT,'pages':manifest,'editorial_corrections':corrections,'baseline_revision':previous.get('baseline_revision'),'source_branch':SOURCE_BRANCH,'source_version':SOURCE_VERSION},indent=2)+'\n',encoding='utf-8')
    print(f'Adapted {len(manifest)} canonical English pages; source hashes recorded.')


if __name__ == '__main__':
    main()
