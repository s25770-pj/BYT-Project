<template>
  <div class="settings-menu" @mouseover="showMenu = true" @mouseleave="showMenu = false">
    <div class="menu-toggle">
      <i class="bi bi-gear"></i>
    </div>
    <div v-if="showMenu" class="menu">
      <ul>
        <li @click="toggleDarkMode">Zmiana motywu</li>
        <li @click="toggleSound">Dźwięk</li>
      </ul>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const showMenu = ref(false);

    const toggleDarkMode = () => {
      // Tutaj można dodać logikę zmiany motywu
    };

    const toggleSound = () => {
      // Tutaj można dodać logikę włączania/wyłączania dźwięku
    };

    return {
      showMenu,
      toggleDarkMode,
      toggleSound,
    };
  },
};
</script>

<style scoped>
.settings-menu {
  position: relative;
  display: inline-block;
}

.menu-toggle {
  display: flex;
  justify-content: flex-end;
  cursor: pointer;
}

.menu {
  position: absolute;
  top: 100%;
  right: 0;
  background: #fff;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  z-index: 10;
}

.menu ul {
  list-style: none;
  padding: 0;
}

.menu li {
  margin: 5px 0;
}
</style>
