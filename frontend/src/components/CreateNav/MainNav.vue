<template>
    <div>
     <NavList :buttons="buttons" :baseStyle="baseStyle"/>
    </div>
</template>

  
  <script>
  import {ref} from 'vue'
  import NavList from '@/components/CreateNav/NavList.vue'
  import menuData from "@/data/nav.json";

  export default {
    name: 'HomePage',
    components:{
      NavList,
    },
    props:{
        baseStyle:Object,
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
      return {buttons}
  }
  }
  </script>

<style scoped>
div
{
  width: 90%;
  position: relative;
  left:-2%;
}
</style>
  