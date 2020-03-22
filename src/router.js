import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: '',
    routes: [
      {
        path: '/',
        name: 'home',
        component: () => import(/* webpackChunkName: "about" */ './components/Dashboard.vue')
      },
      {
        path: '/agreement',
        name: 'agreement',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ './components/Agreement.vue')
      },      
      {
        path: '/agreement/:id',
        name: 'agreement-card',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ './components/Card.vue')
      },
      {
        path: '/load-manager',
        name: 'load-manager',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ './components/LoadManager.vue')
      }
    ]
  })