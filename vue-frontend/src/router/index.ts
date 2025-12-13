import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Intro from '../views/chapters/Intro.vue'
import Builder from '../views/Builder.vue'
import ChapterOverview from '../views/ChapterOverview.vue'
import ExampleChapter from '../views/ExampleChapter.vue'
import ReadBook from '../views/chapters/ReadBook.vue'
import MoreData from '../views/chapters/MoreData.vue'
import OneGram from '../views/chapters/OneGram.vue'
import DiGram from '../views/chapters/DiGram.vue'
import TriGram from '../views/chapters/TriGram.vue'
import WeightedRandom from '../views/chapters/WeightedRandom.vue'
import Tokenization from '../views/chapters/Tokenization.vue'
import NLTK from '../views/chapters/NLTK.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'Overview', component: HomeView },
    { path: '/intro', name: 'Intro', component: Intro },
    { path: '/builder', name: 'Builder', component: Builder },
    { path: '/chapter-overview', name: 'ChapterOverview', component: ChapterOverview },
    { path: '/example', name: 'Example', component: ExampleChapter },
    { path: '/chapters/readbook', name: 'ReadBook', component: ReadBook },
    { path: '/chapters/moredata', name: 'MoreData', component: MoreData },
    { path: '/chapters/onegram', name: 'OneGram', component: OneGram },
    { path: '/chapters/digram', name: 'DiGram', component: DiGram },
    { path: '/chapters/trigram', name: 'TriGram', component: TriGram },
    { path: '/chapters/weighted-random', name: 'WeightedRandom', component: WeightedRandom },
    { path: '/chapters/tokenization', name: 'Tokenization', component: Tokenization },
    { path: '/chapters/nltk', name: 'NLTK', component: NLTK }
  ]
})
