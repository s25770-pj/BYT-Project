<template>
  <div>
    <div class="card" v-if="quests.length > 0" :class="['card', 'daily-quest-card', { 'hide-quest': currentQuest !== 0 }]">
        <div class="row">
          <div class="col-md-4 col-sm-4 card-image-container">
            <img :src="quests[currentQuest].image" class="card-image" alt="Quest Image">
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
  </div>
</template>

<script>
import {onMounted,ref} from 'vue';
const requireIcon = require.context('@/assets/icons', false, /\.png$/);
const icons = {};
requireIcon.keys().forEach((filename) => {
      const iconName = filename.replace(/^\.\/(.*)\.\w+$/, '$1');
      icons[iconName] = requireIcon(filename);
    });
export default {
  props:{
    delay:{
      type:String
    }
  },
  setup(){
    const currentQuest = ref(0);
    const quests=[
        {
          title: "Quest Title 1",
          description: "Quest Description 1",
          image: icons["bag"],
          progress: 30,
        },
        {
          title: "Quest Title 2",
          description: "Quest Description 2",
          image: icons["bag"],
          progress: 50,
        }
      ];
    
    onMounted(()=>{
    setInterval(() => {
      
      currentQuest.value = (currentQuest.value + 1) % quests.length;
      setTimeout(() => {
        currentQuest.value = (currentQuest.value + 1) % quests.length;
      }, 500);
    }, 5000); 
    })
    return {
        icons,
        quests,
      currentQuest
      }
  }
};
</script>
<style scoped>
.card
{
  width: 100%;
  height: 100%;
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
  transition: opacity 1s; /* Płynne przejście opacności trwające 0.5 sekundy */
  opacity: 1; /* Domyślna widoczność */
}

.hide-quest {
  opacity: 0; /* Ukryj zadanie przez ustawienie opacności na 0 */
}

</style>
