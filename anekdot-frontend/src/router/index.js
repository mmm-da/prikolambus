import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/anek',
    name: 'Anekdot',
    component: () => import('../views/Anek.vue')
  },
  {
    path: '/reg',
    name: 'reg',
    component: () => import('../views/Reg.vue')
  },
  {
    path: '/gen',
    name: 'gen',
    component: () => import('../views/GenerateAnek.vue')
  },
  {
    path: '/best',
    name: 'Best anekdots',
    component: () => import('../views/BestAneks.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
