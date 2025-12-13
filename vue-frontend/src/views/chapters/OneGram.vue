<script setup>
import ChapterWrapper from '../../components/ChapterWrapper.vue';

const steps = [
    { title: "", text: "Right now, the AI reads text without understanding the meaning behind the words. It simply adds them to its vocabulary without any sense of which words usually appear together.", slide: 0},
    { title: "", text: "We can make the AI a bit smarter by teaching it to recognize individual words and their frequencies.", slide: 1},
    { title: "", text: "If we have the frequency of each word, we can estimate the probability of each word appearing next.", slide: 2},
    { title: "", text: "The model should be more likely to select the word with the highest probability so let us have it do that.", slide: 3},
    { title: "", text: "This quickly becomes repetitive as it is deterministic. The model is still too simple to capture context of each token." , slide: 4},
    { title: "", text: "The frequency of each token matters, but words alone aren’t enough to make language any meaningful." , slide: 5}
];
</script>

<template>
    <ChapterWrapper
        :slides-src="'/slides/OneGram.html'"
        :steps="steps"
        next-page="/builder"
    />
</template>