import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import Displayer_srch from '@/views/Displayer_srch.vue'
import SQL_typing from '@/views/SQL_typing.vue'
import NotFound from '@/views/NotFound.vue'
import sqlWrongRealtime_srch from '@/views/sqlWrongrealtime_srch.vue'
import sqlMainDisplayer from '@/views/sqlMaindisplayer.vue'
import sqlDisplayerRun from '@/views/sqlDisplayerRun.vue'
import sqlDisplayer_inconsistent from '@/views/sqlDisplayer_inconsistent.vue'
import sqlModelDifferent from '@/views/sqlModelDifferent.vue'
import sqlNewDisplayTable from '@/views/sqlNewDisplayTable.vue'
import sqlDuplicate_alarm_event from '@/views/sqlDuplicate_alarm_event.vue'
import DisplayerNav from '@/views/Nav_Displayer.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name:'home',
      component: HomeView
    },
    {
      path:'/DisplayerNav',
      name:'DisplayerNav',
      component: DisplayerNav
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
      path:'/sqlDuplicate_alarm_event',
      name:'sqlDuplicate_alarm_event',
      component: sqlDuplicate_alarm_event
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
      path:'/sqlDisplayer_inconsistent',
      name:'sqlDisplayer_inconsistent',
      component: sqlDisplayer_inconsistent
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
      path:'/SQL_typing',
      name:'SQL_typing',
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
