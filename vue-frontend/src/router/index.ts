import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Builder from '../views/Builder.vue'
import ExampleChapter from '../views/ExampleChapter.vue'
import OneGram from '../views/chapters/OneGram.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'Overview', component: HomeView },
    { path: '/builder', name: 'Builder', component: Builder },
    { path: '/example', name: 'Example', component: ExampleChapter },
    { path: '/chapters/onegram', name: 'OneGram', component: OneGram }
  ]
})
