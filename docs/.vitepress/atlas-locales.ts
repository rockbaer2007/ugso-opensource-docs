// Keep established German slugs while navigating to the corresponding EN/FR page.
const germanSlugs: Record<string, string> = {
  'atlas/overview': 'atlas/uebersicht',
  'atlas/development-status': 'atlas/entwicklungsstand',
  'atlas-plugins/verified-plugins': 'atlas-plugins/gepruefte-plugins'
}
const translatedSlugs = Object.fromEntries(
  Object.entries(germanSlugs).map(([translated, german]) => [german, translated])
)

export function atlasLocaleTargets(path: string): Record<'DE' | 'EN' | 'FR', string> | undefined {
  const clean = path.split(/[?#]/, 1)[0].replace(/\.html$/, '').replace(/\/index$/, '/')
  const match = clean.match(/^\/(?:en\/|fr\/)?projects\/(atlas(?:-plugins)?)(?:\/(.*))?$/)
  if (!match) return undefined
  const suffix = match[2] ?? ''
  const key = translatedSlugs[match[1] + '/' + suffix] ?? match[1] + '/' + suffix
  return {
    DE: '/projects/' + (germanSlugs[key] ?? key),
    EN: '/en/projects/' + key,
    FR: '/fr/projects/' + key
  }
}
