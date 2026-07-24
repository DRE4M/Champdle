<template>
  <div class="container max-w-xl mx-auto px-2 mb-10">
    <slot />
  </div>
  <div class="px-2 pb-10 text-xs text-gray-700 dark:text-slate-400 text-center">
    League of Legends © {{ new Date().getFullYear() }} Riot Games, Inc. Champdle isn’t endorsed by Riot Games and doesn’t reflect the views or opinions of Riot Games or anyone officially involved in producing or managing League of Legends.<br />
    No copyright or trademark infringement is intended in using League of Legends content on Champdle.
  </div>
</template>
