<script setup>
import ChapterWrapper from '../../components/ChapterWrapper.vue';

const steps = [
    { title: "", text: "In this section, you will get the chance to understand the basics of language models by building your own.", slide: 0},
    { title: "", text: "The page you're about to be sent to will contain a prompt bar where you can type text. When you have finnished typing a word and hit the space bar, the model will predict the next word.", slide: 1},
    { title: "", text: "As you progress you will be able to select upgrades or features to improve your model. This will also unlock further capabilities.", slide: 2},
    { title: "", text: "You can remove features by clicking on them. This will also remove other features that rely on that specific feature.", slide: 3},
    { title: "", text: "However, we need somewhere to start. Let's start by putting all the words that exists in the english dictionary into the model and just pick one at random for the prediction.", slide: 4},
    { title: "", text: "You can begin by clicking the button below.", slide: 5}
]
</script>

<template>
    <ChapterWrapper
        :slides-src="'/slides/Intro.html'"
        :steps="steps"
        next-page="/builder"
    />
</template>