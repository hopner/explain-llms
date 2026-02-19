<script lang="ts" setup>
import { ref, watch, nextTick, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import PromptBar from '../components/builder/PromptBar.vue'
import SkillTreeD3 from '../components/builder/SkillTreeD3.vue'

const router = useRouter()
const showImprovements = ref(false)

const skillTreeWrapper = ref<HTMLElement | null>(null)
const treeBox = ref<{ width: number; height: number } | null>(null)

function handlePromptUsed() {
  showImprovements.value = true
}

function goHome() {
  router.push({ name: 'Home' })
}

function goToGenerator() {
  router.push({ name: 'TextGenerator' })
}

async function measureBox() {
  await nextTick()
  const el = skillTreeWrapper.value
  if (!el) return
  const width = el.clientWidth
  const height = Math.max(300, el.clientHeight || window.innerHeight * 0.55)
  treeBox.value = { width, height }
}

watch(showImprovements, async (val) => {
  if (val) {
    await measureBox()
    document.querySelector('#skill-tree')?.scrollIntoView({ behavior: 'smooth' })
  }
})

let resizeTimer: number | null = null
function onResize() {
  if (!showImprovements.value) return
  if (resizeTimer) window.clearTimeout(resizeTimer)
  resizeTimer = window.setTimeout(() => {
    measureBox()
    resizeTimer = null
  }, 120)
}
onMounted(() => window.addEventListener('resize', onResize))
onBeforeUnmount(() => window.removeEventListener('resize', onResize))
</script>

<template>
  <div class="builder-container">
    <button class="back-button" @click="goHome">← Back</button>
    <button class="generator-button" @click="goToGenerator">Text generator</button>
    <div class="builder-header">
      <h1>Build Your Own AI</h1>
      <p class="subtitle">Customize your language model by selecting improvements</p>
    </div>

    <div class="prompt-section">
      <PromptBar @used="handlePromptUsed" />
    </div>

    <div id="skill-tree" ref="skillTreeWrapper" class="skill-tree-wrapper">
      <SkillTreeD3 v-if="showImprovements" :boundingBox="treeBox || undefined" />
    </div>
  </div>
</template>

<style scoped>
.builder-container {
  min-height: 100vh;
  background: var(--color-bg-primary);
  color: var(--color-text);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  position: relative;
}

.back-button {
  position: absolute;
  top: 1.5rem;
  left: 1.5rem;
  background: var(--color-primary);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
  transition: background 0.2s;
  z-index: 10;
  font-family: inherit;
}

.back-button:hover {
  background: var(--color-primary-hover);
}

.generator-button {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  background: var(--color-primary);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
  transition: background 0.2s;
  z-index: 10;
  font-family: inherit;
}

.generator-button:hover {
  background: var(--color-primary-hover);
}

.builder-header {
  padding: 3rem 2rem;
  text-align: center;
  border-bottom: 1px solid var(--color-primary-15);
  background: var(--color-bg-secondary);
}

.builder-header h1 {
  margin: 0 0 0.5rem 0;
  font-size: 3rem;
  font-weight: 700;
  color: var(--color-primary);
}

.subtitle {
  margin: 0;
  font-size: 1.125rem;
  color: var(--color-accent);
  font-weight: 400;
}

.prompt-section {
  padding: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.skill-tree-wrapper {
  padding: 3rem 2rem;
  margin: 0 auto;
}

@media (max-width: 768px) {
  .builder-header h1 {
    font-size: 2rem;
  }

  .subtitle {
    font-size: 1rem;
  }

  .builder-header {
    padding: 2rem 1rem;
  }
}
</style>