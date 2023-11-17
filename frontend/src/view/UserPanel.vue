<template>
  <div>
    <ProgressUser :style="isSmall ? progressStyle : null " />

    <UserNav lang="pl" nav="user" v-if="!isSmall"  :textShow="!isMedium"/>
    <NavListMin v-else />

    <PanelModul :style="isSmall? PanelStyle : '' "  />
  </div>
</template>

<script>
import PanelModul from "@/modules/panel/MainPanel.vue";
import NavListMin from "@/modules/nav/NavListMin.vue";
import UserNav from "@/modules/nav/UserNav.vue";
import ProgressUser from "@/modules/progressUser/ProgressUser.vue";
import { ref } from "vue";
export default {
  name: "UserPanel",
  components: {
    NavListMin,
    PanelModul,
    UserNav,
    ProgressUser,
  },
  setup() {
    const windowWidth = ref(window.innerWidth);
    const isSmall = ref(false);
    const isMedium = ref(false);
    const isStandard = ref(false);

    const setSize=(small,medium,standard)=>
    {
      isSmall.value = small;
      isMedium.value = medium;
      isStandard.value = standard;
    }
    const setScreenSize = () => {
      const width = window.innerWidth;
      windowWidth.value = width;

      if (width <= 700) {
        setSize(1,0,0);
      } else if (width <= 1250) {
        setSize(0,1,0);
      } else {
        setSize(0,0,1);
      }
    };

    window.addEventListener("resize", setScreenSize);

    setScreenSize();
    return {
      isSmall,
      isMedium,
      isStandard,
      progressStyle: {
        position:"fixed",
        top: "0",
        right: '0',
        minHeight:"10%",
        width:"100vw",
        display: "flex",
        borderRadius:"0"
      },
      PanelStyle:{
        minWidth: "95vw",
        top: "15vh",
        rigth: "5%",
        paddingBottom:"20vh"
      }
    };
  },
};
</script>