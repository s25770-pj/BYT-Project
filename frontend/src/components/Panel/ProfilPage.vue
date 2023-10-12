<template>
<div class="profil">
  <div v-if="isValid">
  </div>
  <EnterPIN v-else @checkValid="handleIsValidChanged"/>
</div>
</template>

<script>
import EnterPIN from '@/components/Panel/components/EnterPIN.vue';
import {ref} from 'vue';
export default {
  components:
  {
    EnterPIN
  },
  setup()
  {
    const isValid = ref(false);
    const handleIsValidChanged = (newValue) => {
      isValid.value = newValue;
    };
    return {handleIsValidChanged,isValid}
  }
  
};
</script>

<style scoped>
h2
{
  color:#358fc4;
}
.profil
{
  height: 100%;
}
</style>
