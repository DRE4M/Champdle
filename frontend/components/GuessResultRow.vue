<template>
  <tr
    v-bind="$attrs"
    :class="mainClass"
    @click="is_show_champion_info = !is_show_champion_info"
  >
    <td class="p-2" v-if="is_show_index">{{ guess_data.index + 1 }}</td>
    <td class="p-2 pr-0 w-12">
      <img
        :alt="state.translateChampionName(guess_data.name, false) || guess_data.name"
        v-lazy="{
          src: championImageUrl,
          error: fallbackChampionImageUrl(champion?.image_path),
        }"
      />
    </td>
    <td class="p-2">
      {{ state.translateChampionName(guess_data.name, false) || guess_data.name }}
    </td>
    <td
      class="p-2"
      :style="{
        color: similarityColor(guess_data.rank),
      }"
    >
      {{ (guess_data.similarity * 100).toFixed(3) }}%
    </td>
    <td class="p-2 text-xs font-mono text-gray-600 dark:text-slate-400 whitespace-nowrap">
      <span v-if="guess_data.formula_detail" class="px-1.5 py-0.5 rounded bg-gray-100 dark:bg-slate-700/60 text-[11px]">
        {{ guess_data.formula_detail }}
      </span>
      <span v-else-if="guess_data.category_score !== undefined" class="px-1.5 py-0.5 rounded bg-gray-100 dark:bg-slate-700/60 text-[11px]">
        카테고리 {{ guess_data.category_score.toFixed(1) }}점 + 스탯 {{ guess_data.stat_score.toFixed(1) }}점
      </span>
      <span v-else class="text-gray-400 text-[11px]">
        -
      </span>
    </td>
    <td
      class="p-2"
      :style="{
        background:
          'linear-gradient(to left, transparent ' +
          rankPercent +
          '%, ' +
          ($colorMode.value === 'dark' ? '#125409' : '#9bff8d') +
          ' ' +
          rankPercent +
          '%)',
      }"
    >
      {{ isCorrect ? $t("correct-guess") : guess_data.rank }}
    </td>
  </tr>
  <tr v-if="is_show_champion_info">
    <td class="p-2" :colspan="is_show_index ? 6 : 5">
      <ChampionInfo v-if="champion" :champion="champion"></ChampionInfo>
    </td>
  </tr>
</template>

<script setup lang="ts">
const state = useStore()
const colorMode = useColorMode()
const props = defineProps<{
  guess_data: GuessData
  is_show_index?: boolean
}>()

const is_show_champion_info = ref(false)

const mainClass = computed(() => {
  const klass = "cursor-pointer"
  const attrs = useAttrs()
  return attrs.class ? `${attrs.class} ${klass}` : klass
})

const rankPercent = computed(() => {
  const total = state.api_data.champions?.length || 1
  return (props.guess_data.rank / total) * 100
})
const isCorrect = computed(() => {
  return props.guess_data.rank === 1
})
const champion = computed(() => {
  if (!props.guess_data?.name) return undefined
  const targetName = props.guess_data.name.trim().toLowerCase()
  return state.api_data.champions?.find((v: any) => {
    const nameEn = (v.name_en || v.name || v.alias || '').trim().toLowerCase()
    const nameKo = (v.name_ko || '').trim().toLowerCase()
    return nameEn === targetName || nameKo === targetName
  })
})

const championImageUrl = computed(() => {
  if (
    champion.value?.image_path === undefined ||
    champion.value?.image_path === ""
  ) {
    return missingChampionImageUrl()
  } else {
    return sprite_base.value + "/" + champion.value?.image_path
  }
})

const championCount = computed(() => state.api_data.champions?.length || 1)

function similarityColor(rank: number): string {
  const relative_rank = 1 - Math.pow(1 - rank / championCount.value, 5) // easeOutQuint
  if (colorMode.value === "dark") {
    return `rgb(203, ${213 * relative_rank}, ${225 * relative_rank})`
  }
  return `rgb(${255 * (1 - relative_rank)}, 0, 0)`
}
</script>
