<template>
  <div :class="viewStyle">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  data(){
        return{
            viewStyle:["h-100" ,"w-100"]
        }
    }
};
</script>