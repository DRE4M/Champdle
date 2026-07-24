<template>
  <div
    v-if="champion"
    class="grid grid-cols-1 zs:grid-cols-2 xs:grid-cols-3 gap-2 text-xs dark:text-slate-300"
  >
    <ChampionInfoBlock>
      <div>
        <img
          class="mx-auto w-full max-w-[100px]"
          :alt="state.translateChampionName(champion.name_en, false) || champion.name_en"
          v-lazy="{
            src: championImageUrl,
            error: fallbackChampionImageUrl(champion.image_path),
          }"
        />
      </div>
    </ChampionInfoBlock>

    <!-- Basic Meta & Formula Categories (1) -->
    <ChampionInfoBlock>
      <p class="leading-relaxed font-bold text-sm">
        {{ state.translateChampionName(champion.name_en, false) || champion.name_en }}
      </p>
      <p class="leading-relaxed italic mb-1">
        {{ state.locale === 'ko' ? champion.title_ko : champion.title_en }}
      </p>
      <p class="leading-relaxed">
        {{ $t('champion-info-release-order') }}: {{ champion.champion_id }}번째
      </p>
      <p class="leading-relaxed">
        {{ $t('champion-info-region') }}: {{ champion.region || 'None' }}
      </p>
      <p class="leading-relaxed">
        {{ $t('champion-info-species') }}: {{ champion.species || 'None' }}
      </p>
      <p class="leading-relaxed">
        {{ $t('champion-info-gender') }}: {{ champion.gender || 'None' }}
      </p>
    </ChampionInfoBlock>

    <!-- Formula Categories (2) -->
    <ChampionInfoBlock>
      <p class="leading-relaxed">
        {{ $t('champion-info-attack-type') }}: {{ champion.attack_type }}
      </p>
      <p class="leading-relaxed">
        {{ $t('champion-info-resource') }}: {{ champion.partype }}
      </p>
      <p class="leading-relaxed">
        {{ $t('champion-info-role-1') }}: 
        <ChampionInfoTag :class="roleBgClass(champion.tag_1)">{{
          champion.tag_1
        }}</ChampionInfoTag>
      </p>
      <p class="leading-relaxed">
        {{ $t('champion-info-role-2') }}: 
        <ChampionInfoTag :class="roleBgClass(champion.tag_2)">{{
          champion.tag_2 !== null && champion.tag_2 !== '' ? champion.tag_2 : "NONE"
        }}</ChampionInfoTag>
      </p>
      <p class="leading-relaxed">
        {{ $t('champion-info-range') }}: {{ champion.attackrange }}
      </p>
      <p class="leading-relaxed">
        {{ $t('champion-info-movespeed') }}: {{ champion.movespeed }}
      </p>
    </ChampionInfoBlock>

    <!-- Formula Stats (1) -->
    <ChampionInfoBlock>
      <p class="leading-relaxed">
        {{ $t('champion-info-hp') }}: {{ champion.hp_base }} ~ {{ champion.hp_max }}
      </p>
      <p class="leading-relaxed">
        {{ $t('champion-info-mp') }}: {{ champion.mp_base }} ~ {{ champion.mp_max }}
      </p>
      <p class="leading-relaxed">
        {{ $t('champion-info-hp-regen') }}: {{ champion.hpregen_base }} ~ {{ champion.hpregen_max }}
      </p>
      <p class="leading-relaxed">
        {{ $t('champion-info-mp-regen') }}: {{ champion.mpregen_base }} ~ {{ champion.mpregen_max }}
      </p>
    </ChampionInfoBlock>

    <!-- Formula Stats (2) -->
    <ChampionInfoBlock>
      <p class="leading-relaxed">
        {{ $t('champion-info-attack-damage') }}: {{ champion.attackdamage_base }} ~ {{ champion.attackdamage_max }}
      </p>
      <p class="leading-relaxed">
        {{ $t('champion-info-attack-speed') }}: {{ champion.attackspeed_base }} ~ {{ champion.attackspeed_max }}
      </p>
      <p class="leading-relaxed">
        {{ $t('champion-info-armor') }}: {{ champion.armor_base }} ~ {{ champion.armor_max }}
      </p>
      <p class="leading-relaxed">
        {{ $t('champion-info-spellblock') }}: {{ champion.spellblock_base }} ~ {{ champion.spellblock_max }}
      </p>
    </ChampionInfoBlock>
  </div>
</template>

<script setup lang="ts">
const state = useStore()
const props = defineProps<{
  champion?: Champion
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
