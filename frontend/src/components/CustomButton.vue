<template>
  <button :class="button.class" :disabled="button.isButtonDisabled">
    <router-link :to="button.to" v-if="button.to">
      <img :src="src" :alt="button.icon.alt" v-show="button.icon.src" :class="button.icon.class">
      <span>{{ button.text }}</span>
    </router-link>
    <div v-else>
      <img :src="src" :alt="button.icon.alt" :class="button.icon.class" v-show="button.icon.src">
      <span>{{ button.text }}</span>
    </div>
  </button>
</template>

<script>
const requireIcon = require.context('@/assets/icons', false, /\.png$/);
const icons = {};

export default {
  props: {
    button: {
      type: Object,
      default: () => ({
        text: "Przykładowy przycisk",
        icon: {
          src: "domyslny-obrazek.png",
          alt: "Opis domyślnego obrazka",
          class: "domyslna-klasa-obrazka"
        },
        to: "/domyslna-sciezka",
        class: "domyslna-klasa-przycisku"
      })
    }
  },
  setup(props) {
    requireIcon.keys().forEach((filename) => {
      const iconName = filename.replace(/^\.\/(.*)\.\w+$/, '$1');
      icons[iconName] = requireIcon(filename);
    });

    return {
      icons,
      src: icons[props.button.icon.src]
    };
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
  width: 100%;
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

.btn {
  background-color: #3b39cb;
  color: #efefef;
  border: 5px solid #3634b9;
  transition: all 0.5s ease-in-out;
  width: 90%;
}

.btn:hover {
  border-color: #3b39cb;
  background-color: #3634b9;
  transform: scale(1.015);
  color: #fff;
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
  background-position: right; /* Po najechaniu tło przesuwa się w lewo */
}
.user-btn:hover::before {
  width: 0;
  height: 0;
  border-width: 2em 0 2em 2em;
  border-color: transparent transparent transparent #50c0bd;
  right: -20px;
}
</style>
