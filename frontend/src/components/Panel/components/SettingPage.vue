<template>
  <div class="settings-menu" @mouseover="showMenu = true" @mouseleave="showMenu = false">
    <div class="menu-toggle" @click="$toggleDarkMode">
      <i class="bi bi-gear-fill"></i>
    </div>
    <div class="menu" v-if="showMenu">
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
    const darkModeEnabled = ref(false); // A reactive variable for dark mode

    const toggleMenu = () => {
      showMenu.value = !showMenu.value; // Toggle the menu visibility
    };

    const toggleDarkMode = () => {
      darkModeEnabled.value = !darkModeEnabled.value; // Toggle dark mode status
    };

    const toggleSound = () => {
      // Implement sound toggling logic here
    };

    return {
      showMenu,
      darkModeEnabled,
      toggleMenu,
      toggleDarkMode,
      toggleSound,
    };
  },
};
</script>

<style scoped>
.settings-menu {
  position: relative;
  z-index: 9999;
}

.menu-toggle {
  display: flex;
  justify-content: flex-end;
  cursor: pointer;
  position: absolute; 
  top: 10px;
  right: 10px; 
}

.menu {
  position: absolute;
  top: 40px;
  right: 0;
  background: #fff;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  z-index: 9999;
}

i {
  height: 1em;
  width: 1em;
  background-color: blue;
}

.menu ul {
  list-style: none;
  padding: 0;
}

.menu li {
  margin: 5px 0;
}
</style>
