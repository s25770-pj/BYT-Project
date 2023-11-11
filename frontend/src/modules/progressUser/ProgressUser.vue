<template>
  <div class="static-bar" :style="style">
    <GenericLoading :isLoading="isLoading">
      <div class="static-item">
        <img src="@/assets/iconsUserStatistics/gold.png" alt="Gold" class="static-icon" />
        <div class="static-value">{{ gold }}</div>
      </div>
    </GenericLoading>
    <GenericLoading :isLoading="isLoading">
      <div class="static-item">
        <img src="@/assets/iconsUserStatistics/gem.png" alt="Gem" class="static-icon" />
        <div class="static-value">{{ gem }}</div>
      </div>
    </GenericLoading>
    <GenericLoading :isLoading="isLoading">
      <div class="static-item">
        <img src="@/assets/iconsUserStatistics/strick.png" alt="Stricks" class="static-icon" />
        <div class="static-value">{{ strick }}</div>
      </div>
    </GenericLoading>
    <div class="static-item d-flex justify-content-between">
      <MoreInfo :size="size"/>
      <SettingPage />
    </div>
  </div>
</template>
<script>
import { fetchDataFromEndpoint } from "@/function/fetchData.js";
import { convertNumber } from "@/function/convertNumber.js";
import { ref, onMounted } from "vue";
import GenericLoading from "@/modules/loader/GenericLoading.vue";
import SettingPage from "@/components/Panel/components/SettingPage.vue";

import MoreInfo from "./MoreInfo.vue";

export default {
  components: { GenericLoading, SettingPage, MoreInfo },
  props:{
    style:{
      type:Object
    },
    size:{
      type:Boolean
    }
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
        .catch((error) => {
          console.error("Błąd podczas pobierania danych:", error);
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
  min-width: 15vw;
}

.static-item {
  display: flex;
  align-items: center;
  margin-right: 10px;
  min-width: 10%;
  height: 100%;
  justify-content:center;
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
