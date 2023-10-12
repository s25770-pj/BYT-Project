<template>
  <div class="static-bar">
    <div class="static-item">
      <img src="@/assets/icons/bag.png" alt="Gold" class="static-icon" />
      <div class="static-value">{{gold}}</div>
    </div>
    <div class="static-item">
      <img src="@/assets/icons/bag.png" alt="Gem" class="static-icon" />
      <div class="static-value">{{gem}}</div>
    </div>
    <div class="static-item">
      <img src="@/assets/icons/bag.png" alt="Stricks" class="static-icon" />
      <div class="static-value">{{strick}}</div>
    </div>
  </div>
</template>
<script>
import {fetchDataFromEndpoint} from '@/function/fetchData.js';
import {convertNumber} from '@/function/convertNumber.js';
import {ref} from 'vue';

export default {
  setup() {
    const gold = ref(null);
    const gem = ref(0);
    const strick = ref(0);

    fetchDataFromEndpoint("GET", "balance")
      .then(response => {
        gold.value = convertNumber(response.gold);
        gem.value = convertNumber(response.gem);
        strick.value = convertNumber(response.strick);
      })
      .catch(error => {
        console.error('Błąd podczas pobierania danych:', error);
      })
    return {gold,gem,strick}
  },
}
</script>

<style scoped>
.static-bar {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.7);
  padding: 5px 10px;
  border-radius: 5px;
  position: fixed;
  right: 5%;
  top:2%;
}

.static-item {
  display: flex;
  align-items: center;
  margin-right: 10px;
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
