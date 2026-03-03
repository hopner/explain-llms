<script lang="ts" setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { fetchPrediction } from '../api/builder';

const content = ref('')
const router = useRouter()

const MIN_LENGTH = 50
const MAX_LENGTH = 500
const LOOP_DETECTION_WINDOW = 15
const MIN_NGRAM = 3
const MAX_NGRAM = 6

async function generateText() {
    const startingText = content.value
    const startingLength = startingText.length
    let text = startingText
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

        const detectedLoop = detectLoop(recentTokens, seenNgrams)
        if (detectedLoop) {
            continueGenerating = false
            content.value = text + ' ' + detectedLoop + '... [Generation stopped due to detected repetition]'
            break
        }

        content.value = text

        const generatedLength = text.length - startingLength
        const hasPeriod = next_token.includes('.')

        if (generatedLength >= MAX_LENGTH) {
            continueGenerating = false
        } else if (generatedLength >= MIN_LENGTH && hasPeriod) {
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

function detectLoop(tokens: string[], seen:Set<string>): string | null {
    for (let ngramSize = MIN_NGRAM; ngramSize <= MAX_NGRAM; ngramSize++) {
        if (tokens.length < ngramSize) {
            continue
        }
        const ngram = tokens.slice(-ngramSize).join(' ')
        if (seen.has(ngram)) {
            return ngram
        }
        seen.add(ngram)
    }
    return null
}

function goBack() {
    router.push({ name: 'Builder' })
}
</script>
<template>
  <div class="generator-page">
    <button class="back-button" @click="goBack">← Back</button>
    
    <div class="generator-container">
      <div class="generator-header">
        <h1>Text Generator</h1>
        <p class="subtitle">Let your AI continue the story</p>
      </div>

      <div class="generator-content">
        <div class="input-section">
          <label for="prompt-input">Start entering text and let you current AI configuration complete it by clicking the button below.</label>
          <textarea 
            id="prompt-input"
            v-model="content" 
            placeholder="Start typing or paste your text here..."
            rows="12"
          ></textarea>
        </div>

        <button class="generate-button" @click="generateText">
          Generate Text
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.generator-page {
  min-height: 100vh;
  background: var(--color-bg-primary);
  color: var(--color-text);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
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

.generator-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
}

.generator-header {
  text-align: center;
  padding: 3rem 2rem 2rem;
}

.generator-header h1 {
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

.generator-content {
  background: var(--color-bg-secondary);
  border-radius: 1rem;
  padding: 2.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.input-section {
  margin-bottom: 1.5rem;
}

.input-section label {
  display: block;
  margin-bottom: 0.75rem;
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--color-text);
}

textarea {
  width: 100%;
  padding: 1.25rem;
  font-size: 1rem;
  line-height: 1.6;
  border: 2px solid var(--color-primary-15);
  border-radius: 0.75rem;
  background: var(--color-white);
  color: var(--color-text);
  font-family: inherit;
  resize: vertical;
  transition: border-color 0.2s, box-shadow 0.2s;
}

textarea:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

textarea::placeholder {
  color: #9ca3af;
}

.generate-button {
  width: 100%;
  padding: 1rem 2rem;
  background: var(--color-primary);
  color: white;
  border: none;
  border-radius: 0.75rem;
  cursor: pointer;
  font-size: 1.125rem;
  font-weight: 600;
  transition: background 0.2s, transform 0.1s;
  font-family: inherit;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.generate-button:hover {
  background: var(--color-primary-hover);
  transform: translateY(-1px);
}

.generate-button:active {
  transform: translateY(0);
}

@media (max-width: 768px) {
  .generator-header h1 {
    font-size: 2rem;
  }

  .subtitle {
    font-size: 1rem;
  }

  .generator-content {
    padding: 1.5rem;
  }

  .generator-container {
    padding: 1rem;
  }
}
</style>