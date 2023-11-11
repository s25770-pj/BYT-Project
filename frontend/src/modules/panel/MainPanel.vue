<template>
  <div class="contener glass-effect" :style="PanelStyle">
    <router-view></router-view>
  </div>
</template>
<script>

export default ({
  props:{
    PanelStyle:{
      type:Object
    }
  }
})
</script>


<style scoped>
.contener {
  position: absolute;
  right: 3%;
  top: 10%;
  min-width: 80vw;
  max-width: 80vw;
  min-height: 80vh;
}
.glass-effect {
  padding: 20px;
  border-radius: 10px;
  background: linear-gradient(
      rgba(255, 255, 255, 0.7),
      rgba(255, 255, 255, 0.7)
    ),
    linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2));
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: white;
}
.leout-3x3 {
  display: grid;
  gap: 10px 10px;
  min-height: 75vh;
  grid-template-rows: var(--grid-rows);
  grid-template-columns: var(--grid-cols);
  grid-template-areas: var(--grid-template-areas);
}
</style>
