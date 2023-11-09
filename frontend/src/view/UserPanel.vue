<template>
  <div>
    <ProgressUser :style="isMinSize ? progressStyle : '' " />
    <UserNav lang="pl" nav="user" v-if="!isMinSize" />
    <PanelModul :style="isMinSize ? PanelStyle : '' "/>
    <!--MainFooter/-->
  </div>
</template>

<script>
import PanelModul from "@/modules/panel/MainPanel.vue";

//import MainFooter from '@/components/Helpful/Footer/MainFooter.vue';
import UserNav from "@/modules/nav/UserNav.vue";
import ProgressUser from "@/components/Panel/components/ProgressUser.vue";
import { ref } from "vue";
export default {
  name: "UserPanel",
  components: {
    PanelModul,
    //MainFooter,
    UserNav,
    ProgressUser,
  },
  setup() {
    const isMinSize = ref(window.innerWidth <= 700);
    window.addEventListener(
      "resize",
      () => (isMinSize.value = window.innerWidth <= 700)
    );
    return {
      isMinSize,
      progressStyle: {
        position:"fixed",
        top: "0",
        left:"0",
        minHeight:"10%",
        width:"100vw",
        display: "flex",
        borderRadius:"0"
      },
      PanelStyle:{
        minWidth: "95vw",
        top: "15vh",
        rigth: "5%"
      }
    };
  },
};
</script>
