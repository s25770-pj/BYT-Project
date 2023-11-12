<template>
  <div>
    <NavList :buttons="buttons" :baseStyle="baseStyle" :class="classNav"/>
  </div>
</template>

  
  <script>
  import {ref} from 'vue'
  import NavList from './NavList.vue'
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
        },
        classNav:{
          type:Array
        }
    },
    setup(props){
      const buttons = ref(menuData[props.lang][props.nav].buttons) || null;
      return {buttons}
  }
  }
  </script>
  