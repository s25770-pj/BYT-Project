<template>
  <button
    :class="button.class"
    :disabled="button.isButtonDisabled"
    :style="btnStyle"
    @mouseover="isHoveredBtn = true"
    @mouseleave="isHoveredBtn = false"
  >
    <router-link :to="button.to" v-if="button.to" :class="button.icon.class">
      <img
        :src="src"
        :alt="button.icon.alt"
        v-if="button.icon.src && imgShow"
        :style="imgStyle"
      />
      <span v-if="textShow">{{ button.text }}</span>
    </router-link>
    <div v-else :class="button.icon.class">
      <img 
        :src="src"
        :alt="button.icon.alt"
        v-if="button.icon.src && imgShow"
        :style="imgStyle"
      />
      <span v-if="textShow">{{ button.text }}</span>
    </div>
  </button>
</template>

<script>
import { ref, computed } from "vue";
const requireIcon = require.context("@/assets/icons", false, /\.png$/);
const icons = {};

requireIcon.keys().forEach((filename) => {
  const iconName = filename.replace(/^\.\/(.*)\.\w+$/, "$1");
  icons[iconName] = requireIcon(filename);
});

export default {
  props: {
    baseStyle: Object,
    button: {
      type: Object,
      default: () => ({}),
    },
    imgShow:{
      type:Boolean,
      default: true
    },
    textShow:{
      type:Boolean,
      default: true
    }
  },
  setup(props) {
    const isHoveredBtn = ref(false);
    const imgStyle = computed(() => {
      return props.baseStyle.img.normal; 
    });
    const btnStyle = computed(() => {
      const style = { ...props.baseStyle.btn.normal };
      if (isHoveredBtn.value) {
        for (const key in props.baseStyle.btn.hover) {
          style[key] = props.baseStyle.btn.hover[key];
        }
      }
      
      return style;
    });

    const src = computed(() => {
      return icons[props.button.icon.src];
    });

    return {
      isHoveredBtn,
      imgStyle,
      btnStyle,
      src,
    };
  },
};
</script>

<style scoped>
button:hover
{
  background-position: left;
}
.userNav:hover a {
  color: var(--color-btn-mNav);
}
.userNav::before {
  opacity: 0;
  position: absolute;
  z-index: 2;
  content: "";
  width: 0;
  height: 0;
  background-color: transparent;
  border: solid;
  border-color: transparent transparent transparent var(--bg-btn-mNav);
  transition: all 1s ease;
  right: -15px;
  border-width: 1em 0 1em 1em;
}
.userNav:hover::before {
  animation: show 0.9s;
  opacity: 1;
}
@keyframes show {
  0% {
    opacity: 0;
    right: 150px;
  }
  100% {
    opacity: 1;
    right: -15px;
  }
}
</style>
