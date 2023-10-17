<template>
  <div class="container-fluid home">
    <div class="row justify-content-center align-items-center vh-100">
      <div class="col-md-5">
        <div class="button-container">
          <MainNav lang="pl" nav="main" :baseStyle="baseStyle"/>
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
    setup()
    {
      return {
        baseStyle:{
          btn:{
            margin: '10px 0',
            padding: '20px',
            width: '100%'
          },
          img:{
            position:'relative',
            left:'-2em'
          }
        }
      }
    }
  }
  </script>

<style scoped>
.home {
  background-image: url('@/assets/images/backgrounds/background-home.svg');
  background-size: cover;
}
</style>