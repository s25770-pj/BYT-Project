<template>
  <div class="lds-ellipsis-container">
    <div class="lds-ellipsis">
      <div 
      class="dot" v-for="n in numDots" 
      :key="n" 
      :style="{ animationDelay: (n % colors.length) * 0.15 + 's', backgroundColor: colors[n % colors.length] }">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  setup() {
    const numDots = 4; 
    const colors = ['#8792da', '#83f2ee','#c342d0','#50c0bd'];

    return {
      numDots,
      colors,
    };
  },
};
</script>

<style>
.lds-ellipsis-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

.lds-ellipsis {
  width: 70%;
    height: 64px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    position: relative;
    transform: translateZ(0);
    align-content: center;
    flex-wrap: wrap;
}

.dot {
  position: relative;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  animation: lds-ellipsis-animation 2s infinite;
}

@keyframes lds-ellipsis-animation {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(0);
  }
}
</style>
