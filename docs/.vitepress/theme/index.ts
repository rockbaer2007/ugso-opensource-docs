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
      applyLocaleFlags()
      observer = new MutationObserver(() => applyLocaleFlags())
      observer.observe(document.body, { childList: true, subtree: true })
    })

    onUnmounted(() => {
      observer?.disconnect()
    })

    watch(
      () => route.path,
      () => nextTick(() => {
        updateRouteClass()
        applyLocaleFlags()
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
                  'Diese Seite basiert auf UIX 8.1.0 und enthält zusätzlich gekennzeichnete Inhalte aus UIX 8.2.0-beta.4. Maßgeblich bleibt die englische Originaldokumentation.'
                ),
                h('span', [
                  h('a', { href: 'https://uix.lf.technology/', target: '_blank', rel: 'noopener' }, 'Englische Originaldoku'),
                  ' · ',
                  h(
                    'a',
                    {
                      href: 'https://github.com/Lint-Free-Technology/uix/commit/9a0fa57d4afd262a5eaec4f1bfb7c154667bb2c9',
                      target: '_blank',
                      rel: 'noopener'
                    },
                    'Source-Revision 9a0fa57'
                  ),
                  ' · ',
                  h(
                    'a',
                    {
                      href: 'https://github.com/Lint-Free-Technology/uix/commit/3e9b1d4',
                      target: '_blank',
                      rel: 'noopener'
                    },
                    'Beta-Revision 3e9b1d4'
                  )
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
