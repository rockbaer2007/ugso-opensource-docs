import { defineConfig } from 'vitepress'

const navDe = [
  { text: 'Startseite', link: '/' },
  { text: 'C# Projekte', link: '/projects/' },
  { text: 'MQTT Projekte', link: '/projects-mqtt/' },
  { text: 'Diverse Projekte', link: '/projects-diverse/' },
  { text: 'UIX Doku', link: '/projects/uix/' },
  {
    text: 'Blog',
    items: [
      { text: 'Blog-Übersicht', link: '/blog/' },
      { text: 'Code-Snippets', link: '/blog/snippets/' },
      { text: 'Blockly / JavaScript (ioBroker)', link: '/blog/snippets/iobroker-blockly' },
      { text: 'Neuer Beitrag', link: '/blog/beitragsvorlage' }
    ]
  },
  { text: 'ATLAS', link: '/projects/atlas/' },
  { text: 'UGSo Software', link: 'https://www.ugso-software.de/' },
  { text: 'GitHub', link: 'https://github.com/rockbaer2007' }
]

const navEn = [
  { text: 'Home', link: '/en/' },
  { text: 'C# Projects', link: '/en/projects/' },
  { text: 'MQTT Projects', link: '/en/projects-mqtt/' },
  { text: 'Misc Projects', link: '/en/projects-diverse/' },
  { text: 'UIX Docs', link: 'https://uix.lf.technology/' },
  {
    text: 'Blog',
    items: [
      { text: 'Blog Overview', link: '/en/blog/' },
      { text: 'Code Snippets', link: '/en/blog/snippets/' },
      { text: 'Blockly / JavaScript (ioBroker)', link: '/en/blog/snippets/iobroker-blockly' },
      { text: 'New Post Template', link: '/en/blog/post-template' }
    ]
  },
  { text: 'ATLAS', link: '/en/projects/atlas/' },
  { text: 'UGSo Software', link: 'https://www.ugso-software.de/' },
  { text: 'GitHub', link: 'https://github.com/rockbaer2007' }
]

