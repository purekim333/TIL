<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <RouterLink
      :to="{name: 'DetailView',
        params: { id: article.id }
      }"
    >Detail
    </RouterLink>
  </div>
</template>

<script setup>
defineProps({
  article: Object
})

import { RouterView, RouterLink } from 'vue-router';
</script>
