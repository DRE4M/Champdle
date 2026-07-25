<template>
  <div class="flex items-center justify-center p-8">
    <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-600"></div>
  </div>
</template>

<script setup lang="ts">
const route = useRoute()
const router = useRouter()

if (typeof route.params.puzzle_number === "string") {
  const puzzleNum = parseInt(route.params.puzzle_number, 10)
  if (!isNaN(puzzleNum)) {
    apiRank(puzzleNum)
      .then((data) => {
        if (data && data.length > 0 && data[0].name) {
          const b64Name = utf8ToB64(data[0].name)
          router.replace(`/rank/${puzzleNum}/${b64Name}`)
        } else {
          router.replace("/")
        }
      })
      .catch(() => {
        router.replace("/")
      })
  } else {
    router.replace("/")
  }
} else {
  router.replace("/")
}
</script>
