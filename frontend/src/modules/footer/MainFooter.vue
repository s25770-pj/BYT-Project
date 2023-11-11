<template>
  <footer class="footer">
    <p>&copy; {{ currentYear }} {{ pageTitle }}</p>
    <MainNav lang="pl" nav="footer" :baseStyle="baseStyle" />
  </footer>
</template>

<script>
import MainNav from "@/modules/nav/MainNav.vue";
export default {
  name: "MainFooter",
  components: {
    MainNav,
  },
  setup() {
    return {
      baseStyle: {
        btn: {
          normal: {
            "text-transform": "uppercase",
            "font-size": "1em",
            position: "relative",
            background: "transparent",
            border: "none",
            transition: "all .5s ease-in-out",
          },
        },
        img: {
          normal: {
            width: "2em",
            height: "2em",
          },
        },
      },
      currentYear: new Date().getFullYear(),
      pageTitle: process.env.VUE_APP_SITE_TITLE || "",
    };
  },
};
</script>

<style scoped>
.footer {
  font-size: 1.1em;
  color: var(--color);
  position: fixed;
  bottom: 1%;
  right: 0;
  background-color: transparent;
  border: none;
  min-height: 5vh;
  width: 50%;
  display: flex;
}
p {
  width: 50%;
}
</style>
