<template>
  <div class="dark:bg-slate-900">
    <NuxtLayout name="default">
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup lang="ts">
import { trackRouter, useState } from "vue-gtag-next"

const config = useRuntimeConfig()
api_server_base.value = config.apiServerBase
api_client_base.value = config.public.apiClientBase
sprite_base.value = config.public.spriteBase

const state = useStore()

state.locale = getLocale()
watchEffect(async () => {
  state.changeLocale(state.locale)
})

state.puzzle_number = todayPuzzleNumber()

const loaded_statistics = loadStatistics()
if (loaded_statistics !== null) {
  state.statistics = loaded_statistics
}

const loaded_api_data = loadApiData()
if (loaded_api_data !== null && loaded_api_data.champions) {
  state.api_data = loaded_api_data
  state.api_data.champions.forEach((champ: any) => {
    if (!champ.name_en && champ.name) champ.name_en = champ.name
    if (!champ.title_en && champ.title) champ.title_en = champ.title
  })
}

apiChampions().then((data) => {
  state.api_data.champions = data
  saveApiData(state.api_data)
})

const loaded_puzzle_number = loadPuzzleNumber()
if (loaded_puzzle_number === state.puzzle_number) {
  const loaded_guess_data_list = loadGuessDataList()
  if (loaded_guess_data_list !== null) {
    state.guess_data_list = loaded_guess_data_list
  }
}

const title = fluent.format("champdle")
useHead({
  title: title,
  meta: [
    { name: "og:title", content: title },
    { name: "og:type", content: "website" },
    { name: "og:description", content: fluent.format("og-description") },
  ],
  link: [
    {
      rel: "icon",
      type: "image/svg+xml",
      href: "/favicon.svg",
    },
    {
      rel: "icon",
      type: "image/png",
      href: "/favicon.png",
    },
  ],
})

if (process.env.NODE_ENV === "production" && process.client) {
  const router = useRouter()
  trackRouter(router)
  useState().property.value = {
    id: config.public.gtagId,
  }
}
</script>
