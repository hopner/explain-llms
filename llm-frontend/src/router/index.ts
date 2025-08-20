import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Builder from '../views/Builder.vue'
import Explain from '../views/Explain.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'Overvie', component: HomeView },
    { path: '/builder', name: 'Builder', component: Builder },
    { path: '/explain/:strategy', name: 'Explain', component: Explain },
  ]
})
