<template>
    <div>
     <NavList :buttons="buttons" />
    </div>
</template>

  
  <script>
  import {ref} from 'vue'
  import NavList from '@/components/NavList.vue'
  import menuData from "@/data/nav.json";

  export default {
    name: 'HomePage',
    components:{
      NavList,
    },
    props:{
        lang:{
            type:String,
            required:true
        },
        nav:{
            type:String,
            required:true
        }
    },
    setup(props){
      const buttons = ref(menuData[props.lang][props.nav].buttons) || null;
      console.log(buttons);
      return {buttons}
  }
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
  