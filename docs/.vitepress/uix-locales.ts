// UIX translations stay local; English opens the canonical documentation separately.
export function uixLocaleTargets(path: string): Record<'DE' | 'EN' | 'FR', string> | undefined {
  const clean = path.split(/[?#]/, 1)[0].replace(/\.html$/, '').replace(/\/index$/, '/')
  const match = clean.match(/^\/(?:en\/|fr\/)?projects\/uix(?:\/(.*))?$/)
  if (!match) return undefined
  const suffix = match[1] ?? ''
  const canonical = suffix === 'translation-status' ? ''
    : suffix.replace(/^extras\/style-custom-panels\/?$/, 'extras/style-frame-panels')
  return {
    DE: '/projects/uix/' + suffix,
    EN: 'https://uix.lf.technology/' + canonical + (canonical && !canonical.endsWith('/') ? '/' : ''),
    FR: '/fr/projects/uix/' + suffix
  }
}
