<template>
  <div>
    <h1>Matematyczny Komponent - Mnożenie</h1>
    <div>
      <input v-model="liczbaA" type="number" placeholder="Liczba A" />
      <span> * </span>
      <input v-model="liczbaB" type="number" placeholder="Liczba B" />
      <button @click="pomnóż">Mnóż</button>
    </div>
    <div>
      <p>Wynik: {{ wynik }}</p>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'Math_01',
  setup() {
    const liczbaA = ref(0);
    const liczbaB = ref(0);
    const wynik = ref(0);

    const pomnóż = () => {
      wynik.value = parseFloat(liczbaA.value) * parseFloat(liczbaB.value);
    };

    return {
      liczbaA,
      liczbaB,
      wynik,
      pomnóż,
    };
  },
};
</script>