const sidebarDe = {
  '/projects-diverse/': [
    {
      text: 'Diverse Projekte',
      collapsed: false,
      items: [
        { text: 'Übersicht', link: '/projects-diverse/' },
        { text: 'Ultimate Timer', link: '/projects/ultimate-timer/' }
      ]
    }
  ],

  '/projects-mqtt/': [
    {
      text: 'MQTT Projekte',
      collapsed: false,
      items: [
        { text: 'Übersicht', link: '/projects-mqtt/' },
        { text: 'FRITZ!Box to MQTT', link: '/projects/fritzbox-to-mqtt/' },
        { text: 'Heizöl to MQTT', link: '/projects/heizoel-to-mqtt/' },
        { text: 'Parcel to MQTT', link: '/projects/parcel-to-mqtt/' }
      ]
    }
  ],

  '/blog/': [
    {
      text: 'Blog',
      collapsed: false,
      items: [
        { text: 'Übersicht', link: '/blog/' },
        { text: 'Code-Snippets', link: '/blog/snippets/' },
        { text: 'Beitragsvorlage', link: '/blog/beitragsvorlage' }
      ]
    },
    {
      text: 'Beiträge',
      collapsed: false,
      items: [
        { text: 'HADash v0.9.4 Preview', link: '/blog/posts/hadash-preview' },
        { text: 'ATLAS Runtime Foundation', link: '/blog/posts/atlas-runtime-foundation' }
      ]
    },
    {
      text: 'Code-Beispiele',
      collapsed: false,
      items: [
        { text: 'Home Assistant YAML', link: '/blog/snippets/home-assistant-yaml' },
        { text: 'JavaScript', link: '/blog/snippets/javascript' },
        { text: 'Blockly / JavaScript (ioBroker)', link: '/blog/snippets/iobroker-blockly' },
        { text: 'Lovelace & Bubble-Card', link: '/blog/snippets/lovelace' }
      ]
    }
  ],

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

  '/projects/fritzbox-to-mqtt/': [
    {
      text: 'FRITZ!Box to MQTT',
      collapsed: false,
      items: [
        { text: 'Übersicht', link: '/projects/fritzbox-to-mqtt/' },
        { text: 'Installation', link: '/projects/fritzbox-to-mqtt/installation' },
        { text: 'Konfiguration', link: '/projects/fritzbox-to-mqtt/konfiguration' },
        { text: 'Entitäten', link: '/projects/fritzbox-to-mqtt/entitaeten' },
        { text: 'Fehlersuche', link: '/projects/fritzbox-to-mqtt/fehlersuche' }
      ]
    }
  ],

  '/projects/heizoel-to-mqtt/': [
    {
      text: 'Heizöl to MQTT',
      collapsed: false,
      items: [
        { text: 'Übersicht', link: '/projects/heizoel-to-mqtt/' },
        { text: 'Installation', link: '/projects/heizoel-to-mqtt/installation' },
        { text: 'Konfiguration', link: '/projects/heizoel-to-mqtt/konfiguration' },
        { text: 'Entitäten', link: '/projects/heizoel-to-mqtt/entitaeten' }
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
        { text: 'Entwicklungsstand', link: '/projects/atlas/entwicklungsstand' },
        { text: 'Home Assistant', link: '/projects/atlas/homeassistant' },
        { text: 'Plugin-Doku', link: '/projects/atlas/plugins' }
      ]
    }
  ],

  '/projects/uix/': [
    {
      text: 'UIX Deutsch',
      collapsed: false,
      items: [
        { text: 'Übersicht', link: '/projects/uix/' },
        { text: 'Schnellstart', link: '/projects/uix/quick-start' },
        { text: 'FAQ', link: '/projects/uix/faq' },
        { text: 'Übersetzungsstatus', link: '/projects/uix/translation-status' },
        { text: 'Mitwirken', link: '/projects/uix/contributing' }
      ]
    },
    {
      text: 'UIX Styling',
      collapsed: false,
      items: [
        { text: 'Übersicht', link: '/projects/uix/using/' },
        { text: 'Karten', link: '/projects/uix/using/cards' },
        { text: 'Entitäten', link: '/projects/uix/using/entities' },
        { text: 'Icons', link: '/projects/uix/using/icons' },
        { text: 'Bilder', link: '/projects/uix/using/images' },
        { text: 'Abschnitte', link: '/projects/uix/using/section-backgrounds' },
        { text: 'Ansichten', link: '/projects/uix/using/view-backgrounds' },
        { text: 'Custom Panels', link: '/projects/uix/using/custom-panels' },
        { text: 'Templates', link: '/projects/uix/using/templates' },
        { text: 'Themes', link: '/projects/uix/using/themes' },
        { text: 'Weitere Optionen', link: '/projects/uix/using/other' }
      ]
    },
    {
      text: 'UIX Broker',
      collapsed: true,
      items: [
        { text: 'Übersicht', link: '/projects/uix/broker/' },
        { text: 'Broker', link: '/projects/uix/broker/broker' },
        { text: 'Realms', link: '/projects/uix/broker/realms' },
        { text: 'Interaction Anchors', link: '/projects/uix/broker/interaction-anchors' },
        { text: 'Rules', link: '/projects/uix/broker/rules' },
        { text: 'Directives', link: '/projects/uix/broker/directives' },
        { text: 'Examples', link: '/projects/uix/broker/examples' }
      ]
    },
    {
      text: 'UIX Forge',
      collapsed: false,
      items: [
        { text: 'Übersicht', link: '/projects/uix/forge/' },
        { text: 'Forge-Referenz', link: '/projects/uix/forge/forge' },
        { text: 'Foundries', link: '/projects/uix/forge/foundries' },
        { text: 'Sparks', link: '/projects/uix/forge/sparks/' },
        { text: 'Tooltip', link: '/projects/uix/forge/sparks/tooltip' },
        { text: 'Button', link: '/projects/uix/forge/sparks/button' },
        { text: 'Attribute', link: '/projects/uix/forge/sparks/attribute' },
        { text: 'Event', link: '/projects/uix/forge/sparks/event' },
        { text: 'Grid', link: '/projects/uix/forge/sparks/grid' },
        { text: 'Map', link: '/projects/uix/forge/sparks/map' },
        { text: 'Lock', link: '/projects/uix/forge/sparks/lock' },
        { text: 'More-info', link: '/projects/uix/forge/sparks/more-info' },
        { text: 'Overlay Icon', link: '/projects/uix/forge/sparks/overlay-icon' },
        { text: 'Background', link: '/projects/uix/forge/sparks/background' },
        { text: 'Theme', link: '/projects/uix/forge/sparks/theme' },
        { text: 'Tile Icon', link: '/projects/uix/forge/sparks/tile-icon' },
        { text: 'State Badge', link: '/projects/uix/forge/sparks/state-badge' },
        { text: 'Search', link: '/projects/uix/forge/sparks/search' }
      ]
    },
    {
      text: 'Konzepte & Hilfe',
      collapsed: false,
      items: [
        { text: 'Konzepte', link: '/projects/uix/concepts/' },
        { text: 'DOM-Konzept', link: '/projects/uix/concepts/dom' },
        { text: 'Anwendung', link: '/projects/uix/concepts/application' },
        { text: 'Debugging', link: '/projects/uix/debugging/' },
        { text: 'Karten debuggen', link: '/projects/uix/debugging/cards' },
        { text: 'Templates debuggen', link: '/projects/uix/debugging/templates' },
        { text: 'Cache-Probleme', link: '/projects/uix/debugging/cache' }
      ]
    },
    {
      text: 'Extras & Entwickler',
      collapsed: true,
      items: [
        { text: 'Extras', link: '/projects/uix/extras/' },
        { text: 'UIX Actions', link: '/projects/uix/extras/uix-actions' },
        { text: 'Frontend State Throttling', link: '/projects/uix/extras/frontend-states-throttling' },
        { text: 'Dialog Styling Delay', link: '/projects/uix/extras/dialog-styling-delay' },
        { text: 'Hash-Template-Variablen', link: '/projects/uix/extras/hash-template-variable-updates' },
        { text: 'Icon-Styling deaktivieren', link: '/projects/uix/extras/disable-icon-styling' },
        { text: 'Entity-Picture-Override', link: '/projects/uix/extras/disable-entity-picture-image-override' },
        { text: 'Always patch ha-card', link: '/projects/uix/extras/always-patch-ha-card' },
        { text: 'Custom Panels im iframe', link: '/projects/uix/extras/style-custom-panels' },
        { text: 'Entwickler', link: '/projects/uix/developers/' },
        { text: 'Karten entwickeln', link: '/projects/uix/developers/cards' },
        { text: 'Themes entwickeln', link: '/projects/uix/developers/themes' }
      ]
    }
  ],

  '/projects/': [
    {
      text: 'C# Projekte',
      collapsed: false,
      items: [
        { text: 'Übersicht', link: '/projects/' },
        { text: 'HADash', link: '/projects/hadash/' },
        { text: 'Home Assistant Automation Exporter', link: '/projects/#home-assistant-automation-exporter' }
      ]
    }
  ]
}

