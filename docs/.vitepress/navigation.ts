import type { DefaultTheme } from 'vitepress/theme'

type Locale = 'de' | 'en' | 'fr'

const labels = {
  de: { apps: 'HA Apps', diverse: 'Diverse', collection: 'Sammlung', overview: 'Übersicht' },
  en: { apps: 'HA Apps', diverse: 'Miscellaneous', collection: 'Collection', overview: 'Overview' },
  fr: { apps: 'Applications HA', diverse: 'Divers', collection: 'Collection', overview: 'Vue d’ensemble' }
}

// Reuse existing destinations and sidebar entries so reorganizing the menu
// does not rename pages or silently drop established navigation links.
export function reorganizeNavigation(
  locale: Locale,
  source: DefaultTheme.NavItem[],
  sidebar: Record<string, DefaultTheme.SidebarItem[]>
): DefaultTheme.NavItem[] {
  const prefix = locale === 'de' ? '' : `/${locale}`
  const text = labels[locale]
  const byText = (name: string) => source.find(item => 'text' in item && item.text === name)!
  const links = (path: string): DefaultTheme.NavItemWithLink[] =>
    (sidebar[path]?.[0]?.items ?? []).filter(item => item.link).map(item => ({ text: item.text!, link: item.link! }))
  const collection = byText(text.collection) as DefaultTheme.NavItemWithChildren
  const blog = byText('Blog') as DefaultTheme.NavItemWithChildren
  const apps = links(`${prefix}/projects-mqtt/`)

  return [
    source[0],
    byText('EEP'),
    { text: text.apps, activeMatch: '^' + prefix + '/(?:projects-mqtt/|projects/(?:dashboard-user-manager|mqtt-client|blocks-for-ha|grafik-visual-studio|callmebot|callmebot-signal|fritzbox-to-mqtt|heizoel-to-mqtt|parcel-to-mqtt)/)', items: apps },
    { text: 'ATLAS', activeMatch: '^' + prefix + '/projects/atlas(?:-plugins)?/', items: [
      { items: links(`${prefix}/projects/atlas/`) },
      { text: 'ATLAS Plugins', items: links(`${prefix}/projects/atlas-plugins/`) }
    ] },
    source.find(item => 'link' in item && item.link.startsWith('https://visualstudio.ugso-software.de/'))!,
    { text: text.diverse, activeMatch: '^' + prefix + '/(?:sammlung|collection|blog)/', items: [
      { text: text.collection, items: collection.items.filter(item => !('link' in item && item.link.includes('uix'))) as DefaultTheme.NavItemWithLink[] },
      { text: 'Blog', items: blog.items as DefaultTheme.NavItemWithLink[] }
    ] },
    locale === 'en'
      ? { text: 'UIX', link: 'https://uix.lf.technology/', target: '_blank', rel: 'noopener noreferrer', activeMatch: '^/en/projects/uix/' }
      : { text: 'UIX', link: `${prefix}/projects/uix/`, activeMatch: '^' + prefix + '/projects/uix/' },
    { text: 'UGSo Software', link: 'https://www.ugso-software.de/' },
    byText('GitHub')
  ]
}
