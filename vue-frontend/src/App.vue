<script setup lang="ts">
import { onMounted } from 'vue';
import { getUserId } from './api/user';

onMounted(async () => {
  const userGuid = await getUserId()
  console.log('User GUID:', userGuid)
})
</script>

<template>
  <router-view />
</template>

<style scoped>

</style>
