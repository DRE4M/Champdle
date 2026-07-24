import { defineNuxtConfig } from 'nuxt/config'
import fluentPlugin from "rollup-plugin-fluent-vue"

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  app: {
    baseURL: process.env.NUXT_APP_BASE_URL || '/',
  },
  modules: ["@nuxtjs/tailwindcss", "@nuxtjs/color-mode", "@pinia/nuxt"],
  typescript: {
    shim: false,
  },
  routeRules: {
    '/languages': { proxy: 'http://localhost:8000/languages' },
    '/champions': { proxy: 'http://localhost:8000/champions' },
    '/champion_name_map/**': { proxy: 'http://localhost:8000/champion_name_map/**' },
    '/rank/**': { proxy: 'http://localhost:8000/rank/**' },
    '/guess/**': { proxy: 'http://localhost:8000/guess/**' },
  },
  runtimeConfig: {
    apiServerBase: process.env.LOLMANTLE_API_SERVER_BASE || "http://localhost:8000",
    public: {
      frontendBase: process.env.LOLMANTLE_FRONTEND_BASE || "http://localhost:3000",
      apiClientBase: process.env.LOLMANTLE_API_CLIENT_BASE || "",
      spriteBase: process.env.LOLMANTLE_SPRITE_BASE || "http://localhost:8001",
      gtagId: "GA_MEASUREMENT_ID",
    },
  },
  colorMode: {
    classSuffix: "",
  },
  vite: {
    plugins: [fluentPlugin()],
    server: {
      hmr: {
        protocol: "ws", // TODO: parse from env var
        port: 50443,
        clientPort: 50443,
      },
    },
  },
})
