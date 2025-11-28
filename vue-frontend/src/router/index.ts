import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Intro from '../views/chapters/Intro.vue'
import Builder from '../views/Builder.vue'
import ChapterOverview from '../views/ChapterOverview.vue'
import ExampleChapter from '../views/ExampleChapter.vue'
import OneGram from '../views/chapters/OneGram.vue'
import DiGram from '../views/chapters/DiGram.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'Overview', component: HomeView },
    { path: '/intro', name: 'Intro', component: Intro },
    { path: '/builder', name: 'Builder', component: Builder },
    { path: '/chapter-overview', name: 'ChapterOverview', component: ChapterOverview },
    { path: '/example', name: 'Example', component: ExampleChapter },
    { path: '/chapters/onegram', name: 'OneGram', component: OneGram },
    { path: '/chapters/digram', name: 'DiGram', component: DiGram }
  ]
})
