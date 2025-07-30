import { createRouter, createWebHistory } from 'vue-router'
import Builder from '../views/Builder.vue'
import Explain from '../views/Explain.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'Builder', component: Builder },
    { path: '/explain/:strategy', name: 'Explain', component: Explain },
  ]
})
