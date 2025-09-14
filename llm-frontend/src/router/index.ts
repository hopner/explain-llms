import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Builder from '../views/Builder.vue'
import MockChapter from '../views/chapters/MockChapter.vue'
import StickyGraphic2 from '../views/StickyGraphic2.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'Overvie', component: HomeView },
    { path: '/builder', name: 'Builder', component: Builder },
    { path: '/mock-chapter', name: 'MockChapter', component: MockChapter },
    { path: '/sticky-graphic-2', name: 'StickyGraphic2', component: StickyGraphic2 },
  ]
})
