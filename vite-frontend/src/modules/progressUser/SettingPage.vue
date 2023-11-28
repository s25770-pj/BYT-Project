<template>
  <img src="@/assets/iconsUserStatistics/settings.svg" alt="info" class="static-icon"  @click="toggleModule" />
  
  <teleport to="body">
      <div class="modal-overlay" v-if="showModule" @click="toggleModule">
        <div class="modal-container">
          <div title="Menu"  size="xl">
            <div class="modal-dialog modal-fullscreen-sm-down">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title">Ustawienia:</h5>
                </div>
                <div class="modal-body">
                  <div class="module-menu">
                    <MainNav lang="pl" nav="settings" :baseStyle="baseStyle" :classNav=classNav />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </teleport>
</template>

<script>
import { ref } from 'vue';
import MainNav from '@/modules/nav/MainNav.vue';
export default {
  components:{
    MainNav
  },
  setup() {
    const showModule = ref(false);

    const toggleModule = () => {
      showModule.value = !showModule.value;
    };

    return {
      showModule,
      toggleModule,
        baseStyle:{
          btn:{
            normal:{
              width: "var(--btn-width)",
              border: "var(--border-btn)",
              textTransform: 'uppercase',
              fontWeight: '700',
              fontSize: '1.2em',
              padding: '20px',
              margin: '10px',
              borderRadius:'var(--border-radius-btn)',
              transition: 'all .5s ease-in-out',
            }
          },
          img:{
            normal:{
              width: '2em',
              height: '2em'
            }
          }
        },
        classNav:["d-flex", "justify-content-center", "flex-wrap"]
    };
  },
};
</script>

<style scoped>

img{
  height: 2em;
}
.static-icon {
  width: 2em;
  height: 2em;
  margin-right: 5px;
}
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
}

.modal-container {
  max-width: 90vw;
}

.module-menu button {
  margin-bottom: 10px;
}
.modal-dialog
{
  padding: 5%;
  min-width: 50vw;
  min-height: 20vh;
  background-color: var(--primary-color-light);
  border-radius: 15px;
}
</style>
