import type { DefaultTheme } from 'vitepress/theme'

type Locale = 'de' | 'en' | 'fr'

const labels = {
  de: { apps: 'Apps', cards: 'Cards', integrations: 'Integrationen', diverse: 'Diverse', collection: 'Sammlung', overview: 'Übersicht', archived: 'archiviert' },
  en: { apps: 'Apps', cards: 'Cards', integrations: 'Integrations', diverse: 'Miscellaneous', collection: 'Collection', overview: 'Overview', archived: 'archived' },
  fr: { apps: 'Applications', cards: 'Cartes', integrations: 'Intégrations', diverse: 'Divers', collection: 'Collection', overview: 'Vue d’ensemble', archived: 'archivé' }
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
  const collectionRoot = `${prefix}/${locale === 'de' ? 'sammlung' : 'collection'}/`
  const page = (name: string, slug: string): DefaultTheme.NavItemWithLink => ({ text: name, link: collectionRoot + slug })
  const overview = (slug: string) => page(text.overview, slug)
  const project = (slug: string) => apps.find(item => item.link === `${prefix}/projects/${slug}/`)!
  const collectionLink = (slug: string) => collection.items.find(item => 'link' in item && item.link === collectionRoot + slug) as DefaultTheme.NavItemWithLink
  const haItems = [
    { text: 'Dashboards', items: [
      overview('ha-dashboard'), project('sidebar-manager'), project('sidebar-colors'),
      page('Dashboard Layout Card V2', 'dashboard-layout-card-v2/'),
      page('Frosted Glass Theme', 'frosted-glass-theme/'), page('NeoMorphix UIX', 'neomorphix-uix/')
    ] },
    { text: text.apps, items: [
      overview('ha-apps'),
      ...apps.filter(item => item.link !== `${prefix}/projects-mqtt/` && !['sidebar-manager', 'sidebar-colors', 'automation-status-card', 'parcel-to-mqtt'].some(slug => item.link === `${prefix}/projects/${slug}/`)),
      { text: 'UGSo HA Apps', link: `${prefix}/projects-mqtt/` },
      { ...project('parcel-to-mqtt'), text: `${project('parcel-to-mqtt').text} (${text.archived})` },
      collectionLink('ha-tools'), collectionLink('ha-blueprints')
    ] },
    { text: text.integrations, items: [
      overview(locale === 'de' ? 'ha-integrationen' : 'ha-integrations'),
      page('Zendure Home Assistant Integration', 'zendure-ha/'),
      page('Frosted Glass Theme Manager', 'frosted-glass-manager/'),
      collectionLink(locale === 'de' ? 'ha-empfehlungen' : 'ha-recommendations'),
      collectionLink(locale === 'de' ? 'hacs-dokus' : 'hacs-docs')
    ] },
    { text: text.cards, items: [
      overview('ha-cards'), project('automation-status-card'),
      page('Calendar Card Pro', 'calendar-card-pro/'), page('Mushroom Cards', 'mushroom/'),
      page('flex-table-card', 'flex-table-card/'),
      { text: 'Bubble Card', link: 'https://github.com/Clooos/Bubble-Card' }
    ] }
  ]

  return [
    source[0],
    byText('EEP'),
    { text: 'Home Assistant', activeMatch: '^' + prefix + '/(?:projects-mqtt/|(?:sammlung|collection)/(?:ha-|hacs-|dashboard-layout|frosted-|neomorphix-|zendure-|calendar-card|mushroom|flex-table)|projects/(?:automation-status-card|sidebar-manager|sidebar-colors|dashboard-user-manager|mqtt-client|blocks-for-ha|grafik-visual-studio|callmebot|callmebot-signal|fritzbox-to-mqtt|heizoel-to-mqtt|parcel-to-mqtt|hadash)/)', items: haItems },
    { text: 'ATLAS', activeMatch: '^' + prefix + '/projects/atlas(?:-plugins)?/', items: [
      { items: links(`${prefix}/projects/atlas/`) },
      { text: 'ATLAS Plugins', items: links(`${prefix}/projects/atlas-plugins/`) }
    ] },
    { text: 'ioBroker', activeMatch: '^' + prefix + '/iobroker/', items: [
      { text: 'Widgets', items: [
        { text: 'UGSo Special', link: `${prefix}/iobroker/widgets/ugso-spezial/` }
      ] },
      { text: { de: 'Veröffentlichungsassistent', en: 'Publishing Assistant', fr: 'Assistant de publication' }[locale], link: `${prefix}/iobroker/publish-assistant/` }
    ] },
    source.find(item => 'link' in item && item.link.startsWith('https://visualstudio.ugso-software.de/'))!,
    { text: text.diverse, activeMatch: '^' + prefix + '/(?:(?:sammlung|collection)/(?:$|weitere-beispiele|interesting-examples)|blog/)', items: [
      { text: text.collection, items: [overview(''), collectionLink(locale === 'de' ? 'weitere-beispiele' : 'interesting-examples')] },
      { text: 'Blog', items: blog.items as DefaultTheme.NavItemWithLink[] }
    ] },
    locale === 'en'
      ? { text: 'UIX', link: 'https://uix.lf.technology/', target: '_blank', rel: 'noopener noreferrer', activeMatch: '^/en/projects/uix/' }
      : { text: 'UIX', link: `${prefix}/projects/uix/`, activeMatch: '^' + prefix + '/projects/uix/' },
    { text: 'UGSo Software', link: 'https://www.ugso-software.de/' },
    byText('GitHub')
  ]
}
