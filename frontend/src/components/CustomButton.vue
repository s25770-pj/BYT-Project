<template>
  <button :class="button.class" :disabled="button.isButtonDisabled" :style="btnStyle">
    <router-link :to="button.to" v-if="button.to" :class="button.icon.class">
      <img :src="src" :alt="button.icon.alt" v-show="button.icon.src" :style="imgStyle">
      <span>{{ button.text }}</span>
    </router-link>
    <div v-else :class="button.icon.class">
      <img :src="src" :alt="button.icon.alt"  v-show="button.icon.src" :style="imgStyle">
      <span>{{ button.text }}</span>
    </div>
  </button>
</template>

<script>
const requireIcon = require.context('@/assets/icons', false, /\.png$/);
const icons = {};
import {ref,onMounted} from 'vue';

export default {
  props: {
    baseStyle:Object,
    button: {
      type: Object,
      default: () => ({})
    }
  },
  setup(props) {
    requireIcon.keys().forEach((filename) => {
      const iconName = filename.replace(/^\.\/(.*)\.\w+$/, '$1');
      icons[iconName] = requireIcon(filename);
    });
    const btnStyle = ref(null);
    const imgStyle = ref(null);
    onMounted(() => {
      if(props.baseStyle)
      {
        
        if (props.baseStyle.btn) {
          btnStyle.value = props.baseStyle.btn;
        }
        if (props.baseStyle.img) {
          imgStyle.value = props.baseStyle.img;
        }
      } 
        console.log(btnStyle.value,imgStyle.value)
    })
    
    return {
      imgStyle,
      btnStyle,
      icons,
      src: icons[props.button.icon.src]
    };
  }
};
</script>
<style scoped>
button {
  
  margin: 10px 0;
  padding: 10px;

  font-size: var(--font-size-btn);
  background-color: var(--bg-btn);
  
  border: var(--border-btn);
  transition: all 0.5s ease-in-out;
  border-radius:var(--border-radius-btn);
}
img
{
  width: 2em;
  height: 2em;
}
a
{
  color:var(--color-btn);
  width: 100%;
}
</style>

<!--style scoped>
*{
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
.btn:hover
{
  border-color: #3b39cb;
  background-color: #3634b9;
  transform: scale(1.015);
  color:#fff;
  width: 100%;
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

.btn {
  background-color: #3b39cb;
  color: #efefef;
  border: 5px solid #3634b9;
  transition: all 0.5s ease-in-out;
  width: 90%;
}



button[disabled] {
  background-color: #ccc; 
  color: #666; 
  border: 5px solid #999;
  cursor: not-allowed;
  transition: none;
}

button[disabled]:hover {
  border-color: #999;
  background-color: #ccc;
  transform: none;
  color: #666;
}
.footer-link {
  color: var(--color);
  border:none;
  margin-right: 20px;
  text-decoration: none;
  position: relative;
  transition: color 0.3s ease-in-out; 
  background-color: transparent;

}
.footer-link img
{
  height: 2em;
  width: 2em;
}
.footer-link::before {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0px; 
  width: 0;
  height: 2px; 
  background-color: var(--color); 
  transition: width 0.3s ease-in-out; 
}

.footer-link:hover {
  color: var(--color-dark); 
}

.footer-link:hover::before {
  width: 100%;
}
button > *
{
  display: flex;
  align-content: center;
  flex-wrap: nowrap;
  justify-content: center;
  align-items: center;
}
.user-btn *
{
  text-decoration: none;
  color:var(--color);
}
.user-btn {
  background: linear-gradient(to right, transparent 50%, #50c0bd 50%);
  background-size: 200% 100%;
  background-position: left;

  width: 100%;
  text-align: center;
  text-transform: uppercase;
  font-weight: 700;
  font-size: 1.2em;
  color: white;
  cursor: pointer;
  position: relative;
  
  border: none;
  transition: all 0.3s;
}

.user-btn::before {
  pointer-events: none;
  position: absolute;
  z-index: -1;
  content: '';
  width: 0;
  height: 0;
  border-style: solid;
  transition: width 0.3s, border-color 0.3s;
}
.user-btn:hover {
  background-position: right;
}
.user-btn:hover::before {
  width: 0;
  height: 0;
  border-width: 2em 0 2em 2em;
  border-color: transparent transparent transparent #50c0bd;
  right: -20px;
}
</style-->
