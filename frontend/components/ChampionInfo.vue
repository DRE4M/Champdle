<template>
  <div v-if="champion" class="space-y-2 text-xs dark:text-slate-300">
    <!-- Image & Hero Banner Card -->
    <div class="flex items-center space-x-3 p-2 rounded-lg bg-gray-100 dark:bg-slate-800 border border-gray-200 dark:border-slate-700">
      <img
        class="w-14 h-14 rounded-full border border-gray-300 dark:border-slate-600 object-cover shadow-sm"
        :alt="state.translateChampionName(champion.name_en, false) || champion.name_en"
        v-lazy="{
          src: championImageUrl,
          error: fallbackChampionImageUrl(champion.image_path),
        }"
      />
      <div>
        <div class="font-bold text-sm text-gray-900 dark:text-slate-100">
          {{ state.translateChampionName(champion.name_en, false) || champion.name_en }}
          <span class="text-xs font-normal text-gray-500 dark:text-slate-400">({{ champion.name_en }})</span>
        </div>
        <div class="italic text-xs text-indigo-600 dark:text-indigo-400 font-medium">
          {{ state.locale === 'ko' ? champion.title_ko : champion.title_en }}
        </div>
        <div v-if="formula_detail" class="mt-1">
          <span class="px-2 py-0.5 text-[11px] font-mono rounded bg-indigo-100 dark:bg-indigo-900/80 text-indigo-800 dark:text-indigo-200">
            📊 계산 구성: {{ formula_detail }}
          </span>
        </div>
      </div>
    </div>

    <!-- Section 1: Official Category Factors (80pts) -->
    <div class="p-2 rounded-lg bg-indigo-50/70 dark:bg-indigo-950/40 border border-indigo-200 dark:border-indigo-900/60">
      <div class="flex items-center justify-between mb-1.5">
        <span class="px-2 py-0.5 text-[11px] font-bold rounded bg-indigo-100 text-indigo-800 dark:bg-indigo-900/80 dark:text-indigo-200">
          📌 공식 카테고리 항목 (80점 만점 요인)
        </span>
      </div>
      <div class="grid grid-cols-1 xs:grid-cols-2 gap-2">
        <ChampionInfoBlock class="bg-white/80 dark:bg-slate-900/80 border-indigo-100 dark:border-indigo-900/40">
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-release-order') }}:</span> {{ champion.champion_id }}번째
          </p>
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-region') }}:</span> {{ champion.region || 'None' }}
          </p>
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-species') }}:</span> {{ champion.species || 'None' }}
          </p>
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-gender') }}:</span> {{ champion.gender || 'None' }}
          </p>
        </ChampionInfoBlock>

        <ChampionInfoBlock class="bg-white/80 dark:bg-slate-900/80 border-indigo-100 dark:border-indigo-900/40">
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-attack-type') }}:</span> {{ champion.attack_type }}
          </p>
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-resource') }}:</span> {{ champion.partype }}
          </p>
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-role-1') }}:</span>
            <ChampionInfoTag :class="roleBgClass(champion.tag_1)" class="ml-1">{{ champion.tag_1 }}</ChampionInfoTag>
          </p>
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-role-2') }}:</span>
            <ChampionInfoTag :class="roleBgClass(champion.tag_2)" class="ml-1">{{
              champion.tag_2 !== null && champion.tag_2 !== '' ? champion.tag_2 : "NONE"
            }}</ChampionInfoTag>
          </p>
        </ChampionInfoBlock>
      </div>
    </div>

    <!-- Section 2: Official Stat Factors (20pts) -->
    <div class="p-2 rounded-lg bg-emerald-50/70 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-900/60">
      <div class="flex items-center justify-between mb-1.5">
        <span class="px-2 py-0.5 text-[11px] font-bold rounded bg-emerald-100 text-emerald-800 dark:bg-emerald-900/80 dark:text-emerald-200">
          📊 공식 스탯 Min-Max 항목 (20점 만점 요인)
        </span>
      </div>
      <div class="grid grid-cols-1 xs:grid-cols-2 gap-2">
        <ChampionInfoBlock class="bg-white/80 dark:bg-slate-900/80 border-emerald-100 dark:border-emerald-900/40">
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-range') }}:</span> {{ champion.attackrange }}
          </p>
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-movespeed') }}:</span> {{ champion.movespeed }}
          </p>
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-hp') }}:</span> {{ champion.hp_base }} ~ {{ champion.hp_max }}
          </p>
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-mp') }}:</span> {{ champion.mp_base }} ~ {{ champion.mp_max }}
          </p>
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-hp-regen') }}:</span> {{ champion.hpregen_base }} ~ {{ champion.hpregen_max }}
          </p>
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-mp-regen') }}:</span> {{ champion.mpregen_base }} ~ {{ champion.mpregen_max }}
          </p>
        </ChampionInfoBlock>

        <ChampionInfoBlock class="bg-white/80 dark:bg-slate-900/80 border-emerald-100 dark:border-emerald-900/40">
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-attack-damage') }}:</span> {{ champion.attackdamage_base }} ~ {{ champion.attackdamage_max }}
          </p>
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-attack-speed') }}:</span> {{ champion.attackspeed_base }} ~ {{ champion.attackspeed_max }}
          </p>
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-armor') }}:</span> {{ champion.armor_base }} ~ {{ champion.armor_max }}
          </p>
          <p class="leading-relaxed">
            <span class="font-semibold text-gray-700 dark:text-slate-300">{{ $t('champion-info-spellblock') }}:</span> {{ champion.spellblock_base }} ~ {{ champion.spellblock_max }}
          </p>
        </ChampionInfoBlock>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const state = useStore()
const props = defineProps<{
  champion: any
  formula_detail?: string
}>()

const championImageUrl = computed(() => {
  if (
    !props.champion ||
    props.champion.image_path === undefined ||
    props.champion.image_path === ""
  ) {
    return missingChampionImageUrl()
  } else {
    return sprite_base.value + "/" + props.champion.image_path
  }
})

function roleBgClass(role?: string): string {
  if (!role) return "bg-none"
  const class_name = {
    Fighter: "bg-red-200 dark:bg-red-900",
    Tank: "bg-lime-200 dark:bg-lime-900",
    Mage: "bg-purple-200 dark:bg-purple-900",
    Assassin: "bg-gray-400 dark:bg-gray-700",
    Support: "bg-green-200 dark:bg-green-900",
    Marksman: "bg-orange-200 dark:bg-orange-900",
  }[role]
  return class_name === undefined ? "bg-none" : class_name
}
</script>
