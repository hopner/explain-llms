import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Builder from '../views/Builder.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'Overvie', component: HomeView },
    { path: '/builder', name: 'Builder', component: Builder },
  ]
})
