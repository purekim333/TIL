<template>
  <div>
    <RouterLink :to="{ name: 'user-profile' }">Profile</RouterLink>
    <RouterLink :to="{ name: 'user-posts' }">Posts</RouterLink>
    <h1>UserView</h1>
    <h2>{{  userId }}번 User 페이지</h2>
    <button @click="goHome"> 홈으로! </button>
    <hr>
    <RouterView />
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';
import { ref } from 'vue'

const route = useRoute()
const router = useRouter()
const userId = ref(route.params.id)
const goHome = function () {
  router.push({name:'home'})
  // router.replace({name:'home'})
}
</script>

<style scoped>

</style>