<template>
  <div>
    <CustomButton v-show="buttons"
      v-for="(button, index) in buttons"
      :key="index"
      :button ="button"
      :baseStyle="baseStyle"
      :imgShow="imgShow"
      :textShow="textShow"
    /> 
  </div>
</template>

<script>
import CustomButton from '@/components/CustomButton.vue';
export default {
  name:'NavList',
    components:{
        CustomButton
    },
  props: {
    baseStyle:Object,
    buttons: {
        type: Array,
        required:true,
        default:()=>[]
    },
    imgShow:{
      type:Boolean,
      default: ()=>{true}
    },
    textShow:{
      type:Boolean,
      default: ()=>{true}
    }
  }
};
</script>