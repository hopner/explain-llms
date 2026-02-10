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
        title: 'Test',
        description: 'This is a test link.',
        url: 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
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
    background: #F5FBE6;
    color: #233D4D;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
}

.overview-header {
    padding: 3rem 2rem 2rem;
    border-bottom: 1px solid rgba(33, 94, 97, 0.15);
    background: #f0f7e6;
    text-align: center;
}

.header-actions {
    display: flex;
    justify-content: flex-start;
    margin-bottom: 1.5rem;
}

.back-button {
    background: #215E61;
    color: #F5FBE6;
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 0.6rem;
    cursor: pointer;
    font-weight: 600;
    transition: background 0.2s ease;
}

.back-button:hover {
    background: #1a4a4d;
}

.overview-header h1 {
    margin: 0 0 0.75rem;
    font-size: 2.75rem;
    color: #215E61;
}

.overview-header p {
    margin: 0 auto;
    max-width: 720px;
    font-size: 1.1rem;
    color: #233D4D;
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
    color: #233D4D;
}

.category-header p {
    margin: 0;
    color: #215E61;
}

.category-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.25rem;
}

.overview-card {
    background: #ffffff;
    border: 1px solid rgba(33, 94, 97, 0.15);
    border-radius: 1rem;
    padding: 1.5rem;
    text-align: left;
    cursor: pointer;
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
    box-shadow: 0 6px 18px rgba(35, 61, 77, 0.08);
}

.overview-card:hover {
    transform: translateY(-4px);
    border-color: rgba(254, 127, 45, 0.6);
    box-shadow: 0 12px 26px rgba(35, 61, 77, 0.12);
}

.card-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #233D4D;
}

.card-description {
    margin-top: 0.5rem;
    font-size: 0.95rem;
    color: #215E61;
}

.card-meta {
    margin-top: 1rem;
    font-size: 0.85rem;
    font-weight: 600;
    color: #FE7F2D;
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