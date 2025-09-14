<script setup lang="ts">
import 'intersection-observer' // polyfill
import Scrollama from 'vue-scrollama'
import { ref } from 'vue'

interface Props {
  videos: string[]
}
const props = defineProps<Props>()

// Which step we're on
const currentStep = ref(0)

function onStepEnter({ index }: { index: number }) {
  if (props.videos[index]) {
    currentStep.value = index
  }
}
</script>

<template>
  <div class="scroll-steps">
    <!-- Sticky video -->
    <div class="video-container">
      <video
        v-if="videos[currentStep]"
        :src="videos[currentStep]"
        autoplay
        muted
        playsinline
        key="currentStep"
      />
    </div>

    <!-- Scroll-driven steps -->
    <Scrollama
      class="text-container"
      @step-enter="onStepEnter"
      :offset="0.6"
    >
      <slot />
    </Scrollama>
  </div>
</template>

<style scoped>
.scroll-steps {
  display: flex;
  height: 100vh;
}

.video-container {
  flex: 1;
  position: sticky;
  top: 0;
  height: 100vh;
  background: black;
  display: flex;
  justify-content: center;
  align-items: center;
}

video {
  max-width: 100%;
  max-height: 100%;
}

.text-container {
  flex: 1;
  padding: 3rem;
}

.text-container > * {
  height: 100vh;
  display: flex;
  align-items: center;
  font-size: 1.2rem;
}
</style>
