<template>
  <div class="static-bar" :style="style">
    <div class="static-item">
      <img
        src="@/assets/iconsUserStatistics/gold.png"
        alt="Gold"
        class="static-icon"
      />
      <GenericLoading :isLoading="isLoading" class="static-value gold">
        <div>{{gold}}</div>
      </GenericLoading>
    </div>

    <div class="static-item">
      <img
        src="@/assets/iconsUserStatistics/gem.png"
        alt="Gem"
        class="static-icon"
      />
      <GenericLoading :isLoading="isLoading" class="static-value gem">
        <div>{{gem}}</div>
      </GenericLoading>
    </div>

    <div class="static-item">
      <img
        src="@/assets/iconsUserStatistics/strick.png"
        alt="Strick"
        class="static-icon"
      />
      <GenericLoading :isLoading="isLoading" class="static-value strick">
        <div>{{strick}}</div>
      </GenericLoading>
    </div>

    <div
      :isLoading="isLoading"
      class="static-item d-flex justify-content-around"
    >
      <MoreInfo />
      <SettingPage />
    </div>
  </div>
</template>
<script>
import { fetchDataFromEndpoint } from "@/function/fetchData.js";
import { convertNumber } from "@/function/convertNumber.js";
import { ref, onMounted } from "vue";
import GenericLoading from "@/modules/loader/GenericLoading.vue";
import SettingPage from "./SettingPage.vue";
//import anime from 'animejs/lib/anime.js';

import MoreInfo from "./MoreInfo.vue";

/*const animateValue = (targetSelector, value) => {
  anime({
    targets: targetSelector,
    innerHTML: [0, value],
    duration: 1000,
    easing: "linear",
    round: 1
  });
};*/
export default {
  components: { GenericLoading, SettingPage, MoreInfo },
  props: {
    style: {
      type: Object,
    },
  },
  setup() {
    const isLoading = ref(true);
    const gold = ref(null);
    const gem = ref(0);
    const strick = ref(0);

    onMounted(() =>
      fetchDataFromEndpoint("GET", "balance")
        .then((response) => {
          gold.value = convertNumber(response.gold);
          gem.value = convertNumber(response.gem);
          strick.value = convertNumber(response.strick);
        })
        .then(() => {  
          /*animateValue(".gold", gold.value);
          animateValue(".gem", gem.value);
          animateValue(".strick", strick.value);*/
        })
        .catch((error) => {
          console.error("Błąd podczas pobierania danych:", error);
          isLoading.value = false;
        })
        .finally(() => {
          isLoading.value = false;
        })
    );

    return { gold, gem, strick, isLoading };
  },
};
</script>

<style scoped>
* {
  text-align: center;
}
.static-bar {
  position: absolute;
  z-index: 10;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.7);
  padding: 5px 10px;
  border-radius: 5px;
  right: 5%;
  top: 2%;
  height: 5vh;
  min-width: 30vw;
}

.static-item {
  display: flex;
  align-items: center;
  margin-right: 10px;
  width: 25%;
  height: 100%;
  justify-content: center;
}

.static-icon {
  width: 2em;
  height: 2em;
  margin-right: 5px;
}

.static-value {
  font-size: 18px;
  font-weight: bold;
  color: #007bff;
}
</style>
