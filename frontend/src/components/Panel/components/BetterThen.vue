<template>
  <div>
    <div class="element" :style="elementStyle">
      <div class="gradient"></div>
    </div>
    <button @click="rozlejKolor">Rozlej kolor</button>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const elementStyle = ref({
      backgroundColor: "transparent",
      width: "200px",
      height: "200px",
    });

    function rozlejKolor() {
      const gradientColor = "red"; // Kolor gradientu
      const gradientDuration = 1000; // Czas trwania animacji gradientu w milisekundach

      elementStyle.value.backgroundColor = gradientColor;
      elementStyle.value.width = "300px";
      elementStyle.value.height = "300px";

      const gradient = document.querySelector('.gradient');
      gradient.style.background = `radial-gradient(circle at center, ${gradientColor} 0%, transparent 100%)`;

      setTimeout(() => {
        gradient.style.transition = `background ${gradientDuration}ms ease-in-out`;
        gradient.style.background = `radial-gradient(circle at center, ${gradientColor} 100%, transparent 100%)`;
        elementStyle.value.backgroundColor = "transparent";
        elementStyle.value.width = "200px";
        elementStyle.value.height = "200px";
      }, 10); // Wprowadzenie minimalnego opóźnienia

      setTimeout(() => {
        gradient.style.transition = '';
        gradient.style.background = '';
      }, gradientDuration);
    }

    return {
      elementStyle,
      rozlejKolor,
    };
  },
};
</script>

<style>
.element {
  position: relative;
}

.gradient {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: transparent;
  transition: background 0s; /* Resetowanie transition */
}

button {
  margin-top: 10px;
}
</style>
