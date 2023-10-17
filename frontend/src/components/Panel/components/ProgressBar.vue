<template>
  
    <GenericLoadingVue :isLoading="isLoading">

      <div class="progress">
        <h2>{{ title }}</h2>
          <div class="progressBar">
            <div 
              v-for="(value, index) in progress"
              :key="index"
              :class="['progress-slot', { 'active': value === 1, 'inactive': value === -1, 'first-slot': index === 0, 'last-slot': index === progress.length - 1 }]">
            </div>
          </div>
          <div class="button-container" v-if="!isLoading">
            <CustomButton :button="button"/>
            </div>
      </div>
    </GenericLoadingVue>
</template>

<script>
import { ref} from 'vue';
import { fetchDataFromEndpoint } from '@/function/fetchData.js';
import CustomButton from '@/components/CustomButton.vue';
import GenericLoadingVue from '@/components/GenericLoading.vue';
export default {
  components: {
    CustomButton,GenericLoadingVue
  },
  setup() {
    const isLoading = ref(true);
    const progress = ref([]);
    const button = ref({});
    const title = ref("");

    fetchDataFromEndpoint("GET", "progress")
      .then(response => {
        progress.value = [...response.progress, ...Array(7 - response.progress.length).fill(0)];
        button.value = response.button;
        title.value = response.title;
        isLoading.value = false;
      })
      .catch(error => {
        console.error('Błąd podczas pobierania danych:', error);
        isLoading.value = false;
      });

    

    return {
      progress,
      isLoading,
      button,
      title
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
  --default:rgb(214, 214, 214);
}
</style>
<style scoped>
.loader {
  text-align: center;
  padding: 20px;
  font-size: 1.2em;
}
h2
{
  color:#333;
  font-size: 1.5em;
  text-align: center;
}
.progress
{
  display: flex;
    justify-content: center;
    height: 100%;
    flex-wrap: wrap;
    align-items: center;
}
.progressBar
{
  display: flex;
  align-content: flex-start;
  justify-content: center;
  flex-wrap: wrap;
  align-items: stretch;
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
