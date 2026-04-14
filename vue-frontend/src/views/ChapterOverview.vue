<script setup lang="ts">
import { useRouter } from 'vue-router'
import { CHAPTERS, CHAPTER_CATEGORIES, type ChapterCategory } from '../data/chapters'

const router = useRouter()

const backToHome = () => {
    router.push({ name: 'Home' })
}

type OverviewItem =
    | { type: 'internal'; id: keyof typeof CHAPTERS; title: string; description: string; routeName: string }
    | { type: 'external'; title: string; description: string; url: string }

type OverviewCategory = {
    title: string
    description: string
    items: OverviewItem[]
}

const externalLinks: OverviewItem[] = [
  {
    type: 'external',
    title: 'Transformer Explainer',
    description:
      'Want a closer look on how LLMs really work? This visualization shows the inner workings of a transformer model in an interactive way.',
    url: 'https://poloclub.github.io/transformer-explainer/',
  },
  {
    type: 'external',
    title: "A Student's Guide to Not Writing with ChatGPT",
    description:
      "This article provides arguments against OpenAI's reasons for why students should use ChatGPT for writing assignments, and offers alternative perspectives on the issue.",
    url: 'https://www.arthurperret.fr/blog/2024-11-14-student-guide-not-writing-with-chatgpt.html',
  },
  {
    type: 'external',
    title: 'LLMs Explained Briefly by 3Blue1Brown',
    description:
      'This video by 3Blue1Brown provides a brief and intuitive explanation of how large language models work, using visualizations and analogies to make the concepts more accessible.',
    url: 'https://www.youtube.com/watch?v=LPZh9BOjkQs',
  },
  {
    type: 'external',
    title: 'Interactive Essays on Machine Learning Topics',
    description:
      'This collection of interactive essays by Google provides in-depth explanations of various machine learning topics.',
    url: 'https://pair.withgoogle.com/explorables/',
  },
  {
    type: 'external',
    title: 'How GPT models work by Bea Stollnitz',
    description:
      'This blog post by Bea Stollnitz provides a brief and effective explanation of how GPT models work. She also has a more technical version for data scientists and engineers.',
    url: 'https://bea.stollnitz.com/blog/how-gpt-works/',
  },
  {
    type: 'external',
    title: 'The Bullshit Machines by Bergstrom and West',
    description:
      'This is more detailed course on the inner workings of LLMs aimed at a non-technical audience.',
    url: 'https://thebullshitmachines.com',
  },
  {
    type: 'external',
    title: 'Save the AI',
    description:
      'This website provides information on the environmental impact of LLMs.',
    url: 'https://savethe.ai/',
  },
]

const categories: OverviewCategory[] = [
    ...CHAPTER_CATEGORIES.map((category: ChapterCategory) => ({
        title: category.title,
        description: category.description,
        items: category.chapterIds.map((id) => ({
            type: 'internal' as const,
            id,
            title: CHAPTERS[id].title,
            description: CHAPTERS[id].description,
            routeName: CHAPTERS[id].routeName,
        })),
    })),
    {
        title: 'Further Reading',
        description: 'External resources for deeper study.',
        items: externalLinks,
    }
]

const goTo = (item: OverviewItem) => {
    if (item.type === 'internal') {
        router.push({ name: item.routeName, query: { from: 'overview' } })
    } else {
        window.open(item.url, '_blank', 'noopener,noreferrer')
    }
}
</script>

<template>
    <div class="overview-page">
        <header class="overview-header">
            <div class="header-actions">
                <button class="back-button" @click="backToHome">← Home</button>
            </div>
            <h1>Chapter Overview</h1>
            <p>Explore the chapters and deepen your understanding with curated resources.</p>
        </header>

        <main class="overview-content">
            <section v-for="category in categories" :key="category.title" class="category">
                <div class="category-header">
                    <h2>{{ category.title }}</h2>
                    <p>{{ category.description }}</p>
                </div>

                <div class="category-grid">
                    <button v-for="item in category.items" :key="item.title" class="overview-card" @click="goTo(item)">
                        <div class="card-title">{{ item.title }}</div>
                        <div class="card-description">{{ item.description }}</div>
                        <div class="card-meta">
                            <span v-if="item.type === 'internal'">Open chapter →</span>
                            <span v-else>Open link ↗</span>
                        </div>
                    </button>
                </div>
            </section>
        </main>
    </div>
</template>

<style scoped>
.overview-page {
    min-height: 100vh;
    background: var(--color-bg-primary);
    color: var(--color-text);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
}

.overview-header {
    padding: 3rem 2rem 2rem;
    border-bottom: 1px solid var(--color-primary-15);
    background: var(--color-bg-secondary);
    text-align: center;
}

.header-actions {
    display: flex;
    justify-content: flex-start;
    margin-bottom: 1.5rem;
}

.back-button {
    background: var(--color-primary);
    color: var(--color-bg-primary);
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 0.6rem;
    cursor: pointer;
    font-weight: 600;
    transition: background 0.2s ease;
}

.back-button:hover {
    background: var(--color-primary-hover);
}

.overview-header h1 {
    margin: 0 0 0.75rem;
    font-size: 2.75rem;
    color: var(--color-primary);
}

.overview-header p {
    margin: 0 auto;
    max-width: 720px;
    font-size: 1.1rem;
    color: var(--color-text);
}

.overview-content {
    padding: 2.5rem 2rem 4rem;
    display: flex;
    flex-direction: column;
    gap: 2.5rem;
}

.category {
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
}

.category-header h2 {
    margin: 0 0 0.4rem;
    font-size: 1.8rem;
    color: var(--color-text);
}

.category-header p {
    margin: 0;
    color: var(--color-primary);
}

.category-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.25rem;
}

.overview-card {
    background: var(--color-white);
    border: 1px solid var(--color-primary-15);
    border-radius: 1rem;
    padding: 1.5rem;
    text-align: left;
    cursor: pointer;
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
    box-shadow: 0 6px 18px var(--color-text-08);
}

.overview-card:hover {
    transform: translateY(-4px);
    border-color: var(--color-primary-60);
    box-shadow: 0 12px 26px var(--color-text-12);
}

.card-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--color-text);
}

.card-description {
    margin-top: 0.5rem;
    font-size: 0.95rem;
    color: var(--color-primary);
}

.card-meta {
    margin-top: 1rem;
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--color-accent);
}

@media (max-width: 768px) {
    .overview-header h1 {
        font-size: 2.2rem;
    }

    .overview-content {
        padding: 2rem 1.5rem 3rem;
    }
}
</style>