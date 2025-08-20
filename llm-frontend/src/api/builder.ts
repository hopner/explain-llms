export async function fetchPrediction(prompt: string): Promise<string> {
  const response = await fetch('http://localhost:8000/api/predict/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  })
  if (!response.ok) throw new Error('Prediction API error')
  const data = await response.json()
  return data.prediction
}
