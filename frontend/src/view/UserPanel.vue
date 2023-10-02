<template>
  <div class="panel vh-100">
  
  
  <UserNav lang="pl" nav="user"/>
  <MainFooter/>
  </div>
  
</template>

<script>
import MainFooter from '@/components/MainFooter.vue';
import UserNav from '@/components/UserNav.vue';
export default {
    name: 'UserPanel',
    components:{
        MainFooter,
        UserNav
    }
}
</script>

<style scope>
.panel {
  background-image: url('@/assets/image/backgrounds/background-panel.svg');
  background-size: cover;
}
</style>