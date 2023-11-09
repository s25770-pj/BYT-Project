<template>
  <div class="overflow d-flex h-100 flex-column align-items-center justify-content-center text-center">
    <BanerBox :style="style" :showMode=false />
    <MainNav
      lang="pl"
      nav="main"
      :baseStyle="baseStyle"
      class="box d-flex h-100 flex-column align-items-center justify-content-center text-center"
    />
  </div>
</template>

<script>
import MainNav from "@/modules/nav/MainNav.vue";
import BanerBox from "@/components/Panel/components/BanerBox.vue";

export default {
  name: "HomePage",
  components: {
    MainNav,
    BanerBox,
  },
  setup() {
    return {
      baseStyle: {
        btn: {
          normal: {
            margin: "10px 0",
            padding: "20px",
            width: "var(--btn-width)",
            border: "var(--border-btn)",
            borderRadius: "var(--border-radius-btn)",
          },
        },
        img: {
          normal: {
            position: "relative",
            left: "-2em",
            height: "3em",
          },
        },
      },
      style: {
        left: "-.5em",
        height: "10vh",
        width: "80%",
      },
    };
  },
};
</script>
<style scoped>
.overflow
{
  overflow: hidden;
}
.box {
  position: relative;
  top:10%;
}
</style>
