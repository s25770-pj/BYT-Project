<template>
  <div class="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>
<style scoped>
.app
{
  background-image: var(--mainPage);
  background-size: cover;
  height:var(--page-height);
  overflow: auto;
}
</style>