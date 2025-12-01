<script lang="ts" setup>
import { ref, watch, nextTick, onMounted, onBeforeUnmount } from 'vue'
import PromptBar from '../components/builder/PromptBar.vue'
import SkillTreeD3 from '../components/builder/SkillTreeD3.vue'

const showImprovements = ref(false)

const skillTreeWrapper = ref<HTMLElement | null>(null)
const treeBox = ref<{ width: number; height: number } | null>(null)

function handlePromptUsed() {
  showImprovements.value = true
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
  <div>
    <h1>Build Your Own AI</h1>
    <PromptBar @used="handlePromptUsed" />
    <div id="skill-tree" ref="skillTreeWrapper">
      <SkillTreeD3 v-if="showImprovements" :boundingBox="treeBox || undefined" />
    </div>
  </div>
</template>

<style>
.h1 {
  text-align: center;
  margin-bottom: 2rem;
  font-family: Arial, Helvetica, sans-serif;
}
</style>