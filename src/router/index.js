import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import Displayer_srch from '@/views/Displayer_srch.vue'
import SQL_typing from '@/views/SQL_typing.vue'
import NotFound from '@/views/NotFound.vue'
import sqlWrongRealtime_srch from '@/views/sqlWrongrealtime_srch.vue'
import sqlMainDisplayer from '@/views/sqlMaindisplayer.vue'
import sqlDisplayerRun from '@/views/sqlDisplayerRun.vue'
import sqlDisplayerRealtime from '@/views/sqldisplayerRealtime.vue'
import sqlModelDifferent from '@/views/sqlModelDifferent.vue'
import sqlNewDisplayTable from '@/views/sqlNewDisplayTable.vue'

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
      path:'/sqlwrongrealtime_srch',
      name:'sqlwrongrealtime_srch',
      component: sqlWrongRealtime_srch
    },
    {
      path:'/sqlMaindisplayer',
      name:'sqlMaindisplayer',
      component: sqlMainDisplayer
    },
    {
      path:'/sqlDisplayerRun',
      name:'sqlDisplayerRun',
      component: sqlDisplayerRun
    },
    {
      path:'/sqlDisplayerRealtime',
      name:'sqlDisplayerRealtime',
      component: sqlDisplayerRealtime
    },
    {
      path:'/sqlModelDifferent',
      name:'sqlModelDifferent',
      component: sqlModelDifferent
    },
    {
      path:'/sqlNewDisplayTable',
      name:'sqlNewDisplayTable',
      component: sqlNewDisplayTable
    },
    {
      path:'/sql_typing',
      name:'sql_typing',
      component: SQL_typing

    },
    {
      path:'/:catchAll(.*)',
      name:'notfound',
      component: NotFound
    }
  ]
})

export default router
