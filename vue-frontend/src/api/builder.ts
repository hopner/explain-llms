export async function fetchPrediction(prompt: string): Promise<string> {
  const response = await fetch('/api/predict/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  })
  if (!response.ok) throw new Error('Prediction API error')
  const data = await response.json()
  return data.prediction
}
export async function fetchAlternatives(): Promise<{ id: string, label: string }[]> {
  return [
    { id: 'feature1', label: 'Feature 1' },
    { id: 'feature2', label: 'Feature 2' }
  ]

}

export async function addFeatureToConfig(featureId: string): Promise<void> {
  console.log(`Feature ${featureId} added to config`)
}
