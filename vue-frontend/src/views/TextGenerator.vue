<script lang="ts" setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { fetchPrediction } from '../api/builder';

const content = ref('')
const router = useRouter()

const MIN_LENGTH = 50
const MAX_LENGTH = 500
const LOOP_DETECTION_WINDOW = 15
const MIN_NGRAM = 2
const MAX_NGRAM = 6

async function generateText() {
    let text = content.value
    let continueGenerating = true
    const recentTokens: string[] = []
    const seenNgrams = new Set<string>()


    while (continueGenerating) {
        let next_token = await fetchPrediction(text)
        next_token = capitalizeAfterPeriod(next_token, text)
        text = addToken(text, next_token)
        recentTokens.push(next_token)

        if (recentTokens.length > LOOP_DETECTION_WINDOW) {
            recentTokens.shift()
        }

        if (isLooping(recentTokens, seenNgrams)) {
            continueGenerating = false
            content.value = text + '... [Generation stopped due to detected repetition]'
            break
        }

        content.value = text

        const textLength = text.trim().length
        const hasPeriod = next_token.includes('.')

        if (text.length >= MAX_LENGTH) {
            continueGenerating = false
        } else if (textLength >= MIN_LENGTH && hasPeriod) {
            continueGenerating = false
        }
    }
}

function addToken(text: string, token: string): string {
    const isPunctuation = /^[.,!?;:()—-]/.test(token)
    if (isPunctuation) {
        return text + token
    } else if (text && !text.endsWith(' ')) {
        return text + ' ' + token
    } else {
        return text + token
    }

}

function capitalizeAfterPeriod(token: string, text: string): string {
    const endsWithPeriod = /[.!?]\s*$/.test(text)
    if (endsWithPeriod && token.length > 0) {
        return token.charAt(0).toUpperCase() + token.slice(1)
    }
    return token
}

function isLooping(tokens: string[], seen:Set<string>): boolean {
    for (let ngramSize = MIN_NGRAM; ngramSize <= MAX_NGRAM; ngramSize++) {
        if (tokens.length < ngramSize) {
            continue
        }
        const ngram = tokens.slice(-ngramSize).join(' ')
        if (seen.has(ngram)) {
            return true
        }
        seen.add(ngram)
    }
    return false
}

function goBack() {
    router.push({ name: 'Builder' })
}
</script>

<template>
    <button class="back-button" @click="goBack">← Back</button>
    <div class="text-generator-container">
        <h1>Text Generator</h1>
        <textarea v-model="content" placeholder="Enter your prompt here..." rows="10"></textarea>
        <button @click="generateText">Generate Text</button>
    </div>
</template>

<style scoped>
.text-generator-container {
    padding: 2rem;
}

textarea {
    width: 100%;
    padding: 1rem;
    font-size: 1rem;
    border: 1px solid var(--color-primary);
    border-radius: 0.5rem;
    background: var(--color-white);
    color: var(--color-text);
    font-family: inherit;
}

button {
    margin-top: 1rem;
    padding: 0.5rem 1rem;
    background: var(--color-primary);
    color: white;
    border: none;
    border-radius: 0.5rem;
    cursor: pointer;
}

button:hover {
    background: var(--color-primary-hover);
}
</style>