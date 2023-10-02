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
    console.log(icons);
    return {icons}
  }
};
</script>

<style scoped>
.btn:hover
{
  border: #3634b980 2px solid;
}
.btn span
{
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}

.icon
{
  margin: 10px 0;
  padding: 2px;
  width: 2em;
  height: 2em;
}
</style>
