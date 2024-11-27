import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // DRF로 전체 게시글 요청을 보내고 응답을 받아 articles에 저장하는 함수
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        // console.log(res.data)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  //회원가입 요청 액션
  const signUp = function (payload) {
    // const username = payload.username
    // const password1 = payload.password1
    // const password2 = payload.password2

    const {username, password1, password2} = payload

    axios({
      method: 'POST',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
    .then((res) => {
      console.log(res.data)
    })
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'POST',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
    .then((res) => {
      token.value = res.data.key
      console.log(res.data)
      router.
    })
  }
  
  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin }
}, { persist: true })
