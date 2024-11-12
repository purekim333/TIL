import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import UserPosts from '@/components/UserPosts.vue'
import UserProfile from '@/components/UserProfile.vue'
import UserHome from '@/components/UserHome.vue'
import LoginView from '@/views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/user/:id',
      // name: 'user',
      component: UserView,
      children: [
        {path: '', name: 'user', component: UserHome },
        {path: 'profile', name: 'user-profile', component: UserProfile },
        {path: 'posts', name: 'user-posts', component: UserPosts},
      ],
      beforeEnter: (to, from) => {
        console.log(to)
        console.log(from)
      }
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    }
  ],
})

// router.beforeEach((to, from) => {
//   const isAuthenticated = false

//   //로그인이 되어있지 않고 이동하고자 하는 페이지가 login이 아니라면
//   if (!isAuthenticated && to.name != 'login'){
//     console.log('로그인이 필요합니다.')
//     return { name: 'login'}
//   }

//   console.log(to)
//   console.log(from)
// })

export default router
