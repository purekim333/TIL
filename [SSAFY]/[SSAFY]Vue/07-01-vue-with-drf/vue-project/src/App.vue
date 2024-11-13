<template>
  <header>
    <nav>
      <RouterLink :to="{name: 'ArticleView'}" >Article</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
</style>
