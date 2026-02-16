<script setup>
import { ref, onMounted } from 'vue'
import ChapterWrapper from '../../components/ChapterWrapper.vue'
import { loadChapterContent } from '../../data/chapters'
import { markIntroAsSeen } from '../../api/user'

const chapter = ref(null)

onMounted(async () => {
    chapter.value = await loadChapterContent('intro')
})

const handleComplete = () => {
    markIntroAsSeen();
}
</script>

<template>
    <ChapterWrapper v-if="chapter" :slides-src="chapter.slidesSrc" :steps="chapter.steps" :next-page="chapter.nextPage"
        @complete="handleComplete" />
</template>