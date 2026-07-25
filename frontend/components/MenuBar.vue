<template>
  <nav class="flex flex-wrap items-center justify-between py-4 mx-auto gap-2">
    <div class="flex items-center space-x-2">
      <NuxtLink to="/" class="font-bold text-xl dark:text-slate-200">{{
        title
      }}</NuxtLink>
      <span
        v-if="subtitle"
        class="font-bold text-md text-gray-700 dark:text-slate-300"
        >{{ subtitle }}</span
      >
    </div>
    <div class="inline-flex items-center space-x-2">
      <!-- Date Picker Input for Custom Champion Date -->
      <div class="flex items-center space-x-1 bg-gray-100 dark:bg-slate-800 p-1 rounded-md border border-gray-200 dark:border-slate-700">
        <span class="text-xs text-gray-500 dark:text-slate-400 pl-1">📅 퍼즐 날짜:</span>
        <input
          type="date"
          v-model="selectedDate"
          @change="onDateChange"
          title="날짜 선택하여 챔피언 변경"
          class="rounded py-0.5 px-1.5 text-xs border border-gray-300 dark:border-slate-600 dark:bg-slate-700 dark:text-slate-200 shadow-sm cursor-pointer"
        />
      </div>

      <button
        v-if="$colorMode.value === 'dark'"
        class="p-2"
        @click="$colorMode.preference = 'light'"
        title="Light Mode"
      >
        <SunIcon></SunIcon>
      </button>
      <button
        v-if="$colorMode.value === 'light'"
        class="p-2"
        @click="$colorMode.preference = 'dark'"
        title="Dark Mode"
      >
        <MoonIcon></MoonIcon>
      </button>
      <select
        v-model="state.locale"
        class="rounded py-1 pl-2 border border-gray-200 dark:border-slate-600 dark:bg-slate-700 dark:text-slate-200 shadow-sm text-sm"
      >
        <option v-for="(_, locale) in fluentBundles" :value="locale">
          {{ $t("language-locale-" + locale) }}
        </option>
      </select>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { fluentBundles } from "#imports"

const state = useStore()
const selectedDate = ref("")

onMounted(() => {
  selectedDate.value = puzzleNumberToDateString(state.puzzle_number)
})

watch(() => state.puzzle_number, (newVal) => {
  selectedDate.value = puzzleNumberToDateString(newVal)
})

const onDateChange = () => {
  if (selectedDate.value) {
    const targetPuzzle = dateToPuzzleNumber(selectedDate.value)
    window.location.href = `/?puzzle=${targetPuzzle}`
  }
}

const props = defineProps({
  title: {
    type: String,
    default: fluent.format("champdle"),
  },
  subtitle: {
    type: String,
  },
})
</script>
