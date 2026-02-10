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
  slidesSrc: string
  nextPage?: string
  contentFile: string
}

export type ChapterStep = {
  title: string
  text: string
  slide: number
}

export type ChapterContent = ChapterMeta & {
  steps: ChapterStep[]
}

export const CHAPTERS: Record<ChapterId, ChapterMeta> = {
  intro: {
    id: 'intro',
    title: 'Intro',
    description: 'How to use the building page.',
    routeName: 'Intro',
    slidesSrc: '/slides/Intro.html',
    nextPage: '/builder',
    contentFile: '/content/intro.md',
  },
  read_book: {
    id: 'read_book',
    title: 'Read Book',
    description: 'Turning text into a clean training corpus.',
    routeName: 'ReadBook',
    slidesSrc: '/slides/ReadBook.html',
    nextPage: '/builder',
    contentFile: '/content/read_book.md',
  },
  more_data: {
    id: 'more_data',
    title: 'Add More Data',
    description: 'How data size impacts results.',
    routeName: 'MoreData',
    slidesSrc: '/slides/MoreData.html',
    nextPage: '/builder',
    contentFile: '/content/more_data.md',
  },
  weighted_random: {
    id: 'weighted_random',
    title: 'Introduce Randomness',
    description: 'Make more varied predictions based on token distributions.',
    routeName: 'WeightedRandom',
    slidesSrc: '/slides/weighted_random.html',
    nextPage: '/builder',
    contentFile: '/content/weighted_random.md',
  },
  onegram: {
    id: 'onegram',
    title: 'UniGram',
    description: 'Unigram model and token frequency.',
    routeName: 'OneGram',
    slidesSrc: '/slides/OneGram.html',
    nextPage: '/builder',
    contentFile: '/content/onegram.md',
  },
  digram: {
    id: 'digram',
    title: 'DiGram',
    description: 'Bigrams for local context.',
    routeName: 'DiGram',
    slidesSrc: '/slides/DiGram.html',
    nextPage: '/builder',
    contentFile: '/content/digram.md',
  },
  trigram: {
    id: 'trigram',
    title: 'TriGram',
    description: 'Trigrams for richer context.',
    routeName: 'TriGram',
    slidesSrc: '/slides/TriGram.html',
    nextPage: '/builder',
    contentFile: '/content/trigram.md',
  },
  tokenization: {
    id: 'tokenization',
    title: 'Tokenization',
    description: 'How text becomes tokens.',
    routeName: 'Tokenization',
    slidesSrc: '/slides/Tokenization.html',
    nextPage: '/builder',
    contentFile: '/content/tokenization.md',
  },
  nltk: {
    id: 'nltk',
    title: 'Language-Aware Tokenization',
    description: 'Make the tokenization better by making it language aware.',
    routeName: 'NLTK',
    slidesSrc: '/slides/nltk.html',
    nextPage: '/builder',
    contentFile: '/content/nltk.md',
  },
  builder: {
    id: 'builder',
    title: 'Builder',
    description: 'Compose improvements interactively.',
    routeName: 'Builder',
    slidesSrc: '',
    contentFile: '',
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

/**
 * Load chapter content from markdown file
 * @param chapterId - The ID of the chapter to load
 * @returns Promise resolving to chapter with steps
 */
export async function loadChapterContent(chapterId: ChapterId): Promise<ChapterContent> {
  const chapter = CHAPTERS[chapterId]
  if (!chapter) {
    throw new Error(`Chapter '${chapterId}' not found`)
  }

  if (!chapter.contentFile) {
    throw new Error(`Chapter '${chapterId}' has no content file`)
  }

  const response = await fetch(chapter.contentFile)
  const markdown = await response.text()
  
  // Parse front-matter style markdown
  // Format: ---\nslide: N\n---\nContent\n---\nslide: N+1\n---\nContent...
  const steps: ChapterStep[] = []
  
  // Split by --- and process in pairs (front-matter + content)
  const parts = markdown.split(/\n?---\n?/).filter(s => s.trim())
  
  for (let i = 0; i < parts.length; i += 2) {
    const frontMatter = parts[i]
    const content = parts[i + 1] || ''
    
    let title = ''
    let slide = Math.floor(i / 2)
    
    // Parse front-matter
    const fmLines = frontMatter.trim().split('\n')
    for (const line of fmLines) {
      if (line.startsWith('slide:')) {
        slide = parseInt(line.split(':')[1].trim())
      } else if (line.startsWith('title:')) {
        title = line.split(':').slice(1).join(':').trim()
      }
    }
    
    steps.push({ title, text: content.trim(), slide })
  }

  return {
    ...chapter,
    steps,
  }
}
