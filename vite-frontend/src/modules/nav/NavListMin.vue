<template>
  <MainNav
    class="nav"
    lang="pl"
    nav="user"
    :baseStyle="baseStyle"
    :classNav="classNav"
    :imgShow="imgShow"
    :textShow="textShow"
  />
</template>

<script>
import MainNav from "./MainNav.vue";
export default {
  components: {
    MainNav,
  },
  setup() {
    return {
      baseStyle: {
        btn: {
          normal: {
            border: "var(--border-btn)",
            textTransform: "uppercase",
            fontWeight: "700",
            fontSize: "1.2em",
            padding: "20px",
            margin: "10px",
            borderRadius: "var(--border-radius-btn)",
            transition: "all .5s ease-in-out",
            flex: "1",
          },
        },
        img: {
          normal: {
            width: "2em",
            height: "2em",
          },
        },
      },
      classNav: ["d-flex", "justify-content-space", "flex-row", "w-100"],
      imgShow: true,
      textShow: false,
    };
  },
};
</script>
<style scoped>
.nav {
  position: fixed;
  bottom: 0;
  left: 0;
  z-index: 5;
  width: 100%;
}
</style>
