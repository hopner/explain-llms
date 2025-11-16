export function featureToRoute(featureId: string): string {
    const id = String(featureId).toLowerCase().trim()
    const map: Record<string, string> = {
        '1gram': 'OneGram',
        'onegram': 'OneGram',
        '1-gram': 'OneGram',
        // add more mappings here:
        // 'someFeatureId': 'RouteName',
    }
    // try exact match, then fallback by contains
    if (map[id]) return map[id]
    return 'Example'
}