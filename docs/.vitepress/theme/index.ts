import { defineComponent, h, nextTick, onMounted, onUnmounted, watch } from 'vue'
import { useRoute } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import './custom.css'
import '../blog.css'

const localeFlags: Record<string, string> = {
  DE: '/images/flags/deutschland.png',
  EN: '/images/flags/englische-sprache.png',
  FR: '/images/flags/frankreich.png'
}

const localeSelector = [
  '.VPNavBarTranslations .title',
  '.VPNavBarTranslations .link span',
  '.VPNavBarExtra .translations .trans-title',
  '.VPNavBarExtra .translations .link span'
].join(',')

const translatedCollectionRoutes = new Set([
  '/sammlung/',
  '/sammlung/ha-cards',
  '/sammlung/ha-dashboard',
  '/sammlung/dashboard-layout-card-v2/',
  '/sammlung/ha-integrationen',
  '/sammlung/ha-blueprints',
  '/sammlung/ha-tools',
  '/sammlung/ha-apps',
  '/sammlung/hacs-dokus',
  '/sammlung/weitere-beispiele',
  '/sammlung/calendar-card-pro/',
  '/sammlung/flex-table-card/',
  '/sammlung/mushroom/',
  '/sammlung/zendure-ha/'
])

function normalizePath(path: string) {
  return path.replace(/\.html$/, '').replace(/\/index$/, '/')
}

function hasVisibleLocaleSwitch(path: string) {
  const normalizedPath = normalizePath(path)

  if (normalizedPath.startsWith('/sammlung/')) {
    return true
  }

  return true
}

const collectionPathMap: Record<string, string> = {
  'ha-empfehlungen': 'ha-recommendations',
  'ha-integrationen': 'ha-integrations',
  'hacs-dokus': 'hacs-docs',
  'weitere-beispiele': 'interesting-examples'
}

const reverseCollectionPathMap = Object.fromEntries(
  Object.entries(collectionPathMap).map(([dePath, enPath]) => [enPath, dePath])
)

function trimSlashes(path: string) {
  return path.replace(/^\/+|\/+$/g, '')
}

function mapCollectionPath(path: string, map: Record<string, string>) {
  const cleanPath = trimSlashes(path)
  if (!cleanPath) return ''
  const parts = cleanPath.split('/')
  parts[0] = map[parts[0]] ?? parts[0]
  return parts.join('/')
}

function withTrailingSlashForIndex(path: string, suffix: string) {
  return suffix ? `${path}/${suffix}` : `${path}/`
}

function collectionLocaleTargets(path: string): Partial<Record<'DE' | 'EN' | 'FR', string>> | undefined {
  const normalizedPath = normalizePath(path)

  if (normalizedPath.startsWith('/sammlung/')) {
    const sourcePath = trimSlashes(normalizedPath.slice('/sammlung/'.length))
    const translatedPath = mapCollectionPath(sourcePath, collectionPathMap)
    return {
      EN: withTrailingSlashForIndex('/en/collection', translatedPath),
      FR: withTrailingSlashForIndex('/fr/collection', translatedPath)
    }
  }

  if (normalizedPath.startsWith('/en/collection/')) {
    const sourcePath = trimSlashes(normalizedPath.slice('/en/collection/'.length))
    const germanPath = mapCollectionPath(sourcePath, reverseCollectionPathMap)
    return {
      DE: withTrailingSlashForIndex('/sammlung', germanPath),
      FR: withTrailingSlashForIndex('/fr/collection', sourcePath)
    }
  }

  if (normalizedPath.startsWith('/fr/collection/')) {
    const sourcePath = trimSlashes(normalizedPath.slice('/fr/collection/'.length))
    const germanPath = mapCollectionPath(sourcePath, reverseCollectionPathMap)
    return {
      DE: withTrailingSlashForIndex('/sammlung', germanPath),
      EN: withTrailingSlashForIndex('/en/collection', sourcePath)
    }
  }

  return undefined
}

function applyLocaleLinks(path: string) {
  const targets = collectionLocaleTargets(path)

  if (!targets) {
    return
  }

  document.querySelectorAll<HTMLAnchorElement>(
    '.VPNavBarTranslations a.link, .VPNavBarExtra .translations a.link'
  ).forEach((link) => {
    const code = link.textContent?.trim().match(/^(DE|EN|FR)\b/)?.[1] as 'DE' | 'EN' | 'FR' | undefined
    const target = code ? targets[code] : undefined

    if (target) {
      link.hidden = false
      link.style.display = ''
      link.setAttribute('href', target)
    } else if (code === 'FR') {
      link.hidden = true
      link.style.display = 'none'
    }
  })
}

