import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import Displayer_srch from '@/views/Displayer_srch.vue'
import SQL_typing from '@/views/SQL_typing.vue'
import NotFound from '@/views/NotFound.vue'
import dynascan_main_db from '@/views/dynascan_main_db.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name:'home',
      component: HomeView
    },
    {
      path:'/about',
      name:'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AboutView
    },
    {
      path:'/displayer_srch',
      name:'displayer_srch',
      component: Displayer_srch
    },
    {
      path:'/sql_typing',
      name:'sql_typing',
      component: SQL_typing

    },
    {
      path:'/dynascan_main_db',
      name:'dynascan_main_db',
      component: dynascan_main_db
    },
    {
      path:'/:catchAll(.*)',
      name:'notfound',
      component: NotFound
    }
  ]
})

export default router
