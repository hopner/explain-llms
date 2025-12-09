export function featureToRoute(featureId: string): string {
    const id = String(featureId).toLowerCase().trim()
    const map: Record<string, string> = {
        '1gram': 'OneGram',
        'onegram': 'OneGram',
        '1-gram': 'OneGram',
        '2gram': 'DiGram',
        'digram': 'DiGram',
        '2-gram': 'DiGram',
        '3gram': 'TriGram',
        'trigram': 'TriGram',
        '3-gram': 'TriGram',
        'readbook': 'ReadBook',
        'read-book': 'ReadBook',
        'read_book': 'ReadBook',
        'read_another': 'MoreData',
        'tokenization': 'Tokenization'
        
    }
    if (map[id]) return map[id]
    return 'Example'
}