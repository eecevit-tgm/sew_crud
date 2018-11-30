import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Ping from '@/components/Ping';
import User from '@/components/User'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'User',
      component: User,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping
    }
  ],
  mode: 'history',
})