function applyLocaleChrome(path: string) {
  applyLocaleFlags()
  applyLocaleLinks(path)
}

function applyLocaleFlags() {
  document.querySelectorAll<HTMLElement>(localeSelector).forEach((label) => {
    const code = label.textContent?.trim().match(/^(DE|EN|FR)\b/)?.[1]

    if (!code) {
      return
    }

    const textNode = Array.from(label.childNodes).find((node) => node.nodeType === Node.TEXT_NODE)
    const existingFlag = label.querySelector<HTMLImageElement>('.ugso-locale-flag')
    const expectedFlag = localeFlags[code]

    if (textNode?.textContent === code && existingFlag?.getAttribute('src') === expectedFlag) {
      return
    }

    const flag = document.createElement('img')
    flag.className = 'ugso-locale-flag'
    flag.src = expectedFlag
    flag.alt = `${code} flag`
    flag.loading = 'lazy'

    label.classList.add('ugso-locale-label')
    label.replaceChildren(document.createTextNode(code), flag)
  })
}

const UgsoLayout = defineComponent({
  name: 'UgsoLayout',
  setup() {
    const route = useRoute()
    let observer: MutationObserver | undefined

    const updateRouteClass = () => {
      document.body.classList.toggle('uix-doc-route', /^\/(?:fr\/)?projects\/uix\//.test(route.path))
      document.body.classList.toggle('ugso-hide-locale-switch', !hasVisibleLocaleSwitch(route.path))
    }

    onMounted(() => {
      updateRouteClass()
      applyLocaleChrome(route.path)
      observer = new MutationObserver(() => applyLocaleChrome(route.path))
      observer.observe(document.body, { childList: true, subtree: true })
    })

    onUnmounted(() => {
      observer?.disconnect()
    })

    watch(
      () => route.path,
      () => nextTick(() => {
        updateRouteClass()
        applyLocaleChrome(route.path)
      })
    )

    return () =>
      h(DefaultTheme.Layout, null, {
        'doc-after': () =>
          /^\/(?:fr\/)?projects\/uix\//.test(route.path)
            ? (() => {
                const isFrench = route.path.startsWith('/fr/')
                return h('div', { class: 'uix-version-footer' }, [
                  h('strong', isFrench ? 'Traduction française d’UIX' : 'UIX deutsche Übersetzung'),
                  h(
                    'span',
                    isFrench
                      ? 'Base stable : UIX 8.2.0. Compléments signalés jusqu’à 8.3.0-beta.8, vérifiés le 13/09/2026. La documentation originale en anglais reste la référence.'
                      : 'Stabile Basis: UIX 8.2.0. Gekennzeichnete Ergänzungen bis 8.3.0-beta.8, geprüft am 13.09.2026. Maßgeblich bleibt die englische Originaldokumentation.'
                  ),
                  h('span', [
                    h('a', { href: 'https://uix.lf.technology/', target: '_blank', rel: 'noopener' }, isFrench ? 'Documentation originale en anglais' : 'Englische Originaldoku'),
                    ' · ',
                    h(
                      'a',
                      {
                        href: 'https://github.com/Lint-Free-Technology/uix/commit/f9eb8fa571dbce6cd771c53ca11dcf2401c8a933',
                        target: '_blank',
                        rel: 'noopener'
                      },
                      isFrench ? 'Base stable f9eb8fa' : 'Stabile Basis f9eb8fa'
                    ),
                    ' · ',
                    h('a', { href: isFrench ? '/fr/projects/uix/translation-status' : '/projects/uix/translation-status' }, isFrench ? 'Comparaison c33ff79' : 'Abgleich c33ff79')
                  ]),
                  h('span', [
                    isFrench ? 'Documentation originale d’UIX par ' : 'Originale UIX-Dokumentation von ',
                    h('a', { href: 'https://github.com/Lint-Free-Technology/uix', target: '_blank', rel: 'noopener' }, 'Lint-Free-Technology/uix'),
                    isFrench ? ', publiée sous licence ' : ', lizenziert unter ',
                    h('a', { href: 'https://creativecommons.org/licenses/by/4.0/', target: '_blank', rel: 'noopener' }, 'CC BY 4.0'),
                    '.'
                  ])
                ])
              })()
            : null
      })
  }
})

export default {
  extends: DefaultTheme,
  Layout: UgsoLayout
} satisfies Theme
