import { defineConfig } from 'vite'
import { fileURLToPath } from 'node:url'

// "type": "module" means no __dirname, so resolve entries relative to this file.
export default defineConfig({
  appType: 'mpa',
  build: {
    rollupOptions: {
      input: {
        main: fileURLToPath(new URL('./index.html', import.meta.url)),
        guide: fileURLToPath(new URL('./guide/index.html', import.meta.url)),
      },
    },
  },
})
