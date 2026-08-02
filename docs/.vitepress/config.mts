import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'de-DE',
  title: 'UGSo Open Source',
  titleTemplate: ':title | UGSo Open Source',
  description:
    'Open-Source-Projekte von UGSo Software rund um Home Assistant, ESPHome, ATLAS und Lovelace.',

  base: '/',
  cleanUrls: true,
  lastUpdated: true,

  head: [
    ['meta', { name: 'theme-color', content: '#0f172a' }],
    ['meta', { name: 'application-name', content: 'UGSo Open Source' }]
  ],

  themeConfig: {
    logo: 'https://www.ugso-software.de/images/ugso_gross1.png',
    siteTitle: 'UGSo Open Source',

    nav: [
      { text: 'Startseite', link: '/' },
      { text: 'Projekte', link: '/projects/' },
      { text: 'HADash', link: '/projects/hadash/' },
      { text: 'Ultimate Timer', link: '/projects/ultimate-timer/' },
      { text: 'ATLAS', link: '/projects/atlas/' },
      { text: 'UGSo Software', link: 'https://www.ugso-software.de/' },
      { text: 'GitHub', link: 'https://github.com/rockbaer2007' }
    ],

    sidebar: {
      '/projects/hadash/': [
        {
          text: 'HADash',
          collapsed: false,
          items: [
            { text: 'Übersicht', link: '/projects/hadash/' },
            { text: 'Erste Schritte', link: '/projects/hadash/erste-schritte' },
            { text: 'Dashboard einlesen', link: '/projects/hadash/dashboard-einlesen' },
            { text: 'Ansicht exportieren', link: '/projects/hadash/ansicht-exportieren' },
            { text: 'Backups und JSON', link: '/projects/hadash/backups-und-json' },
            { text: 'Portable Nutzung', link: '/projects/hadash/portable-nutzung' }
          ]
        }
      ],

      '/projects/ultimate-timer/': [
        {
          text: 'Ultimate Timer',
          collapsed: false,
          items: [
            { text: 'Übersicht', link: '/projects/ultimate-timer/' },
            { text: 'Installation', link: '/projects/ultimate-timer/installation' },
            { text: 'Konfiguration', link: '/projects/ultimate-timer/konfiguration' },
            { text: 'Funktionsweise', link: '/projects/ultimate-timer/funktionsweise' },
            { text: 'Beispiele', link: '/projects/ultimate-timer/beispiele' }
          ]
        }
      ],

      '/projects/atlas/': [
        {
          text: 'ATLAS',
          collapsed: false,
          items: [
            { text: 'Übersicht', link: '/projects/atlas/' },
            { text: 'Architektur', link: '/projects/atlas/uebersicht' },
            { text: 'Entwicklungsstand', link: '/projects/atlas/entwicklungsstand' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/rockbaer2007' }
    ],

    search: {
      provider: 'local'
    },

    footer: {
      message:
        '<a href="https://www.ugso-software.de/index.php/impressum" target="_blank" rel="noopener">Impressum</a>',
      copyright: '© 2026 UGSo Software'
    },

    outline: {
      label: 'Auf dieser Seite'
    },

    lastUpdated: {
      text: 'Zuletzt aktualisiert'
    },

    docFooter: {
      prev: 'Vorherige Seite',
      next: 'Nächste Seite'
    }
  }
})
