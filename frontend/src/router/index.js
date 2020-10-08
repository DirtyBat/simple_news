import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import NewsDetail from '@/components/NewsDetail'
import Edit from '@/components/Edit'
import Admin from '@/components/Admin'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/news/:id/',
      name: 'NewsDetail',
      component: NewsDetail
    },
    {
      path: '/edit/:id/',
      name: 'Edit',
      component: Edit
    },{
      path: '/admin',
      name: 'Admin',
      component: Admin
    },
  ]
  ]
})
