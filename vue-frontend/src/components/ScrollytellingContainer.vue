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
    iframe.value.contentWindow.postMessage(
      JSON.stringify({
        method: 'slide',
        args: [slideIndex]
      }),
      "*"
    );
  }
}

onMounted(() => {
  if (iframe.value) {
    iframe.value.onload = () => {
      setTimeout(() => {
        const iframeDoc = iframe.value?.contentDocument || iframe.value?.contentWindow?.document;
        if (iframeDoc) {
          const videos = iframeDoc.querySelectorAll('video');
          videos.forEach(video => {
            video.muted = true;
            video.playsInline = true;
            video.autoplay = true;
            video.play().catch(err => console.log('Video play failed:', err));
          });
        }

        sendToIframe(props.steps[0].slide);

        scroller = scrollama();

        scroller
          .setup({
            step: ".story-step",
            offset: 0.9,
            once: false,
          })
          .onStepEnter(({ index }) => {
            sendToIframe(props.steps[index].slide);

            document
              .querySelectorAll<HTMLElement>(".story-step")
              .forEach((el, i) => el.classList.toggle("is-active", i === index));
          });
      }, 500);
    };
  }
});

onBeforeUnmount(() => {
  scroller?.destroy();
});
</script>

<template>
  <div class="scrollytelling-container">
    <!-- Left: Sticky Slideshow -->
    <div class="slideshow">
      <iframe ref="iframe" :src="slidesSrc" class="slides-frame" allow="autoplay; fullscreen"></iframe>
    </div>

    <!-- Right: Scrollable Narrative -->
    <div class="story">
      <section v-for="(step, index) in steps" :key="index" class="story-step">
        <h2>{{ step.title }}</h2>
        <div>{{ step.text }}</div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.scrollytelling-container {
  position: relative;
  width: 100vw;
  background: #000;
  min-height: 100vh;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}

.slideshow {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 0;
}

.slides-frame {
  width: 100%;
  height: 80%;
  border: none;
}

.story {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  gap: 100vh;
  /* pacing for scroll */
  padding-top: 100vh;
  padding-bottom: 100vh;
}

.story-step {
  min-height: 20vh;
  width: 100%;
  padding: .5rem 2rem;
  background: var(--color-overlay-bg);
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 20px var(--color-overlay-shadow);
  transition: all 0.3s ease;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  font-size: 1.25rem;
  line-height: 1.6;
  color: #1d1d1f;
  box-sizing: border-box;
}

.story-step h2 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: #1d1d1f;
}

.story-step.is-active {
  background: var(--color-overlay-active);
  transform: scale(1.02);
  box-shadow: 0 12px 48px var(--color-overlay-shadow-active);
}
</style>