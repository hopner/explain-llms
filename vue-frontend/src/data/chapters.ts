export type ChapterId =
  | 'intro'
  | 'read_book'
  | 'more_data'
  | 'weighted_random'
  | 'onegram'
  | 'digram'
  | 'trigram'
  | 'tokenization'
  | 'nltk'
  | 'builder'

export type ChapterMeta = {
  id: ChapterId
  title: string
  description: string
  routeName: string
}

export const CHAPTERS: Record<ChapterId, ChapterMeta> = {
  intro: {
    id: 'intro',
    title: 'Intro',
    description: 'How to use the building page.',
    routeName: 'Intro',
  },
  read_book: {
    id: 'read_book',
    title: 'Read Book',
    description: 'Turning text into a clean training corpus.',
    routeName: 'ReadBook',
  },
  more_data: {
    id: 'more_data',
    title: 'Add More Data',
    description: 'How data size impacts results.',
    routeName: 'MoreData',
  },
  weighted_random: {
    id: 'weighted_random',
    title: 'Introduce Randomness',
    description: 'Make more varied predictions based on token distributions.',
    routeName: 'WeightedRandom',
  },
  onegram: {
    id: 'onegram',
    title: 'UniGram',
    description: 'Unigram model and token frequency.',
    routeName: 'OneGram',
  },
  digram: {
    id: 'digram',
    title: 'DiGram',
    description: 'Bigrams for local context.',
    routeName: 'DiGram',
  },
  trigram: {
    id: 'trigram',
    title: 'TriGram',
    description: 'Trigrams for richer context.',
    routeName: 'TriGram',
  },
  tokenization: {
    id: 'tokenization',
    title: 'Tokenization',
    description: 'How text becomes tokens.',
    routeName: 'Tokenization',
  },
  nltk: {
    id: 'nltk',
    title: 'Language-Aware Tokenization',
    description: 'Make the tokenization better by making it language aware.',
    routeName: 'NLTK',
  },
  builder: {
    id: 'builder',
    title: 'Builder',
    description: 'Compose improvements interactively.',
    routeName: 'Builder',
  },
}

export type ChapterCategory = {
  title: string
  description: string
  chapterIds: ChapterId[]
}

export const CHAPTER_CATEGORIES: ChapterCategory[] = [
  {
    title: 'Foundations',
    description: 'Introduction to the project and the random model.',
    chapterIds: ['intro'],
  },
  {
    title: 'Data Sampling',
    description: 'Prepare data and sample from distributions.',
    chapterIds: ['read_book', 'more_data', 'weighted_random'],
  },
  {
    title: 'N-gram Models',
    description: 'Build intuition with count-based models.',
    chapterIds: ['onegram', 'digram', 'trigram'],
  },
  {
    title: 'Tokenization',
    description: 'Understand how text is converted to tokens and how to improve it.',
    chapterIds: ['tokenization', 'nltk'],
  },
]

// Map backend feature IDs to frontend chapter IDs
export const FEATURE_TO_CHAPTER: Record<string, ChapterId | null> = {
  'read_book': 'read_book',
  'read_another': 'more_data',
  '1gram': 'onegram',
  '2gram': 'digram',
  '3gram': 'trigram',
  'weighted_random': 'weighted_random',
  'tokenization': 'tokenization',
  'nltk': 'nltk',
  'select_corpus': null, // No chapter for corpus selection
}