const sidebarEn = {
  '/en/projects-diverse/': [
    {
      text: 'Misc Projects',
      collapsed: false,
      items: [
        { text: 'Overview', link: '/en/projects-diverse/' },
        { text: 'Ultimate Timer', link: '/en/projects/ultimate-timer/' }
      ]
    }
  ],

  '/en/projects-mqtt/': [
    {
      text: 'MQTT Projects',
      collapsed: false,
      items: [
        { text: 'Overview', link: '/en/projects-mqtt/' },
        { text: 'FRITZ!Box to MQTT', link: '/en/projects/fritzbox-to-mqtt/' },
        { text: 'Heizöl to MQTT', link: '/en/projects/heizoel-to-mqtt/' },
        { text: 'Parcel to MQTT', link: '/en/projects/parcel-to-mqtt/' }
      ]
    }
  ],

  '/en/blog/': [
    {
      text: 'Blog',
      collapsed: false,
      items: [
        { text: 'Overview', link: '/en/blog/' },
        { text: 'Code Snippets', link: '/en/blog/snippets/' },
        { text: 'Post Template', link: '/en/blog/post-template' }
      ]
    },
    {
      text: 'Posts',
      collapsed: false,
      items: [
        { text: 'HADash v0.9.4 Preview', link: '/en/blog/posts/hadash-preview' },
        { text: 'ATLAS Runtime Foundation', link: '/en/blog/posts/atlas-runtime-foundation' }
      ]
    },
    {
      text: 'Code Examples',
      collapsed: false,
      items: [
        { text: 'Home Assistant YAML', link: '/en/blog/snippets/home-assistant-yaml' },
        { text: 'JavaScript', link: '/en/blog/snippets/javascript' },
        { text: 'Blockly / JavaScript (ioBroker)', link: '/en/blog/snippets/iobroker-blockly' },
        { text: 'Lovelace & Bubble Card', link: '/en/blog/snippets/lovelace' }
      ]
    }
  ],

  '/en/projects/hadash/': [
    {
      text: 'HADash',
      collapsed: false,
      items: [
        { text: 'Overview', link: '/en/projects/hadash/' },
        { text: 'Getting Started', link: '/en/projects/hadash/getting-started' },
        { text: 'Import Dashboard', link: '/en/projects/hadash/import-dashboard' },
        { text: 'Export View', link: '/en/projects/hadash/export-view' },
        { text: 'Backups and JSON', link: '/en/projects/hadash/backups-and-json' },
        { text: 'Portable Usage', link: '/en/projects/hadash/portable-usage' }
      ]
    }
  ],

  '/en/projects/ultimate-timer/': [
    {
      text: 'Ultimate Timer',
      collapsed: false,
      items: [
        { text: 'Overview', link: '/en/projects/ultimate-timer/' },
        { text: 'Installation', link: '/en/projects/ultimate-timer/installation' },
        { text: 'Configuration', link: '/en/projects/ultimate-timer/configuration' },
        { text: 'How It Works', link: '/en/projects/ultimate-timer/how-it-works' },
        { text: 'Examples', link: '/en/projects/ultimate-timer/examples' }
      ]
    }
  ],

  '/en/projects/fritzbox-to-mqtt/': [
    {
      text: 'FRITZ!Box to MQTT',
      collapsed: false,
      items: [
        { text: 'Overview', link: '/en/projects/fritzbox-to-mqtt/' },
        { text: 'Installation', link: '/en/projects/fritzbox-to-mqtt/installation' },
        { text: 'Configuration', link: '/en/projects/fritzbox-to-mqtt/configuration' },
        { text: 'Entities', link: '/en/projects/fritzbox-to-mqtt/entities' },
        { text: 'Troubleshooting', link: '/en/projects/fritzbox-to-mqtt/troubleshooting' }
      ]
    }
  ],

  '/en/projects/heizoel-to-mqtt/': [
    {
      text: 'Heizöl to MQTT',
      collapsed: false,
      items: [
        { text: 'Overview', link: '/en/projects/heizoel-to-mqtt/' },
        { text: 'Installation', link: '/en/projects/heizoel-to-mqtt/installation' },
        { text: 'Configuration', link: '/en/projects/heizoel-to-mqtt/configuration' },
        { text: 'Entities', link: '/en/projects/heizoel-to-mqtt/entities' }
      ]
    }
  ],

  '/en/projects/atlas/': [
    {
      text: 'ATLAS',
      collapsed: false,
      items: [
        { text: 'Overview', link: '/en/projects/atlas/' },
        { text: 'Architecture', link: '/en/projects/atlas/overview' },
        { text: 'Development Status', link: '/en/projects/atlas/development-status' },
        { text: 'Home Assistant', link: '/en/projects/atlas/homeassistant' },
        { text: 'Plugin Docs', link: '/en/projects/atlas/plugins' }
      ]
    }
  ],

  '/en/projects/': [
    {
      text: 'C# Projects',
      collapsed: false,
      items: [
        { text: 'Overview', link: '/en/projects/' },
        { text: 'HADash', link: '/en/projects/hadash/' },
        { text: 'Home Assistant Automation Exporter', link: '/en/projects/#home-assistant-automation-exporter' }
      ]
    }
  ]
}

