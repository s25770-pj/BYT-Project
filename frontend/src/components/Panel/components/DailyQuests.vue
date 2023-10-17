<template>
  <div class="questBox">
    <GenericLoading :isLoading="isLoading">
    
        <h2>{{ title }}</h2>
        <div class="card" v-if="quests.length > 0" :class="['card', 'daily-quest-card']">
          <div class="row">
            <div class="col-md-4 col-sm-4 card-image-container">
              <img :src="icons[quests[currentQuest].image]" class="card-image" alt="Quest Image">
            </div>
            <div class="col-md-8 col-sm-8">
              <div class="card-body">
                <h5 class="card-title">{{ quests[currentQuest].title }}</h5>
                <p class="card-text">{{ quests[currentQuest].description }}</p>
                <div class="progress">
                  <div class="progress-bar" role="progressbar" :style="{ width: quests[currentQuest].progress + '%' }">
                    {{ quests[currentQuest].progress }}%
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

    </GenericLoading>
  </div>
</template>

<script>
import { ref,onMounted } from 'vue';
import { fetchDataFromEndpoint } from '@/function/fetchData.js';
import GenericLoading from '@/components/GenericLoading.vue';

const requireIcon = require.context('@/assets/icons', false, /\.png$/);
const icons = {};
requireIcon.keys().forEach((filename) => {
  const iconName = filename.replace(/^\.\/(.*)\.\w+$/, '$1');
  icons[iconName] = requireIcon(filename);
});

export default {
  components: {
    GenericLoading
  },
  props: {
    delay: {
      type: String
    }
  },
  setup(props) {
    const currentQuest = ref(0);
    const quests = ref([]);
    const title = ref("");
    const isLoading = ref(true);

    onMounted(()=>fetchDataFromEndpoint("GET", "quests")
      .then(response => {
        quests.value = response.quests;
        title.value = response.title;
        setInterval(() => {
          currentQuest.value = (currentQuest.value + 1) % quests.value.length;
        }, props.delay);
      })
      .catch(error => {
        console.error('Błąd podczas pobierania danych:', error);
      })
      .finally(() => {
        isLoading.value = false;
      })
    );
    return {
      icons,
      quests,
      title,
      currentQuest,
      isLoading
    }
  }
};
</script>

<style scoped>

.questBox
{
  height: 100%;
}
.progressUser
{
  display: flex;
  align-content: space-between;
  justify-content: center;
}
.progressUser h2
{
  color:#333;
  font-size: 1.5em;
  text-align: center;
}
.card
{
  width: 100%;
  max-height: 100%;
  min-height: 15%;
  font-size: 1em;
  min-height: 25%;
}
.card-body
{
  width: 100%;
}
.card-image-container {
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 30%;
}
img
{
  width: 100%;
}
.card-image {
  max-width: 100%;
  height: auto;
}
.daily-quest-card {

  opacity: 1; 
}
</style>
