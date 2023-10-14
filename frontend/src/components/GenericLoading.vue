<template>
  <div>
    <div v-if="isLoading">
      <transition name="slide-fade">
        <div key="loader">
          <SmallLoader />
        </div>
      </transition>
    </div>
    <div v-else>
      <transition name="slide-fade">
        <div key="content">
          <slot></slot>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import SmallLoader from "@/components/SmallLoader.vue";

export default {
  components: {
    SmallLoader
  },
  props: {
    isLoading: Boolean
  },
  setup(props) {
    console.log(props.isLoading);
  }
};
</script>

<style scoped>
div {
  height: 100%;
  width: 100%;
}

.slide-fade-enter-active, .slide-fade-leave-active {
  transition: opacity 0.5s;
  background: red;
}
.slide-fade-enter, .slide-fade-leave-to {
  background: purple;
  opacity: 0;
}
</style>
