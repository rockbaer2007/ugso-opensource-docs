import { defineComponent, h, nextTick, onMounted, onUnmounted, watch } from 'vue'
import { useRoute } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import './custom.css'
import '../blog.css'
import { atlasLocaleTargets } from '../atlas-locales'
import { uixLocaleTargets } from '../uix-locales'
import pageLocales from '../page-locales.json'

declare global {
  interface Window {
    ugsoTrack?: (path?: string) => void
  }
}

const statsScriptUrl = 'https://stats.ugso-software.de/tracker.js'

function trackPage(path: string) {
  window.ugsoTrack?.(path)
}

function loadStatsTracker(getPath: () => string) {
  const existingScript = document.querySelector<HTMLScriptElement>(`script[src="${statsScriptUrl}"]`)

  if (existingScript) {
    if (window.ugsoTrack) {
      trackPage(getPath())
    } else {
      existingScript.addEventListener('load', () => trackPage(getPath()), { once: true })
    }
    return
  }

  const script = document.createElement('script')
  script.src = statsScriptUrl
  script.async = true
  script.onload = () => trackPage(getPath())
  document.head.appendChild(script)
}

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
  const uixTargets = uixLocaleTargets(path)
  const statusTargets = /^\/(?:(?:en|fr)\/)?documentation-status$/.test(normalizePath(path))
    ? { DE: '/documentation-status', EN: '/en/documentation-status', FR: '/fr/documentation-status' }
    : undefined
  const pageTargets = (pageLocales as Record<string, Partial<Record<'DE' | 'EN' | 'FR', string>>>)[normalizePath(path)]
  const targets = uixTargets ?? statusTargets ?? atlasLocaleTargets(path) ?? pageTargets ?? collectionLocaleTargets(path)

  document.querySelectorAll<HTMLAnchorElement>(
    '.VPNavBarTranslations a.link, .VPNavBarExtra .translations a.link, .VPNavScreenTranslations a'
  ).forEach((link) => {
    const code = link.textContent?.trim().match(/^(DE|EN|FR)\b/)?.[1] as 'DE' | 'EN' | 'FR' | undefined
    const target = code ? targets?.[code] : undefined

    if (uixTargets && code === 'EN') {
      link.setAttribute('target', '_blank')
      link.setAttribute('rel', 'noopener noreferrer')
      link.dataset.ugsoUixExternal = 'true'
    } else if (link.dataset.ugsoUixExternal) {
      link.removeAttribute('target')
      link.removeAttribute('rel')
      delete link.dataset.ugsoUixExternal
    }

    if (!targets) return

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
  applyMobileNavSelection(path)
}

function applyMobileNavSelection(path: string) {
  const current = normalizePath(path)
  const matches = (link: HTMLAnchorElement) => {
    const href = link.getAttribute('href') ?? ''
    if (href === 'https://uix.lf.technology/') return /^\/en\/projects\/uix\//.test(current)
    if (!href.startsWith('/')) return false
    const target = normalizePath(href)
    if (['/sammlung/', '/en/collection/', '/fr/collection/'].includes(target)) return current === target
    return current === target || (target.endsWith('/') && !['/', '/en/', '/fr/'].includes(target) && current.startsWith(target))
  }
  document.querySelectorAll<HTMLAnchorElement>('.VPNavScreenMenuLink').forEach(link => {
    const active = matches(link)
    link.dataset.ugsoActive = String(active)
    if (active) link.setAttribute('aria-current', 'page')
    else link.removeAttribute('aria-current')
  })
  document.querySelectorAll<HTMLElement>('.VPNavScreenMenuGroup').forEach(group => {
    group.dataset.ugsoActive = String(Array.from(group.querySelectorAll<HTMLAnchorElement>('a')).some(matches))
  })
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
      document.body.classList.toggle('uix-doc-route', /^\/(?:(?:en|fr)\/)?projects\/uix\//.test(route.path))
      document.body.classList.toggle('ugso-hide-locale-switch', !hasVisibleLocaleSwitch(route.path))
    }

    onMounted(() => {
      updateRouteClass()
      applyLocaleChrome(route.path)
      loadStatsTracker(() => route.path)
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
        trackPage(route.path)
      })
    )

    return () =>
      h(DefaultTheme.Layout, null, {
        'doc-after': () =>
          /^\/(?:(?:en|fr)\/)?projects\/uix\//.test(route.path)
            ? (() => {
                const isFrench = route.path.startsWith('/fr/')
                const isEnglish = route.path.startsWith('/en/')
                return h('div', { class: 'uix-version-footer' }, [
                  h('strong', isEnglish ? 'UIX English source mirror' : isFrench ? 'Traduction française d’UIX' : 'UIX deutsche Übersetzung'),
                  h(
                    'span',
                    isEnglish
                      ? 'Stable baseline: UIX 9.1.0, Home Assistant 2026.11.0 minimum, release ca36726. All 66 canonical pages compared on 23 November 2026 through dev 9528baa: three changed, 63 unchanged. Retry/failed actions and data substitutions describe dev 9.2.0-beta.1, without claiming stable availability. The original English documentation remains authoritative.'
                      : isFrench
                      ? 'Base stable : UIX 9.1.0, Home Assistant 2026.11.0 minimum, révision ca36726. Les 66 pages sont comparées le 23/11/2026 à dev 9528baa : trois modifiées, 63 inchangées. Les actions retry/failed et substitutions décrivent dev 9.2.0-beta.1, sans garantir leur disponibilité dans la version stable. La documentation originale en anglais reste la référence.'
                      : 'Stabile Basis: UIX 9.1.0, benötigt Home Assistant ab 2026.11.0, Release ca36726. Alle 66 Quellseiten am 23.11.2026 bis dev 9528baa verglichen: drei geändert, 63 unverändert. Retry-/Failed-Aktionen und Datenersetzungen beschreiben dev 9.2.0-beta.1, ohne Zusage zur stabilen Verfügbarkeit. Maßgeblich bleibt die englische Originaldokumentation.'
                  ),
                  h('span', [
                    h('a', { href: 'https://uix.lf.technology/', target: '_blank', rel: 'noopener' }, isEnglish ? 'Canonical English documentation' : isFrench ? 'Documentation originale en anglais' : 'Englische Originaldoku'),
                    ' · ',
                    h(
                      'a',
                      {
                        href: 'https://github.com/Lint-Free-Technology/uix/releases/tag/v9.1.0',
                        target: '_blank',
                        rel: 'noopener'
                      },
                      isEnglish ? 'Stable release 9.1.0' : isFrench ? 'Version stable 9.1.0' : 'Stabile Version 9.1.0'
                    ),
                    ' · ',
                    h('a', { href: 'https://github.com/Lint-Free-Technology/uix/commit/ca3672619a11858bbc7f9165db999c0aaa7cef00', target: '_blank', rel: 'noopener' }, isEnglish ? 'Release revision ca36726' : isFrench ? 'Révision publiée ca36726' : 'Release-Revision ca36726'),
                    ' · ',
                    h('a', { href: 'https://github.com/Lint-Free-Technology/uix/commit/9528baaee9cedc2cfb862cda2d6391b8a1fc647c', target: '_blank', rel: 'noopener' }, isEnglish ? 'Canonical docs 9528baa' : isFrench ? 'Sources documentaires 9528baa' : 'Quellabgleich 9528baa'),
                    ' · ',
                    h('a', { href: isEnglish ? '/en/projects/uix/translation-status' : isFrench ? '/fr/projects/uix/translation-status' : '/projects/uix/translation-status' }, isEnglish ? 'Translation status' : isFrench ? 'État de la traduction' : 'Übersetzungsstatus')
                  ]),
                  h('span', [
                    isEnglish ? 'Original UIX documentation by ' : isFrench ? 'Documentation originale d’UIX par ' : 'Originale UIX-Dokumentation von ',
                    h('a', { href: 'https://github.com/Lint-Free-Technology/uix', target: '_blank', rel: 'noopener' }, 'Lint-Free-Technology/uix'),
                    isEnglish ? ', licensed under ' : isFrench ? ', publiée sous licence ' : ', lizenziert unter ',
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
