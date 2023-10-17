<template>
    <div class="h-100 pin-input">
    <h2>Wprowadź kod pezpieczeństwa</h2>
    <div class="pin-input-row">
      <input
        v-for="(char, index) in pin"
        :key="index"
        :value="char"
        type="text"
        :maxlength="1"
        @input="handleInput(index, $event.target.value)"
        class="pin-input-field"
        :class="{ 'filled': char !== '' }"
        ref="pinInputRefs"
      />
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';

export default {

  setup(props, { emit }) {
    const pin = ref(['', '', '', '']);
    const pinLength = 4;
    const pinInputRefs = ref([]);
    const isValid = ref(false);

    const handleInput = (index, char) => {
      if (char.length === 1) {
        pin.value[index] = char;
        if (index < pinLength - 1) {
          focusNextInput(index);
        }
      } else if (char === '') {
        pin.value[index] = '';
        if (index > 0) {
          focusPreviousInput(index);
        }
      }
      pin.value.every(el => el !== '')?checkPIN():'';
    };

    const focusNextInput = (index) => {
      if (index < pinLength - 1) {
        const nextInput = pinInputRefs.value[index + 1];
        if (nextInput) {
          nextInput.focus();
        }
      }
    };

    const focusPreviousInput = (index) => {
      if (index > 0) {
        const previousInput = pinInputRefs.value[index - 1];
        if (previousInput) {
          previousInput.focus();
        }
      }
    };

    const checkPIN = () => {
      const enteredPIN = pin.value.join('');
      if(enteredPIN == "1234")
      {
        emit('checkValid', true);
      }
    };

    onMounted(() => {
      if (pin.value[0] === '') {
        focusNextInput(0);
      }
    });

    return {
      isValid,
      pin,
      pinLength,
      handleInput,
      pinInputRefs,
    };
  },
};
</script>

<style scoped>
h2
{
  color:#358fc4;
}
.profil
{
  height: 100%;
}
.pin-input {
    display: flex;
    justify-content: space-around;
    align-items: center;
    height: 100%;
    flex-wrap: nowrap;
    flex-direction: column;
}

.pin-input-row {
  display: flex;
  align-items: center;
}

.pin-input-field {
  width: 3em;
  height: 3em;
  text-align: center;
  font-size: 18px;
  border: 1px solid #ccc;
  margin: 0 5px;
  border-radius: 4px;
}

.pin-input-field:focus {
  border-color: #007bff; /* Kolor obramowania podczas fokusa */
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5); /* Efekt cienia podczas fokusa */
}

.filled {
  background-color: #007bff;
  color: #d3d3d3;
  border-color: #007bff;
}
.pin-input {
    display: flex;
    justify-content: space-around;
    align-items: center;
    height: 100%;
    flex-wrap: nowrap;
    flex-direction: column;
}
</style>
