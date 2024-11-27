import { createRouter, createWebHistory } from 'vue-router'

// Views
import HomeView from '@/views/HomeView.vue'

// account 기능
import ChangePasswordView from '@/views/accounts/ChangePasswordView.vue'
import FindPasswordView from '@/views/accounts/FindPasswordView.vue'
import LogInView from '@/views/accounts/LoginView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'
import SignUpView from '@/views/accounts/SignUpView.vue'
import EditProfileView from '@/views/accounts/EditProfileView.vue'
import OtherUserProfile from '@/views/accounts/OtherUserProfile.vue'

// 게시글 기능
import ArticleView from '@/views/articles/ArticleView.vue'
import CreateView from '@/views/articles/CreateView.vue'
import DetailView from '@/views/articles/DetailView.vue'
import UpdateView from '@/views/articles/UpdateView.vue'

// etc 기능
import MapView from '@/views/etc/MapView.vue'
import ExchangeView from '@/views/etc/ExchangeView.vue'
import NewsHomeView from '@/views/etc/NewsHomeView.vue'
import NotFoundView from '@/views/etc/NotFoundView.vue'

// finance 기능
import Favorites from '@/views/finance/FavoritesView.vue'
import FinanceView from '@/views/finance/FinanceView.vue'
import DepositView from '@/views/finance/deposit/DepositView.vue'
import DepositDetailView from '@/views/finance/deposit/DepositDetailView.vue'
import SavingView from '@/views/finance/saving/SavingView.vue'
import SavingDetailView from '@/views/finance/saving/SavingDetailView.vue'

// portfolio 기능
import PortfolioCreateView from '@/views/portfolios/PortfolioCreateView.vue'
import RecommendationView from '@/views/portfolios/RecommendationView.vue'
import DepositPortDetailView from '@/views/portfolios/DepositPortDetailView.vue'
import SavingPortDetailView from '@/views/portfolios/SavingPortDetailView.vue'

import { useAccountStore } from '@/stores/accounts'

// 라우터 설정
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // 홈 화면
    {
      path: '/',
      name: 'HomeView',
      component: HomeView,
    },
    // 로그인
    {
      path: '/accounts/auth/logIn',
      name: 'LogInView',
      component: LogInView,
    },
    // 회원가입
    {
      path: '/accounts/auth/signup',
      name: 'SignUpView',
      component: SignUpView,
    },
    // 비밀번호 찾기
    {
      path: '/accounts/auth/password/reset',
      name: 'FindPasswordView',
      component: FindPasswordView,
    },
    // 비밀번호 변경
    {
      path: '/accounts/auth/password/change',
      name: 'ChangePasswordView',
      component: ChangePasswordView,
    },
    // 프로필
    {
      path: '/profile',
      name: 'ProfileView',
      component: ProfileView,
    },
    // 회원 정보 수정
    {
      path: '/accounts/edit/',
      name: 'EditProfileView',
      component: EditProfileView,
    },
    // 다른 사람 프로필
    {
      path: '/detail/:username',
      name: 'OtherUserProfile',
      component: OtherUserProfile,
    },
    // 게시판 목록 및 작성
    {
      path: '/articles',
      name: 'ArticleView',
      component: ArticleView,
    },
    // 게시글 수정
    {
      path: '/articles/:id/edit',
      name: 'UpdateView',
      component: UpdateView,
    },
    // 게시글 상세
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView,
    },
    // 새 글 작성
    {
      path: '/articles/create',
      name: 'CreateView',
      component: CreateView,
    },
    // 지도
    {
      path: '/map',
      name: 'MapView',
      component: MapView,
    },
    // 환전
    {
      path: '/exchange',
      name: 'ExchangeView',
      component: ExchangeView,
    },
    // 뉴스
    {
      path: '/news',
      name: 'NewsHomeView',
      component: NewsHomeView,
    },
    // 장바구니
    {
      path: '/favorites',
      name: 'FavoritesView',
      component: Favorites,
    },
    //예/적금 조회
    {
      path: '/finance',
      name: 'FinanceView',
      component: FinanceView,
      children: [
        {
          path: 'deposit',
          name: 'DepositView',
          component: DepositView,
        },
        {
          path: 'saving',
          name: 'SavingView',
          component: SavingView,
        },
      ],
    },
    //예금 상품 상세
    {
      path: '/finance/deposit/:product_id',
      name: 'DepositDetailView',
      component: DepositDetailView,
    },
     //적금 상품 상세
    {
      path: '/finance/saving/:product_id',
      name: 'SavingDetailView',
      component: SavingDetailView,
    },
    // 추천 시스템
    {
      path: '/algorithm',
      name: 'AlgorithmView',
      component: () => import('@/views/etc/AlgorithmView.vue'),
    },
    // Not Found
    {
      path: '/:catchAll(.*)',
      name: 'NotFoundView',
      component: NotFoundView,
    },
    // 포트폴리오 생성
    {
      path: '/portfolio/create',
      name: 'PortfolioCreateView',
      component: PortfolioCreateView
    },
    //추천 상품
    {
      path: '/recommendation/:portfolioId',
      name: 'RecommendationView',
      component: RecommendationView
    },
    // 예금 포트폴리오 상세
    {
      path: '/portfolio/:portfolio_id/deposit/:product_id',
      name: 'DepositPortDetailView',
      component: DepositPortDetailView,
    },
    // 적금 포트폴리오 상세
    {
      path: '/portfolio/:portfolio_id/saving/:product_id',
      name: 'SavingPortDetailView',
      component: SavingPortDetailView,
    },
  ],
})

// 기본 라우팅 가드
router.beforeEach((to, from) => {
  const store = useAccountStore()
  const publicPages = ['HomeView', 'ArticleView', 'DetailView', 'LogInView', 'SignUpView']
  const authRequired = !publicPages.includes(to.name)

  if (authRequired && !store.isLogin) {
    window.alert('로그인이 필요한 서비스입니다.')
    return { name: 'LogInView' }
  }

  if ((to.name === 'SignUpView' || to.name === 'LogInView') && store.isLogin) {
    window.alert('이미 로그인 되어있습니다.')
    return { name: 'ArticleView' }
  }
})

export default router
