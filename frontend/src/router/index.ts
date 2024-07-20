import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ExpensesView from '../views/ExpensesView.vue'
import AttendeesView from '../views/AttendeesView.vue'
import ExpensesHeader from '../components/headers/ExpensesHeader.vue'
import HomeHeader from '../components/headers/HomeHeader.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      components: {
        default: HomeView,
        Header: HomeHeader
      }
    },
    {
      path: '/expenses',
      name: 'expenses',
      components: {
        default: ExpensesView,
        Header: ExpensesHeader
      }
    },
    {
      path: '/attendees',
      name: 'attendees',
      component: AttendeesView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
