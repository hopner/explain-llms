export async function predict(prompt: string): Promise<string> {
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
