<template>
  <div>
    <div v-if="isLoading">Trwa ładowanie danych...</div>
    <div v-else class="progressBar">
      <div v-for="(value, index) in progress" :key="index" :class="['progress-slot', { 'active': value == 1,'inactive': value == -1, 'first-slot': index === 0, 'last-slot': index === progress.length - 1 }]">
      </div>
    </div>
  </div>
</template>

<script>
import {ref} from 'vue';
import { fetchDataFromEndpoint } from '@/function/fetchData.js';

export default {
  setup() {
    const isLoading = ref(true);
    const progress = ref([]);

    fetchDataFromEndpoint("GET", "progress")
      .then(response => {
        progress.value = [...response.progress, ...Array(7 - response.progress.length).fill(0)];
      })
      .catch(error => {
        console.error('Błąd podczas pobierania danych:', error);
      })
      .finally(() => {
        isLoading.value = false;
      });

    return {
      progress,
      isLoading,
    };
  },
};
</script>


<style>
:root
{
  --progress-border-color:rgb(88, 88, 88);
  --active:rgb(68, 230, 68);
  --inactive:rgb(186, 245, 180);
  --default:d6d6d6;
}
.progressBar
{
  display: flex;
  align-content: center;
  justify-content: center;
}
.progress-slot {
  border:2px solid var(--progress-border-color);
  border-left:none;
  width: 30px;
  height: 30px;
  background-color: var(--default);
}
.first-slot {
  border-left:2px solid var(--progress-border-color);
  border-top-left-radius: 50%;
  border-bottom-left-radius: 50%;
}

.last-slot {
  border-top-right-radius: 50%;
  border-bottom-right-radius: 50%;
}
.active {
  background-color: var(--active);
}
.inactive
{
  background-color: var(--inactive);
}
</style>
