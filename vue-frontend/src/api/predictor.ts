export async function predict(prompt: string): Promise<string> {
  const model = JSON.parse(localStorage.getItem('trainedModel') || 'null')

  if (model && (model.counts || model.vocab || model.vocabulary)) {
    try {
      if (model.counts) {
        const tokenizerType = model.tokenizer || model.tokenizer_type || 'whitespace'
        const tokens = await tokenize(prompt, tokenizerType)
        return localNGramPredictFromTokens(tokens, model)
      }
      if (model.vocab || model.vocabulary) {
        const vocab = model.vocab || model.vocabulary
        if (Array.isArray(vocab) && vocab.length) {
          return randomFromArray(vocab)
        }
      }
    } catch (e) {
      console.warn('Local prediction failed, falling back to server', e)
    }
  }

  const response = await fetch('/api/predict/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  })
  if (!response.ok) throw new Error('Prediction API error')
  const data = await response.json()
  if (data.model) {
    localStorage.setItem('trainedModel', JSON.stringify(data.model))
  }
  return data.prediction
}

async function tokenize(text: string, tokenizerType: string | undefined): Promise<string[]> {
  const response = await fetch('/api/tokenize/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt: text, tokenizer_type: tokenizerType }),
  })
  if (!response.ok) {
    console.warn('Remote tokenization failed, falling back to whitespace tokenization')
    return text.trim() ? text.trim().split(/\s+/) : []
  }
  const data = await response.json()
  return Array.isArray(data.tokens) ? data.tokens : []
}

function localNGramPredictFromTokens(tokens: string[], model: any): string {
  const depth = typeof model.ngram === 'number' ? model.ngram : inferDepthFromCounts(model.counts)
  if (!tokens.length) {
    const vocab = collectVocabularyFromCounts(model.counts)
    return randomFromArray(vocab) || ''
  }

  for (let d = Math.min(depth, tokens.length); d >= 1; d--) {
    const key = tokens.slice(-d).join(' ')
    const countsLevel = model.counts?.[String(d)] || model.counts?.[d]
    if (!countsLevel) continue
    const options = countsLevel[key]
    if (options && Object.keys(options).length) {
      // choose most frequent (deterministic)
      const entries = Object.entries(options as Record<string, number>) as [string, number][]
      const best = entries.reduce((a, b) => (b[1] > a[1] ? b : a), ['', 0])
      return String(best[0])
    }
  }

  const vocab = collectVocabularyFromCounts(model.counts)
  return randomFromArray(vocab) || ''
}

function inferDepthFromCounts(counts: any): number {
  if (!counts) return 1
  const keys = Object.keys(counts)
  const numeric = keys.map(k => parseInt(k, 10)).filter(n => !Number.isNaN(n))
  return numeric.length ? Math.max(...numeric) : 1
}

function collectVocabularyFromCounts(counts: any): string[] {
  const vocab = new Set<string>()
  if (!counts) return []
  for (const levelKey of Object.keys(counts)) {
    const level = counts[levelKey]
    if (!level) continue
    for (const nextMap of Object.values(level)) {
      if (typeof nextMap === 'object' && nextMap !== null) {
        for (const tok of Object.keys(nextMap)) vocab.add(tok)
      }
    }
  }
  return Array.from(vocab)
}

function randomFromArray<T>(arr: T[]): T | '' {
  if (!arr || !arr.length) return '' as any
  return arr[Math.floor(Math.random() * arr.length)]
}