<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from "vue";
import scrollama from "scrollama";

interface Step {
  title: string;
  text: string;
  slide: number;
}

const props = defineProps<{
  slidesSrc: string;
  steps: Step[];
}>();

const iframe = ref<HTMLIFrameElement | null>(null);
let scroller: ReturnType<typeof scrollama> | null = null;

function sendToIframe(slideIndex: number) {
  if (iframe.value && iframe.value.contentWindow) {
    // Use Reveal.js postMessage API
    iframe.value.contentWindow.postMessage(
      JSON.stringify({
        method: 'slide',
        args: [slideIndex] // Reveal.js expects slide index
      }),
      "*"
    );
  }
}

onMounted(() => {
  scroller = scrollama();

  scroller
    .setup({
      step: ".story-step",
      offset: 0.5,
      once: false,
    })
    .onStepEnter(({ index }) => {
      sendToIframe(props.steps[index].slide);

      // highlight active step
      document
        .querySelectorAll<HTMLElement>(".story-step")
        .forEach((el, i) => el.classList.toggle("is-active", i === index));
    });
});

onBeforeUnmount(() => {
  scroller?.destroy();
});
</script>

<template>
  <div class="scrollytelling-container">
    <!-- Left: Sticky Slideshow -->
    <div class="slideshow">
      <iframe
        ref="iframe"
        :src="slidesSrc"
        class="slides-frame"
      ></iframe>
    </div>

    <!-- Right: Scrollable Narrative -->
    <div class="story">
      <section
        v-for="(step, index) in steps"
        :key="index"
        class="story-step"
      >
        <h2>{{ step.title }}</h2>
        <p>{{ step.text }}</p>
      </section>
    </div>
  </div>
</template>

<style scoped>
.scrollytelling-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.slideshow {
  position: sticky;
  top: 0;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.slides-frame {
  width: 100%;
  height: 100vh;
  border: none;
}

.story {
  display: flex;
  flex-direction: column;
  gap: 100vh; /* pacing for scroll */
}

.story-step {
  min-height: 100vh;
  padding: 2rem;
  border-left: 3px solid #eee;
  transition: background 0.3s;
}

.story-step.is-active {
  background: #f9f9f9;
  border-left-color: #333;
}
</style>