<template>
  <div>
    <component :is="selectedComponent" v-if="selectedComponent"></component>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const selectedComponent = ref(null);

    const loadRandomModule = async () => {
      const modules = ref(['Math_01', 'Math_02']); 
      const randomModule = modules.value[Math.floor(Math.random() * modules.value.length)];
      try {
        const module = await import(`@/components/modul/math/${randomModule}.vue`);
        selectedComponent.value = module.default;
      } catch (error) {
        console.error('Błąd ładowania modułu:', error);
      }
    };
    loadRandomModule();
    return {
      selectedComponent,
      loadRandomModule,
    };
  },
};
</script>
