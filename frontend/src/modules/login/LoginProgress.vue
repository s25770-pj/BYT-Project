 
<template>
  <div class="login-progress modal fade" :class="{ 'show': loading }" tabindex="-1" role="dialog">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-body">
          {{ message }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {watch} from 'vue';
export default {
  props: {
    loading: Boolean, 
    message: String,
  },
  setup(props,{ emit }){
    watch(props.loading,emit('login-success', 'Zalogowano pomyślnie!'))
  }
};
</script>