export default defineConfig({
  lang: 'de-DE',
  title: 'UGSo Open Source',
  titleTemplate: ':title | UGSo Open Source',
  description:
    'Open-Source-Projekte, Code-Snippets und Blog von UGSo Software rund um Home Assistant, ioBroker Blockly, ESPHome, ATLAS und Lovelace.',

  base: '/',
  cleanUrls: true,
  lastUpdated: true,

  markdown: {
    lineNumbers: true
  },

  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/favicon.png' }],
    ['link', { rel: 'apple-touch-icon', href: '/favicon.png' }],
    ['meta', { name: 'theme-color', content: '#f4f5f7' }],
    ['meta', { name: 'application-name', content: 'UGSo Open Source' }]
  ],

  themeConfig: {
    logo: '/ugso-klein.png',
    siteTitle: 'UGSo Open Source',

    nav: navDe,

    sidebar: sidebarDe,

    socialLinks: [
      { icon: 'github', link: 'https://github.com/rockbaer2007' }
    ],

    search: {
      provider: 'local'
    },

    footer: {
      message:
        '<a href="/impressum/">Impressum</a>',
      copyright: '© 2026 UGSo Software'
    },

    outline: {
      label: 'Auf dieser Seite'
    },

    lastUpdated: {
      text: 'Zuletzt aktualisiert'
    },

    docFooter: {
      prev: 'Vorheriger Beitrag',
      next: 'Nächster Beitrag'
    }
  },

  locales: {
    root: {
      label: 'DE',
      lang: 'de-DE',
      themeConfig: {
        nav: navDe,
        sidebar: sidebarDe
      }
    },
    en: {
      label: 'EN',
      lang: 'en-US',
      title: 'UGSo Open Source',
      description:
        'Open-source projects, code snippets and documentation by UGSo Software for Home Assistant, ESPHome, ATLAS and Lovelace.',
      themeConfig: {
        nav: navEn,
        sidebar: sidebarEn,
        outline: {
          label: 'On this page'
        },
        lastUpdated: {
          text: 'Last updated'
        },
        docFooter: {
          prev: 'Previous page',
          next: 'Next page'
        }
      }
    }
  }
})
