import { predict } from './predictor'

const MAX_STORAGE_SIZE = 10 * 1024 * 1024 // 5 MB

function canStoreModel(modelJson: string): boolean {
  try {
    const currentSize = JSON.stringify(localStorage).length
    const newSize = modelJson.length
    return (currentSize + newSize) < MAX_STORAGE_SIZE
  } catch {
    return false
  }
}

function safeStoreModel(model: any): void {
  try {
    const modelJson = JSON.stringify(model)
    if (canStoreModel(modelJson)) {
      localStorage.setItem('trainedModel', modelJson)
    } else {
      console.warn('Model too large to store in localStorage')
      // Optionally clear old data and retry
      localStorage.removeItem('trainedModel')
      localStorage.setItem('trainedModel', modelJson)
    }
  } catch (e) {
    if (e instanceof DOMException && e.code === 22) {
      console.error('localStorage quota exceeded, clearing old model')
      localStorage.removeItem('trainedModel')
      try {
        localStorage.setItem('trainedModel', JSON.stringify(model))
      } catch {
        console.error('Still cannot store model after clearing')
      }
    }
  }
}

export async function fetchPrediction(prompt: string): Promise<string> {
  return predict(prompt)
}

export async function fetchAlternatives(): Promise<{ id: string, label: string }[]> {
  const response = await fetch('/api/available-features/')
  if (!response.ok) throw new Error('Could not fetch available features')
  const data = await response.json()
  return data.features
}

export async function fetchSkillTree(): Promise<Record<string, any>> {
  const response = await fetch('/api/skill-tree/')
  if (!response.ok) throw new Error('Could not fetch skill tree')
  const data = await response.json()
  
  function toD3Tree(name: string, node: any): any {
    return {
      name,
      status: node.status,
      children: Object.entries(node.children || {}).map(([childName, childNode]) =>
        toD3Tree(childName, childNode)
      )
    }
  }

  const [rootKey, rootNode] = Object.entries(data.tree)[0];
  return toD3Tree(rootKey, rootNode);
}



export async function addFeatureToConfig(featureId: string): Promise<void> {
  const model = JSON.parse(localStorage.getItem('trainedModel') || 'null')

  const response = await fetch('/api/add-feature/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ feature_id: featureId, model }),
  })

  if (!response.ok) throw new Error('Add feature API error')

  const data = await response.json()
  if (data.model) {
    safeStoreModel(data.model)
  }
}

export async function removeFeatureFromConfig(featureId: string): Promise<string[]> {
  const model = JSON.parse(localStorage.getItem('trainedModel') || 'null')
  const response = await fetch('/api/remove-feature/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ feature_id: featureId, model }),
  })
  
  if (!response.ok) throw new Error('Remove feature API error')

  const data = await response.json()
  if (data.model) {
    safeStoreModel(data.model)
  }
  return data.removed_features
}

export async function fetchBooksDataset() {
  const response = await fetch(`/api/books-dataset/`, {
    credentials: 'include'
  })
  if (!response.ok) throw new Error('Failed to fetch books')
  return response.json()
}

export async function setCorpus(bookIds: string[]) {
  const response = await fetch(`/api/set-corpus/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify({ ids: bookIds })
  })
  if (!response.ok) throw new Error('Failed to set corpus')

  const data = await response.json()
  if (data.model) {
    safeStoreModel(data.model)
  }
  return data
}