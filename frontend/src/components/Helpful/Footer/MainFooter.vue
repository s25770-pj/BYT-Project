<template>
  <footer class="footer">
    <div class="container">
      <div class="row">
        <div class="col-md-6 text-md-end">
          <p>&copy; {{ currentYear }} {{ pageTitle }}</p>
          <MainNav lang="pl" nav="footer" :baseStyle="baseStyle" />
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
import MainNav from "@/components/CreateNav/MainNav.vue";
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
}
p {
  width: 50%;
}
.row div {
  height: 100%;
  width: 80%;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
