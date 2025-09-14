<script setup lang="ts">
import 'intersection-observer'
import Scrollama from 'vue-scrollama'
import { ref } from 'vue'

const steps = [{ id: "A" }, { id: "B" }, { id: "C" }, { id: "D" }]
const activeStepId = ref("A")

function stepEnterHandler({ element, index, direction }: any) {
  console.log("step-enter", { element, index, direction })
  activeStepId.value = element.dataset.stepId
}
</script>

<template>
  <div class="flex w-full h-screen">
    <!-- Sticky graphic on the left -->
    <div
      class="graphic flex-1 sticky top-0 bg-gray-300 border border-black flex items-center justify-center text-8xl"
    >
      {{ activeStepId }}
    </div>

    <!-- Scrollable steps on the right -->
    <Scrollama
      :offset="0.6"
      @step-enter="stepEnterHandler"
      class="flex-1"
    >
      <template v-for="step in steps" :key="step.id">
        <div
          :data-step-id="step.id"
          class="my-[100vh] h-48 w-48 mx-auto bg-yellow-300 border border-black flex justify-center items-center"
        >
          Step {{ step.id }}
        </div>
      </template>
    </Scrollama>
  </div>
</template>

<style scoped>
.graphic {
  height: 100vh; /* full viewport height */
}
.step {
  font-size: 2rem;
}
</style>
