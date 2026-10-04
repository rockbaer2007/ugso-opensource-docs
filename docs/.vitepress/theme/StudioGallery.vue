<script setup lang="ts">
import { withBase } from 'vitepress'
import images from './studio-gallery.json'

const props = defineProps<{ locale: 'de' | 'en' }>()
const imageUrl = (file: string) => withBase(`/images/grafik-visual-studio/gallery/${file}`)
</script>

<template>
  <div class="studio-gallery">
    <figure class="studio-gallery-overview">
      <a :href="imageUrl(images[0].file)" :aria-label="images[0].title[props.locale]">
        <img :src="imageUrl(images[0].file)" :alt="images[0].title[props.locale]" fetchpriority="high">
      </a>
      <figcaption>
        <h2>{{ images[0].title[props.locale] }}</h2>
        <p>{{ images[0].caption[props.locale] }}</p>
      </figcaption>
    </figure>
    <div class="studio-gallery-grid">
      <figure v-for="image in images.slice(1)" :key="image.file"
        :class="{ 'studio-gallery-wide': image.file.includes('toolbar') }">
        <a :href="imageUrl(image.file)" :aria-label="image.title[props.locale]">
          <img :src="imageUrl(image.file)" :alt="image.title[props.locale]" loading="lazy" decoding="async">
        </a>
        <figcaption>
          <h2>{{ image.title[props.locale] }}</h2>
          <p>{{ image.caption[props.locale] }}</p>
        </figcaption>
      </figure>
    </div>
  </div>
</template>

<style scoped>
.studio-gallery figure {
  margin: 0;
  min-width: 0;
  padding: 16px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  background: var(--vp-c-bg-soft);
}
.studio-gallery a {
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  overflow: hidden;
}
.studio-gallery img {
  display: block;
  max-width: 100%;
  max-height: 360px;
  width: auto;
  height: auto;
  object-fit: contain;
}
.studio-gallery-overview {
  text-align: center;
  margin-bottom: 24px !important;
}
.studio-gallery-overview img {
  width: 100%;
  max-height: none;
}
.studio-gallery-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 24px;
  align-items: start;
}
.studio-gallery-wide {
  grid-column: 1 / -1;
}
.studio-gallery h2 {
  margin: 16px 0 8px;
  padding: 0;
  border: 0;
  font-size: 1.15rem;
  line-height: 1.4;
}
.studio-gallery p {
  margin: 0;
  font-size: 0.95rem;
  overflow-wrap: anywhere;
}
@media (max-width: 640px) {
  .studio-gallery-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }
  .studio-gallery figure {
    padding: 12px;
  }
}
</style>
