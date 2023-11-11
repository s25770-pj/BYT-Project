<template>
  <div v-if="size"><img src="@/assets/iconsUserStatistics/info.svg" alt="info" class="static-icon" /></div>
</template>

<script>
export default {
    props:{
        size:{
            type:Boolean
        }
    }
}
</script>

<style scoped>
.static-icon {
  width: 2em;
  height: 2em;
  margin-right: 5px;
}
</style>