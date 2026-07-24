<template>
  <div>
    <MenuBar
      :subtitle="
        $t('champdle-index-subtitle', { puzzle_number: state.puzzle_number })
      "
    />
    <p class="text-sm text-gray-600 dark:text-slate-400 mb-4 text-center">
      {{ $t('og-description') }}
    </p>
    <ClientOnly>
      <Share v-if="isFinished" />
    </ClientOnly>
    <GuessInput />
    <ClientOnly>
      <GuessResult
        :guess_list="state.guess_data_list"
        :is_show_index="true"
        :is_show_fixed_last="true"
        v-if="state.guess_data_list.length > 0"
      />
    </ClientOnly>
    <Faq class="mt-24" />
  </div>
</template>

<script setup lang="ts">
const state = useStore()
const isFinished = computed(
  () => state.guess_data_list.find((v) => v.rank === 1) !== undefined
)
</script>
