<script setup lang="ts">
import { onMounted } from "vue";
import ScrollSteps from "../../components/ScrollSteps.vue";
import { usePartialVideos } from "../../composables/usePartialVideos";

const { videos, load } = usePartialVideos(
  "/media/videos/simple/480p15/partial_movie_files",
  "ShapeTransform"
);

onMounted(async () => {
  await load();
  console.log(videos.value)
});
</script>

<template>
  <ScrollSteps :videos="videos">
    <div class="step">Vi starter med en sirkel.</div>
    <div class="step">Så transformerer den til et kvadrat.</div>
    <div class="step">Til slutt ser vi sluttresultatet.</div>
  </ScrollSteps>
</template>
