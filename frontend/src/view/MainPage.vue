<template>
  <div class="container-fluid home">
    <div class="row justify-content-center align-items-center vh-100">
      <div class="col-md-4">
        <div class="button-container">
          <MainNav lang="pl" nav="main"/>
        </div>
      </div>
    </div>
  </div>
</template>

  
  <script>
  import MainNav from '@/components/MainNav.vue';

  export default {
    name: 'HomePage',
    components:{
      MainNav,
    },
  }
  </script>

<style scoped>
.home {
  background-image: url('@/assets/image/backgrounds/background-home.svg');
  background-size: cover;
}
.button-container {
  padding: 20px;
  border-radius: 5px;
  text-align: center;
  width: 100%;
}
</style>
  