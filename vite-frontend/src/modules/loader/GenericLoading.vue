<template>
  <div>
    <div v-if="isLoading">
          <SmallLoader/>
    </div>
    <div v-else>
          <slot></slot>
    </div>
  </div>
</template>

<script>
import SmallLoader from "./SmallLoader.vue";

export default {
  components: {
    SmallLoader
  },
  props: {
    isLoading: Boolean
  }
};
</script>
