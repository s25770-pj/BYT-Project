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
<style scoped>
:root
{
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
.btn-custom {
  color:#efefef;
  border-color:#3634b9;
  margin: 10px 0;
  padding: 20px;
  width: 100%;
  background-color: #3b39cb;
  transition: background-color 0.3s ease-in-out, width 0.3s ease-in-out;
}
</style>
