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

  if (!normalizedPath.startsWith('/sammlung/')) {
    return true
  }

  return translatedCollectionRoutes.has(normalizedPath)
}

const localeRouteTargets: Record<string, Partial<Record<'DE' | 'EN' | 'FR', string>>> = {
  '/sammlung/dashboard-layout-card-v2/': {
    EN: '/en/collection/dashboard-layout-card-v2/',
    FR: '/fr/collection/dashboard-layout-card-v2/'
  },
  '/en/collection/dashboard-layout-card-v2/': {
    DE: '/sammlung/dashboard-layout-card-v2/',
    FR: '/fr/collection/dashboard-layout-card-v2/'
  },
  '/fr/collection/dashboard-layout-card-v2/': {
    DE: '/sammlung/dashboard-layout-card-v2/',
    EN: '/en/collection/dashboard-layout-card-v2/'
  }
}

function applyLocaleLinks(path: string) {
  const targets = localeRouteTargets[normalizePath(path)]

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
      document.body.classList.toggle('uix-doc-route', route.path.startsWith('/projects/uix/'))
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
          route.path.startsWith('/projects/uix/')
            ? h('div', { class: 'uix-version-footer' }, [
                h('strong', 'UIX deutsche Übersetzung'),
                h(
                  'span',
                  'Stabile Basis: UIX 8.2.0. Gekennzeichnete Ergänzungen bis 8.3.0-beta.8, geprüft am 13.09.2026. Maßgeblich bleibt die englische Originaldokumentation.'
                ),
                h('span', [
                  h('a', { href: 'https://uix.lf.technology/', target: '_blank', rel: 'noopener' }, 'Englische Originaldoku'),
                  ' · ',
                  h(
                    'a',
                    {
                      href: 'https://github.com/Lint-Free-Technology/uix/commit/f9eb8fa571dbce6cd771c53ca11dcf2401c8a933',
                      target: '_blank',
                      rel: 'noopener'
                    },
                    'Stabile Basis f9eb8fa'
                  ),
                  ' · ',
                  h('a', { href: '/projects/uix/translation-status' }, 'Abgleich c33ff79')
                ]),
                h('span', [
                  'Originale UIX-Dokumentation von ',
                  h('a', { href: 'https://github.com/Lint-Free-Technology/uix', target: '_blank', rel: 'noopener' }, 'Lint-Free-Technology/uix'),
                  ', lizenziert unter ',
                  h('a', { href: 'https://creativecommons.org/licenses/by/4.0/', target: '_blank', rel: 'noopener' }, 'CC BY 4.0'),
                  '.'
                ])
              ])
            : null
      })
  }
})

export default {
  extends: DefaultTheme,
  Layout: UgsoLayout
} satisfies Theme
