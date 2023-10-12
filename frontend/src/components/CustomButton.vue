<template>
    <router-link :to="button.to" :class="button.class">
      <img :src="icons[button.icon.src]" :alt="button.icon.alt" v-show="button.icon.src" :class="button.icon.class">
      <span>{{ button.text }}</span>
  </router-link>
</template>

<script>
const requireIcon = require.context('@/assets/icons', false, /\.png$/);
const icons = {};



export default {
  props: {
    button:{
      type: Object,
      required:true
    }, 
  },setup(){
    requireIcon.keys().forEach((filename) => {
      const iconName = filename.replace(/^\.\/(.*)\.\w+$/, '$1');
      icons[iconName] = requireIcon(filename);
    });
    return {icons}
  }
};
</script>

<style scoped>
*{
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
.btn:hover
{
  border-color: #3b39cb;
  background-color: #3634b9;
  transform: scale(1.015);
  color:#fff;
}
.btn-custom {
  color:#efefef;
  border: #3634b980 5px solid;
  margin: 10px 0;
  padding: 20px;
  width: 100%;
  background-color: #3b39cb;
  transition: all 0.5s ease-in-out;
}
.icon
{
  margin: 10px 0;
  padding: 2px;
  width: 3em;
  height: 3em;
}
.icon_min
{
  width: 2em;
  height: 2em;
}
</style>
