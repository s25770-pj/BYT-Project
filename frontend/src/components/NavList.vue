<template>
  <div>
    <CustomButton v-show="buttons"
      v-for="(button, index) in buttons"
      :key="index"
      :button ="button"
    /> 
  </div>
</template>

<script>
import CustomButton from './CustomButton.vue';
export default {
  name:'NavList',
    components:{
        CustomButton
    },
  props: {
    buttons: {
        type: Array,
        required:true,
        default:()=>[]
    }
  },
};
</script>