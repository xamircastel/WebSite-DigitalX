// @ts-check

import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://digital-x.com.co',
  integrations: [mdx(), sitemap()],

  devToolbar: {
    enabled: false, // Deshabilitar la barra de herramientas de desarrollo
  },

  vite: {
    plugins: [tailwindcss()],
  },
});