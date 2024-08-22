import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/add',
      name: 'addBooking',
      component: () => import('../views/AddBooking.vue'),
    },
    {
      path: '/all',
      name: 'Bookings',
      component: () => import('../views/BookingList.vue'),
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/Signup.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue'),
    },
    {
      path: '/is_admin',
      name: 'isAdmin',
      component: () => import('../views/IsAdmin.vue'),
    },
    {
      path: '/admin',
      name: 'Admin',
      component: () => import('../views/Admin.vue'),
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // }
  ]
})

export default router
