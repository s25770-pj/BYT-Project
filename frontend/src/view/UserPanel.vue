<template>
  <div class="panel vh-100">
    
  <ProgressUser />
  
  <UserNav lang="pl" nav="user"/>
  <div class="contener glass-effect">
    <router-view></router-view>
  </div>
  <MainFooter/>
  </div>
  
</template>

<script>
import MainFooter from '@/components/MainFooter.vue';
import UserNav from '@/components/UserNav.vue';
import ProgressUser from '@/components/ProgressUser.vue';
export default {
    name: 'UserPanel',
    components:{
        MainFooter,
        UserNav,
        ProgressUser
    }
}
</script>

<style scoped>
.panel {
  background-image: url('@/assets/images/backgrounds/background-panel.svg');
  background-size: cover;
}
.contener
{
  position: fixed;
  right: 3%;
  top:10%;
  min-width: 80vw;
  min-height: 80vh;
}
.glass-effect {
  width: 300px;
  height: 300px;
  padding: 20px;
  border-radius: 10px;
  background: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)), 
              linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2));
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: white;
}


</style>