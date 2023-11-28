<template>
  <div>
    <h2>Ekwipunek</h2>
    <div class="inventory">
      <div class="slot" v-for="item in items" :key="item.id">
        {{ item.name }} ({{ item.type }})
      </div>
    </div>
  </div>
</template>

<script>
import {ref} from 'vue';
export default {

  setup() {
    const items = ref([]);
    return {
      items
    };
  }
};
</script>

<style scoped>
/* Dodaj odpowiednie style dla slotów i ekwipunku */
.inventory {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.slot {
  width: 80px;
  height: 80px;
  background-color: #ccc;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid #999;
  font-size: 14px;
}
</style>
